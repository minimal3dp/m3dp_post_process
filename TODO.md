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
- [ ] **Project Setup:** Initialize `minimal-3dp-platform` repo with Docker Compose structure (FastAPI, Postgres, Redis).
- [ ] **G-code Parser:** Implement a robust G-code parser in Python that can:
    -   Identify "Print Segments" (extrusion moves).
    -   Identify "Travel Moves" (non-extrusion).
    -   Group segments into "Layers" and "Islands".
- [ ] **Viewer:** Implement a basic 2D G-code viewer using HTML5 Canvas (or integrate a lightweight JS library like `gcode-preview`) to visualize the path before/after.

### Phase 2: Optimization Engine
- [ ] **Travel Optimization (Speed):**
    -   Implement a "Greedy" optimizer (Next Closest) as a baseline.
    -   Implement an "ACO" optimizer (Ant Colony) for advanced travel reduction.
- [ ] **Sequence Reordering:** Logic to safely reorder G-code blocks without breaking dependencies (e.g., don't print layer 2 before layer 1).

### Phase 3: Web Application
- [ ] **Upload Interface:** Drag-and-drop G-code upload (HTMX).
- [ ] **Dashboard:** View file stats (print time, filament used).
- [ ] **Optimization Controls:** Select "Speed", "Quality", "Hybrid".
- [ ] **Results View:** Compare "Original vs. Optimized" stats (e.g., "Saved 15 minutes").

### Phase 4: Advanced Features (AI/ML)
- [ ] **ML Prediction:** Train a simple model to predict "Print Success" or "Stringing Risk" based on G-code features (travel length, retraction count).
- [ ] **LLM Integration:** Use LLM to parse G-code headers/comments to extract slicer settings (as suggested in Strategy Report).

## Deployment Plan
1.  **Local Dev:** Docker Compose.
2.  **Staging:** Deploy to a small VPS (e.g., $5/mo droplet).
3.  **Production:** Scale VPS or move to managed container service if traffic grows.
