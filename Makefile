# Simple Makefile to run ACO benchmark presets via Python (uv)

UV=uv
PY=$(UV) run python
BENCH=Scripts to compare ACO variants on G-code
FILE=g-code/3DBenchy_PLA_NoScripts.gcode
# Output path for init-bench (can be overridden: make init-bench OUT=bench.local.json)
OUT?=bench.json

.PHONY: bench-quick bench-3layers bench-full help bench list-presets init-bench

help:
	@echo "Available targets:"
	@echo "  make bench-quick   # 1x1, first layer, fast sanity compare"
	@echo "  make bench-3layers # 8x8, first 3 layers, illustrative compare"
	@echo "  make bench-full    # 8x8 over full file (can take time)"

bench-quick:
	$(PY) scripts/bench_aco_variants.py $(FILE) \
		--ants 1 \
		--iters 1 \
		--layers 1 \
		--max-nodes 500

bench-3layers:
	$(PY) scripts/bench_aco_variants.py $(FILE) \
		--ants 8 \
		--iters 8 \
		--layers 3 \
		--max-nodes 5000

bench-full:
	$(PY) scripts/bench_aco_variants.py $(FILE) \
		--ants 8 \
		--iters 8

# Generic preset runner via bench.json
bench:
	@if [ -z "$(PRESET)" ]; then echo "Usage: make bench PRESET=<name> (see: make list-presets)"; exit 1; fi
	$(PY) scripts/bench.py $(PRESET)

list-presets:
	$(PY) scripts/bench.py --list

# Scaffold bench.json from template if missing
init-bench:
	@if [ -f $(OUT) ]; then \
		echo "$(OUT) already exists"; \
	else \
		mkdir -p presets; \
		cp presets/preset.template.json $(OUT); \
		echo "Created $(OUT) from presets/preset.template.json"; \
	fi
