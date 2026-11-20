import pypdfium2 as pdfium
import glob
import os
import re

def parse_class9():
    print("=== CLASS 9 SCIENCE DETAILED AUDIT ===")
    files = sorted(glob.glob("public/9/class 9th science/iesc*.pdf"))
    for f in files:
        doc = pdfium.PdfDocument(f)
        bname = os.path.basename(f)
        
        # Scan for 'Revise, Reflect, Refine'
        rrr_page = None
        for i, page in enumerate(doc):
            t = page.get_textpage().get_text_range()
            if "revise, reflect, refine" in t.lower():
                rrr_page = i + 1
                break
                
        # Count questions in RRR
        rrr_questions = []
        if rrr_page:
            for p in range(rrr_page - 1, len(doc)):
                t = doc[p].get_textpage().get_text_range()
                matches = re.findall(r'(?:^|\n)\s*([0-9]{1,2})\.\s+([A-Z].*)', t)
                for qnum, qtext in matches:
                    rrr_questions.append((p + 1, qnum, qtext[:60]))
                    
        print(f"{bname} (Total {len(doc)} pgs): RRR starts on p{rrr_page}, found {len(rrr_questions)} exercise items")

def parse_class10():
    print("\n=== CLASS 10 SCIENCE DETAILED AUDIT ===")
    files = sorted(glob.glob("public/10/class10_science/jesc*.pdf"))
    for f in files:
        doc = pdfium.PdfDocument(f)
        bname = os.path.basename(f)
        
        # Scan for in-text questions and exercises
        in_text_pages = []
        ex_page = None
        for i, page in enumerate(doc):
            t = page.get_textpage().get_text_range()
            if "exercises" in t.lower() and len([l for l in t.splitlines() if l.strip().upper() == "EXERCISES"]) > 0:
                ex_page = i + 1
            if "questions" in t.lower() and len([l for l in t.splitlines() if l.strip().upper() == "QUESTIONS"]) > 0:
                in_text_pages.append(i + 1)
                
        # Count exercise questions
        ex_questions = []
        if ex_page:
            for p in range(ex_page - 1, len(doc)):
                t = doc[p].get_textpage().get_text_range()
                matches = re.findall(r'(?:^|\n)\s*([0-9]{1,2})\.\s+([A-Z].*)', t)
                for qnum, qtext in matches:
                    ex_questions.append((p + 1, qnum, qtext[:60]))
                    
        print(f"{bname} (Total {len(doc)} pgs): In-text pages: {in_text_pages}, Exercises start p{ex_page}, found {len(ex_questions)} exercise items")

parse_class9()
parse_class10()
