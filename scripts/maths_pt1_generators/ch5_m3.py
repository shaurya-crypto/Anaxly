"""
Chapter 5: I’m Up and Down, and Round and Round - Module 3
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_circle_geometry_svg

def get_m3():
    m3_svg = build_circle_geometry_svg(
        radius=90, center=(290, 200),
        points=[
            {"x": 290, "y": 200, "label": "Centre O"},
            {"x": 290, "y": 146, "label": "M1 (d=3)"},
            {"x": 290, "y": 272, "label": "M2 (d=4)"}
        ],
        chords=[
            {"p1": (220, 146), "p2": (360, 146), "label": "Chord 1 = 8 cm", "color": "#2563EB"},
            {"p1": (236, 272), "p2": (344, 272), "label": "Chord 2 = 6 cm", "color": "#DC2626"}
        ],
        title="Opposite Parallel Chords Distance: 3 + 4 = 7 cm",
        caption="Circle of radius 5 cm with parallel chords of lengths 8 cm and 6 cm on opposite sides of centre"
    )

    return {
        "order_index": 3,
        "title": "Textbook Exercise Solver 2: Midpoints, Perpendicular Bisectors & Equidistant Chords (Exercises 5.3 & 5.4 Complete)",
        "description": "Comprehensive step-by-step solutions to in-text Theorems 4, 5, 6, 7 and Exercises 5.3 and 5.4. Master the perpendicular bisector chord theorem, altitude of inscribed isosceles triangles, parallel chords on opposite sides of centre (lengths 6 cm and 8 cm with r = 5 cm, distance = 7 cm), and the Baudhayana-Pythagoras proof of chord equidistance.",
        "subtopics": [
            "Theorem 4: The line joining circle centre to the midpoint of a chord is perpendicular to the chord",
            "Theorem 5 (Converse): The perpendicular from centre to a chord bisects the chord",
            "Altitude of inscribed isosceles triangle ABC with AB = AC passes through the centre",
            "Calculating distance between parallel chords on opposite sides of the centre (r = 5 cm)",
            "Theorem 6 & 7: Equidistant chords theorem and its Baudhayana-Pythagoras algebraic derivation"
        ],
        "key_concepts": [
            "Chord Bisector Perpendicularity: In triangle OMA and triangle OMB, OA = OB = r and AM = MB. By SSS, triangle OMA ~= OMB, so angle OMA = angle OMB = 90°.",
            "RHS Congruence Converse: If OM perp AB, then in right triangles OMA and OMB, OA = OB = r (hypotenuses) and OM is common. By RHS, AM = MB.",
            "Parallel Chord Separation: For parallel chords on opposite sides of centre, total distance between midpoints is d1 + d2.",
            "Pythagorean Half-Chord Relation: (L/2)^2 + d^2 = r^2. If r = 5 cm, L1 = 8 => d1 = sqrt(25 - 16) = 3 cm; L2 = 6 => d2 = sqrt(25 - 9) = 4 cm. Separation = 3 + 4 = 7 cm.",
            "Equidistant Chords Equality: If d1 = d2, then L1/2 = sqrt(r^2 - d1^2) = sqrt(r^2 - d2^2) = L2/2 => L1 = L2."
        ],
        "success_criteria": "Students can apply RHS and SSS congruence to prove circle theorems, compute perpendicular distances between parallel chords, and apply the Baudhayana-Pythagoras theorem to chord problems.",
        "chapter_notes": "Module 3 resolves all problems in Exercises 5.3 and 5.4, providing complete geometric proofs alongside arithmetic computations.",
        "common_misconceptions": [
            {"misconception": "Adding chord lengths directly to find distance", "clarification": "Distance from centre must be computed via Pythagoras theorem for each half-chord separately."},
            {"misconception": "Subtracting distances when chords are on opposite sides", "clarification": "When parallel chords lie on OPPOSITE sides of the centre, their distances ADD (d1 + d2); they subtract only when on the SAME side."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through chord distance proofs and the classic parallel chords problem. Always draw right triangle OMA with hypotenuse r, leg d, and leg L/2.",
        "visual_lesson_plan": {
            "title": "Visualizing Chord Bisectors and Parallel Chords",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Vector circle showing two parallel chords on opposite sides of the centre with perpendicular distance segments d1 = 3 and d2 = 4.",
            "concept_visuals": [
                {
                    "concept_title": "Parallel Chords on Opposite Sides: Separation 7 cm",
                    "diagram_title": "Chords of 8 cm and 6 cm in Circle r = 5 cm",
                    "interactive_math_formula": "D = d_1 + d_2 = \\sqrt{5^2 - 4^2} + \\sqrt{5^2 - 3^2} = 3 + 4 = 7\\text{ cm}",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circle r=5"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 0, "intercept": 3, "color": "#2563EB", "label": "Chord 1 (L=8, y=3)"},
                            {"slope": 0, "intercept": -4, "color": "#DC2626", "label": "Chord 2 (L=6, y=-4)"},
                            {"slope": 999, "intercept": 0, "color": "#64748B", "label": "Perpendicular Bisector Axis"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 0, "y": 3, "label": "M1(0, 3)"},
                            {"x": 0, "y": -4, "label": "M2(0, -4)"}
                        ]
                    },
                    "image_query": "two parallel chords opposite sides of centre radius 5 distance 7 cm",
                    "video_query": "two parallel chords of length 6 and 8 cm opposite sides radius 5",
                    "what_to_explain": "Chord of 8 cm has half-length 4 cm and distance 3 cm. Chord of 6 cm has half-length 3 cm and distance 4 cm. Total separation is 3 + 4 = 7 cm."
                },
                {
                    "concept_title": "Perpendicular Bisector Chord Invariant",
                    "diagram_title": "Right Triangles OMA and OMB: RHS Congruence",
                    "interactive_math_formula": "OM \\perp AB \\iff AM = MB",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circle r=5"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 0, "intercept": 3, "color": "#2563EB", "label": "Chord AB"},
                            {"slope": 999, "intercept": 0, "color": "#16A34A", "label": "Perpendicular OM"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Centre O"},
                            {"x": 0, "y": 3, "label": "M(0, 3) [90°]"},
                            {"x": -4, "y": 3, "label": "A(-4, 3)"},
                            {"x": 4, "y": 3, "label": "B(4, 3)"}
                        ]
                    },
                    "image_query": "perpendicular from centre to chord bisects chord geometry diagram",
                    "video_query": "the perpendicular from the centre of a circle to a chord bisects the chord",
                    "what_to_explain": "Hypotenuses OA and OB are radii (5 cm). Since OM is common, right triangles OMA and OMB are congruent by RHS, proving AM = MB = 4 cm."
                },
                {
                    "concept_title": "Equidistant Chords Theorem (Baudhayana-Pythagoras)",
                    "diagram_title": "Equal Distances d1 = d2 implies Equal Chords L1 = L2",
                    "interactive_math_formula": "d_1 = d_2 \\implies L_1 = 2\\sqrt{r^2 - d_1^2} = 2\\sqrt{r^2 - d_2^2} = L_2",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circle r=5"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 0, "intercept": 3, "color": "#2563EB", "label": "Chord 1 (d=3)"},
                            {"slope": 999, "intercept": 3, "color": "#2563EB", "label": "Chord 2 (d=3)"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O"},
                            {"x": 0, "y": 3, "label": "d=3"},
                            {"x": 3, "y": 0, "label": "d=3"}
                        ]
                    },
                    "image_query": "chords equidistant from the centre are equal in length proof",
                    "video_query": "chords equidistant from centre of circle are equal proof",
                    "what_to_explain": "Equal perpendicular distances guarantee equal half-chords by Pythagoras theorem, yielding identical full chord lengths."
                },
                {
                    "concept_title": "Inscribed Isosceles Triangle Altitude Property",
                    "diagram_title": "Altitude from A to BC Passes Through Centre O",
                    "interactive_math_formula": "AB = AC \\implies \\text{Altitude } AD = \\text{Perpendicular Bisector of } BC",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circle"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 999, "intercept": 0, "color": "#DC2626", "label": "Axis / Altitude"}
                        ],
                        "points": [
                            {"x": 0, "y": 5, "label": "A(0, 5)"},
                            {"x": 0, "y": 0, "label": "Centre O(0, 0)"},
                            {"x": -4, "y": -3, "label": "B(-4, -3)"},
                            {"x": 4, "y": -3, "label": "C(4, -3)"},
                            {"x": 0, "y": -3, "label": "D(0, -3)"}
                        ]
                    },
                    "image_query": "isosceles triangle inscribed in circle altitude passes through centre",
                    "video_query": "altitude of inscribed isosceles triangle passes through centre of circle",
                    "what_to_explain": "Because AB = AC, the altitude from A is the perpendicular bisector of chord BC, which unconditionally passes through circumcentre O."
                },
                {
                    "concept_title": "Paper Circle Crease: Geometric Chord Symmetry",
                    "diagram_title": "Fold Axis Bisects Crease at 90°",
                    "interactive_math_formula": "\\text{Crease}_2 \\perp \\text{Crease}_1",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-5, 5],
                        "curves": [
                            {"fn": "sqrt(16 - x^2)", "color": "#94A3B8", "label": "Paper Boundary"},
                            {"fn": "-sqrt(16 - x^2)", "color": "#94A3B8", "label": ""}
                        ],
                        "lines": [
                            {"slope": 0, "intercept": 2, "color": "#2563EB", "label": "Fold 1: Chord"},
                            {"slope": 999, "intercept": 0, "color": "#DC2626", "label": "Fold 2: Diameter Bisector"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Centre (on Fold 2)"},
                            {"x": 0, "y": 2, "label": "Midpoint M"}
                        ]
                    },
                    "image_query": "paper circle folding chord and perpendicular bisector activity",
                    "video_query": "paper folding circle geometry chord midpoint",
                    "what_to_explain": "Folding a circle so chord endpoints meet produces a crease along the diameter, bisecting the chord at 90°."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Perpendicular Bisector Theorems",
                    "questions": [
                        {
                            "question": "What congruence criterion proves that the perpendicular from the centre to a chord bisects the chord?",
                            "type": "short_answer",
                            "ideal_answer": "RHS (Right angle - Hypotenuse - Side) congruence criterion.",
                            "socratic_hint": "Both triangles share a 90° angle, equal radii as hypotenuses, and the perpendicular segment as a common leg."
                        },
                        {
                            "question": "Two parallel chords of lengths 6 cm and 8 cm lie on opposite sides of the centre of a circle of radius 5 cm. What is the distance between them?",
                            "type": "short_answer",
                            "ideal_answer": "7 cm (3 cm + 4 cm = 7 cm).",
                            "socratic_hint": "Calculate the perpendicular distance from the centre to each chord separately using Pythagoras theorem, then add."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 5.3 Q1: Explain why the converse to Theorem 4 is true: why does the perpendicular from the centre of a circle to a chord bisect the chord?",
                "given": "A circle with centre C and chord AB. Perpendicular CM is drawn to AB such that angle CMA = angle CMB = 90°.",
                "formula": "RHS Congruence Criterion: In right-angled triangles, if the hypotenuse and one leg are equal, the triangles are congruent.",
                "substitution": "In right triangles CMA and CMB: angle CMA = angle CMB = 90°; hypotenuse CA = hypotenuse CB = r; leg CM is common.",
                "calculation": "1. In triangle CMA and triangle CMB:\n   - angle CMA = angle CMB = 90° (given CM perp AB)\n   - CA = CB = r (radii of the same circle, acting as hypotenuses)\n   - CM = CM (common leg)\n2. Therefore, triangle CMA is congruent to triangle CMB by the RHS criterion (triangle CMA ~= triangle CMB).\n3. By Corresponding Parts of Congruent Triangles (CPCTC):\n   AM = BM.\n4. Since AM = BM, point M is the midpoint of segment AB.\n5. Hence, the perpendicular CM from centre C bisects the chord AB.",
                "finalAnswer": "Proved: By RHS congruence of triangles CMA and CMB, AM = BM (CPCTC), so the perpendicular bisects the chord.",
                "unit": "congruence proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.3 Q2: An isosceles triangle ABC is inscribed in a circle, with AB = AC. Show that the altitude from A to BC passes through the centre of the circle.",
                "given": "Isosceles triangle ABC inscribed in circle with centre O, where AB = AC. AD is the altitude from A to BC (AD perp BC).",
                "formula": "In an isosceles triangle, the altitude to the base is the perpendicular bisector of the base. The perpendicular bisector of any chord passes through the centre.",
                "substitution": "BC is a chord of the circumcircle. AD perp BC.",
                "calculation": "1. In triangle ABC, AB = AC. In right triangles ADB and ADC:\n   - angle ADB = angle ADC = 90° (AD is altitude)\n   - AB = AC (given)\n   - AD = AD (common side)\n   Therefore, triangle ADB ~= triangle ADC by RHS criterion.\n2. By CPCTC, BD = CD. Thus, D is the midpoint of side (chord) BC.\n3. Since AD perp BC and D is the midpoint of BC, line AD is the perpendicular bisector of chord BC.\n4. By Theorem 4/5, the perpendicular bisector of any chord of a circle passes through the centre O of the circle.\n5. Therefore, the altitude AD unconditionally passes through the centre O.",
                "finalAnswer": "Proved: The altitude AD bisects chord BC at 90°, making it the perpendicular bisector of BC, which passes through centre O.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.3 Q3: Two parallel chords of lengths 6 cm and 8 cm are on opposite sides of the centre of a circle of radius 5 cm. Find the distance between the midpoints of the chords.",
                "given": "Radius r = 5 cm. Chord 1 (AB) = 8 cm. Chord 2 (CD) = 6 cm. Chords are parallel and on opposite sides of centre O.",
                "formula": "For any chord of length L, perpendicular distance from centre is d = sqrt(r^2 - (L/2)^2). Total distance D = d1 + d2.",
                "substitution": "Half-chord 1 = 8/2 = 4 cm. Half-chord 2 = 6/2 = 3 cm. r = 5 cm.",
                "calculation": "1. Let M1 be the midpoint of chord AB (8 cm). Half-length AM1 = 4 cm.\n   In right triangle OM1A:\n   OM1^2 = OA^2 - AM1^2 = 5^2 - 4^2 = 25 - 16 = 9.\n   OM1 = sqrt(9) = 3 cm.\n2. Let M2 be the midpoint of chord CD (6 cm). Half-length CM2 = 3 cm.\n   In right triangle OM2C:\n   OM2^2 = OC^2 - CM2^2 = 5^2 - 3^2 = 25 - 9 = 16.\n   OM2 = sqrt(16) = 4 cm.\n3. Since the chords are parallel and on OPPOSITE sides of centre O, points M1, O, M2 are collinear.\n4. Total distance M1M2 = OM1 + OM2 = 3 cm + 4 cm = 7 cm.",
                "finalAnswer": "7 cm",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.4 Q1: Use the Baudhayana-Pythagoras theorem to show why Theorem 6 (Chords that are equal in length are equidistant from the centre) must be true.",
                "given": "Two chords AB and CD of equal length (AB = CD = 2s) in a circle of radius r. Let distances from centre O be d1 and d2.",
                "formula": "Baudhayana-Pythagoras theorem: Hypotenuse^2 = Base^2 + Altitude^2 => r^2 = s^2 + d^2 => d^2 = r^2 - s^2.",
                "substitution": "s = AB / 2 = CD / 2.",
                "calculation": "1. Drop perpendiculars OM1 perp AB and OM2 perp CD. Then AM1 = AB/2 = s and CM2 = CD/2 = s.\n2. In right triangle OM1A: OA^2 = OM1^2 + AM1^2 => r^2 = d1^2 + s^2 => d1^2 = r^2 - s^2.\n3. In right triangle OM2C: OC^2 = OM2^2 + CM2^2 => r^2 = d2^2 + s^2 => d2^2 = r^2 - s^2.\n4. Since the RHS for both equations is identical (r^2 - s^2), we have d1^2 = d2^2.\n5. Since distances are positive real quantities, d1 = d2.\n6. Therefore, chords of equal length are equidistant from the centre.",
                "finalAnswer": "Proved algebraically: d1 = sqrt(r^2 - s^2) and d2 = sqrt(r^2 - s^2); since s = AB/2 = CD/2, d1 = d2.",
                "unit": "algebraic proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.4 Q2: In Fig. 5.15, if CE perp AB, CH perp GF, and CE = CH, show that AB = GF.",
                "given": "Circle with centre C. CE perp AB, CH perp GF. CE = CH (chords AB and GF are equidistant from centre C).",
                "formula": "RHS congruence in right triangles CEA and CHG.",
                "substitution": "Hypotenuses CA = CG = r; legs CE = CH.",
                "calculation": "1. In right triangle CEA and right triangle CHG:\n   - angle CEA = angle CHG = 90°\n   - CA = CG = r (radii of the circle, hypotenuses)\n   - CE = CH (given equal perpendicular distances)\n2. By RHS congruence criterion, triangle CEA ~= triangle CHG.\n3. By CPCTC, AE = GH.\n4. By Theorem 5, the perpendicular from the centre bisects the chord: AB = 2*AE and GF = 2*GH.\n5. Since AE = GH, multiplying both sides by 2 gives 2*AE = 2*GH => AB = GF.",
                "finalAnswer": "AB = GF (Proved by RHS congruence and the perpendicular bisector theorem).",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.4 Q3: Solve the previous question (show AB = GF given CE = CH) using the Baudhayana-Pythagoras theorem directly.",
                "given": "Circle of radius r with centre C. CE = CH = d, CE perp AB, CH perp GF.",
                "formula": "Baudhayana-Pythagoras theorem: In right triangle CEA, AE = sqrt(CA^2 - CE^2) = sqrt(r^2 - d^2).",
                "substitution": "AE = sqrt(r^2 - d^2) and GH = sqrt(CG^2 - CH^2) = sqrt(r^2 - d^2).",
                "calculation": "1. In right triangle CEA: CA = r, CE = d. Therefore, AE^2 = r^2 - d^2 => AE = sqrt(r^2 - d^2).\n2. Chord AB = 2 * AE = 2*sqrt(r^2 - d^2).\n3. In right triangle CHG: CG = r, CH = d. Therefore, GH^2 = r^2 - d^2 => GH = sqrt(r^2 - d^2).\n4. Chord GF = 2 * GH = 2*sqrt(r^2 - d^2).\n5. Comparing the two expressions: AB = 2*sqrt(r^2 - d^2) = GF.\n6. Hence, AB = GF.",
                "finalAnswer": "AB = GF = 2*sqrt(r^2 - d^2) (Proved directly using Baudhayana-Pythagoras theorem).",
                "unit": "algebraic derivation",
                "has_diagram": False
            }
        ]
    }
