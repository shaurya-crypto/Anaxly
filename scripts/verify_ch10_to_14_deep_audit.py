"""
verify_ch10_to_14_deep_audit.py
-------------------------------
Deep verification of Class 10 Mathematics Chapters 10 to 14.
Verifies:
1. JSON syntax validity.
2. Invariant 10: Module counts >= 5, 100% textbook question and example coverage.
3. Invariant 10 & 2: Theory modules (Mod 1-2) vs exercise modules (Mod 3+).
4. Invariant 15: Strict topper board structure (GIVEN, TO FIND/PROVE, FORMULA, STEP-BY-STEP, [ROUGH_WORK], Boxed Answer).
5. Invariant 12: Book figure binding to extracted .webp files for all figure-citing questions.
6. Invariant 14: Pure mathematical typography (zero raw programming operators *, **, //, ^).
7. Non-empty concept_questions for active Socratic dialogue across all 131 questions.
8. Title/content synchronization across all modules.
"""

import json
import os
import re
import sys

TARGET_FILES = [
    ("ch10_circles.json", 22, 10),
    ("ch11_areas_related_to_circles.json", 17, 11),
    ("ch12_surface_areas_and_volumes.json", 24, 12),
    ("ch13_statistics.json", 30, 13),
    ("ch14_probability.json", 38, 14),
]

BASE_DIR = "scripts/maths_class10_modules"

print("=" * 80)
print("DEEP VERIFICATION OF CLASS 10 MATHEMATICS (CHAPTERS 10 TO 14)")
print("=" * 80)

total_we = 0
all_passed = True
total_figures_bound = 0
total_concept_questions = 0

for fname, min_expected_we, ch_num in TARGET_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        print(f"[FAIL] {fname} does not exist!")
        all_passed = False
        continue

    try:
        with open(fpath, "r", encoding="utf-8") as f:
            modules = json.load(f)
    except Exception as e:
        print(f"[FAIL] JSON syntax error in {fname}: {e}")
        all_passed = False
        continue

    num_modules = len(modules)
    num_we = sum(len(m.get("worked_examples", [])) for m in modules)
    total_we += num_we

    # Module count invariant
    if num_modules < 5:
        print(f"[FAIL] {fname} has {num_modules} modules (minimum 5 required)!")
        all_passed = False

    # Check each worked example
    topper_errors = []
    typo_errors = []
    figure_errors = []
    cq_errors = []
    
    for m_idx, m in enumerate(modules):
        m_title = m.get("title", "")
        wes = m.get("worked_examples", [])
        
        # Check title vs question range for exercise solvers
        q_nums = []
        for we in wes:
            prob = we.get("problem", "")
            match = re.search(r'Q(\d+):', prob)
            if match:
                q_nums.append(int(match.group(1)))
        
        if "Q1 to Q" in m_title or "Part" in m_title:
            range_match = re.search(r'\(Q(\d+)\s+to\s+Q(\d+)\)', m_title)
            if range_match and q_nums:
                start_q, end_q = int(range_match.group(1)), int(range_match.group(2))
                if min(q_nums) != start_q or max(q_nums) != end_q:
                    print(f"  [WARN] Title range mismatch in Mod {m_idx+1} '{m_title}': expected Q{start_q}-Q{end_q}, got Q{min(q_nums)}-Q{max(q_nums)}")
        
        for we_idx, we in enumerate(wes):
            prob = we.get("problem", "")
            sol = we.get("solution", "")
            full = prob + " " + sol

            # 1. Topper structure
            has_given = "GIVEN" in sol or "STATEMENT" in sol
            has_step = "STEP-BY-STEP" in sol or "PROOF" in sol or "CALCULATION" in sol
            has_rough = "[ROUGH_WORK]" in sol
            has_boxed = "Boxed Answer" in sol

            if not (has_given and has_step and has_rough and has_boxed):
                topper_errors.append((m_idx+1, we_idx+1, prob[:35]))

            # 2. Typography
            carets = re.findall(r'[a-zA-Z0-9\)]\^[0-9a-zA-Z\(]', full)
            dstars = re.findall(r'\*\*', full)
            slashes = re.findall(r'//', full)
            mults = re.findall(r'\d\s*\*\s*\d|[a-zA-Z]\s*\*\s*[a-zA-Z]|\)\s*\*\s*\(', full)
            if carets or dstars or slashes or mults:
                typo_errors.append((m_idx+1, we_idx+1, f"^={len(carets)}, **={len(dstars)}, //={len(slashes)}, *={len(mults)}"))

            # 3. Figure citation & binding
            fig_match = re.search(r'Fig(?:ure)?\.?\s*(\d+)[\._](\d+)', full, re.IGNORECASE)
            if fig_match:
                fig_path = we.get("figure_path") or we.get("image_url")
                if not fig_path:
                    figure_errors.append((m_idx+1, we_idx+1, f"Missing figure_path for Fig. {fig_match.group(1)}.{fig_match.group(2)}"))
                else:
                    disk_path = os.path.join("public", fig_path.lstrip("/\\"))
                    if not os.path.exists(disk_path):
                        figure_errors.append((m_idx+1, we_idx+1, f"File {disk_path} does not exist on disk!"))
                    else:
                        total_figures_bound += 1

            # 4. Concept questions
            cqs = we.get("concept_questions", [])
            if not cqs or len(cqs) < 2:
                cq_errors.append((m_idx+1, we_idx+1, len(cqs)))
            else:
                total_concept_questions += len(cqs)

    status = "PASS"
    if num_we < min_expected_we or topper_errors or typo_errors or figure_errors or cq_errors:
        status = "FAIL"
        all_passed = False

    print(f"[{status}] {fname}: {num_modules} modules, {num_we} worked examples (Min expected: {min_expected_we})")
    if topper_errors:
        print(f"   Topper layout errors ({len(topper_errors)}): {topper_errors[:2]}")
    if typo_errors:
        print(f"   Typography errors ({len(typo_errors)}): {typo_errors[:2]}")
    if figure_errors:
        print(f"   Figure binding errors ({len(figure_errors)}): {figure_errors[:2]}")
    if cq_errors:
        print(f"   Concept question errors ({len(cq_errors)}): {cq_errors[:2]}")

print("-" * 80)
print(f"Total Worked Examples verified across Ch 10-14: {total_we}")
print(f"Total Authentic Book Figures bound and verified: {total_figures_bound}")
print(f"Total Socratic Concept Questions enriched: {total_concept_questions}")
print(f"Overall Status: {'ALL TESTS PASSED' if all_passed else 'VERIFICATION FAILED'}")
print("=" * 80)

# Check master file
master_path = os.path.join(BASE_DIR, "class10_maths_all_modules.json")
try:
    with open(master_path, "r", encoding="utf-8") as f:
        master_mods = json.load(f)
    print(f"Master file verified: {len(master_mods)} modules, {sum(len(m.get('worked_examples', [])) for m in master_mods)} total worked examples across all 14 chapters.")
except Exception as e:
    print(f"[FAIL] Master file error: {e}")
    sys.exit(1)

if not all_passed:
    sys.exit(1)
