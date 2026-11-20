import pypdfium2 as pdfium
import glob
import os

for p in sorted(glob.glob("public/10/class10_science/jesc*.pdf")):
    doc = pdfium.PdfDocument(p)
    found = []
    for i, page in enumerate(doc):
        t = page.get_textpage().get_text_range()
        for line in t.splitlines():
            l = line.strip()
            if any(h in l.lower() for h in ["exercises", "exercise", "questions", "what you have learnt"]):
                if len(l) < 30:
                    found.append((i + 1, l))
    print(f"{os.path.basename(p)} ({len(doc)} pages):")
    for page_num, h in found:
        print(f"   p{page_num}: {h}")
