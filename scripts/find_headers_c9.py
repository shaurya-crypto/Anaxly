import pypdfium2 as pdfium
import glob
import os

for p in sorted(glob.glob("public/9/class 9th science/iesc*.pdf")):
    doc = pdfium.PdfDocument(p)
    found = []
    for i, page in enumerate(doc):
        t = page.get_textpage().get_text_range()
        for line in t.splitlines():
            l = line.strip()
            if any(h in l.lower() for h in ["revise, reflect", "exercise", "think it over", "the journey beyond"]):
                if len(l) < 40:
                    found.append((i + 1, l))
    print(f"{os.path.basename(p)} ({len(doc)} pages):")
    for page_num, h in found[:5]:
        print(f"   p{page_num}: {h}")
