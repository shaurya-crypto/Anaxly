"""
generate_all_class11_physics_pt1.py
Master Aggregator and Validator for CBSE Class 11 Physics Part 1 (Mid-Term Syllabus)
Compiles Chapters 1 to 7 into structured JSON files categorized strictly by Syllabus Term (Mid-Term Examination).
No start or end dates; pure term classification as per official CBSE syllabus.
"""

import sys
import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
GEN_DIR = os.path.join(CURRENT_DIR, "physics_class11_generators")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "physics_class11_modules")
os.makedirs(OUTPUT_DIR, exist_ok=True)

if GEN_DIR not in sys.path:
    sys.path.append(GEN_DIR)

import ch1_units_and_measurements as ch1
import ch2_motion_in_a_straight_line as ch2
import ch3_motion_in_a_plane as ch3
import ch4_laws_of_motion as ch4
import ch5_work_energy_power as ch5
import ch6_system_of_particles_rotational_motion as ch6
import ch7_gravitation as ch7

CHAPTER_METADATA = [
    {
        "chapter_num": 1,
        "curriculum_id": "c11_phy_ch01_units_measurements",
        "title": "Chapter 1: Units and Measurements",
        "description": "Comprehensive study of base SI units, dimensional analysis, and error propagation in measurement.",
        "category": "Physics",
        "difficulty_level": "intermediate",
        "estimated_duration_minutes": 275,
        "order_index": 1,
        "class_level": "Class 11",
        "board": "CBSE",
        "syllabus_term": "Mid-Term Examination",
        "unit_name": "Unit I: Physical World and Measurement",
        "weightage_marks": "23 Marks (Combined with Units II & III in Final Exam / 100% in Mid-Term)",
        "notes_source_filename": "keph101.pdf",
        "notes_summary": "Mid-Term master curriculum for Class 11 Physics Chapter 1: Units and Measurements, covering 7 base SI units, radian and steradian, error propagation, dimensional formulas, and NCERT exercise solutions.",
        "generator": ch1
    },
    {
        "chapter_num": 2,
        "curriculum_id": "c11_phy_ch02_motion_in_a_straight_line",
        "title": "Chapter 2: Motion in a Straight Line",
        "description": "Kinematics of rectilinear motion, position-time, velocity-time, acceleration-time graphs, calculus derivation of kinematic equations, and stopping distance.",
        "category": "Physics",
        "difficulty_level": "intermediate",
        "estimated_duration_minutes": 330,
        "order_index": 2,
        "class_level": "Class 11",
        "board": "CBSE",
        "syllabus_term": "Mid-Term Examination",
        "unit_name": "Unit II: Kinematics",
        "weightage_marks": "23 Marks (Combined with Units I & III in Final Exam / 100% in Mid-Term)",
        "notes_source_filename": "keph102.pdf",
        "notes_summary": "Mid-Term master curriculum for Class 11 Physics Chapter 2: Motion in a Straight Line, covering rectilinear kinematics, calculus derivations of motion equations, x-t/v-t/a-t plots, stopping distance, and NCERT exercise solutions.",
        "generator": ch2
    },
    {
        "chapter_num": 3,
        "curriculum_id": "c11_phy_ch03_motion_in_a_plane",
        "title": "Chapter 3: Motion in a Plane",
        "description": "Vectors, scalar and vector addition, relative velocity in 2D, projectile motion trajectory, and uniform circular motion.",
        "category": "Physics",
        "difficulty_level": "advanced",
        "estimated_duration_minutes": 385,
        "order_index": 3,
        "class_level": "Class 11",
        "board": "CBSE",
        "syllabus_term": "Mid-Term Examination",
        "unit_name": "Unit II: Kinematics",
        "weightage_marks": "23 Marks (Combined with Units I & III in Final Exam / 100% in Mid-Term)",
        "notes_source_filename": "keph103.pdf",
        "notes_summary": "Mid-Term master curriculum for Class 11 Physics Chapter 3: Motion in a Plane, covering vector operations, relative velocity, projectile motion mechanics, centripetal acceleration, and NCERT exercise solutions.",
        "generator": ch3
    },
    {
        "chapter_num": 4,
        "curriculum_id": "c11_phy_ch04_laws_of_motion",
        "title": "Chapter 4: Laws of Motion",
        "description": "Newton's laws of motion, momentum conservation, friction, inclined plane dynamics, circular motion, and banked curves.",
        "category": "Physics",
        "difficulty_level": "advanced",
        "estimated_duration_minutes": 385,
        "order_index": 4,
        "class_level": "Class 11",
        "board": "CBSE",
        "syllabus_term": "Mid-Term Examination",
        "unit_name": "Unit III: Laws of Motion",
        "weightage_marks": "23 Marks (Combined with Units I & II in Final Exam / 100% in Mid-Term)",
        "notes_source_filename": "keph104.pdf",
        "notes_summary": "Mid-Term master curriculum for Class 11 Physics Chapter 4: Laws of Motion, covering Newton's three laws, free body diagrams, friction mechanics, banked roads, and NCERT exercise solutions.",
        "generator": ch4
    },
    {
        "chapter_num": 5,
        "curriculum_id": "c11_phy_ch05_work_energy_power",
        "title": "Chapter 5: Work, Energy and Power",
        "description": "Scalar product, work by constant and variable forces, Work-Energy theorem, conservative forces, spring potential energy, vertical circle motion, power, and collisions.",
        "category": "Physics",
        "difficulty_level": "advanced",
        "estimated_duration_minutes": 335,
        "order_index": 5,
        "class_level": "Class 11",
        "board": "CBSE",
        "syllabus_term": "Mid-Term Examination",
        "unit_name": "Unit IV: Work, Energy and Power",
        "weightage_marks": "17 Marks (Combined with Units V & VI in Final Exam / 100% in Mid-Term)",
        "notes_source_filename": "keph105.pdf",
        "notes_summary": "Mid-Term master curriculum for Class 11 Physics Chapter 5: Work, Energy and Power, covering scalar product, Work-Energy Theorem, spring potential energy, vertical circles, 1D/2D collisions, and NCERT exercise solutions.",
        "generator": ch5
    },
    {
        "chapter_num": 6,
        "curriculum_id": "c11_phy_ch06_rotational_motion",
        "title": "Chapter 6: System of Particles and Rotational Motion",
        "description": "Center of mass, rotational kinematics, vector cross product, torque, angular momentum conservation, rigid body equilibrium, moments of inertia, and pure rolling motion.",
        "category": "Physics",
        "difficulty_level": "advanced",
        "estimated_duration_minutes": 390,
        "order_index": 6,
        "class_level": "Class 11",
        "board": "CBSE",
        "syllabus_term": "Mid-Term Examination",
        "unit_name": "Unit V: Motion of System of Particles and Rigid Body",
        "weightage_marks": "17 Marks (Combined with Units IV & VI in Final Exam / 100% in Mid-Term)",
        "notes_source_filename": "keph106.pdf",
        "notes_summary": "Mid-Term master curriculum for Class 11 Physics Chapter 6: System of Particles and Rotational Motion, covering center of mass, torque, angular momentum, axis theorems, rolling without slipping, and NCERT exercise solutions.",
        "generator": ch6
    },
    {
        "chapter_num": 7,
        "curriculum_id": "c11_phy_ch07_gravitation",
        "title": "Chapter 7: Gravitation",
        "description": "Kepler's laws, universal law of gravitation, Cavendish experiment, variation of g, gravitational potential energy, escape speed, earth satellites, and weightlessness.",
        "category": "Physics",
        "difficulty_level": "intermediate",
        "estimated_duration_minutes": 335,
        "order_index": 7,
        "class_level": "Class 11",
        "board": "CBSE",
        "syllabus_term": "Mid-Term Examination",
        "unit_name": "Unit VI: Gravitation",
        "weightage_marks": "17 Marks (Combined with Units IV & V in Final Exam / 100% in Mid-Term)",
        "notes_source_filename": "keph107.pdf",
        "notes_summary": "Mid-Term master curriculum for Class 11 Physics Chapter 7: Gravitation, covering Kepler's laws, Newton's law of gravitation, variation of g with altitude/depth/rotation, escape speed, orbital mechanics, and NCERT exercise solutions.",
        "generator": ch7
    }
]

def main():
    print("=" * 75)
    print("COMPILING CLASS 11 PHYSICS PART 1: MID-TERM EXAMINATION SYLLABUS")
    print("=" * 75)

    all_modules = []
    chapter_stats = []

    for meta in CHAPTER_METADATA:
        ch_num = meta["chapter_num"]
        print(f"\nProcessing Chapter {ch_num}: {meta['title']} ({meta['unit_name']})...")
        mods = meta["generator"].get_modules()
        print(f"-> Generated {len(mods)} modules.")

        # Attach curriculum_id, syllabus_term, unit_name to each module
        for m in mods:
            m["curriculum_id"] = meta["curriculum_id"]
            m["syllabus_term"] = meta["syllabus_term"]
            m["unit_name"] = meta["unit_name"]
            m["syllabus_pacing"] = f"{meta['syllabus_term']} | {meta['unit_name']}"
            # Remove any dates
            m.pop("start_date", None)
            m.pop("end_date", None)
            m.pop("target_completion_date", None)

            if "visual_lesson_plan" in m and isinstance(m["visual_lesson_plan"], dict):
                m["visual_lesson_plan"]["syllabus_term"] = meta["syllabus_term"]
                m["visual_lesson_plan"]["unit_name"] = meta["unit_name"]
                m["visual_lesson_plan"]["syllabus_pacing"] = f"{meta['syllabus_term']} | {meta['unit_name']}"
                m["visual_lesson_plan"].pop("start_date", None)
                m["visual_lesson_plan"].pop("end_date", None)
                m["visual_lesson_plan"].pop("target_completion_date", None)

        # Save individual chapter file
        ch_filepath = os.path.join(OUTPUT_DIR, f"physics_modules_ch{ch_num}.json")
        with open(ch_filepath, "w", encoding="utf-8") as f:
            json.dump(mods, f, indent=2, ensure_ascii=False)
        print(f"-> Saved {ch_filepath} ({os.path.getsize(ch_filepath):,} bytes)")

        all_modules.extend(mods)
        chapter_stats.append({
            "chapter": ch_num,
            "title": meta["title"],
            "unit": meta["unit_name"],
            "curriculum_id": meta["curriculum_id"],
            "module_count": len(mods),
            "syllabus_term": meta["syllabus_term"]
        })

    # Save master file with all 44 modules
    master_filepath = os.path.join(OUTPUT_DIR, "class11_physics_pt1_all_modules.json")
    with open(master_filepath, "w", encoding="utf-8") as f:
        json.dump(all_modules, f, indent=2, ensure_ascii=False)
    print(f"\nSaved MASTER FILE: {master_filepath} ({os.path.getsize(master_filepath):,} bytes)")

    # Save curriculum entries
    curriculums_data = []
    for meta in CHAPTER_METADATA:
        curriculums_data.append({
            "id": meta["curriculum_id"],
            "title": meta["title"],
            "description": meta["description"],
            "category": meta["category"],
            "difficulty_level": meta["difficulty_level"],
            "estimated_duration_minutes": meta["estimated_duration_minutes"],
            "is_published": True,
            "class_level": meta["class_level"],
            "order_index": meta["order_index"],
            "board": meta["board"],
            "syllabus_term": meta["syllabus_term"],
            "unit_name": meta["unit_name"],
            "weightage_marks": meta["weightage_marks"],
            "notes_source_filename": meta["notes_source_filename"],
            "notes_summary": meta["notes_summary"]
        })
    curr_filepath = os.path.join(OUTPUT_DIR, "class11_physics_pt1_curriculums.json")
    with open(curr_filepath, "w", encoding="utf-8") as f:
        json.dump(curriculums_data, f, indent=2, ensure_ascii=False)
    print(f"Saved CURRICULUMS METADATA: {curr_filepath} ({os.path.getsize(curr_filepath):,} bytes)")

    # -------------------------------------------------------------
    # INVARIANT VALIDATION SUITE
    # -------------------------------------------------------------
    print("\n" + "=" * 75)
    print("RUNNING PEDAGOGICAL INVARIANT & SYLLABUS TERM CHECKS")
    print("=" * 75)

    assert len(all_modules) == 44, f"Expected 44 modules, got {len(all_modules)}"
    print("✓ Total module count = 44")

    # Verify contiguous order_index 1..44
    indices = [m["order_index"] for m in all_modules]
    assert indices == list(range(1, 45)), f"Indices mismatch: {indices}"
    print("✓ Order indices are strictly continuous from 1 to 44 without gaps or duplicates")

    # Verify syllabus_term and pedagogical structures
    for m in all_modules:
        assert m.get("syllabus_term") == "Mid-Term Examination", f"Invalid term in mod {m['order_index']}"
        assert "subtopics" in m and len(m["subtopics"]) >= 4, f"Insufficient subtopics in mod {m['order_index']}"
        assert "key_concepts" in m and len(m["key_concepts"]) >= 3, f"Insufficient key concepts in mod {m['order_index']}"
        assert "success_criteria" in m and len(m["success_criteria"]) >= 3, f"Insufficient success criteria in mod {m['order_index']}"
        assert "worked_examples" in m and len(m["worked_examples"]) >= 1, f"Missing worked examples in mod {m['order_index']}"
        assert "visual_lesson_plan" in m, f"Missing visual plan in mod {m['order_index']}"
        assert "concept_visuals" in m["visual_lesson_plan"], f"Missing concept visuals in mod {m['order_index']}"
        assert "concept_questions" in m["visual_lesson_plan"], f"Missing concept questions in mod {m['order_index']}"
        assert "svg" in m["visual_lesson_plan"], f"Missing SVG in mod {m['order_index']}"

    print("✓ All 44 modules have verified syllabus_term, subtopics, success criteria, and visual lesson plans")

    # Print summary table
    print("\nCHAPTER SYLLABUS CLASSIFICATION:")
    print("-" * 75)
    for stat in chapter_stats:
        print(f"Ch {stat['chapter']:02d}: {stat['title'][:38]:<38} | {stat['unit']:<30} | {stat['module_count']} Mods | {stat['syllabus_term']}")
    print("-" * 75)
    print("ALL CHECKS PASSED WITH ZERO VIOLATIONS!")

if __name__ == "__main__":
    main()
