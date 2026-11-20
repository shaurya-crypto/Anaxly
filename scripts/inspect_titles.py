import pypdfium2 as pdfium
import glob
import os
import re

def main():
    pdfs = sorted(glob.glob('public/**/*.pdf', recursive=True))
    chapter_pdfs = [
        p for p in pdfs
        if not p.endswith('_EM.pdf')
        and 'syllabus' not in p.lower()
        and 'p1x' not in p.lower()
        and 'secp1' not in p.lower()
    ]
    print(f"Total PDFs: {len(chapter_pdfs)}")
    for p in chapter_pdfs:
        doc = pdfium.PdfDocument(p)
        txt0 = doc[0].get_textpage().get_text_range()
        txt1 = doc[1].get_textpage().get_text_range() if len(doc) > 1 else ''
        lines = [l.strip() for l in (txt0 + '\n' + txt1).replace('\r', '').split('\n') if l.strip()]
        fname = os.path.basename(p)
        print(f"=== {fname} ({p}) ===")
        for l in lines[:6]:
            print(f"   {l}")

if __name__ == '__main__':
    main()
