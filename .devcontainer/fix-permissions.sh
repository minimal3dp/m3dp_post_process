#!/bin/bash
# Fix ownership issues in devcontainer
# This script ensures all workspace files are owned by the vscode user

set -e

echo "🔧 Fixing file ownership in workspace..."

# Fix ownership of all files in workspace to vscode:vscode
sudo chown -R vscode:vscode /workspace

# Ensure .git directory has correct permissions
sudo chmod -R u+rw /workspace/.git

# Fix common directories that might have permission issues
for dir in .venv .pytest_cache .ruff_cache .mypy_cache __pycache__ outputs uploads; do
    if [ -d "/workspace/$dir" ]; then
        echo "  ✓ Fixed $dir"
        sudo chown -R vscode:vscode "/workspace/$dir"
    fi
done

# Fix research directory files
if [ -d "/workspace/research" ]; then
    echo "  ✓ Fixed research/"
    sudo chown -R vscode:vscode /workspace/research
fi

# Ensure UV cache is owned by vscode
if [ -d "/home/vscode/.cache/uv" ]; then
    sudo chown -R vscode:vscode /home/vscode/.cache/uv
fi

echo "✅ Ownership fixes complete!"
echo ""
echo "Current user: $(whoami) (UID: $(id -u))"
echo "Workspace owner: $(stat -c '%U (UID: %u)' /workspace)"
