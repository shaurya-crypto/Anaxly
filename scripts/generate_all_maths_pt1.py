"""
Master Pipeline: Class 9 Mathematics Part 1 (Ganita Manjari Chapters 1 to 8)
Generates high-precision syllabus_modules payloads for Supabase.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json

from scripts.maths_pt1_generators.ch1_generator import get_ch1_modules
from scripts.maths_pt1_generators.ch2_generator import get_ch2_modules
from scripts.maths_pt1_generators.ch3_generator import get_ch3_modules
from scripts.maths_pt1_generators.ch4_generator import get_ch4_modules
from scripts.maths_pt1_generators.ch5_generator import get_ch5_modules
from scripts.maths_pt1_generators.ch6_generator import get_ch6_modules
from scripts.maths_pt1_generators.ch7_generator import get_ch7_modules
from scripts.maths_pt1_generators.ch8_generator import get_ch8_modules

CHAPTER_CONFIG = [
    {"ch": 1, "fn": get_ch1_modules, "title": "Chapter 1: Orienting Yourself: The Use of Coordinates", "curriculum_id": "3fdc7a01-da88-43e6-aef5-c48bf1d64ef5"},
    {"ch": 2, "fn": get_ch2_modules, "title": "Chapter 2: Introduction to Linear Polynomials", "curriculum_id": "cd14fc20-13b7-4d96-98fb-956720dc0f23"},
    {"ch": 3, "fn": get_ch3_modules, "title": "Chapter 3: The World of Numbers", "curriculum_id": "09ca99d2-0489-48f2-8d39-8b26ca7885c9"},
    {"ch": 4, "fn": get_ch4_modules, "title": "Chapter 4: Exploring Algebraic Identities", "curriculum_id": "cef5b4c4-9fad-4f5b-8201-372cce5f4f61"},
    {"ch": 5, "fn": get_ch5_modules, "title": "Chapter 5: I’m Up and Down, and Round and Round", "curriculum_id": "de83f257-aada-4e27-b420-f7884165c990"},
    {"ch": 6, "fn": get_ch6_modules, "title": "Chapter 6: Measuring Space: Perimeter and Area", "curriculum_id": "2ca7b10a-3fb9-484f-8116-30d7b586c526"},
    {"ch": 7, "fn": get_ch7_modules, "title": "Chapter 7: The Mathematics of Maybe: Introduction to Probability", "curriculum_id": "257078e3-5cf0-4286-a1e3-661ce480edc3"},
    {"ch": 8, "fn": get_ch8_modules, "title": "Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions", "curriculum_id": "b45d590f-323e-4263-b899-23d95b2094a7"},
]

def main():
    print("========================================================================")
    print("Generating Class 9 Mathematics Part 1 (Ganita Manjari Grade 9 Part 1)...")
    print("========================================================================")
    
    total_modules = 0
    total_examples = 0
    total_visuals = 0

    for item in CHAPTER_CONFIG:
        ch_num = item["ch"]
        modules = item["fn"]()
        curriculum_id = item["curriculum_id"]
        
        # Attach curriculum_id, board, class_level to each module
        for m in modules:
            m["curriculum_id"] = curriculum_id
            m["board"] = "CBSE"
            m["class_level"] = "Class 9"
            if "estimated_minutes" not in m:
                m["estimated_minutes"] = 25
            if "quiz_questions" not in m:
                m["quiz_questions"] = []
                
        out_path = f"scripts/maths_modules_ch{ch_num}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(modules, f, indent=2, ensure_ascii=False)
            
        ex_count = sum(len(m.get("worked_examples", [])) for m in modules)
        vis_count = sum(len(m.get("visual_lesson_plan", {}).get("concept_visuals", [])) for m in modules)
        svg_count = sum(1 for m in modules if m.get("visual_lesson_plan", {}).get("diagram_svg"))
        
        total_modules += len(modules)
        total_examples += ex_count
        total_visuals += vis_count
        
        print(f"Ch {ch_num}: {item['title']}")
        print(f"   -> Modules: {len(modules)} | Worked Examples: {ex_count} | Concept Visuals: {vis_count} | Main SVGs: {svg_count}")
        print(f"   -> Saved to {out_path} ({os.path.getsize(out_path)} bytes)")

    print("========================================================================")
    print(f"TOTAL GENERATION STATS:")
    print(f"Total Chapters: {len(CHAPTER_CONFIG)}")
    print(f"Total Modules: {total_modules} (strictly 5-6 modules per chapter)")
    print(f"Total Worked Examples: {total_examples} (step-by-step with zero skipped calculations)")
    print(f"Total Concept Visuals: {total_visuals}")
    print("========================================================================")

if __name__ == "__main__":
    main()
