# Project Tasks and Recommendations

## Recommendations

### Technology Stack
- **Backend:** Python 3.11+ with **FastAPI**.
    - *Reason:* High performance, easy integration with AI/ML libraries (NumPy, NetworkX, Scikit-learn), and fits the "Unified Python" goal.
- **Frontend:** **Jinja2 Templates** + **HTMX** + **TailwindCSS**.
    - *Reason:* Allows building a dynamic "Single Page App" feel without writing a separate React/Vue codebase. Keeps logic in Python.
- **Database:** **PostgreSQL** (with JSONB for storing G-code metadata/stats).
- **G-code Processing:** Custom Python parser + **NetworkX** for graph algorithms + **NumPy** for vector math.
- **Deployment:** **Docker Compose** on a cheap VPS (e.g., Hetzner, DigitalOcean, or Railway).
    - *Reason:* Optimization algorithms (ACO/TSP) can be CPU-intensive and long-running, which makes them unsuitable for Vercel's 10-second serverless function timeouts. A VPS allows for background workers (Celery/Redis) to process G-code asynchronously.

### Optimization Strategies (Based on Research)
1.  **Speed (Time Minimization):**
    -   *Algorithm:* **Ant Colony Optimization (ACO)** or **Greedy Next-Closest**.
    -   *Goal:* Reorder print segments (islands/paths) to minimize non-printing travel moves.
    -   *Source:* `Fok - ACO Based Tool Path Optimizer.md`.
2.  **Quality (Defect Reduction):**
    -   *Algorithm:* **Constrained Optimization**.
    -   *Goal:* Minimize "shell crossings" (hopping between disjoint parts) to reduce stringing.
    -   *Goal:* **Seam Hiding** (Randomize or align start points of closed loops).
3.  **Properties (Strength):**
    -   *Note:* Hard to change *after* slicing without re-slicing.
    -   *Goal:* **Anisotropy Analysis**. Analyze the G-code to predict weak points (Z-strength) based on `FDM Filament Data Analysis` research.

## Tasks

### Phase 1: Foundation & Infrastructure
- [x] **Project Setup:** Initialize `minimal-3dp-platform` repo with Docker Compose structure (FastAPI, Postgres, Redis).
- [x] **G-code Parser:** Implement a robust G-code parser in Python.
- [x] **Viewer:** Implement a basic 2D G-code viewer.

### Phase 2: Optimization Engine
- [x] **Travel Optimization (Speed):**
    -   [x] Implement a "Greedy" optimizer (Next Closest) as a baseline.
    -   [x] **ACO Phase 1:** Implement core ACO optimizer with MMAS, candidate lists, early termination
        -   *Research:* Based on Fok et al. (2019), Stützle & Hoos (2000), Dorigo & Gambardella (1997)
        -   *Achievement:* 66% speedup (5m 12s → 1m 45s), 2.6% quality improvement
        -   *Status:* ✅ COMPLETE - 12 tests, 84% coverage
    -   [x] **ACO Phase 2 Infrastructure:** Segment Integration data structures and tests
        -   *Research:* Fok et al. (2019) Section IV.C - Segment Integration mechanism
        -   *Achievement:* Infrastructure complete with 19 tests (100% passing)
        -   *Status:* ✅ COMPLETE - Ready for integration into main loop
    -   [ ] **ACO Phase 2 Tier 1 Implementation:** Wire Segment Integration + Sparse Pheromone Memory
        -   *Goal:* Additional 40-60% speedup (1m 45s → 40-60s total)
        -   *Components:*
            - [ ] Modify `_aco_tsp()` to work with `SegmentGraph` instead of raw points
            - [ ] Call `_integrate_segments_in_solution()` after each ACO iteration
            - [ ] Dynamically resize pheromone matrix as graph shrinks
            - [ ] Implement `SparsePheromoneMatrix` for 50-70% memory reduction
            - [ ] Benchmark on 3.3MB Benchy file to validate 30-40% speedup
        -   *Timeline:* 2-3 weeks (see PHASE_2_ROADMAP.md)
        -   *Expected Impact:* 87% total speedup from baseline (5m → 40-60s)
    -   [ ] **ACO Phase 2 Tier 2 (Optional):** K-means clustering, multi-population, local decay
        -   *Goal:* Handle >50K segment files, improve quality by 10-15%
        -   *Timeline:* 2-3 weeks after Tier 1
        -   *Priority:* Medium (only if working with very large files)
- [x] **Structural Optimization (Strength):**
    -   [x] **BrickLayers:** Implement "BrickLayers" technique (shifting layers to interlock perimeters) for strength.
        -   *Reference:* `TengerTechnologies/Bricklayers` (Python script available).
        -   *Feasibility:* High. Can be adapted from existing script.
- [x] **Quality Optimization:**
    -   [x] ~~**Seam Hiding:**~~ *REMOVED* - Not needed for current use case
    -   [x] **Shell Crossing Reduction:** Integrated into ACO travel optimization
        -   *Research:* Fok et al. reduced strings by 90% (23 → 2 on test model)
        -   *Status:* ✅ COMPLETE - Achieved via better part sequencing
- [ ] **Sequence Reordering:** Logic to safely reorder G-code blocks.

### Phase 2.5: Analytics & Prediction (ML/AI)
- [ ] **Energy & Time Prediction:**
    -   [ ] Train MLP model to predict energy consumption and print time
        -   *Research:* El youbi El idrissi et al. achieved 99.59% R² accuracy
        -   *Requirements:* Collect training data from various prints
        -   *Use Case:* Optimize part orientation for minimal energy/time
- [ ] **Parameter Optimization:**
    -   [ ] Implement hybrid AI approach (ANN + optimization algorithm)
        -   *Goal:* Multi-objective optimization (speed vs quality vs strength)
        -   *Research:* Multiple papers show feasibility
        -   *Complexity:* High - Requires extensive training data
- [ ] **G-code Analysis Dashboard:**
    -   [ ] Display estimated print time, energy consumption, material usage
    -   [ ] Visualize toolpath efficiency metrics
    -   [ ] Highlight potential quality issues (long travels, shell crossings)

### Phase 3: Web Application
- [x] **Upload Interface:** Drag-and-drop G-code upload (HTMX).
- [ ] **Dashboard:** View file stats (print time, filament used).
- [x] **Optimization Controls:** Select "Speed", "Quality", "Hybrid".
- [x] **Results View:** Compare "Original vs. Optimized" stats.
- [x] **G-code Viewer:** Integrate a web-based G-code viewer.
    -   *Recommendation:* **hudbrog/gCodeViewer** (Web-based, Docker-ready).
    -   *Alternatives:* Most others (`yagv`, `Cute-Gcode`, `tatlin`) are desktop Python apps using OpenGL/Tkinter, which are hard to embed in a web app.
    -   *Action:* Clone `gCodeViewer` and serve it via iframe or integrate its JS logic.

### Phase 4: Advanced Features (AI/ML)
- [ ] **Defect Detection (Computer Vision):**
    -   [ ] Integrate camera for real-time print monitoring
        -   *Research:* ResNet-50/EfficientNet achieve 99%+ accuracy
        -   *Use Case:* Detect warping, layer shifts, stringing during print
        -   *Complexity:* High - Requires camera hardware, GPU, trained models
- [ ] **ML Prediction:** Train a simple model to predict "Print Success"
    -   *Resource:* **Slice-100K** dataset (100k+ G-code files) for training data
    -   *Research:* Multiple papers show CNN-based success prediction
- [ ] **LLM Integration:** Use LLM to parse G-code headers and suggest optimizations
    -   *Research:* Recent work shows LLMs can modify G-code for improved mechanical properties
    -   *Use Case:* AI-assisted parameter tuning (temperature, speed, etc.)

## Current Sprint (Phase 2 Tier 1 Completion)
- [ ] **Segment Integration Main Loop:** Wire integration into `_aco_tsp()`
    -   *Task:* Modify ACO loop to work with `SegmentGraph`, call integration after each iteration
    -   *Validation:* Run benchmark on Benchy, expect 30-40% speedup
    -   *Timeline:* 3-5 days
- [ ] **Sparse Pheromone Memory:** Implement `SparsePheromoneMatrix` class
    -   *Task:* Replace NumPy matrices with scipy.sparse or dict-based storage
    -   *Validation:* Memory usage < 100MB for 45K nodes, no speed regression
    -   *Timeline:* 2-3 days
- [ ] **Performance Benchmarking:** Measure improvements on multiple file sizes
    -   *Task:* Test on small (<500 segs), medium (5K segs), large (45K segs) files
    -   *Validation:* Achieve Phase 2 targets from PHASE_2_ROADMAP.md
    -   *Timeline:* 1-2 days
- [ ] **Documentation Update:** Update README with Phase 2 performance metrics
    -   *Task:* Add performance comparison table, update feature list
    -   *Timeline:* 1 day

## Completed Tasks
- [x] **Environment:** Implement Ruff and Pre-commit.
- [x] **UX:** Clarify optimization type (Speed/Cost/Quality) in UI.
- [x] **Cleanup:** Remove `requirements.txt`, rely on `pyproject.toml`.
- [x] **BrickLayers:** Create a new branch `feature/bricklayers` and port the algorithm.
- [x] **Viewer:** Create a new branch `feature/viewer` and integrate `gCodeViewer`.
- [x] **ACO Phase 1:** Implement core ACO with MMAS, candidate lists, early termination (66% speedup)
- [x] **ACO Phase 2 Infrastructure:** Segment Integration data structures + 19 tests
- [x] **Phase 2 Documentation:** Create PHASE_2_ROADMAP.md and update ACO_PERFORMANCE_IMPROVEMENTS.md
- [x] **Research Integration:** Add 12 new research paper citations with analysis

## Repository Organization & Best Practices

### Current Structure (Follows Python Standards)
```
m3dp_post_process/
├── .github/                # GitHub workflows (future CI/CD)
├── m3dp_post_process/      # Main package (flat structure)
│   ├── __init__.py
│   ├── main.py            # FastAPI app entry point
│   ├── gcode_processor.py # Core parser & data models
│   ├── aco_optimizer.py   # ACO algorithm (370 lines, 88% coverage)
│   ├── bricklayers.py     # Strength optimization
│   ├── quality_optimizer.py # Quality improvements
│   └── templates/         # Jinja2 HTML templates
├── tests/                 # Parallel test structure
│   ├── test_parser.py
│   ├── test_aco_optimizer.py (12 tests)
│   ├── test_segment_integration.py (19 tests)
│   └── ...
├── research/              # Research papers (.md tracked, .pdf ignored)
├── guide/                 # Architecture & strategy docs
├── g-code/                # Sample files for testing
├── uploads/               # Runtime: user uploads (gitignored)
├── outputs/               # Runtime: optimized files (gitignored)
├── pyproject.toml         # Modern Python project config
├── docker-compose.yml     # Container orchestration
├── TODO.md                # This file
├── ACO_PERFORMANCE_IMPROVEMENTS.md  # Phase 1 results
└── PHASE_2_ROADMAP.md     # Phase 2 detailed plan
```

### Design Principles Applied ✅
- **Flat Package Structure:** Simple import paths, easy to understand
- **Single Responsibility:** Each file has clear purpose (parser, optimizer, etc.)
- **Test Coverage:** 91% overall, 88% on critical ACO code
- **Type Hints:** Used throughout for maintainability
- **Documentation:** Comprehensive docstrings, research citations in code
- **Configuration as Code:** pyproject.toml for all Python config
- **Separation of Concerns:**
  - Data models in `gcode_processor.py`
  - Algorithms in separate optimizer files
  - Web layer in `main.py`
  - Tests mirror source structure

### Code Quality Metrics ✅
- **Linting:** Ruff configured and enforced
- **Testing:** pytest with 70/70 tests passing
- **Coverage:** 91% overall, tracking per-file
- **Git Hygiene:** Feature branches, descriptive commits, no large binaries
- **Research-Driven:** All algorithms cited with peer-reviewed sources

### Future Refactoring (When Needed)
**Current:** Flat module structure (appropriate for current size)
```python
from m3dp_post_process.aco_optimizer import ACOOptimizer
```

**Future (>5 optimizers):** Modular monolith
```python
m3dp_post_process/
├── core/
│   ├── parser.py
│   └── models.py
├── optimizers/
│   ├── __init__.py
│   ├── travel.py      # ACO + Greedy
│   ├── bricklayers.py
│   └── quality.py
└── api/
    └── routes.py
```

**Trigger for refactoring:** 3+ new optimizer types (avoid premature abstraction)

### CI/CD Recommendations (Future)
- [ ] GitHub Actions workflow for automated testing
- [ ] Pre-commit hooks for linting (ruff) and type checking (mypy)
- [ ] Automated coverage reporting (codecov.io)
- [ ] Docker image builds on main branch
- [ ] Automated deployment to staging VPS

### Security & Maintenance
- [x] No secrets in repository (use environment variables)
- [x] Runtime data (uploads/outputs) gitignored
- [x] Research PDFs gitignored (large files), markdown tracked
- [ ] Dependabot for automated dependency updates
- [ ] SECURITY.md for vulnerability reporting

## Deployment Plan
1.  **Local Dev:** Docker Compose.
2.  **Staging:** Deploy to a small VPS (e.g., $5/mo droplet).
3.  **Production:** Scale VPS or move to managed container service if traffic grows.
