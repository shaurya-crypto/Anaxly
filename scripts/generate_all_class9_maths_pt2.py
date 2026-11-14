import os
import json
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "maths_pt2_generators"))

from ch9_propositions import get_ch9_modules
from ch10_understanding_data import get_ch10_modules
from ch11_algorithms import get_ch11_modules
from ch12_quadrilaterals import get_ch12_modules
from ch13_linear_equations import get_ch13_modules
from ch14_surface_areas_volumes import get_ch14_modules

def main():
    os.makedirs("scripts/maths_pt2_modules", exist_ok=True)
    
    chapters = [
        (9, "ch9_propositions", get_ch9_modules),
        (10, "ch10_understanding_data", get_ch10_modules),
        (11, "ch11_algorithms", get_ch11_modules),
        (12, "ch12_quadrilaterals", get_ch12_modules),
        (13, "ch13_linear_equations", get_ch13_modules),
        (14, "ch14_surface_areas_volumes", get_ch14_modules),
    ]
    
    all_modules = []
    
    print("================================================================================")
    print("SYNTHESIZING CLASS 9 MATHEMATICS PART 2 (FINAL-TERM) MODULES")
    print("================================================================================")
    
    for ch_num, filename, get_fn in chapters:
        mods = get_fn()
        out_path = f"scripts/maths_pt2_modules/{filename}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(mods, f, indent=2, ensure_ascii=False)
        print(f"[+] Chapter {ch_num}: {len(mods)} modules written to {out_path}")
        all_modules.extend(mods)
        
    master_path = "scripts/class9_maths_pt2_all_modules.json"
    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(all_modules, f, indent=2, ensure_ascii=False)
        
    print(f"\n[✓] All {len(all_modules)} modules synthesized and saved to {master_path}!")

if __name__ == "__main__":
    main()
