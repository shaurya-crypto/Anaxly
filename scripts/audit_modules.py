import json

for ch in [3, 4, 5, 6]:
    with open(f'scripts/science_modules_ch{ch}.json', 'r', encoding='utf-8') as f:
        mods = json.load(f)
    print(f'=== CH {ch}: {len(mods)} modules ===')
    for m in mods:
        cv_count = len(m.get('visual_lesson_plan', {}).get('concept_visuals', []))
        kc_count = len(m.get('key_concepts', []))
        we_count = len(m.get('worked_examples', []))
        sub_count = len(m.get('subtopics', []))
        notes_len = len(m.get('chapter_notes', ''))
        prompt_len = len(m.get('ai_system_prompt_context', ''))
        order = m.get('order_index')
        title = m.get('title', '')[:40]
        print(f'  Mod {order}: {title} | KC: {kc_count} | CV: {cv_count} | WE: {we_count} | Sub: {sub_count} | Notes: {notes_len} | Prompt: {prompt_len}')
