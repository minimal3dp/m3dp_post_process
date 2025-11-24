# M3DP Post Process

G-code post-processing application for FDM 3D printing optimization.

## Features
- Upload G-code files.
- Optimize travel moves using a Greedy algorithm.
- Download optimized G-code.

## Prerequisites
- **Podman** (for containerized deployment)
- **uv** (for local Python management)
- **Python 3.12+**

## Local Development

### Setup with uv

1.  **Install dependencies:**
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install -e .
    ```

2.  **Run the application:**
    ```bash
    uvicorn m3dp_post_process.main:app --reload
    ```

3.  **Run Tests:**
    ```bash
    pytest tests/
    ```

### Deployment with Podman

1.  **Build and Run:**
    ```bash
    podman-compose up --build
    ```
    *Note: Ensure you have `podman-compose` installed.*

## Project Structure
- `m3dp_post_process/`: Source code.
    - `main.py`: FastAPI application.
    - `gcode_processor.py`: Core logic.
    - `templates/`: HTML templates.
- `tests/`: Unit and integration tests.
