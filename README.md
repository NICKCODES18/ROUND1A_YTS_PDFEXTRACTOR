Here is your updated `README.md` for **Round 1A**, with all symbols and emojis removed for a more formal, professional look—while still retaining all the clarity and strength needed to impress the Adobe hackathon judges.

---

# PDF Title and Hierarchical Outline Extractor

Built for the Adobe “Connecting the Dots” Hackathon (Round 1A)

This tool intelligently extracts a document’s title and hierarchical headings (H1, H2, H3), providing a structured JSON outline of the content. It enables smarter document understanding, search, and contextual linking—crucial for next-generation PDF experiences.

---

## Why This Matters

PDFs are ubiquitous, but machines struggle to interpret their structure. This extractor bridges that gap by decoding document hierarchy using layout-aware logic. It’s fast, accurate, and entirely offline—ready to be extended into semantic tools or a futuristic document reader.

---

## What It Does

* Extracts the document title from the most prominent text on the first page
* Identifies and labels headings as H1, H2, or H3 based on font size
* Processes multiple PDFs in batch
* Outputs clean JSON files for each PDF
* Runs entirely offline in a Docker container
* Meets all Adobe Round 1A requirements

---

## Output JSON Format

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

* `title`: Largest prominent text from the first page
* `outline`: List of headings with their type, content, and 1-based page number

---

## Project Structure

```
.
├── app/
│   ├── main.py
│   └── extractor.py
├── input/
├── output/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Usage Instructions

### Step 1: Build the Docker Image

```sh
docker build --platform linux/amd64 -t pdf-extractor .
```

### Step 2: Prepare Your Folders

* Place your `.pdf` files in the `input/` directory
* Ensure `output/` exists (will be created if not)

### Step 3: Run the Extractor

On Linux/macOS:

```sh
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-extractor
```

On Windows (PowerShell):

```sh
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output pdf-extractor
```

---

## Example

Input: `file03.pdf`
Output: `file03.json`
Time taken: Approximately 2 seconds
Headings detected: 22 across H1, H2, H3 levels

---

## Technical Summary

* Title detection uses font size and visual prominence
* Headings classified using configurable thresholds for size
* Fast execution using PyMuPDF
* No external API or web access required
* Modular design ready for Round 1B and Round 2 extensions

---

## Requirements

* Docker
* Linux/AMD64 architecture support
* CPU only, no GPU or network access
* Executes in under 10 seconds per 50-page PDF
* Model-free and lightweight

---

## Optimization Highlights

| Feature           | Description                       |
| ----------------- | --------------------------------- |
| Offline Execution | No internet dependency            |
| Lightweight       | Minimal size and dependency usage |
| Structured Output | Clean, machine-readable JSON      |
| Hackathon Ready   | Meets all Round 1A requirements   |

---

## Hackathon Compliance Checklist

* [x] Accepts PDF input (up to 50 pages)
* [x] Extracts Title, H1, H2, H3 with page numbers
* [x] Outputs correct JSON format
* [x] Dockerized and runs in AMD64 CPU environment
* [x] Fully offline, no network calls
* [x] Completes execution within time and memory constraints
* [x] Easily extendable for future rounds

---

## License

MIT License

---

