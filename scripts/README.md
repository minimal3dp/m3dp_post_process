# Scripts

Utility scripts for the m3dp_post_process project.

## pdf_to_markdown.py

Converts PDF research papers to Markdown format for git tracking.

### Installation

Install the required dependency:

```bash
uv pip install pymupdf
```

### Usage

Convert all PDFs in `research/` directory:

```bash
python scripts/pdf_to_markdown.py
```

Convert a specific PDF:

```bash
python scripts/pdf_to_markdown.py "paper.pdf"
# or
python scripts/pdf_to_markdown.py paper
```

### Output

- Creates `.md` files with the same name as the PDF
- Preserves document structure and metadata
- Markdown files can be tracked in git while PDFs remain ignored

### Workflow

1. Add new PDF to `research/` directory
2. Run conversion script
3. PDFs are automatically ignored (`.gitignore`)
4. Commit the generated `.md` files

### Example

```bash
# Add a new paper
cp ~/Downloads/new-paper.pdf research/

# Convert it
python scripts/pdf_to_markdown.py new-paper.pdf

# Git will ignore the PDF but track the markdown
git add research/new-paper.md
git commit -m "Add research: new paper"
```
