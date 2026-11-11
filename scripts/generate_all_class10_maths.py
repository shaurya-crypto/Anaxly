"""
Master Batch Compilation & Invariant Verification Script for Class 10 Mathematics (NCERT CBSE)
Aggregates all 14 chapter generators, validates strict adherence to Invariant 10,
and compiles production-ready JSON payloads for Supabase ingestion.
"""

import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), "maths_class10_generators"))

from ch1_real_numbers import get_ch1_modules
from ch2_polynomials import get_ch2_modules
from ch3_linear_equations import get_ch3_modules
from ch4_quadratic_equations import get_ch4_modules
from ch5_arithmetic_progressions import get_ch5_modules
from ch6_triangles import get_ch6_modules
from ch7_coordinate_geometry import get_ch7_modules
from ch8_trigonometry import get_ch8_modules
from ch9_applications_trigonometry import get_ch9_modules
from ch10_circles import get_ch10_modules
from ch11_areas_related_circles import get_ch11_modules
from ch12_surface_areas_volumes import get_ch12_modules
from ch13_statistics import get_ch13_modules
from ch14_probability import get_ch14_modules

CHAPTER_GENERATORS = [
    (1, "Real Numbers", "4f230f16-2470-4304-b7cd-4aeacbc51831", get_ch1_modules),
    (2, "Polynomials", "71ff1091-5502-490c-bcc1-9624b699620f", get_ch2_modules),
    (3, "Pair of Linear Equations in Two Variables", "990a1496-d88d-4665-8176-cd3cae0f488a", get_ch3_modules),
    (4, "Quadratic Equations", "f476ad58-425d-44d9-8150-4fc0c478834a", get_ch4_modules),
    (5, "Arithmetic Progressions", "916e8989-c22e-4dd9-97a0-f081e63fb77d", get_ch5_modules),
    (6, "Triangles", "5a8a4828-b882-4576-aeaf-fd3a7a2a8354", get_ch6_modules),
    (7, "Coordinate Geometry", "12f22395-a321-4a9d-85af-cd50b0fdcafe", get_ch7_modules),
    (8, "Introduction to Trigonometry", "d854ea09-23bd-4eeb-b9b0-0b943b22ed76", get_ch8_modules),
    (9, "Some Applications of Trigonometry", "28268af8-3331-453a-ad5e-6add84c0c2ba", get_ch9_modules),
    (10, "Circles", "0eba841d-8fcd-4e01-bbc0-247a3f0a29c5", get_ch10_modules),
    (11, "Areas Related to Circles", "938ed126-df2f-438f-b6dc-8c7e1273ec24", get_ch11_modules),
    (12, "Surface Areas and Volumes", "f30fffde-90c1-402d-83c3-7d2af0e9f423", get_ch12_modules),
    (13, "Statistics", "ee79fe72-f746-45c7-a36e-b5a11c82d479", get_ch13_modules),
    (14, "Probability", "019778b1-dc6c-4660-9538-1940ec6cad64", get_ch14_modules),
]

def main():
    output_dir = os.path.join(os.path.dirname(__file__), "maths_class10_modules")
    os.makedirs(output_dir, exist_ok=True)
    
    all_compiled_modules = []
    total_worked_examples = 0
    total_key_concepts = 0
    total_svgs = 0
    
    print("=" * 80)
    print("STARTING CLASS 10 MATHEMATICS FULL CURRICULUM BATCH SYNTHESIS")
    print("Target: 14 Chapters | CBSE NCERT | Strict Invariant 10 Compliance")
    print("=" * 80)
    
    for ch_num, ch_title, curriculum_id, gen_fn in CHAPTER_GENERATORS:
        print(f"\nProcessing Chapter {ch_num}: {ch_title}...")
        modules = gen_fn()
        
        # Invariant 10 Verification: Minimum 5 to 8 modules
        if len(modules) < 5:
            raise ValueError(f"FATAL: Chapter {ch_num} has only {len(modules)} modules! Invariant 10 requires >= 5 modules.")
            
        ch_examples = 0
        ch_concepts = 0
        ch_svgs = 0
        
        for idx, mod in enumerate(modules, start=1):
            assert mod["curriculum_id"] == curriculum_id, f"Curriculum ID mismatch in Ch {ch_num} Mod {idx}"
            assert mod["order_index"] == idx, f"Order index error in Ch {ch_num} Mod {idx}"
            assert mod["class_level"] == "Class 10", f"Class level error in Ch {ch_num} Mod {idx}"
            assert mod["board"] == "CBSE", f"Board error in Ch {ch_num} Mod {idx}"
            assert len(mod["key_concepts"]) >= 3, f"Insufficient key concepts in Ch {ch_num} Mod {idx}"
            assert len(mod["worked_examples"]) >= 1, f"Insufficient worked examples in Ch {ch_num} Mod {idx}"
            
            # Check SVG in visual_lesson_plan
            vlp = mod.get("visual_lesson_plan", {})
            svg_content = vlp.get("svg") or vlp.get("diagram_svg") or ""
            if "<svg" in svg_content and "</svg>" in svg_content:
                # Ensure canonical 'svg' key exists
                vlp["svg"] = svg_content
                ch_svgs += 1
            else:
                raise ValueError(f"Missing or invalid vector SVG in Ch {ch_num} Mod {idx}")
                
            ch_examples += len(mod["worked_examples"])
            ch_concepts += len(mod["key_concepts"])
            
            all_compiled_modules.append(mod)
            
        total_worked_examples += ch_examples
        total_key_concepts += ch_concepts
        total_svgs += ch_svgs
        
        # Save individual chapter JSON
        ch_filename = os.path.join(output_dir, f"ch{ch_num}_{ch_title.lower().replace(' ', '_')}.json")
        with open(ch_filename, "w", encoding="utf-8") as f:
            json.dump(modules, f, indent=2, ensure_ascii=False)
            
        print(f"  ✓ Verified: {len(modules)} Modules | {ch_examples} Worked Examples | {ch_concepts} Key Concepts | {ch_svgs} Vector SVGs")
        print(f"  ✓ Saved to: {os.path.basename(ch_filename)}")

    # Save master aggregation JSON
    master_file = os.path.join(output_dir, "class10_maths_all_modules.json")
    with open(master_file, "w", encoding="utf-8") as f:
        json.dump(all_compiled_modules, f, indent=2, ensure_ascii=False)
        
    print("\n" + "=" * 80)
    print("BATCH SYNTHESIS & AUDIT SUCCESSFUL!")
    print(f"Total Chapters Processed: {len(CHAPTER_GENERATORS)}")
    print(f"Total Modules Generated: {len(all_compiled_modules)} (Average: {len(all_compiled_modules)/len(CHAPTER_GENERATORS):.1f} per chapter)")
    print(f"Total Worked Examples (Topper Board Layouts): {total_worked_examples}")
    print(f"Total Key Theoretical Concepts: {total_key_concepts}")
    print(f"Total High-Precision Vector SVGs: {total_svgs}")
    print(f"Master Payload Saved: {master_file} ({os.path.getsize(master_file)/1024:.1f} KB)")
    print("=" * 80)

if __name__ == "__main__":
    main()
