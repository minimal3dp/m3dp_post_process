# Copilot Instructions for m3dp_post_process

## Project Overview

**Python FastAPI application** for G-code post-processing and FDM 3D printing optimization. Part of minimal3dp.com ecosystem. Current implementation includes travel optimization (greedy/ACO), BrickLayers strength enhancement, and quality improvements (seam hiding).

## Architecture & Code Structure

### Current Implementation (Flat Module Pattern)
```
m3dp_post_process/
├── main.py                 # FastAPI app with upload/optimize endpoints
├── gcode_processor.py      # Core: GCodeParser + Optimizer (greedy baseline)
├── aco_optimizer.py        # ACO travel optimization (30-35% improvement)
├── bricklayers.py          # Layer-shifting for strength (port from TengerTechnologies)
├── quality_optimizer.py    # Seam hiding + shell crossing reduction
└── templates/              # Jinja2 HTML (HTMX-enhanced)
```

**Key Pattern:** Each optimizer (`Optimizer`, `ACOOptimizer`, `BrickLayersOptimizer`, `QualityOptimizer`) returns `OptimizationResult` with segments, travel stats, and metadata dict.

### Data Flow
1. **Upload** → `GCodeParser.parse()` → segments (list of `Segment` objects)
2. **Optimize** → Algorithm-specific optimizer → `OptimizationResult`
3. **Download** → `Optimizer.to_gcode(segments)` → modified G-code file

### Core Data Structures
```python
@dataclass
class Point: x, y, z, e  # Coordinates + extrusion

@dataclass
class Segment:           # Single G-code move
    start: Point
    end: Point
    type: SegmentType    # EXTRUSION | TRAVEL | RETRACT | Z_HOP
    speed: float
    line_number: int
    original_text: str

@dataclass
class OptimizationResult:
    segments: list[Segment]
    original_travel_dist: float
    optimized_travel_dist: float
    optimization_type: str
    metadata: dict        # Algorithm-specific stats (e.g., ACO iterations)
```

## Development Environment

### Local Development with UV
- **Python 3.12+** + **UV** package manager
- **CRITICAL:** Always use `uv` commands, not plain `pip`/`python`
  ```bash
  uv venv                      # Create virtual environment
  source .venv/bin/activate    # Activate venv
  uv pip install -e ".[dev]"   # Install with dev dependencies
  uv run pytest                # Run tests with correct env
  uv run uvicorn m3dp_post_process.main:app --reload  # Dev server
  ```

### Testing Strategy
- **Unit tests:** Per-algorithm logic (pytest fixtures for sample G-code)
- **Locations:** `tests/test_parser.py`, `tests/test_aco_optimizer.py`, etc.
- **Run:** `uv run pytest` (auto-discovers tests/)
- **Pattern:** Most tests use `sample_gcode` fixtures with minimal G-code strings

## G-code Processing Patterns

### Parser State Machine (`GCodeParser`)
```python
# Modal state tracking (survives across lines)
self.current_pos = Point(0, 0, 0, 0)      # Absolute position
self.relative_positioning = False          # G90/G91
self.relative_extrusion = False            # M82/M83
self.current_speed = 0.0                   # Last F-code value

# Parse cycle: _parse_line() → _handle_move() → append Segment
```

**Critical:** Parser handles both absolute (G90) and relative (G91) positioning. Most slicers use G90 (absolute XYZ) + M83 (relative E).

### Segment Type Detection Logic
- **EXTRUSION:** E value increases (relative) or E > prev_E (absolute)
- **TRAVEL:** XY movement with no E change
- **RETRACT:** E value decreases (firmware retraction)
- **Z_HOP:** Z changes without XY movement

### Optimization Algorithm Interface
All optimizers follow this contract:
```python
class SomeOptimizer:
    def __init__(self, segments: List[Segment], config: OptConfig):
        self.segments = segments
        self.config = config or OptConfig()
    
    def optimize(self) -> OptimizationResult:
        # 1. Group segments (by layer, part, etc.)
        # 2. Apply algorithm (reorder, modify, insert)
        # 3. Reconstruct G-code segments
        # 4. Return OptimizationResult with stats
```

### Travel Optimization Strategy (Greedy vs ACO)
1. **Greedy** (`Optimizer.optimize_travel_greedy()`):
   - Groups extrusion segments into "blocks"
   - Sorts blocks by nearest-neighbor distance
   - Inserts travel moves between blocks
   - Fast, baseline algorithm (~15% improvement)

2. **ACO** (`ACOOptimizer.optimize()`):
   - Processes each layer independently
   - TSP for part visiting sequence
   - URPP for segment sequence within parts
   - Pheromone-based learning (8 ants × 8 iterations default)
   - Expected 30-35% improvement over greedy

### BrickLayers Implementation Details
- **Port from:** `TengerTechnologies/Bricklayers` (Python script)
- **Algorithm:** Detects internal perimeter blocks via slicer comments (`;TYPE:Perimeter` or `;TYPE:Inner wall`)
- **Shifting:** Odd-numbered perimeter blocks get `Z + layer_height*0.5` offset
- **Edge cases:** First/last layer get E-value multipliers (1.5x and 0.5x) for adhesion
- **Output:** Writes G-code directly (does not use `Segment` reconstruction)

## Development Commands & Workflows

### Running the App
```bash
# Development server (hot reload)
uv run uvicorn m3dp_post_process.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uv run uvicorn m3dp_post_process.main:app --host 0.0.0.0 --port 8000
```

### Testing
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_aco_optimizer.py

# Run with coverage
uv run pytest --cov=m3dp_post_process --cov-report=term-missing

# Watch mode (requires pytest-watch)
uv run ptw
```

### Code Quality
```bash
# Lint with Ruff
ruff check .                    # Check for issues
ruff check --fix .              # Auto-fix issues

# Type checking
mypy m3dp_post_process/         # Type check main package

# Format code
ruff format .                   # Auto-format all Python files
```

## FastAPI Endpoint Architecture

### Current Routes (`main.py`)
1. **`GET /`** → `index.html` template (upload form)
2. **`POST /upload`** → Parses G-code, returns upload success partial (HTMX)
3. **`POST /optimize`** → Runs optimization pipeline, returns results partial (HTMX)
4. **`GET /download/{filename}`** → Serves optimized G-code file
5. **`GET /files/{filename}`** → Serves uploaded G-code file

### Form Parameter Flow (`/optimize`)
```python
optimization_type: "travel" | "bricklayers"
algorithm: "greedy" | "aco"               # For travel optimization
layer_height: float                       # BrickLayers param
num_ants: int, num_iterations: int        # ACO params
seam_hiding: bool, seam_strategy: str     # Quality params
reduce_crossings: bool                    # Quality param
```

### HTMX Pattern
- Templates return HTML partials (not full pages)
- `templates/index.html` → Main upload form
- `templates/partials/upload_success.html` → Shows parsed segment count
- `templates/partials/optimization_result.html` → Shows before/after stats + download link
- No JavaScript framework needed (HTMX handles DOM swapping)

## Testing Conventions

### Fixture Pattern
```python
@pytest.fixture
def sample_gcode():
    """Minimal G-code string for testing parser."""
    return """
G90  ; Absolute positioning
M83  ; Relative extrusion
G1 X10 Y10 E5 F3000
G1 X20 Y20 E10
G0 X30 Y30  ; Travel move
"""

# Usage in test
def test_parser(sample_gcode):
    parser = GCodeParser(content=sample_gcode)
    parser.parse()
    assert len(parser.segments) > 0
```

### Test File Structure
- `test_parser.py` → G-code parsing edge cases (G90/G91, M82/M83)
- `test_optimizer.py` → Greedy algorithm logic
- `test_aco_optimizer.py` → ACO algorithm behavior
- `test_bricklayers.py` → Layer shifting logic
- `test_quality_optimizer.py` → Seam hiding strategies
- `test_main.py` → FastAPI endpoint integration tests

## File Organization & Git Patterns

```
/workspace/
├── m3dp_post_process/        # Main package (flat structure, NOT nested src/)
├── tests/                    # Parallel test structure
├── research/                 # PDFs gitignored, .md tracked
├── guide/                    # Strategy/architecture docs
├── g-code/                   # Sample files for manual testing
├── uploads/                  # Runtime: user uploads (gitignored)
└── outputs/                  # Runtime: optimized files (gitignored)
```

**Git ignore pattern:** Research PDFs ignored (large files), markdown conversions tracked.

## Common Pitfalls & Solutions

### 1. Parser State Leakage
**Problem:** Reusing `GCodeParser` instance without resetting state  
**Solution:** Create new parser per file: `parser = GCodeParser(file_path=path)`

### 2. ACO Convergence Issues
**Problem:** ACO produces worse results than greedy  
**Solution:** Tune `num_ants` (8-16) and `num_iterations` (5-20). More ants = better exploration, more iterations = better convergence.

### 3. BrickLayers Slicer Compatibility
**Problem:** Slicer doesn't use `;TYPE:` comments  
**Solution:** BrickLayers requires OrcaSlicer, PrusaSlicer, or Cura (all emit type comments). Won't work with Simplify3D or older slicers.

### 4. UV Environment Issues
**Problem:** `python` command uses system Python, not UV venv  
**Solution:** Always prefix with `uv run python` or activate venv first

## Research Integration

### Key Papers (in `/research/`)
- `Fok - ACO Based Tool Path Optimizer.md` → ACO algorithm foundation
- `Feasibility.md` → Literature review of optimization strategies
- `FullControl-GCode-Designer-Author-Version-3.md` → G-code manipulation techniques
- Papers prefixed with `IMECE2024_143962` → FEA-based strength optimization

### Citation Pattern in Code
```python
"""
Ant Colony Optimization for G-code toolpath optimization.

Based on research by Fok et al. (2018):
"An ACO-Based Tool-Path Optimizer for 3D Printing Applications"

Expected improvement: 30-35% reduction in extrusionless travel.
"""
```

## Future Architecture Considerations

### Database Integration (Future Consideration)
- Planned for: User profiles, optimization history, material libraries
- Not currently implemented (application is stateless)
- Would require adding PostgreSQL connection via SQLAlchemy

### Modular Monolith Evolution
Current flat structure will refactor to:
```
m3dp_post_process/
├── core/
│   ├── parser.py
│   └── models.py
├── optimizers/
│   ├── travel.py      # Greedy + ACO
│   ├── bricklayers.py
│   └── quality.py
└── api/
    └── routes.py
```

**When to refactor:** After 3+ new optimizers added (avoid premature abstraction)
