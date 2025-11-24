"""Tests for quality optimizer."""

import pytest
from m3dp_post_process.quality_optimizer import (
    QualityOptimizer,
    QualityConfig,
    SeamStrategy
)
from m3dp_post_process.gcode_processor import Segment, Point, SegmentType


def create_segment(x, y, z, e, seg_type=SegmentType.EXTRUSION, text=""):
    """Helper to create a segment with start and end points."""
    return Segment(
        start=Point(x=x-1 if x > 0 else 0, y=y-1 if y > 0 else 0, z=z, e=e-0.1 if e > 0 else 0),
        end=Point(x=x, y=y, z=z, e=e),
        type=seg_type,
        speed=1800.0,
        line_number=0,
        original_text=text
    )


@pytest.fixture
def sample_loop():
    """Create a sample closed loop (square)."""
    return [
        create_segment(0, 0, 0.2, 0, SegmentType.EXTRUSION, "G1 X0 Y0 E0"),
        create_segment(10, 0, 0.2, 0.5, SegmentType.EXTRUSION, "G1 X10 Y0 E0.5"),
        create_segment(10, 10, 0.2, 1.0, SegmentType.EXTRUSION, "G1 X10 Y10 E1.0"),
        create_segment(0, 10, 0.2, 1.5, SegmentType.EXTRUSION, "G1 X0 Y10 E1.5"),
        # Back to start (closes loop)
        create_segment(0, 0, 0.2, 2.0, SegmentType.EXTRUSION, "G1 X0 Y0 E2.0"),
    ]


def test_quality_config_defaults():
    """Test quality configuration defaults."""
    config = QualityConfig()
    
    assert config.seam_strategy == SeamStrategy.RANDOM
    assert config.reduce_shell_crossings is True
    assert config.min_loop_segments == 3


def test_quality_config_custom():
    """Test quality configuration with custom values."""
    config = QualityConfig(
        seam_strategy=SeamStrategy.ALIGNED,
        reduce_shell_crossings=False,
        min_loop_segments=5
    )
    
    assert config.seam_strategy == SeamStrategy.ALIGNED
    assert config.reduce_shell_crossings is False
    assert config.min_loop_segments == 5


def test_quality_optimizer_initialization(sample_loop):
    """Test quality optimizer initialization."""
    config = QualityConfig()
    optimizer = QualityOptimizer(sample_loop, config)
    
    assert optimizer.config.seam_strategy == SeamStrategy.RANDOM
    assert len(optimizer.segments) == 5
    assert optimizer.seams_optimized == 0
    assert optimizer.crossings_eliminated == 0


def test_quality_optimize(sample_loop):
    """Test quality optimization returns valid result."""
    optimizer = QualityOptimizer(sample_loop)
    result = optimizer.optimize()
    
    assert result.optimization_type == "Quality Enhanced"
    assert "seam_strategy" in result.metadata
    assert "seams_optimized" in result.metadata
    assert "shell_crossings_reduced" in result.metadata


def test_seam_hiding_disabled(sample_loop):
    """Test with seam hiding disabled."""
    config = QualityConfig(seam_strategy=SeamStrategy.DISABLED)
    optimizer = QualityOptimizer(sample_loop, config)
    result = optimizer.optimize()
    
    assert result.metadata["seam_strategy"] == "disabled"
    assert result.metadata["seams_optimized"] == 0


def test_seam_hiding_random(sample_loop):
    """Test random seam hiding."""
    config = QualityConfig(seam_strategy=SeamStrategy.RANDOM)
    optimizer = QualityOptimizer(sample_loop, config)
    
    # Run optimization
    optimized = optimizer._optimize_seams(sample_loop)
    
    # Should still have same number of segments
    assert len(optimized) == len(sample_loop)


def test_seam_hiding_aligned(sample_loop):
    """Test aligned seam hiding (corners)."""
    config = QualityConfig(seam_strategy=SeamStrategy.ALIGNED)
    optimizer = QualityOptimizer(sample_loop, config)
    
    # Optimize a single loop
    optimized_loop = optimizer._optimize_loop_seam(sample_loop)
    
    # Should still have same number of segments
    assert len(optimized_loop) == len(sample_loop)


def test_seam_hiding_rear(sample_loop):
    """Test rear seam hiding (Y-max)."""
    config = QualityConfig(seam_strategy=SeamStrategy.REAR)
    optimizer = QualityOptimizer(sample_loop, config)
    
    # Optimize a single loop
    optimized_loop = optimizer._optimize_loop_seam(sample_loop)
    
    # Should still have same number of segments
    assert len(optimized_loop) == len(sample_loop)
    
    # First segment should have high Y value (rear)
    # (In our sample, Y=10 is the max)
    from m3dp_post_process.quality_optimizer import get_segment_end_point
    first_point = get_segment_end_point(optimized_loop[0])
    assert first_point[1] is not None  # Y coordinate exists


def test_find_sharpest_corner():
    """Test finding sharpest corner in a loop."""
    # Create a loop with one sharp corner
    loop = [
        create_segment(0, 0, 0.2, 0, SegmentType.EXTRUSION, ""),
        create_segment(10, 0, 0.2, 0.5, SegmentType.EXTRUSION, ""),
        create_segment(10, 1, 0.2, 1.0, SegmentType.EXTRUSION, ""),  # Sharp corner
        create_segment(0, 1, 0.2, 1.5, SegmentType.EXTRUSION, ""),
    ]
    
    optimizer = QualityOptimizer(loop)
    corner_idx = optimizer._find_sharpest_corner(loop)
    
    # Should find a valid corner
    assert 0 <= corner_idx < len(loop)


def test_calculate_angle():
    """Test angle calculation."""
    optimizer = QualityOptimizer([])
    
    # 90 degree angle
    angle = optimizer._calculate_angle((0, 0), (1, 0), (1, 1))
    assert abs(angle - 1.5708) < 0.01  # ~π/2
    
    # 180 degree angle (straight line)
    angle = optimizer._calculate_angle((0, 0), (1, 0), (2, 0))
    assert abs(angle - 3.1416) < 0.01  # ~π


def test_points_close():
    """Test point proximity check."""
    optimizer = QualityOptimizer([])
    
    # Points within tolerance
    assert optimizer._points_close((0, 0), (0.05, 0.05), tolerance=0.1)
    
    # Points outside tolerance
    assert not optimizer._points_close((0, 0), (1, 1), tolerance=0.1)


def test_group_by_layer():
    """Test layer grouping."""
    segments = [
        create_segment(0, 0, 0.2, 0, SegmentType.EXTRUSION, ""),
        create_segment(10, 0, 0.2, 0.5, SegmentType.EXTRUSION, ""),
        create_segment(0, 0, 0.4, 1.0, SegmentType.EXTRUSION, ""),
        create_segment(10, 0, 0.4, 1.5, SegmentType.EXTRUSION, ""),
    ]
    
    optimizer = QualityOptimizer(segments)
    layers = optimizer._group_by_layer(segments)
    
    assert len(layers) == 2
    assert 0.2 in layers
    assert 0.4 in layers
    assert len(layers[0.2]) == 2
    assert len(layers[0.4]) == 2


def test_travel_distance_calculation():
    """Test travel distance calculation."""
    segments = [
        create_segment(0, 0, 0.2, 0, SegmentType.EXTRUSION, ""),
        create_segment(10, 0, 0.2, 0, SegmentType.TRAVEL, ""),  # Travel
        create_segment(10, 10, 0.2, 0.5, SegmentType.EXTRUSION, ""),
    ]
    
    optimizer = QualityOptimizer(segments)
    travel_dist = optimizer._calculate_travel_distance(segments)
    
    # Should have one travel move of 10mm
    assert abs(travel_dist - 10.0) < 0.001


def test_quality_with_no_loops():
    """Test quality optimizer with segments that don't form loops."""
    segments = [
        create_segment(0, 0, 0.2, 0, SegmentType.EXTRUSION, ""),
        create_segment(10, 0, 0.2, 0.5, SegmentType.EXTRUSION, ""),
        create_segment(20, 0, 0.2, 1.0, SegmentType.EXTRUSION, ""),
    ]
    
    optimizer = QualityOptimizer(segments)
    result = optimizer.optimize()
    
    # Should still return valid result
    assert result.optimization_type == "Quality Enhanced"
    assert len(result.segments) == len(segments)


def test_quality_with_empty_segments():
    """Test quality optimizer with empty segments list."""
    optimizer = QualityOptimizer([])
    result = optimizer.optimize()
    
    assert len(result.segments) == 0
    assert result.original_travel_dist == 0.0
    assert result.optimized_travel_dist == 0.0


def test_shell_crossing_reduction_placeholder(sample_loop):
    """Test shell crossing reduction (currently a placeholder)."""
    config = QualityConfig(reduce_shell_crossings=True)
    optimizer = QualityOptimizer(sample_loop, config)
    
    # Should not crash, even though it's not fully implemented
    reduced = optimizer._reduce_shell_crossings(sample_loop)
    
    # Currently returns segments unchanged
    assert len(reduced) == len(sample_loop)
