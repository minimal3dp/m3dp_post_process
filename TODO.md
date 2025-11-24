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
    -   [ ] Implement an "ACO" optimizer (Ant Colony) for advanced travel reduction.
        -   *Research:* Fok et al. achieved 34% reduction in extrusionless travel and 8.58% print time savings
        -   *Complexity:* Medium - Requires TSP/URPP solver implementation
        -   *Expected Impact:* 30-35% improvement over greedy baseline
- [x] **Structural Optimization (Strength):**
    -   [x] **BrickLayers:** Implement "BrickLayers" technique (shifting layers to interlock perimeters) for strength.
        -   *Reference:* `TengerTechnologies/Bricklayers` (Python script available).
        -   *Feasibility:* High. Can be adapted from existing script.
- [ ] **Quality Optimization:**
    -   [ ] **Seam Hiding:** Randomize or align start points of closed loops to reduce visible seams
        -   *Complexity:* Low - Modify segment ordering logic
        -   *Expected Impact:* Improved visual quality, minimal performance cost
    -   [ ] **Shell Crossing Reduction:** Minimize transitions across part boundaries to reduce stringing
        -   *Research:* Fok et al. reduced strings by 90% (23 → 2 on test model)
        -   *Complexity:* Low-Medium - Refine existing travel optimization
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

## Immediate Tasks (Refinement)
- [x] **Environment:** Implement Ruff and Pre-commit.
- [x] **UX:** Clarify optimization type (Speed/Cost/Quality) in UI.
- [x] **Cleanup:** Remove `requirements.txt`, rely on `pyproject.toml`.
- [x] **BrickLayers:** Create a new branch `feature/bricklayers` and port the algorithm.
- [x] **Viewer:** Create a new branch `feature/viewer` and integrate `gCodeViewer`.

## Deployment Plan
1.  **Local Dev:** Docker Compose.
2.  **Staging:** Deploy to a small VPS (e.g., $5/mo droplet).
3.  **Production:** Scale VPS or move to managed container service if traffic grows.
