# PDF Title & Heading Extractor

This tool extracts the title and headings (H1, H2, H3) from PDF files using PyMuPDF (fitz). It processes all PDFs in the `input/` directory and outputs structured JSON files to the `output/` directory. Headings are classified by font size, and the largest text on the first page is used as the document title.

## Features
- **Batch processing:** Automatically processes all PDFs in the input folder.
- **Heading detection:** Classifies headings as H1, H2, or H3 based on font size.
- **Title extraction:** Picks the largest text on the first page as the title.
- **Dockerized:** Runs in a reproducible, isolated environment.

## Usage

### 1. Build the Docker image
```sh
docker build -t pdf-extractor .
```

### 2. Prepare your input/output folders
- Place your PDF files in the `input/` directory (create it if it doesn't exist).
- Ensure the `output/` directory exists (it will be created if missing).

### 3. Run the extractor
```sh
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-extractor
```
- On Windows (PowerShell):
```sh
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output pdf-extractor
```

### 4. Check the results
- Extracted JSON files will appear in the `output/` directory, one per PDF.

## Input Format
- Place one or more `.pdf` files in the `input/` directory.

## Output Format
Each output JSON will have the following structure:

```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Heading 1", "page": 1 },
    { "level": "H2", "text": "Subheading", "page": 2 },
    { "level": "H3", "text": "Subsubheading", "page": 2 }
    // ...
  ]
}
```
- `title`: The largest text on the first page.
- `outline`: List of detected headings with their level, text, and page number (1-based).

## Requirements
- Docker (no Python installation needed on host)

## License
MIT 