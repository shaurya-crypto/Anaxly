import json

for ch in [3, 4, 5, 6]:
    with open(f'scripts/science_modules_ch{ch}.json', 'r', encoding='utf-8') as f:
        mods = json.load(f)
    print(f'*** Chapter {ch} ({len(mods)} modules) ***')
    for m in mods:
        plan = m.get('visual_lesson_plan') or {}
        cvs = plan.get('concept_visuals') or []
        wes = m.get('worked_examples') or []
        kcs = m.get('key_concepts') or []
        print(f"Mod {m['order_index']}: '{m['title']}'")
        print(f"   Key Concepts ({len(kcs)}):")
        for kc in kcs[:2]:
            print(f"     - {kc[:60]}...")
        print(f"   Visuals ({len(cvs)}):")
        for cv in cvs[:2]:
            print(f"     - img: {cv.get('image_url')} | q: {cv.get('image_query')}")
        print(f"   Worked Examples ({len(wes)}):")
        for we in wes[:1]:
            print(f"     - {we.get('problem')[:60]}...")
