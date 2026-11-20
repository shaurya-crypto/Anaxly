import json
import glob
import os

target_files = [
    ("ch10_circles.json", 22),
    ("ch11_areas_related_to_circles.json", 16), # 16 or 17
    ("ch12_surface_areas_and_volumes.json", 24),
    ("ch13_statistics.json", 30),
    ("ch14_probability.json", 38),
]

base_dir = "scripts/maths_class10_modules"
print("=" * 70)
print("VERIFICATION OF CLASS 10 MATHEMATICS CHAPTERS 10 TO 14")
print("=" * 70)

total_target_examples = 0
all_valid = True

for fname, min_expected in target_files:
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"FAIL: {fname} does not exist!")
        all_valid = False
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        modules = json.load(f)
        
    num_modules = len(modules)
    num_we = sum(len(m.get("worked_examples", [])) for m in modules)
    total_target_examples += num_we
    
    # Check each worked example for topper structure
    topper_compliant = True
    missing_fields = []
    
    for m_idx, m in enumerate(modules):
        for we_idx, we in enumerate(m.get("worked_examples", [])):
            sol = we.get("solution", "")
            prob = we.get("problem", "")
            
            has_given = "GIVEN" in sol or "STATEMENT" in sol
            has_step = "STEP-BY-STEP" in sol or "PROOF" in sol or "CALCULATION" in sol
            has_rough = "[ROUGH_WORK]" in sol
            has_boxed = "Boxed Answer" in sol
            
            if not (has_given and has_step and has_rough and has_boxed):
                topper_compliant = False
                missing_fields.append((m_idx+1, we_idx+1, we.get("problem", "")[:40]))
    
    status = "PASS" if num_we >= min_expected and topper_compliant else "WARN/FAIL"
    print(f"[{status}] {fname}: {num_modules} modules, {num_we} worked examples (Min expected: {min_expected})")
    if not topper_compliant:
        print(f"  Missing topper fields in: {missing_fields[:3]}")
        all_valid = False

print("-" * 70)
print(f"Total worked examples across Ch 10 - 14: {total_target_examples}")
print("=" * 70)

# Now update class10_maths_all_modules.json
print("\nUpdating class10_maths_all_modules.json...")
master_path = os.path.join(base_dir, "class10_maths_all_modules.json")

# Map of chapter files to their modules
updated_map = {}
for fname, _ in target_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        mods = json.load(f)
        curric_id = mods[0]["curriculum_id"]
        updated_map[curric_id] = mods

if os.path.exists(master_path):
    with open(master_path, "r", encoding="utf-8") as f:
        all_mods = json.load(f)
    
    new_all_mods = []
    curric_seen = set()
    for mod in all_mods:
        cid = mod.get("curriculum_id")
        if cid in updated_map:
            if cid not in curric_seen:
                new_all_mods.extend(updated_map[cid])
                curric_seen.add(cid)
        else:
            new_all_mods.append(mod)
            
    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(new_all_mods, f, indent=2, ensure_ascii=False)
        
    total_master_we = sum(len(m.get("worked_examples", [])) for m in new_all_mods)
    print(f"Successfully updated master file {master_path}:")
    print(f"  Total modules: {len(new_all_mods)}")
    print(f"  Total worked examples across entire Class 10 Maths: {total_master_we}")
