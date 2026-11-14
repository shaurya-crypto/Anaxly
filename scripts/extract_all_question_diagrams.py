#!/usr/bin/env python3
"""
extract_all_question_diagrams.py
Extracts figures from textbook PDFs specifically for chapters with diagram-based questions
in Class 9 Maths, Class 10 Maths, and links them to question problems.
"""

import os
import subprocess
import sys

TARGETS = [
    ("public/9/class9_maths/pt1/iemh103.pdf", "public/extracted_diagrams/math9_ch3"),
    ("public/9/class9_maths/pt1/iemh105.pdf", "public/extracted_diagrams/math9_ch5"),
    ("public/9/class9_maths/pt1/iemh108.pdf", "public/extracted_diagrams/math9_ch8"),
    ("public/10/class10_maths/jemh106.pdf", "public/extracted_diagrams/math10_ch6"),
    ("public/10/class10_maths/jemh108.pdf", "public/extracted_diagrams/math10_ch8"),
    ("public/10/class10_maths/jemh109.pdf", "public/extracted_diagrams/math10_ch9"),
    ("public/10/class10_maths/jemh110.pdf", "public/extracted_diagrams/math10_ch10"),
    ("public/10/class10_maths/jemh111.pdf", "public/extracted_diagrams/math10_ch11"),
    ("public/10/class10_maths/jemh112.pdf", "public/extracted_diagrams/math10_ch12"),
]

def main():
    print("========================================================================")
    print("EXTRACTING BOOK DIAGRAMS FOR QUESTION-BASED VISUALS (MATHS & SCIENCE)")
    print("========================================================================\n")

    for pdf_path, out_dir in TARGETS:
        if not os.path.exists(pdf_path):
            print(f"Skipping missing PDF: {pdf_path}")
            continue

        print(f"[*] Extracting: {pdf_path} -> {out_dir}")
        os.makedirs(out_dir, exist_ok=True)
        cmd = [
            sys.executable,
            "scripts/extract_textbook_diagrams.py",
            "--pdf", pdf_path,
            "--out", out_dir,
            "--dpi", "200"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            count = len([f for f in os.listdir(out_dir) if f.endswith('.webp')])
            print(f"    [+] Successfully extracted {count} figures into {out_dir}")
        else:
            print(f"    [-] Failed extracting {pdf_path}: {res.stderr[:200]}")

    print("\nExtraction of all target textbook diagram folders complete!")

if __name__ == "__main__":
    main()
