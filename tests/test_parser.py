import pytest
from pathlib import Path
from m3dp_post_process.gcode_processor import GCodeParser, SegmentType

def test_parser_initialization():
    parser = GCodeParser(Path("test.gcode"))
    assert parser.file_path.name == "test.gcode"
    assert len(parser.segments) == 0

def test_parse_simple_movement():
    # Create a dummy G-code file content
    gcode_content = """
    G1 X10 Y10 E0.5 F1200
    G1 X20 Y10 E1.0
    G0 X30 Y30
    """
    parser = GCodeParser(content=gcode_content)
    parser.parse()
    
    assert len(parser.segments) == 3
    
    # Check first segment (Extrusion)
    seg1 = parser.segments[0]
    assert seg1.type == SegmentType.EXTRUSION
    assert seg1.start.x == 0.0
    assert seg1.end.x == 10.0
    assert seg1.end.e == 0.5
    assert seg1.speed == 1200.0
    
    # Check second segment (Extrusion)
    seg2 = parser.segments[1]
    assert seg2.type == SegmentType.EXTRUSION
    assert seg2.start.x == 10.0
    assert seg2.end.x == 20.0
    assert seg2.end.e == 1.0
    
    # Check third segment (Travel)
    seg3 = parser.segments[2]
    assert seg3.type == SegmentType.TRAVEL
    assert seg3.start.x == 20.0
    assert seg3.end.x == 30.0
    assert seg3.end.y == 30.0

def test_relative_positioning():
    gcode_content = """
    G91 ; Relative positioning
    G1 X10 Y0
    G1 X10 Y0
    """
    parser = GCodeParser(content=gcode_content)
    parser.parse()
    
    assert parser.segments[0].end.x == 10.0
    assert parser.segments[1].end.x == 20.0

def test_retraction():
    gcode_content = """
    G1 E1.0
    G1 E0.5 ; Retract to 0.5
    """
    parser = GCodeParser(content=gcode_content)
    parser.parse()
    
    assert parser.segments[1].type == SegmentType.RETRACT
    assert parser.segments[1].end.e == 0.5
