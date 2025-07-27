import os
from extractor import extract_headings

INPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../input'))
PDF_FILE = 'file03.pdf'

pdf_path = os.path.join(INPUT_DIR, PDF_FILE)

if not os.path.exists(pdf_path):
    print(f"File not found: {pdf_path}")
else:
    result = extract_headings(pdf_path)
    print("Extracted Headings:")
    print(result) 