import json

with open('scripts/maths_pt2_modules/ch9_propositions.json', 'r', encoding='utf-8') as f:
    modules = json.load(f)

for m_idx, m in enumerate(modules):
    for w_idx, we in enumerate(m.get('worked_examples', [])):
        sol = we['solution']
        if "THEOREM / LOGICAL PRINCIPLE USED" not in sol and "FORMULA USED" not in sol and "THEOREM USED" not in sol:
            if m_idx == 0:
                th = "THEOREM / LOGICAL PRINCIPLE USED:\nPropositional Logic & Implication Invariant:\nA conditional statement 'If P, then Q' (P ⇒ Q) is false iff hypothesis P is true and conclusion Q is false."
            elif m_idx == 1:
                th = "THEOREM / LOGICAL PRINCIPLE USED:\nLaw of the Converse & Baudhāyana-Pythagoras Converse Theorem:\nThe converse of 'If P, then Q' is 'If Q, then P'. A theorem and its converse must be proved independently."
            elif m_idx == 2:
                th = "THEOREM / LOGICAL PRINCIPLE USED:\nGeometric Propositional Logic: Triangle Angle Bisector, Transversal Parallel Angles, Incenter Invariance."
            elif m_idx == 3:
                th = "THEOREM / LOGICAL PRINCIPLE USED:\nNumber-Theoretic Propositions: Prime Factorization, Divisibility Rules, Even/Odd Parity Invariants."
            else:
                th = "THEOREM / LOGICAL PRINCIPLE USED:\nCounterexample Disproof Principle & Polynomial Prime Non-existence (Euler / Goldbach Invariants)."
            
            sol = sol.replace("STEP-BY-STEP", f"{th}\n\nSTEP-BY-STEP")
            we['solution'] = sol

with open('scripts/maths_pt2_modules/ch9_propositions.json', 'w', encoding='utf-8') as f:
    json.dump(modules, f, indent=2, ensure_ascii=False)

print('Updated ch9_propositions.json successfully!')
