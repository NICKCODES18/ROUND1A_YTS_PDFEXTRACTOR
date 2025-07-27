import os
import json
from extractor import extract_headings

INPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../input'))
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f'No PDF files found in {INPUT_DIR}')
        return
    for pdf_file in pdf_files:
        input_path = os.path.join(INPUT_DIR, pdf_file)
        result = extract_headings(input_path)
        output_filename = os.path.splitext(pdf_file)[0] + '.json'
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f'Processed {pdf_file} -> {output_path}')

if __name__ == '__main__':
    main() 