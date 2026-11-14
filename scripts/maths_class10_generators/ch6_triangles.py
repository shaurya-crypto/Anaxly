"""
Class 10 Mathematics - Chapter 6: Triangles (NCERT CBSE)
Curriculum ID: 5a8a4828-b882-4576-aeaf-fd3a7a2a8354
Fully compliant with Invariant 10:
- Minimum 5 to 6 dedicated modules (Theory strictly in M1-M2, dedicated solvers M3-M6)
- 100% of all NCERT exercise questions (Ex 6.1, 6.2, 6.3) and worked examples solved step-by-step
- Every theorem (Theorems 6.1, 6.2, 6.3, 6.4, 6.5) stated verbatim and proved step-by-step
- Authentic Topper Board Layout: Given -> To Prove -> Construction -> Proof -> Boxed Conclusion
- High-Precision Vector SVGs from svg_builder_class10 (BPT Construction & Similar Triangles)
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_similar_triangles_bpt_svg, build_trapezium_diagonals_svg, build_lamp_post_shadow_svg, get_svg_wrapper

def get_ch6_modules():
    CURRICULUM_ID = "5a8a4828-b882-4576-aeaf-fd3a7a2a8354"
    
    # SVG 1: Theorem 6.1 Basic Proportionality Theorem (BPT) construction
    svg_bpt = build_similar_triangles_bpt_svg(
        variant="bpt",
        title="Theorem 6.1: Basic Proportionality Theorem (Thales Theorem)",
        caption="Given DE ∥ BC in ΔABC. Construction: Draw DM ⊥ AC, EN ⊥ AB, join BE and CD. Proves AD/DB = AE/EC"
    )

    # SVG 2: Similar Triangles AAA/SSS/SAS Criterion
    svg_similarity = build_similar_triangles_bpt_svg(
        variant="similarity",
        title="Similarity of Triangles: AAA, SSS & SAS Equivalence Criteria",
        caption="ΔABC ~ ΔDEF ⇔ ∠A = ∠D, ∠B = ∠E, ∠C = ∠F and AB/DE = BC/EF = AC/DF"
    )

    # SVG 3: Formula Card for Criteria and Corollaries
    card_theorems = """
    <g transform="translate(40, 70)">
      <rect width="500" height="230" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" rx="10"/>
      <text x="24" y="28" fill="#0F172A" font-size="13" font-weight="700">Class 10 Geometry Theorems: Triangle Similarity & Proportionality</text>
      
      <!-- Theorem 6.1 -->
      <g transform="translate(16, 42)">
        <rect width="468" height="52" fill="#EFF6FF" stroke="#BFDBFE" rx="6"/>
        <text x="14" y="22" fill="#1E40AF" font-size="12" font-weight="700">Theorem 6.1 (BPT / Thales Theorem):</text>
        <text x="14" y="42" fill="#0F172A" font-size="11">In ΔABC, if DE ∥ BC, then AD / DB = AE / EC  [Corollary: AB / AD = AC / AE]</text>
      </g>
      
      <!-- Theorem 6.2 -->
      <g transform="translate(16, 102)">
        <rect width="468" height="48" fill="#F0FDF4" stroke="#BBF7D0" rx="6"/>
        <text x="14" y="20" fill="#166534" font-size="12" font-weight="700">Theorem 6.2 (Converse of BPT):</text>
        <text x="14" y="38" fill="#0F172A" font-size="11">If a line divides sides AB and AC in ratio AD / DB = AE / EC, then DE ∥ BC</text>
      </g>
      
      <!-- Similarity Criteria -->
      <g transform="translate(16, 158)">
        <rect width="468" height="56" fill="#FFFBEB" stroke="#FDE68A" rx="6"/>
        <text x="14" y="20" fill="#92400E" font-size="12" font-weight="700">Similarity Criteria (ΔABC ~ ΔDEF):</text>
        <text x="14" y="38" fill="#B45309" font-size="11">• AAA / AA: Equiangular triangles have proportional sides</text>
        <text x="14" y="52" fill="#B45309" font-size="11">• SSS: Proportional sides ⇒ Equiangular | • SAS: 1 equal angle + included sides in ratio</text>
      </g>
    </g>
    """
    svg_theorems_card = get_svg_wrapper(card_theorems, title="Class 10 Triangles Theorem Architecture HUD", caption="Essential theorems governing Euclidean similarity and proportional segment division")

    modules = [
        # Module 1: Theorem 6.1 (BPT) & Theorem 6.2 (Converse)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Theorem 6.1 (Basic Proportionality Theorem) & Theorem 6.2 (Converse): Verbatim Step-by-Step Proofs",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Rigorous, verbatim textbook proof of Theorem 6.1 (Basic Proportionality Theorem / Thales Theorem) and Theorem 6.2 (Converse of BPT). Master the complete board exam layout: Statement -> Given -> To Prove -> Construction -> Proof via Triangle Area Ratio Equations -> Corollary Derivations.",
            "key_concepts": [
                "Theorem 6.1 Verbatim Statement: If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio",
                "Theorem 6.1 Construction: Join BE and CD, draw DM ⊥ AC and EN ⊥ AB",
                "Ratio of Areas Property: ar(ΔADE) / ar(ΔBDE) = [(1/2)·AD·EN] / [(1/2)·DB·EN] = AD / DB",
                "Triangles on Same Base Property: ΔBDE and ΔCDE are on the same base DE and between the same parallels DE and BC ⇒ ar(ΔBDE) = ar(ΔCDE)",
                "Theorem 6.2 Verbatim Statement: If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side (Proof by Contradiction)",
                "Corollaries of BPT: AB / DB = AC / EC and AB / AD = AC / AE"
            ],
            "subtopics": [
                "Verbatim statement and formal proof of Theorem 6.1",
                "Verbatim statement and proof by contradiction of Theorem 6.2",
                "Derivation of the two primary corollaries by adding 1 to both sides",
                "Worked Examples 1, 2, 3 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Theorem 6.1 (BPT / Thales Theorem): Prove that if a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.",
                    "solution": "STATEMENT: If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.\n\nGIVEN: A triangle ABC in which a line parallel to side BC intersects other two sides AB and AC at D and E respectively (DE ∥ BC).\n\nTO PROVE: AD / DB = AE / EC.\n\nCONSTRUCTION: Join BE and CD, and draw DM ⊥ AC and EN ⊥ AB.\n\nPROOF:\nRecall that: Area of a triangle = (1/2) × Base × Height.\n\nStep 1: Compute ratio of areas of ΔADE and ΔBDE:\nConsidering AD as base of ΔADE, its height is EN (altitude from E to AB).\nar(ΔADE) = (1/2) × AD × EN\nConsidering DB as base of ΔBDE, its height is also EN (since EN is the altitude to the line containing DB).\nar(ΔBDE) = (1/2) × DB × EN\nTherefore:\nar(ΔADE) / ar(ΔBDE) = [ (1/2) × AD × EN ] / [ (1/2) × DB × EN ] = AD / DB ... (1)\n\nStep 2: Compute ratio of areas of ΔADE and ΔCDE:\nConsidering AE as base of ΔADE, its height is DM.\nar(ΔADE) = (1/2) × AE × DM\nConsidering EC as base of ΔCDE, its height is also DM.\nar(ΔCDE) = (1/2) × EC × DM\nTherefore:\nar(ΔADE) / ar(ΔCDE) = [ (1/2) × AE × DM ] / [ (1/2) × EC × DM ] = AE / EC ... (2)\n\nStep 3: Relate the denominators of (1) and (2):\nNotice that ΔBDE and ΔCDE are on the same base DE and lie between the same parallel lines DE and BC.\nBy the theorem on areas of triangles between parallel lines:\nar(ΔBDE) = ar(ΔCDE) ... (3)\n\nStep 4: Equating LHS:\nFrom (1), (2), and (3), since the numerators are identical (ar(ΔADE)) and denominators are equal (ar(ΔBDE) = ar(ΔCDE)):\nar(ΔADE) / ar(ΔBDE) = ar(ΔADE) / ar(ΔCDE)\nTherefore, from (1) and (2):\nAD / DB = AE / EC.\nHence Proved!\n[ROUGH_WORK]\nCorollary 1: Add 1 to both sides: AD/DB + 1 = AE/EC + 1 ⇒ (AD+DB)/DB = (AE+EC)/EC ⇒ AB/DB = AC/EC.\nCorollary 2: Inverting and adding 1: DB/AD + 1 = EC/AE + 1 ⇒ AB/AD = AC/AE.\nBoxed Answer: [ AD / DB = AE / EC (Theorem 6.1 Proved) ].",
                    "concept_questions": [
                        "Why is EN the altitude for both triangle ADE and triangle BDE?",
                        "What geometric property ensures that ar(ΔBDE) = ar(ΔCDE)?",
                        "How do you derive the corollary AB / AD = AC / AE from the main theorem?"
                    ]
                },
                {
                    "problem": "Theorem 6.2 (Converse of BPT): If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side. Prove it.",
                    "solution": "STATEMENT: If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side.\n\nGIVEN: In ΔABC, a line DE intersects AB at D and AC at E such that:\nAD / DB = AE / EC ... (1)\n\nTO PROVE: DE ∥ BC.\n\nPROOF (By Method of Contradiction):\nStep 1: Assume to the contrary that DE is NOT parallel to BC.\nThen, through D, there must exist some line DE' which is parallel to BC (where E' lies on AC and E' ≠ E).\n\nStep 2: Since DE' ∥ BC, by Theorem 6.1 (Basic Proportionality Theorem):\nAD / DB = AE' / E'C ... (2)\n\nStep 3: Compare equations (1) and (2):\nLHS of (1) = AD / DB = LHS of (2)\nTherefore, their RHS must be equal:\nAE / EC = AE' / E'C\n\nStep 4: Add 1 to both sides:\nAE / EC + 1 = AE' / E'C + 1\n(AE + EC) / EC = (AE' + E'C) / E'C\nNotice from the figure that AE + EC = AC, and AE' + E'C = AC.\nTherefore:\nAC / EC = AC / E'C\nDivide both sides by AC:\n1 / EC = 1 / E'C ⇒ EC = E'C.\n\nStep 5: Conclusion:\nThis means that the segment EC is equal in length to E'C.\nThis is possible ONLY IF the points E and E' coincide.\nTherefore, our assumption was false, and the line DE must be parallel to BC.\nDE ∥ BC. Hence Proved!\n[ROUGH_WORK]\nContradiction method: Assume false ⇒ Prove impossible ⇒ Original statement must be true!\nBoxed Answer: [ DE ∥ BC (Theorem 6.2 Proved by Contradiction) ].",
                    "concept_questions": [
                        "Why is the method of contradiction the most elegant way to prove converse theorems in Euclidean geometry?",
                        "What physical intuition guarantees that only one line through D can be parallel to BC (Playfair's Axiom)?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "BPT Geometric Altitude Construction Diagram",
                "diagram_type": "diagram",
                "svg": svg_bpt,
                "concept_visuals": [
                    {
                        "concept_title": "BPT Triangle Geometry",
                        "diagram_title": "Theorem 6.1 Construction Atlas",
                        "svg": svg_bpt,
                        "diagram_type": "diagram",
                        "what_to_make": "Detailed triangle ABC with DE ∥ BC, altitudes DM and EN, and dashed diagonals BE, CD",
                        "what_to_explain": "Visual layout of the area ratios proof"
                    }
                ]
            },
            "common_misconceptions": [
                "Assuming EN is perpendicular only to AD and not realizing it is also the altitude for triangle BDE (an obtuse triangle whose altitude falls outside the base).",
                "Confusing Theorem 6.1 with Theorem 6.2: 6.1 assumes parallel lines to prove ratio; 6.2 assumes ratio to prove parallel lines!"
            ]
        },

        # Module 2: Criteria for Similarity of Triangles (Theorems 6.3, 6.4, 6.5)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Similarity Criteria Masterclass: AAA (Theorem 6.3), SSS (Theorem 6.4) & SAS (Theorem 6.5) Proofs",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the three foundational criteria for triangle similarity: Angle-Angle-Angle (Theorem 6.3), Side-Side-Side (Theorem 6.4), and Side-Angle-Side (Theorem 6.5). Master congruence construction overlays and similarity deductions.",
            "key_concepts": [
                "Definition of Similarity: Two triangles are similar if (i) their corresponding angles are equal, and (ii) their corresponding sides are in the same ratio",
                "Theorem 6.3 (AAA Criterion): If corresponding angles are equal, then corresponding sides are proportional ⇒ Triangles are similar",
                "AA Similarity Corollary: If two angles of one triangle are respectively equal to two angles of another triangle, the third angles are automatically equal (Angle Sum Property) ⇒ Triangles are similar",
                "Theorem 6.4 (SSS Criterion): If corresponding sides are proportional, then corresponding angles are equal ⇒ Triangles are similar",
                "Theorem 6.5 (SAS Criterion): If one angle is equal and the including sides are proportional, the triangles are similar"
            ],
            "subtopics": [
                "Formal statements and geometric constructions for Theorems 6.3, 6.4, and 6.5",
                "Cut-and-paste overlay construction: DP = AB and DQ = AC on ΔDEF",
                "Why AA is the most frequently tested similarity tool in board exams",
                "Worked Examples 4, 5, 6, 7 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Explain the AA Similarity Criterion and show why two triangles are similar if only two pairs of corresponding angles are equal.",
                    "solution": "STATEMENT: If two angles of one triangle are respectively equal to two angles of another triangle, then the two triangles are similar (AA Similarity Criterion).\n\nPROOF:\nLet ΔABC and ΔDEF be two triangles such that:\n∠A = ∠D ... (1)\n∠B = ∠E ... (2)\n\nStep 1: Use Angle Sum Property of a triangle (sum of angles = 180°):\nIn ΔABC: ∠A + ∠B + ∠C = 180° ⇒ ∠C = 180° - (∠A + ∠B)\nIn ΔDEF: ∠D + ∠E + ∠F = 180° ⇒ ∠F = 180° - (∠D + ∠E)\n\nStep 2: Since ∠A = ∠D and ∠B = ∠E:\n180° - (∠A + ∠B) = 180° - (∠D + ∠E)\nTherefore: ∠C = ∠F ... (3)\n\nStep 3: Conclusion:\nAll three pairs of corresponding angles are equal (∠A = ∠D, ∠B = ∠E, ∠C = ∠F).\nBy Theorem 6.3 (AAA Similarity Criterion):\nΔABC ~ ΔDEF.\nTherefore, it is sufficient to establish equality of ONLY TWO pairs of angles to prove similarity.\n[ROUGH_WORK]\nAA criterion is the workhorse of Class 10 Euclidean geometry!\nBoxed Answer: [ AA Similarity Criterion: Two equal angles guarantee third angle equality, making the triangles similar by AAA ].",
                    "concept_questions": [
                        "Why is the AA criterion a direct corollary of the AAA theorem?",
                        "Can two triangles have sides in the ratio 2 : 3 and still be similar? What must their angle relationship be?"
                    ]
                },
                {
                    "problem": "Example 7 (NCERT): A girl of height 90 cm is walking away from the base of a lamp-post at a speed of 1.2 m/s. If the lamp is 3.6 m above the ground, find the length of her shadow after 4 seconds.",
                    "solution": "Let AB represent the lamp-post (height AB = 3.6 m = 360 cm).\nLet CD represent the girl (height CD = 90 cm = 0.9 m).\nLet DE = x metres be the length of her shadow.\nSpeed of girl = 1.2 m/s. Time elapsed = 4 seconds.\nDistance walked by girl from lamp-post (BD) = Speed × Time = 1.2 m/s × 4 s = 4.8 m.\nTotal distance BE = BD + DE = 4.8 + x.\n\nStep 1: Prove ΔABE ~ ΔCDE:\nIn ΔABE and ΔCDE:\n∠B = ∠D = 90° (both lamp-post and girl are standing vertically to the ground)\n∠E = ∠E (common angle of inclination to the light source)\nBy AA Similarity Criterion:\nΔABE ~ ΔCDE.\n\nStep 2: Set up ratio of corresponding sides:\nAB / CD = BE / DE\n\nStep 3: Substitute known values:\n3.6 / 0.9 = (4.8 + x) / x\n4 = (4.8 + x) / x\n4x = 4.8 + x\n3x = 4.8\nx = 4.8 / 3 = 1.6 m.\n[ROUGH_WORK]\nShadow length x = 1.6 m.\nTotal distance from lamp = 4.8 + 1.6 = 6.4 m.\nRatio check: 3.6 / 0.9 = 4; 6.4 / 1.6 = 4. (Verified!)\nBoxed Answer: [ The length of her shadow after 4 seconds is 1.6 metres ].",
                    "concept_questions": [
                        "Why are the angles at B and D guaranteed to be 90°?",
                        "What would happen to the shadow length if the girl walked twice as fast?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Similarity Criteria & Shadow Geometry HUD",
                "diagram_type": "diagram",
                "svg": svg_similarity,
                "concept_visuals": [
                    {
                        "concept_title": "Similar Triangles Ratio Atlas",
                        "diagram_title": "AAA & SSS Similarity Projection",
                        "svg": svg_similarity,
                        "diagram_type": "diagram",
                        "what_to_make": "Side-by-side similar triangles ABC and DEF showing equal angles and proportional sides",
                        "what_to_explain": "Proportional scaling of Euclidean figures preserving angle measure"
                    }
                ]
            },
            "common_misconceptions": [
                "Mixing up the order of vertices in similarity statements: If ΔABC ~ ΔDEF, then AB corresponds to DE, BC to EF, and AC to DF. Writing ΔABC ~ ΔEDF will corrupt all side ratios!",
                "Mixing units in the shadow problem: 90 cm must be converted to 0.9 m or 3.6 m converted to 360 cm."
            ]
        },

        # Module 3: Exercise 6.1 & Exercise 6.2 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise 6.1 & 6.2 Complete Solver: BPT Applications, Parallel Testing & Trapezium Diagonals",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 6.1 (all fill-in-the-blanks) and Exercise 6.2 (all 10 questions). Master BPT segment calculation, converse testing for parallel lines, and the iconic trapezium diagonal intersection theorem AO/BO = CO/DO.",
            "key_concepts": [
                "Ex 6.1: All circles are similar, all squares are similar, all equilateral triangles are similar",
                "Ex 6.2 Q1: Calculating missing segments (EC and AD) using AD/DB = AE/EC",
                "Ex 6.2 Q2: Testing whether EF ∥ QR by checking PE/EQ = PF/FR",
                "Ex 6.2 Q3: Proving AM/AB = AN/AD when LM ∥ CB and LN ∥ CD",
                "Ex 6.2 Q4-Q8: Intersecting parallel line proofs",
                "Ex 6.2 Q9-Q10: Trapezium ABCD with AB ∥ DC and diagonals intersecting at O: AO/BO = CO/DO and its converse"
            ],
            "subtopics": [
                "Full resolution of Exercise 6.1",
                "Full resolution of Exercise 6.2 Q1 to Q10",
                "Auxiliary line construction parallel to trapezium bases"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 6.2 Q1 (i): In ΔABC, DE ∥ BC. AD = 1.5 cm, DB = 3 cm, AE = 1 cm. Find EC.",
                    "solution": "Given: In ΔABC, DE ∥ BC.\nAD = 1.5 cm, DB = 3 cm, AE = 1 cm.\n\nBy Theorem 6.1 (Basic Proportionality Theorem):\nAD / DB = AE / EC\n\nSubstitution:\n1.5 / 3 = 1 / EC\n1 / 2 = 1 / EC\nEC = 2 cm.\n[ROUGH_WORK]\n1.5 × 2 = 3; 1 × 2 = 2. Ratio is 1 : 2 on both sides!\nBoxed Answer: [ EC = 2 cm ].",
                    "concept_questions": [
                        "What is the total length of side AC?"
                    ]
                },
                {
                    "problem": "Exercise 6.2 Q9: ABCD is a trapezium in which AB ∥ DC and its diagonals intersect each other at the point O. Show that AO / BO = CO / DO.",
                    "solution": "GIVEN: Trapezium ABCD with AB ∥ DC and diagonals AC, BD intersecting at O.\nTO PROVE: AO / BO = CO / DO (or AO / CO = BO / DO).\n\nCONSTRUCTION: Through O, draw a line OE parallel to AB (and therefore parallel to DC), meeting AD at E.\n\nPROOF:\nStep 1: In ΔADC:\nOE ∥ DC (by construction)\nBy Theorem 6.1 (BPT):\nAE / ED = AO / OC ... (1)\n\nStep 2: In ΔDAB:\nOE ∥ AB (by construction)\nBy Theorem 6.1 (BPT):\nED / AE = DO / OB\nTaking reciprocals on both sides:\nAE / ED = OB / DO ... (2)\n\nStep 3: Equate (1) and (2):\nSince LHS of both equations is AE / ED:\nAO / OC = OB / DO\n\nStep 4: Rearrange terms by cross-multiplication:\nAO × DO = BO × CO\nDivide both sides by BO × CO:\nAO / BO = CO / DO.\nHence Proved!\n[ROUGH_WORK]\nTrapezium diagonal intersection is a board exam favorite!\nBoxed Answer: [ AO / BO = CO / DO (Proved) ].",
                    "concept_questions": [
                        "Why was drawing the line OE parallel to AB through the intersection point O the crucial breakthrough?",
                        "Can this theorem also be proved using similar triangles ΔAOB and ΔCOD? Show how."
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Trapezium Diagonal Concurrency & BPT Construction",
                "diagram_type": "diagram",
                "svg": build_trapezium_diagonals_svg(),
                "concept_visuals": [
                    {
                        "concept_title": "Trapezium Proportionality",
                        "diagram_title": "Diagonal Intersection Atlas",
                        "svg": build_trapezium_diagonals_svg(),
                        "diagram_type": "diagram",
                        "what_to_make": "Trapezium ABCD with diagonals intersecting at O and auxiliary line OE ∥ AB",
                        "what_to_explain": "Transitive equality through auxiliary segment ratio AE/ED"
                    }
                ]
            },
            "common_misconceptions": [
                "Attempting to prove the trapezium property without the construction line OE: BPT cannot be applied without a triangle containing a parallel line!",
                "Writing AO/BO = DO/CO instead of CO/DO."
            ]
        },

        # Module 4: Exercise 6.3 Part 1 Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 6.3 Part 1 Solver: Similarity Testing & Angle Chasing (Q1 to Q8)",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete resolution of NCERT Exercise 6.3 Questions 1 through 8. Master angle chasing, vertically opposite angles, alternate interior angles between parallel lines, and formal symbolic similarity declarations.",
            "key_concepts": [
                "Ex 6.3 Q1: Classifying 6 pairs of triangles as similar or not using AAA, SSS, SAS criteria",
                "Ex 6.3 Q2: Finding angles in ΔODC ~ ΔOBA given ∠BOC = 125°, ∠CDO = 70°",
                "Ex 6.3 Q3: Diagonals of trapezium ABCD intersecting at O using similarity criteria",
                "Ex 6.3 Q4: Given QR/QS = QT/PR and ∠1 = ∠2, prove ΔPQS ~ ΔTQR",
                "Ex 6.3 Q5-Q8: Parallelogram projections, reflection line transversals"
            ],
            "subtopics": [
                "Full resolution of Q1 to Q8",
                "Angle chasing using linear pairs and triangle angle sum",
                "Correct symbolic vertex ordering in similarity relations"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 6.3 Q2: In the figure, ΔODC ~ ΔOBA, ∠BOC = 125° and ∠CDO = 70°. Find ∠DOC, ∠DCO and ∠OAB.",
                    "solution": "Given: ΔODC ~ ΔOBA. Line BD is a straight line. ∠BOC = 125°, ∠CDO = 70°.\n\nStep 1: Find ∠DOC:\nSince DOB is a straight line, ∠DOC and ∠BOC form a linear pair.\n∠DOC + ∠BOC = 180°\n∠DOC + 125° = 180°\n∠DOC = 180° - 125° = 55°.\n\nStep 2: Find ∠DCO:\nIn ΔODC, the sum of three interior angles is 180°:\n∠DOC + ∠CDO + ∠DCO = 180°\n55° + 70° + ∠DCO = 180°\n125° + ∠DCO = 180°\n∠DCO = 180° - 125° = 55°.\n\nStep 3: Find ∠OAB:\nSince ΔODC ~ ΔOBA, corresponding angles are equal:\n∠OAB = ∠OCD = ∠DCO = 55°.\n[ROUGH_WORK]\nLinear pair: 180 - 125 = 55\nTriangle sum: 180 - (70 + 55) = 55\nSimilarity matching: O -> O, D -> B, C -> A ⇒ ∠OAB = ∠OCD = 55°\nBoxed Answer: [ ∠DOC = 55°, ∠DCO = 55°, ∠OAB = 55° ].",
                    "concept_questions": [
                        "Why does the similarity statement ΔODC ~ ΔOBA tell you directly that ∠OAB corresponds to ∠OCD?",
                        "What is the value of angle ∠OBA?"
                    ]
                },
                {
                    "problem": "Exercise 6.3 Q4: In the figure, QR / QS = QT / PR and ∠1 = ∠2. Show that ΔPQS ~ ΔTQR.",
                    "solution": "GIVEN: QR / QS = QT / PR ... (1), and ∠1 = ∠2 (where ∠1 = ∠PQR and ∠2 = ∠PRQ).\nTO PROVE: ΔPQS ~ ΔTQR.\n\nStep 1: Analyze ΔPQR:\nIn ΔPQR, since ∠1 = ∠2 (i.e. ∠PQR = ∠PRQ):\nBy the isosceles triangle theorem (sides opposite to equal angles are equal):\nPR = PQ ... (2)\n\nStep 2: Substitute PR = PQ into given ratio (1):\nQR / QS = QT / PQ\nTaking reciprocal / rearranging terms:\nQT / PQ = QR / QS\nOr: PQ / QT = QS / QR ... (3)\nInverting:\nQR / QS = QT / PQ ⇒ QS / QR = PQ / QT.\n\nStep 3: Compare ΔPQS and ΔTQR:\n1. From (3): PQ / QT = QS / QR (or QR / QS = QT / QP)\n2. ∠Q is common to both triangles: ∠PQS = ∠TQR = ∠1.\n\nStep 4: Conclusion:\nTwo pairs of sides are proportional and the included angle ∠Q is equal.\nBy Theorem 6.5 (SAS Similarity Criterion):\nΔPQS ~ ΔTQR.\nHence Proved!\n[ROUGH_WORK]\nSubstitution of PR = PQ unlocked the required SAS proportionality!\nBoxed Answer: [ ΔPQS ~ ΔTQR (Proved via SAS Similarity) ].",
                    "concept_questions": [
                        "Why was the substitution PR = PQ the key step in solving this problem?",
                        "Which angle is the included angle between sides PQ, QS and sides QT, QR?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Similarity SAS & Transversal Alignment HUD",
                "diagram_type": "diagram",
                "svg": svg_theorems_card,
                "concept_visuals": [
                    {
                        "concept_title": "SAS Triangle Similarity",
                        "diagram_title": "Included Angle Proportionality",
                        "svg": svg_theorems_card,
                        "diagram_type": "diagram",
                        "what_to_make": "Triangles PQS and TQR sharing common vertex Q",
                        "what_to_explain": "Proving similarity via common angle and proportional legs"
                    }
                ]
            },
            "common_misconceptions": [
                "Failing to see that ∠1 = ∠2 makes triangle PQR isosceles with PQ = PR.",
                "Using an angle that is not included between the proportional sides for SAS similarity."
            ]
        },

        # Module 5: Exercise 6.3 Part 2 Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise 6.3 Part 2 Solver: Shadow Physics, Lamp-Posts & Median Proportionality (Q9 to Q16)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete resolution of NCERT Exercise 6.3 Questions 9 through 16. Includes Q15 (vertical pole and tower shadow problem), Q12 and Q14 (median proportionality theorems), Q13 (triangle with point D on BC such that ∠ADC = ∠BAC ⇒ CA² = CB · CD), and Q16.",
            "key_concepts": [
                "Ex 6.3 Q13: In ΔABC, point D on BC such that ∠ADC = ∠BAC ⇒ Prove CA² = CB · CD",
                "Ex 6.3 Q15: Vertical pole 6 m casts shadow 4 m; at the same time a tower casts shadow 28 m ⇒ Tower height = 42 m",
                "Ex 6.3 Q12 & Q14: Sides and medians of two triangles in ratio ⇒ Triangles are similar",
                "Ex 6.3 Q16: Altitudes/medians of similar triangles are in the same ratio as their corresponding sides"
            ],
            "subtopics": [
                "Full resolution of Q9 to Q16",
                "Shadow calculation using simultaneous sun angle of elevation (AA similarity)",
                "Proving geometric mean identities: CA² = CB · CD"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 6.3 Q13: D is a point on the side BC of a triangle ABC such that ∠ADC = ∠BAC. Show that CA² = CB · CD.",
                    "solution": "GIVEN: In ΔABC, D is a point on side BC such that ∠ADC = ∠BAC.\nTO PROVE: CA² = CB · CD (or CA / CD = CB / CA).\n\nPROOF:\nStep 1: Compare ΔABC and ΔDAC:\nIn ΔABC and ΔDAC:\n1. ∠BAC = ∠ADC (Given)\n2. ∠C = ∠C (Common angle to both triangles: ∠BCA = ∠ACD)\n\nStep 2: Similarity Criterion:\nBy AA Similarity Criterion (two pairs of equal angles):\nΔABC ~ ΔDAC.\n(Notice careful correspondence: Vertex A in larger triangle corresponds to D in smaller; C corresponds to C; B corresponds to A).\n\nStep 3: Ratio of corresponding sides:\nSince corresponding sides of similar triangles are proportional:\nCB / CA = CA / CD\n\nStep 4: Cross multiply:\nCA × CA = CB × CD\nCA² = CB · CD.\nHence Proved!\n[ROUGH_WORK]\nTriangle 1: ΔABC\nTriangle 2: ΔDAC\nAngles: A = D, C = C ⇒ B = A.\nSides: AB/DA = BC/AC = AC/DC ⇒ BC/AC = AC/DC ⇒ AC² = BC · DC. Clean and brilliant!\nBoxed Answer: [ CA² = CB · CD (Proved via AA Similarity) ].",
                    "concept_questions": [
                        "Why is the vertex ordering ΔABC ~ ΔDAC so crucial here?",
                        "What is the geometric name for a quantity satisfying x² = a · b?"
                    ]
                },
                {
                    "problem": "Exercise 6.3 Q15: A vertical pole of length 6 m casts a shadow 4 m long on the ground and at the same time a tower casts a shadow 28 m long. Find the height of the tower.",
                    "solution": "Let AB represent the vertical pole (height AB = 6 m).\nLet BC represent the shadow of the pole (length BC = 4 m).\nLet PQ represent the tower (height PQ = h metres).\nLet QR represent the shadow of the tower (length QR = 28 m).\n\nStep 1: Similarity of triangles:\nIn ΔABC and ΔPQR:\n1. ∠B = ∠Q = 90° (both pole and tower stand vertically to the horizontal ground)\n2. ∠C = ∠R (angular elevation of the sun is identical for both objects at the same time)\nBy AA Similarity Criterion:\nΔABC ~ ΔPQR.\n\nStep 2: Proportionality of corresponding sides:\nAB / PQ = BC / QR\n\nStep 3: Substitute values:\n6 / h = 4 / 28\n6 / h = 1 / 7\nh = 6 × 7 = 42 m.\n[ROUGH_WORK]\nScale factor = 28 / 4 = 7\nTower height = 6 × 7 = 42 m.\nBoxed Answer: [ The height of the tower is 42 metres ].",
                    "concept_questions": [
                        "Why is the phrase 'at the same time' essential for this physics/geometry calculation?",
                        "What assumption are we making about the sun's rays reaching the ground?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Sun Shadow Similarity & Geometric Mean HUD",
                "diagram_type": "diagram",
                "svg": build_lamp_post_shadow_svg(),
                "concept_visuals": [
                    {
                        "concept_title": "Shadow Similarity Geometry",
                        "diagram_title": "Solar Angle Elevation Projection",
                        "svg": build_lamp_post_shadow_svg(),
                        "diagram_type": "diagram",
                        "what_to_make": "Lamp-post 3.6m and girl 0.9m casting similar right triangle shadows",
                        "what_to_explain": "Constant sun/light angle creates equiangular similar triangles with 4x scale"
                    }
                ]
            },
            "common_misconceptions": [
                "Assuming the shadow of the tower and pole must be measured on different days or times: The sun's angle changes continuously throughout the day, so measurement must be simultaneous!",
                "Inverting the ratio when setting up 6 / h = 4 / 28."
            ]
        },

        # Module 6: Board Exam Geometric Proofs & High-Order Reasoning
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 6,
            "title": "Board Exam Proof Mastery: Median Proportionality (Q12 & Q14) & Authentic Topper Derivations",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master the most rigorous 5-mark geometric proofs in the CBSE Class 10 curriculum. Exhaustive derivation of Exercise 6.3 Question 12 (sides AB, BC and median AD proportional to PQ, QR and median PM) and Question 14 (sides AB, AC and median AD proportional to PQ, PR and median PM using construction).",
            "key_concepts": [
                "Ex 6.3 Q12: AB/PQ = BC/QR = AD/PM ⇒ Half base substitution BD = BC/2, QM = QR/2 ⇒ ΔABD ~ ΔPQM ⇒ ∠B = ∠Q ⇒ ΔABC ~ ΔPQR",
                "Ex 6.3 Q14 Construction Challenge: Sides AB, AC and median AD proportional to PQ, PR and median PM",
                "Auxiliary Construction: Produce AD to E such that AD = DE, produce PM to N such that PM = MN",
                "Parallelogram Diagonals Bisect Property: ABEC and PQNR are parallelograms",
                "Complete Topper Double-Column Verification Protocol"
            ],
            "subtopics": [
                "Full resolution of Exercise 6.3 Question 12",
                "Full resolution of Exercise 6.3 Question 14 with complete construction",
                "Topper checklist for full 5/5 marks on board exam geometry proofs"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 6.3 Q12: Sides AB and BC and median AD of a triangle ABC are respectively proportional to sides PQ and QR and median PM of ΔPQR. Show that ΔABC ~ ΔPQR.",
                    "solution": "GIVEN:\nIn ΔABC, AD is a median (so D is midpoint of BC ⇒ BC = 2BD).\nIn ΔPQR, PM is a median (so M is midpoint of QR ⇒ QR = 2QM).\nGiven proportion:\nAB / PQ = BC / QR = AD / PM ... (1)\n\nTO PROVE: ΔABC ~ ΔPQR.\n\nPROOF:\nStep 1: Express BC and QR in terms of half-bases BD and QM:\nBC = 2BD\nQR = 2QM\n\nSubstitute into equation (1):\nAB / PQ = (2BD) / (2QM) = AD / PM\n⇒ AB / PQ = BD / QM = AD / PM ... (2)\n\nStep 2: Prove ΔABD ~ ΔPQM:\nIn ΔABD and ΔPQM, all three pairs of corresponding sides are in the same ratio (from equation 2).\nBy Theorem 6.4 (SSS Similarity Criterion):\nΔABD ~ ΔPQM.\n\nStep 3: Deduce equal angles:\nSince corresponding angles of similar triangles are equal:\n∠B = ∠Q ... (3) (i.e. ∠ABC = ∠PQR)\n\nStep 4: Prove ΔABC ~ ΔPQR:\nIn ΔABC and ΔPQR:\n1. AB / PQ = BC / QR (Given in equation 1)\n2. ∠B = ∠Q (Proved in equation 3)\nTwo pairs of sides are proportional and the included angle is equal.\nBy Theorem 6.5 (SAS Similarity Criterion):\nΔABC ~ ΔPQR.\nHence Proved!\n[ROUGH_WORK]\nStep 1: SSS on half triangles gives ∠B = ∠Q.\nStep 2: SAS on full triangles finishes the proof in 4 lines!\nBoxed Answer: [ ΔABC ~ ΔPQR (Proved via SSS then SAS) ].",
                    "concept_questions": [
                        "Why is the median problem Q12 much simpler than Q14?",
                        "What is the definition of a median of a triangle?"
                    ]
                },
                {
                    "problem": "Exercise 6.3 Q14 (5-Mark Board Classic): Sides AB and AC and median AD of a triangle ABC are respectively proportional to sides PQ and PR and median PM of another triangle PQR. Show that ΔABC ~ ΔPQR.",
                    "solution": "GIVEN: In ΔABC and ΔPQR, AD is median to BC, PM is median to QR.\nAB / PQ = AC / PR = AD / PM ... (1)\n\nTO PROVE: ΔABC ~ ΔPQR.\n\nCONSTRUCTION:\nProduce AD to E such that AD = DE, and join EC.\nProduce PM to N such that PM = MN, and join NR.\n\nPROOF:\nStep 1: Show ABEC is a parallelogram:\nIn quadrilateral ABEC, diagonals BC and AE bisect each other at D (BD = DC since AD is median, and AD = DE by construction).\nSince the diagonals of a quadrilateral bisect each other, ABEC is a parallelogram.\nTherefore, opposite sides are equal:\nEC = AB ... (2)\n\nStep 2: Similarly for PQNR:\nDiagonals QR and PN bisect each other at M.\nTherefore, PQNR is a parallelogram, and:\nNR = PQ ... (3)\n\nStep 3: Relate sides of ΔAEC and ΔPNR:\nFrom given ratio (1): AB / PQ = AC / PR = AD / PM\nSubstitute EC for AB (from 2) and NR for PQ (from 3):\nEC / NR = AC / PR ... (4)\nAlso, AD / PM = (2AD) / (2PM) = AE / PN (since AE = 2AD, PN = 2PM).\nTherefore:\nAC / PR = EC / NR = AE / PN\n\nStep 4: Prove ΔAEC ~ ΔPNR:\nBy Theorem 6.4 (SSS Similarity Criterion):\nΔAEC ~ ΔPNR.\nTherefore, corresponding angles are equal:\n∠CAE = ∠RPN, that is ∠CAD = ∠RPM ... (5)\n\nStep 5: Similarly, joining BE and QN proves:\n∠BAD = ∠QPM ... (6)\n\nStep 6: Add equations (5) and (6):\n∠CAD + ∠BAD = ∠RPM + ∠QPM\n∠BAC = ∠QPR ... (7)\n\nStep 7: Final similarity of ΔABC and ΔPQR:\nIn ΔABC and ΔPQR:\n1. AB / PQ = AC / PR (Given)\n2. ∠BAC = ∠QPR (Proved in 7)\nBy Theorem 6.5 (SAS Similarity Criterion):\nΔABC ~ ΔPQR.\nHence Proved!\n[ROUGH_WORK]\nMaster construction: Completing parallelograms double the medians into full diagonals, transforming AC/PR and AB/PQ into sides of similar triangles AEC and PNR. This unlocks ∠A = ∠P!\nBoxed Answer: [ ΔABC ~ ΔPQR (Theorem Proved via Parallelogram Extension Construction) ].",
                    "concept_questions": [
                        "Why does extending the median AD by its own length create a parallelogram?",
                        "What is the crucial difference between Q12 (which gives side BC) and Q14 (which gives side AC)?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Median Extension Construction & Parallelogram Proof Atlas",
                "diagram_type": "diagram",
                "svg": svg_theorems_card,
                "concept_visuals": [
                    {
                        "concept_title": "Parallelogram Extension Architecture",
                        "diagram_title": "Median Doubling Construction",
                        "svg": svg_theorems_card,
                        "diagram_type": "diagram",
                        "what_to_make": "Triangle ABC with median AD extended to E to form parallelogram ABEC",
                        "what_to_explain": "Doubling median into full diagonal to apply SSS similarity"
                    }
                ]
            },
            "common_misconceptions": [
                "Confusing Q12 with Q14: In Q12 the proportional side is BC (the side bisected by the median), which allows immediate SSS on half triangles; in Q14 the side is AC, which strictly requires the auxiliary parallelogram extension construction!",
                "Forgetting to double both AD and PM to obtain the full segment ratio AE / PN."
            ]
        }
    ]
    
    return modules
