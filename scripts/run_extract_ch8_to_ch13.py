import subprocess
import sys

chapters = [
    (8, "public/class 9th science/iesc108.pdf", "public/extracted_diagrams/ch8"),
    (9, "public/class 9th science/iesc109.pdf", "public/extracted_diagrams/ch9"),
    (10, "public/class 9th science/iesc110.pdf", "public/extracted_diagrams/ch10"),
    (11, "public/class 9th science/iesc111.pdf", "public/extracted_diagrams/ch11"),
    (12, "public/class 9th science/iesc112.pdf", "public/extracted_diagrams/ch12"),
    (13, "public/class 9th science/iesc113.pdf", "public/extracted_diagrams/ch13"),
]

for ch, pdf, out in chapters:
    print(f"\n=======================================================")
    print(f"Extracting Chapter {ch} from {pdf} -> {out}")
    print(f"=======================================================")
    cmd = [
        sys.executable,
        "scripts/extract_textbook_diagrams.py",
        "--pdf", pdf,
        "--out", out,
        "--dpi", "250"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        lines = res.stdout.strip().split("\n")
        summary_lines = [l for l in lines if "complete" in l.lower() or "manifest" in l.lower() or "saved" in l.lower()]
        for sl in summary_lines:
            print(" ", sl)
    else:
        print(f"  [ERROR] Chapter {ch} extraction failed:")
        print(res.stderr[:500])

print("\nAll chapters 8 to 13 diagram extractions complete!")
