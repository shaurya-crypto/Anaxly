"""
Chapter 5: I’m Up and Down, and Round and Round - Module 4
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_circle_geometry_svg

def get_m4():
    m4_svg = build_circle_geometry_svg(
        radius=90, center=(290, 200),
        points=[
            {"x": 290, "y": 200, "label": "Centre O"},
            {"x": 290, "y": 165, "label": "M1 (d=5)"},
            {"x": 290, "y": 116, "label": "M2 (d=12)"}
        ],
        chords=[
            {"p1": (207, 165), "p2": (373, 165), "label": "Chord 1 = 24 cm (y=5)", "color": "#2563EB"},
            {"p1": (255, 116), "p2": (325, 116), "label": "Chord 2 = 10 cm (y=12)", "color": "#DC2626"}
        ],
        title="Parallel Chords on the Same Side: Radius = 13 cm",
        caption="Chords of 24 cm and 10 cm on same side separated by 7 cm: d2 - d1 = 12 - 5 = 7 cm"
    )

    return {
        "order_index": 4,
        "title": "Textbook Exercise Solver 3: Distance Formula for Chords & Parallel Chord Configurations (Exercise 5.5 & End-of-Chapter Set 1)",
        "description": "Comprehensive step-by-step solutions to Exercise 5.5 (Q1, Q2) and End-of-Chapter Questions 1, 3, 4, 9, 13, 18, 22, and 23. Master the algebraic chord length formula L = 2*sqrt(r^2 - d^2), parallel chords on the SAME side of centre (lengths 10 cm and 24 cm with separation 7 cm -> r = 13 cm), proving diameter is the maximum chord, and showing shortest chord through internal point A is perpendicular to OA.",
        "subtopics": [
            "Derivation of the universal chord length formula: L = 2*sqrt(r^2 - d^2)",
            "Inverse monotonic variation: Longer chords lie closer to the centre",
            "Radius determination from parallel chords on the same side (separation 7 cm, chords 10 and 24 cm)",
            "Strict inequality proof: Diameter is the maximum possible chord (L <= 2r)",
            "Extremal optimization: The shortest chord through an interior point A is perpendicular to OA"
        ],
        "key_concepts": [
            "Universal Chord Formula: Half-chord s = sqrt(r^2 - d^2), so full chord length L = 2*sqrt(r^2 - d^2).",
            "Pythagorean Triplet Invariance: Standard 5-12-13, 6-8-10, and 9-12-15 right triangles govern classical textbook chord configurations.",
            "Same-Side Parallel Separation: When parallel chords lie on the same side of the centre, the distance between them is delta d = d2 - d1 = sqrt(r^2 - s2^2) - sqrt(r^2 - s1^2).",
            "Diameter Maximality: Since d^2 >= 0, L = 2*sqrt(r^2 - d^2) <= 2*sqrt(r^2) = 2r. Maximum occurs uniquely at d = 0.",
            "Shortest Chord Invariant: For any chord through point A, its distance d from centre satisfies d <= OA. Therefore, length L = 2*sqrt(r^2 - d^2) is minimized when d is maximized, which occurs when d = OA (meaning chord is perpendicular to OA)."
        ],
        "success_criteria": "Students can apply the chord distance formula to calculate radii, chord lengths, and distances, solve complex two-chord parallel systems on the same side, and construct extremal geometric proofs.",
        "chapter_notes": "Module 4 focuses on metric circular calculations and algebraic geometry proofs for chord lengths and extremal chord configurations.",
        "common_misconceptions": [
            {"misconception": "Assuming parallel chords on the same side have distances that add", "clarification": "On the same side, distances subtract (d2 - d1 = 7 cm); they add only when on opposite sides."},
            {"misconception": "Believing a chord through interior point A can be made arbitrarily small", "clarification": "The minimum possible chord length through point A is strictly bounded by 2*sqrt(r^2 - OA^2)."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through chord length formulas. Carefully explain the difference between same-side parallel chords (distances subtract) and opposite-side parallel chords (distances add).",
        "visual_lesson_plan": {
            "title": "Visualizing Metric Chord Relationships",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Interactive circle with two parallel chords on the same side of the centre at distances 5 cm and 12 cm, showing the 7 cm separation.",
            "concept_visuals": [
                {
                    "concept_title": "Parallel Chords on Same Side: Radius 13 cm",
                    "diagram_title": "Chords of 24 cm (d=5) and 10 cm (d=12)",
                    "interactive_math_formula": "d_2 - d_1 = 12 - 5 = 7\\text{ cm} \\implies r = 13\\text{ cm}",
                    "mafs_graph_config": {
                        "domain": [-15, 15],
                        "range": [-15, 15],
                        "curves": [
                            {"fn": "sqrt(169 - x^2)", "color": "#2563EB", "label": "Circle r=13"},
                            {"fn": "-sqrt(169 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 0, "intercept": 5, "color": "#2563EB", "label": "Chord 1 = 24 cm"},
                            {"slope": 0, "intercept": 12, "color": "#DC2626", "label": "Chord 2 = 10 cm"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 0, "y": 5, "label": "M1(0, 5)"},
                            {"x": 0, "y": 12, "label": "M2(0, 12)"}
                        ]
                    },
                    "image_query": "two parallel chords same side of centre distance 7 cm radius 13",
                    "video_query": "two parallel chords of length 10 and 24 on same side radius",
                    "what_to_explain": "In circle r = 13, half-chords are 12 and 5. Their distances from centre are 5 and 12 cm. Separation is 12 - 5 = 7 cm."
                },
                {
                    "concept_title": "Monotonic Decay: Chord Length vs Distance",
                    "diagram_title": "L(d) = 2*sqrt(r^2 - d^2)",
                    "interactive_math_formula": "L = 2\\sqrt{100 - d^2}",
                    "mafs_graph_config": {
                        "domain": [0, 12],
                        "range": [0, 22],
                        "curves": [
                            {"fn": "2*sqrt(max(0, 100 - x^2))", "color": "#2563EB", "label": "L(d) for r=10"}
                        ],
                        "points": [
                            {"x": 0, "y": 20, "label": "Max: Diameter L=20"},
                            {"x": 6, "y": 16, "label": "d=6, L=16"},
                            {"x": 8, "y": 12, "label": "d=8, L=12"},
                            {"x": 10, "y": 0, "label": "d=10, L=0 (Tangent)"}
                        ]
                    },
                    "image_query": "graph of chord length as function of distance from circle centre",
                    "video_query": "relationship between chord length and distance from centre",
                    "what_to_explain": "As distance d increases from 0 to r, chord length smoothly drops from the diameter 2r down to 0."
                },
                {
                    "concept_title": "Classic 5-12-13 Right Triangle in Circle",
                    "diagram_title": "Half-Chord 12, Distance 5, Radius 13",
                    "interactive_math_formula": "5^2 + 12^2 = 13^2",
                    "mafs_graph_config": {
                        "domain": [-15, 15],
                        "range": [-15, 15],
                        "curves": [
                            {"fn": "sqrt(169 - x^2)", "color": "#2563EB", "label": "Circle r=13"},
                            {"fn": "-sqrt(169 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 0, "y": 5, "label": "M(0, 5) [d=5]"},
                            {"x": 12, "y": 5, "label": "A(12, 5) [r=13]"},
                            {"x": -12, "y": 5, "label": "B(-12, 5)"}
                        ]
                    },
                    "image_query": "pythagorean theorem chord 24 distance 5 radius 13",
                    "video_query": "find length of chord distance 5 cm radius 13 cm",
                    "what_to_explain": "Hypotenuse is radius 13 cm, perpendicular distance is 5 cm, half-chord is 12 cm, so full chord is 24 cm."
                },
                {
                    "concept_title": "Shortest Chord Through Interior Point A",
                    "diagram_title": "Perpendicular Chord Minimizes Length",
                    "interactive_math_formula": "L_{\\min} = 2\\sqrt{r^2 - OA^2}",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Circle r=8"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 999, "intercept": 4, "color": "#DC2626", "label": "Shortest Chord (perp to OA)"},
                            {"slope": 0.5, "intercept": 2, "color": "#94A3B8", "label": "Longer Oblique Chord"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 4, "y": 0, "label": "Point A(4, 0)"}
                        ]
                    },
                    "image_query": "shortest chord through a point in circle perpendicular to radius",
                    "video_query": "shortest chord of a circle passing through a given point",
                    "what_to_explain": "For any chord through A, distance d <= OA. Distance is maximized when d = OA, which minimizes chord length."
                },
                {
                    "concept_title": "Diameter Maximality: L <= 2r",
                    "diagram_title": "Diameter Passes Through Centre (d = 0)",
                    "interactive_math_formula": "d = 0 \\implies L = 2\\sqrt{r^2 - 0} = 2r",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [-8, 8],
                        "curves": [
                            {"fn": "sqrt(36 - x^2)", "color": "#2563EB", "label": "Circle r=6"},
                            {"fn": "-sqrt(36 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#16A34A", "label": "Diameter (d=0, L=12)"},
                            {"slope": 0, "intercept": 4, "color": "#DC2626", "label": "Chord (d=4, L=8.94)"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O"},
                            {"x": -6, "y": 0, "label": "-r"},
                            {"x": 6, "y": 0, "label": "+r"}
                        ]
                    },
                    "image_query": "diameter is the longest chord of a circle proof diagram",
                    "video_query": "prove that diameter is the longest chord of a circle",
                    "what_to_explain": "Any non-diameter chord has d > 0, so 2*sqrt(r^2 - d^2) is strictly less than 2r."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Chord Distance Formula",
                    "questions": [
                        {
                            "question": "What is the length of a chord in a circle of radius 13 cm if its distance from the centre is 5 cm?",
                            "type": "short_answer",
                            "ideal_answer": "24 cm (half-chord is sqrt(13^2 - 5^2) = 12 cm, so chord is 2 * 12 = 24 cm).",
                            "socratic_hint": "Use Pythagoras theorem on the right triangle formed by the radius, distance, and half-chord."
                        },
                        {
                            "question": "Why is the shortest chord passing through an interior point A perpendicular to segment OA?",
                            "type": "short_answer",
                            "ideal_answer": "Because the distance d from the centre to any chord through A satisfies d <= OA; the distance is maximized when d = OA (at 90°), which minimizes chord length 2*sqrt(r^2 - d^2).",
                            "socratic_hint": "Remember that greater distance from the centre means shorter chord length."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 5.5 Q1: Find the length of the chord of a circle where the radius is 7 cm and perpendicular distance is 6 cm.",
                "given": "Radius r = 7 cm, perpendicular distance d = 6 cm.",
                "formula": "Chord length L = 2*sqrt(r^2 - d^2).",
                "substitution": "L = 2*sqrt(7^2 - 6^2).",
                "calculation": "1. 7^2 = 49.\n2. 6^2 = 36.\n3. r^2 - d^2 = 49 - 36 = 13.\n4. Half-chord s = sqrt(13) cm.\n5. Full chord length L = 2*sqrt(13) approx 2 * 3.606 = 7.21 cm.",
                "finalAnswer": "2*sqrt(13) cm (approx 7.21 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.5 Q2: Explain why the statement is true: If the perpendicular distance of a chord from the centre is d and radius is r, then chord length is 2*sqrt(r^2 - d^2).",
                "given": "A circle with centre O, radius r, chord AB, and perpendicular OM from O to AB of length d.",
                "formula": "Baudhayana-Pythagoras theorem: OM^2 + AM^2 = OA^2.",
                "substitution": "OM = d, OA = r, AM = s (half-chord).",
                "calculation": "1. By Theorem 5, the perpendicular OM from centre O bisects chord AB: AM = MB = AB / 2.\n2. In right-angled triangle OMA, angle OMA = 90°.\n3. By Pythagoras theorem: OA^2 = OM^2 + AM^2 => r^2 = d^2 + AM^2.\n4. Subtract d^2 from both sides: AM^2 = r^2 - d^2.\n5. Take square root: AM = sqrt(r^2 - d^2).\n6. Full chord length AB = 2 * AM = 2*sqrt(r^2 - d^2).",
                "finalAnswer": "Proved: Half-chord is sqrt(r^2 - d^2) by Pythagoras theorem, so full chord length is 2*sqrt(r^2 - d^2).",
                "unit": "algebraic derivation",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q1: In a circle, a chord is 5 cm away from the centre. If the radius of the circle is 13 cm, what is the length of the chord?",
                "given": "Radius r = 13 cm, perpendicular distance d = 5 cm.",
                "formula": "L = 2*sqrt(r^2 - d^2).",
                "substitution": "L = 2*sqrt(13^2 - 5^2).",
                "calculation": "1. 13^2 = 169.\n2. 5^2 = 25.\n3. 169 - 25 = 144.\n4. sqrt(144) = 12 cm (half-chord).\n5. L = 2 * 12 = 24 cm.",
                "finalAnswer": "24 cm",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q3: The diameter of a circle is 26 cm. A chord of length 24 cm is drawn in the circle. Find the distance from the centre of the circle to the chord.",
                "given": "Diameter D = 26 cm => Radius r = 26 / 2 = 13 cm. Chord length L = 24 cm.",
                "formula": "d = sqrt(r^2 - (L/2)^2).",
                "substitution": "Half-chord s = 24 / 2 = 12 cm. d = sqrt(13^2 - 12^2).",
                "calculation": "1. 13^2 = 169.\n2. 12^2 = 144.\n3. d^2 = 169 - 144 = 25.\n4. d = sqrt(25) = 5 cm.",
                "finalAnswer": "5 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4: A circle has a radius of 15 cm. A chord is drawn at a distance of 9 cm from the centre. What is the length of the chord?",
                "given": "Radius r = 15 cm, distance d = 9 cm.",
                "formula": "L = 2*sqrt(r^2 - d^2).",
                "substitution": "L = 2*sqrt(15^2 - 9^2).",
                "calculation": "1. 15^2 = 225.\n2. 9^2 = 81.\n3. 225 - 81 = 144.\n4. Half-chord s = sqrt(144) = 12 cm.\n5. Full chord L = 2 * 12 = 24 cm.",
                "finalAnswer": "24 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q9: The distance of a chord of length 16 cm from the centre of a circle is 6 cm. Find the radius of the circle.",
                "given": "Chord length L = 16 cm => Half-chord s = 16 / 2 = 8 cm. Distance d = 6 cm.",
                "formula": "r = sqrt(s^2 + d^2).",
                "substitution": "r = sqrt(8^2 + 6^2).",
                "calculation": "1. 8^2 = 64.\n2. 6^2 = 36.\n3. 64 + 36 = 100.\n4. r = sqrt(100) = 10 cm.",
                "finalAnswer": "10 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q13: Draw a circle in which a chord of 6 cm length stands at a distance of 3 cm from the centre. Explain the construction.",
                "given": "Chord L = 6 cm, perpendicular distance d = 3 cm.",
                "formula": "Radius r = sqrt((L/2)^2 + d^2) = sqrt(3^2 + 3^2) = sqrt(18) = 3*sqrt(2) cm.",
                "substitution": "Half-chord s = 3 cm, distance d = 3 cm.",
                "calculation": "1. Calculate required radius: r = sqrt(3^2 + 3^2) = sqrt(9 + 9) = sqrt(18) approx 4.24 cm.\n2. Geometric Construction:\n   - Draw a line segment AB of length 6 cm.\n   - Construct the perpendicular bisector of AB, intersecting AB at its midpoint M (so AM = MB = 3 cm).\n   - On the perpendicular bisector, mark a point O at a distance of 3 cm from M (so OM = 3 cm).\n   - With O as centre and radius OA (where OA = sqrt(3^2 + 3^2) = 3*sqrt(2) cm), draw the circle.\n3. The circle passes through A and B, and chord AB has length 6 cm at distance 3 cm from centre O.",
                "finalAnswer": "Construct line AB = 6 cm, find midpoint M, mark centre O along perpendicular bisector at OM = 3 cm, and draw circle with radius OA = 3*sqrt(2) cm (approx 4.24 cm).",
                "unit": "construction",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q18: Two parallel chords of lengths 10 cm and 24 cm are on the same side of the centre of a circle. The distance between the chords is 7 cm. Find the radius of the circle.",
                "given": "Parallel chords on SAME side: L1 = 24 cm (half-chord s1 = 12 cm), L2 = 10 cm (half-chord s2 = 5 cm). Distance between chords = 7 cm.",
                "formula": "Let distance of chord 1 from centre be d. Then distance of chord 2 is d + 7. In both right triangles: r^2 = d^2 + 12^2 and r^2 = (d + 7)^2 + 5^2.",
                "substitution": "Equate the two expressions for r^2: d^2 + 144 = (d + 7)^2 + 25.",
                "calculation": "1. Expand RHS: (d + 7)^2 + 25 = d^2 + 14d + 49 + 25 = d^2 + 14d + 74.\n2. Set equal to LHS: d^2 + 144 = d^2 + 14d + 74.\n3. Subtract d^2 from both sides: 144 = 14d + 74.\n4. 14d = 144 - 74 = 70.\n5. d = 70 / 14 = 5 cm.\n6. Compute radius r:\n   r^2 = d^2 + 12^2 = 5^2 + 12^2 = 25 + 144 = 169.\n   r = sqrt(169) = 13 cm.\n7. Check with chord 2: distance = 5 + 7 = 12 cm. r^2 = 12^2 + 5^2 = 144 + 25 = 169. Consistent!",
                "finalAnswer": "13 cm",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q22: 'There is no chord of a circle that is longer than its diameter.' How do you justify this statement?",
                "given": "A circle of radius r and diameter D = 2r. Let AB be any chord with distance d from centre O.",
                "formula": "Chord length formula: L = 2*sqrt(r^2 - d^2). Alternatively, Triangle Inequality in triangle OAB.",
                "substitution": "In triangle OAB, side AB < OA + OB.",
                "calculation": "1. Proof Method 1 (Algebraic): For any chord AB, the perpendicular distance d from centre O satisfies d >= 0.\n   Since d^2 >= 0, r^2 - d^2 <= r^2.\n   Taking square root: sqrt(r^2 - d^2) <= r.\n   Multiplying by 2: L = 2*sqrt(r^2 - d^2) <= 2r.\n   Since 2r is the diameter, L <= Diameter, with equality if and only if d = 0 (when chord passes through centre).\n2. Proof Method 2 (Geometric Triangle Inequality): If chord AB does not pass through centre O, points O, A, B form a triangle.\n   By the triangle inequality: AB < OA + OB.\n   Since OA = r and OB = r, AB < r + r = 2r.\n   If chord AB passes through centre O, then A, O, B are collinear and AB = OA + OB = 2r.\n3. In all cases, AB <= 2r.",
                "finalAnswer": "Proved: By the triangle inequality, AB <= OA + OB = 2r = diameter. Equality holds only when the chord passes through the centre.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q23: Let A be any point within a given circle with centre O. Show that the shortest chord of the circle that passes through point A is the one that is perpendicular to OA.",
                "given": "Circle with centre O and radius r. Point A is inside the circle (OA < r).",
                "formula": "Chord length L = 2*sqrt(r^2 - d^2), where d is the perpendicular distance from centre O to the chord.",
                "substitution": "Compare perpendicular chord through A with any other chord through A.",
                "calculation": "1. Let C1 be the chord through A perpendicular to segment OA. The foot of perpendicular from O to C1 is point A itself, so distance d1 = OA.\n   Length of C1 = 2*sqrt(r^2 - OA^2).\n2. Let C2 be any other chord passing through A that is not perpendicular to OA.\n   Drop perpendicular OM from centre O to chord C2. In right triangle OMA, angle OMA = 90°.\n   In any right-angled triangle, the hypotenuse is strictly longer than either leg: OA > OM => OM < OA, meaning distance d2 < OA.\n3. Now compare chord lengths:\n   Since d2 < OA, d2^2 < OA^2 => -d2^2 > -OA^2 => r^2 - d2^2 > r^2 - OA^2.\n4. Taking square roots and multiplying by 2:\n   2*sqrt(r^2 - d2^2) > 2*sqrt(r^2 - OA^2).\n5. This proves that any other chord C2 is strictly longer than C1.\n6. Therefore, chord C1 (which is perpendicular to OA) is the shortest possible chord passing through point A.",
                "finalAnswer": "Proved: The perpendicular distance to any oblique chord through A is less than OA, making its length strictly greater than 2*sqrt(r^2 - OA^2).",
                "unit": "extremal proof",
                "has_diagram": True
            }
        ]
    }
