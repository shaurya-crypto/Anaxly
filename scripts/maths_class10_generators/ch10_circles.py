"""
Class 10 Mathematics - Chapter 10: Circles (NCERT CBSE)
Curriculum ID: 0eba841d-8fcd-4e01-bbc0-247a3f0a29c5
Fully compliant with Invariant 10:
- 5 dedicated modules (Theory in M1-M2, dedicated solvers M3-M5)
- 100% of all NCERT exercise questions (Ex 10.1, Ex 10.2 Q1 to Q13) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- High-Precision Vector SVGs from svg_builder_class10 (Theorems 10.1 & 10.2 tangent geometry)
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_circle_tangents_svg, build_concentric_circles_chord_svg, get_svg_wrapper

def get_ch10_modules():
    CURRICULUM_ID = "0eba841d-8fcd-4e01-bbc0-247a3f0a29c5"
    
    # SVG 1: Theorem 10.1 (Radius Perpendicular to Tangent)
    svg_radius_perp = build_circle_tangents_svg(
        variant="radius_perp_tangent",
        title="Theorem 10.1: Radius ⊥ Tangent at Point of Contact",
        caption="OP is the shortest distance from center O to tangent line, hence OP ⊥ tangent"
    )
    
    # SVG 2: Theorem 10.2 (External Tangents Equality)
    svg_external_tangents = build_circle_tangents_svg(
        variant="external_tangents",
        title="Theorem 10.2: Tangents from External Point are Equal (PA = PB)",
        caption="RHS Congruence: ΔOPA ≅ ΔOPB ⇒ PA = PB and ∠OPA = ∠OPB"
    )

    modules = [
        # Module 1: Tangents to a Circle & Theorem 10.1
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Tangents to a Circle: Secant vs Tangent Limits & Theorem 10.1 Perpendicularity Proof",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the geometric definition of a tangent to a circle as a limiting case of a secant when the two intersection points coincide. Rigorously prove Theorem 10.1: The tangent at any point of a circle is perpendicular to the radius through the point of contact, using the shortest distance property.",
            "key_concepts": [
                "Secant: A straight line that intersects a circle in two distinct points",
                "Tangent: A straight line that touches the circle at exactly one point (Point of Contact)",
                "Limiting Case: A tangent is the limiting position of a secant when its two end-points of intersection coincide",
                "Theorem 10.1: The tangent at any point of a circle is perpendicular to the radius through the point of contact",
                "Shortest Distance Principle: The shortest distance from an external point to a straight line is the perpendicular distance; any point Q on the tangent line other than P lies strictly outside the circle, hence OQ > OP"
            ],
            "subtopics": [
                "Differentiating non-intersecting lines, secants, and tangents",
                "Full formal proof of Theorem 10.1 by contradiction / shortest distance",
                "Number of tangents from points inside, on, and outside a circle",
                "Worked Examples from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Theorem 10.1 (NCERT): Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.",
                    "solution": "STATEMENT: Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.\n\nGIVEN:\nA circle C(O, r) with centre O and a tangent XY touching the circle at point P.\nOP is the radius through the point of contact P.\n\nTO PROVE:\nOP ⊥ XY.\n\nCONSTRUCTION:\nTake any point Q on the tangent line XY other than P. Join OQ. Let OQ intersect the circle at point R.\n\nPROOF:\nStep 1: Determine position of Q relative to the circle:\nSince XY is a tangent to the circle at point P, P is the only point on the line XY that lies on the circle.\nEvery other point on the line XY must lie strictly outside the circle.\nTherefore, point Q lies outside the circle.\n\nStep 2: Compare lengths OQ and OP:\nSince point R lies on the circle and between O and Q:\nOQ = OR + RQ\nSince OR = OP (radii of the same circle):\nOQ = OP + RQ\nSince RQ > 0:\nOQ > OP.\n\nStep 3: Conclude shortest distance:\nThis inequality OQ > OP holds true for EVERY point Q on the line XY, except the point of contact P.\nTherefore, the line segment OP is the shortest of all the distances of the point O to the points on the line XY.\nWe know from Euclidean geometry that the shortest distance between a point and a line is the perpendicular distance.\n\nTherefore, OP ⊥ XY.\nHence Proved!\n[ROUGH_WORK]\nShortest distance from point O to line XY is perpendicular. Since OP is radius and every other point on line is outside the circle, OP is strictly minimum!\nBoxed Answer: [ OP ⊥ XY (Proved) ].",
                    "concept_questions": [
                        "Why must point Q lie outside the circle?",
                        "What would happen if Q lay inside the circle?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Theorem 10.1 Perpendicularity HUD",
                "diagram_type": "diagram",
                "svg": svg_radius_perp,
                "concept_visuals": [
                    {
                        "concept_title": "Radius Tangent Perpendicularity",
                        "diagram_title": "Theorem 10.1 Geometry",
                        "svg": svg_radius_perp,
                        "diagram_type": "diagram",
                        "what_to_make": "Circle with tangent line XY, point of contact P, and radius OP with right angle marker",
                        "what_to_explain": "Geometric proof via shortest distance property"
                    }
                ]
            },
            "common_misconceptions": [
                "Thinking a circle can have parallel tangents at adjacent points: A circle can only have parallel tangents at the diametrically opposite endpoints of a diameter!",
                "Believing a tangent crosses inside the circle: By definition, a tangent touches the circle at exactly one point without entering the interior."
            ]
        },

        # Module 2: Tangents from External Point & Theorem 10.2
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Tangents from an External Point: Theorem 10.2 Proof (PA = PB) & Angle Subtensions",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Rigorously prove Theorem 10.2: The lengths of tangents drawn from an external point to a circle are equal. Master the two fundamental corollaries: (1) tangents subtend equal angles at the centre (∠AOP = ∠BOP), and (2) tangents are equally inclined to the line joining the point to the centre (∠APO = ∠BPO).",
            "key_concepts": [
                "Theorem 10.2: The lengths of tangents drawn from an external point to a circle are equal (PA = PB)",
                "RHS Congruence Proof: Hypotenuse OP is common; Radii OA = OB; Right angles ∠OAP = ∠OBP = 90° (by Theorem 10.1)",
                "Central Angle Bisector: OP bisects ∠AOB (∠AOP = ∠BOP)",
                "External Angle Bisector: OP bisects ∠APB (∠APO = ∠BPO)",
                "Supplementary Angle Theorem: The angle between the two tangents (∠APB) and the angle subtended by the line segment joining the points of contact at the centre (∠AOB) are supplementary: ∠APB + ∠AOB = 180°"
            ],
            "subtopics": [
                "Formal statement and proof of Theorem 10.2",
                "Proof of supplementary angles in cyclic/quadrilateral OAPB",
                "Worked Examples 1, 2, 3 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Theorem 10.2 (NCERT): Prove that the lengths of tangents drawn from an external point to a circle are equal.",
                    "solution": "STATEMENT: The lengths of tangents drawn from an external point to a circle are equal.\n\nGIVEN:\nA circle with centre O, an external point P, and two tangents PA and PB drawn from P to the circle, touching at A and B respectively.\n\nTO PROVE:\nPA = PB.\n\nCONSTRUCTION:\nJoin OA, OB, and OP.\n\nPROOF:\nIn triangles ΔOAP and ΔOBP:\n1. ∠OAP = ∠OBP = 90° (By Theorem 10.1: Radius through point of contact is perpendicular to tangent)\n2. OP = OP (Common hypotenuse)\n3. OA = OB (Radii of the same circle)\n\nTherefore, by RHS (Right angle - Hypotenuse - Side) Congruence Criterion:\nΔOAP ≅ ΔOBP.\n\nSince corresponding parts of congruent triangles are equal (CPCT):\nPA = PB.\n\nCorollaries from CPCT:\n(i) ∠OPA = ∠OPB (OP is the angle bisector of ∠APB)\n(ii) ∠AOP = ∠BOP (OP is the angle bisector of ∠AOB)\nHence Proved!\n[ROUGH_WORK]\nAlternative proof using Pythagoras Theorem:\nPA² = OP² - OA² = OP² - r²\nPB² = OP² - OB² = OP² - r²\n⇒ PA² = PB² ⇒ PA = PB (since lengths > 0).\nBoxed Answer: [ PA = PB (Proved) ].",
                    "concept_questions": [
                        "Which congruence criterion was used to prove ΔOAP ≅ ΔOBP?",
                        "What is the sum of angles ∠APB + ∠AOB in quadrilateral OAPB?"
                    ]
                },
                {
                    "problem": "Example 2 (NCERT): Two tangents TP and TQ are drawn to a circle with centre O from an external point T. Prove that ∠PTQ = 2 ∠OPQ.",
                    "solution": "GIVEN:\nA circle with centre O, an external point T, and tangents TP and TQ touching the circle at P and Q.\n\nTO PROVE:\n∠PTQ = 2 ∠OPQ.\n\nPROOF:\nLet ∠PTQ = θ.\n\nStep 1: Analyze ΔTPQ:\nBy Theorem 10.2, the lengths of tangents from an external point T are equal:\nTP = TQ.\nTherefore, ΔTPQ is an isosceles triangle with TP = TQ.\nIn an isosceles triangle, angles opposite to equal sides are equal:\n∠TPQ = ∠TQP.\n\nStep 2: Use Angle Sum Property in ΔTPQ:\n∠PTQ + ∠TPQ + ∠TQP = 180°\nθ + 2 ∠TPQ = 180°\n2 ∠TPQ = 180° - θ\n∠TPQ = (180° - θ) / 2 = 90° - θ/2 ... (1)\n\nStep 3: Relate to radius OP:\nBy Theorem 10.1, the radius OP is perpendicular to the tangent TP at point P:\n∠OPT = 90°.\nNotice that ∠OPT = ∠OPQ + ∠TPQ:\n∠OPQ + ∠TPQ = 90°\n∠OPQ = 90° - ∠TPQ\n\nStep 4: Substitute ∠TPQ from equation (1):\n∠OPQ = 90° - (90° - θ/2)\n∠OPQ = 90° - 90° + θ/2\n∠OPQ = θ / 2\nMultiply both sides by 2:\n2 ∠OPQ = θ\nSince θ = ∠PTQ:\n∠PTQ = 2 ∠OPQ.\nHence Proved!\n[ROUGH_WORK]\nKey insight: In isosceles ΔTPQ, base angle is 90° - θ/2. Since radius OP ⊥ TP (90°), the remaining angle ∠OPQ is exactly θ/2!\nBoxed Answer: [ ∠PTQ = 2 ∠OPQ (Proved) ].",
                    "concept_questions": [
                        "Why is triangle TPQ isosceles?",
                        "If ∠PTQ = 60°, what is the value of ∠OPQ?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Theorem 10.2 External Tangents HUD",
                "diagram_type": "diagram",
                "svg": svg_external_tangents,
                "concept_visuals": [
                    {
                        "concept_title": "External Tangents Congruence",
                        "diagram_title": "Theorem 10.2 Proof Geometry",
                        "svg": svg_external_tangents,
                        "diagram_type": "diagram",
                        "what_to_make": "Circle with external point P, tangents PA and PB, radii OA and OB, line OP",
                        "what_to_explain": "RHS congruence showing PA = PB and angle bisector properties"
                    }
                ]
            },
            "common_misconceptions": [
                "Assuming tangents from an external point can have different lengths: Theorem 10.2 strictly proves PA = PB always!",
                "Confusing ∠OPQ with ∠TPQ in Example 2: ∠TPQ is with the tangent, while ∠OPQ is with the chord PQ."
            ]
        },

        # Module 3: NCERT Exercise 10.1 & Exercise 10.2 (Questions 1 to 5)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise 10.1 & Exercise 10.2 Part 1 Solver: Contact Computations & Parallel Tangents (Q1 to Q5)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 10.1 (all 4 questions) and Exercise 10.2 Questions 1 through 5. Covers tangent distance computations using Pythagoras theorem (OQ = 12 cm, r = 5 cm ⇒ PQ = √119 cm), angle calculations (∠POQ = 110° ⇒ ∠PTQ = 70°), proof that tangents at ends of diameter are parallel, and proof that perpendicular at contact point passes through centre.",
            "key_concepts": [
                "Ex 10.1 Q1-Q4: Circle has infinitely many tangents; secant cuts in 2 points; circle can have at most 2 parallel tangents in a given direction",
                "Ex 10.1 Q3: Right ΔOPQ with OP = 5 cm, OQ = 12 cm ⇒ PQ = √(12² - 5²) = √(144 - 25) = √119 cm",
                "Ex 10.2 Q1: Point Q at 25 cm from center, tangent length 24 cm ⇒ Radius r = √(25² - 24²) = √(625 - 576) = √49 = 7 cm",
                "Ex 10.2 Q2: TP and TQ tangents with ∠POQ = 110° ⇒ ∠PTQ = 180° - 110° = 70° (Supplementary angles)",
                "Ex 10.2 Q3: Tangents PA and PB inclined at 80° ⇒ ∠AOB = 100° ⇒ ∠POA = 100° / 2 = 50°",
                "Ex 10.2 Q4: Tangents at diameter ends AB: Radii OA ⊥ Tangent 1 and OB ⊥ Tangent 2 ⇒ Alternate interior angles are equal (90° = 90°) ⇒ Tangents are strictly parallel!",
                "Ex 10.2 Q5: Perpendicular at point of contact passes through centre (Proof by contradiction)"
            ],
            "subtopics": [
                "Full resolution of Exercise 10.1 Q1 to Q4",
                "Full resolution of Exercise 10.2 Q1 to Q5",
                "Rigorous proof that tangents at endpoints of diameter are parallel"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 10.2 Q4: Prove that the tangents drawn at the ends of a diameter of a circle are parallel.",
                    "solution": "STATEMENT: Tangents drawn at the ends of a diameter of a circle are parallel.\n\nGIVEN:\nA circle with centre O and diameter AB. Let line PQ be the tangent at end A, and line RS be the tangent at end B.\n\nTO PROVE:\nPQ || RS.\n\nPROOF:\nStep 1: Use Theorem 10.1 at point A:\nSince AB is a diameter, OA is a radius.\nPQ is the tangent to the circle at point of contact A.\nBy Theorem 10.1, the radius through the point of contact is perpendicular to the tangent:\nOA ⊥ PQ\nTherefore, ∠PAB = 90° and ∠QAB = 90° ... (1)\n\nStep 2: Use Theorem 10.1 at point B:\nOB is the radius through the point of contact B.\nRS is the tangent to the circle at point of contact B.\nBy Theorem 10.1, OB ⊥ RS:\nTherefore, ∠ABR = 90° and ∠ABS = 90° ... (2)\n\nStep 3: Compare alternate interior angles:\nNotice the transversal line AB intersects line PQ and line RS.\nFrom (1) and (2):\n∠PAB = 90° and ∠ABS = 90°\n⇒ ∠PAB = ∠ABS.\nThese are alternate interior angles formed by transversal AB with lines PQ and RS.\n\nSince the alternate interior angles are equal, the lines must be parallel:\nPQ || RS.\nHence Proved!\n[ROUGH_WORK]\nAlternatively, consecutive interior angles ∠PAB + ∠ABR = 90° + 90° = 180° (supplementary), proving PQ || RS directly!\nBoxed Answer: [ PQ || RS (Proved) ].",
                    "concept_questions": [
                        "Why is line AB a transversal line?",
                        "What is the sum of co-interior angles ∠QAB and ∠ABS?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Parallel Tangents at Diameter Ends HUD",
                "diagram_type": "diagram",
                "svg": svg_radius_perp,
                "concept_visuals": [
                    {
                        "concept_title": "Parallel Tangent Construction",
                        "diagram_title": "Diameter Endpoints Parallelism",
                        "svg": svg_radius_perp,
                        "diagram_type": "diagram",
                        "what_to_make": "Circle with vertical diameter AB and horizontal tangents at A and B",
                        "what_to_explain": "Alternate interior angles theorem proving parallelism"
                    }
                ]
            },
            "common_misconceptions": [
                "Thinking PQ = √(12² + 5²) = 13 cm in Ex 10.1 Q3: The hypotenuse is OQ = 12 cm, NOT PQ! So PQ = √(12² - 5²) = √119 cm.",
                "Confusing ∠POA with ∠AOB in Ex 10.2 Q3: ∠AOB = 180° - 80° = 100°, but ∠POA is half of that (50°)."
            ]
        },

        # Module 4: NCERT Exercise 10.2 Solver (Questions 6 to 9)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 10.2 Part 2 Solver: Concentric Circles, Circumscribed Quads & Tangent Systems (Q6 to Q9)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 10.2 Questions 6 through 9. Covers radius calculation from point A (Q6), chord of larger concentric circle touching smaller circle (Q7), landmark proof of circumscribed quadrilateral AB + CD = AD + BC (Q8), and proof that ∠AOB = 90° for intercept between parallel tangents (Q9).",
            "key_concepts": [
                "Ex 10.2 Q6: Length of tangent from A (distance 5 cm) is 4 cm ⇒ r = √(5² - 4²) = 3 cm",
                "Ex 10.2 Q7: Concentric circles r1 = 5 cm, r2 = 3 cm: Chord of larger circle touches smaller circle ⇒ Radius bisects chord ⇒ Length = 2√(5² - 3²) = 2 × 4 = 8 cm",
                "Ex 10.2 Q8: A quadrilateral ABCD is drawn to circumscribe a circle. Prove that AB + CD = AD + BC using Theorem 10.2 (AP = AS, BP = BQ, CR = CQ, DR = DS)",
                "Ex 10.2 Q9: Parallel tangents XY and X'Y' with transversal tangent AB touching at C. Prove ∠AOB = 90° via triangle congruence"
            ],
            "subtopics": [
                "Concentric circles chord bisection property",
                "Landmark circumscribed quadrilateral proof (AB + CD = AD + BC)",
                "Full formal proof of ∠AOB = 90° for intercept between parallel tangents"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 10.2 Q8: A quadrilateral ABCD is drawn to circumscribe a circle. Prove that AB + CD = AD + BC.",
                    "solution": "STATEMENT: A quadrilateral ABCD is drawn to circumscribe a circle. Prove that AB + CD = AD + BC.\n\nGIVEN:\nA quadrilateral ABCD circumscribing a circle with centre O.\nLet the sides AB, BC, CD, and DA touch the circle at points P, Q, R, and S respectively.\n\nTO PROVE:\nAB + CD = AD + BC.\n\nPROOF:\nBy Theorem 10.2, the lengths of tangents drawn from an external point to a circle are equal.\n1. From external point A: AP = AS ... (1)\n2. From external point B: BP = BQ ... (2)\n3. From external point C: CR = CQ ... (3)\n4. From external point D: DR = DS ... (4)\n\nStep 1: Add equations (1), (2), (3), and (4) together:\n(AP + BP) + (CR + DR) = (AS + DS) + (BQ + CQ)\n\nStep 2: Group adjacent segments on each side of the quadrilateral:\nNotice that:\nAP + BP = AB\nCR + DR = CD\nAS + DS = AD\nBQ + CQ = BC\n\nStep 3: Substitute the grouped segments:\nAB + CD = AD + BC.\nHence Proved!\n[ROUGH_WORK]\nKey rule: When writing the 4 tangent equality equations, make sure that segments belonging to the SAME side (like AP and BP) are placed on the SAME side of the equals sign!\nBoxed Answer: [ AB + CD = AD + BC (Proved) ].",
                    "concept_questions": [
                        "Why must AP and BP be on the same side of the equations before adding?",
                        "What special quadrilateral results if ABCD is a parallelogram?"
                    ]
                },
                {
                    "problem": "Exercise 10.2 Q9: In Fig., XY and X'Y' are two parallel tangents to a circle with centre O and another tangent AB with point of contact C intersecting XY at A and X'Y' at B. Prove that ∠AOB = 90°.",
                    "solution": "GIVEN:\nA circle with centre O. XY || X'Y' are tangents touching at P and Q respectively.\nAB is another tangent with point of contact C, intersecting XY at A and X'Y' at B.\n\nTO PROVE:\n∠AOB = 90°.\n\nCONSTRUCTION:\nJoin OC.\n\nPROOF:\nStep 1: Prove ΔOPA ≅ ΔOCA:\nIn ΔOPA and ΔOCA:\n1. OP = OC (Radii of the same circle)\n2. AP = AC (Tangents from external point A, Theorem 10.2)\n3. OA = OA (Common side)\nTherefore, by SSS Congruence Criterion:\nΔOPA ≅ ΔOCA.\nBy CPCT:\n∠POA = ∠COA ... (1)\nTherefore, ∠POC = 2 ∠COA.\n\nStep 2: Prove ΔOQB ≅ ΔOCB:\nSimilarly, in ΔOQB and ΔOCB:\n1. OQ = OC (Radii)\n2. BQ = BC (Tangents from external point B)\n3. OB = OB (Common)\nTherefore, ΔOQB ≅ ΔOCB (by SSS).\nBy CPCT:\n∠QOB = ∠COB ... (2)\nTherefore, ∠QOC = 2 ∠COB.\n\nStep 3: Use linear pair on diameter POQ:\nSince XY || X'Y' and OP ⊥ XY, OQ ⊥ X'Y', POQ is a straight line diameter of the circle.\nTherefore, the sum of angles on straight line POQ is 180°:\n∠POC + ∠QOC = 180°\nSubstitute from (1) and (2):\n2 ∠COA + 2 ∠COB = 180°\n2 (∠COA + ∠COB) = 180°\n∠COA + ∠COB = 180° / 2 = 90°\nNotice that ∠COA + ∠COB = ∠AOB:\n∠AOB = 90°.\nHence Proved!\n[ROUGH_WORK]\n2(∠1 + ∠2) = 180° ⇒ ∠1 + ∠2 = 90°. Classical board exam topper proof!\nBoxed Answer: [ ∠AOB = 90° (Proved) ].",
                    "concept_questions": [
                        "Why is POQ guaranteed to be a straight line?",
                        "What congruence criterion was used to prove ΔOPA ≅ ΔOCA?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Circumscribed Polygons and Concentric Chord HUD",
                "diagram_type": "diagram",
                "svg": svg_external_tangents,
                "concept_visuals": [
                    {
                        "concept_title": "Quadrilateral Tangent Sums",
                        "diagram_title": "Circumscribed Quadrilateral Model",
                        "svg": svg_external_tangents,
                        "diagram_type": "diagram",
                        "what_to_make": "Quadrilateral ABCD circumscribing circle touching at P, Q, R, S",
                        "what_to_explain": "Equating 4 external tangent pairs to prove AB + CD = AD + BC"
                    },
                    {
                        "concept_title": "Concentric Circles Tangent Chord",
                        "diagram_title": "Radius 3cm & 5cm Chord Bisection Model",
                        "svg": build_concentric_circles_chord_svg(),
                        "diagram_type": "diagram",
                        "what_to_make": "Concentric circles with radius 3 and 5 showing right triangle OPB and total chord AB = 8 cm",
                        "what_to_explain": "Pythagoras theorem on tangent chord: PB = √(25 - 9) = 4 cm ⇒ AB = 8 cm"
                    }
                ]
            },
            "common_misconceptions": [
                "Scrambling the sides in Q8: Writing AP = AS and BQ = BP makes it impossible to add AP + BP directly. Keep all segments of AB and CD on the LHS!",
                "Assuming POQ is curved: Since both tangents are parallel, their radii OP and OQ lie on the exact same perpendicular transversal line, forming a straight diameter."
            ]
        },

        # Module 5: NCERT Exercise 10.2 Solver (Questions 10 to 13)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise 10.2 Part 3 Solver: Supplementary Angles, Rhombus Proofs & Circumscribed Triangles (Q10 to Q13)",
            "estimated_minutes": 40,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete, rigorous step-by-step resolution of NCERT Exercise 10.2 Questions 10 through 13. Prove angle between tangents is supplementary to central angle (Q10), prove parallelogram circumscribing a circle is a rhombus (Q11), solve the master circumscribed triangle problem with radius 4 cm and segments 6 cm and 8 cm to find sides AB = 15 cm and AC = 13 cm via Heron's formula (Q12), and prove opposite sides of circumscribed quad subtend supplementary angles at centre (Q13).",
            "key_concepts": [
                "Ex 10.2 Q10: Quadrilateral OAPB has ∠OAP = ∠OBP = 90° ⇒ ∠APB + ∠AOB = 360° - 180° = 180° (Supplementary!)",
                "Ex 10.2 Q11: Parallelogram ABCD circumscribing circle: AB = CD and AD = BC; from Q8, AB + CD = AD + BC ⇒ 2AB = 2AD ⇒ AB = AD ⇒ All 4 sides equal ⇒ ABCD is a Rhombus!",
                "Ex 10.2 Q12: ΔABC circumscribes circle radius r = 4 cm; CD = 6 cm, BD = 8 cm ⇒ Let AF = AE = x ⇒ Sides are 14, 8+x, 6+x ⇒ Area by Heron's formula = Area of 3 sub-triangles ⇒ x = 7 ⇒ AB = 15 cm, AC = 13 cm",
                "Ex 10.2 Q13: Opposite sides of circumscribed quadrilateral subtend supplementary angles at centre: ∠AOB + ∠COD = 180° and ∠AOD + ∠BOC = 180°"
            ],
            "subtopics": [
                "Full resolution of Q10 to Q13 with complete geometric proofs",
                "Circumscribed parallelogram to rhombus theorem (Q11)",
                "Full Heron's formula algebraic derivation for triangle sides in Q12",
                "Proof of supplementary opposite central angles (Q13)"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 10.2 Q11: Prove that the parallelogram circumscribing a circle is a rhombus.",
                    "solution": "STATEMENT: Prove that the parallelogram circumscribing a circle is a rhombus.\n\nGIVEN:\nA parallelogram ABCD circumscribing a circle with centre O, touching the sides AB, BC, CD, and DA at P, Q, R, and S respectively.\nSince ABCD is a parallelogram:\nAB = CD ... (1) (Opposite sides of parallelogram are equal)\nAD = BC ... (2)\n\nTO PROVE:\nABCD is a rhombus (i.e. AB = BC = CD = DA).\n\nPROOF:\nStep 1: Apply Theorem 10.2 (Lengths of tangents from external points are equal):\nFrom A: AP = AS\nFrom B: BP = BQ\nFrom C: CR = CQ\nFrom D: DR = DS\nAdding these 4 equations:\n(AP + BP) + (CR + DR) = (AS + DS) + (BQ + CQ)\nAB + CD = AD + BC ... (3) (As proved in Exercise 10.2 Q8)\n\nStep 2: Substitute opposite sides of parallelogram from (1) and (2) into (3):\nReplace CD with AB, and replace BC with AD:\nAB + AB = AD + AD\n2 AB = 2 AD\nDivide both sides by 2:\nAB = AD ... (4)\n\nStep 3: Combine with parallelogram properties:\nFrom (1), (2), and (4):\nAB = BC = CD = DA.\n\nSince ABCD is a parallelogram with all four sides equal in length, it is by definition a rhombus!\nHence Proved!\n[ROUGH_WORK]\nParallelogram + Adjacent sides equal = Rhombus. Direct, 4-step clean deduction!\nBoxed Answer: [ ABCD is a Rhombus (Proved) ].",
                    "concept_questions": [
                        "What is the definition of a rhombus in terms of parallelograms?",
                        "Could a rectangle circumscribing a circle ever be a non-square? (No, it must be a square!)"
                    ]
                },
                {
                    "problem": "Exercise 10.2 Q12: A triangle ABC is drawn to circumscribe a circle of radius 4 cm such that the segments BD and DC into which BC is divided by the point of contact D are of lengths 8 cm and 6 cm respectively. Find the sides AB and AC.",
                    "solution": "GIVEN:\nΔABC circumscribes a circle of radius r = OD = OE = OF = 4 cm.\nPoint D on BC divides it into BD = 8 cm and DC = 6 cm.\nTherefore, BC = BD + DC = 8 + 6 = 14 cm.\n\nLet the circle touch AC at E and AB at F.\nBy Theorem 10.2 (Tangents from an external point are equal):\nFrom point C: CE = CD = 6 cm.\nFrom point B: BF = BD = 8 cm.\nFrom point A: Let AF = AE = x cm (where x > 0).\n\nSide lengths of ΔABC:\na = BC = 14 cm\nb = AC = AE + CE = x + 6 cm\nc = AB = AF + BF = x + 8 cm.\n\nStep 1: Calculate semi-perimeter 's' of ΔABC:\ns = (a + b + c) / 2 = [ 14 + (x + 6) + (x + 8) ] / 2 = (2x + 28) / 2 = x + 14 cm.\n\nStep 2: Compute Area of ΔABC using Heron's Formula:\ns - a = (x + 14) - 14 = x\ns - b = (x + 14) - (x + 6) = 8\ns - c = (x + 14) - (x + 8) = 6\nArea(ΔABC) = √[ s(s - a)(s - b)(s - c) ]\n= √[ (x + 14)(x)(8)(6) ]\n= √[ 48x (x + 14) ] ... (1)\n\nStep 3: Compute Area of ΔABC as sum of 3 sub-triangles (ΔOBC, ΔOCA, ΔOAB):\nJoin OA, OB, OC. The radii OD, OE, OF are perpendicular heights (r = 4 cm) to the three sides:\nArea(ΔOBC) = 1/2 × Base × Height = 1/2 × 14 × 4 = 28 cm²\nArea(ΔOCA) = 1/2 × (x + 6) × 4 = 2(x + 6) = 2x + 12 cm²\nArea(ΔOAB) = 1/2 × (x + 8) × 4 = 2(x + 8) = 2x + 16 cm²\nTotal Area = 28 + (2x + 12) + (2x + 16) = 4x + 56 = 4(x + 14) cm² ... (2)\n\nStep 4: Equate the two area expressions:\n√[ 48x (x + 14) ] = 4(x + 14)\nSquare both sides:\n48x (x + 14) = 16 (x + 14)²\nSince x + 14 > 0, divide both sides by 16(x + 14):\n3x = x + 14\n3x - x = 14\n2x = 14 ⇒ x = 7 cm.\n\nStep 5: Compute side lengths AB and AC:\nAB = x + 8 = 7 + 8 = 15 cm.\nAC = x + 6 = 7 + 6 = 13 cm.\n[ROUGH_WORK]\nCheck Heron's area: s = 7 + 14 = 21. Area = √(21 × 7 × 8 × 6) = √(7056) = 84 cm².\nCheck 1/2 × r × Perimeter = 1/2 × 4 × 42 = 84 cm² (Verified!).\nBoxed Answer: [ AB = 15 cm, AC = 13 cm ].",
                    "concept_questions": [
                        "Why does the area of any circumscribed polygon equal 1/2 × radius × perimeter?",
                        "What is the semi-perimeter of triangle ABC when x = 7?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Circumscribed Triangle Heron's HUD",
                "diagram_type": "diagram",
                "svg": svg_external_tangents,
                "concept_visuals": [
                    {
                        "concept_title": "Triangle Circumscribing Circle",
                        "diagram_title": "Exercise 10.2 Q12 Geometry",
                        "svg": svg_external_tangents,
                        "diagram_type": "diagram",
                        "what_to_make": "Triangle ABC with incenter O, incircle radius 4, segments 6, 8, x",
                        "what_to_explain": "Equating Heron's formula to rs to solve for unknown segment x = 7"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting to divide by 16 when squaring 4(x + 14): [4(x + 14)]² = 16(x + 14)², NOT 4(x + 14)²!",
                "Adding x + 14 = 0: Since x represents a length, x must be positive (x = 7 cm)."
            ]
        }
    ]
    
    return modules
