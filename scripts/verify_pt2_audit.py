import json
import glob
import os
import re

files = sorted(glob.glob('scripts/maths_pt2_modules/*.json'))

print(f"Auditing {len(files)} files in scripts/maths_pt2_modules/...\n")

total_modules_all = 0
total_we_all = 0
total_issues = 0

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        modules = json.load(f)
    
    total_modules_all += len(modules)
    ch_we = sum(len(m.get('worked_examples', [])) for m in modules)
    total_we_all += ch_we
    
    print(f"==================================================")
    print(f"FILE: {fname} | Modules: {len(modules)} | Total Worked Examples: {ch_we}")
    print(f"==================================================")
    
    for i, m in enumerate(modules):
        vlp = m.get('visual_lesson_plan', {})
        img_q = vlp.get('image_search_query', 'MISSING')
        align = vlp.get('textbook_alignment', 'MISSING')
        wes = m.get('worked_examples', [])
        print(f"  Module {i+1}: {m['title'][:55]}...")
        print(f"    - image_search_query: '{img_q}'")
        print(f"    - textbook_alignment: '{align}'")
        print(f"    - WE count: {len(wes)}")
        
        for j, we in enumerate(wes):
            prob = we.get('problem', '')
            sol = we.get('solution', '')
            
            # Check structure
            has_given = "GIVEN" in sol
            has_goal = ("TO FIND" in sol) or ("TO PROVE" in sol) or ("TO EVALUATE" in sol) or ("TO FORMULATE" in sol) or ("TO COMPUTE" in sol)
            has_formula = ("FORMULA" in sol) or ("THEOREM" in sol) or ("ALGORITHM" in sol) or ("PRINCIPLE" in sol)
            has_steps = ("STEP-BY-STEP" in sol) or ("PROOF" in sol)
            has_rough = "[ROUGH_WORK]" in sol
            has_boxed = "Boxed Answer:" in sol
            
            # Check raw operators
            has_raw_pow = "**" in sol
            has_raw_div = "//" in sol and not "http://" in sol and not "https://" in sol and not "// dictionary" in sol and not "// " in sol
            
            issues = []
            if not has_given: issues.append("Missing GIVEN")
            if not has_goal: issues.append("Missing TO FIND/PROVE")
            if not has_formula: issues.append("Missing FORMULA/THEOREM USED")
            if not has_steps: issues.append("Missing STEP-BY-STEP")
            if not has_rough: issues.append("Missing [ROUGH_WORK]")
            if not has_boxed: issues.append("Missing Boxed Answer")
            if has_raw_pow: issues.append("Found raw **")
            if has_raw_div: issues.append("Found raw //")
            
            if issues:
                total_issues += len(issues)
                print(f"      [!] WE {j+1} Issues: {', '.join(issues)}")

print(f"\n==================================================")
print(f"GRAND TOTALS: {total_modules_all} Modules across {len(files)} Chapters | {total_we_all} Comprehensive Worked Examples")
print(f"TOTAL SCHEMA ISSUES DETECTED: {total_issues}")
print(f"==================================================")
