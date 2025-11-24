#!/usr/bin/env python3
"""
Quick benchmark comparing ACO variants on a single G-code file.

Usage:
    uv run python scripts/bench_aco_variants.py [path/to/file.gcode] [--ants 8] [--iters 8] [--layers 1]

Defaults:
  - File: g-code/3DBenchy_PLA_NoScripts.gcode
    - Ants: 8, Iters: 8, Layers: 1 (for speed)

Outputs a side-by-side summary of:
  - Original travel distance
  - Optimized travel distance (original AS vs MMAS)
  - Absolute and percent improvement
  - Processing time
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

from m3dp_post_process.aco_optimizer import ACOConfig, ACOOptimizer
from m3dp_post_process.gcode_processor import GCodeParser, Segment


def mm(x: float) -> str:
    return f"{x:.2f} mm"


def pct(x: float) -> str:
    return f"{x:.1f}%"


def run_variant(segments, variant: str, ants: int, iters: int):
    cfg = ACOConfig(aco_variant=variant, num_ants=ants, num_iterations=iters)
    opt = ACOOptimizer(segments, cfg)
    t0 = time.time()
    res = opt.optimize()
    dt = time.time() - t0
    return {
        "variant": variant,
        "original_travel": res.original_travel_dist,
        "optimized_travel": res.optimized_travel_dist,
        "saved_travel": res.original_travel_dist - res.optimized_travel_dist,
        "saved_pct": (res.original_travel_dist - res.optimized_travel_dist)
        / res.original_travel_dist
        * 100
        if res.original_travel_dist > 0
        else 0.0,
        "time_s": dt,
        "ants": cfg.num_ants,
        "iters": cfg.num_iterations,
    }


def main():
    parser = argparse.ArgumentParser(description="Benchmark ACO variants on a G-code file")
    parser.add_argument("file", nargs="?", default="g-code/3DBenchy_PLA_NoScripts.gcode")
    parser.add_argument("--ants", type=int, default=8)
    parser.add_argument("--iters", type=int, default=8)
    parser.add_argument("--layers", type=int, default=1, help="Limit to first N layers for speed")
    parser.add_argument(
        "--max-nodes", type=int, default=1000, help="Limit to first N segments (approx nodes)"
    )
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    print(f"📄 File: {path}")
    print(f"🐜 Params: ants={args.ants}, iters={args.iters}")

    # Parse
    gp = GCodeParser(file_path=path)
    gp.parse()
    print(f"🧩 Segments: {len(gp.segments)} total")

    # Optionally limit to first N layers to keep benchmarks fast
    layers_to_use = args.layers if args.layers and args.layers > 0 else 0
    segments: list[Segment] = gp.segments
    if layers_to_use:
        unique_z = []
        seen = set()
        for s in segments:
            z = s.end.z
            if z not in seen:
                seen.add(z)
                unique_z.append(z)
        selected_z = set(unique_z[:layers_to_use])
        segments = [s for s in segments if s.end.z in selected_z]
        print(f"🧪 Using first {layers_to_use} layer(s): {len(segments)} segments")

    # Cap segment count for speed
    max_nodes = args.max_nodes if args.max_nodes and args.max_nodes > 0 else 0
    if max_nodes and len(segments) > max_nodes:
        segments = segments[:max_nodes]
        print(f"⏩ Limiting to first {max_nodes} segments for speed")

    # Variants to compare
    results = []
    for variant in ("original", "mmas"):
        print(f"\n▶ Running ACO variant: {variant} ...")
        r = run_variant(segments, variant, args.ants, args.iters)
        print(f"   - Original travel: {mm(r['original_travel'])}")
        print(f"   - Optimized travel: {mm(r['optimized_travel'])}")
        print(f"   - Saved: {mm(r['saved_travel'])} ({pct(r['saved_pct'])})")
        print(f"   - Time: {r['time_s']:.2f}s")
        results.append(r)

    # Summary table
    print("\n===== Summary =====")
    print("Variant        Original        Optimized       Saved            Time (s)")
    print("-------------- --------------- --------------- ---------------- ----------")
    for r in results:
        print(
            f"{r['variant']:<14} "
            f"{mm(r['original_travel']):<15} "
            f"{mm(r['optimized_travel']):<15} "
            f"{mm(r['saved_travel'])} ({pct(r['saved_pct'])}) "
            f"{r['time_s']:.2f}"
        )


if __name__ == "__main__":
    main()
