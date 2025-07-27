import fitz  # PyMuPDF
from collections import Counter, defaultdict

def combine_lines(lines, y_threshold=2.0):
    # Group lines that are close together vertically
    if not lines:
        return []
    lines = sorted(lines, key=lambda x: x['y'])
    combined = []
    current = lines[0]
    for line in lines[1:]:
        if abs(line['y'] - current['y']) <= y_threshold and line['size'] == current['size']:
            current['text'] += ' ' + line['text']
        else:
            combined.append(current)
            current = line
    combined.append(current)
    return combined

def extract_headings(pdf_path: str) -> dict:
    doc = fitz.open(pdf_path)
    headings = []
    font_sizes = []
    all_lines = []

    # Step 1: Collect all lines with their font size and position
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")['blocks']
        for block in blocks:
            if block['type'] != 0:
                continue
            for line in block['lines']:
                line_text = ''
                max_size = 0
                min_y = None
                for span in line['spans']:
                    text = span['text'].strip()
                    if not text:
                        continue
                    line_text += (' ' if line_text else '') + text
                    if span['size'] > max_size:
                        max_size = span['size']
                    if min_y is None or span['origin'][1] < min_y:
                        min_y = span['origin'][1]
                if line_text:
                    all_lines.append({
                        'text': line_text.strip(),
                        'size': max_size,
                        'y': min_y,
                        'page': page_num + 1
                    })
                    font_sizes.append(max_size)

    # Step 2: Determine font size thresholds for H1, H2, H3
    unique_sizes = sorted(set(font_sizes), reverse=True)
    if len(unique_sizes) < 3:
        thresholds = unique_sizes + [0] * (3 - len(unique_sizes))
    else:
        thresholds = unique_sizes[:3]
    size_to_level = {thresholds[0]: 'H1', thresholds[1]: 'H2', thresholds[2]: 'H3'}

    # Step 3: Combine lines with the same size and close y to avoid fragments
    lines_by_page_and_size = defaultdict(list)
    for line in all_lines:
        lines_by_page_and_size[(line['page'], line['size'])].append(line)
    combined_lines = []
    for (page, size), lines in lines_by_page_and_size.items():
        combined = combine_lines(lines)
        for c in combined:
            combined_lines.append(c)

    # Step 4: Extract title (combine all largest-size lines on first page)
    first_page_lines = [l for l in combined_lines if l['page'] == 1 and l['size'] == thresholds[0]]
    if first_page_lines:
        # Join all lines with largest font size on first page
        title = ' '.join([l['text'] for l in sorted(first_page_lines, key=lambda x: x['y'])]).strip()
    else:
        title = ''

    # Step 5: Extract headings, deduplicate, filter short/fragmented
    seen = set()
    for line in sorted(combined_lines, key=lambda x: (x['page'], -x['size'], x['y'])):
        text = line['text'].strip()
        size = line['size']
        page = line['page']
        if size in size_to_level and len(text) > 5:
            level = size_to_level[size]
            key = (level, text, page)
            if key not in seen:
                headings.append({
                    'level': level,
                    'text': text,
                    'page': page
                })
                seen.add(key)

    return {
        'title': title,
        'outline': headings
    }

def extract_pdf_structure(pdf_path):
    # TODO: Implement actual extraction logic
    # For now, return a stub result
    return {
        'title': 'Stub Title',
        'headings': [
            {'level': 'H1', 'text': 'Stub Heading 1'},
            {'level': 'H2', 'text': 'Stub Heading 2'},
            {'level': 'H3', 'text': 'Stub Heading 3'}
        ]
    } 