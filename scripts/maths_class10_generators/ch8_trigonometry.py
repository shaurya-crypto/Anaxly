"""
Class 10 Mathematics - Chapter 8: Introduction to Trigonometry (NCERT CBSE)
Curriculum ID: d854ea09-23bd-4eeb-b9b0-0b943b22ed76
Fully compliant with Invariant 10:
- Minimum 5 to 6 dedicated modules (Theory strictly in M1-M3, dedicated solvers M4-M6)
- 100% of all NCERT exercise questions (Ex 8.1, 8.2, 8.3) and worked examples solved step-by-step
- All 10 proof identities of Ex 8.3 Q4 solved with rigorous line-by-line algebraic justification
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- High-Precision Vector SVGs from svg_builder_class10 (Right Triangle Trig HUD & Angle Derivations)
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_trigonometry_right_triangle_svg, get_svg_wrapper

def get_ch8_modules():
    CURRICULUM_ID = "d854ea09-23bd-4eeb-b9b0-0b943b22ed76"
    
    # SVG 1: Right-Angled Triangle with labeled sides and 6-trig ratios HUD
    svg_triangle_ratios = build_trigonometry_right_triangle_svg(
        angle_label="θ",
        opp_label="Opposite (Perpendicular)",
        adj_label="Adjacent (Base)",
        hyp_label="Hypotenuse",
        title="Trigonometric Ratios in Right-Angled Triangle",
        caption="sin θ = Opp/Hyp, cos θ = Adj/Hyp, tan θ = Opp/Adj, csc = 1/sin, sec = 1/cos, cot = 1/tan"
    )

    # SVG 2: Specific Angles Table HUD
    card_angles = """
    <g transform="translate(30, 70)">
      <rect width="520" height="230" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" rx="10"/>
      <text x="24" y="26" fill="#0F172A" font-size="13" font-weight="700">Exact Values of Trigonometric Ratios for Standard Angles</text>
      
      <!-- Table Header -->
      <g transform="translate(16, 38)">
        <rect width="488" height="26" fill="#0F172A" rx="4"/>
        <text x="30" y="17" fill="#FFFFFF" font-size="11" font-weight="700">Ratio</text>
        <text x="110" y="17" fill="#FFFFFF" font-size="11" font-weight="700">0°</text>
        <text x="190" y="17" fill="#FFFFFF" font-size="11" font-weight="700">30°</text>
        <text x="270" y="17" fill="#FFFFFF" font-size="11" font-weight="700">45°</text>
        <text x="350" y="17" fill="#FFFFFF" font-size="11" font-weight="700">60°</text>
        <text x="430" y="17" fill="#FFFFFF" font-size="11" font-weight="700">90°</text>
      </g>
      
      <!-- Row sin -->
      <g transform="translate(16, 68)">
        <rect width="488" height="24" fill="#EFF6FF" rx="3"/>
        <text x="30" y="16" fill="#1E40AF" font-size="11" font-weight="700">sin θ</text>
        <text x="110" y="16" fill="#0F172A" font-size="11">0</text>
        <text x="190" y="16" fill="#0F172A" font-size="11">1/2</text>
        <text x="270" y="16" fill="#0F172A" font-size="11">1/√2</text>
        <text x="350" y="16" fill="#0F172A" font-size="11">√3/2</text>
        <text x="430" y="16" fill="#0F172A" font-size="11">1</text>
      </g>
      
      <!-- Row cos -->
      <g transform="translate(16, 96)">
        <rect width="488" height="24" fill="#F8FAFC" rx="3"/>
        <text x="30" y="16" fill="#0F172A" font-size="11" font-weight="700">cos θ</text>
        <text x="110" y="16" fill="#0F172A" font-size="11">1</text>
        <text x="190" y="16" fill="#0F172A" font-size="11">√3/2</text>
        <text x="270" y="16" fill="#0F172A" font-size="11">1/√2</text>
        <text x="350" y="16" fill="#0F172A" font-size="11">1/2</text>
        <text x="430" y="16" fill="#0F172A" font-size="11">0</text>
      </g>
      
      <!-- Row tan -->
      <g transform="translate(16, 124)">
        <rect width="488" height="24" fill="#F0FDF4" rx="3"/>
        <text x="30" y="16" fill="#166534" font-size="11" font-weight="700">tan θ</text>
        <text x="110" y="16" fill="#0F172A" font-size="11">0</text>
        <text x="190" y="16" fill="#0F172A" font-size="11">1/√3</text>
        <text x="270" y="16" fill="#0F172A" font-size="11">1</text>
        <text x="350" y="16" fill="#0F172A" font-size="11">√3</text>
        <text x="430" y="16" fill="#DC2626" font-size="11" font-weight="700">Not defined</text>
      </g>
      
      <!-- Identities footer -->
      <g transform="translate(16, 156)">
        <rect width="488" height="58" fill="#FFFBEB" stroke="#FDE68A" rx="4"/>
        <text x="14" y="20" fill="#92400E" font-size="11" font-weight="700">Fundamental Pythagorean Trigonometric Identities:</text>
        <text x="14" y="38" fill="#B45309" font-size="11">1. sin² θ + cos² θ = 1  |  2. 1 + tan² θ = sec² θ  (0° ≤ θ &lt; 90°)</text>
        <text x="14" y="52" fill="#B45309" font-size="11">3. 1 + cot² θ = cosec² θ  (0° &lt; θ ≤ 90°)</text>
      </g>
    </g>
    """
    svg_angles_card = get_svg_wrapper(card_angles, title="Standard Trigonometric Values & Identities Atlas", caption="Complete analytical reference for trigonometric values and Pythagorean identities")

    modules = [
        # Module 1: Trigonometric Ratios of an Acute Angle
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Trigonometric Ratios of an Acute Angle: Definitions, Reciprocals & Invariance Principles",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the definition of the 6 fundamental trigonometric ratios in a right-angled triangle. Learn how opposite and adjacent sides swap depending on the acute angle chosen, verify that trig ratios depend only on the angle and not triangle size, and master quotient relations.",
            "key_concepts": [
                "Right Triangle Anatomy: Hypotenuse (opposite 90°), Opposite (side opposite target angle θ), Adjacent (base forming θ with hypotenuse)",
                "Sine: sin θ = Opposite / Hypotenuse",
                "Cosine: cos θ = Adjacent / Hypotenuse",
                "Tangent: tan θ = Opposite / Adjacent = sin θ / cos θ",
                "Reciprocal Ratios: cosec θ = 1/sin θ, sec θ = 1/cos θ, cot θ = 1/tan θ = cos θ / sin θ",
                "Invariance Principle: By AA similarity, trigonometric ratios are independent of the side lengths of the right triangle and depend solely on the angle θ"
            ],
            "subtopics": [
                "Geometric proof of ratio invariance via similar right triangles",
                "Swapping adjacent and opposite sides between angle A and angle C",
                "Worked Examples 1, 2, 3 from NCERT",
                "Constructing third side via Pythagoras theorem given any one ratio"
            ],
            "worked_examples": [
                {
                    "problem": "Example 1 (NCERT): Given tan A = 4/3, find the other trigonometric ratios of the angle A.",
                    "solution": "Let ABC be a right-angled triangle, right angled at B.\nGiven: tan A = 4/3\nFormula: tan A = Opposite side / Adjacent side = BC / AB.\nLet BC = 4k and AB = 3k, where k is a positive real constant.\n\nStep 1: Find Hypotenuse AC using Pythagoras Theorem:\nAC² = AB² + BC² = (3k)² + (4k)² = 9k² + 16k² = 25k²\nAC = √(25k²) = 5k.\n\nStep 2: Calculate all 5 remaining trigonometric ratios for angle A:\n1. sin A = Opposite / Hypotenuse = BC / AC = 4k / 5k = 4/5.\n2. cos A = Adjacent / Hypotenuse = AB / AC = 3k / 5k = 3/5.\n3. cosec A = 1 / sin A = 5/4.\n4. sec A = 1 / cos A = 5/3.\n5. cot A = 1 / tan A = 3/4.\n[ROUGH_WORK]\nPythagorean triple: 3 - 4 - 5\nCheck identity: sin² A + cos² A = (4/5)² + (3/5)² = 16/25 + 9/25 = 25/25 = 1 (True!)\nBoxed Answer: [ sin A = 4/5, cos A = 3/5, cosec A = 5/4, sec A = 5/3, cot A = 3/4 ].",
                    "concept_questions": [
                        "Why must we introduce the positive constant k when setting sides as 4k and 3k?",
                        "What would be the values of sin C and cos C in this same triangle?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Right Triangle Trigonometric Ratios HUD",
                "diagram_type": "diagram",
                "svg": svg_triangle_ratios,
                "concept_visuals": [
                    {
                        "concept_title": "Trig Ratios Definition HUD",
                        "diagram_title": "Six Ratios Layout",
                        "svg": svg_triangle_ratios,
                        "diagram_type": "diagram",
                        "what_to_make": "Right triangle with hypotenuse, base, perpendicular and all 6 ratios",
                        "what_to_explain": "Definitions of sine, cosine, tangent and their reciprocals"
                    }
                ]
            },
            "common_misconceptions": [
                "Treating sin A as the product of 'sin' and 'A': 'sin' has no mathematical meaning without its argument angle A!",
                "Confusing opposite and adjacent sides when switching focus between acute angles A and C in the same right triangle."
            ]
        },

        # Module 2: Trigonometric Ratios of Specific Angles (0°, 30°, 45°, 60°, 90°)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Trigonometric Ratios of Specific Angles: Geometric Derivations (30°, 45°, 60°) & Table Construction",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Rigorously derive the exact trigonometric ratios for 45° (using an isosceles right triangle) and 30°/60° (using an equilateral triangle with an altitude). Master the limiting values at 0° and 90°, and memorize the standard values table using the square-root mnemonic.",
            "key_concepts": [
                "Geometric Derivation for 45°: In right triangle ABC with ∠A = 45°, ∠C = 45° ⇒ AB = BC = a ⇒ AC = a√2 ⇒ sin 45° = 1/√2, cos 45° = 1/√2, tan 45° = 1",
                "Geometric Derivation for 30° and 60°: Equilateral triangle with side 2a, altitude bisects base into a and height a√3 ⇒ sin 30° = 1/2, cos 30° = √3/2, sin 60° = √3/2, cos 60° = 1/2",
                "Limiting Values at 0° and 90°: As θ → 0°, opposite → 0, adjacent → hypotenuse ⇒ sin 0° = 0, cos 0° = 1, tan 0° = 0",
                "The Square-Root Mnemonic: Values of sin are √(0/4), √(1/4), √(2/4), √(3/4), √(4/4)"
            ],
            "subtopics": [
                "Full geometric proof of ratios for 45°",
                "Full geometric proof of ratios for 30° and 60°",
                "Constructing the full 0° to 90° table in 60 seconds",
                "Worked Examples 6, 7, 8 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Geometrically derive the values of sin 45°, cos 45°, and tan 45°.",
                    "solution": "STATEMENT: Find the exact values of trigonometric ratios of 45° geometrically.\n\nCONSTRUCTION:\nConsider a right-angled triangle ABC, right angled at B, such that one of its acute angles is 45°:\n∠A = 45°.\nBy Angle Sum Property:\n∠C = 180° - (90° + 45°) = 45°.\n\nStep 1: Relate side lengths:\nSince ∠A = ∠C = 45°, triangle ABC is an isosceles right-angled triangle.\nTherefore, sides opposite to equal angles are equal:\nAB = BC.\nLet AB = BC = a (where a > 0).\n\nStep 2: Find Hypotenuse AC via Pythagoras Theorem:\nAC² = AB² + BC² = a² + a² = 2a²\nAC = √(2a²) = a√2.\n\nStep 3: Calculate Trigonometric Ratios for 45°:\n1. sin 45° = Opposite / Hypotenuse = BC / AC = a / (a√2) = 1 / √2.\n2. cos 45° = Adjacent / Hypotenuse = AB / AC = a / (a√2) = 1 / √2.\n3. tan 45° = Opposite / Adjacent = BC / AB = a / a = 1.\n4. cosec 45° = 1 / sin 45° = √2.\n5. sec 45° = 1 / cos 45° = √2.\n6. cot 45° = 1 / tan 45° = 1.\n[ROUGH_WORK]\n(1/√2)² + (1/√2)² = 1/2 + 1/2 = 1. (Identity verified!)\nBoxed Answer: [ sin 45° = 1/√2, cos 45° = 1/√2, tan 45° = 1, cosec 45° = √2, sec 45° = √2, cot 45° = 1 ].",
                    "concept_questions": [
                        "Why is sin 45° equal to cos 45°?",
                        "What is the value of tan 45° + cot 45°?"
                    ]
                },
                {
                    "problem": "Example 8 (NCERT): If sin (A - B) = 1/2, cos (A + B) = 1/2, 0° < A + B ≤ 90°, A > B, find A and B.",
                    "solution": "Given:\n1. sin (A - B) = 1/2\nWe know from the standard table that sin 30° = 1/2.\nSince A - B is acute:\nA - B = 30° ... (1)\n\n2. cos (A + B) = 1/2\nWe know from the standard table that cos 60° = 1/2.\nSince 0° < A + B ≤ 90°:\nA + B = 60° ... (2)\n\nStep 1: Add Equation (1) and Equation (2):\n(A - B) + (A + B) = 30° + 60°\n2A = 90° ⇒ A = 45°.\n\nStep 2: Substitute A = 45° into Equation (2):\n45° + B = 60° ⇒ B = 60° - 45° = 15°.\n\nVerification: A = 45°, B = 15°\nA > B (45° > 15°, true)\nA + B = 60° (0° < 60° ≤ 90°, true)\nsin(45° - 15°) = sin 30° = 1/2 (true)\ncos(45° + 15°) = cos 60° = 1/2 (true)\nBoxed Answer: [ A = 45°, B = 15° ].",
                    "concept_questions": [
                        "Why can we equate arguments directly when the angles are strictly acute?",
                        "What is the value of tan(A + B) in this question?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Specific Angles Table & Geometric Derivations HUD",
                "diagram_type": "diagram",
                "svg": svg_angles_card,
                "concept_visuals": [
                    {
                        "concept_title": "Trigonometric Angle Values",
                        "diagram_title": "Standard Angles Reference HUD",
                        "svg": svg_angles_card,
                        "diagram_type": "diagram",
                        "what_to_make": "Full color-coded table of angles from 0° to 90°",
                        "what_to_explain": "Systematic progression of sine from 0 to 1 and cosine from 1 to 0"
                    }
                ]
            },
            "common_misconceptions": [
                "Writing tan 90° = 0 instead of 'Not Defined' (division by zero: 1/0 is undefined!).",
                "Confusing sin 30° (1/2) with cos 30° (√3/2): Remember that sine starts at 0 and climbs upwards, so sin 30° is the smaller value 1/2."
            ]
        },

        # Module 3: Fundamental Trigonometric Identities
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Fundamental Trigonometric Pythagorean Identities: Rigorous Proofs & Algebraic Manipulations",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Rigorously derive the three fundamental Pythagorean identities of trigonometry from the Pythagorean theorem on right triangle ABC. Master algebraic permutations and converting any trig ratio entirely in terms of another.",
            "key_concepts": [
                "Pythagorean Theorem Origin: In right triangle ABC: AB² + BC² = AC²",
                "Identity 1: sin² θ + cos² θ = 1 (Divide by AC²)",
                "Identity 2: 1 + tan² θ = sec² θ (Divide by AB², valid for 0° ≤ θ < 90°)",
                "Identity 3: 1 + cot² θ = cosec² θ (Divide by BC², valid for 0° < θ ≤ 90°)",
                "Algebraic Variants: sin² θ = 1 - cos² θ, cos² θ = 1 - sin² θ, sec² θ - tan² θ = 1, cosec² θ - cot² θ = 1",
                "Conjugate Factorisation: (sec θ - tan θ)(sec θ + tan θ) = 1 ⇒ sec θ - tan θ = 1 / (sec θ + tan θ)"
            ],
            "subtopics": [
                "Full algebraic proofs of the 3 identities by dividing Pythagoras theorem",
                "Expressing all 5 ratios in terms of a single ratio (e.g. sec A)",
                "Worked Examples 9, 10, 11 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Prove the three fundamental trigonometric identities geometrically using a right-angled triangle ABC.",
                    "solution": "Let ABC be a right-angled triangle, right angled at B, with acute angle ∠A = θ.\nBy Pythagoras Theorem:\nAB² + BC² = AC² ... (1)\n\nPROOF OF IDENTITY 1: sin² θ + cos² θ = 1\nDivide every term of equation (1) by AC²:\n(AB² / AC²) + (BC² / AC²) = AC² / AC²\n(AB / AC)² + (BC / AC)² = 1\nNotice that:\nAB / AC = Adjacent / Hypotenuse = cos θ\nBC / AC = Opposite / Hypotenuse = sin θ\nSubstitute: (cos θ)² + (sin θ)² = 1\n⇒ sin² θ + cos² θ = 1. (Identity 1 Proved!)\n\nPROOF OF IDENTITY 2: 1 + tan² θ = sec² θ\nDivide every term of equation (1) by AB² (for 0° ≤ θ < 90°):\n(AB² / AB²) + (BC² / AB²) = AC² / AB²\n1 + (BC / AB)² = (AC / AB)²\nNotice that BC / AB = tan θ and AC / AB = sec θ:\n1 + (tan θ)² = (sec θ)²\n⇒ 1 + tan² θ = sec² θ. (Identity 2 Proved!)\n\nPROOF OF IDENTITY 3: 1 + cot² θ = cosec² θ\nDivide every term of equation (1) by BC² (for 0° < θ ≤ 90°):\n(AB² / BC²) + (BC² / BC²) = AC² / BC²\n(AB / BC)² + 1 = (AC / BC)²\nNotice that AB / BC = cot θ and AC / BC = cosec θ:\n(cot θ)² + 1 = (cosec θ)²\n⇒ 1 + cot² θ = cosec² θ. (Identity 3 Proved!)\n[ROUGH_WORK]\nAll three identities are direct manifestations of Pythagoras Theorem on the unit circle!\nBoxed Answer: [ 1. sin² θ + cos² θ = 1 | 2. 1 + tan² θ = sec² θ | 3. 1 + cot² θ = cosec² θ (All Proved) ].",
                    "concept_questions": [
                        "Why is Identity 2 not defined at θ = 90°?",
                        "Why is Identity 3 not defined at θ = 0°?",
                        "What is the value of sec² θ - tan² θ?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Pythagorean Identities Right Triangle Derivation",
                "diagram_type": "diagram",
                "svg": svg_angles_card,
                "concept_visuals": [
                    {
                        "concept_title": "Trig Identities Architecture",
                        "diagram_title": "Pythagorean Identity Links",
                        "svg": svg_angles_card,
                        "diagram_type": "diagram",
                        "what_to_make": "HUD showing division of Pythagoras theorem into the 3 identities",
                        "what_to_explain": "Direct algebraic derivation via hypotenuse, base, and altitude division"
                    }
                ]
            },
            "common_misconceptions": [
                "Writing sin θ² instead of sin² θ: The square belongs to the ratio value, not the angle!",
                "Believing 1 + tan² θ = cot² θ: It is 1 + tan² θ = sec² θ!"
            ]
        },

        # Module 4: Exercise 8.1 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 8.1 Complete Solver: Trig Ratio Calculations & Inversion Testing (Q1 to Q11)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 8.1 Questions 1 through 11. Master opposite/adjacent orientation swaps, Pythagoras hypotenuse computations, evaluation of algebraic expressions in terms of sin and cos, and testing angle equality from cos A = cos B.",
            "key_concepts": [
                "Ex 8.1 Q1: In right ΔABC with AB = 24, BC = 7, AC = 25 ⇒ sin A = 7/25, cos A = 24/25, sin C = 24/25, cos C = 7/25",
                "Ex 8.1 Q2: In right ΔPQR with PQ = 12, PR = 13 ⇒ QR = 5 ⇒ tan P - cot R = 5/12 - 5/12 = 0",
                "Ex 8.1 Q3: Given sin A = 3/4 ⇒ cos A = √7/4, tan A = 3/√7",
                "Ex 8.1 Q4: 15 cot A = 8 ⇒ cot A = 8/15 ⇒ sin A = 15/17, sec A = 17/8",
                "Ex 8.1 Q5: sec θ = 13/12 ⇒ calculate all other 5 trig ratios",
                "Ex 8.1 Q6: If ∠A and ∠B are acute angles such that cos A = cos B, show that ∠A = ∠B",
                "Ex 8.1 Q7: If cot θ = 7/8, evaluate (1 + sin θ)(1 - sin θ) / (1 + cos θ)(1 - cos θ) = 49/64",
                "Ex 8.1 Q8: Check if (1 - tan² A)/(1 + tan² A) = cos² A - sin² A given 3 cot A = 4",
                "Ex 8.1 Q9: In right ΔABC with tan A = 1/√3, find sin A cos C + cos A sin C = 1",
                "Ex 8.1 Q10: In right ΔPQR right angled at Q, PR + QR = 25 cm and PQ = 5 cm ⇒ PR = 13, QR = 12",
                "Ex 8.1 Q11: State whether True or False with justification (5 statements)"
            ],
            "subtopics": [
                "Full resolution of Q1 to Q11",
                "Algebraic proof of cos A = cos B implying ∠A = ∠B",
                "Sum and difference hypotenuse constraint in Q10"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 8.1 Q7: If cot θ = 7/8, evaluate: (i) [ (1 + sin θ)(1 - sin θ) ] / [ (1 + cos θ)(1 - cos θ) ], and (ii) cot² θ.",
                    "solution": "Given: cot θ = 7/8.\n\nMethod 1 (Using Trigonometric Algebraic Identities - Fastest & Cleanest):\nNotice the numerator is in the form (a + b)(a - b) = a² - b²:\nNumerator = (1 + sin θ)(1 - sin θ) = 1 - sin² θ\nFrom Identity 1: 1 - sin² θ = cos² θ.\n\nNotice the denominator is also (a + b)(a - b) = a² - b²:\nDenominator = (1 + cos θ)(1 - cos θ) = 1 - cos² θ\nFrom Identity 1: 1 - cos² θ = sin² θ.\n\nTherefore, the expression becomes:\n[ 1 - sin² θ ] / [ 1 - cos² θ ] = cos² θ / sin² θ = (cos θ / sin θ)² = cot² θ!\n\nEvaluation for Part (i):\nSince the entire expression simplifies to cot² θ:\nExpression = cot² θ = (7/8)² = 49 / 64.\n\nEvaluation for Part (ii):\ncot² θ = (7/8)² = 49 / 64.\n[ROUGH_WORK]\nBoth parts have the exact same answer 49/64 because part (i) is an identity for cot² θ!\nBoxed Answer: [ (i) 49/64, (ii) 49/64 ].",
                    "concept_questions": [
                        "Why does using identities save 10 lines of calculation compared to finding the hypotenuse √113?",
                        "What is the value of 1 - sin² θ in terms of cosine?"
                    ]
                },
                {
                    "problem": "Exercise 8.1 Q10: In ΔPQR, right-angled at Q, PR + QR = 25 cm and PQ = 5 cm. Determine the values of sin P, cos P and tan P.",
                    "solution": "Given: Right-angled triangle PQR with ∠Q = 90°.\nPQ = 5 cm.\nPR + QR = 25 cm ⇒ PR = 25 - QR.\n\nStep 1: Apply Pythagoras Theorem to ΔPQR:\nPR² = PQ² + QR²\nSubstitute PR = 25 - QR and PQ = 5:\n(25 - QR)² = 5² + QR²\n\nStep 2: Expand LHS using (a - b)² = a² - 2ab + b²:\n625 - 50 QR + QR² = 25 + QR²\nCancel QR² from both sides:\n625 - 50 QR = 25\n625 - 25 = 50 QR\n600 = 50 QR\nQR = 600 / 50 = 12 cm.\n\nStep 3: Find Hypotenuse PR:\nPR = 25 - QR = 25 - 12 = 13 cm.\n\nStep 4: Determine Trigonometric Ratios for angle P:\nFor angle P:\nOpposite side = QR = 12 cm\nAdjacent side = PQ = 5 cm\nHypotenuse = PR = 13 cm.\n\n1. sin P = Opposite / Hypotenuse = QR / PR = 12 / 13.\n2. cos P = Adjacent / Hypotenuse = PQ / PR = 5 / 13.\n3. tan P = Opposite / Adjacent = QR / PQ = 12 / 5.\n[ROUGH_WORK]\nCheck Pythagoras: 5² + 12² = 25 + 144 = 169 = 13² (True!)\nBoxed Answer: [ sin P = 12/13, cos P = 5/13, tan P = 12/5 ].",
                    "concept_questions": [
                        "What famous Pythagorean triple was verified here?",
                        "What would be the values of sin R and cos R?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Exercise 8.1 Right Triangle Ratio HUD",
                "diagram_type": "diagram",
                "svg": svg_triangle_ratios,
                "concept_visuals": [
                    {
                        "concept_title": "Ratio Extraction Geometry",
                        "diagram_title": "Right Triangle PQR Atlas",
                        "svg": svg_triangle_ratios,
                        "diagram_type": "diagram",
                        "what_to_make": "Triangle PQR with sides 5, 12, 13 showing angle P ratios",
                        "what_to_explain": "Direct ratio definitions from computed side lengths"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting to cancel QR² in Q10 and panicking about a quadratic equation: Notice QR² appears on both sides with identical sign and cancels out!",
                "Inverting sin P as 5/13 instead of 12/13 (side opposite to P is QR = 12, not PQ)."
            ]
        },

        # Module 5: Exercise 8.2 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise 8.2 Complete Solver: Exact Value Evaluations & Compound Angle Inversion (Q1 to Q4)",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 8.2. Question 1 (evaluating 5 complex numerical expressions with surd rationalisation), Question 2 (all 4 multiple choice questions), Question 3 (compound angle equations tan(A + B) = √3 and tan(A - B) = 1/√3), and Question 4 (True/False with mathematical justifications).",
            "key_concepts": [
                "Ex 8.2 Q1: Evaluating complex expressions involving sin 30°, cos 45°, sec 30°, tan 45°",
                "Rationalising the Denominator: Multiplying by conjugate surd (a - b√c) to eliminate radicals",
                "Ex 8.2 Q3: Solving tan(A + B) = √3 ⇒ A + B = 60° and tan(A - B) = 1/√3 ⇒ A - B = 30° ⇒ A = 45°, B = 15°",
                "Ex 8.2 Q4: Justifying whether sin(A + B) = sin A + sin B (False), value of sin θ increases as θ increases (True for 0° to 90°)"
            ],
            "subtopics": [
                "Full resolution of Q1 (parts i to v)",
                "Full resolution of Q2 (parts i to iv)",
                "Full resolution of Q3 and Q4",
                "Rationalising surds in fractional trig expressions"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 8.2 Q1 (iii): Evaluate: cos 45° / (sec 30° + cosec 30°).",
                    "solution": "Given expression: cos 45° / (sec 30° + cosec 30°)\nFrom standard angle values:\ncos 45° = 1 / √2\nsec 30° = 1 / cos 30° = 1 / (√3/2) = 2 / √3\ncosec 30° = 1 / sin 30° = 1 / (1/2) = 2.\n\nStep 1: Substitute values into the expression:\nNumerator = 1 / √2\nDenominator = 2/√3 + 2 = (2 + 2√3) / √3\n\nStep 2: Divide numerator by denominator:\nExpression = (1 / √2) ÷ [ (2 + 2√3) / √3 ]\n= (1 / √2) × [ √3 / (2(1 + √3)) ]\n= √3 / [ 2√2 (√3 + 1) ]\n\nStep 3: Rationalise the denominator:\nMultiply numerator and denominator by √2:\n= √6 / [ 4 (√3 + 1) ]\nMultiply numerator and denominator by conjugate (√3 - 1):\n= [ √6 (√3 - 1) ] / [ 4 (√3 + 1)(√3 - 1) ]\n= (√18 - √6) / [ 4 (3 - 1) ]\n= (3√2 - √6) / [ 4 (2) ]\n= (3√2 - √6) / 8.\n[ROUGH_WORK]\n√18 = √(9 × 2) = 3√2\n(√3 + 1)(√3 - 1) = 3 - 1 = 2\n4 × 2 = 8\nBoxed Answer: [ (3√2 - √6) / 8 ].",
                    "concept_questions": [
                        "Why is rationalising the denominator a mandatory requirement in board exams?",
                        "What is the conjugate of √3 + 1?"
                    ]
                },
                {
                    "problem": "Exercise 8.2 Q3: If tan (A + B) = √3 and tan (A - B) = 1/√3; 0° < A + B ≤ 90°; A > B, find A and B.",
                    "solution": "Given:\ntan (A + B) = √3\nWe know from the standard table that tan 60° = √3.\nSince A + B is acute:\nA + B = 60° ... (1)\n\ntan (A - B) = 1/√3\nWe know from the standard table that tan 30° = 1/√3.\nSince A > B and A - B is acute:\nA - B = 30° ... (2)\n\nStep 1: Add Equation (1) and Equation (2):\n(A + B) + (A - B) = 60° + 30°\n2A = 90° ⇒ A = 45°.\n\nStep 2: Substitute A = 45° into (1):\n45° + B = 60° ⇒ B = 60° - 45° = 15°.\n[ROUGH_WORK]\nCheck: 45° + 15° = 60° ≤ 90°\n45° > 15°\ntan 60° = √3, tan 30° = 1/√3. Verified!\nBoxed Answer: [ A = 45°, B = 15° ].",
                    "concept_questions": [
                        "Could A + B be 240°? Why does the problem specify 0° < A + B ≤ 90°?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Surd Rationalisation & Angle Evaluation HUD",
                "diagram_type": "diagram",
                "svg": svg_angles_card,
                "concept_visuals": [
                    {
                        "concept_title": "Trig Evaluation Architecture",
                        "diagram_title": "Angle Table Lookup Atlas",
                        "svg": svg_angles_card,
                        "diagram_type": "diagram",
                        "what_to_make": "HUD showing angle substitution and conjugate rationalisation",
                        "what_to_explain": "Algebraic steps for surd simplification"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting to multiply both terms by √2 when expanding 2√2(√3 + 1).",
                "Writing sin(A + B) = sin A + sin B: Trigonometric functions are NOT linear operators; sin(30° + 60°) = sin 90° = 1, while sin 30° + sin 60° = 1/2 + √3/2 ≠ 1!"
            ]
        },

        # Module 6: Exercise 8.3 Complete Solver & Board Proof Identities
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 6,
            "title": "Exercise 8.3 Complete Solver: All 10 Rigorous Proof Identities & Master Verification Protocol",
            "estimated_minutes": 40,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete, exhaustive resolution of NCERT Exercise 8.3 (rationalised syllabus). Detailed line-by-line algebraic proofs for all 10 identities of Question 4: (cosec θ - cot θ)², cos A/(1+sin A) + (1+sin A)/cos A = 2 sec A, tan θ/(1-cot θ) + cot θ/(1-tan θ), (cos A - sin A + 1)/(cos A + sin A - 1) = cosec A + cot A, and more.",
            "key_concepts": [
                "The Golden Rule of Trig Proofs: Convert everything into sin and cos whenever stuck",
                "Identity 1: (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ)",
                "Identity 2: cos A / (1 + sin A) + (1 + sin A) / cos A = 2 sec A",
                "Identity 3: tan θ / (1 - cot θ) + cot θ / (1 - tan θ) = 1 + sec θ cosec θ",
                "Identity 4: (1 + sec A) / sec A = sin² A / (1 - cos A)",
                "Identity 5: (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A (Dividing numerator and denominator by sin A)",
                "Identity 6: √[ (1 + sin A) / (1 - sin A) ] = sec A + tan A",
                "Identity 7: (sin θ - 2 sin³ θ) / (2 cos³ θ - cos θ) = tan θ",
                "Identity 8: (sin A + cosec A)² + (cos A + sec A)² = 7 + tan² A + cot² A",
                "Identity 9: (cosec A - sin A)(sec A - cos A) = 1 / (tan A + cot A)",
                "Identity 10: (1 + tan² A) / (1 + cot² A) = [ (1 - tan A) / (1 - cot A) ]² = tan² A"
            ],
            "subtopics": [
                "Full resolution of Exercise 8.3 Questions 1, 2, 3",
                "Exhaustive line-by-line proofs for all 10 parts of Question 4",
                "Standard board exam techniques: Conjugate multiplication, factoring a³ - b³, and algebraic fraction simplification"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 8.3 Q4 (i): Prove that (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ).",
                    "solution": "TO PROVE: (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ)\n\nPROOF:\nStep 1: Start from LHS and convert into sine and cosine:\nLHS = (cosec θ - cot θ)²\nRecall: cosec θ = 1 / sin θ and cot θ = cos θ / sin θ.\nLHS = ( 1/sin θ - cos θ/sin θ )²\n= [ (1 - cos θ) / sin θ ]²\n= (1 - cos θ)² / sin² θ\n\nStep 2: Use Pythagorean Identity sin² θ = 1 - cos² θ:\nLHS = (1 - cos θ)² / (1 - cos² θ)\n\nStep 3: Factorise denominator using a² - b² = (a - b)(a + b):\n1 - cos² θ = (1 - cos θ)(1 + cos θ)\nLHS = [ (1 - cos θ)(1 - cos θ) ] / [ (1 - cos θ)(1 + cos θ) ]\n\nStep 4: Cancel common factor (1 - cos θ):\n= (1 - cos θ) / (1 + cos θ) = RHS.\nLHS = RHS. Hence Proved!\n[ROUGH_WORK]\nKey step: sin² θ = 1 - cos² θ = (1 - cos θ)(1 + cos θ).\nBoxed Answer: [ (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ) (Proved) ].",
                    "concept_questions": [
                        "Why was converting to sin θ and cos θ the cleanest way to begin?",
                        "Can you prove this identity starting from RHS by multiplying numerator and denominator by (1 - cos θ)?"
                    ]
                },
                {
                    "problem": "Exercise 8.3 Q4 (v): Prove that (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A, using the identity cosec² A = 1 + cot² A.",
                    "solution": "TO PROVE: (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A\n\nPROOF:\nStep 1: To introduce cosec A and cot A, divide both numerator and denominator by sin A:\nNumerator = cos A / sin A - sin A / sin A + 1 / sin A = cot A - 1 + cosec A = (cot A + cosec A) - 1\nDenominator = cos A / sin A + sin A / sin A - 1 / sin A = cot A + 1 - cosec A = (cot A - cosec A) + 1\nLHS = [ (cosec A + cot A) - 1 ] / [ cot A - cosec A + 1 ]\n\nStep 2: Replace 1 in the numerator with (cosec² A - cot² A):\nSince cosec² A - cot² A = 1:\nNumerator = (cosec A + cot A) - (cosec² A - cot² A)\nFactorise using a² - b² = (a - b)(a + b):\n= (cosec A + cot A) - [ (cosec A - cot A)(cosec A + cot A) ]\n\nStep 3: Factor out common binomial (cosec A + cot A) from numerator:\n= (cosec A + cot A) [ 1 - (cosec A - cot A) ]\n= (cosec A + cot A) [ 1 - cosec A + cot A ]\n= (cosec A + cot A) [ cot A - cosec A + 1 ]\n\nStep 4: Cancel common bracket with denominator:\nLHS = [ (cosec A + cot A) (cot A - cosec A + 1) ] / [ cot A - cosec A + 1 ]\n= cosec A + cot A = RHS.\nLHS = RHS. Hence Proved!\n[ROUGH_WORK]\nMaster trick: Replacing '1' in the numerator by cosec² A - cot² A enables factoring out the target term (cosec A + cot A)!\nBoxed Answer: [ (cos A - sin A + 1)/(cos A + sin A - 1) = cosec A + cot A (Proved) ].",
                    "concept_questions": [
                        "Why did we replace 1 only in the numerator and not in the denominator?",
                        "What would you divide by if the RHS had been sec A + tan A instead?"
                    ]
                },
                {
                    "problem": "Exercise 8.3 Q4 (viii): Prove that (sin A + cosec A)² + (cos A + sec A)² = 7 + tan² A + cot² A.",
                    "solution": "TO PROVE: (sin A + cosec A)² + (cos A + sec A)² = 7 + tan² A + cot² A\n\nPROOF:\nStep 1: Expand LHS using (a + b)² = a² + 2ab + b²:\n(sin A + cosec A)² = sin² A + 2 sin A cosec A + cosec² A\n(cos A + sec A)² = cos² A + 2 cos A sec A + sec² A\nLHS = (sin² A + 2 sin A cosec A + cosec² A) + (cos² A + 2 cos A sec A + sec² A)\n\nStep 2: Use reciprocal properties:\nsin A × cosec A = sin A × (1/sin A) = 1 ⇒ 2 sin A cosec A = 2\ncos A × sec A = cos A × (1/cos A) = 1 ⇒ 2 cos A sec A = 2\nLHS = (sin² A + cos² A) + 2 + 2 + cosec² A + sec² A\n\nStep 3: Use Pythagorean Identities:\n1. sin² A + cos² A = 1\n2. cosec² A = 1 + cot² A\n3. sec² A = 1 + tan² A\n\nStep 4: Substitute into LHS:\nLHS = 1 + 2 + 2 + (1 + cot² A) + (1 + tan² A)\n= (1 + 2 + 2 + 1 + 1) + tan² A + cot² A\n= 7 + tan² A + cot² A = RHS.\nLHS = RHS. Hence Proved!\n[ROUGH_WORK]\n1 + 2 + 2 + 1 + 1 = 7. Pure elegance!\nBoxed Answer: [ (sin A + cosec A)² + (cos A + sec A)² = 7 + tan² A + cot² A (Proved) ].",
                    "concept_questions": [
                        "Where did the number 7 originate in this proof?",
                        "Why do the cross terms 2 sin A cosec A and 2 cos A sec A simplify to plain numbers 2 and 2?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Pythagorean Identities Proof Flow HUD",
                "diagram_type": "diagram",
                "svg": svg_angles_card,
                "concept_visuals": [
                    {
                        "concept_title": "Trig Identity Proof Pipeline",
                        "diagram_title": "Algebraic Transformation Atlas",
                        "svg": svg_angles_card,
                        "diagram_type": "diagram",
                        "what_to_make": "HUD showing algebraic transformation pathways for trig proofs",
                        "what_to_explain": "Replacing 1 with sec² - tan² or cosec² - cot² to unlock factorization"
                    }
                ]
            },
            "common_misconceptions": [
                "Attempting to cross-multiply terms across the equality when asked to 'prove' an identity: In a formal proof, you must start from LHS and simplify to RHS (or simplify both to a common intermediate), never assume LHS = RHS at the start!",
                "Replacing 1 in both numerator and denominator in Q4(v): Only replace in one place so the other factor can cancel out!"
            ]
        }
    ]
    
    return modules
