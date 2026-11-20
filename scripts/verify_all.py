import json
import re

def verify_all():
    print("================== VERIFICATION REPORT ==================")
    grand_we = 0
    grand_cq = 0
    for ch in [11, 12, 13, 14]:
        with open(f"scripts/physics_class11_modules/physics_modules_ch{ch}.json", "r", encoding="utf-8") as f:
            mods = json.load(f)
        ch_we = sum(len(m.get("worked_examples", [])) for m in mods)
        ch_cq = sum(len(m.get("concept_questions", [])) for m in mods)
        grand_we += ch_we
        grand_cq += ch_cq
        print(f"Chapter {ch}:")
        for idx, m in enumerate(mods):
            we = len(m.get("worked_examples", []))
            cq = len(m.get("concept_questions", []))
            # Verify fields and typography
            assert "^" not in m.get("title", ""), f"Raw caret in title of Ch {ch} M{idx+1}"
            for w in m.get("worked_examples", []):
                for k in ["problem", "given", "formula", "calculation", "rough_work", "finalAnswer", "unit", "textbook_reference", "image_search_query"]:
                    assert k in w, f"Missing {k} in Ch {ch} M{idx+1}"
                    val = str(w[k])
                    assert "^" not in val, f"Raw caret in worked_example.{k} of Ch {ch} M{idx+1}: {val}"
                    assert not re.search(r'\d\s*\*\s*\d', val), f"Raw asterisk in worked_example.{k} of Ch {ch} M{idx+1}: {val}"
                    if "http" not in val:
                        assert "//" not in val, f"Raw double slash in worked_example.{k} of Ch {ch} M{idx+1}: {val}"
            for q in m.get("concept_questions", []):
                for k in ["question", "options", "explanation", "textbook_reference", "image_search_query"]:
                    assert k in q, f"Missing {k} in Ch {ch} M{idx+1}"
                assert "correctAnswer" in q or "correct_answer" in q, f"Missing answer in Ch {ch} M{idx+1}"
                assert "^" not in q.get("question", ""), f"Raw caret in question of Ch {ch} M{idx+1}"
                assert "^" not in q.get("explanation", ""), f"Raw caret in explanation of Ch {ch} M{idx+1}"
                for opt in q.get("options", []):
                    assert "^" not in opt, f"Raw caret in option of Ch {ch} M{idx+1}: {opt}"
            print(f"  M{idx+1} [Order {m['order_index']}]: {m['title'][:55]}... | WE: {we} | CQ: {cq} | Total: {we+cq}")
        print(f"Chapter {ch} Subtotal: {ch_we} Worked Examples + {ch_cq} Concept Questions = {ch_we + ch_cq} Problems\n")

    print(f"GRAND TOTAL (Chapters 11-14): {grand_we} Worked Examples + {grand_cq} Concept Questions = {grand_we + grand_cq} Problems")

    # Verify merged file
    with open("scripts/physics_class11_modules/class11_physics_pt2_modules.json", "r", encoding="utf-8") as f:
        pt2 = json.load(f)
    print(f"Merged class11_physics_pt2_modules.json has {len(pt2)} total modules across Class 11 Physics Part 2.")
    for m in pt2:
        if 65 <= m["order_index"] <= 88:
            assert "^" not in m.get("title", ""), f"Raw caret in pt2 title {m['order_index']}"
            for w in m.get("worked_examples", []):
                for k in ["formula", "calculation", "rough_work", "finalAnswer"]:
                    assert "^" not in str(w.get(k, "")), f"Raw caret in pt2 worked_example.{k} {m['order_index']}"
    print("ALL RIGOROUS INTEGRITY & TYPOGRAPHY ASSERTIONS PASSED PERFECTLY!")

if __name__ == "__main__":
    verify_all()
