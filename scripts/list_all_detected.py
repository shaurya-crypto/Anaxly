import pypdfium2 as pdfium
import glob
import sys, os
sys.path.insert(0, os.path.abspath('.'))
from scripts.generate_textbook_index import detect_chapter_metadata, NCERT_TITLES


def main():
    pdfs = sorted(glob.glob('public/**/*.pdf', recursive=True))
    chapter_pdfs = [
        p for p in pdfs
        if not p.endswith('_EM.pdf')
        and 'syllabus' not in p.lower()
        and 'p1x' not in p.lower()
        and 'secp1' not in p.lower()
    ]
    for p in chapter_pdfs:
        meta = detect_chapter_metadata(p)
        cls = meta['classLevel']
        sub = meta['subject']
        ch = meta['chapterNumber']
        title = meta['chapterTitle']
        print(f"[{cls} {sub}] Ch {ch}: {title} <= {meta['filename']}")

if __name__ == '__main__':
    main()
