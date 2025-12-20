#!/usr/bin/env python3
"""
PDF to Text Converter with OCR Support
Extracts text from all PDF files (including scanned/image PDFs) and saves as .txt files
"""

import os
from pathlib import Path

try:
    import pytesseract
    from pdf2image import convert_from_path
    from PIL import Image
except ImportError as e:
    print("Error: Required libraries are not installed.")
    print("\nPlease install the required packages:")
    print("  pip install pytesseract pdf2image pillow")
    print("\nYou also need to install Tesseract OCR:")
    print("  macOS: brew install tesseract")
    print("  Also install poppler: brew install poppler")
    exit(1)


def convert_pdf_to_text_ocr(pdf_path):
    """Extract text from a PDF file using OCR."""
    try:
        print(f"  Converting PDF to images...")
        # Convert PDF to images
        images = convert_from_path(pdf_path)

        text = ""
        total_pages = len(images)

        # Process each page
        for page_num, image in enumerate(images, 1):
            print(f"  OCR processing page {page_num}/{total_pages}...")

            # Perform OCR on the image
            page_text = pytesseract.image_to_string(image)

            text += f"--- Page {page_num} ---\n"
            text += page_text + "\n\n"

        return text
    except Exception as e:
        print(f"  Error processing {pdf_path}: {e}")
        return None


def main():
    # Get current directory
    current_dir = Path.cwd()

    # Find all PDF files in current directory
    pdf_files = list(current_dir.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    print(f"Found {len(pdf_files)} PDF file(s) to process:\n")

    # Process each PDF
    successful = 0
    failed = 0

    for pdf_path in pdf_files:
        print(f"\nProcessing: {pdf_path.name}")

        # Extract text using OCR
        text = convert_pdf_to_text_ocr(pdf_path)

        if text:
            # Create output filename (same name but .txt extension)
            output_path = pdf_path.with_suffix('.txt')

            # Write to text file
            try:
                with open(output_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text)
                print(f"  ✓ Created: {output_path.name}")
                successful += 1
            except Exception as e:
                print(f"  ✗ Failed to write {output_path.name}: {e}")
                failed += 1
        else:
            failed += 1

    print(f"\n{'='*50}")
    print(f"--- Summary ---")
    print(f"Successfully converted: {successful}")
    print(f"Failed: {failed}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
