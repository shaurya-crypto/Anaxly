"""
Chapter 5: I’m Up and Down, and Round and Round - Module 1
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_circle_geometry_svg

def get_m1():
    m1_svg = build_circle_geometry_svg(
        radius=90, center=(290, 200),
        points=[
            {"x": 290, "y": 200, "label": "Circumcentre O"},
            {"x": 230, "y": 140, "label": "A"},
            {"x": 350, "y": 140, "label": "B"},
            {"x": 290, "y": 290, "label": "C"}
        ],
        triangles=[
            {"pts": [(230, 140), (350, 140), (290, 290)], "stroke": "#2563EB", "fill": "rgba(37,99,235,0.08)"}
        ],
        title="Circumcircle & Triangle Circumcentre",
        caption="Unique circle passing through non-collinear vertices A, B, C with circumcentre O at bisector intersection"
    )

    return {
        "order_index": 1,
        "title": "Symmetries, Points and Circles: Triangle Circumcentres & Uniqueness (Exercise 5.1 & Think/Infer Complete)",
        "description": "Comprehensive step-by-step solutions to in-text examples, Exercise 5.1, and Think, Draw and Infer activities. Explore circle reflection and rotational symmetries, the two-point infinite coaxal family, perpendicular bisectors, and circumcentres of acute, obtuse, and right-angled triangles.",
        "subtopics": [
            "Geometric definition of a circle and continuous rotational and reflection symmetries",
            "Circles through points: infinite coaxal family through two points vs uniqueness through three non-collinear points",
            "Minimum radius invariant through two points A and B (radius = AB/2)",
            "Circumcentre position theorem: interior for acute, hypotenuse midpoint for right, exterior for obtuse triangles",
            "Impossibility proof: Why no circle can pass through three collinear points"
        ],
        "key_concepts": [
            "Circle Locus: Set of all coplanar points equidistant from a fixed centre point.",
            "Diameter Reflection Symmetry: A circle reflects onto itself across every line passing through its centre.",
            "Two-Point Coaxal Locus: The locus of centres of all circles passing through A and B is the perpendicular bisector of segment AB.",
            "Minimum Circle Invariant: The smallest circle through points A and B has diameter AB, with radius equal to AB/2.",
            "Circumcentre Invariant: The intersection of perpendicular bisectors of any two sides of a triangle is equidistant from all three vertices (OA = OB = OC = R).",
            "Collinear Parallelism: Perpendicular bisectors of segments between three collinear points are parallel and cannot intersect, proving collinear points cannot be concyclic."
        ],
        "success_criteria": "Students can construct circumcircles for any given triangle, determine whether circumcentres lie inside, outside, or on the boundary, and prove uniqueness and non-concyclicity.",
        "chapter_notes": "Module 1 establishes the axiomatic foundation of circular geometry and the definitive relationship between triangles and circumcircles.",
        "common_misconceptions": [
            {"misconception": "Believing a circle's centre is always inside any inscribed triangle", "clarification": "For an obtuse triangle, the circumcentre lies strictly outside the triangle; for a right triangle, it lies exactly on the hypotenuse midpoint."},
            {"misconception": "Thinking three collinear points can define a very large circle", "clarification": "A straight line can intersect a circle in at most two points; three collinear points can never lie on any circle."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Chapter 5 Module 1. Draw diagrams of triangles and their circumcircles on the digital chalkboard, highlighting the position of the circumcentre relative to the triangle's angles.",
        "visual_lesson_plan": {
            "title": "Visualizing Symmetries and Triangle Circumcentres",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Interactive circle with an inscribed triangle showing the circumcentre O equidistant to vertices A, B, and C.",
            "concept_visuals": [
                {
                    "concept_title": "Acute Triangle: Circumcentre Inside",
                    "diagram_title": "Equilateral/Acute Inscribed Triangle with Interior O",
                    "interactive_math_formula": "OA = OB = OC = R",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circumcircle r=5"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": "r=5"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": -4.33, "y": -2.5, "label": "A"},
                            {"x": 4.33, "y": -2.5, "label": "B"},
                            {"x": 0, "y": 5, "label": "C"}
                        ]
                    },
                    "image_query": "acute triangle circumcentre inside circle perpendicular bisectors",
                    "video_query": "circumcircle of acute angled triangle construction",
                    "what_to_explain": "All three angles are less than 90°, so the perpendicular bisectors intersect strictly inside the triangle boundary."
                },
                {
                    "concept_title": "Obtuse Triangle: Circumcentre Outside",
                    "diagram_title": "Obtuse Triangle with Exterior Circumcentre",
                    "interactive_math_formula": "\\angle A > 90^\\circ \\implies O \\notin \\Delta ABC",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circumcircle"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Circumcentre O (Outside)"},
                            {"x": 0, "y": 5, "label": "A (Obtuse > 90°)"},
                            {"x": -4.9, "y": 1, "label": "B"},
                            {"x": 4.9, "y": 1, "label": "C"}
                        ]
                    },
                    "image_query": "obtuse triangle circumcentre outside circle geometry",
                    "video_query": "circumcentre of obtuse triangle lies outside",
                    "what_to_explain": "When one angle exceeds 90°, the perpendicular bisectors meet outside the opposite side, placing O exterior to the triangle."
                },
                {
                    "concept_title": "Right-Angled Triangle: Thales Hypotenuse Midpoint",
                    "diagram_title": "Circumcentre at Midpoint of Hypotenuse",
                    "interactive_math_formula": "O = \\text{Midpoint}(AB) \\implies R = \\frac{AB}{2}",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circumcircle"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O = Midpoint(AB)"},
                            {"x": -5, "y": 0, "label": "A(-5, 0)"},
                            {"x": 5, "y": 0, "label": "B(5, 0)"},
                            {"x": 3, "y": 4, "label": "C(3, 4) [90°]"}
                        ]
                    },
                    "image_query": "right triangle circumcentre midpoint of hypotenuse Thales theorem",
                    "video_query": "why circumcentre of right triangle is on hypotenuse",
                    "what_to_explain": "By Thales' theorem, the angle inscribed in a semicircle is 90°, so the hypotenuse is the diameter and its midpoint is the circumcentre."
                },
                {
                    "concept_title": "Two-Point Infinite Coaxal Family",
                    "diagram_title": "Centres Moving on Perpendicular Bisector of AB",
                    "interactive_math_formula": "OA = OB \\implies O \\in \\text{PerpBisector}(AB)",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "lines": [
                            {"slope": 999, "intercept": 0, "color": "#DC2626", "label": "Locus of Centres"}
                        ],
                        "points": [
                            {"x": -3, "y": 0, "label": "A(-3, 0)"},
                            {"x": 3, "y": 0, "label": "B(3, 0)"},
                            {"x": 0, "y": 0, "label": "Min Centre (r=3)"},
                            {"x": 0, "y": 4, "label": "Centre O2 (r=5)"}
                        ]
                    },
                    "image_query": "family of circles passing through two points perpendicular bisector",
                    "video_query": "how many circles can pass through two given points",
                    "what_to_explain": "Every point on the perpendicular bisector can serve as a centre; the smallest circle has radius AB/2 = 3."
                },
                {
                    "concept_title": "Collinear Points: Impossibility of Circle",
                    "diagram_title": "Parallel Perpendicular Bisectors Never Meet",
                    "interactive_math_formula": "L_1 \\parallel L_2 \\implies L_1 \\cap L_2 = \\emptyset",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-4, 4],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Collinear Axis"},
                            {"slope": 999, "intercept": -1.5, "color": "#2563EB", "label": "Bisector 1"},
                            {"slope": 999, "intercept": 1.5, "color": "#059669", "label": "Bisector 2"}
                        ],
                        "points": [
                            {"x": -3, "y": 0, "label": "A"},
                            {"x": 0, "y": 0, "label": "B"},
                            {"x": 3, "y": 0, "label": "C"}
                        ]
                    },
                    "image_query": "why three collinear points cannot form a circle parallel bisectors",
                    "video_query": "prove that a circle cannot pass through three collinear points",
                    "what_to_explain": "The perpendicular bisectors of AB and BC are parallel vertical lines that never intersect, so no circumcentre exists."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Circumcentre Geometry",
                    "questions": [
                        {
                            "question": "Where does the circumcentre of an obtuse-angled triangle lie?",
                            "type": "short_answer",
                            "ideal_answer": "It lies strictly outside (in the exterior of) the triangle.",
                            "socratic_hint": "Recall how the perpendicular bisectors of the two sides adjacent to the obtuse angle extend away from the triangle."
                        },
                        {
                            "question": "What is the minimum radius of a circle that can pass through two points separated by distance d?",
                            "type": "short_answer",
                            "ideal_answer": "d / 2 (when the segment connecting the two points is the diameter of the circle).",
                            "socratic_hint": "Can a chord ever be longer than the diameter of a circle?"
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 5.1 Q1: Draw triangle ABC with AB = 5 cm, angle A = 70°, and angle B = 60°. Draw the circumcircle. Is the centre inside or outside the triangle?",
                "given": "Triangle ABC with AB = 5 cm, angle A = 70°, angle B = 60°.",
                "formula": "Sum of angles in triangle = 180°. Circumcentre is inside if all three angles are < 90° (acute triangle).",
                "substitution": "Angle C = 180° - (70° + 60°).",
                "calculation": "1. Angle C = 180° - 130° = 50°.\n2. All three angles (70°, 60°, 50°) are strictly less than 90°.\n3. Therefore, triangle ABC is an acute-angled triangle.\n4. Draw the perpendicular bisectors of sides AB and BC; their intersection point O is the circumcentre.\n5. Because the triangle is acute-angled, the circumcentre O lies strictly inside the triangle.",
                "finalAnswer": "The centre (circumcentre O) lies strictly INSIDE the triangle (because triangle ABC is acute-angled).",
                "unit": "circumcentre position",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.1 Q2: Draw triangle ABC with AB = 5 cm, angle A = 100°, AC = 4 cm. Draw the circumcircle. Is the centre inside or outside the triangle?",
                "given": "Triangle ABC with angle A = 100° (obtuse angle), AB = 5 cm, AC = 4 cm.",
                "formula": "Circumcentre position rule: For any triangle with an angle > 90°, the circumcentre lies in the exterior of the triangle.",
                "substitution": "Angle A = 100° > 90°.",
                "calculation": "1. Triangle ABC is an obtuse-angled triangle because angle A = 100°.\n2. Construct perpendicular bisectors of AB and AC.\n3. The perpendicular bisectors intersect at circumcentre O on the opposite side of vertex A beyond side BC.\n4. Therefore, circumcentre O lies strictly outside the triangle.",
                "finalAnswer": "The centre lies strictly OUTSIDE the triangle (in the exterior) because triangle ABC has an obtuse angle of 100°.",
                "unit": "circumcentre position",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.1 Q3: Draw triangle ABC with AB = 6 cm, BC = 7 cm, CA = 7 cm. Draw the circumcircle. Let circumcentre be O. Measure and compare OA, OB, OC.",
                "given": "Isosceles triangle with AB = 6 cm, BC = 7 cm, CA = 7 cm.",
                "formula": "By definition of circumcircle, OA = OB = OC = R (radius of circumcircle).",
                "substitution": "Measure distances from circumcentre O to all three vertices A, B, and C.",
                "calculation": "1. Since CA = BC = 7 cm and AB = 6 cm, triangle ABC is an acute isosceles triangle.\n2. Construct the perpendicular bisector of base AB (which is also the median and altitude from C).\n3. Construct the perpendicular bisector of side AC. Their intersection is circumcentre O.\n4. Measuring OA, OB, and OC with a ruler confirms OA = OB = OC approx 3.65 cm.\n5. Circumcentre O lies inside the triangle.",
                "finalAnswer": "OA = OB = OC = R (approx 3.65 cm). All three lengths are exactly equal because O is equidistant to all three vertices.",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.1 Q4: What is the least possible radius of a circle through two points A and B separated by distance d?",
                "given": "Two points A and B with distance AB = d.",
                "formula": "Any segment AB inscribed in a circle is a chord. A chord of length d cannot exceed the diameter: d <= 2r => r >= d/2.",
                "substitution": "r_min = AB / 2 = d / 2.",
                "calculation": "1. The longest chord in any circle is its diameter (length 2r).\n2. Since A and B lie on the circle, segment AB is a chord of length d.\n3. Therefore, d <= 2r, which means r >= d/2.\n4. The minimum radius occurs when equality holds, which is when segment AB is the diameter of the circle.\n5. In this case, the centre of the circle is the midpoint of AB, and radius is d/2.",
                "finalAnswer": "The least possible radius is AB / 2 (half the distance between A and B).",
                "unit": "radius",
                "has_diagram": True
            },
            {
                "problem": "Think, Draw & Infer 1: A, B, C are three collinear points. Can you find a point P such that PA = PB = PC? Show that perpendicular bisectors of AB and BC are parallel. Can a circle pass through collinear points?",
                "given": "Three distinct collinear points A, B, C lying on line L.",
                "formula": "Perpendicular to a line at distinct points are parallel: if L1 perp L and L2 perp L, then L1 || L2.",
                "substitution": "Let M1 be midpoint of AB, M2 be midpoint of BC.",
                "calculation": "1. The perpendicular bisector of AB is line L1 perpendicular to line L at M1.\n2. The perpendicular bisector of BC is line L2 perpendicular to line L at M2.\n3. Because both L1 and L2 are perpendicular to the same straight line L at distinct points M1 != M2, lines L1 and L2 are strictly parallel (L1 || L2).\n4. Since parallel lines in Euclidean geometry never intersect, there is no point that lies on both bisectors: L1 cap L2 = emptyset.\n5. Therefore, no point P can be equidistant to A, B, and C (PA = PB = PC is impossible).\n6. Consequently, no circle can pass through three collinear points, and a straight line can cut a circle at most at two distinct points.",
                "finalAnswer": "No point P can satisfy PA = PB = PC. The perpendicular bisectors are parallel and never intersect, proving no circle can pass through collinear points.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "Think, Draw & Infer 2: The circumcircle of a given triangle ABC is drawn. Can there be other triangles congruent to triangle ABC that share the exact same circumcircle?",
                "given": "A circumcircle C with inscribed triangle ABC.",
                "formula": "Rigid motions (rotations and reflections) preserve distance, producing congruent triangles inscribed in the same circle.",
                "substitution": "Rotate triangle ABC about the circumcentre O by any arbitrary angle theta.",
                "calculation": "1. If triangle ABC is rotated by any non-zero angle theta about circumcentre O, the vertices move to A', B', C'.\n2. Since rotation preserves distances from O, OA' = OA = R, OB' = OB = R, OC' = OC = R, so A', B', C' all lie on the exact same circumcircle.\n3. Since rotation is an isometry, triangle A'B'C' is congruent to triangle ABC.\n4. Continuous rotation produces infinitely many congruent triangles inscribed in the same circumcircle.\n5. Reflection across any diameter also produces congruent inscribed triangles.",
                "finalAnswer": "Yes, infinitely many congruent triangles can share the exact same circumcircle (obtained by rotating or reflecting triangle ABC about the centre O).",
                "unit": "congruence geometry",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q5: Prove that the perpendicular bisector of a chord of a circle passes through the centre of the circle.",
                "given": "A circle with centre O and a chord AB. Let line L be the perpendicular bisector of AB.",
                "formula": "Perpendicular Bisector Theorem: The locus of points equidistant from two points A and B is the perpendicular bisector of AB.",
                "substitution": "Test whether centre O is equidistant from A and B.",
                "calculation": "1. Points A and B lie on the circle with centre O.\n2. By definition of a circle, the distance from the centre to any point on the circumference is equal to the radius r.\n3. Therefore, OA = r and OB = r, which means OA = OB.\n4. Since point O is equidistant from endpoints A and B, by the Perpendicular Bisector Theorem, point O must lie on the perpendicular bisector of segment AB.\n5. Hence, the perpendicular bisector of any chord of a circle unconditionally passes through the centre O.",
                "finalAnswer": "Proved: Since OA = OB = r, the centre O is equidistant from A and B, so O must lie on the perpendicular bisector of chord AB.",
                "unit": "geometric proof",
                "has_diagram": True
            }
        ]
    }
