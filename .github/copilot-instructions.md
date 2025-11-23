# Copilot Instructions for m3dp_post_process

## Project Overview

This is a **Python-based G-code post-processing application** for FDM 3D printing optimization, part of the minimal3dp.com ecosystem. The application enables users to upload G-code files and apply optimization strategies (speed, cost, quality, physical properties) through advanced path planning and parameter adjustment algorithms.

## Core Mission

Transform slicer-generated G-code into optimized print instructions by applying research-validated algorithms that most slicers (including OrcaSlicer, Cura, PrusaSlicer) lack: graph theory path planning, Ant Colony Optimization (ACO), K-means clustering for parameter optimization, and kinematic smoothing.

## Brand Context: minimal3dp.com

**Brand Identity:** Minimal 3DP (operated by Mike Wilson) specializes in making complex 3D printing topics accessible to "Ambitious Beginners" and intermediate users. The brand's philosophy is **functional minimalism**—taking inherently complex subjects (Klipper firmware, advanced calibration) and minimizing cognitive load through practical tools.

**Ecosystem Integration:** All tools must integrate with:
- Main site: minimal3dp.com (Hugo static site)
- YouTube channel (primary content engine)
- Klipper calibration tools suite
- OrcaSlicer expertise

## Technical Architecture (From Strategic Plan)

### Target Stack
- **Language:** Python 3.12+
- **Framework:** FastAPI (backend API), with potential for HTMX/Jinja2 frontend
- **Database:** PostgreSQL with JSONB for flexible configuration storage
- **Deployment:** Docker Compose for development, Vercel for production hosting

### Architecture Pattern: Modular Monolith
Avoid microservices complexity. Structure as domain-separated modules within single repo:
```
src/
├── modules/
│   ├── gcode_parser/      # G-code analysis and manipulation
│   ├── optimizer/         # Optimization algorithms (ACO, K-means, MOO)
│   ├── validator/         # Integrity checks (geometric, kinematic)
│   └── profiles/          # Material and printer profile management
```

## G-code Processing Requirements

### Critical Integrity Rules
1. **Never break geometry:** Modified G-code must maintain original object dimensions
2. **Kinematic safety:** Prevent nozzle collisions with printed parts or frame
3. **Parameter bounds:** Keep speeds/temps within material-safe ranges

### Key G-code Commands
- **G1 F-code:** Feedrate (speed optimization target)
- **G0:** Travel moves (path planning optimization)
- **M104/M109/M140/M190:** Temperature control (cost/quality optimization)
- **M221:** Flow control (material usage optimization)
- **G02/G03:** Arc commands (kinematic smoothing for quality)

### Optimization Objectives & Algorithms

| Goal | Target Parameters | Research Algorithm | Expected Outcome |
|------|------------------|-------------------|------------------|
| **Speed** | G1 F-code, G0 travel | K-means clustering, ACO/URPP | 24% time reduction |
| **Cost** | M221 flow, temperatures | K-means, Multi-Objective Evolutionary | 5% material reduction |
| **Quality** | Feedrate, temp, arc fitting | ANN-based Whale Optimization, ACO | Minimize surface roughness |
| **Strength** | Infill, orientation, layer height | Multi-Objective Evolution, FEA | Optimize tensile strength |

## Development Workflow

### Development Container

**This project uses a devcontainer for consistent development environments.** The container includes:
- Python 3.12 with UV pre-installed
- PostgreSQL (ready to enable when needed)
- Dev tools (pytest, ruff, mypy)
- Podman-compatible configuration

To use the devcontainer:
1. Open project in VS Code
2. Select "Reopen in Container" when prompted
3. Dependencies install automatically via `postCreateCommand`

See `.devcontainer/README.md` for detailed setup instructions.

### Python Environment Setup

**This project uses UV for Python environment management.** UV is already installed and configured.

```bash
# Activate the UV venv (if not already active)
source .venv/bin/activate  # On macOS/Linux

# Install/sync dependencies with UV
uv pip install -e ".[dev]"  # Install with dev dependencies
uv pip sync                  # Sync exact dependencies from lock file

# Run Python scripts with UV
uv run python script.py      # Ensures correct venv is used
```

**Important:** Always use `uv` commands instead of plain `pip` or `python` to ensure the UV-managed environment is properly utilized.

### Testing Strategy
- Unit tests for G-code parser (line-by-line accuracy)
- Integration tests for full optimization pipelines
- Validation tests against known-good prints (geometric accuracy)

### File Organization Conventions
- Place research papers in `/research/` (already gitignored as PDFs)
- Strategy documents in `/guide/` (markdown format)
- Data files (CSV calibrations, test G-code) in `/data/` when created

## Klipper-Specific Knowledge

This project must understand Klipper firmware conventions:
- **Pressure Advance:** Extruder-specific physics compensation
- **Input Shaping:** Resonance frequency tuning for print quality
- **Rotation Distance:** Stepper calibration formula
- Klipper G-code commands: `SAVE_CONFIG`, `PID_CALIBRATE`, `QUERY_ENDSTOPS`

Reference the minimal3dp Klipper calibration standards when processing firmware-specific parameters.

## Code Style & Philosophy

### Prompt Efficiency & Cost-Awareness

- **Goal:** Help minimize heavy or expensive model calls and reduce token usage while preserving result quality.
- **Feasibility:** Copilot can heuristically detect and flag high-cost prompts — those that request:
  - complete dumps of large files or entire datasets; or
  - extremely long code reviews (e.g., > 2,000 lines) or multi-file refactors in one prompt; or
  - requests for full dataset transformations on millions of rows without a sample; or
  - output of enormous binary blobs or large base64 content.
- **Actionable behavior:** When Copilot sees such prompts, it should:
  - politely notify the user that the prompt appears expensive and why (explain the heuristic),
  - suggest concrete, lower-cost alternatives (split the task into steps, provide a small sample, request a small proof-of-concept, or ask to confirm before proceeding), and
  - include a succinct example of a more efficient prompt the user can copy/paste.
- **Example:** If a user says "process 1M rows and return the full CSV", Copilot should recommend returning a small sample + code to run locally, or run an on-disk transformation script that writes a CSV instead of printing it.

### Minimal3dp Principles
1. **Practicality over elegance:** Code should solve real problems, not demonstrate theoretical purity
2. **Thoroughness over brevity:** Comprehensive error handling and validation preferred over "clever" shortcuts
3. **Open-source ethos:** Write code that can be understood, forked, and improved by the community

### Python Conventions
- Heavy commenting explaining *why*, not just *what*
- Type hints for all function signatures
- Explicit is better than implicit (Zen of Python)
- Validate inputs at boundaries (API endpoints, file uploads)

### Documentation Requirements
- All algorithms must cite research sources (see `research/Feasibility.md`)
- Complex mathematical operations need inline LaTeX comments
- Configuration examples must be tested with real G-code files

## Common Pitfalls to Avoid

1. **Don't assume slicer capabilities:** Most slicers use simple path planning. That's why this tool exists.
2. **Don't skip validation:** Geometric integrity checks are computationally expensive but mandatory
3. **Don't hardcode printer limits:** Material-safe ranges vary (PLA ≠ ABS ≠ PETG)
4. **Don't optimize blindly:** K-means clustering requires historical successful print data

## Integration Points

### Hugo Static Site (minimal3dp.com)
- Tool will be embedded as `/tools/gcode-optimizer` path
- Must provide standalone HTML/JS interface (no external build required)
- Use TailwindCSS for styling consistency with main site

### Amazon Affiliate Integration
When recommending hardware/materials, use minimal3dp's affiliate disclosure:
```markdown
** Links are Amazon Affiliate Links **
```
Focus on utility-based recommendations (specific tools for specific optimizations).

## External Dependencies & APIs

### Research-Validated Libraries
- **scikit-learn:** K-means clustering implementation
- **NetworkX:** Graph theory for path planning (ACO/URPP)
- **NumPy/Pandas:** Numerical analysis and data processing
- **PyTorch/TensorFlow:** If implementing ANN-based optimization

### G-code Libraries (Evaluate)
- Consider existing parsers but be prepared to write custom line-by-line analyzer
- G-code format is simple but nuanced (modal commands, coordinate systems)

## Critical Questions to Ask

Before implementing any optimization algorithm:
1. What is the validation strategy? (How do we prove it didn't break the print?)
2. What are the material/printer constraints? (Where does the data come from?)
3. What is the computational budget? (Can this run in browser vs. server?)
4. What is the failure mode? (What happens if optimization produces invalid G-code?)

## Getting Started Checklist

For new developers or AI agents:
1. Read `/research/Feasibility.md` for algorithm context
2. Review `/guide/Minimal 3DP Development Strategy Report.md` for architecture
3. Check `/guide/MINIMAL3DP_APP_GUIDE.md` for deployment standards
4. Examine `pyproject.toml` for current dependency state
5. Create sample G-code test fixtures before implementing parsers

## Success Metrics

A successful implementation will:
- Process real-world slicer G-code (Cura, OrcaSlicer, PrusaSlicer)
- Achieve measurable optimization (time/cost/quality) without visual defects
- Pass geometric integrity validation (Hausdorff distance < 0.1mm)
- Integrate seamlessly into minimal3dp.com tooling ecosystem
- Provide clear, educational output (explain *why* each change was made)

---

**Remember:** This tool's goal isn't just to optimize prints—it's to *educate users* about the optimization process. The brand's "Detailed (And Boring)" philosophy means we show our work, cite our sources, and explain trade-offs.
