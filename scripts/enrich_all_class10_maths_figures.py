"""
enrich_all_class10_maths_figures.py
Enriches all 75 CBSE Class 10 Mathematics modules:
1. Attaches authentic high-precision diagram_svg, has_diagram=True, and graph_config to ALL 166 worked examples!
2. Populates visual_lesson_plan.concept_visuals for EVERY concept in key_concepts across all 75 modules!
3. Saves to scripts/maths_class10_modules/class10_maths_all_modules.json AND all 14 individual chapter files!
"""

import json
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

GENERATORS_DIR = os.path.join(CURRENT_DIR, "maths_class10_generators")
if GENERATORS_DIR not in sys.path:
    sys.path.append(GENERATORS_DIR)

import question_figure_builder as qfb
import svg_builder_class10 as sb

INPUT_JSON = os.path.join(CURRENT_DIR, "maths_class10_modules", "class10_maths_all_modules.json")

CHAPTER_FILES = [
    ("4f230f16-2470-4304-b7cd-4aeacbc51831", "scripts/maths_class10_modules/ch1_real_numbers.json"),
    ("71ff1091-5502-490c-bcc1-9624b699620f", "scripts/maths_class10_modules/ch2_polynomials.json"),
    ("990a1496-d88d-4665-8176-cd3cae0f488a", "scripts/maths_class10_modules/ch3_pair_of_linear_equations_in_two_variables.json"),
    ("f476ad58-425d-44d9-8150-4fc0c478834a", "scripts/maths_class10_modules/ch4_quadratic_equations.json"),
    ("916e8989-c22e-4dd9-97a0-f081e63fb77d", "scripts/maths_class10_modules/ch5_arithmetic_progressions.json"),
    ("5a8a4828-b882-4576-aeaf-fd3a7a2a8354", "scripts/maths_class10_modules/ch6_triangles.json"),
    ("12f22395-a321-4a9d-85af-cd50b0fdcafe", "scripts/maths_class10_modules/ch7_coordinate_geometry.json"),
    ("d854ea09-23bd-4eeb-b9b0-0b943b22ed76", "scripts/maths_class10_modules/ch8_introduction_to_trigonometry.json"),
    ("28268af8-3331-453a-ad5e-6add84c0c2ba", "scripts/maths_class10_modules/ch9_some_applications_of_trigonometry.json"),
    ("0eba841d-8fcd-4e01-bbc0-247a3f0a29c5", "scripts/maths_class10_modules/ch10_circles.json"),
    ("938ed126-df2f-438f-b6dc-8c7e1273ec24", "scripts/maths_class10_modules/ch11_areas_related_to_circles.json"),
    ("f30fffde-90c1-402d-83c3-7d2af0e9f423", "scripts/maths_class10_modules/ch12_surface_areas_and_volumes.json"),
    ("ee79fe72-f746-45c7-a36e-b5a11c82d479", "scripts/maths_class10_modules/ch13_statistics.json"),
    ("019778b1-dc6c-4660-9538-1940ec6cad64", "scripts/maths_class10_modules/ch14_probability.json"),
]

def main():
    print(f"Reading {INPUT_JSON}...")
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        modules = json.load(f)

    total_modules = len(modules)
    total_examples = 0
    enriched_examples = 0
    total_concept_visuals = 0

    print(f"Enriching {total_modules} modules with Question Figures & Concept Visuals...")

    for i, mod in enumerate(modules):
        mod_order = i + 1
        mod_title = mod.get("title", "")
        key_concepts = mod.get("key_concepts", [])
        
        # 1. Enrich Worked Examples
        worked_examples = mod.get("worked_examples", [])
        for j, ex in enumerate(worked_examples):
            total_examples += 1
            prob = ex.get("problem", "")
            
            # Generate figure
            svg, cfg, is_g = qfb.build_question_figure(mod_order, j, prob, mod_title)
            
            ex["has_diagram"] = True
            ex["diagram_svg"] = svg
            if cfg:
                ex["graph_config"] = cfg
            if is_g:
                ex["is_graph"] = True
            
            enriched_examples += 1

        # 2. Enrich Visual Lesson Plan & Concept Visuals
        vlp = mod.get("visual_lesson_plan")
        if not vlp or not isinstance(vlp, dict):
            vlp = {}
            mod["visual_lesson_plan"] = vlp

        # Ensure top-level module SVG exists
        if not vlp.get("svg"):
            vlp["svg"] = worked_examples[0]["diagram_svg"] if worked_examples else sb.build_cartesian_svg(title=mod_title)
            
        # Build concept_visuals for every concept
        enriched_cvs = []
        for c_idx, concept in enumerate(key_concepts):
            cv = qfb.build_concept_visual_for_topic(concept, mod_order, c_idx)
            enriched_cvs.append(cv)
            total_concept_visuals += 1

        vlp["concept_visuals"] = enriched_cvs

        # If module is graph-based, ensure diagram_type reflects it
        if any(cv.get("diagram_type") == "graph" for cv in enriched_cvs):
            vlp["diagram_type"] = "graph"
            graph_cv = next((cv for cv in enriched_cvs if cv.get("interactive_math_formula")), None)
            if graph_cv:
                vlp["interactive_math_formula"] = graph_cv["interactive_math_formula"]

    print("\n--- ENRICHMENT COMPLETE ---")
    print(f"Total Modules Processed: {total_modules}")
    print(f"Total Worked Examples Enriched: {enriched_examples} / {total_examples} (100%)")
    print(f"Total Concept Visuals Generated: {total_concept_visuals}")

    # 1. Save master file
    with open(INPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(modules, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved enriched modules to {INPUT_JSON}!")

    # 2. Split and save to each individual chapter JSON
    for curr_id, file_path in CHAPTER_FILES:
        ch_mods = [m for m in modules if m.get("curriculum_id") == curr_id]
        if ch_mods:
            full_path = os.path.join(CURRENT_DIR, "..", file_path) if not os.path.isabs(file_path) else file_path
            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(ch_mods, f, indent=2, ensure_ascii=False)
            print(f"  Saved {len(ch_mods)} modules to {file_path}")

if __name__ == "__main__":
    main()
