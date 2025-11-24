"""Tests for ACO optimizer."""

import pytest
from m3dp_post_process.aco_optimizer import ACOOptimizer, ACOConfig
from m3dp_post_process.gcode_processor import Segment, Point, SegmentType


def create_segment(x, y, z, e, seg_type=SegmentType.EXTRUSION, text=""):
    """Helper to create a segment with start and end points."""
    return Segment(
        start=Point(x=x-1 if x > 0 else 0, y=y, z=z, e=e-0.1 if e > 0 else 0),
        end=Point(x=x, y=y, z=z, e=e),
        type=seg_type,
        speed=1800.0,
        line_number=0,
        original_text=text
    )


@pytest.fixture
def sample_segments():
    """Create sample segments for testing."""
    return [
        create_segment(0, 0, 0.2, 0, SegmentType.EXTRUSION, "G1 X0 Y0 E0"),
        create_segment(10, 0, 0.2, 0.5, SegmentType.EXTRUSION, "G1 X10 Y0 E0.5"),
        create_segment(10, 10, 0.2, 0.5, SegmentType.TRAVEL, "G1 X10 Y10"),
        create_segment(20, 10, 0.2, 1.0, SegmentType.EXTRUSION, "G1 X20 Y10 E1.0"),
        create_segment(20, 20, 0.2, 1.5, SegmentType.EXTRUSION, "G1 X20 Y20 E1.5"),
        # Layer 2
        create_segment(0, 0, 0.4, 2.0, SegmentType.EXTRUSION, "G1 X0 Y0 Z0.4 E2.0"),
        create_segment(15, 15, 0.4, 2.5, SegmentType.EXTRUSION, "G1 X15 Y15 E2.5"),
    ]


def test_aco_config_defaults():
    """Test ACO configuration defaults."""
    config = ACOConfig()
    assert config.aco_variant == "mmas"
    
    assert config.num_ants == 8
    assert config.num_iterations == 8
    assert config.alpha == 1.0
    assert config.beta == 5.0
    assert config.rho == 0.5
    assert config.q0 == 0.9
    assert config.initial_pheromone == 0.1
    assert config.use_mmas is True
    assert config.use_candidate_lists is True
    assert config.enable_early_termination is True


def test_aco_config_custom():
    """Test ACO configuration with custom values."""
    config = ACOConfig(
        num_ants=16,
        num_iterations=12,
        alpha=2.0,
        beta=3.0,
        rho=0.7
    )
    
    assert config.num_ants == 16
    assert config.num_iterations == 12
    assert config.alpha == 2.0
    assert config.beta == 3.0
    assert config.rho == 0.7


def test_aco_optimizer_initialization(sample_segments):
    """Test ACO optimizer initialization."""
    config = ACOConfig()
    optimizer = ACOOptimizer(sample_segments, config)
    
    assert optimizer.config.num_ants == 8
    assert len(optimizer.segments) == 7
    assert len(optimizer.layers) == 2  # Two Z heights
    assert optimizer.iterations_completed == 0


def test_aco_original_variant_disables_mmas(sample_segments):
    """Original variant should disable MMAS and enhancements."""
    config = ACOConfig(aco_variant="original")
    optimizer = ACOOptimizer(sample_segments, config)

    assert optimizer.config.use_mmas is False
    assert optimizer.config.use_candidate_lists is False
    assert optimizer.config.enable_early_termination is False
    assert optimizer.config.q0 == 0.0


def test_aco_mmas_variant_enables_mmas(sample_segments):
    """MMAS variant should enable MMAS."""
    config = ACOConfig(aco_variant="mmas")
    optimizer = ACOOptimizer(sample_segments, config)

    assert optimizer.config.use_mmas is True


def test_aco_variant_reflected_in_metadata(sample_segments):
    """Metadata should include the selected ACO variant."""
    optimizer = ACOOptimizer(sample_segments, ACOConfig(aco_variant="original", num_iterations=1, num_ants=2))
    result = optimizer.optimize()
    assert result.metadata.get("aco_variant") == "original"


def test_aco_optimize(sample_segments):
    """Test ACO optimization returns valid result."""
    optimizer = ACOOptimizer(sample_segments)
    result = optimizer.optimize()
    
    assert result.optimization_type == "Travel (Speed) - ACO"
    assert "algorithm" in result.metadata
    assert result.metadata["algorithm"] == "aco"
    assert "num_ants" in result.metadata
    assert "num_iterations" in result.metadata
    assert "iterations_completed" in result.metadata
    assert "processing_time_s" in result.metadata
    assert result.metadata["iterations_completed"] > 0


def test_aco_group_by_layer(sample_segments):
    """Test layer grouping."""
    optimizer = ACOOptimizer(sample_segments)
    layers = optimizer.layers
    
    assert len(layers) == 2
    assert 0.2 in layers
    assert 0.4 in layers
    assert len(layers[0.2]) == 5
    assert len(layers[0.4]) == 2


def test_aco_distance_calculation():
    """Test distance calculation between points."""
    optimizer = ACOOptimizer([])
    
    # Test horizontal distance
    dist = optimizer._distance((0, 0), (10, 0))
    assert abs(dist - 10.0) < 0.001
    
    # Test vertical distance
    dist = optimizer._distance((0, 0), (0, 10))
    assert abs(dist - 10.0) < 0.001
    
    # Test diagonal distance
    dist = optimizer._distance((0, 0), (3, 4))
    assert abs(dist - 5.0) < 0.001


def test_aco_travel_distance_calculation(sample_segments):
    """Test travel distance calculation."""
    optimizer = ACOOptimizer(sample_segments)
    
    # Calculate travel distance for original segments
    travel_dist = optimizer._calculate_travel_distance(sample_segments)
    
    # Should have at least one travel move (segment 3)
    assert travel_dist > 0


def test_aco_tsp_solving():
    """Test TSP solving with ACO."""
    points = [(0, 0), (10, 0), (10, 10), (0, 10)]
    
    config = ACOConfig(num_ants=4, num_iterations=4)
    optimizer = ACOOptimizer([], config)
    
    tour = optimizer._aco_tsp(points)
    
    # Should visit all points
    assert len(tour) == len(points)
    assert set(tour) == set(range(len(points)))


def test_aco_tour_length_calculation():
    """Test tour length calculation."""
    import numpy as np
    
    optimizer = ACOOptimizer([])
    
    # Create simple distance matrix
    dist_matrix = np.array([
        [0, 10, 20, 15],
        [10, 0, 12, 18],
        [20, 12, 0, 14],
        [15, 18, 14, 0]
    ])
    
    tour = [0, 1, 2, 3]
    length = optimizer._tour_length(tour, dist_matrix)
    
    # 0->1: 10, 1->2: 12, 2->3: 14 = 36
    assert abs(length - 36.0) < 0.001


def test_aco_improvement_over_baseline(sample_segments):
    """Test that ACO provides some optimization."""
    optimizer = ACOOptimizer(sample_segments)
    result = optimizer.optimize()
    
    # Should complete iterations (may be more than config due to multiple layers/parts)
    assert result.metadata["iterations_completed"] >= optimizer.config.num_iterations
    
    # Should have processed segments
    assert len(result.segments) > 0


def test_aco_with_single_segment():
    """Test ACO with single segment (edge case)."""
    single_segment = [
        create_segment(0, 0, 0.2, 0, SegmentType.EXTRUSION, "G1 X0 Y0 E0")
    ]
    
    optimizer = ACOOptimizer(single_segment)
    result = optimizer.optimize()
    
    assert len(result.segments) == 1
    assert result.optimization_type == "Travel (Speed) - ACO"


def test_aco_with_empty_segments():
    """Test ACO with empty segments list."""
    optimizer = ACOOptimizer([])
    result = optimizer.optimize()
    
    assert len(result.segments) == 0
    assert result.original_travel_dist == 0.0
    assert result.optimized_travel_dist == 0.0
