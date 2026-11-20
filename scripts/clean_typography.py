import json
import re

SUPERSCRIPTS = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
    'n': 'ⁿ', 'i': 'ⁱ', 't': 'ᵗ', 'x': 'ˣ', 'y': 'ʸ', 'k': 'ᵏ',
    'm': 'ᵐ', 'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ',
    'r': 'ʳ', 's': 'ˢ', 'v': 'ᵛ', 'o': 'ᵒ', 'p': 'ᵖ', 'T': 'ᵀ',
    '.': '·', '·': '·', '/': 'ᐟ', 'γ': 'ᵞ', 'ω': 'ʷ'
}

def to_sup(s):
    return ''.join(SUPERSCRIPTS.get(c, c) for c in s)

def clean_non_latex_typography(text):
    if not isinstance(text, str):
        return text
    
    s = text
    # Specific known mathematical strings
    s = s.replace('(2.0)^1.4', '(2.0)¹·⁴')
    s = s.replace('(2)^1.4', '(2)¹·⁴')
    s = s.replace('2^1.4', '2¹·⁴')
    s = s.replace('2^(7/5)', '2⁷ᐟ⁵')
    s = s.replace('log₁₀(2^1.4)', 'log₁₀(2¹·⁴)')
    s = s.replace('10^0.4214', '10⁰·⁴²¹⁴')
    s = s.replace('8^1.4', '8¹·⁴')
    s = s.replace('(2³)^1.4', '(2³)¹·⁴')
    s = s.replace('2^4.2', '2⁴·²')
    s = s.replace('8^0.4', '8⁰·⁴')
    s = s.replace('(8)^1.4', '(8)¹·⁴')
    s = s.replace('(8)^(1.4 - 1.0)', '(8)⁰·⁴')
    s = s.replace('2^1.2', '2¹·²')
    s = s.replace('(2)^(0.4)', '(2)⁰·⁴')
    s = s.replace('(2)^0.4', '(2)⁰·⁴')
    s = s.replace('(10)^(1/3)', '(10)¹ᐟ³')
    s = s.replace('10^(1/3)', '10¹ᐟ³')
    s = s.replace('d^2', 'd²')
    s = s.replace('v_rms^2', 'v_rms²')
    s = s.replace('sin^3 ωt', 'sin³ ωt')
    s = s.replace('sin^3', 'sin³')
    s = s.replace('exp(-ω^2 t^2)', 'exp(-ω² t²)')
    s = s.replace('-ω^2 t^2', '-ω² t²')
    s = s.replace('ω^2 t^2', 'ω² t²')
    s = s.replace('e^(-ωt)', 'e⁻ʷᵗ')
    s = s.replace('exp[-(x - vt)^2]', 'exp[-(x - vt)²]')
    s = s.replace('(x - vt)^2', '(x - vt)²')
    s = s.replace('-(x - vt)^2', '-(x - vt)²')
    s = s.replace('P₁ · V₁^γ = P₂ · V₂^γ => P₂ = P₁ · (V₁ / V₂)^γ', 'P₁ · V₁ᵞ = P₂ · V₂ᵞ ⇒ P₂ = P₁ · (V₁ / V₂)ᵞ')
    s = s.replace('P₁ · V₁^γ = P₂ · V₂^γ => P₂ / P₁ = (V₁ / V₂)^γ', 'P₁ · V₁ᵞ = P₂ · V₂ᵞ ⇒ P₂ / P₁ = (V₁ / V₂)ᵞ')
    s = s.replace('P₁ · V₁^γ = P₂ · V₂^γ', 'P₁ · V₁ᵞ = P₂ · V₂ᵞ')
    s = s.replace('(V₁ / V₂)^γ', '(V₁ / V₂)ᵞ')
    s = s.replace('(V₁/V₂)^γ', '(V₁/V₂)ᵞ')
    s = s.replace('T₁ · V₁^(γ-1) = T₂ · V₂^(γ-1) => T₂ = T₁ · (V₁ / V₂)^(γ-1)', 'T₁ · V₁ᵞ⁻¹ = T₂ · V₂ᵞ⁻¹ ⇒ T₂ = T₁ · (V₁ / V₂)ᵞ⁻¹')
    s = s.replace('T₁ · V₁^(γ-1) = T₂ · V₂^(γ-1) => T₂ / T₁ = (V₁ / V₂)^(γ-1)', 'T₁ · V₁ᵞ⁻¹ = T₂ · V₂ᵞ⁻¹ ⇒ T₂ / T₁ = (V₁ / V₂)ᵞ⁻¹')
    s = s.replace('T₁ · V₁^(γ-1) = T₂ · V₂^(γ-1)', 'T₁ · V₁ᵞ⁻¹ = T₂ · V₂ᵞ⁻¹')
    s = s.replace('P·V^γ = constant', 'P · Vᵞ = constant')
    s = s.replace('P·V^γ = const', 'P · Vᵞ = const')
    s = s.replace('(dP/dV)_adia = -γ·P/V', '(dP/dV)ₐ𝒹ᵢₐ = -γ · P / V')
    s = s.replace('(V₁/V₂)^(γ-1)', '(V₁/V₂)ᵞ⁻¹')
    s = s.replace('(V₁ / V₂)^(γ-1)', '(V₁ / V₂)ᵞ⁻¹')
    s = s.replace('^(3/2)', '³ᐟ²')
    s = s.replace('^(1/2)', '¹ᐟ²')
    s = s.replace('^(1/4)', '¹ᐟ⁴')
    s = s.replace('^(1/3)', '¹ᐟ³')
    s = s.replace('(1/3 ρ', '(⅓ ρ')
    s = s.replace('1/3 ρ', '⅓ ρ')
    s = s.replace('1/4)(3 sin', '¼) · (3 sin')
    s = s.replace('(1/4)(3 sin', '¼ · (3 sin')
    s = s.replace('(3/4) sin', '¾ · sin')
    s = s.replace('(1/4) sin', '¼ · sin')

    # Regex pass for parenthesized powers: ^(...)
    s = re.sub(r'\^(\([^\)]+\))', lambda m: to_sup(m.group(1)), s)
    # Regex pass for signed / numeric / single char powers: ^-11, ^2, ^γ, etc.
    s = re.sub(r'\^([0-9\+\-γa-zA-Z\.]+)', lambda m: to_sup(m.group(1)), s)
    # Strip any remaining stray carets
    s = s.replace('^', '')
    return s

def clean_obj(obj, is_chapter_notes=False):
    if is_chapter_notes:
        return obj
    if isinstance(obj, str):
        return clean_non_latex_typography(obj)
    elif isinstance(obj, list):
        return [clean_obj(x, is_chapter_notes) for x in obj]
    elif isinstance(obj, dict):
        return {k: clean_obj(v, is_chapter_notes=(k == 'chapter_notes')) for k, v in obj.items()}
    return obj

def run():
    all_ch = {}
    for ch in [11, 12, 13, 14]:
        fname = f'scripts/physics_class11_modules/physics_modules_ch{ch}.json'
        with open(fname, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cleaned = clean_obj(data)
        all_ch[ch] = cleaned
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(cleaned, f, indent=2, ensure_ascii=False)
        print(f"Processed Ch {ch}")

    # Synchronize class11_physics_pt2_modules.json
    with open('scripts/physics_class11_modules/class11_physics_pt2_modules.json', 'r', encoding='utf-8') as f:
        pt2 = json.load(f)
    new_pt2 = []
    for m in pt2:
        oid = m['order_index']
        if 65 <= oid <= 70:
            new_pt2.append(next(x for x in all_ch[11] if x['order_index'] == oid))
        elif 71 <= oid <= 76:
            new_pt2.append(next(x for x in all_ch[12] if x['order_index'] == oid))
        elif 77 <= oid <= 82:
            new_pt2.append(next(x for x in all_ch[13] if x['order_index'] == oid))
        elif 83 <= oid <= 88:
            new_pt2.append(next(x for x in all_ch[14] if x['order_index'] == oid))
        else:
            new_pt2.append(m)
    with open('scripts/physics_class11_modules/class11_physics_pt2_modules.json', 'w', encoding='utf-8') as f:
        json.dump(new_pt2, f, indent=2, ensure_ascii=False)
    print("Master pt2 modules synchronized successfully!")

if __name__ == '__main__':
    run()
