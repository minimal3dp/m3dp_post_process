#!/usr/bin/env python3
"""
Tiny wrapper to run ACO benchmark presets from bench.json.

Usage:
  uv run python scripts/bench.py --list
  uv run python scripts/bench.py <preset-name> [<preset-name> ...] [--ants N] [--iters N] [--layers N] [--max-nodes N] [--file PATH]

Notes:
- Presets are defined in bench.json at the repo root.
- CLI flags override preset values.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESETS_FILE = ROOT / "bench.json"
SCRIPT = ROOT / "scripts" / "bench_aco_variants.py"


def load_presets() -> dict[str, dict]:
    if not PRESETS_FILE.exists():
        raise SystemExit(f"bench.json not found at {PRESETS_FILE}")
    with PRESETS_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    presets = data.get("presets", {})
    if not isinstance(presets, dict):
        raise SystemExit("Invalid bench.json: 'presets' must be a JSON object")
    return presets


def build_cmd(args: argparse.Namespace, preset: dict) -> list[str]:
    # Start with Python interpreter
    cmd = [sys.executable, str(SCRIPT)]

    # Resolve values: CLI overrides preset; fall back to preset
    file = args.file or preset.get("file")
    if not file:
        raise SystemExit("No file specified (neither preset nor --file provided)")
    cmd.append(str(file))

    if args.ants is not None:
        cmd += ["--ants", str(args.ants)]
    elif "ants" in preset:
        cmd += ["--ants", str(preset["ants"])]

    if args.iters is not None:
        cmd += ["--iters", str(args.iters)]
    elif "iters" in preset:
        cmd += ["--iters", str(preset["iters"])]

    if args.layers is not None:
        cmd += ["--layers", str(args.layers)]
    elif "layers" in preset:
        cmd += ["--layers", str(preset["layers"])]

    if args.max_nodes is not None:
        cmd += ["--max-nodes", str(args.max_nodes)]
    elif "max_nodes" in preset:
        cmd += ["--max-nodes", str(preset["max_nodes"])]

    return cmd


def main():
    parser = argparse.ArgumentParser(description="Run ACO benchmark presets")
    parser.add_argument("presets", nargs="*", help="Preset names to run (see --list)")
    parser.add_argument("--list", action="store_true", help="List available presets")
    parser.add_argument("--ants", type=int)
    parser.add_argument("--iters", type=int)
    parser.add_argument("--layers", type=int)
    parser.add_argument("--max-nodes", type=int)
    parser.add_argument("--file", type=str)
    args = parser.parse_args()

    presets = load_presets()

    if args.list:
        if not presets:
            print("No presets found in bench.json")
            return
        print("Available presets:")
        for name, cfg in presets.items():
            parts = [f"{k}={v}" for k, v in cfg.items()]
            print(f"- {name}: " + ", ".join(parts))
        return

    if not args.presets:
        parser.error("No preset specified. Use --list to see available presets.")

    for name in args.presets:
        if name not in presets:
            print(f"Preset not found: {name}", file=sys.stderr)
            continue
        preset = presets[name]
        cmd = build_cmd(args, preset)
        print(f"\n▶ Running preset: {name}")
        # Run the benchmark script as a subprocess
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Preset '{name}' failed with code {e.returncode}", file=sys.stderr)
            sys.exit(e.returncode)


if __name__ == "__main__":
    main()
