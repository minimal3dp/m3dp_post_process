"""
Tests for Segment Integration (Fok et al. 2019).

Validates the dynamic graph reduction mechanism that merges
frequently-traversed segment pairs into super-segments.
"""

import numpy as np
import pytest

from m3dp_post_process.aco_optimizer import (
    ACOConfig,
    ACOOptimizer,
    SegmentGraph,
    SuperSegment,
)
from m3dp_post_process.gcode_processor import Point, Segment, SegmentType

# ===========================================================================
# Fixtures
# ===========================================================================

@pytest.fixture
def simple_segments():
    """Create 4 segments forming a square path."""
    segments = [
        # Bottom edge (0,0) -> (10,0)
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 5),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=1,
            original_text="G1 X10 Y0 E5 F3000"
        ),
        # Right edge (10,0) -> (10,10)
        Segment(
            start=Point(10, 0, 0, 5),
            end=Point(10, 10, 0, 10),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=2,
            original_text="G1 X10 Y10 E10 F3000"
        ),
        # Top edge (10,10) -> (0,10)
        Segment(
            start=Point(10, 10, 0, 10),
            end=Point(0, 10, 0, 15),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=3,
            original_text="G1 X0 Y10 E15 F3000"
        ),
        # Left edge (0,10) -> (0,0)
        Segment(
            start=Point(0, 10, 0, 15),
            end=Point(0, 0, 0, 20),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=4,
            original_text="G1 X0 Y0 E20 F3000"
        ),
    ]
    return segments


@pytest.fixture
def connected_segments():
    """Create 6 segments where 2-3 are tightly connected."""
    segments = [
        # Segment 0: (0,0) -> (5,0)
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(5, 0, 0, 5),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=1,
            original_text="G1 X5 Y0 E5"
        ),
        # Segment 1: (5,0) -> (10,0) - spatially adjacent to 0
        Segment(
            start=Point(5, 0, 0, 5),
            end=Point(10, 0, 0, 10),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=2,
            original_text="G1 X10 Y0 E10"
        ),
        # Segment 2: (10,0) -> (10,5) - spatially adjacent to 1
        Segment(
            start=Point(10, 0, 0, 10),
            end=Point(10, 5, 0, 15),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=3,
            original_text="G1 X10 Y5 E15"
        ),
        # Segment 3: (0,10) -> (5,10) - NOT adjacent (gap)
        Segment(
            start=Point(0, 10, 0, 15),
            end=Point(5, 10, 0, 20),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=4,
            original_text="G1 X5 Y10 E20"
        ),
    ]
    return segments


@pytest.fixture
def aco_config_with_integration():
    """ACO config with segment integration enabled."""
    return ACOConfig(
        num_ants=5,
        num_iterations=5,
        enable_segment_integration=True,
        integration_threshold=0.5,
        integration_probability=1.0,  # Deterministic for testing
        min_integration_iteration=1,
        max_integration_distance=1.0,  # 1mm tolerance
    )


# ===========================================================================
# Test SuperSegment Data Structure
# ===========================================================================

def test_super_segment_creation(simple_segments):
    """Test creating a SuperSegment from two segments."""
    seg1 = simple_segments[0]
    seg2 = simple_segments[1]

    super_seg = SuperSegment(
        id="SS_0_1",
        original_indices=[0, 1],
        original_segments=[seg1, seg2],
        start_point=(seg1.start.x, seg1.start.y),
        end_point=(seg2.end.x, seg2.end.y),
        total_length=20.0,  # 10 + 10
        is_super=True
    )

    assert super_seg.id == "SS_0_1"
    assert len(super_seg.original_indices) == 2
    assert super_seg.original_indices == [0, 1]
    assert len(super_seg.original_segments) == 2
    assert super_seg.start_point == (0, 0)
    assert super_seg.end_point == (10, 10)
    assert super_seg.total_length == 20.0
    assert super_seg.is_super is True


def test_super_segment_expansion(simple_segments):
    """Test expanding a SuperSegment back to original segments."""
    seg1 = simple_segments[0]
    seg2 = simple_segments[1]

    super_seg = SuperSegment(
        id="SS_0_1",
        original_indices=[0, 1],
        original_segments=[seg1, seg2],
        start_point=(0, 0),
        end_point=(10, 10),
        total_length=20.0,
    )

    expanded = super_seg.original_segments
    assert len(expanded) == 2
    assert expanded[0] == seg1
    assert expanded[1] == seg2


# ===========================================================================
# Test SegmentGraph
# ===========================================================================

def test_segment_graph_initialization(simple_segments):
    """Test SegmentGraph initializes with all segments."""
    graph = SegmentGraph(
        original_segments=simple_segments,
        active_nodes=[],
        node_to_original={}
    )

    assert len(graph.original_segments) == 4
    assert len(graph.active_nodes) == 4  # Auto-initialized
    assert graph.active_nodes == [0, 1, 2, 3]
    assert graph.size() == 4


def test_segment_graph_get_point(simple_segments):
    """Test getting endpoint from graph node."""
    graph = SegmentGraph(
        original_segments=simple_segments,
        active_nodes=[],
        node_to_original={}
    )

    point0 = graph.get_point(0)
    assert point0 == (10, 0)  # End of segment 0

    point1 = graph.get_point(1)
    assert point1 == (10, 10)  # End of segment 1


def test_segment_graph_get_point_super_segment(simple_segments):
    """Test getting endpoint from SuperSegment node."""
    seg1 = simple_segments[0]
    seg2 = simple_segments[1]

    super_seg = SuperSegment(
        id="SS_0_1",
        original_indices=[0, 1],
        original_segments=[seg1, seg2],
        start_point=(0, 0),
        end_point=(10, 10),
        total_length=20.0,
    )

    graph = SegmentGraph(
        original_segments=simple_segments,
        active_nodes=[super_seg, 2, 3],  # super_seg replaces 0 and 1
        node_to_original={}
    )

    point = graph.get_point(super_seg)
    assert point == (10, 10)


def test_segment_graph_get_original_indices(simple_segments):
    """Test getting original indices from nodes."""
    seg1 = simple_segments[0]
    seg2 = simple_segments[1]

    super_seg = SuperSegment(
        id="SS_0_1",
        original_indices=[0, 1],
        original_segments=[seg1, seg2],
        start_point=(0, 0),
        end_point=(10, 10),
        total_length=20.0,
    )

    graph = SegmentGraph(
        original_segments=simple_segments,
        active_nodes=[super_seg, 2, 3],
        node_to_original={}
    )

    # Regular segment
    indices_2 = graph.get_original_indices(2)
    assert indices_2 == [2]

    # SuperSegment
    indices_super = graph.get_original_indices(super_seg)
    assert indices_super == [0, 1]


# ===========================================================================
# Test Spatial Adjacency Detection
# ===========================================================================

def test_are_spatially_adjacent_true(connected_segments, aco_config_with_integration):
    """Test detecting adjacent segments."""
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    # Segment 0 ends at (5,0), Segment 1 starts at (5,0) - exact match
    assert optimizer._are_spatially_adjacent(connected_segments[0], connected_segments[1])

    # Segment 1 ends at (10,0), Segment 2 starts at (10,0) - exact match
    assert optimizer._are_spatially_adjacent(connected_segments[1], connected_segments[2])


def test_are_spatially_adjacent_false(connected_segments, aco_config_with_integration):
    """Test detecting non-adjacent segments."""
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    # Segment 2 ends at (10,5), Segment 3 starts at (0,10) - large gap
    assert not optimizer._are_spatially_adjacent(connected_segments[2], connected_segments[3])


def test_are_spatially_adjacent_tolerance(aco_config_with_integration):
    """Test spatial adjacency with tolerance."""
    # Create segments with small gap (0.5mm)
    seg1 = Segment(
        start=Point(0, 0, 0, 0),
        end=Point(10, 0, 0, 5),
        type=SegmentType.EXTRUSION,
        speed=3000,
        line_number=1,
        original_text="G1 X10 Y0 E5"
    )
    seg2 = Segment(
        start=Point(10.5, 0, 0, 5),  # 0.5mm gap
        end=Point(20, 0, 0, 10),
        type=SegmentType.EXTRUSION,
        speed=3000,
        line_number=2,
        original_text="G1 X20 Y0 E10"
    )

    optimizer = ACOOptimizer([seg1, seg2], aco_config_with_integration)

    # Should be adjacent within 1.0mm tolerance
    assert optimizer._are_spatially_adjacent(seg1, seg2)


# ===========================================================================
# Test STS Pattern Detection
# ===========================================================================

def test_find_sts_patterns_high_pheromone(connected_segments, aco_config_with_integration):
    """Test finding STS patterns with high pheromone."""
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    n = len(connected_segments)
    pheromone = np.ones((n, n)) * 0.1

    # Set high pheromone on edge 0 -> 1 (adjacent segments)
    pheromone[0][1] = 0.9
    pheromone[1][0] = 0.9

    # Set high pheromone on edge 1 -> 2 (adjacent segments)
    pheromone[1][2] = 0.8
    pheromone[2][1] = 0.8

    # Mock tau_max for threshold calculation
    optimizer.tau_max = 1.0

    patterns = optimizer._find_sts_patterns(
        connected_segments,
        pheromone,
        threshold=0.5  # 50% of tau_max = 0.5
    )

    # Should find 2 patterns: (0,1) and (1,2)
    assert len(patterns) >= 2

    # First pattern should be strongest (0,1 with tau=0.9)
    assert patterns[0][0] == 0
    assert patterns[0][1] == 1
    assert patterns[0][2] == pytest.approx(0.9)


def test_find_sts_patterns_no_adjacency(connected_segments, aco_config_with_integration):
    """Test that non-adjacent segments are not detected even with high pheromone."""
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    n = len(connected_segments)
    pheromone = np.ones((n, n)) * 0.1

    # Set high pheromone on edge 2 -> 3 (NOT adjacent - large gap)
    pheromone[2][3] = 0.9
    pheromone[3][2] = 0.9

    optimizer.tau_max = 1.0

    patterns = optimizer._find_sts_patterns(
        connected_segments,
        pheromone,
        threshold=0.5
    )

    # Should NOT find (2,3) because they're not spatially adjacent
    pattern_pairs = [(p[0], p[1]) for p in patterns]
    assert (2, 3) not in pattern_pairs


# ===========================================================================
# Test Segment Merging
# ===========================================================================

def test_merge_segments(connected_segments, aco_config_with_integration):
    """Test merging two segments into a SuperSegment."""
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    super_seg = optimizer._merge_segments(connected_segments, 0, 1)

    assert super_seg.id == "SS_0_1"
    assert super_seg.original_indices == [0, 1]
    assert len(super_seg.original_segments) == 2
    assert super_seg.start_point == (0, 0)
    assert super_seg.end_point == (10, 0)
    assert super_seg.total_length > 0  # Should be sum of two 5mm segments


def test_expand_super_segment(connected_segments, aco_config_with_integration):
    """Test expanding SuperSegment back to original segments."""
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    super_seg = optimizer._merge_segments(connected_segments, 0, 1)
    expanded = optimizer._expand_super_segment(super_seg)

    assert len(expanded) == 2
    assert expanded[0] == connected_segments[0]
    assert expanded[1] == connected_segments[1]


# ===========================================================================
# Test Integration Process
# ===========================================================================

def test_integrate_segments_disabled(connected_segments):
    """Test that integration does nothing when disabled."""
    config = ACOConfig(enable_segment_integration=False)
    optimizer = ACOOptimizer(connected_segments, config)

    n = len(connected_segments)
    pheromone = np.ones((n, n)) * 0.5

    result_segs, merge_count = optimizer._integrate_segments_in_solution(
        connected_segments,
        pheromone,
        iteration=5
    )

    assert result_segs == connected_segments
    assert merge_count == 0


def test_integrate_segments_before_warmup(connected_segments, aco_config_with_integration):
    """Test that integration doesn't run before min_integration_iteration."""
    aco_config_with_integration.min_integration_iteration = 3
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    n = len(connected_segments)
    pheromone = np.ones((n, n)) * 0.9

    result_segs, merge_count = optimizer._integrate_segments_in_solution(
        connected_segments,
        pheromone,
        iteration=2  # Before warmup
    )

    assert result_segs == connected_segments
    assert merge_count == 0


def test_integrate_segments_merges_strong_patterns(connected_segments, aco_config_with_integration):
    """Test that integration merges segments with strong STS patterns."""
    optimizer = ACOOptimizer(connected_segments, aco_config_with_integration)

    n = len(connected_segments)
    pheromone = np.ones((n, n)) * 0.1

    # Set high pheromone on adjacent pair (0, 1)
    pheromone[0][1] = 0.9
    pheromone[1][0] = 0.9

    optimizer.tau_max = 1.0

    result_segs, merge_count = optimizer._integrate_segments_in_solution(
        connected_segments,
        pheromone,
        iteration=3
    )

    # Should have performed at least 1 merge
    assert merge_count >= 1


# ===========================================================================
# Test Edge Cases
# ===========================================================================

def test_integration_with_single_segment(aco_config_with_integration):
    """Test integration with only 1 segment (should do nothing)."""
    single_seg = [
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 5),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=1,
            original_text="G1 X10 Y0 E5"
        )
    ]

    optimizer = ACOOptimizer(single_seg, aco_config_with_integration)

    pheromone = np.ones((1, 1)) * 0.9

    result_segs, merge_count = optimizer._integrate_segments_in_solution(
        single_seg,
        pheromone,
        iteration=3
    )

    assert result_segs == single_seg
    assert merge_count == 0


def test_integration_with_no_adjacency(aco_config_with_integration):
    """Test integration when no segments are spatially adjacent."""
    # Create widely separated segments
    separated_segs = [
        Segment(
            start=Point(0, 0, 0, 0),
            end=Point(10, 0, 0, 5),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=1,
            original_text="G1 X10 Y0 E5"
        ),
        Segment(
            start=Point(100, 100, 0, 5),
            end=Point(110, 100, 0, 10),
            type=SegmentType.EXTRUSION,
            speed=3000,
            line_number=2,
            original_text="G1 X110 Y100 E10"
        ),
    ]

    optimizer = ACOOptimizer(separated_segs, aco_config_with_integration)

    n = len(separated_segs)
    pheromone = np.ones((n, n)) * 0.9
    optimizer.tau_max = 1.0

    result_segs, merge_count = optimizer._integrate_segments_in_solution(
        separated_segs,
        pheromone,
        iteration=3
    )

    # No merges should occur (segments too far apart)
    assert merge_count == 0


def test_integration_probability_effect(connected_segments):
    """Test that integration_probability affects merge rate."""
    # Low probability (10%) - expect few merges
    config_low = ACOConfig(
        enable_segment_integration=True,
        integration_probability=0.1,
        min_integration_iteration=1,
        max_integration_distance=1.0,
    )

    optimizer_low = ACOOptimizer(connected_segments, config_low)

    n = len(connected_segments)
    pheromone = np.ones((n, n)) * 0.1
    pheromone[0][1] = 0.9
    pheromone[1][0] = 0.9
    pheromone[1][2] = 0.9
    pheromone[2][1] = 0.9

    optimizer_low.tau_max = 1.0

    # Run multiple times and count average merges
    merge_counts = []
    for _ in range(10):
        _, merge_count = optimizer_low._integrate_segments_in_solution(
            connected_segments,
            pheromone,
            iteration=3
        )
        merge_counts.append(merge_count)

    avg_merges_low = sum(merge_counts) / len(merge_counts)

    # High probability (90%) - expect more merges
    config_high = ACOConfig(
        enable_segment_integration=True,
        integration_probability=0.9,
        min_integration_iteration=1,
        max_integration_distance=1.0,
    )

    optimizer_high = ACOOptimizer(connected_segments, config_high)
    optimizer_high.tau_max = 1.0

    merge_counts = []
    for _ in range(10):
        _, merge_count = optimizer_high._integrate_segments_in_solution(
            connected_segments,
            pheromone,
            iteration=3
        )
        merge_counts.append(merge_count)

    avg_merges_high = sum(merge_counts) / len(merge_counts)

    # High probability should result in more merges on average
    assert avg_merges_high >= avg_merges_low
