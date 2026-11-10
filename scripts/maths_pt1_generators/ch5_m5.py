"""
Chapter 5: I’m Up and Down, and Round and Round - Module 5
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_circle_geometry_svg

def get_m5():
    m5_svg = build_circle_geometry_svg(
        radius=90, center=(290, 200),
        points=[
            {"x": 290, "y": 200, "label": "Centre O"},
            {"x": 226, "y": 264, "label": "A"},
            {"x": 354, "y": 264, "label": "B"},
            {"x": 290, "y": 110, "label": "C (Inscribed theta)"}
        ],
        angles=[
            {"p1": (226, 264), "vertex": (290, 200), "p2": (354, 264), "label": "2*theta = 70°", "color": "#2563EB"},
            {"p1": (226, 264), "vertex": (290, 110), "p2": (354, 264), "label": "theta = 35°", "color": "#DC2626"}
        ],
        title="Inscribed Angle Theorem: 2θ at Centre, θ at Circumference",
        caption="Arc AB subtends central angle 2*theta = 70° and inscribed angle theta = 35° on circumference"
    )

    return {
        "order_index": 5,
        "title": "Textbook Exercise Solver 4: Inscribed Angles, Arc Subtensions & Semicircle Right Angles (Exercise 5.6 Part 2 & End-of-Chapter Set 2)",
        "description": "Comprehensive step-by-step solutions to Exercise 5.6 (Q2 parts i to iii, Q3) and End-of-Chapter Questions 2, 6, 20, and 24. Master the Inscribed Angle Theorem (central angle = 2 * inscribed angle), angles in the same segment equality, Thales theorem (angle in a semicircle is 90°), and arc subtension calculations.",
        "subtopics": [
            "Inscribed Angle Theorem: The angle subtended by an arc at the centre is double the angle subtended by it on the circle",
            "Angles in the same segment of a circle are equal (Theorem 9)",
            "Concyclicity Criterion: Segment subtending equal angles at two points on the same side (Theorem 10)",
            "Thales' Theorem: The angle subtended by a diameter (semicircle) is strictly 90°",
            "Algebraic proof using isosceles radii: 2a + 2b = 180° implies a + b = 90°"
        ],
        "key_concepts": [
            "Inscribed Angle Ratio: For any arc AB and point P on the remaining circle, angle AOB = 2 * angle APB.",
            "Same Segment Equality: If C and D lie on the same circular segment of chord AB, angle ACB = angle ADB.",
            "Opposite Segment Supplementarity: If C and D lie on opposite sides of chord AB, angle ACB + angle ADB = 180°.",
            "Angle in a Semicircle: Since the diameter subtends a straight angle (180°) at the centre, any angle inscribed in a semicircle is 180° / 2 = 90°.",
            "Fig 5.30 Angle Partition Proof: In triangle ABC with diameter AB and circumcentre O, OA = OB = OC = r forms two isosceles triangles with base angles a and b. In triangle ABC, 2a + 2b = 180° => a + b = 90°."
        ],
        "success_criteria": "Students can apply the Inscribed Angle Theorem to find unknown angles, prove that angles in a semicircle are right angles, and establish concyclicity of four points.",
        "chapter_notes": "Module 5 covers the core angular theorems of circles that establish the foundations for cyclic quadrilaterals and circle geometry.",
        "common_misconceptions": [
            {"misconception": "Believing the inscribed angle equals the central angle", "clarification": "The inscribed angle is exactly HALF of the central angle subtended by the same arc: theta = (1/2) * (2*theta)."},
            {"misconception": "Applying same-segment theorem to points on opposite sides of the chord", "clarification": "Points on opposite sides of a chord subtend supplementary angles (summing to 180°), not equal angles."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through inscribed angles and Thales theorem. Show how drawing the radius to the inscribed vertex splits the triangle into two isosceles triangles.",
        "visual_lesson_plan": {
            "title": "Visualizing Inscribed and Semicircular Angles",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Interactive circle showing central angle 70° and inscribed angle 35° subtended by the same arc.",
            "concept_visuals": [
                {
                    "concept_title": "Inscribed Angle Theorem: 2*theta vs theta",
                    "diagram_title": "Central Angle 70° vs Inscribed Angle 35°",
                    "interactive_math_formula": "\\angle APB = \\frac{1}{2} \\angle AOB = \\frac{70^\\circ}{2} = 35^\\circ",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Circle r=8"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O (70°)"},
                            {"x": -4.59, "y": -6.55, "label": "A"},
                            {"x": 4.59, "y": -6.55, "label": "B"},
                            {"x": 0, "y": 8, "label": "P (35°)"}
                        ]
                    },
                    "image_query": "inscribed angle theorem central angle double circle geometry",
                    "video_query": "angle subtended by arc at centre is double angle on circle proof",
                    "what_to_explain": "The central angle 2*theta is exactly twice any inscribed angle theta on the opposite arc."
                },
                {
                    "concept_title": "Thales Semicircle Right Angle: 90°",
                    "diagram_title": "Angle Subtended by Diameter is 90°",
                    "interactive_math_formula": "\\angle ACB = \\frac{180^\\circ}{2} = 90^\\circ",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [-8, 8],
                        "curves": [
                            {"fn": "sqrt(36 - x^2)", "color": "#2563EB", "label": "Circle r=6"},
                            {"fn": "-sqrt(36 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#16A34A", "label": "Diameter AB"}
                        ],
                        "points": [
                            {"x": -6, "y": 0, "label": "A(-6, 0)"},
                            {"x": 6, "y": 0, "label": "B(6, 0)"},
                            {"x": 2, "y": 5.66, "label": "C (90°)"},
                            {"x": 0, "y": 0, "label": "O (180°)"}
                        ]
                    },
                    "image_query": "angle in a semicircle is a right angle Thales theorem",
                    "video_query": "prove that angle in a semicircle is 90 degrees",
                    "what_to_explain": "Because the diameter subtends 180° at the centre, the angle on the semicircle circumference is 180° / 2 = 90°."
                },
                {
                    "concept_title": "Angles in the Same Segment are Equal",
                    "diagram_title": "angle ACB = angle ADB",
                    "interactive_math_formula": "\\angle ACB = \\angle ADB = \\theta",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Circle"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": -6, "y": -5.29, "label": "A"},
                            {"x": 6, "y": -5.29, "label": "B"},
                            {"x": -2, "y": 7.75, "label": "C (theta)"},
                            {"x": 4, "y": 6.93, "label": "D (theta)"}
                        ]
                    },
                    "image_query": "angles in the same segment of a circle are equal theorem",
                    "video_query": "angles in same segment of circle are equal proof",
                    "what_to_explain": "Both inscribed angles C and D subtend the exact same arc AB, so both are equal to (1/2)*angle AOB."
                },
                {
                    "concept_title": "Fig 5.30 Proof Breakdown: 2a + 2b = 180°",
                    "diagram_title": "Two Isosceles Radii Triangles OAC and OBC",
                    "interactive_math_formula": "2(a + b) = 180^\\circ \\implies a + b = 90^\\circ",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [-8, 8],
                        "points": [
                            {"x": -6, "y": 0, "label": "A (angle a)"},
                            {"x": 6, "y": 0, "label": "B (angle b)"},
                            {"x": 0, "y": 0, "label": "O"},
                            {"x": 0, "y": 6, "label": "C (angle a + b = 90°)"}
                        ]
                    },
                    "image_query": "proof angle in semicircle 90 degrees two isosceles triangles",
                    "video_query": "algebraic proof angle in semicircle is 90 degrees",
                    "what_to_explain": "Connecting centre O to C creates isosceles triangles OAC and OBC with base angles a and b. Sum of angles in triangle ABC is 2a + 2b = 180°, so angle C = a + b = 90°."
                },
                {
                    "concept_title": "Intersecting Chords Angle Relation (Fig 5.26)",
                    "diagram_title": "Central & Inscribed Angles with Bowtie Intersections",
                    "interactive_math_formula": "x = 180^\\circ - 100^\\circ = 80^\\circ",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Circle"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": -5, "y": 6.24, "label": "D (100°)"},
                            {"x": 5, "y": 6.24, "label": "C"},
                            {"x": 5, "y": -6.24, "label": "B (x)"},
                            {"x": -5, "y": -6.24, "label": "A"}
                        ]
                    },
                    "image_query": "cyclic quadrilateral find angle x textbook problem",
                    "video_query": "find angle x in circle geometry intersecting chords",
                    "what_to_explain": "Using circle segment properties and angle sum of intersecting chords allows direct solution for unknown angle x."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Arc Subtensions and Semicircles",
                    "questions": [
                        {
                            "question": "If an arc of a circle subtends an angle of 70° at the centre, what is the angle subtended by it at a point on the remaining circle?",
                            "type": "short_answer",
                            "ideal_answer": "35° (the inscribed angle is half the central angle: 70° / 2 = 35°).",
                            "socratic_hint": "Recall the Inscribed Angle Theorem: angle at circumference = (1/2) * angle at centre."
                        },
                        {
                            "question": "What is the measure of an angle inscribed in a semicircle?",
                            "type": "short_answer",
                            "ideal_answer": "90° (a right angle).",
                            "socratic_hint": "What is the angle subtended by a straight diameter line at the centre of the circle?"
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 5.6 Q2 (i): Let A and B be two points on a circle with centre O. Are there points X, Y on the circle, on the same side of AB, such that angle AXB is different from angle AYB?",
                "given": "Points A, B on a circle with centre O. Points X, Y lie on the circumference on the SAME side of chord AB.",
                "formula": "Theorem 9 (Angles in the same segment): Angles subtended by an arc at any points in the same segment of a circle are equal.",
                "substitution": "Angle AXB and angle AYB are both inscribed in the same major (or minor) segment of chord AB.",
                "calculation": "1. Let arc AB subtend a central angle angle AOB = 2*theta.\n2. By the Inscribed Angle Theorem, any point X on the circle on the remaining part of the arc subtends angle AXB = (1/2)*angle AOB = theta.\n3. Similarly, for point Y on the same segment, angle AYB = (1/2)*angle AOB = theta.\n4. Therefore, angle AXB = angle AYB = theta for all points on the same side of AB.\n5. Hence, there can be NO points X and Y on the same side of AB having different angles.",
                "finalAnswer": "No, it is impossible. By Theorem 9, all angles subtended by chord AB at points in the same segment of the circle are strictly equal (angle AXB = angle AYB).",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.6 Q2 (ii): Is it true that if angle AXB = angle AYB, then X and Y must lie on the same side of the circle?",
                "given": "Points X, Y on the circle with angle AXB = angle AYB.",
                "formula": "Opposite Segment Theorem: If X and Y lie on opposite sides of chord AB, then quadrilateral AXBY is cyclic, so angle AXB + angle AYB = 180°.",
                "substitution": "Test whether angle AXB can equal angle AYB when on opposite sides.",
                "calculation": "1. If X and Y are on the same side of AB, then angle AXB = angle AYB is always true.\n2. If X and Y are on OPPOSITE sides of AB, then AXBY forms a cyclic quadrilateral.\n3. In a cyclic quadrilateral, opposite angles are supplementary: angle AXB + angle AYB = 180°.\n4. If we also have angle AXB = angle AYB, then 2*angle AXB = 180° => angle AXB = 90°.\n5. In the special case where AB is a diameter, angle AXB = 90° and angle AYB = 90°, so angle AXB = angle AYB even when X and Y lie on opposite sides of AB.\n6. For any chord AB that is not a diameter (angle AXB != 90°), angle AXB = angle AYB strictly forces X and Y to lie on the same side.",
                "finalAnswer": "It is true for all non-diameter chords. (The only exception is when AB is a diameter, where both angles are 90° even on opposite sides).",
                "unit": "theorem analysis",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.6 Q2 (iii): If angle AXB = angle AYB, and X and Y do not lie on the circle, does the circle through A, B, and X also pass through Y?",
                "given": "Segment AB subtends equal angles at points X and Y (angle AXB = angle AYB) lying on the same side of AB.",
                "formula": "Theorem 10 (Concyclicity Criterion): If a line segment joining two points subtends equal angles at two other points on the same side, the four points are concyclic.",
                "substitution": "Points A, B, X, Y lie on the same circle.",
                "calculation": "1. Draw the unique circle passing through the three non-collinear points A, B, and X.\n2. Suppose to the contrary that Y does not lie on this circle.\n3. Then line AY (or its extension) must intersect the circle at some distinct point Y'.\n4. Since Y' lies on the circle with A, B, and X, by Theorem 9: angle AY'B = angle AXB.\n5. But we are given angle AXB = angle AYB, which implies angle AY'B = angle AYB.\n6. In triangle BYY', an exterior angle would equal an interior opposite angle, which is impossible in Euclidean geometry unless Y and Y' coincide.\n7. Therefore, Y must lie on the circle through A, B, and X.",
                "finalAnswer": "Yes, the circle through A, B, and X must also pass through Y (by Theorem 10, the four points A, B, X, Y are concyclic).",
                "unit": "concyclicity proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.6 Q3: Find the value of angle x in Fig. 5.26.",
                "given": "Circle with chords forming cyclic configuration. Angle at D = 100°.",
                "formula": "Sum of opposite angles of a cyclic quadrilateral is 180°: angle D + angle B = 180°.",
                "substitution": "100° + x = 180°.",
                "calculation": "1. Identify the inscribed quadrilateral ABCD in Fig. 5.26.\n2. Vertices A, B, C, D all lie on the circumference of the circle, so ABCD is a cyclic quadrilateral.\n3. By the Cyclic Quadrilateral Theorem, the opposite angles sum to 180°:\n   angle ADC + angle ABC = 180°.\n4. Given angle ADC = 100° and angle ABC = x:\n   100° + x = 180°.\n5. Subtract 100° from both sides: x = 180° - 100° = 80°.",
                "finalAnswer": "x = 80°",
                "unit": "degrees",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q2: An arc of a circle subtends an angle of 70° at the centre. What is the measure of the angle subtended by the arc at a point on the circle?",
                "given": "Central angle angle AOB = 70°.",
                "formula": "Inscribed Angle Theorem: angle APB = (1/2) * angle AOB.",
                "substitution": "angle APB = 70° / 2.",
                "calculation": "1. 70° / 2 = 35°.\n2. The angle subtended at any point on the remaining circumference is exactly 35°.",
                "finalAnswer": "35°",
                "unit": "degrees",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q6: The diameter of a circle is AB. Point C is on the circumference. What is the measure of angle ACB? Explain your reasoning.",
                "given": "Diameter AB of circle with centre O. Point C lies on the circumference.",
                "formula": "Central angle subtended by diameter AB is 180° (a straight line). Inscribed angle angle ACB = (1/2) * 180°.",
                "substitution": "angle ACB = 180° / 2.",
                "calculation": "1. Since AB is a diameter, segment AOB is a straight line, so central angle angle AOB = 180°.\n2. By the Inscribed Angle Theorem, the angle subtended by arc AB at any point C on the circle is half the central angle:\n   angle ACB = (1/2) * angle AOB = (1/2) * 180° = 90°.\n3. Therefore, angle ACB is a right angle (90°).",
                "finalAnswer": "90° (The angle subtended by a diameter at the circumference is half of the straight angle 180°, which is 90°).",
                "unit": "degrees",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q20: A quadrilateral MNOP is inscribed in a circle. If MN is a diameter, what can you say about angle MOP and angle MNP? Explain your reasoning.",
                "given": "Cyclic quadrilateral MNOP with diameter MN.",
                "formula": "Angle inscribed in a semicircle is 90°: angle MON is a straight angle = 180°, so angle MPN = 90°.",
                "substitution": "MN is diameter, so triangle MPN has hypotenuse MN.",
                "calculation": "1. Since MN is a diameter, any point on the circumference subtends a right angle with MN.\n2. In particular, vertex P lies on the circumference, so angle MPN = 90°.\n3. Similarly, vertex O lies on the circumference, so angle MON is not 90° because O is a vertex on the circumference and MN is a diameter; rather, the segment MO and ON subtend angle MON = 90°.\n4. In cyclic quadrilateral MNOP, the opposite angles sum to 180°:\n   angle MNP + angle MOP = 180° (opposite angles of cyclic quad).\n5. Therefore, angle MOP and angle MNP are supplementary: angle MOP + angle MNP = 180°.",
                "finalAnswer": "angle MOP and angle MNP are supplementary (angle MOP + angle MNP = 180°) because they are opposite angles of cyclic quadrilateral MNOP. Furthermore, angle MPN = 90° and angle MON = 90°.",
                "unit": "geometric deduction",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q24: How would you use Fig. 5.30 to justify the statement that the angle in a semicircle is 90°?",
                "given": "Fig. 5.30: Circle with diameter AB, centre O, point C on circumference. Radii OA, OB, OC are drawn, dividing angle C into a and b.",
                "formula": "OA = OC => angle OAC = angle OCA = a. OB = OC => angle OBC = angle OCB = b. Sum of angles in triangle ABC = 180°.",
                "substitution": "angle A = a, angle B = b, angle C = a + b.",
                "calculation": "1. In triangle OAC: OA = OC = r (both are radii). Therefore, triangle OAC is isosceles, so angle OAC = angle OCA = a.\n2. In triangle OBC: OB = OC = r (both are radii). Therefore, triangle OBC is isosceles, so angle OBC = angle OCB = b.\n3. Total angle at vertex C is angle ACB = angle OCA + angle OCB = a + b.\n4. Consider triangle ABC. The sum of interior angles of triangle ABC is 180°:\n   angle A + angle B + angle ACB = 180°.\n5. Substitute the expressions in terms of a and b:\n   a + b + (a + b) = 180° => 2a + 2b = 180°.\n6. Factor out 2:\n   2(a + b) = 180°.\n7. Divide by 2:\n   a + b = 90°.\n8. Since angle ACB = a + b, we have angle ACB = 90°.",
                "finalAnswer": "Proved using Fig. 5.30: OA=OC and OB=OC create two isosceles triangles with base angles a and b. In triangle ABC, 2(a + b) = 180°, so angle ACB = a + b = 90°.",
                "unit": "algebraic proof",
                "has_diagram": True
            }
        ]
    }
