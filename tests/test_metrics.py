"""
Tests for print time and material usage calculation.
"""
import pytest
from m3dp_post_process.gcode_processor import (
    GCodeParser,
    Optimizer,
    Segment,
    SegmentType,
    Point,
)


@pytest.fixture
def sample_segments_with_time():
    """Create sample segments with speed for time calculation."""
    return [
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 0),
            type=SegmentType.TRAVEL,
            speed=3000,  # 3000 mm/min = 50 mm/s
            line_number=1,
            original_text="G0 X10 F3000"
        ),
        Segment(
            start=Point(10, 0, 0, 0),
            end=Point(10, 10, 0, 5),
            type=SegmentType.EXTRUSION,
            speed=1200,  # 1200 mm/min = 20 mm/s
            line_number=2,
            original_text="G1 X10 Y10 E5 F1200"
        ),
        Segment(
            start=Point(10, 10, 0, 5),
            end=Point(20, 10, 0, 10),
            type=SegmentType.EXTRUSION,
            speed=1200,
            line_number=3,
            original_text="G1 X20 Y10 E10"
        ),
    ]


@pytest.fixture
def sample_gcode_with_extrusion():
    """Sample G-code with extrusion for material calculation."""
    return """
G90 ; Absolute positioning
M83 ; Relative extrusion
G1 X10 Y10 E5 F3000
G1 X20 Y20 E10
G1 X30 Y30 E8
G0 X40 Y40 ; Travel (no extrusion)
G1 X50 Y50 E7
"""


def test_calculate_print_time():
    """Test print time calculation."""
    segments = [
        # 10mm travel at 3000 mm/min (50 mm/s) = 0.2 seconds
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 0),
            type=SegmentType.TRAVEL,
            speed=3000,
            line_number=1,
            original_text="G0 X10 F3000"
        ),
        # 10mm extrusion at 1200 mm/min (20 mm/s) = 0.5 seconds
        Segment(
            start=Point(10, 0, 0, 0),
            end=Point(10, 10, 0, 5),
            type=SegmentType.EXTRUSION,
            speed=1200,
            line_number=2,
            original_text="G1 Y10 E5 F1200"
        ),
    ]
    
    optimizer = Optimizer(segments)
    print_time = optimizer._calculate_print_time(segments)
    
    # Expected: 0.2 + 0.5 = 0.7 seconds
    assert abs(print_time - 0.7) < 0.01


def test_calculate_material_usage():
    """Test material usage calculation."""
    segments = [
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 5),
            type=SegmentType.EXTRUSION,
            speed=1200,
            line_number=1,
            original_text="G1 X10 E5"
        ),
        Segment(
            start=Point(10, 0, 0, 5),
            end=Point(20, 0, 0, 12),
            type=SegmentType.EXTRUSION,
            speed=1200,
            line_number=2,
            original_text="G1 X20 E12"
        ),
        # Travel move - should not count
        Segment(
            start=Point(20, 0, 0, 12),
            end=Point(30, 0, 0, 12),
            type=SegmentType.TRAVEL,
            speed=3000,
            line_number=3,
            original_text="G0 X30"
        ),
    ]
    
    optimizer = Optimizer(segments)
    material_mm, material_grams = optimizer._calculate_material_usage(segments)
    
    # Expected: 5mm + 7mm = 12mm of filament
    assert abs(material_mm - 12.0) < 0.01
    
    # Expected weight for 1.75mm PLA:
    # Volume = π * (0.875)² * 12 = ~28.95 mm³ = 0.02895 cm³
    # Weight = 0.02895 * 1.24 = ~0.036 g
    assert material_grams > 0
    assert material_grams < 1  # Should be less than 1g for 12mm


def test_calculate_material_usage_custom_diameter():
    """Test material usage with custom filament diameter."""
    segments = [
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 100),
            type=SegmentType.EXTRUSION,
            speed=1200,
            line_number=1,
            original_text="G1 X10 E100"
        ),
    ]
    
    optimizer = Optimizer(segments)
    
    # Test with 1.75mm (default)
    _, weight_175 = optimizer._calculate_material_usage(segments, filament_diameter=1.75)
    
    # Test with 2.85mm
    _, weight_285 = optimizer._calculate_material_usage(segments, filament_diameter=2.85)
    
    # 2.85mm should use more material (larger cross-section)
    assert weight_285 > weight_175


def test_greedy_optimizer_includes_metrics(sample_segments_with_time):
    """Test that greedy optimizer returns print time and material metrics."""
    optimizer = Optimizer(sample_segments_with_time)
    result = optimizer.optimize_travel_greedy()
    
    # Check that metrics are included
    assert result.print_time_seconds is not None
    assert result.material_used_mm is not None
    assert result.material_used_grams is not None
    
    # Verify metrics are reasonable
    assert result.print_time_seconds > 0
    assert result.material_used_mm >= 0
    assert result.material_used_grams >= 0


def test_parser_to_optimizer_metrics_flow(sample_gcode_with_extrusion):
    """Test full flow from parsing to optimization with metrics."""
    # Parse G-code
    parser = GCodeParser(content=sample_gcode_with_extrusion)
    parser.parse()
    
    # Optimize
    optimizer = Optimizer(parser.segments)
    result = optimizer.optimize_travel_greedy()
    
    # Verify metrics exist
    assert result.print_time_seconds is not None
    assert result.material_used_mm is not None
    assert result.material_used_grams is not None
    
    # Verify material matches sum of E values (5+10+8+7 = 30mm)
    assert abs(result.material_used_mm - 30.0) < 0.1


def test_zero_speed_handling():
    """Test that zero speed doesn't cause division by zero."""
    segments = [
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 0),
            type=SegmentType.TRAVEL,
            speed=0,  # Invalid but should handle gracefully
            line_number=1,
            original_text="G0 X10"
        ),
    ]
    
    optimizer = Optimizer(segments)
    print_time = optimizer._calculate_print_time(segments)
    
    # Should not crash, time should be 0 or minimal
    assert print_time >= 0


def test_no_extrusion_material():
    """Test material calculation with no extrusion moves."""
    segments = [
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 0),
            type=SegmentType.TRAVEL,
            speed=3000,
            line_number=1,
            original_text="G0 X10"
        ),
    ]
    
    optimizer = Optimizer(segments)
    material_mm, material_grams = optimizer._calculate_material_usage(segments)
    
    # No extrusion = 0 material
    assert material_mm == 0.0
    assert material_grams == 0.0


def test_negative_extrusion_ignored():
    """Test that retractions (negative E) don't count as material usage."""
    segments = [
        Segment(
            start=Point(0, 0, 0, 10),
            end=Point(0, 0, 0, 5),  # Retraction: E goes from 10 to 5
            type=SegmentType.RETRACT,
            speed=1200,
            line_number=1,
            original_text="G1 E5"
        ),
    ]
    
    optimizer = Optimizer(segments)
    material_mm, material_grams = optimizer._calculate_material_usage(segments)
    
    # Retractions should not count
    assert material_mm == 0.0
    assert material_grams == 0.0
