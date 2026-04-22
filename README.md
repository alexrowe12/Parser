# PDF Parser

Simple tool to parse PDFs into .txt files to use as context.

This repo contains a single OCR-based parser script, [`pdf_to_text.py`](/Users/alexrowe/Desktop/Personal/Parser/pdf_to_text.py), that:

- finds every `*.pdf` file in the current working directory
- converts each page to an image
- runs OCR with Tesseract
- writes a matching `.txt` file next to the source PDF

It is best suited for turning scanned PDFs or image-heavy PDFs into plain text that can be reused as context in other tools.

## Quickstart

### 1. Install Python packages

```bash
pip install -r requirements.txt
```

### 2. Install system dependencies

On macOS:

```bash
brew install tesseract poppler
```

### 3. Put PDFs in the directory you want to process

The script only processes PDFs in the directory where you run it.

Example from the repo root:

```bash
python3 pdf_to_text.py
```

Example if your PDFs are inside `toParse/`:

```bash
cd toParse
python3 ../pdf_to_text.py
```

### 4. Collect the output

Each PDF produces a `.txt` file with the same base name.

Example:

```text
report.pdf -> report.txt
```

The output includes page markers like `--- Page 1 ---` to preserve rough page boundaries.

## Notes

- OCR quality depends on the scan quality of the PDF.
- The script currently processes only top-level `*.pdf` files in the current directory, not nested folders.
- Output files are written beside the source PDFs.
