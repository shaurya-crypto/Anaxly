import json
import os

all_ok = True
total_modules = 0
total_visuals = 0
total_examples = 0

for ch in range(7, 14):
    p = f"scripts/science_modules_ch{ch}.json"
    if not os.path.exists(p):
        print(f"FAILED: {p} missing!")
        all_ok = False
        continue
    with open(p, "r", encoding="utf-8") as f:
        modules = json.load(f)
    print(f"\n================ CHAPTER {ch} ({len(modules)} modules) ================")
    if len(modules) < 5 or len(modules) > 8:
        print(f"FAILED: Chapter {ch} has {len(modules)} modules (requires 5-8)")
        all_ok = False
    
    for m in modules:
        total_modules += 1
        order = m.get("order_index")
        title = m.get("title", "")
        kc = m.get("key_concepts", [])
        we = m.get("worked_examples", [])
        vlp = m.get("visual_lesson_plan", {})
        cv = vlp.get("concept_visuals", [])
        total_visuals += len(cv)
        total_examples += len(we)
        
        # Check counts
        if len(kc) < 5:
            print(f"  [Mod {order}] WARNING: key_concepts count {len(kc)} < 5")
            all_ok = False
        if len(cv) != len(kc):
            print(f"  [Mod {order}] WARNING: 1:1 visual mismatch: {len(cv)} visuals vs {len(kc)} concepts")
            all_ok = False
        if len(we) < 5:
            print(f"  [Mod {order}] WARNING: worked_examples count {len(we)} < 5")
            all_ok = False
            
        # Check image files
        for v in cv:
            img_url = v.get("image_url", "")
            if img_url.startswith("/extracted_diagrams/"):
                disk_path = "public" + img_url
                if not os.path.exists(disk_path):
                    print(f"  [Mod {order}] MISSING FILE on disk: {disk_path}")
                    all_ok = False

        print(f"  [Mod {order}] {title[:40]}... | Concepts: {len(kc)} | Visuals: {len(cv)} | Examples: {len(we)} (OK)")

print(f"\n=======================================================")
print(f"AUDIT SUMMARY: Total Modules: {total_modules} | Total Visuals: {total_visuals} | Total Examples: {total_examples}")
print(f"Overall status: {'ALL PASS (100% Validated)' if all_ok else 'FAILED SOME CHECKS'}")
print(f"=======================================================")
