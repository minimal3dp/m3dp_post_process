#!/usr/bin/env python3
"""
Convert PDF files in research/ directory to Markdown format.

This script extracts text from PDF research papers and converts them to
markdown files that can be tracked in git. Run this whenever you add new PDFs.

Usage:
    python scripts/pdf_to_markdown.py              # Convert all PDFs
    python scripts/pdf_to_markdown.py paper.pdf    # Convert specific PDF
"""

import sys
from pathlib import Path

try:
    import pymupdf  # PyMuPDF - aka fitz
except ImportError:
    print("ERROR: PyMuPDF not installed")
    print("Install with: uv pip install pymupdf")
    sys.exit(1)


def extract_pdf_metadata(pdf_path: Path) -> dict[str, str]:
    """Extract metadata from PDF file."""
    try:
        doc = pymupdf.open(pdf_path)
        metadata = doc.metadata
        doc.close()
        return {
            "title": metadata.get("title", ""),
            "author": metadata.get("author", ""),
            "subject": metadata.get("subject", ""),
            "creator": metadata.get("creator", ""),
        }
    except Exception as e:
        print(f"Warning: Could not extract metadata from {pdf_path.name}: {e}")
        return {}


def pdf_to_markdown(pdf_path: Path, output_path: Path | None = None) -> Path:
    """
    Convert a PDF file to Markdown format.

    Args:
        pdf_path: Path to the PDF file
        output_path: Optional output path. Defaults to same name with .md extension

    Returns:
        Path to the created markdown file
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    # Default output path: same name, .md extension
    if output_path is None:
        output_path = pdf_path.with_suffix(".md")

    print(f"Converting: {pdf_path.name} -> {output_path.name}")

    # Extract metadata
    metadata = extract_pdf_metadata(pdf_path)

    # Open PDF and extract text
    doc = pymupdf.open(pdf_path)

    # Build markdown content
    markdown_lines = []

    # Add metadata header
    markdown_lines.append(f"# {metadata.get('title', pdf_path.stem)}\n")

    if metadata.get("author"):
        markdown_lines.append(f"**Author:** {metadata['author']}\n")

    if metadata.get("subject"):
        markdown_lines.append(f"**Subject:** {metadata['subject']}\n")

    markdown_lines.append(f"\n**Source:** `{pdf_path.name}`\n")
    markdown_lines.append("---\n\n")

    # Extract text from each page
    total_pages = len(doc)
    for page_num in range(total_pages):
        page = doc[page_num]

        # Extract text with layout preservation
        text = page.get_text("text")

        if text.strip():
            # Add page marker
            markdown_lines.append(f"## Page {page_num + 1}\n\n")
            markdown_lines.append(text)
            markdown_lines.append("\n\n")

    doc.close()

    # Write markdown file
    output_path.write_text("".join(markdown_lines), encoding="utf-8")
    print(f"✓ Created: {output_path}")

    return output_path


def convert_all_pdfs(research_dir: Path) -> list[Path]:
    """
    Convert all PDF files in the research directory.

    Args:
        research_dir: Path to research directory

    Returns:
        List of created markdown files
    """
    pdf_files = sorted(research_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in {research_dir}")
        return []

    print(f"Found {len(pdf_files)} PDF file(s) to convert\n")

    converted_files = []
    for pdf_path in pdf_files:
        try:
            md_path = pdf_to_markdown(pdf_path)
            converted_files.append(md_path)
        except Exception as e:
            print(f"✗ Error converting {pdf_path.name}: {e}")

    return converted_files


def main():
    """Main entry point."""
    # Determine workspace root
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent
    research_dir = workspace_root / "research"

    if not research_dir.exists():
        print(f"ERROR: Research directory not found: {research_dir}")
        sys.exit(1)

    # Check if specific file provided
    if len(sys.argv) > 1:
        # Convert specific PDF
        pdf_name = sys.argv[1]
        pdf_path = research_dir / pdf_name

        if not pdf_path.exists():
            # Try without .pdf extension
            pdf_path = research_dir / f"{pdf_name}.pdf"

        if not pdf_path.exists():
            print(f"ERROR: PDF not found: {pdf_name}")
            print(f"Searched in: {research_dir}")
            sys.exit(1)

        pdf_to_markdown(pdf_path)
    else:
        # Convert all PDFs
        converted = convert_all_pdfs(research_dir)
        print(f"\n✓ Converted {len(converted)} file(s)")
        print("\nMarkdown files created:")
        for md_file in converted:
            print(f"  - {md_file.name}")


if __name__ == "__main__":
    main()
