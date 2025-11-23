from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import numpy as np


class SegmentType(Enum):
    EXTRUSION = "EXTRUSION"
    TRAVEL = "TRAVEL"
    RETRACT = "RETRACT"
    RECOVER = "RECOVER"
    Z_HOP = "Z_HOP"
    OTHER = "OTHER"


@dataclass
class Point:
    x: float
    y: float
    z: float
    e: float


@dataclass
class Segment:
    start: Point
    end: Point
    type: SegmentType
    speed: float  # mm/min
    line_number: int
    original_text: str


class GCodeParser:
    def __init__(self, file_path: Path | None = None, content: str | None = None):
        self.file_path = file_path
        self.content = content
        self.segments: list[Segment] = []

        # State
        self.current_pos = Point(0.0, 0.0, 0.0, 0.0)
        self.relative_positioning = False  # G91
        self.relative_extrusion = False  # M83
        self.current_speed = 0.0

    def parse(self):
        """Parse the G-code file or content into segments."""
        if self.file_path:
            with open(self.file_path) as f:
                lines = f.readlines()
        elif self.content:
            lines = self.content.splitlines()
        else:
            raise ValueError("No file path or content provided")

        for i, line in enumerate(lines):
            self._parse_line(line.strip(), i + 1)

    def _parse_line(self, line: str, line_num: int):
        if not line or line.startswith(";"):
            return

        # Remove comments
        command = line.split(";")[0].strip()
        parts = command.split()
        if not parts:
            return

        cmd_type = parts[0].upper()

        if cmd_type in ["G0", "G1"]:
            self._handle_move(parts, line, line_num)
        elif cmd_type == "G90":
            self.relative_positioning = False
        elif cmd_type == "G91":
            self.relative_positioning = True
        elif cmd_type == "M82":
            self.relative_extrusion = False
        elif cmd_type == "M83":
            self.relative_extrusion = True

    def _handle_move(self, parts: list[str], original_text: str, line_num: int):
        new_x = self.current_pos.x
        new_y = self.current_pos.y
        new_z = self.current_pos.z
        new_e = self.current_pos.e

        params = {}
        for part in parts[1:]:
            if len(part) > 1:
                key = part[0].upper()
                try:
                    val = float(part[1:])
                    params[key] = val
                except ValueError:
                    continue

        # Update speed if F is present
        if "F" in params:
            self.current_speed = params["F"]

        # Calculate new position
        if "X" in params:
            new_x = (self.current_pos.x + params["X"]) if self.relative_positioning else params["X"]
        if "Y" in params:
            new_y = (self.current_pos.y + params["Y"]) if self.relative_positioning else params["Y"]
        if "Z" in params:
            new_z = (self.current_pos.z + params["Z"]) if self.relative_positioning else params["Z"]

        # Handle Extrusion
        is_extrusion = False
        is_retraction = False

        if "E" in params:
            e_val = params["E"]
            if self.relative_extrusion:
                if e_val > 0:
                    new_e += e_val
                    is_extrusion = True
                elif e_val < 0:
                    new_e += e_val
                    is_retraction = True
            else:
                # Absolute extrusion
                if e_val > self.current_pos.e:
                    is_extrusion = True
                elif e_val < self.current_pos.e:
                    is_retraction = True
                new_e = e_val

        start_point = Point(
            self.current_pos.x, self.current_pos.y, self.current_pos.z, self.current_pos.e
        )
        end_point = Point(new_x, new_y, new_z, new_e)

        # Determine segment type
        seg_type = SegmentType.OTHER
        if is_extrusion:
            seg_type = SegmentType.EXTRUSION
        elif is_retraction:
            seg_type = SegmentType.RETRACT
        elif new_x != self.current_pos.x or new_y != self.current_pos.y:
            seg_type = SegmentType.TRAVEL
        elif new_z != self.current_pos.z:
            seg_type = SegmentType.Z_HOP

        # Only add segment if there is movement or extrusion
        if seg_type != SegmentType.OTHER or is_retraction:
            self.segments.append(
                Segment(
                    start=start_point,
                    end=end_point,
                    type=seg_type,
                    speed=self.current_speed,
                    line_number=line_num,
                    original_text=original_text,
                )
            )

        # Update current position
        self.current_pos = end_point


@dataclass
class OptimizationResult:
    segments: list[Segment]
    original_travel_dist: float
    optimized_travel_dist: float
    optimization_type: str
    metadata: dict | None = None  # Optional metadata for optimization-specific stats


class Optimizer:
    def __init__(self, segments: list[Segment]):
        self.segments = segments

    def _calculate_distance(self, p1: Point, p2: Point) -> float:
        return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def _calculate_total_travel(self, segments: list[Segment]) -> float:
        total = 0.0
        for seg in segments:
            if seg.type == SegmentType.TRAVEL:
                total += self._calculate_distance(seg.start, seg.end)
        return total

    def optimize_travel_greedy(self) -> OptimizationResult:
        """
        Optimize travel moves using a greedy algorithm.
        Returns OptimizationResult with segments and stats.
        """
        original_travel = self._calculate_total_travel(self.segments)

        blocks = []
        current_block = []

        # 1. Group into blocks
        for seg in self.segments:
            if seg.type == SegmentType.EXTRUSION:
                current_block.append(seg)
            else:
                if current_block:
                    blocks.append(current_block)
                    current_block = []

        if current_block:
            blocks.append(current_block)

        if not blocks:
            return OptimizationResult(
                segments=self.segments,
                original_travel_dist=original_travel,
                optimized_travel_dist=original_travel,
                optimization_type="Travel (Speed)",
            )

        # 2. Greedy Sort
        ordered_blocks = []
        current_pos = Point(0, 0, 0, 0)
        remaining_blocks = blocks.copy()

        while remaining_blocks:
            # Find closest block
            best_idx = -1
            min_dist = float("inf")

            for i, block in enumerate(remaining_blocks):
                start_point = block[0].start
                dist = self._calculate_distance(current_pos, start_point)
                if dist < min_dist:
                    min_dist = dist
                    best_idx = i

            # Add best block
            best_block = remaining_blocks.pop(best_idx)
            ordered_blocks.append(best_block)
            current_pos = best_block[-1].end

        # 3. Reconstruct
        new_segments = []
        current_pos = Point(0, 0, 0, 0)

        for block in ordered_blocks:
            start_point = block[0].start

            # Insert Travel if needed
            if start_point.x != current_pos.x or start_point.y != current_pos.y:
                new_segments.append(
                    Segment(
                        start=current_pos,
                        end=start_point,
                        type=SegmentType.TRAVEL,
                        speed=3000,  # Default travel speed
                        line_number=-1,
                        original_text=f"G0 X{start_point.x:.3f} Y{start_point.y:.3f} ; Optimized Travel",
                    )
                )

            new_segments.extend(block)
            current_pos = block[-1].end

        optimized_travel = self._calculate_total_travel(new_segments)

        return OptimizationResult(
            segments=new_segments,
            original_travel_dist=original_travel,
            optimized_travel_dist=optimized_travel,
            optimization_type="Travel (Speed)",
        )

    def to_gcode(self, segments: list[Segment]) -> str:
        """Convert segments back to G-code string."""
        lines = []
        lines.append("; Optimized by M3DP Post Process")

        for seg in segments:
            if seg.original_text:
                lines.append(seg.original_text)
            else:
                # Reconstruct G-code for new segments (Travel)
                # Assuming G0 for travel
                lines.append(f"G0 X{seg.end.x:.3f} Y{seg.end.y:.3f} F{seg.speed:.1f}")

        return "\n".join(lines)
