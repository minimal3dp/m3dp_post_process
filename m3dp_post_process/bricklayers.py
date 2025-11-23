"""
BrickLayers Optimization Module

Port of the BrickLayers algorithm from TengerTechnologies/Bricklayers.
Implements layer shifting to create interlocking layers for improved print strength.

Original: https://github.com/TengerTechnologies/Bricklayers
Copyright (c) 2025 Roman Tenger
"""

import re
import logging
from dataclasses import dataclass

from .gcode_processor import GCodeParser, Segment, SegmentType, OptimizationResult

logger = logging.getLogger(__name__)


@dataclass
class BrickLayersConfig:
    """Configuration for BrickLayers optimization."""

    layer_height: float = 0.2  # Layer height in mm
    extrusion_multiplier: float = 1.0  # Extrusion multiplier for shifted blocks


class BrickLayersOptimizer:
    """
    Optimizer that implements the BrickLayers layer-shifting algorithm.

    The algorithm shifts alternating internal perimeter blocks by half the layer height
    to create interlocking layers, improving print strength.
    """

    def __init__(self, segments: list[Segment], config: BrickLayersConfig | None = None):
        self.segments = segments
        self.config = config or BrickLayersConfig()
        self.z_shift = self.config.layer_height * 0.5

    def optimize(self) -> OptimizationResult:
        """
        Apply BrickLayers optimization to the segments.

        Returns:
            OptimizationResult with modified segments and statistics
        """
        logger.info("Starting BrickLayers optimization")
        logger.info(
            f"Z-shift: {self.z_shift} mm, Layer height: {self.config.layer_height} mm"
        )

        # Convert segments back to G-code lines for processing
        gcode_lines = self._segments_to_gcode()

        # Process the G-code
        modified_lines = self._process_gcode(gcode_lines)

        # Convert back to segments using content parameter
        parser = GCodeParser(content="\n".join(modified_lines))
        parser.parse()
        modified_segments = parser.segments

        # Calculate statistics
        total_layers = self._count_layers(gcode_lines)
        shifted_blocks = self._count_shifted_blocks(modified_lines)

        logger.info("BrickLayers optimization completed")
        logger.info(f"Total layers: {total_layers}, Shifted blocks: {shifted_blocks}")

        return OptimizationResult(
            segments=modified_segments,
            optimization_type="BrickLayers (Strength)",
            original_travel_dist=0.0,  # Not applicable for this optimization
            optimized_travel_dist=0.0,
            metadata={
                "total_layers": total_layers,
                "shifted_blocks": shifted_blocks,
                "z_shift_mm": self.z_shift,
            },
        )

    def _segments_to_gcode(self) -> list[str]:
        """Convert segments back to G-code lines."""
        lines = []
        for seg in self.segments:
            if seg.original_text:
                lines.append(seg.original_text)
        return lines

    def _process_gcode(self, lines: list[str]) -> list[str]:
        """
        Process G-code lines to apply BrickLayers shifting.

        This is the core algorithm ported from the original bricklayers.py.
        """
        current_layer = 0
        current_z = 0.0
        perimeter_type = None
        perimeter_block_count = 0
        inside_perimeter_block = False
        is_shifted = False

        # Identify total number of layers
        total_layers = sum(1 for line in lines if line.startswith("G1 Z"))

        modified_lines = []

        for line in lines:
            # Detect layer changes
            if line.startswith("G1 Z"):
                z_match = re.search(r"Z([-\d.]+)", line)
                if z_match:
                    current_z = float(z_match.group(1))
                    current_layer = int(current_z / self.config.layer_height)
                    perimeter_block_count = 0  # Reset block counter for new layer
                    logger.debug(f"Layer {current_layer} detected at Z={current_z:.3f}")
                modified_lines.append(line)
                continue

            # Detect perimeter types from slicer comments
            if ";TYPE:External perimeter" in line or ";TYPE:Outer wall" in line:
                perimeter_type = "external"
                inside_perimeter_block = False
                logger.debug(f"External perimeter detected at layer {current_layer}")
            elif ";TYPE:Perimeter" in line or ";TYPE:Inner wall" in line:
                perimeter_type = "internal"
                inside_perimeter_block = False
                logger.debug(f"Internal perimeter block started at layer {current_layer}")
            elif ";TYPE:" in line:  # Reset for other types
                perimeter_type = None
                inside_perimeter_block = False

            # Group lines into perimeter blocks
            if (
                perimeter_type == "internal"
                and line.startswith("G1")
                and "X" in line
                and "Y" in line
                and "E" in line
            ):
                # Start a new perimeter block if not already inside one
                if not inside_perimeter_block:
                    perimeter_block_count += 1
                    inside_perimeter_block = True
                    logger.debug(
                        f"Perimeter block #{perimeter_block_count} detected at layer {current_layer}"
                    )

                    # Insert the corresponding Z height for this block
                    is_shifted = False
                    if perimeter_block_count % 2 == 1:  # Apply Z-shift to odd-numbered blocks
                        adjusted_z = current_z + self.z_shift
                        logger.debug(
                            f"Inserting G1 Z{adjusted_z:.3f} for shifted perimeter block #{perimeter_block_count}"
                        )
                        modified_lines.append(
                            f"G1 Z{adjusted_z:.3f} ; Shifted Z for block #{perimeter_block_count}\n"
                        )
                        is_shifted = True
                    else:  # Reset to the true layer height for even-numbered blocks
                        logger.debug(
                            f"Inserting G1 Z{current_z:.3f} for non-shifted perimeter block #{perimeter_block_count}"
                        )
                        modified_lines.append(
                            f"G1 Z{current_z:.3f} ; Reset Z for block #{perimeter_block_count}\n"
                        )

                # Adjust extrusion (E values) for shifted blocks on first and last layer
                if is_shifted:
                    e_match = re.search(r"E([-\d.]+)", line)
                    if e_match:
                        e_value = float(e_match.group(1))
                        if current_layer == 0:  # First layer
                            new_e_value = e_value * 1.5
                            logger.debug(
                                f"Multiplying E value by 1.5 on first layer (shifted block): {e_value:.5f} -> {new_e_value:.5f}"
                            )
                            line = re.sub(r"E[-\d.]+", f"E{new_e_value:.5f}", line).strip()
                            line += f" ; Adjusted E for first layer, block #{perimeter_block_count}\n"
                        elif current_layer == total_layers - 1:  # Last layer
                            new_e_value = e_value * 0.5
                            logger.debug(
                                f"Multiplying E value by 0.5 on last layer (shifted block): {e_value:.5f} -> {new_e_value:.5f}"
                            )
                            line = re.sub(r"E[-\d.]+", f"E{new_e_value:.5f}", line).strip()
                            line += f" ; Adjusted E for last layer, block #{perimeter_block_count}\n"
                        else:
                            new_e_value = e_value * self.config.extrusion_multiplier
                            logger.debug("Multiplying E value by extrusionMultiplier")
                            line = re.sub(r"E[-\d.]+", f"E{new_e_value:.5f}", line).strip()
                            line += f" ; Adjusted E for extrusionMultiplier, block #{perimeter_block_count}\n"

            elif (
                perimeter_type == "internal"
                and line.startswith("G1")
                and "X" in line
                and "Y" in line
                and "F" in line
            ):  # End of perimeter block
                inside_perimeter_block = False

            modified_lines.append(line)

        return modified_lines

    def _count_layers(self, lines: list[str]) -> int:
        """Count the total number of layers in the G-code."""
        return sum(1 for line in lines if line.startswith("G1 Z"))

    def _count_shifted_blocks(self, lines: list[str]) -> int:
        """Count the number of shifted perimeter blocks."""
        return sum(1 for line in lines if "; Shifted Z for block #" in line)
