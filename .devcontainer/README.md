# Development Container Setup

This devcontainer provides a consistent development environment for the m3dp_post_process project.

## Features

- **Python 3.12** with UV package manager pre-installed
- **Podman-compatible** configuration
- **Pre-configured dev tools**: pytest, ruff, mypy
- **PostgreSQL service** (ready to enable when needed)
- **VS Code extensions** for Python, Copilot, and Git
- **Zsh shell** with developer utilities

## Using with Podman

This project uses Podman instead of Docker. The devcontainer is fully compatible.

### First-time Setup

1. Ensure Podman is running:
   ```bash
   podman machine start
   ```

2. Install the VS Code Remote - Containers extension

3. Open the project in VS Code and select "Reopen in Container" when prompted

### Manual Start

```bash
# From project root
cd .devcontainer
podman-compose up -d
```

## Enabling PostgreSQL

When you're ready to add database functionality:

1. Edit `docker-compose.yml`:
   - Uncomment the `depends_on: - db` line in the `app` service
   - Uncomment the `profiles:` section in the `db` service

2. Rebuild the container:
   ```bash
   podman-compose down
   podman-compose up -d --build
   ```

3. Connect to PostgreSQL:
   ```bash
   psql -h localhost -U m3dp -d m3dp_post_process
   # Password: m3dp_dev_password
   ```

## UV Python Environment

The container uses UV for Python package management:

```bash
# Install dependencies
uv pip install -e ".[dev]"

# Sync exact dependencies
uv pip sync

# Run Python scripts
uv run python script.py

# Add a new dependency
uv pip install package-name
```

## Installed Extensions

- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Ruff (charliermarsh.ruff)
- Mypy Type Checker (ms-python.mypy-type-checker)
- GitHub Copilot
- GitHub Copilot Chat
- GitLens
- Docker/Podman support

## Port Forwarding

- **8000**: FastAPI development server
- **5432**: PostgreSQL (when enabled)

## File Structure

```
.devcontainer/
├── devcontainer.json       # VS Code configuration
├── Dockerfile              # Python 3.12 + UV environment
├── docker-compose.yml      # Service orchestration
└── README.md              # This file
```

## Troubleshooting

### Podman socket issues

If VS Code can't connect to Podman:

```bash
# Check Podman socket
podman info

# Restart Podman machine
podman machine stop
podman machine start
```

### Python environment issues

```bash
# Rebuild the venv
rm -rf .venv
uv pip install -e ".[dev]"
```

### Container rebuild

```bash
# Complete rebuild
podman-compose down
podman-compose up -d --build
```

## Development Workflow

1. **Start container**: Open project in VS Code (auto-starts container)
2. **Install dependencies**: `uv pip install -e ".[dev]"` (runs automatically)
3. **Run tests**: `pytest`
4. **Lint code**: `ruff check .`
5. **Type check**: `mypy src/`
6. **Run application**: `uv run python main.py`

## AI Agent Usage

This devcontainer is optimized for AI coding agents:

- Consistent Python environment across sessions
- Pre-configured linting and formatting
- Type checking enabled
- All development tools pre-installed
- Comprehensive Copilot instructions in `.github/copilot-instructions.md`
