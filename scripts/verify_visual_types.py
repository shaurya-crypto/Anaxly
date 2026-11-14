import json

for ch in [3, 4, 5, 6]:
    with open(f'scripts/science_modules_ch{ch}.json', 'r', encoding='utf-8') as f:
        mods = json.load(f)
    print(f'=== CH {ch} Visual Types ===')
    for m in mods:
        plan = m.get('visual_lesson_plan', {})
        cvs = plan.get('concept_visuals', [])
        types = set(c.get('diagram_type') for c in cvs)
        has_img_url = sum(1 for c in cvs if c.get('image_url'))
        has_query = sum(1 for c in cvs if c.get('image_query'))
        has_video = sum(1 for c in cvs if c.get('video_query'))
        order = m.get('order_index')
        print(f'  Mod {order}: types={types} | img_urls={has_img_url}/{len(cvs)} | img_queries={has_query}/{len(cvs)} | video_queries={has_video}/{len(cvs)}')
