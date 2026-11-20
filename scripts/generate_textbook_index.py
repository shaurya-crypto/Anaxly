#!/usr/bin/env python3
"""
Automated Textbook Indexing Engine (NCERT STEM Platform)
-------------------------------------------------------
Scans all 102 NCERT chapter PDFs in `public/` (Classes 9, 10, 11, 12: Maths, Science, Physics, Chemistry).
Extracts:
  1. Chapter metadata (class, subject, part, chapter number, title, pdfPath, totalPages, dimensions)
  2. Section headings with exact PDF page coordinates (bbox, topPercent)
  3. Examples with exact PDF page coordinates (bbox, topPercent)
  4. Exercises & question anchors with exact PDF page coordinates (bbox, topPercent)
Outputs:
  - src/lib/textbookPageMap.json (Full indexed database)
  - src/lib/textbookRegistry.ts (TypeScript registry and typed helper methods)
  - src/lib/textbookResolver.ts (Auto-scroll and query resolver engine)
"""

import os
import sys
import glob
import re
import json
import time
from typing import List, Dict, Any, Optional

try:
    import pypdfium2 as pdfium
except ImportError:
    print("Error: pypdfium2 is required. Please install with: pip install pypdfium2")
    sys.exit(1)

# Canonical NCERT chapter titles map
NCERT_TITLES = {
    # Class 10 Maths
    (10, "Mathematics", 1): "Real Numbers",
    (10, "Mathematics", 2): "Polynomials",
    (10, "Mathematics", 3): "Pair of Linear Equations in Two Variables",
    (10, "Mathematics", 4): "Quadratic Equations",
    (10, "Mathematics", 5): "Arithmetic Progressions",
    (10, "Mathematics", 6): "Triangles",
    (10, "Mathematics", 7): "Coordinate Geometry",
    (10, "Mathematics", 8): "Introduction to Trigonometry",
    (10, "Mathematics", 9): "Some Applications of Trigonometry",
    (10, "Mathematics", 10): "Circles",
    (10, "Mathematics", 11): "Areas Related to Circles",
    (10, "Mathematics", 12): "Surface Areas and Volumes",
    (10, "Mathematics", 13): "Statistics",
    (10, "Mathematics", 14): "Probability",

    # Class 10 Science
    (10, "Science", 1): "Chemical Reactions and Equations",
    (10, "Science", 2): "Acids, Bases and Salts",
    (10, "Science", 3): "Metals and Non-metals",
    (10, "Science", 4): "Carbon and its Compounds",
    (10, "Science", 5): "Life Processes",
    (10, "Science", 6): "Life Processes",
    (10, "Science", 7): "Control and Coordination",
    (10, "Science", 8): "How do Organisms Reproduce?",
    (10, "Science", 9): "Heredity",
    (10, "Science", 10): "Light – Reflection and Refraction",
    (10, "Science", 11): "The Human Eye and the Colourful World",
    (10, "Science", 12): "Electricity",
    (10, "Science", 13): "Magnetic Effects of Electric Current",

    # Class 11 Physics
    (11, "Physics", 1): "Units and Measurements",
    (11, "Physics", 2): "Motion in a Straight Line",
    (11, "Physics", 3): "Motion in a Plane",
    (11, "Physics", 4): "Laws of Motion",
    (11, "Physics", 5): "Work, Energy and Power",
    (11, "Physics", 6): "System of Particles and Rotational Motion",
    (11, "Physics", 7): "Gravitation",
    (11, "Physics", 8): "Mechanical Properties of Solids",
    (11, "Physics", 9): "Mechanical Properties of Fluids",
    (11, "Physics", 10): "Thermal Properties of Matter",
    (11, "Physics", 11): "Thermodynamics",
    (11, "Physics", 12): "Kinetic Theory",
    (11, "Physics", 13): "Oscillations",
    (11, "Physics", 14): "Waves",

    # Class 11 Chemistry
    (11, "Chemistry", 1): "Some Basic Concepts of Chemistry",
    (11, "Chemistry", 2): "Structure of Atom",
    (11, "Chemistry", 3): "Classification of Elements and Periodicity in Properties",
    (11, "Chemistry", 4): "Chemical Bonding and Molecular Structure",
    (11, "Chemistry", 5): "Thermodynamics",
    (11, "Chemistry", 6): "Equilibrium",
    (11, "Chemistry", 7): "Redox Reactions",
    (11, "Chemistry", 8): "Organic Chemistry – Some Basic Principles and Techniques",
    (11, "Chemistry", 9): "Hydrocarbons",

    # Class 11 Mathematics
    (11, "Mathematics", 1): "Sets",
    (11, "Mathematics", 2): "Relations and Functions",
    (11, "Mathematics", 3): "Trigonometric Functions",
    (11, "Mathematics", 4): "Complex Numbers and Quadratic Equations",
    (11, "Mathematics", 5): "Linear Inequalities",
    (11, "Mathematics", 6): "Permutations and Combinations",
    (11, "Mathematics", 7): "Binomial Theorem",
    (11, "Mathematics", 8): "Sequences and Series",
    (11, "Mathematics", 9): "Straight Lines",
    (11, "Mathematics", 10): "Conic Sections",
    (11, "Mathematics", 11): "Introduction to Three Dimensional Geometry",
    (11, "Mathematics", 12): "Limits and Derivatives",
    (11, "Mathematics", 13): "Statistics",
    (11, "Mathematics", 14): "Probability",

    # Class 12 Mathematics
    (12, "Mathematics", 1): "Relations and Functions",
    (12, "Mathematics", 2): "Inverse Trigonometric Functions",
    (12, "Mathematics", 3): "Matrices",
    (12, "Mathematics", 4): "Determinants",
    (12, "Mathematics", 5): "Continuity and Differentiability",
    (12, "Mathematics", 6): "Application of Derivatives",
    (12, "Mathematics", 7): "Integrals",
    (12, "Mathematics", 8): "Application of Integrals",
    (12, "Mathematics", 9): "Differential Equations",
    (12, "Mathematics", 10): "Vector Algebra",
    (12, "Mathematics", 11): "Three Dimensional Geometry",
    (12, "Mathematics", 12): "Linear Programming",
    (12, "Mathematics", 13): "Probability",

    # Class 9 Science
    (9, "Science", 1): "Matter in Our Surroundings",
    (9, "Science", 2): "Cell: The Building Block of Life",
    (9, "Science", 3): "Tissues in Action",
    (9, "Science", 4): "Describing Motion",
    (9, "Science", 5): "Forces and Newton's Laws",
    (9, "Science", 6): "Gravitation",
    (9, "Science", 7): "Work and Energy",
    (9, "Science", 8): "Sound",
    (9, "Science", 9): "Matter in Our Surroundings",
    (9, "Science", 10): "Is Matter Around Us Pure?",
    (9, "Science", 11): "Atoms and Molecules",
    (9, "Science", 12): "Structure of the Atom",
    (9, "Science", 13): "Improvement in Food Resources",

    # Class 9 Mathematics
    (9, "Mathematics", 1): "Orienting Yourself: The Use of Coordinates",
    (9, "Mathematics", 2): "Introduction to Linear Polynomials",
    (9, "Mathematics", 3): "The World of Numbers",
    (9, "Mathematics", 4): "Lines and Angles",
    (9, "Mathematics", 5): "Triangles",
    (9, "Mathematics", 6): "Linear Equations in Two Variables",
    (9, "Mathematics", 7): "Coordinate Geometry",
    (9, "Mathematics", 8): "Heron's Formula",
    (9, "Mathematics", 9): "Propositions and their Converses",
    (9, "Mathematics", 10): "How Quantities Combine: Understanding Data",
    (9, "Mathematics", 11): "The World of Algorithms",
    (9, "Mathematics", 12): "Quadrilaterals",
    (9, "Mathematics", 13): "Two Variables, One Line",
    (9, "Mathematics", 14): "Circles",
}

def detect_chapter_metadata(pdf_path: str) -> Dict[str, Any]:
    norm = pdf_path.replace('\\', '/')
    fname = os.path.basename(norm).lower()
    
    # Class detection
    grade = 10
    if '/9/' in norm or 'class 9' in norm or 'class9' in norm or fname.startswith('ie'):
        grade = 9
    elif '/10/' in norm or 'class10' in norm or fname.startswith('je'):
        grade = 10
    elif '/11/' in norm or 'class11' in norm or fname.startswith('ke'):
        grade = 11
    elif '/12/' in norm or 'class12' in norm or '/12/' in norm or fname.startswith('le'):
        grade = 12

    # Subject detection
    subject = "Mathematics"
    if 'sci' in norm or 'sc' in fname or 'science' in norm:
        subject = "Science"
    elif 'phy' in norm or 'ph' in fname:
        subject = "Physics"
    elif 'chem' in norm or 'ch' in fname:
        subject = "Chemistry"
    elif 'math' in norm or 'mh' in fname:
        subject = "Mathematics"

    part = 1
    if 'pt2' in norm or 'part 2' in norm or 'part2' in norm:
        part = 2

    # Book code and chapter number
    m = re.search(r'([a-z]+)(\d)(\d\d)', fname)
    book_code = ""
    ch_num = 1
    ch_in_part = 1
    if m:
        book_code = m.group(1)
        pt_digit = int(m.group(2))
        ch_in_part = int(m.group(3))
        if pt_digit == 2:
            part = 2
            if subject == "Physics" and grade == 11:
                ch_num = 7 + ch_in_part
            elif subject == "Chemistry" and grade == 11:
                ch_num = 6 + ch_in_part
            elif subject == "Mathematics" and grade == 12:
                ch_num = 6 + ch_in_part
            elif subject == "Mathematics" and grade == 9:
                ch_num = 8 + ch_in_part
            else:
                ch_num = ch_in_part
        else:
            part = 1
            ch_num = ch_in_part

    # For Class 10 Science: jesc106 is Life Processes
    if fname.startswith('jesc'):
        ch_num = int(fname.replace('jesc', '').replace('.pdf', '')) % 100
        ch_in_part = ch_num

    title = NCERT_TITLES.get((grade, subject, ch_num), f"Chapter {ch_num}")
    
    public_idx = norm.find('public/')
    web_pdf_path = norm[public_idx + len('public'):] if public_idx != -1 else norm
    if not web_pdf_path.startswith('/'):
        web_pdf_path = '/' + web_pdf_path

    chapter_id = f"cbse-class{grade}-{subject.lower()}-ch{ch_num}"

    return {
        "id": chapter_id,
        "classLevel": grade,
        "subject": subject,
        "part": part,
        "chapterNumber": ch_num,
        "chapterInPart": ch_in_part,
        "chapterTitle": title,
        "bookCode": book_code,
        "pdfPath": web_pdf_path,
        "fullPath": norm,
        "filename": os.path.basename(norm)
    }


def clean_line_text(text: str) -> str:
    cleaned = re.sub(r'\s+', ' ', text).strip()
    return cleaned


def is_valid_section_heading(sec_num: str, title: str, ch_num: int, ch_in_part: int) -> bool:
    """Validate that this is a genuine chapter section heading, not a floating decimal or unit."""
    t = title.strip()
    if len(t) < 3 or len(t) > 95:
        return False
    if t.endswith('.') or t.endswith(','):
        return False
    if not t[0].isupper():
        return False
    # Filter common sentences / verbs
    first_word = t.split()[0].lower()
    if first_word in [
        'shows', 'gives', 'indicates', 'represents', 'is', 'was', 'are', 'were',
        'can', 'has', 'have', 'mm', 'cm', 'm', 'km', 'g', 'kg', 'mol', 'moles',
        'billion', 'million', 'double', 'has'
    ]:
        return False

    parts = sec_num.split('.')
    try:
        prefix_num = int(parts[0])
        valid_prefixes = {ch_num, ch_in_part}
        # In Class 9/10/11/12, sections always start with chapter number or part number
        if prefix_num not in valid_prefixes:
            return False
    except ValueError:
        return False

    return True


def scan_single_pdf(pdf_info: Dict[str, Any]) -> Dict[str, Any]:
    full_path = pdf_info["fullPath"]
    ch_num = pdf_info["chapterNumber"]
    ch_in_part = pdf_info.get("chapterInPart", ch_num)
    
    pdf = pdfium.PdfDocument(full_path)
    total_pages = len(pdf)
    
    first_page_w, first_page_h = (504, 720)
    if total_pages > 0:
        first_page_w, first_page_h = pdf[0].get_size()
    
    sections_dict = {}  # key: sec_num -> item
    examples_dict = {}  # key: ex_num -> item
    exercises = []
    all_questions = []

    current_exercise = None

    for p_idx in range(total_pages):
        page_num = p_idx + 1
        page = pdf[p_idx]
        pw, ph = page.get_size()
        tp = page.get_textpage()
        raw_text = tp.get_text_range()

        if not raw_text:
            continue

        # CRITICAL: Normalize Windows CRLF into LF so regex multiline ^ and $ match accurately!
        text = raw_text.replace('\r\n', '\n').replace('\r', '\n')

        # -------------------------------------------------------------
        # 1. Section Headings: e.g. "1.1 Introduction" or "10.2 Reflection"
        # -------------------------------------------------------------
        for m in re.finditer(r'(?m)^[ \t]*(\d+\.\d+(?:\.\d+)?)[ \t]+([A-Za-z][^\n\r]*)$', text):
            sec_num = m.group(1).strip()
            sec_title_raw = clean_line_text(m.group(2))
            sec_title = re.sub(r'\s+\d+$', '', sec_title_raw).strip()

            if is_valid_section_heading(sec_num, sec_title, ch_num, ch_in_part):
                span_start = m.start()
                span_len = len(m.group(0))
                n_rects = tp.count_rects(span_start, span_len)
                if n_rects > 0:
                    r = tp.get_rect(0)
                    top = round(ph - r[3], 2)
                    bbox = [round(r[0], 2), top, round(r[2], 2), round(ph - r[1], 2)]
                    top_percent = round(max(0.0, min(1.0, top / ph)), 4)
                    
                    item = {
                        "id": f"sec-{sec_num}",
                        "number": sec_num,
                        "title": sec_title,
                        "page": page_num,
                        "bbox": bbox,
                        "topPercent": top_percent
                    }
                    
                    # If this section appeared on page 1 (TOC) and now appears on a later page (> 1),
                    # overwrite it with the body occurrence!
                    if sec_num in sections_dict:
                        existing = sections_dict[sec_num]
                        if existing["page"] == 1 and page_num > 1:
                            sections_dict[sec_num] = item
                    else:
                        sections_dict[sec_num] = item

                    # Encountering a genuine section heading ends the previous exercise block (e.g. Summary)
                    if current_exercise and page_num > current_exercise["page"]:
                        current_exercise = None

        # -------------------------------------------------------------
        # 2. Examples: e.g. "Example 1", "Example 2.3", "Example 4 :"
        # -------------------------------------------------------------
        for m in re.finditer(r'(?i)\bExample\s+(\d+(?:\.\d+)?)\b[ \t]*(?::[ \t]*)?([^\n\r]*)', text):
            ex_num = m.group(1).strip()
            snippet = clean_line_text(m.group(2))[:90]
            span_start = m.start()
            span_len = len(f"Example {ex_num}")
            n_rects = tp.count_rects(span_start, span_len)
            if n_rects > 0:
                r = tp.get_rect(0)
                top = round(ph - r[3], 2)
                bbox = [round(r[0], 2), top, round(r[2], 2), round(ph - r[1], 2)]
                top_percent = round(max(0.0, min(1.0, top / ph)), 4)
                
                item = {
                    "id": f"ex-{ex_num}",
                    "number": ex_num,
                    "title": f"Example {ex_num}" + (f": {snippet}" if snippet else ""),
                    "snippet": snippet,
                    "page": page_num,
                    "bbox": bbox,
                    "topPercent": top_percent
                }
                if ex_num not in examples_dict:
                    examples_dict[ex_num] = item

        # -------------------------------------------------------------
        # 3. Exercises:
        #    - "EXERCISE 1.1", "EXERCISE 2.2"
        #    - "EXERCISES", "QUESTIONS", "IN-TEXT QUESTIONS"
        #    (Skip page 1 table-of-contents mentions)
        # -------------------------------------------------------------
        if page_num > 1 or total_pages <= 2:
            for m in re.finditer(r'(?i)\b(EXERCISE\s+\d+(?:\.\d+)?|EXERCISES|IN-TEXT QUESTIONS|QUESTIONS)\b', text):
                ex_label = clean_line_text(m.group(1))
                span_start = m.start()
                span_len = len(m.group(0))
                n_rects = tp.count_rects(span_start, span_len)
                if n_rects > 0:
                    r = tp.get_rect(0)
                    top = round(ph - r[3], 2)
                    bbox = [round(r[0], 2), top, round(r[2], 2), round(ph - r[1], 2)]
                    top_percent = round(max(0.0, min(1.0, top / ph)), 4)
                    
                    num_match = re.search(r'\d+(?:\.\d+)?', ex_label)
                    ex_num_str = num_match.group(0) if num_match else "End"
                    
                    ex_obj = {
                        "id": f"exercise-{ex_num_str.lower()}-{page_num}",
                        "number": ex_num_str,
                        "title": ex_label.upper(),
                        "page": page_num,
                        "bbox": bbox,
                        "topPercent": top_percent,
                        "questions": []
                    }
                    exercises.append(ex_obj)
                    current_exercise = ex_obj

        # -------------------------------------------------------------
        # 4. Individual Questions under Exercises:
        # -------------------------------------------------------------
        if current_exercise and page_num >= current_exercise["page"]:
            lines = text.split('\n')
            for l_idx, line in enumerate(lines):
                l_str = line.strip()
                if not l_str:
                    continue

                # Maths/Science "1. Question..." or Physics/Chem "C.1 Question..."
                m_q = re.match(r'^(\d+)\.\s+([A-Za-z][^\n\r]*)$', l_str)
                if not m_q:
                    m_q = re.match(rf'^({ch_num}\.\d+)\.?\s+([A-Za-z][^\n\r]*)$', l_str)
                if not m_q and ch_in_part != ch_num:
                    m_q = re.match(rf'^({ch_in_part}\.\d+)\.?\s+([A-Za-z][^\n\r]*)$', l_str)

                if m_q:
                    q_num = m_q.group(1).strip()
                    q_text = clean_line_text(m_q.group(2))[:100]
                    
                    # Locate position
                    span_start = text.find(l_str)
                    if span_start != -1:
                        span_len = min(len(l_str), 20)
                        n_rects = tp.count_rects(span_start, span_len)
                        if n_rects > 0:
                            r = tp.get_rect(0)
                            top = round(ph - r[3], 2)
                            bbox = [round(r[0], 2), top, round(r[2], 2), round(ph - r[1], 2)]
                            top_percent = round(max(0.0, min(1.0, top / ph)), 4)
                            
                            q_obj = {
                                "id": f"q-{q_num}-p{page_num}",
                                "number": q_num,
                                "title": f"Question {q_num}: {q_text}",
                                "snippet": q_text,
                                "page": page_num,
                                "bbox": bbox,
                                "topPercent": top_percent
                            }
                            # Avoid duplicates within same exercise
                            if not any(eq["number"] == q_num and eq["page"] == page_num for eq in current_exercise["questions"]):
                                current_exercise["questions"].append(q_obj)
                                all_questions.append(q_obj)

    # Convert dicts to sorted lists
    sections = sorted(list(sections_dict.values()), key=lambda x: (x["page"], x["topPercent"]))
    examples = sorted(list(examples_dict.values()), key=lambda x: (x["page"], x["topPercent"]))
    exercises = sorted(exercises, key=lambda x: (x["page"], x["topPercent"]))
    all_questions = sorted(all_questions, key=lambda x: (x["page"], x["topPercent"]))

    return {
        "id": pdf_info["id"],
        "classLevel": pdf_info["classLevel"],
        "subject": pdf_info["subject"],
        "part": pdf_info["part"],
        "chapterNumber": pdf_info["chapterNumber"],
        "chapterTitle": pdf_info["chapterTitle"],
        "bookCode": pdf_info["bookCode"],
        "pdfPath": pdf_info["pdfPath"],
        "totalPages": total_pages,
        "pageWidth": round(first_page_w, 2),
        "pageHeight": round(first_page_h, 2),
        "totalSections": len(sections),
        "totalExamples": len(examples),
        "totalExercises": len(exercises),
        "totalQuestions": len(all_questions),
        "sections": sections,
        "examples": examples,
        "exercises": exercises,
        "questions": all_questions
    }


def generate_textbook_registry_ts(chapters: List[Dict[str, Any]], output_path: str):
    """Generate typed TypeScript registry `src/lib/textbookRegistry.ts`."""
    ts_code = """/**
 * Textbook Registry & Query API (NCERT STEM Platform)
 * Auto-generated by scripts/generate_textbook_index.py
 * Total Chapters Indexed: __TOTAL_CHAPTERS__
 */

import textbookPageMap from './textbookPageMap.json'

export interface BoundingBox {
  x0: number
  top: number
  x1: number
  bottom: number
}

export interface TextbookIndexItem {
  id: string
  number: string
  title: string
  snippet?: string
  page: number
  bbox: [number, number, number, number]
  topPercent: number
}

export interface TextbookExerciseItem extends TextbookIndexItem {
  questions: TextbookIndexItem[]
}

export interface TextbookChapter {
  id: string
  classLevel: number
  subject: string
  part: number
  chapterNumber: number
  chapterTitle: string
  bookCode: string
  pdfPath: string
  totalPages: number
  pageWidth: number
  pageHeight: number
  totalSections: number
  totalExamples: number
  totalExercises: number
  totalQuestions: number
  sections: TextbookIndexItem[]
  examples: TextbookIndexItem[]
  exercises: TextbookExerciseItem[]
  questions: TextbookIndexItem[]
}

export interface TextbookDatabase {
  metadata: {
    generatedAt: string
    totalChapters: number
    totalSections: number
    totalExamples: number
    totalExercises: number
    totalQuestions: number
  }
  chapters: TextbookChapter[]
}

const db = textbookPageMap as unknown as TextbookDatabase

/**
 * Get all indexed textbook chapters
 */
export function getAllChapters(): TextbookChapter[] {
  return db.chapters
}

/**
 * Lookup chapter by Class, Subject, and Chapter Number
 */
export function getChapter(
  classLevel: number | string,
  subject: string,
  chapterNumber: number | string
): TextbookChapter | undefined {
  const normClass = typeof classLevel === 'string' ? parseInt(classLevel.replace(/\\D/g, ''), 10) : classLevel
  const normCh = typeof chapterNumber === 'string' ? parseInt(chapterNumber.replace(/\\D/g, ''), 10) : chapterNumber
  const normSub = (subject || '').trim().toLowerCase()

  return db.chapters.find((c) => {
    if (c.classLevel !== normClass) return false
    if (c.chapterNumber !== normCh) return false
    const s = c.subject.toLowerCase()
    return s.includes(normSub) || normSub.includes(s)
  })
}

/**
 * Lookup chapter by PDF path (e.g. '/10/class10_maths/jemh101.pdf')
 */
export function getChapterByPdf(pdfPath: string): TextbookChapter | undefined {
  if (!pdfPath) return undefined
  const clean = pdfPath.trim().toLowerCase()
  return db.chapters.find((c) => c.pdfPath.toLowerCase().endsWith(clean) || clean.endsWith(c.pdfPath.toLowerCase()))
}

/**
 * Lookup chapter by unique chapter ID (e.g. 'cbse-class10-mathematics-ch1')
 */
export function getChapterById(id: string): TextbookChapter | undefined {
  return db.chapters.find((c) => c.id === id)
}

/**
 * Get all chapters for a given class and subject
 */
export function getChaptersBySubject(classLevel: number | string, subject: string): TextbookChapter[] {
  const normClass = typeof classLevel === 'string' ? parseInt(classLevel.replace(/\\D/g, ''), 10) : classLevel
  const normSub = (subject || '').trim().toLowerCase()

  return db.chapters.filter((c) => {
    if (c.classLevel !== normClass) return false
    const s = c.subject.toLowerCase()
    return s.includes(normSub) || normSub.includes(s)
  })
}

/**
 * Search the index for any section, example, or exercise matching query text
 */
export function searchIndex(
  query: string,
  filter?: { classLevel?: number; subject?: string; chapterNumber?: number }
): Array<{
  chapter: TextbookChapter
  item: TextbookIndexItem
  type: 'section' | 'example' | 'exercise' | 'question'
  relevance: number
}> {
  if (!query || !query.trim()) return []
  const qLower = query.toLowerCase().trim()
  const qTokens = qLower.split(/\\s+/).filter(Boolean)
  const results: Array<{
    chapter: TextbookChapter
    item: TextbookIndexItem
    type: 'section' | 'example' | 'exercise' | 'question'
    relevance: number
  }> = []

  const targetChapters = db.chapters.filter((c) => {
    if (filter?.classLevel && c.classLevel !== filter.classLevel) return false
    if (filter?.chapterNumber && c.chapterNumber !== filter.chapterNumber) return false
    if (filter?.subject) {
      const s = c.subject.toLowerCase()
      const fs = filter.subject.toLowerCase()
      if (!s.includes(fs) && !fs.includes(s)) return false
    }
    return true
  })

  for (const ch of targetChapters) {
    // Check sections
    for (const sec of ch.sections) {
      const text = `${sec.number} ${sec.title}`.toLowerCase()
      if (text.includes(qLower)) {
        results.push({ chapter: ch, item: sec, type: 'section', relevance: 1.0 })
      } else if (qTokens.every((tok) => text.includes(tok))) {
        results.push({ chapter: ch, item: sec, type: 'section', relevance: 0.8 })
      }
    }

    // Check examples
    for (const ex of ch.examples) {
      const text = `${ex.title} ${ex.snippet || ''}`.toLowerCase()
      if (text.includes(qLower)) {
        results.push({ chapter: ch, item: ex, type: 'example', relevance: 1.0 })
      } else if (qTokens.every((tok) => text.includes(tok))) {
        results.push({ chapter: ch, item: ex, type: 'example', relevance: 0.8 })
      }
    }

    // Check exercises
    for (const exer of ch.exercises) {
      const text = `${exer.title} ${exer.number}`.toLowerCase()
      if (text.includes(qLower)) {
        results.push({ chapter: ch, item: exer, type: 'exercise', relevance: 1.0 })
      }
      for (const q of exer.questions) {
        const qText = `${q.title} ${q.snippet || ''}`.toLowerCase()
        if (qText.includes(qLower)) {
          results.push({ chapter: ch, item: q, type: 'question', relevance: 0.9 })
        }
      }
    }
  }

  results.sort((a, b) => b.relevance - a.relevance)
  return results.slice(0, 50)
}
""".replace("__TOTAL_CHAPTERS__", str(len(chapters)))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ts_code)
    print(f"Generated {output_path}")


def generate_textbook_resolver_ts(output_path: str):
    """Generate typed auto-scroller and resolver engine `src/lib/textbookResolver.ts`."""
    ts_code = """/**
 * Textbook Resolver & Real-Time Auto-Scroll Engine (NCERT STEM Platform)
 * ----------------------------------------------------------------------
 * Resolves pedagogical teaching concepts, exercise numbers, examples, and topics
 * to exact PDF pages, bounding coordinates, and scroll targets in real time.
 */

import {
  TextbookChapter,
  TextbookIndexItem,
  getChapter,
  getChapterByPdf,
  getAllChapters,
} from './textbookRegistry'

export interface TextbookResolveQuery {
  classLevel?: number | string
  subject?: string
  category?: string
  chapterNumber?: number | string
  chapterOrderIndex?: number
  chapterTitle?: string
  topic?: string
  conceptTitle?: string
  conceptName?: string
  capsuleTitle?: string
  sectionNumber?: string
  exampleNumber?: string | number
  exerciseNumber?: string
  questionNumber?: string | number
  pdfPath?: string
  notesSourceFilename?: string
}

export interface ResolvedTextbookTarget {
  chapter: TextbookChapter
  matchedItem: TextbookIndexItem
  pdfPath: string
  page: number
  bbox: [number, number, number, number]
  topPercent: number
  scrollTargetY: number
  scrollUrl: string
  matchType:
    | 'exact_section'
    | 'exact_example'
    | 'exact_exercise'
    | 'exact_question'
    | 'fuzzy_topic'
    | 'proportional'
    | 'chapter_first_page'
  confidence: number
  label: string
}

export interface ResolveBookForChapterParams {
  classLevel?: number | string
  category?: string
  subject?: string
  chapterTitle?: string
  chapterOrderIndex?: number
  notesSourceFilename?: string
}

export interface ResolvedBook {
  id: string
  classLevel: number
  subject: string
  chapterNumber: number
  title: string
  chapterTitle: string
  pdfUrl: string
  totalPages: number
  pageWidth: number
  pageHeight: number
  bookCode: string
}

export interface ResolveTargetPageForLessonParams {
  conceptIndex?: number
  totalConcepts?: number
  moduleIndex?: number
  totalModules?: number
  totalPages: number
  conceptName?: string
  capsuleTitle?: string
  chapterNumber?: number
  classLevel?: number | string
  subject?: string
  pdfPath?: string
  content?: string
  extractedPage?: number
}

function normalizeStr(s: string): string {
  return (s || '')
    .toLowerCase()
    .replace(/[^a-z0-9]/g, ' ')
    .replace(/\\s+/g, ' ')
    .trim()
}

/**
 * Extracts the chapter number from a chapter title, order index, or filename.
 */
export function extractChapterNumber(input: string): number | null {
  if (!input) return null
  const chMatch = input.match(/chapter\\s*(\\d+)/i) || input.match(/\\bch\\.?\\s*(\\d+)/i)
  if (chMatch) return parseInt(chMatch[1], 10)

  const fnMatch = input.match(/([a-z]+)(\\d)(\\d\\d)/i)
  if (fnMatch) {
    const pt = parseInt(fnMatch[2], 10)
    const chInPt = parseInt(fnMatch[3], 10)
    if (pt === 2) {
      const code = fnMatch[1].toLowerCase()
      if (code === 'keph') return 7 + chInPt
      if (code === 'kech') return 6 + chInPt
      if (code === 'lemh') return 6 + chInPt
      if (code === 'iemh') return 8 + chInPt
    }
    return chInPt
  }

  const numMatch = input.match(/\\b(\\d+)\\b/)
  return numMatch ? parseInt(numMatch[1], 10) : null
}

/**
 * Resolves the authentic textbook chapter for a given curriculum chapter.
 */
export function resolveBookForChapter(params: ResolveBookForChapterParams): ResolvedBook | null {
  const { classLevel, category, subject, chapterTitle, chapterOrderIndex, notesSourceFilename } = params
  const targetSub = subject || category || ''

  // 1. Try resolving by notesSourceFilename
  if (notesSourceFilename) {
    const ch = getChapterByPdf(notesSourceFilename)
    if (ch) {
      return {
        id: ch.id,
        classLevel: ch.classLevel,
        subject: ch.subject,
        chapterNumber: ch.chapterNumber,
        title: ch.chapterTitle,
        chapterTitle: ch.chapterTitle,
        pdfUrl: ch.pdfPath,
        totalPages: ch.totalPages,
        pageWidth: ch.pageWidth,
        pageHeight: ch.pageHeight,
        bookCode: ch.bookCode,
      }
    }
  }

  // 2. Try resolving by classLevel + subject + chapterOrderIndex
  const chNum = chapterOrderIndex ?? (chapterTitle ? extractChapterNumber(chapterTitle) : undefined)
  if (classLevel && targetSub && chNum) {
    const ch = getChapter(classLevel, targetSub, chNum)
    if (ch) {
      return {
        id: ch.id,
        classLevel: ch.classLevel,
        subject: ch.subject,
        chapterNumber: ch.chapterNumber,
        title: ch.chapterTitle,
        chapterTitle: ch.chapterTitle,
        pdfUrl: ch.pdfPath,
        totalPages: ch.totalPages,
        pageWidth: ch.pageWidth,
        pageHeight: ch.pageHeight,
        bookCode: ch.bookCode,
      }
    }
  }

  // 3. Try resolving by chapterTitle fuzzy search
  if (chapterTitle) {
    const normSearch = normalizeStr(chapterTitle)
    const normCls = classLevel ? parseInt(String(classLevel).replace(/\\D/g, ''), 10) : undefined

    const match = getAllChapters().find((c) => {
      if (normCls && c.classLevel !== normCls) return false
      const cTitle = normalizeStr(c.chapterTitle)
      return cTitle.includes(normSearch) || normSearch.includes(cTitle)
    })

    if (match) {
      return {
        id: match.id,
        classLevel: match.classLevel,
        subject: match.subject,
        chapterNumber: match.chapterNumber,
        title: match.chapterTitle,
        chapterTitle: match.chapterTitle,
        pdfUrl: match.pdfPath,
        totalPages: match.totalPages,
        pageWidth: match.pageWidth,
        pageHeight: match.pageHeight,
        bookCode: match.bookCode,
      }
    }
  }

  return null
}

/**
 * Resolves a teacher's lesson topic or question into exact PDF page coordinates.
 */
export function resolveTextbookTarget(query: TextbookResolveQuery): ResolvedTextbookTarget | null {
  let chapter: TextbookChapter | undefined

  if (query.pdfPath || query.notesSourceFilename) {
    chapter = getChapterByPdf(query.pdfPath || query.notesSourceFilename || '')
  }

  const sub = query.subject || query.category
  const chNum = query.chapterNumber ?? query.chapterOrderIndex ?? (query.chapterTitle ? extractChapterNumber(query.chapterTitle) : undefined)

  if (!chapter && query.classLevel && sub && chNum) {
    chapter = getChapter(query.classLevel, sub, chNum)
  }

  if (!chapter && query.chapterTitle) {
    const normTitle = normalizeStr(query.chapterTitle)
    chapter = getAllChapters().find((c) => {
      const cTitle = normalizeStr(c.chapterTitle)
      return cTitle.includes(normTitle) || normTitle.includes(cTitle)
    })
  }

  if (!chapter) return null

  // 1. Exact Exercise Match
  if (query.exerciseNumber) {
    const exNumNorm = String(query.exerciseNumber).trim().toLowerCase().replace(/^exercise\\s*/i, '')
    const matchedEx = chapter.exercises.find((ex) => {
      const eNum = ex.number.toLowerCase()
      return eNum === exNumNorm || ex.title.toLowerCase().includes(exNumNorm)
    })

    if (matchedEx) {
      if (query.questionNumber) {
        const qNumStr = String(query.questionNumber).trim().replace(/^q(?:uestion)?\\s*/i, '')
        const matchedQ = matchedEx.questions.find((q) => q.number === qNumStr || q.title.includes(qNumStr))
        if (matchedQ) {
          return createResolvedTarget(chapter, matchedQ, 'exact_question', 1.0, `Exercise ${matchedEx.number} Q${matchedQ.number}`)
        }
      }
      return createResolvedTarget(chapter, matchedEx, 'exact_exercise', 0.98, matchedEx.title)
    }
  }

  // 2. Exact Example Match
  if (query.exampleNumber) {
    const exNumStr = String(query.exampleNumber).trim().replace(/^example\\s*/i, '')
    const matchedEx = chapter.examples.find((ex) => ex.number === exNumStr || ex.number.endsWith(`.${exNumStr}`))
    if (matchedEx) {
      return createResolvedTarget(chapter, matchedEx, 'exact_example', 0.99, `Example ${matchedEx.number}`)
    }
  }

  // 3. Exact Section Number Match
  if (query.sectionNumber) {
    const sNum = String(query.sectionNumber).trim()
    const matchedSec = chapter.sections.find((s) => s.number === sNum || s.number.endsWith(`.${sNum}`))
    if (matchedSec) {
      return createResolvedTarget(chapter, matchedSec, 'exact_section', 0.99, `${matchedSec.number} ${matchedSec.title}`)
    }
  }

  // 4. Topic / Concept Title Matching
  const topicQuery = query.conceptName || query.conceptTitle || query.topic || query.capsuleTitle
  if (topicQuery) {
    const normTopic = normalizeStr(topicQuery)
    const topicTokens = normTopic.split(' ').filter((t) => t.length > 2)

    let bestSection: TextbookIndexItem | null = null
    let bestSecScore = 0

    for (const sec of chapter.sections) {
      const normSec = normalizeStr(`${sec.number} ${sec.title}`)
      let score = 0
      if (normSec === normTopic || normSec.includes(normTopic) || normTopic.includes(normSec)) {
        score = 0.95
      } else {
        const matches = topicTokens.filter((tok) => normSec.includes(tok)).length
        if (topicTokens.length > 0) {
          score = (matches / topicTokens.length) * 0.8
        }
      }
      if (score > bestSecScore) {
        bestSecScore = score
        bestSection = sec
      }
    }

    if (bestSection && bestSecScore >= 0.45) {
      return createResolvedTarget(chapter, bestSection, 'fuzzy_topic', bestSecScore, `${bestSection.number} ${bestSection.title}`)
    }

    // Check examples for topic
    for (const ex of chapter.examples) {
      const normEx = normalizeStr(ex.title)
      if (normEx.includes(normTopic) || (topicTokens.length > 0 && topicTokens.every((tok) => normEx.includes(tok)))) {
        return createResolvedTarget(chapter, ex, 'exact_example', 0.88, ex.title)
      }
    }
  }

  // Fallback: Chapter Page 1
  const firstItem: TextbookIndexItem = chapter.sections[0] || {
    id: 'ch-start',
    number: '1',
    title: chapter.chapterTitle,
    page: 1,
    bbox: [0, 0, chapter.pageWidth, 50],
    topPercent: 0.0,
  }

  return createResolvedTarget(chapter, firstItem, 'chapter_first_page', 0.5, chapter.chapterTitle)
}

function createResolvedTarget(
  chapter: TextbookChapter,
  item: TextbookIndexItem,
  matchType: ResolvedTextbookTarget['matchType'],
  confidence: number,
  label: string
): ResolvedTextbookTarget {
  const topY = item.bbox ? item.bbox[1] : 0
  const topPercent = item.topPercent ?? (topY / (chapter.pageHeight || 720))
  const scrollTargetY = Math.round(topY)

  const scrollUrl = `${chapter.pdfPath}#page=${item.page}&view=FitH,${scrollTargetY}`

  return {
    chapter,
    matchedItem: item,
    pdfPath: chapter.pdfPath,
    page: item.page,
    bbox: item.bbox,
    topPercent,
    scrollTargetY,
    scrollUrl,
    matchType,
    confidence,
    label,
  }
}

/**
 * Automatically computes the target PDF page for a lesson concept.
 * Combines explicit page instructions, figure manifest extracted pages,
 * exact index lookup, and proportional interpolation fallback.
 */
export function resolveTargetPageForLesson(params: ResolveTargetPageForLessonParams): number {
  const {
    content,
    extractedPage,
    conceptIndex = 0,
    totalConcepts = 1,
    moduleIndex = 0,
    totalModules = 1,
    totalPages,
    conceptName,
    capsuleTitle,
    chapterNumber,
    classLevel,
    subject,
    pdfPath,
  } = params

  const effectiveTotalPages = Math.max(1, totalPages || 20)

  // 1. Explicit tutor directive: "Page 12", "page 5"
  if (content) {
    const pageMatch = content.match(/\\b(?:page|pg\\.?)\\s*(\\d+)\\b/i)
    if (pageMatch) {
      const parsed = parseInt(pageMatch[1], 10)
      if (!isNaN(parsed) && parsed > 0) {
        return Math.max(1, Math.min(effectiveTotalPages, parsed))
      }
    }
  }

  // 2. Direct extracted figure page from manifest
  if (typeof extractedPage === 'number' && extractedPage > 0) {
    return Math.max(1, Math.min(effectiveTotalPages, extractedPage))
  }

  // 3. Try exact match from textbook index
  if (conceptName || capsuleTitle) {
    const matched = resolveTextbookTarget({
      classLevel,
      subject,
      chapterNumber,
      conceptName,
      capsuleTitle,
      pdfPath,
    })
    if (matched && matched.confidence >= 0.6) {
      return Math.max(1, Math.min(effectiveTotalPages, matched.page))
    }
  }

  // 4. Mathematical concept progression interpolation across modules:
  const effTotalModules = Math.max(1, totalModules)
  const effTotalConcepts = Math.max(1, totalConcepts)
  const pagesPerModule = effectiveTotalPages / effTotalModules

  const basePage = moduleIndex === 0 ? 1 : Math.round(moduleIndex * pagesPerModule)
  const conceptOffset =
    effTotalConcepts > 1
      ? (conceptIndex / (effTotalConcepts - 1)) * Math.max(0, pagesPerModule - 1)
      : 0
  const targetPage = Math.round(basePage + conceptOffset)

  return Math.max(1, Math.min(effectiveTotalPages, targetPage))
}

/**
 * Computes the auto-scroll target when the teacher moves to a concept or stage in class.
 */
export function getAutoScrollTargetForLesson(params: {
  capsuleTitle?: string
  conceptName?: string
  classLevel?: number | string
  subject?: string
  chapterNumber?: number | string
}): ResolvedTextbookTarget | null {
  const { capsuleTitle, conceptName, classLevel, subject, chapterNumber } = params

  if (conceptName) {
    const res = resolveTextbookTarget({
      classLevel,
      subject,
      chapterNumber,
      conceptTitle: conceptName,
    })
    if (res && res.confidence >= 0.5) return res
  }

  if (capsuleTitle) {
    const res = resolveTextbookTarget({
      classLevel,
      subject,
      chapterNumber,
      topic: capsuleTitle,
    })
    if (res) return res
  }

  return resolveTextbookTarget({
    classLevel,
    subject,
    chapterNumber,
  })
}
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ts_code)
    print(f"Generated {output_path}")


def main():
    start_time = time.time()
    print("================================================================================")
    print("NCERT Automated Textbook Indexing Engine")
    print("Scanning all NCERT chapter PDFs in public/...")
    print("================================================================================")

    pdf_files = glob.glob('public/**/*.pdf', recursive=True)
    chapter_pdfs = [
        p for p in pdf_files
        if not p.endswith('_EM.pdf')
        and 'syllabus' not in p.lower()
        and 'p1x' not in p.lower()
        and 'secp1' not in p.lower()
    ]

    print(f"Discovered {len(chapter_pdfs)} NCERT chapter PDFs to index.\n")

    indexed_chapters = []
    total_sections = 0
    total_examples = 0
    total_exercises = 0
    total_questions = 0

    for idx, pdf_path in enumerate(sorted(chapter_pdfs)):
        meta = detect_chapter_metadata(pdf_path)
        print(f"[{idx+1}/{len(chapter_pdfs)}] Indexing Class {meta['classLevel']} {meta['subject']} Ch {meta['chapterNumber']}: {meta['filename']} ...", end="", flush=True)
        t0 = time.time()
        try:
            ch_data = scan_single_pdf(meta)
            indexed_chapters.append(ch_data)
            dt = time.time() - t0
            print(f" Done ({dt:.2f}s, {ch_data['totalPages']} pgs, {ch_data['totalSections']} secs, {ch_data['totalExamples']} exs, {ch_data['totalExercises']} exers, {ch_data['totalQuestions']} qs)")
            total_sections += ch_data['totalSections']
            total_examples += ch_data['totalExamples']
            total_exercises += ch_data['totalExercises']
            total_questions += ch_data['totalQuestions']
        except Exception as e:
            print(f" FAILED: {e}")

    database = {
        "metadata": {
            "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "totalChapters": len(indexed_chapters),
            "totalSections": total_sections,
            "totalExamples": total_examples,
            "totalExercises": total_exercises,
            "totalQuestions": total_questions,
            "engine": "pypdfium2-vector-scanner-v1"
        },
        "chapters": indexed_chapters
    }

    # 1. Output src/lib/textbookPageMap.json
    json_path = os.path.join("src", "lib", "textbookPageMap.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=2, ensure_ascii=False)
    print(f"\n[OK] Saved {json_path} ({os.path.getsize(json_path):,} bytes)")

    # 2. Output src/lib/textbookRegistry.ts
    registry_path = os.path.join("src", "lib", "textbookRegistry.ts")
    generate_textbook_registry_ts(indexed_chapters, registry_path)

    # 3. Output src/lib/textbookResolver.ts
    resolver_path = os.path.join("src", "lib", "textbookResolver.ts")
    generate_textbook_resolver_ts(resolver_path)

    total_time = time.time() - start_time
    print("================================================================================")
    print(f"Textbook Indexing Completed in {total_time:.1f}s")
    print(f"Chapters: {len(indexed_chapters)}")
    print(f"Sections: {total_sections}")
    print(f"Examples: {total_examples}")
    print(f"Exercises: {total_exercises}")
    print(f"Questions: {total_questions}")
    print("================================================================================")


if __name__ == '__main__':
    main()
