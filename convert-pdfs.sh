#!/bin/bash
# Quick wrapper to convert PDFs in research/ folder to markdown
#
# Usage:
#   ./convert-pdfs.sh              # Convert all PDFs
#   ./convert-pdfs.sh paper.pdf    # Convert specific PDF

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure we're in the workspace (script is at root)
cd "$SCRIPT_DIR"

# Check if pymupdf is installed
if ! python -c "import pymupdf" 2>/dev/null; then
    echo "📦 Installing pymupdf..."
    uv pip install pymupdf
fi

# Run the conversion script
echo "🔄 Converting PDFs to Markdown..."
python scripts/pdf_to_markdown.py "$@"

echo ""
echo "✅ Done! Markdown files are ready to commit."
echo "   Run: git add research/*.md"
