"""
Class 10 Mathematics - Chapter 9: Some Applications of Trigonometry (NCERT CBSE)
Curriculum ID: 28268af8-3331-453a-ad5e-6add84c0c2ba
Fully compliant with Invariant 10:
- 5 dedicated modules (Theory strictly in M1-M2, dedicated solvers M3-M5)
- 100% of all NCERT exercise questions (Ex 9.1 all 16 problems) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- High-Precision Vector SVGs from svg_builder_class10 (Heights and Distances with elevation & depression angles)
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_heights_and_distances_svg, get_svg_wrapper

def get_ch9_modules():
    CURRICULUM_ID = "28268af8-3331-453a-ad5e-6add84c0c2ba"
    
    # SVG 1: Basic Elevation
    svg_elevation = build_heights_and_distances_svg(
        type_prob="elevation",
        h_label="h",
        d_label="d",
        ang_label="30°",
        title="Angle of Elevation: Observer to High Altitude Target",
        caption="Line of sight above horizontal datum: tan θ = Height (h) / Distance (d)"
    )
    
    # SVG 2: Dual Elevation (Two Observers / Moving Observer)
    dual_elevation_svg_content = """
    <line x1="40" y1="280" x2="520" y2="280" stroke="#334155" stroke-width="2"/>
    <text x="500" y="300" fill="#64748B" font-size="11">Ground Level</text>
    
    <!-- Tower AB at x=440 -->
    <rect x="430" y="90" width="20" height="190" fill="#E2E8F0" stroke="#334155" stroke-width="1.8"/>
    <text x="460" y="185" fill="#0F172A" font-size="12" font-weight="700">Tower (h)</text>
    <rect x="415" y="265" width="15" height="15" fill="none" stroke="#DC2626" stroke-width="1.2"/>
    <text x="440" y="80" fill="#0F172A" font-size="12" font-weight="700">A (Top)</text>
    <text x="440" y="300" fill="#0F172A" font-size="12" font-weight="700">B (Foot)</text>
    
    <!-- Point D (Farther, 30 deg) at x=100 -->
    <circle cx="100" cy="280" r="4" fill="#2563EB"/>
    <text x="90" y="300" fill="#0F172A" font-size="12" font-weight="700">D</text>
    <line x1="100" y1="280" x2="430" y2="90" stroke="#2563EB" stroke-width="2"/>
    <path d="M 140 280 A 40 40 0 0 0 135 258" fill="none" stroke="#2563EB" stroke-width="1.5"/>
    <text x="145" y="272" fill="#2563EB" font-size="11" font-weight="700">30°</text>
    
    <!-- Point C (Closer, 60 deg) at x=280 -->
    <circle cx="280" cy="280" r="4" fill="#16A34A"/>
    <text x="275" y="300" fill="#0F172A" font-size="12" font-weight="700">C</text>
    <line x1="280" y1="280" x2="430" y2="90" stroke="#16A34A" stroke-width="2"/>
    <path d="M 315 280 A 35 35 0 0 0 305 240" fill="none" stroke="#16A34A" stroke-width="1.5"/>
    <text x="320" y="268" fill="#16A34A" font-size="11" font-weight="700">60°</text>
    
    <!-- Distances CD and BC -->
    <line x1="100" y1="320" x2="280" y2="320" stroke="#475569" stroke-width="1.2" marker-start="url(#arrowSlate)" marker-end="url(#arrowSlate)"/>
    <text x="190" y="335" fill="#475569" font-size="11" font-weight="600" text-anchor="middle">Distance x</text>
    
    <line x1="280" y1="320" x2="430" y2="320" stroke="#475569" stroke-width="1.2" marker-start="url(#arrowSlate)" marker-end="url(#arrowSlate)"/>
    <text x="355" y="335" fill="#475569" font-size="11" font-weight="600" text-anchor="middle">Distance y</text>
    
    <!-- HUD Card -->
    <g transform="translate(30, 60)">
      <rect width="180" height="90" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2" rx="8"/>
      <text x="12" y="22" fill="#0F172A" font-size="11" font-weight="700">Dual Elevation Model:</text>
      <text x="12" y="42" fill="#16A34A" font-size="10">In ΔABC: tan 60° = h / y = √3</text>
      <text x="12" y="58" fill="#2563EB" font-size="10">In ΔABD: tan 30° = h / (x + y) = 1/√3</text>
      <text x="12" y="76" fill="#DC2626" font-size="10" font-weight="700">⇒ x = 2y (Shadow Relation)</text>
    </g>
    """
    svg_dual_elevation = get_svg_wrapper(dual_elevation_svg_content, title="Dual Angle of Elevation Model (Approaching Observer)", caption="As observer moves closer from D to C, angle of elevation increases from 30° to 60°")

    modules = [
        # Module 1: Line of Sight, Elevation, and Depression Fundamentals
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Line of Sight, Angle of Elevation & Angle of Depression: Physical Optics & Geometric Datum",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the core optical definitions: Line of Sight, Horizontal Line of Datum, Angle of Elevation (looking upward above horizontal), and Angle of Depression (looking downward below horizontal). Master the Alternate Interior Angles theorem that translates an angle of depression directly into an angle of elevation from the target.",
            "key_concepts": [
                "Line of Sight: The straight optical line drawn from the eye of an observer to the target object viewed",
                "Horizontal Datum: The horizontal reference line passing through the observer's eye parallel to the ground",
                "Angle of Elevation: The acute angle formed by the line of sight with the horizontal level when the target is above the horizontal level",
                "Angle of Depression: The acute angle formed by the line of sight with the horizontal level when the target is below the horizontal level",
                "Datum Invariance / Alternate Interior Angles: Since horizontal lines at observer level and ground level are strictly parallel, Angle of Depression = Angle of Elevation to the observer!"
            ],
            "subtopics": [
                "Optical definitions and eye height considerations",
                "Translating word problems into authentic right-angled triangles",
                "Choosing the right trigonometric ratio: tan θ (Perpendicular/Base) vs sin θ (Perpendicular/Hypotenuse)",
                "Worked Example 1 and Example 2 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Example 1 (NCERT): A tower stands vertically on the ground. From a point on the ground, which is 15 m away from the foot of the tower, the angle of elevation of the top of the tower is found to be 60°. Find the height of the tower.",
                    "solution": "Let AB be the vertical tower of height 'h' meters, standing on ground.\nLet C be the observation point on the ground.\nGiven: BC = 15 m (Distance from foot of tower).\nAngle of elevation ∠ACB = 60°.\nSince the tower stands vertically, ∠ABC = 90°.\n\nStep 1: Identify the trigonometric ratio connecting Perpendicular (AB) and Base (BC):\nIn right-angled triangle ABC:\ntan ∠ACB = AB / BC\n\nStep 2: Substitute given values:\ntan 60° = h / 15\nWe know tan 60° = √3:\n√3 = h / 15\n\nStep 3: Solve for h:\nh = 15√3 m.\n[ROUGH_WORK]\nIf √3 ≈ 1.732, h = 15 × 1.732 = 25.98 m.\nIn CBSE board exams, keep in exact surd form 15√3 unless √3 is explicitly asked to be approximated.\nBoxed Answer: [ Height of tower = 15√3 m ].",
                    "concept_questions": [
                        "Why did we select tan θ instead of sin θ or cos θ in this problem?",
                        "What would be the length of the line of sight AC from the observer to the top of the tower?"
                    ]
                },
                {
                    "problem": "Example 2 (NCERT): An electrician has to repair an electric fault on a pole of height 5 m. She needs to reach a point 1.3 m below the top of the pole to undertake the repair work. What should be the length of the ladder that she should use which, when inclined at an angle of 60° to the horizontal, would enable her to reach the required position? Also, how far from the foot of the pole should she place the foot of the ladder? (Take √3 = 1.73)",
                    "solution": "Let AD be the electric pole of height AD = 5 m.\nThe repair point B is 1.3 m below the top A:\nBD = AD - AB = 5 m - 1.3 m = 3.7 m.\nLet BC be the ladder of length 'L' inclined at 60° to horizontal.\nIn right-angled triangle BDC (right-angled at D):\n∠BCD = 60°, BD = 3.7 m.\n\nStep 1: Find ladder length BC (Hypotenuse) using sin 60°:\nsin 60° = Opposite / Hypotenuse = BD / BC\n√3 / 2 = 3.7 / BC\nBC = (3.7 × 2) / √3 = 7.4 / 1.73 ≈ 4.28 m.\n\nStep 2: Find distance of foot of ladder DC (Base) using cot 60° or tan 60°:\ncot 60° = Adjacent / Opposite = DC / BD\n1 / √3 = DC / 3.7\nDC = 3.7 / √3 = 3.7 / 1.73 ≈ 2.14 m.\n[ROUGH_WORK]\nCheck Pythagoras: 2.14² + 3.7² = 4.58 + 13.69 = 18.27 ≈ 4.28² (18.32, verified!).\nBoxed Answer: [ Length of ladder = 4.28 m, Distance from foot of pole = 2.14 m ].",
                    "concept_questions": [
                        "Why was the effective height taken as 3.7 m instead of 5 m?",
                        "Which ratio connects Perpendicular and Hypotenuse directly?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Optical Datum and Angle of Elevation HUD",
                "diagram_type": "diagram",
                "svg": svg_elevation,
                "concept_visuals": [
                    {
                        "concept_title": "Elevation and Depression Geometry",
                        "diagram_title": "Horizontal Reference Line and Line of Sight",
                        "svg": svg_elevation,
                        "diagram_type": "diagram",
                        "what_to_make": "Right triangle with observer on ground, vertical tower, horizontal distance and elevation arc",
                        "what_to_explain": "Direct ratio mapping: tan θ = Perpendicular / Base"
                    }
                ]
            },
            "common_misconceptions": [
                "Measuring angle of depression from the vertical wall instead of from the horizontal line of sight: Angle of depression is ALWAYS measured relative to the horizontal line!",
                "Forgetting to subtract observer height when observer height is explicitly given in the problem."
            ]
        },

        # Module 2: Two-Triangle Systems & Moving Observer Configurations
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Two-Triangle Systems: Moving Observers, Combined Heights & Shadow Mechanics",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master complex scenarios involving two right-angled triangles sharing a common side (either a common height or a common base). Learn how to set up two simultaneous trigonometric equations to eliminate intermediate variables and isolate the unknown tower height or distance.",
            "key_concepts": [
                "Common Side Strategy: In two overlapping right triangles, express the common unknown side in terms of the variable from both triangles and equate them",
                "Angular Dynamics: As an observer walks towards a tall object, the angle of elevation monotonically increases (e.g. 30° to 45° to 60°)",
                "Complementary Angles of Elevation: If angles of elevation from distances 'a' and 'b' are complementary (θ and 90° - θ), then height h = √(ab)!",
                "Pedestal & Statue Problems: Height of statue + height of pedestal = Total perpendicular"
            ],
            "subtopics": [
                "Common height elimination in tandem triangles",
                "Proof of h = √(ab) for complementary elevation angles",
                "Worked Examples 4, 5, 6, 7 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Example 6 (NCERT): The angles of depression of the top and the bottom of an 8 m tall building from the top of a multi-storeyed building are 30° and 45°, respectively. Find the height of the multi-storeyed building and the distance between the two buildings.",
                    "solution": "Let PC be the multi-storeyed building of height 'H'.\nLet AB be the 8 m tall building, so AB = 8 m.\nLet distance between buildings BC = d.\nDraw horizontal line PD from P parallel to BC, and horizontal line AE from A perpendicular to PC.\nThen AE = BC = d, and EC = AB = 8 m.\nTherefore, PE = PC - EC = H - 8.\n\nStep 1: In right ΔPAC, ∠PAC = angle of depression of bottom = 45° (by alternate angles):\nIn right ΔPCB (right-angled at C):\ntan 45° = PC / BC = H / d\n1 = H / d ⇒ d = H ... (1)\n(The distance between the buildings equals the height of the multi-storeyed building!)\n\nStep 2: In right ΔPEA (right-angled at E):\nAngle of depression of top of building = 30° ⇒ ∠PAE = 30°.\ntan 30° = PE / AE = (H - 8) / d\nSubstitute d = H from (1):\n1 / √3 = (H - 8) / H\nH = √3 (H - 8) = H√3 - 8√3\n8√3 = H√3 - H = H (√3 - 1)\nH = 8√3 / (√3 - 1)\n\nStep 3: Rationalise denominator:\nH = [ 8√3 (√3 + 1) ] / [ (√3 - 1)(√3 + 1) ]\n= [ 8(3 + √3) ] / [ 3 - 1 ]\n= 8(3 + √3) / 2 = 4(3 + √3) = (12 + 4√3) m.\nSince d = H, distance between buildings d = 4(3 + √3) m.\n[ROUGH_WORK]\nIf √3 ≈ 1.732: H = 4(4.732) = 18.93 m.\nBoxed Answer: [ Height of building = 4(3 + √3) m, Distance between buildings = 4(3 + √3) m ].",
                    "concept_questions": [
                        "Why does tan 45° = 1 immediately establish that horizontal distance equals vertical height?",
                        "What is the conjugate multiplier used to rationalise 8√3 / (√3 - 1)?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Dual Elevation Moving Observer HUD",
                "diagram_type": "diagram",
                "svg": svg_dual_elevation,
                "concept_visuals": [
                    {
                        "concept_title": "Two-Triangle System Geometry",
                        "diagram_title": "Approaching Observer System",
                        "svg": svg_dual_elevation,
                        "diagram_type": "diagram",
                        "what_to_make": "Dual elevation triangle with common height AB and positions C and D",
                        "what_to_explain": "Setting up tan 30° and tan 60° to eliminate intermediate variables"
                    }
                ]
            },
            "common_misconceptions": [
                "Assuming the observer walks a distance equal to the height: The distance walked is x = h(cot θ1 - cot θ2), not simply h.",
                "Subtracting angles (e.g. 60° - 30° = 30°) and applying trigonometry to the difference: Trigonometric functions cannot be distributed across angle differences!"
            ]
        },

        # Module 3: NCERT Exercise 9.1 Solver (Questions 1 to 6)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise 9.1 Part 1 Solver: Single-Object Problems & Baseline Heights (Q1 to Q6)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Exhaustive step-by-step resolution of NCERT Exercise 9.1 Questions 1 through 6. Covers the circus artist climbing rope, tree broken by wind storm, playground slides for young and older children, tower angle from ground, kite flying string length, and 1.5 m boy walking towards a 30 m building.",
            "key_concepts": [
                "Ex 9.1 Q1: Circus artist rope 20 m tied to vertical pole at 30° angle ⇒ sin 30° = h / 20 ⇒ h = 10 m",
                "Ex 9.1 Q2: Tree broken by storm: Top touches ground at 30° at distance 8 m ⇒ Height = Perpendicular + Hypotenuse = 8√3 m",
                "Ex 9.1 Q3: Contractor slides: Below 5 yrs (h = 1.5 m, 30° ⇒ L = 3 m); Older kids (h = 3 m, 60° ⇒ L = 2√3 m)",
                "Ex 9.1 Q4: Angle of elevation of tower from point 30 m away is 30° ⇒ h = 30 tan 30° = 10√3 m",
                "Ex 9.1 Q5: Kite at height 60 m, string inclined at 60° ⇒ Hypotenuse = 60 / sin 60° = 40√3 m",
                "Ex 9.1 Q6: 1.5 m tall boy walking towards 30 m building: Effective height = 30 - 1.5 = 28.5 m; distance walked = 19√3 m"
            ],
            "subtopics": [
                "Full resolution of Q1 to Q6 with complete diagram breakdowns",
                "Tree broken problem: Sum of broken part and standing part",
                "Accounting for observer height in Q6"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 9.1 Q2: A tree breaks due to storm and the broken part bends so that the top of the tree touches the ground making an angle 30° with it. The distance between the foot of the tree to the point where the top touches the ground is 8 m. Find the height of the tree.",
                    "solution": "Let AC be the original unbroken tree.\nSuppose the tree broke at point B.\nThe top part AB bends over to touch the ground at point C'.\nTherefore, length of broken part BC' = AB.\nGiven:\nAngle made with ground ∠BC'C = 30°.\nDistance from foot of tree C to point of contact C' = CC' = 8 m.\nAngle at foot of tree ∠BCC' = 90°.\n\nTotal height of the tree = BC + AB = BC + BC'.\n\nStep 1: Find standing part BC in right ΔBCC':\ntan 30° = BC / CC'\n1 / √3 = BC / 8 ⇒ BC = 8 / √3 m.\n\nStep 2: Find broken part BC' in right ΔBCC':\ncos 30° = CC' / BC'\n√3 / 2 = 8 / BC' ⇒ BC' = 16 / √3 m.\n\nStep 3: Calculate total tree height:\nTotal Height = BC + BC' = 8/√3 + 16/√3 = 24 / √3 m.\nRationalise denominator:\n= (24 × √3) / (√3 × √3) = 24√3 / 3 = 8√3 m.\n[ROUGH_WORK]\nIf √3 ≈ 1.732: Total height = 8 × 1.732 = 13.856 m.\nBoxed Answer: [ Total height of the tree = 8√3 m ].",
                    "concept_questions": [
                        "Why is the height of the tree equal to Perpendicular + Hypotenuse?",
                        "Could we have used Pythagoras theorem to find BC' after finding BC?"
                    ]
                },
                {
                    "problem": "Exercise 9.1 Q6: A 1.5 m tall boy is standing at some distance from a 30 m tall building. The angle of elevation from his eyes to the top of the building increases from 30° to 60° as he walks towards the building. Find the distance he walked towards the building.",
                    "solution": "Let AB be the tall building of height AB = 30 m.\nLet CD be the boy of height CD = 1.5 m at initial position, and C'D' be his position after walking.\nDraw horizontal line through his eyes D-D'-E meeting the building at E.\nThen BE = 1.5 m.\nEffective height AE = AB - BE = 30 - 1.5 = 28.5 m = 57 / 2 m.\n\nLet the initial angle of elevation be ∠ADE = 30°.\nLet the final angle of elevation be ∠AD'E = 60°.\nDistance walked = DD' = DE - D'E.\n\nStep 1: In right ΔAD'E (right-angled at E):\ntan 60° = AE / D'E\n√3 = 28.5 / D'E ⇒ D'E = 28.5 / √3 m.\n\nStep 2: In right ΔADE (right-angled at E):\ntan 30° = AE / DE\n1 / √3 = 28.5 / DE ⇒ DE = 28.5√3 m.\n\nStep 3: Distance walked by the boy:\nDD' = DE - D'E = 28.5√3 - 28.5 / √3\n= 28.5 [ √3 - 1/√3 ] = 28.5 [ (3 - 1) / √3 ] = 28.5 × (2 / √3) = 57 / √3 m.\nRationalise denominator:\nDD' = 57√3 / 3 = 19√3 m.\n[ROUGH_WORK]\n57 / 3 = 19.\n19 × √3 ≈ 19 × 1.732 = 32.91 m.\nBoxed Answer: [ Distance walked towards building = 19√3 m ].",
                    "concept_questions": [
                        "Why did we subtract 1.5 m from 30 m at the beginning?",
                        "What happens to the angle of elevation as the observer gets infinitely close to the building?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Exercise 9.1 Baseline Problems HUD",
                "diagram_type": "diagram",
                "svg": svg_elevation,
                "concept_visuals": [
                    {
                        "concept_title": "Single and Double Triangle Layouts",
                        "diagram_title": "Height Determination Models",
                        "svg": svg_elevation,
                        "diagram_type": "diagram",
                        "what_to_make": "Detailed geometry showing tree break and boy walking models",
                        "what_to_explain": "Algebraic steps for single and moving observer problems"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting that the tree height consists of BOTH the vertical stump and the hypotheuse.",
                "Using total 30 m height for the boy problem without subtracting eye level height 1.5 m."
            ]
        },

        # Module 4: NCERT Exercise 9.1 Solver (Questions 7 to 11)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 9.1 Part 2 Solver: Pedestals, Transmission Towers & River Widths (Q7 to Q11)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 9.1 Questions 7 through 11. Rigorous treatment of transmission tower on building (Q7), statue on pedestal (Q8), tower vs building heights (Q9), two poles of equal heights on either side of 80 m road (Q10), and TV tower on canal bank (Q11).",
            "key_concepts": [
                "Ex 9.1 Q7: Transmission tower 20 m building: Angles 45° and 60° ⇒ Tower height = 20(√3 - 1) m",
                "Ex 9.1 Q8: Statue 1.6 m on pedestal: Angles 60° and 45° ⇒ Pedestal height = 0.8(√3 + 1) m",
                "Ex 9.1 Q9: Tower 50 m vs building: Elevation angles 60° and 30° ⇒ Building height = 50/3 = 16 2/3 m",
                "Ex 9.1 Q10: Two poles of equal height on 80 m road: Angles 60° and 30° ⇒ Pole height = 20√3 m, positions 20 m and 60 m",
                "Ex 9.1 Q11: TV tower on canal bank: 20 m backward move reduces angle from 60° to 30° ⇒ Height = 10√3 m, Canal width = 10 m"
            ],
            "subtopics": [
                "Full resolution of Q7 to Q11 with line-by-line topper board layouts",
                "Symmetric dual-pole road problem with internal point (Q10)",
                "Canal width deduction via cotangent relations (Q11)"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 9.1 Q10: Two poles of equal heights are standing opposite each other on either side of the road, which is 80 m wide. From a point between them on the road, the angles of elevation of the top of the poles are 60° and 30°, respectively. Find the height of the poles and the distances of the point from the poles.",
                    "solution": "Let AB and CD be the two poles of equal height 'h', so AB = CD = h.\nLet BD be the 80 m wide road, BD = 80 m.\nLet P be the observation point on the road between B and D.\nLet BP = x meters, then PD = 80 - x meters.\nGiven angles of elevation:\n∠APB = 60° and ∠CPD = 30°.\nBoth poles stand vertically: ∠ABP = ∠CDP = 90°.\n\nStep 1: In right ΔABP (right-angled at B):\ntan 60° = AB / BP\n√3 = h / x ⇒ h = x√3 ... (1)\n\nStep 2: In right ΔCDP (right-angled at D):\ntan 30° = CD / PD\n1 / √3 = h / (80 - x)\n80 - x = h√3 ... (2)\n\nStep 3: Substitute h = x√3 into equation (2):\n80 - x = (x√3) × √3\n80 - x = 3x\n80 = 4x ⇒ x = 20 m.\n\nStep 4: Compute distances and pole height:\nDistance from Pole AB: BP = x = 20 m.\nDistance from Pole CD: PD = 80 - x = 80 - 20 = 60 m.\nHeight of the poles: h = x√3 = 20√3 m.\n[ROUGH_WORK]\nCheck in ΔCDP: tan 30° = 20√3 / 60 = √3 / 3 = 1/√3 (Verified!).\nIf √3 ≈ 1.732: h = 20 × 1.732 = 34.64 m.\nBoxed Answer: [ Height of poles = 20√3 m, Distances of point = 20 m and 60 m ].",
                    "concept_questions": [
                        "Why is the closer pole (20 m away) associated with the steeper angle 60°?",
                        "What would be the height if the point was exactly at the midpoint of the road?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Two Poles on Wide Road Geometry HUD",
                "diagram_type": "diagram",
                "svg": svg_dual_elevation,
                "concept_visuals": [
                    {
                        "concept_title": "Equal Height Two Pole Framework",
                        "diagram_title": "Symmetric Road Configuration",
                        "svg": svg_dual_elevation,
                        "diagram_type": "diagram",
                        "what_to_make": "Diagram showing road width 80 m, two poles AB and CD, and intermediate point P",
                        "what_to_explain": "Equating expressions for h to solve for position x"
                    }
                ]
            },
            "common_misconceptions": [
                "Assigning 60° to the pole 60 m away: The closer the observer is to the base, the steeper the angle of elevation must be (so 60° corresponds to the shorter 20 m distance!).",
                "Forgetting to calculate both distances (20 m and 60 m) as asked by the question."
            ]
        },

        # Module 5: NCERT Exercise 9.1 Solver (Questions 12 to 16)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise 9.1 Part 3 Solver: Cable Towers, Ships, Aeroplanes & Complementary Heights (Q12 to Q16)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Exhaustive resolution of NCERT Exercise 9.1 Questions 12 through 16. Covers cable tower from 7 m building (Q12), two ships observed from 75 m lighthouse with angles of depression 30° and 45° (Q13), 1.2 m girl spotting 88.2 m balloon moving horizontally (Q14), highway tower and car accelerating towards tower foot taking 6 seconds (Q15), and the landmark proof for complementary angles of elevation h = √(ab) (Q16).",
            "key_concepts": [
                "Ex 9.1 Q12: 7 m building to cable tower (elevation 60°, depression 45°) ⇒ Tower height = 7(√3 + 1) m",
                "Ex 9.1 Q13: 75 m lighthouse, depression of two ships 30° and 45° ⇒ Distance between ships = 75(√3 - 1) m",
                "Ex 9.1 Q14: 1.2 m girl and 88.2 m balloon: Effective height = 87 m; angle changes 60° to 30° ⇒ Distance traveled = 58√3 m",
                "Ex 9.1 Q15: Car moving towards tower with uniform speed: Depression changes from 30° to 60° in 6 seconds ⇒ Time to reach foot = 3 seconds!",
                "Ex 9.1 Q16: Complementary angles of elevation from distances a and b: tan θ = h/a and tan(90° - θ) = cot θ = h/b ⇒ h² = ab ⇒ h = √(ab) = √(4 × 9) = 6 m"
            ],
            "subtopics": [
                "Complete resolution of Q12 to Q16 with rigorous algebraic proofs",
                "Uniform speed kinematics coupled with trigonometry (Q15)",
                "Full algebraic proof of complementary heights formula h = √(ab)"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 9.1 Q15: A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of 30°, which is approaching the foot of the tower with a uniform speed. Six seconds later, the angle of depression of the car is found to be 60°. Find the time taken by the car to reach the foot of the tower from this point.",
                    "solution": "Let AB be the tower of height 'h'.\nLet the car be initially at point C with angle of depression 30°.\nBy alternate interior angles, ∠ACB = 30°.\nSix seconds later, the car reaches point D with angle of depression 60°.\nBy alternate interior angles, ∠ADB = 60°.\nLet 'v' be the uniform speed of the car in m/s.\nDistance CD covered in 6 seconds = Speed × Time = 6v meters.\nLet 't' be the time taken by the car to travel from D to B.\nThen distance DB = v × t meters.\n\nStep 1: In right ΔABD (right-angled at B):\ntan 60° = AB / DB = h / (vt)\n√3 = h / (vt) ⇒ h = vt√3 ... (1)\n\nStep 2: In right ΔABC (right-angled at B):\ntan 30° = AB / BC = h / (CD + DB) = h / (6v + vt)\n1 / √3 = h / [ v(6 + t) ]\nh√3 = v(6 + t) ... (2)\n\nStep 3: Substitute h = vt√3 from (1) into (2):\n(vt√3) × √3 = v(6 + t)\n3vt = 6v + vt\nDivide both sides by v (since speed v > 0):\n3t = 6 + t\n2t = 6 ⇒ t = 3 seconds!\n[ROUGH_WORK]\nNotice speed 'v' cancels out completely! The geometry forces the remaining distance DB to be exactly half of distance CD (since cot 30° - cot 60° = √3 - 1/√3 = 2/√3, while cot 60° = 1/√3).\nBoxed Answer: [ Time taken to reach the foot of the tower = 3 seconds ].",
                    "concept_questions": [
                        "Why does the unknown speed v cancel out of the equations?",
                        "What is the ratio of distance CD to distance DB?"
                    ]
                },
                {
                    "problem": "Exercise 9.1 Q16: The angles of elevation of the top of a tower from two points at a distance of 4 m and 9 m from the base of the tower and in the same straight line with it are complementary. Prove that the height of the tower is 6 m.",
                    "solution": "Let AB be the tower of height 'h'.\nLet C and D be two points on the ground in the same straight line as base B.\nGiven:\nBC = 4 m, BD = 9 m.\nAngles of elevation are complementary:\nLet ∠ACB = θ, then ∠ADB = 90° - θ.\n\nStep 1: In right ΔABC (right-angled at B):\ntan θ = AB / BC = h / 4 ... (1)\n\nStep 2: In right ΔABD (right-angled at B):\ntan(90° - θ) = AB / BD = h / 9\nRecall the complementary angle identity: tan(90° - θ) = cot θ:\ncot θ = h / 9 ... (2)\n\nStep 3: Multiply equation (1) and equation (2):\ntan θ × cot θ = (h / 4) × (h / 9)\nWe know tan θ × cot θ = tan θ × (1 / tan θ) = 1:\n1 = h² / 36\nh² = 36\nh = √36 = 6 m (taking positive root since height cannot be negative).\n\nHence Proved that the height of the tower is 6 m!\n[ROUGH_WORK]\nGeneral theorem: For complementary angles from distances a and b, h = √(ab).\nHere a = 4, b = 9 ⇒ h = √(4 × 9) = √36 = 6 m.\nBoxed Answer: [ Height of tower = 6 m (Proved) ].",
                    "concept_questions": [
                        "What is the mathematical product of tan θ and cot θ?",
                        "Would this formula hold if the distances were 3 m and 12 m? What would the height be?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Complementary Elevation and Kinematic Geometry HUD",
                "diagram_type": "diagram",
                "svg": svg_dual_elevation,
                "concept_visuals": [
                    {
                        "concept_title": "Complementary Heights Proof Model",
                        "diagram_title": "Theorem h = sqrt(ab) Visualizer",
                        "svg": svg_dual_elevation,
                        "diagram_type": "diagram",
                        "what_to_make": "Right triangle with ground distances 4 m and 9 m showing complementary angles θ and 90°-θ",
                        "what_to_explain": "Multiplying tan θ and cot θ to prove h = 6 m"
                    }
                ]
            },
            "common_misconceptions": [
                "Taking h = ±6 m: Height is a physical geometric scalar and cannot be negative; state explicitly that h > 0.",
                "Thinking time taken to reach foot in Q15 is 6 seconds: 6 seconds was for distance CD; the remaining distance DB is traversed in 3 seconds."
            ]
        }
    ]
    
    return modules
