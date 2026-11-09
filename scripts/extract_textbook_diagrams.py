#!/usr/bin/env python3
"""
Textbook Diagram Extraction Engine (Anaxly STEM Platform)
---------------------------------------------------------
Extracts authentic geometric figures, graphs, and worked-example diagrams
directly from textbook PDFs (NCERT, ICSE Selina, Cambridge IB) using
dynamic visual cluster analysis, vector path bounding envelopes, and
high-resolution rasterization.

Features:
- Distinguishes true figure captions from running in-text citations.
- Spatially partitions multiple diagrams per page without cross-diagram bleeding.
- Detects column bounds (single vs. dual-column) preventing column bleed.
- Dynamically bounds diagrams using vector curves, lines, rects, and images.
- Filters repeated background watermarks and printer registration marks.
- Trims whitespace margins and exports high-DPI lossless WebP/PNG.
- Generates a structured manifest.json indexing every extracted figure.

Usage:
    python scripts/extract_textbook_diagrams.py --pdf "public/class 9th science/iesc107.pdf" --out "public/extracted_diagrams/ch7" --dpi 250
"""

import os
import re
import sys
import json
import argparse
from typing import List, Dict, Any, Optional, Tuple

try:
    import pdfplumber
    from PIL import Image, ImageOps
except ImportError as err:
    print(f"Error: Missing required packages: {err}")
    print("Please install requirements: pip install pdfplumber pillow")
    sys.exit(1)

# Prepositions and words that indicate an in-text reference rather than a caption
IN_TEXT_PREPOSITIONS = {
    'in', 'see', 'refer', 'to', 'from', 'at', 'with', 'and', 'given',
    'of', 'as', 'than', 'while', 'when', 'under', 'for', 'about', 'like'
}


def clean_fig_id(raw_id: str) -> str:
    """Normalize figure numbers like '7-4' or '7_4' or '7.13a' into '7.4' or '7.13a'."""
    cleaned = raw_id.replace('-', '.').replace('_', '.').strip()
    return cleaned


def find_captions_on_page(page: Any) -> List[Dict[str, Any]]:
    """
    Scans a PDF page and identifies true figure caption anchors.
    Rejects in-text citations like '(Fig. 7.1)', 'as shown in Fig. 7.2b,'.
    """
    words = page.extract_words()
    captions = []
    seen_fig_ids = set()

    for idx, w in enumerate(words):
        t = w['text']
        if not re.match(r'^(?:Fig\.|Figure)', t, re.IGNORECASE):
            continue

        # In-text citations often start with parenthesis or brackets: (Fig. 7.1)
        if t.startswith('(') or t.startswith('['):
            continue

        # Check if preceded by a preposition or open parenthesis
        if idx > 0:
            prev_word = words[idx - 1]['text'].strip()
            if prev_word.endswith('(') or prev_word.endswith('[') or prev_word.lower() in IN_TEXT_PREPOSITIONS:
                continue

        # Determine figure ID from current word or adjacent word
        next_word = words[idx + 1]['text'].strip() if idx + 1 < len(words) else ''

        # Reject if next word is an in-text citation ending with ')' or ',' like 'Fig. 7.2b,'
        if next_word.endswith(')') or next_word.endswith('),') or next_word.endswith(').') or (next_word.endswith(',') and not next_word.endswith(':,')):
            continue

        combined = f"{t} {next_word}"
        match = re.match(r'^(?:Fig\.|Figure)\s*(\d+[\.\-_]\d+[a-zA-Z]?)(?:\s*[:\.\-])?', combined, re.IGNORECASE)

        if match:
            fig_id = clean_fig_id(match.group(1))
            cap_words = [w, words[idx + 1]]
            start_scan = idx + 2
        else:
            match_single = re.match(r'^(?:Fig\.|Figure)\s*(\d+[\.\-_]\d+[a-zA-Z]?)(?:\s*[:\.\-])?', t, re.IGNORECASE)
            if not match_single:
                continue
            fig_id = clean_fig_id(match_single.group(1))
            cap_words = [w]
            start_scan = idx + 1

        if fig_id in seen_fig_ids:
            continue

        # Collect the rest of the caption line/phrase
        for j in range(start_scan, min(len(words), start_scan + 20)):
            curr_w = words[j]
            if abs(curr_w['top'] - w['top']) <= 16:
                cap_words.append(curr_w)
            elif curr_w['top'] > w['top'] + 16 and curr_w['top'] <= w['top'] + 32 and abs(curr_w['x0'] - w['x0']) < 80:
                cap_words.append(curr_w)
            else:
                break

        caption_str = ' '.join(cw['text'] for cw in cap_words)
        if ':' in caption_str or '.' in caption_str or len(cap_words) >= 3:
            seen_fig_ids.add(fig_id)
            captions.append({
                'fig_id': fig_id,
                'caption': caption_str,
                'words': cap_words,
                'x0': min(cw['x0'] for cw in cap_words),
                'top': min(cw['top'] for cw in cap_words),
                'x1': max(cw['x1'] for cw in cap_words),
                'bottom': max(cw['bottom'] for cw in cap_words)
            })

    # Sort captions from top of the page downwards
    captions.sort(key=lambda c: c['top'])
    return captions


def compute_diagram_bounding_box(
    page: Any,
    caption: Dict[str, Any],
    all_page_captions: List[Dict[str, Any]],
    page_width: float,
    page_height: float
) -> Tuple[float, float, float, float]:
    """
    Computes an accurate bounding box around the visual diagram corresponding
    to a figure caption, preventing cross-column bleed and paragraph clipping.
    """
    cap_x0 = caption['x0']
    cap_top = caption['top']
    cap_x1 = caption['x1']
    cap_bottom = caption['bottom']

    # 1. Determine column layout
    is_left_column = cap_x1 < page_width * 0.52 and cap_x0 < page_width * 0.45
    is_right_column = cap_x0 > page_width * 0.46
    is_full_width = (cap_x0 < page_width * 0.40 and cap_x1 > page_width * 0.60) or (not is_left_column and not is_right_column)

    if is_left_column:
        col_x0 = max(24.0, page_width * 0.04)
        col_x1 = min(page_width * 0.50, page_width - 24.0)
    elif is_right_column:
        col_x0 = max(page_width * 0.48, 24.0)
        col_x1 = min(page_width * 0.96, page_width - 24.0)
    else:
        col_x0 = max(24.0, page_width * 0.04)
        col_x1 = min(page_width * 0.96, page_width - 24.0)

    # 2. Determine vertical ceiling
    # Find any preceding caption on the same page in the same column span
    preceding_caps = [
        c for c in all_page_captions
        if c['bottom'] < cap_top and not (c['x1'] < col_x0 or c['x0'] > col_x1)
    ]
    if preceding_caps:
        ceiling_top = max(32.0, max(c['bottom'] for c in preceding_caps) + 4.0)
    else:
        ceiling_top = max(36.0, cap_top - 380.0)

    search_top = ceiling_top
    search_bottom = min(page_height - 24.0, cap_bottom + 12.0)

    # 3. Filter visual elements (images, curves, lines, rects)
    visual_elements = []
    all_raw_elements = (
        getattr(page, 'images', []) +
        getattr(page, 'curves', []) +
        getattr(page, 'lines', []) +
        getattr(page, 'rects', [])
    )

    for el in all_raw_elements:
        # Ignore printer registration / trim marks at page edges
        if (el['x0'] < 25 or el['x1'] > page_width - 25) and el['width'] < 30:
            continue
        if (el['top'] < 25 or el['bottom'] > page_height - 25) and el['height'] < 30:
            continue

        # Ignore repeated background watermark (466x466 or full page)
        if abs(el['width'] - 466.07) < 3 and abs(el['height'] - 466.07) < 3:
            continue
        if el['width'] > page_width * 0.82 and el['height'] > page_height * 0.6:
            continue

        # Must be situated ABOVE the caption (bottom must not extend past caption bottom)
        if el['bottom'] > search_bottom:
            continue
        if el['top'] < search_top:
            continue

        # Must overlap column horizontally
        if el['x1'] < col_x0 - 8 or el['x0'] > col_x1 + 8:
            continue

        visual_elements.append(el)

    if visual_elements:
        # Envelope of detected visual elements
        env_x0 = min(el['x0'] for el in visual_elements)
        env_top = min(el['top'] for el in visual_elements)
        env_x1 = max(el['x1'] for el in visual_elements)
        env_bottom = max(el['bottom'] for el in visual_elements)

        # Include diagram label words inside or immediately adjacent to this visual cluster
        for w in page.extract_words():
            if w['x0'] >= env_x0 - 15 and w['x1'] <= env_x1 + 15:
                if w['top'] >= env_top - 12 and w['bottom'] <= cap_bottom + 6:
                    env_x0 = min(env_x0, w['x0'])
                    env_top = min(env_top, w['top'])
                    env_x1 = max(env_x1, w['x1'])

        # Clamp within column bounds with a small margin
        crop_x0 = max(col_x0, env_x0 - 6.0)
        crop_top = max(search_top, env_top - 6.0)
        crop_x1 = min(col_x1, env_x1 + 6.0)
        crop_bottom = min(page_height - 24.0, max(env_bottom, cap_bottom) + 6.0)
    else:
        # Fallback when visual elements are glyph-based or background vector streams
        crop_x0 = col_x0
        crop_x1 = col_x1
        crop_top = max(search_top, cap_top - 200.0)
        crop_bottom = min(page_height - 24.0, cap_bottom + 6.0)

    return (crop_x0, crop_top, crop_x1, crop_bottom)


def extract_diagrams_from_pdf(
    pdf_path: str,
    output_dir: str,
    dpi: int = 300,
    format_ext: str = "webp",
    max_pages: Optional[int] = None,
    page_start: int = 1,
    page_end: Optional[int] = None,
    prefix: str = ""
) -> List[Dict[str, Any]]:
    """
    Extracts authentic figures and diagrams matching caption anchors from a PDF textbook.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    os.makedirs(output_dir, exist_ok=True)
    extracted_records: List[Dict[str, Any]] = []

    print(f"[DiagramExtractor] Processing PDF: {pdf_path}")
    print(f"[DiagramExtractor] Target Resolution: {dpi} DPI | Format: {format_ext.upper()}")

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        start_idx = max(0, page_start - 1)
        end_idx = min(total_pages, page_end) if page_end else total_pages
        if max_pages:
            end_idx = min(end_idx, start_idx + max_pages)

        for page_idx in range(start_idx, end_idx):
            page_num = page_idx + 1
            page = pdf.pages[page_idx]
            page_width = float(page.width)
            page_height = float(page.height)

            text = page.extract_text() or ""
            if "fig" not in text.lower():
                continue

            captions = find_captions_on_page(page)
            if not captions:
                continue

            for cap in captions:
                fig_id = cap['fig_id']
                crop_bbox = compute_diagram_bounding_box(page, cap, captions, page_width, page_height)

                try:
                    cropped_page = page.crop(crop_bbox)
                    page_img = cropped_page.to_image(resolution=dpi)
                    pil_img = page_img.original

                    # Auto-trim blank margins using inverted bounding box
                    bg = Image.new(pil_img.mode, pil_img.size, (255, 255, 255))
                    diff = ImageOps.invert(pil_img.convert('RGB'))
                    bbox = diff.getbbox()
                    if bbox:
                        pad = 8
                        pad_bbox = (
                            max(0, bbox[0] - pad),
                            max(0, bbox[1] - pad),
                            min(pil_img.width, bbox[2] + pad),
                            min(pil_img.height, bbox[3] + pad)
                        )
                        pil_img = pil_img.crop(pad_bbox)

                    # Filter out tiny noise / empty crops
                    if pil_img.width < 70 or pil_img.height < 45:
                        continue

                    safe_fig_name = f"{prefix}fig_{fig_id.replace('.', '_')}"
                    out_filename = f"{safe_fig_name}.{format_ext.lower()}"
                    out_path = os.path.join(output_dir, out_filename)

                    if format_ext.lower() == "webp":
                        pil_img.save(out_path, format="WEBP", quality=90, method=6)
                    elif format_ext.lower() == "png":
                        pil_img.save(out_path, format="PNG", optimize=True)
                    else:
                        pil_img.save(out_path, format="JPEG", quality=90, optimize=True)

                    file_size_kb = round(os.path.getsize(out_path) / 1024, 1)

                    record = {
                        "figure_id": f"Fig. {fig_id}",
                        "page_number": page_num,
                        "caption": cap['caption'],
                        "filename": out_filename,
                        "file_path": out_path,
                        "dimensions": {
                            "width": pil_img.width,
                            "height": pil_img.height,
                            "aspect_ratio": round(pil_img.width / pil_img.height, 2)
                        },
                        "file_size_kb": file_size_kb,
                        "crop_bbox": [round(c, 1) for c in crop_bbox]
                    }
                    extracted_records.append(record)
                    print(f"  [+] Page {page_num:2d} | {record['figure_id']:<10} -> {out_filename:<18} ({file_size_kb} KB, {pil_img.width}x{pil_img.height}px)")

                except Exception as ex:
                    print(f"  [-] Page {page_num:2d} | Failed extracting Fig. {fig_id}: {ex}")

    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(extracted_records, f, indent=2, ensure_ascii=False)

    print(f"\n[DiagramExtractor] Extraction complete! {len(extracted_records)} figures saved to {output_dir}")
    print(f"[DiagramExtractor] Manifest index created at: {manifest_path}")
    return extracted_records


def main():
    parser = argparse.ArgumentParser(description="Extract textbook figures from PDF curriculum documents.")
    parser.add_argument("--pdf", required=True, help="Path to input textbook PDF file")
    parser.add_argument("--out", default="extracted_diagrams", help="Output directory for images")
    parser.add_argument("--dpi", type=int, default=300, help="Rasterization resolution DPI (default: 300)")
    parser.add_argument("--format", default="webp", choices=["webp", "png", "jpg"], help="Output format (default: webp)")
    parser.add_argument("--max-pages", type=int, default=None, help="Limit pages to process (optional)")
    parser.add_argument("--page-start", type=int, default=1, help="Starting page number (default: 1)")
    parser.add_argument("--page-end", type=int, default=None, help="Ending page number (optional)")
    parser.add_argument("--prefix", default="", help="Optional filename prefix (e.g. 'ch7_')")

    args = parser.parse_args()
    extract_diagrams_from_pdf(
        pdf_path=args.pdf,
        output_dir=args.out,
        dpi=args.dpi,
        format_ext=args.format,
        max_pages=args.max_pages,
        page_start=args.page_start,
        page_end=args.page_end,
        prefix=args.prefix
    )

if __name__ == "__main__":
    main()
