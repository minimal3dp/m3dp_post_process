"""
Tests for BrickLayers optimization module.
"""

import pytest
from m3dp_post_process.bricklayers import BrickLayersConfig, BrickLayersOptimizer
from m3dp_post_process.gcode_processor import GCodeParser


@pytest.fixture
def sample_gcode():
    """Sample G-code with perimeter blocks for testing."""
    return """
;LAYER:0
G1 Z0.2
;TYPE:External perimeter
G1 X10 Y10 E0.5
;TYPE:Perimeter
G1 X20 Y20 E1.0
G1 X30 Y30 E1.5
G1 X40 Y40 F3000
;TYPE:Perimeter
G1 X50 Y50 E2.0
G1 X60 Y60 E2.5
G1 X70 Y70 F3000
;LAYER:1
G1 Z0.4
;TYPE:Perimeter
G1 X10 Y10 E3.0
G1 X20 Y20 E3.5
G1 X30 Y30 F3000
"""


def test_bricklayers_config_defaults():
    """Test BrickLayersConfig default values."""
    config = BrickLayersConfig()
    assert config.layer_height == 0.2
    assert config.extrusion_multiplier == 1.0


def test_bricklayers_config_custom():
    """Test BrickLayersConfig with custom values."""
    config = BrickLayersConfig(layer_height=0.3, extrusion_multiplier=1.2)
    assert config.layer_height == 0.3
    assert config.extrusion_multiplier == 1.2


def test_bricklayers_optimizer_initialization(sample_gcode):
    """Test BrickLayersOptimizer initialization."""
    parser = GCodeParser(content=sample_gcode)
    parser.parse()
    segments = parser.segments
    
    config = BrickLayersConfig()
    optimizer = BrickLayersOptimizer(segments, config)
    
    assert optimizer.config.layer_height == 0.2
    assert optimizer.z_shift == 0.1  # 0.2 * 0.5


def test_bricklayers_optimize(sample_gcode):
    """Test BrickLayersOptimizer.optimize() returns OptimizationResult."""
    parser = GCodeParser(content=sample_gcode)
    parser.parse()
    segments = parser.segments
    
    optimizer = BrickLayersOptimizer(segments)
    result = optimizer.optimize()
    
    assert result.optimization_type == "BrickLayers (Strength)"
    assert "total_layers" in result.metadata
    assert "shifted_blocks" in result.metadata
    assert "z_shift_mm" in result.metadata
    assert result.metadata["z_shift_mm"] == 0.1


def test_bricklayers_shifts_odd_blocks(sample_gcode):
    """Test that BrickLayers shifts odd-numbered perimeter blocks."""
    parser = GCodeParser(content=sample_gcode)
    parser.parse()
    segments = parser.segments
    
    optimizer = BrickLayersOptimizer(segments)
    result = optimizer.optimize()
    
    # Convert result segments back to G-code to check for shift comments
    gcode_lines = [seg.original_text for seg in result.segments if seg.original_text]
    
    # Should have at least one shifted block
    shifted_lines = [line for line in gcode_lines if "; Shifted Z for block #" in line]
    assert len(shifted_lines) > 0


def test_bricklayers_count_layers(sample_gcode):
    """Test layer counting."""
    parser = GCodeParser(content=sample_gcode)
    parser.parse()
    segments = parser.segments
    
    optimizer = BrickLayersOptimizer(segments)
    lines = optimizer._segments_to_gcode()
    
    layer_count = optimizer._count_layers(lines)
    assert layer_count == 2  # Sample has 2 layers


def test_bricklayers_with_no_perimeters():
    """Test BrickLayers with G-code that has no perimeters."""
    gcode = """
G1 Z0.2
G1 X10 Y10 E0.5
G1 Z0.4
G1 X20 Y20 E1.0
"""
    parser = GCodeParser(content=gcode)
    parser.parse()
    segments = parser.segments
    
    optimizer = BrickLayersOptimizer(segments)
    result = optimizer.optimize()
    
    # Should still return a valid result
    assert result.optimization_type == "BrickLayers (Strength)"
    assert result.metadata["shifted_blocks"] == 0
