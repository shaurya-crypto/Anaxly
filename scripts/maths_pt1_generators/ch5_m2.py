"""
Chapter 5: I’m Up and Down, and Round and Round - Module 2
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_circle_geometry_svg

def get_m2():
    m2_svg = build_circle_geometry_svg(
        radius=90, center=(290, 200),
        points=[
            {"x": 290, "y": 200, "label": "Centre O"},
            {"x": 245, "y": 122, "label": "A"},
            {"x": 335, "y": 122, "label": "B"}
        ],
        triangles=[
            {"pts": [(290, 200), (245, 122), (335, 122)], "stroke": "#DC2626", "fill": "rgba(220,38,38,0.08)"}
        ],
        title="Equilateral Chord Subtension (60° Central Angle)",
        caption="When central angle is 60°, isosceles triangle OAB becomes equilateral with chord AB = radius = 12 cm"
    )

    return {
        "order_index": 2,
        "title": "Textbook Exercise Solver 1: Chords, Central Angles & Equilateral Subtensions (Exercises 5.2 & 5.6 Part 1 & Challenges)",
        "description": "Step-by-step solutions to Exercise 5.2 (Q1, Q2), Exercise 5.6 (Q1), and End-of-Chapter Questions 16, 17, and 19. Explore the isosceles chord-centre triangle, equal chords subtending equal central angles, equilateral triangle subtension (60° angle), the concentric midpoint locus, and regular hexagons inscribed in circles.",
        "subtopics": [
            "Proof of the Isosceles Chord-Centre Triangle: OA = OB = r",
            "SSS congruence theorem for chord triangles with equal base lengths",
            "Equilateral chord property: Central angle 60° implies chord length equals radius r = 12 cm",
            "Locus of midpoints of congruent chords: Concentric circle of radius d = sqrt(r^2 - (L/2)^2)",
            "Angle bisector property of congruent adjacent chords AB = AC",
            "Regular hexagon decomposition into six congruent equilateral triangles"
        ],
        "key_concepts": [
            "Chord-Centre Triangle Invariant: Any chord AB forms triangle OAB where OA = OB = r, so triangle OAB is unconditionally isosceles.",
            "Congruence Criterion: If chords AB = CD, then triangle OAB is congruent to triangle OCD by SSS (OA=OC=r, OB=OD=r, AB=CD).",
            "Angle Equality Theorem: Equal chords subtend equal angles at the centre: angle AOB = angle COD.",
            "Equilateral Special Case: If central angle is 60°, the base angles are (180 - 60)/2 = 60°, making triangle OAB equilateral with chord AB = r.",
            "Concentric Locus Theorem: All chords of length L lie at fixed distance d from the centre; their midpoints trace a concentric circle.",
            "Hexagonal Circumradius Equality: In a regular hexagon, the side length is exactly r and apothem is r * sqrt(3)/2."
        ],
        "success_criteria": "Students can prove chord triangle congruence, calculate chord lengths from central angles, identify concentric midpoint loci, and analyze inscribed regular polygons.",
        "chapter_notes": "Module 2 connects chord lengths to subtended central angles, deriving properties of regular hexagons and equilateral chord configurations.",
        "common_misconceptions": [
            {"misconception": "Believing doubling the central angle doubles the chord length", "clarification": "Chord length is L = 2r*sin(theta/2); it is non-linear and not directly proportional to the central angle."},
            {"misconception": "Assuming midpoints of equal chords form a polygon", "clarification": "Midpoints are equidistant from the centre and therefore trace a smooth continuous concentric circle."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through chord properties and central angles. Emphasize that radii OA = OB = r always create isosceles triangles.",
        "visual_lesson_plan": {
            "title": "Visualizing Chords and Central Angles",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Interactive circle with a 60° central angle showing the equilateral triangle formed by the chord and two radii.",
            "concept_visuals": [
                {
                    "concept_title": "Equilateral Subtension: 60° Central Angle",
                    "diagram_title": "Chord AB = Radius = 12 cm",
                    "interactive_math_formula": "L = 2r \\sin(30^\\circ) = 2(12)(0.5) = 12\\text{ cm}",
                    "mafs_graph_config": {
                        "domain": [-15, 15],
                        "range": [-15, 15],
                        "curves": [
                            {"fn": "sqrt(144 - x^2)", "color": "#2563EB", "label": "Circle r=12"},
                            {"fn": "-sqrt(144 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 0, "y": 12, "label": "A(0, 12)"},
                            {"x": 10.39, "y": 6, "label": "B(10.39, 6)"}
                        ]
                    },
                    "image_query": "circle 60 degree central angle chord length equilateral triangle",
                    "video_query": "why 60 degree chord equals radius of circle",
                    "what_to_explain": "Because OA = OB = 12 cm and angle AOB = 60°, base angles are 60°, making triangle OAB equilateral with AB = 12 cm."
                },
                {
                    "concept_title": "Isosceles Triangle Formed by Chord and Radii",
                    "diagram_title": "OA = OB = r with Base Angles Equal",
                    "interactive_math_formula": "OA = OB = r \\implies \\angle OAB = \\angle OBA",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Circle r=8"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Centre O"},
                            {"x": -6, "y": 5.29, "label": "A"},
                            {"x": 6, "y": 5.29, "label": "B"}
                        ]
                    },
                    "image_query": "isosceles triangle formed by chord and two radii of circle",
                    "video_query": "triangle formed by chord and centre of circle is isosceles",
                    "what_to_explain": "Any chord AB forms a triangle with the centre where two legs are radii OA and OB, making it isosceles."
                },
                {
                    "concept_title": "Concentric Locus of Midpoints of Equal Chords",
                    "diagram_title": "Circle of Radius d Traced by Midpoints",
                    "interactive_math_formula": "d = \\sqrt{r^2 - (L/2)^2} = \\text{constant}",
                    "mafs_graph_config": {
                        "domain": [-12, 12],
                        "range": [-12, 12],
                        "curves": [
                            {"fn": "sqrt(100 - x^2)", "color": "#2563EB", "label": "Outer Circle r=10"},
                            {"fn": "-sqrt(100 - x^2)", "color": "#2563EB", "label": ""},
                            {"fn": "sqrt(36 - x^2)", "color": "#DC2626", "label": "Midpoint Circle d=6"},
                            {"fn": "-sqrt(36 - x^2)", "color": "#DC2626", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O"},
                            {"x": 0, "y": 6, "label": "M1(0, 6)"},
                            {"x": 6, "y": 0, "label": "M2(6, 0)"}
                        ]
                    },
                    "image_query": "locus of midpoints of equal chords concentric circle",
                    "video_query": "locus of midpoints of chords of fixed length",
                    "what_to_explain": "Because every chord of fixed length L is at distance d from the centre, their midpoints form a concentric circle of radius d."
                },
                {
                    "concept_title": "Inscribed Regular Hexagon Geometry",
                    "diagram_title": "Six Equilateral Triangles with Side = r",
                    "interactive_math_formula": "s = r, \\quad d = r\\frac{\\sqrt{3}}{2}",
                    "mafs_graph_config": {
                        "domain": [-12, 12],
                        "range": [-12, 12],
                        "curves": [
                            {"fn": "sqrt(100 - x^2)", "color": "#2563EB", "label": "Circumcircle r=10"},
                            {"fn": "-sqrt(100 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 10, "y": 0, "label": "V1(10, 0)"},
                            {"x": 5, "y": 8.66, "label": "V2(5, 8.66)"},
                            {"x": -5, "y": 8.66, "label": "V3(-5, 8.66)"},
                            {"x": -10, "y": 0, "label": "V4(-10, 0)"},
                            {"x": -5, "y": -8.66, "label": "V5(-5, -8.66)"},
                            {"x": 5, "y": -8.66, "label": "V6(5, -8.66)"}
                        ]
                    },
                    "image_query": "regular hexagon inscribed in circle six equilateral triangles",
                    "video_query": "regular hexagon inscribed in a circle side length apothem",
                    "what_to_explain": "Each of the 6 sides subtends 360/6 = 60° at the centre, forming 6 equilateral triangles of side length r."
                },
                {
                    "concept_title": "Congruent Chords from Common Vertex: Angle Bisector",
                    "diagram_title": "Centre O Lies on Angle Bisector of BAC",
                    "interactive_math_formula": "\\Delta OAB \\cong \\Delta OAC \\implies \\angle OAB = \\angle OAC",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#DC2626", "label": "Angle Bisector AO"}
                        ],
                        "points": [
                            {"x": -8, "y": 0, "label": "Vertex A"},
                            {"x": 0, "y": 0, "label": "Centre O"},
                            {"x": 4, "y": 6, "label": "B"},
                            {"x": 4, "y": -6, "label": "C"}
                        ]
                    },
                    "image_query": "chords AB and AC congruent centre lies on angle bisector",
                    "video_query": "two equal chords from same point angle bisector passes through centre",
                    "what_to_explain": "Triangles OAB and OAC are congruent by SSS, so ray AO bisects angle BAC."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Chord Central Angle Relations",
                    "questions": [
                        {
                            "question": "If a chord subtends an angle of 60° at the centre of a circle of radius 15 cm, what is the length of the chord?",
                            "type": "short_answer",
                            "ideal_answer": "15 cm (the triangle formed by the chord and the centre is equilateral).",
                            "socratic_hint": "What are the base angles of an isosceles triangle with vertex angle 60°?"
                        },
                        {
                            "question": "What geometric figure is formed by the midpoints of all chords of length 8 cm in a circle of radius 5 cm?",
                            "type": "short_answer",
                            "ideal_answer": "A concentric circle of radius 3 cm (since d = sqrt(5^2 - 4^2) = 3 cm).",
                            "socratic_hint": "Calculate the perpendicular distance of each such chord from the centre."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 5.2 Q1: Show that the triangle formed by a chord and the centre of the circle is isosceles.",
                "given": "A circle with centre O and a chord AB.",
                "formula": "Definition of an isosceles triangle: A triangle with at least two sides of equal length.",
                "substitution": "Join OA and OB.",
                "calculation": "1. Points A and B lie on the circumference of the circle with centre O.\n2. By definition of a circle, the distance from centre O to any point on the circumference is equal to radius r.\n3. Therefore, segment OA = r and segment OB = r.\n4. In triangle OAB, side OA is equal in length to side OB (OA = OB = r).\n5. By definition, a triangle with two equal sides is an isosceles triangle.\n6. Hence, triangle OAB formed by chord AB and centre O is unconditionally isosceles.",
                "finalAnswer": "Proved: Since OA = OB = r (both are radii), triangle OAB is isosceles.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.2 Q2: Show that if two such isosceles triangles (occurring in the previous question) have equal base length, they are congruent to each other.",
                "given": "Two chords AB and CD of a circle with centre O, such that AB = CD (equal base lengths).",
                "formula": "SSS Congruence Criterion: If three sides of one triangle are equal to three sides of another triangle, the triangles are congruent.",
                "substitution": "Compare triangle OAB and triangle OCD.",
                "calculation": "1. In triangle OAB and triangle OCD:\n   - OA = OC = r (radii of the same circle)\n   - OB = OD = r (radii of the same circle)\n   - AB = CD (given equal chord lengths / bases)\n2. All three corresponding sides are equal.\n3. By the SSS (Side-Side-Side) congruence criterion, triangle OAB is congruent to triangle OCD (triangle OAB ~= triangle OCD).\n4. As a corollary (CPCTC), their corresponding central angles are equal: angle AOB = angle COD.",
                "finalAnswer": "Proved: Triangle OAB is congruent to triangle OCD by SSS congruence (radii OA=OC=r, OB=OD=r, and chords AB=CD).",
                "unit": "congruence proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 5.6 Q1: In a circle with centre O, the central angle AOB is 60°. If the radius of the circle is 12 cm, what is the length of the chord AB?",
                "given": "Radius r = 12 cm, central angle AOB = 60°.",
                "formula": "In triangle OAB, OA = OB = r. Base angles angle OAB = angle OBA = (180° - 60°) / 2.",
                "substitution": "Angle OAB = angle OBA = 120° / 2 = 60°.",
                "calculation": "1. In triangle OAB, OA = OB = 12 cm, so triangle OAB is isosceles.\n2. Sum of angles in triangle OAB = 180°.\n3. Angle OAB + angle OBA = 180° - angle AOB = 180° - 60° = 120°.\n4. Since base angles are equal: angle OAB = angle OBA = 120° / 2 = 60°.\n5. Since all three interior angles are 60°, triangle OAB is an equiangular (and therefore equilateral) triangle.\n6. In an equilateral triangle, all three sides are equal: AB = OA = OB = 12 cm.",
                "finalAnswer": "12 cm (Triangle OAB is equilateral, so chord AB = radius = 12 cm).",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q16: Consider all chords of a circle of a fixed length L. What is the shape formed by the midpoints of all these chords?",
                "given": "A circle of radius r with a family of all chords of fixed length L (where 0 < L <= 2r).",
                "formula": "Perpendicular distance from centre to midpoint M of chord of length L: d = sqrt(r^2 - (L/2)^2).",
                "substitution": "Distance OM = d is constant for all chords of length L.",
                "calculation": "1. Let AB be any chord of length L. Drop perpendicular OM from centre O to chord AB.\n2. By Theorem 5, M is the midpoint of AB, so AM = L/2.\n3. In right triangle OMA: OM^2 + AM^2 = OA^2 => d^2 + (L/2)^2 = r^2.\n4. Therefore, d = OM = sqrt(r^2 - (L/2)^2).\n5. Since both r and L are fixed constants, the distance d from centre O to midpoint M is constant for every chord of length L.\n6. The locus of all points M that remain at a fixed distance d from the fixed point O is a circle with centre O and radius d.\n7. This circle is concentric with the original circle.",
                "finalAnswer": "A concentric circle (a circle having the same centre O and radius d = sqrt(r^2 - L^2 / 4)).",
                "unit": "geometric locus",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q17: In a circle with centre O, chords AB and AC are congruent. Explain why this statement is true: 'The centre of the circle lies on the angle bisector of angle BAC'.",
                "given": "Chords AB and AC are congruent (AB = AC) in a circle with centre O.",
                "formula": "SSS congruence: Triangle OAB and triangle OAC have three pairs of equal sides.",
                "substitution": "Compare triangle OAB and triangle OAC.",
                "calculation": "1. In triangle OAB and triangle OAC:\n   - AB = AC (given)\n   - OA = OA (common side)\n   - OB = OC = r (radii of the same circle)\n2. Therefore, triangle OAB is congruent to triangle OAC by SSS congruence criterion.\n3. By Corresponding Parts of Congruent Triangles (CPCTC):\n   angle OAB = angle OAC.\n4. Since ray AO divides angle BAC into two equal halves (angle OAB = angle OAC), line AO is the angle bisector of angle BAC.\n5. Because line AO contains the centre O, the centre O lies on the angle bisector of angle BAC.",
                "finalAnswer": "Proved: Triangles OAB and OAC are congruent by SSS, so angle OAB = angle OAC (CPCTC), meaning line AO is the angle bisector of angle BAC.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q19: A regular hexagon is inscribed in a circle of radius r. Find the length of the sides of the hexagon and the distance of each side from the centre of the circle.",
                "given": "Regular hexagon inscribed in a circle of radius r.",
                "formula": "Central angle = 360° / 6 = 60°. Distance (apothem) d = r * cos(30°) = r * sqrt(3) / 2.",
                "substitution": "Each side forms an equilateral triangle with the centre.",
                "calculation": "1. A regular hexagon has 6 equal sides. The angle subtended by each side at the centre is 360° / 6 = 60°.\n2. For each side AB, OA = OB = r and angle AOB = 60°.\n3. As proved in Exercise 5.6 Q1, triangle OAB is equilateral, which means side length s = AB = r.\n4. To find the perpendicular distance d from centre O to side AB:\n   In right triangle OMA where M is midpoint of AB: AM = r / 2 and OA = r.\n5. OM^2 = OA^2 - AM^2 = r^2 - (r/2)^2 = r^2 - r^2/4 = (3/4)r^2.\n6. OM = sqrt(3)/2 * r.",
                "finalAnswer": "Side length = r; Distance from centre = (sqrt(3)/2) * r.",
                "unit": "algebraic lengths",
                "has_diagram": True
            }
        ]
    }
