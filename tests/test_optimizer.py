import pytest
from m3dp_post_process.gcode_processor import Segment, Point, SegmentType, Optimizer

def create_segment(x1, y1, x2, y2, seg_type=SegmentType.EXTRUSION):
    return Segment(
        start=Point(x1, y1, 0, 0),
        end=Point(x2, y2, 0, 0),
        type=seg_type,
        speed=1000,
        line_number=1,
        original_text=""
    )

def test_greedy_optimization():
    # Create 2 blocks
    # Block 1: (10,10) -> (20,10)
    # Block 2: (100,100) -> (110,100)
    # Start is (0,0)
    
    # Case A: Input order is Block 2 then Block 1
    # Greedy should pick Block 1 first (closer to 0,0) then Block 2
    
    block2_seg = create_segment(100, 100, 110, 100)
    block1_seg = create_segment(10, 10, 20, 10)
    
    # Add a travel segment between them to separate into blocks
    travel_seg = Segment(
        start=block2_seg.end,
        end=block1_seg.start,
        type=SegmentType.TRAVEL,
        speed=3000,
        line_number=1,
        original_text=""
    )
    
    segments = [block2_seg, travel_seg, block1_seg] # Wrong order
    
    optimizer = Optimizer(segments)
    optimized = optimizer.optimize_travel_greedy()
    
    # Expected: Travel -> Block 1 -> Travel -> Block 2
    # Count: Travel(1) + Block1(1) + Travel(1) + Block2(1) = 4 segments
    
    assert len(optimized) == 4
    assert optimized[1] == block1_seg # First extrusion block should be Block 1
    assert optimized[3] == block2_seg # Second extrusion block should be Block 2

def test_already_optimal():
    # Case B: Input order is Block 1 then Block 2
    # Greedy should keep it
    block1_seg = create_segment(10, 10, 20, 10)
    block2_seg = create_segment(100, 100, 110, 100)
    
    travel_seg = Segment(
        start=block1_seg.end,
        end=block2_seg.start,
        type=SegmentType.TRAVEL,
        speed=3000,
        line_number=1,
        original_text=""
    )
    
    segments = [block1_seg, travel_seg, block2_seg]
    
    optimizer = Optimizer(segments)
    optimized = optimizer.optimize_travel_greedy()
    
    assert optimized[1] == block1_seg
    assert optimized[3] == block2_seg
