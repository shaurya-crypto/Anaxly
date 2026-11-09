import json

for ch, mod_idx in [(3, 6), (5, 5), (6, 5)]:
    with open(f'scripts/science_modules_ch{ch}.json', 'r', encoding='utf-8') as f:
        mods = json.load(f)
    m = mods[mod_idx]
    order = m.get('order_index')
    print(f'=== CH {ch} Mod {order} ===')
    lines = m.get('chapter_notes', '').split('\n')
    q_lines = [l for l in lines if l.startswith('#### Q') or l.startswith('### Q') or l.startswith('**Q')]
    print('Questions found in notes:', len(q_lines))
    for q in q_lines[:5]:
        print(' ', q)
