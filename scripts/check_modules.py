import json

for ch in [7, 8]:
    with open(f"scripts/science_modules_ch{ch}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Chapter {ch}: {len(data)} modules")
    for m in data:
        n_c = len(m.get("key_concepts", []))
        n_v = len(m.get("visual_lesson_plan", {}).get("concept_visuals", []))
        n_w = len(m.get("worked_examples", []))
        print(f"  Mod {m.get('order_index')}: {m.get('title')[:45]} | concepts: {n_c} | visuals: {n_v} | examples: {n_w}")
