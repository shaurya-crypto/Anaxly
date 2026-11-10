"""
Chapter 6: Measuring Space: Perimeter and Area - Module 5
Curriculum ID: 2ca7b10a-3fb9-484f-8116-30d7b586c526
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_circle_geometry_svg

def get_m5():
    m5_svg = build_circle_geometry_svg(
        radius=90, center=(290, 200),
        points=[
            {"x": 290, "y": 200, "label": "Centre O"},
            {"x": 245, "y": 122, "label": "A"},
            {"x": 335, "y": 122, "label": "B"}
        ],
        angles=[
            {"p1": (245, 122), "vertex": (290, 200), "p2": (335, 122), "label": "60° Sector", "color": "#2563EB"}
        ],
        title="Minor Segment: Sector minus Equilateral Triangle",
        caption="Area of minor segment = Area(Sector) - Area(Triangle) = r²*(pi/6 - sqrt(3)/4)"
    )

    return {
        "order_index": 5,
        "title": "Textbook Exercise Solver 4: Circle Sectors, Segments, Windshield Wipers & Quadrants (Exercise 6.3 Complete)",
        "description": "Comprehensive step-by-step solutions to Exercise 6.3 (Q1 to Q8) and End-of-Chapter Question 8. Master the sector area formula A = (theta/360)*pi*r^2, quadrant areas from circumference, clock minute hand sweep areas, minor and major segments from chord subtensions (90° and 60°), car dual-wiper sweep areas, the algebraic derivation of segment area A = pi*r^2*(1/6 - sqrt(3)/4), and the circumscribed equilateral triangle area ratio 3*sqrt(3)/(4*pi) approx 0.413.",
        "subtopics": [
            "Sector Area Formula: A = (theta / 360) * pi * r^2",
            "Quadrant Area from Circumference C: r = C / (2*pi) and Area = (1/4)*pi*r^2",
            "Clock kinematics: Minute hand sweeps 6° per minute (60° in 10 minutes)",
            "Minor Segment calculation: Area(Segment) = Area(Sector) - Area(Triangle)",
            "Major Segment calculation: Total Circle Area - Minor Segment Area",
            "Dual-blade non-overlapping windshield wiper sweep integration",
            "Rigorous algebraic proof: Minor segment of 60° chord = r^2*(pi/6 - sqrt(3)/4)",
            "Area ratio of inscribed equilateral triangle to circle = 3*sqrt(3)/(4*pi) approx 0.413"
        ],
        "key_concepts": [
            "Proportional Sector Law: A sector subtending angle theta occupies exactly theta/360 fraction of the circle's total area pi*r^2.",
            "Segment Area Decomposition: The area of a circular segment bounded by chord AB is Area(Sector OAB) - Area(Triangle OAB).",
            "Equilateral Triangle Area Invariant: When central angle is 60°, triangle OAB is equilateral with side r; its area is (sqrt(3)/4)*r^2.",
            "Inscribed Equilateral Side Theorem: In a circle of radius r, an inscribed equilateral triangle has side s = 2r*sin(60°) = r*sqrt(3).",
            "Inscribed Equilateral Ratio: Area(Triangle) / Area(Circle) = ((sqrt(3)/4)*(3r^2)) / (pi*r^2) = (3*sqrt(3)) / (4*pi) approx 0.413.",
            "Wiper Blade Coverage: Total cleaned area for n non-overlapping identical wipers is n * (theta/360) * pi * r^2."
        ],
        "success_criteria": "Students can calculate areas of sectors, quadrants, segments, and sweep paths, derive symbolic segment area formulas, and prove geometric area ratios.",
        "chapter_notes": "Module 5 covers circular area partitions and curvilinear applications in everyday engineering and geometry.",
        "common_misconceptions": [
            {"misconception": "Confusing a sector with a segment", "clarification": "A sector is bounded by two radii and an arc (pie slice); a segment is bounded by a chord and an arc (crust slice)."},
            {"misconception": "Thinking major segment area is just major sector area", "clarification": "Major segment = Total Circle Area - Minor Segment Area = Major Sector + Triangle Area."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Exercise 6.3. Emphasize the visual distinction between a sector and a segment on the digital chalkboard.",
        "visual_lesson_plan": {
            "title": "Visualizing Sectors, Segments and Inscribed Triangles",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Vector diagram of a 60° circular sector showing the shaded minor segment formed by subtracting the equilateral triangle.",
            "concept_visuals": [
                {
                    "concept_title": "Minor Segment: Sector minus Equilateral Triangle",
                    "diagram_title": "Area = r²*(pi/6 - sqrt(3)/4)",
                    "interactive_math_formula": "A_{\\text{segment}} = r^2\\left(\\frac{\\pi}{6} - \\frac{\\sqrt{3}}{4}\\right)",
                    "mafs_graph_config": {
                        "domain": [-15, 15],
                        "range": [-5, 18],
                        "curves": [
                            {"fn": "sqrt(max(0, 144 - x^2))", "color": "#2563EB", "label": "Arc r=12"}
                        ],
                        "lines": [
                            {"slope": 1.732, "intercept": 0, "color": "#0F172A", "label": "Radius 1 (60°)"},
                            {"slope": 0, "intercept": 0, "color": "#0F172A", "label": "Radius 2 (0°)"},
                            {"slope": -0.577, "intercept": 10.39, "color": "#DC2626", "label": "Chord"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O"},
                            {"x": 12, "y": 0, "label": "B"},
                            {"x": 6, "y": 10.39, "label": "A"}
                        ]
                    },
                    "image_query": "area of minor segment of circle sector minus triangle formula diagram",
                    "video_query": "how to find area of segment of a circle class 9 maths",
                    "what_to_explain": "Subtracting the area of equilateral triangle OAB from sector OAB leaves the curved minor segment."
                },
                {
                    "concept_title": "Inscribed Equilateral Triangle Area Ratio: 0.413",
                    "diagram_title": "Ratio = 3*sqrt(3) / (4*pi) approx 41.3% Coverage",
                    "interactive_math_formula": "\\frac{A_{\\text{triangle}}}{A_{\\text{circle}}} = \\frac{3\\sqrt{3}}{4\\pi} \\approx 0.413",
                    "mafs_graph_config": {
                        "domain": [-12, 12],
                        "range": [-12, 12],
                        "curves": [
                            {"fn": "sqrt(100 - x^2)", "color": "#2563EB", "label": "Circumcircle r=10"},
                            {"fn": "-sqrt(100 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 10, "label": "Vertex A(0, 10)"},
                            {"x": -8.66, "y": -5, "label": "Vertex B(-8.66, -5)"},
                            {"x": 8.66, "y": -5, "label": "Vertex C(8.66, -5)"},
                            {"x": 0, "y": 0, "label": "Centroid O"}
                        ]
                    },
                    "image_query": "equilateral triangle inscribed in circle area ratio 3 root 3 over 4 pi",
                    "video_query": "ratio of area of inscribed equilateral triangle to circle",
                    "what_to_explain": "The inscribed equilateral triangle occupies approximately 41.3% of the circle's area, leaving 58.7% in the three outer segments."
                },
                {
                    "concept_title": "Clock Minute Hand Sweep: 10 Minutes = 60°",
                    "diagram_title": "Sector Area for r = 7 cm: 77/3 cm²",
                    "interactive_math_formula": "A = \\frac{60^\\circ}{360^\\circ}\\pi(7^2) = \\frac{1}{6}\\left(\\frac{22}{7}\\right)(49) = \\frac{77}{3}\\text{ cm}^2",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(49 - x^2)", "color": "#64748B", "label": "Clock Face r=7"},
                            {"fn": "-sqrt(49 - x^2)", "color": "#64748B", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Clock Centre"},
                            {"x": 0, "y": 7, "label": "12:00 Position"},
                            {"x": 6.06, "y": 3.5, "label": "10 min: 2:00 Position (60°)"}
                        ]
                    },
                    "image_query": "area swept by minute hand in 10 minutes circle sector math",
                    "video_query": "area swept by minute hand of clock in 10 minutes",
                    "what_to_explain": "Each minute the minute hand moves 360/60 = 6°. In 10 minutes it moves 60°, sweeping 1/6 of the clock face area."
                },
                {
                    "concept_title": "Dual Windshield Wipers: 2 x 120° Sweep",
                    "diagram_title": "Total Area = 2 * (120/360) * pi * (28)² = 1642.67 cm²",
                    "interactive_math_formula": "A_{\\text{total}} = 2 \\times \\frac{1}{3}\\pi(28)^2 = \\frac{11498}{7} \\approx 1642.67\\text{ cm}^2",
                    "mafs_graph_config": {
                        "domain": [-35, 35],
                        "range": [0, 35],
                        "points": [
                            {"x": -15, "y": 0, "label": "Pivot 1"},
                            {"x": 15, "y": 0, "label": "Pivot 2"}
                        ]
                    },
                    "image_query": "car windshield wipers sector area sweep angle 120 degrees",
                    "video_query": "car has two wipers each sweeps through 120 degrees find area",
                    "what_to_explain": "Two non-overlapping wipers sweep two separate 120° sectors, cleaning 2/3 of a full circle of radius 28 cm."
                },
                {
                    "concept_title": "Sector Area Proportionality: A(theta)",
                    "diagram_title": "Linear Variation: Area vs Angle",
                    "interactive_math_formula": "A = \\left(\\frac{\\pi r^2}{360^\\circ}\\right) \\theta",
                    "mafs_graph_config": {
                        "domain": [0, 360],
                        "range": [0, 160],
                        "curves": [
                            {"fn": "(154/360)*x", "color": "#2563EB", "label": "A(theta) for r=7"}
                        ],
                        "points": [
                            {"x": 90, "y": 38.5, "label": "Quadrant (90°): 38.5 cm²"},
                            {"x": 180, "y": 77, "label": "Semicircle (180°): 77 cm²"},
                            {"x": 360, "y": 154, "label": "Full Circle (360°): 154 cm²"}
                        ]
                    },
                    "image_query": "sector area as function of angle linear relationship graph",
                    "video_query": "how to find area of sector of circle formula explained",
                    "what_to_explain": "Sector area grows linearly with angle theta; at 90° it is 1/4 the circle, at 180° it is 1/2 the circle, and at 360° it is the full circle."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Sector and Segment Areas",
                    "questions": [
                        {
                            "question": "What is the area of a sector of a circle of radius 7 cm with sector angle 60° (using pi = 22/7)?",
                            "type": "short_answer",
                            "ideal_answer": "77/3 cm^2 approx 25.67 cm^2 (A = (60/360) * (22/7) * 49 = 77/3).",
                            "socratic_hint": "Use A = (theta / 360) * pi * r^2."
                        },
                        {
                            "question": "How do you find the area of a minor segment bounded by a chord?",
                            "type": "short_answer",
                            "ideal_answer": "Subtract the area of the corresponding triangle from the area of the sector: Area(Segment) = Area(Sector) - Area(Triangle).",
                            "socratic_hint": "Look at the pie slice and subtract the triangle formed by the two radii and the chord."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 6.3 Q1: Find the area of a sector of a circle with radius 7 cm if the angle of the sector is 60°.",
                "given": "Radius r = 7 cm, sector angle theta = 60°.",
                "formula": "Area = (theta / 360) * pi * r^2.",
                "substitution": "Area = (60 / 360) * (22/7) * 7^2.",
                "calculation": "1. 60 / 360 = 1/6.\n2. (22/7) * 49 = 22 * 7 = 154 cm^2.\n3. Area = (1/6) * 154 = 154 / 6 = 77 / 3 cm^2.\n4. Numerical value: 77 / 3 = 25.67 cm^2.",
                "finalAnswer": "77/3 cm^2 (approx 25.67 cm^2)",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.3 Q2: Find the area of a quadrant of a circle whose circumference is 44 cm.",
                "given": "Circumference C = 44 cm. A quadrant has sector angle theta = 90°.",
                "formula": "r = C / (2*pi). Area of quadrant = (1/4) * pi * r^2.",
                "substitution": "r = 44 / (2 * 22/7) = 7 cm. Area = (1/4) * (22/7) * 7^2.",
                "calculation": "1. r = 7 cm.\n2. Full circle area = pi * r^2 = (22/7) * 49 = 154 cm^2.\n3. Quadrant area = 154 / 4 = 77 / 2 = 38.5 cm^2.",
                "finalAnswer": "38.5 cm^2 (or 77/2 cm^2)",
                "unit": "cm^2",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.3 Q3: The length of the minute hand of a clock is 7 cm. Find the area swept by the minute hand in 10 minutes.",
                "given": "Length of minute hand r = 7 cm. Time elapsed = 10 minutes.",
                "formula": "Minute hand completes 360° in 60 minutes => Rate = 360° / 60 = 6° per minute. Angle swept theta = 10 * 6° = 60°. Area = (theta / 360) * pi * r^2.",
                "substitution": "Area = (60 / 360) * (22/7) * 7^2.",
                "calculation": "1. Angle swept in 10 minutes: theta = 60°.\n2. Area = (1/6) * (22/7) * 49 = 154 / 6 = 77 / 3 cm^2.\n3. Numerical value: 25.67 cm^2.",
                "finalAnswer": "77/3 cm^2 (approx 25.67 cm^2)",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.3 Q4: A chord of a circle of radius 10 cm subtends 90° at the centre. Find the area of: (i) minor sector (subtends 90°), and (ii) major sector (subtends 270°). (Use pi = 3.14)",
                "given": "Radius r = 10 cm. Minor angle theta1 = 90°, Major angle theta2 = 360° - 90° = 270°.",
                "formula": "Area = (theta / 360) * pi * r^2.",
                "substitution": "Full circle area = 3.14 * 10^2 = 314 cm^2.",
                "calculation": "1. Part (i): Minor sector area (90°):\n   Area = (90 / 360) * 314 = (1/4) * 314 = 78.5 cm^2.\n2. Part (ii): Major sector area (270°):\n   Area = (270 / 360) * 314 = (3/4) * 314 = 235.5 cm^2.\n   (Verification: 78.5 + 235.5 = 314 cm^2).",
                "finalAnswer": "(i) Minor sector = 78.5 cm^2; (ii) Major sector = 235.5 cm^2",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.3 Q5: A chord of a circle of radius 15 cm subtends an angle of 60° at the centre. Find the areas of the corresponding minor and major segments. (Use pi = 3.14, sqrt(3) = 1.73)",
                "given": "Radius r = 15 cm, central angle theta = 60°.",
                "formula": "Area(Minor Sector) = (60/360)*pi*r^2. Area(Triangle OAB) = (sqrt(3)/4)*r^2. Area(Minor Segment) = Sector - Triangle. Area(Major Segment) = Total Area - Minor Segment.",
                "substitution": "r^2 = 225. pi = 3.14, sqrt(3) = 1.73.",
                "calculation": "1. Area of minor sector (60°):\n   A_sector = (1/6) * 3.14 * 225 = 706.5 / 6 = 117.75 cm^2.\n2. Area of equilateral triangle OAB:\n   A_tri = (sqrt(3)/4) * 225 = (1.73 / 4) * 225 = 0.4325 * 225 = 97.3125 cm^2 approx 97.31 cm^2.\n3. Area of minor segment:\n   A_minor_seg = 117.75 - 97.31 = 20.44 cm^2.\n4. Total area of circle:\n   A_circle = pi * r^2 = 3.14 * 225 = 706.5 cm^2.\n5. Area of major segment:\n   A_major_seg = A_circle - A_minor_seg = 706.5 - 20.44 = 686.06 cm^2.",
                "finalAnswer": "Minor segment area = 20.44 cm^2; Major segment area = 686.06 cm^2",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.3 Q6: A car has two wipers which do not overlap. Each blade has length 28 cm and sweeps through an angle of 120°. Find the total area cleaned at each sweep of the blades.",
                "given": "Two identical wipers. Blade length r = 28 cm, sweep angle theta = 120°.",
                "formula": "Total cleaned area = 2 * [(theta / 360) * pi * r^2].",
                "substitution": "Total Area = 2 * [(120 / 360) * (22/7) * 28^2].",
                "calculation": "1. 120 / 360 = 1/3.\n2. Area of one sweep = (1/3) * (22/7) * 784.\n   784 / 7 = 112.\n   22 * 112 = 2464.\n   Area of one wiper = 2464 / 3 cm^2.\n3. For two wipers: Total Area = 2 * (2464 / 3) = 4928 / 3 cm^2.\n4. Numerical value: 4928 / 3 = 1642.67 cm^2.",
                "finalAnswer": "4928/3 cm^2 (approx 1642.67 cm^2)",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.3 Q7: A chord of a circle of radius r subtends an angle of 60° at the centre. Show that the area of the corresponding minor segment is equal to r^2 * (pi/6 - sqrt(3)/4).",
                "given": "Circle of radius r, central angle theta = 60°.",
                "formula": "Area(Minor Segment) = Area(Sector) - Area(Triangle).",
                "substitution": "theta = 60° in sector formula; triangle is equilateral with side r.",
                "calculation": "1. Area of sector with central angle 60°:\n   A_sector = (60° / 360°) * pi * r^2 = (1/6) * pi * r^2.\n2. In triangle OAB, OA = OB = r and angle AOB = 60°. Therefore, triangle OAB is equilateral with side length r.\n   Area of an equilateral triangle of side r is:\n   A_triangle = (sqrt(3)/4) * r^2.\n3. Area of minor segment = A_sector - A_triangle:\n   Area = (1/6) * pi * r^2 - (sqrt(3)/4) * r^2.\n4. Factor out r^2:\n   Area = r^2 * (pi/6 - sqrt(3)/4).",
                "finalAnswer": "Proved: Area of minor segment = r^2 * (pi/6 - sqrt(3)/4).",
                "unit": "algebraic proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.3 Q8: An equilateral triangle is inscribed in a circle of radius r. Show that the ratio of the area of the triangle to the area of the circle is (3*sqrt(3)) / (4*pi) approx 0.413.",
                "given": "Equilateral triangle inscribed in a circle of radius r.",
                "formula": "Side of inscribed equilateral triangle s = 2r*sin(60°) = r*sqrt(3). Area of triangle = (sqrt(3)/4)*s^2. Area of circle = pi*r^2.",
                "substitution": "s = r*sqrt(3). s^2 = 3r^2.",
                "calculation": "1. Side length of inscribed equilateral triangle:\n   By sine rule: s / sin(60°) = 2r => s = 2r * (sqrt(3)/2) = r*sqrt(3).\n2. Area of equilateral triangle:\n   A_triangle = (sqrt(3)/4) * s^2 = (sqrt(3)/4) * (r*sqrt(3))^2 = (sqrt(3)/4) * 3r^2 = (3*sqrt(3)/4) * r^2.\n3. Area of circumscribed circle:\n   A_circle = pi * r^2.\n4. Ratio of areas:\n   Ratio = A_triangle / A_circle = [(3*sqrt(3)/4) * r^2] / [pi * r^2] = (3*sqrt(3)) / (4*pi).\n5. Numerical evaluation:\n   3 * sqrt(3) = 3 * 1.73205 = 5.19615.\n   4 * pi = 4 * 3.14159 = 12.56637.\n   Ratio = 5.19615 / 12.56637 = 0.4135 approx 0.413.",
                "finalAnswer": "Ratio = (3*sqrt(3)) / (4*pi) approx 0.413 (Proved).",
                "unit": "ratio",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q8: Find the area of a quadrant of a circle whose circumference is 66 cm.",
                "given": "Circumference C = 66 cm. Quadrant angle theta = 90°.",
                "formula": "r = C / (2*pi). Area = (1/4) * pi * r^2.",
                "substitution": "r = 66 / (2 * 22/7) = (66 * 7) / 44 = (3 * 7) / 2 = 21/2 = 10.5 cm.",
                "calculation": "1. Radius r = 10.5 cm.\n2. Area of circle = (22/7) * (21/2)^2 = (22/7) * (441/4) = (22 * 63) / 4 = 1386 / 4 = 346.5 cm^2.\n3. Quadrant area = (1/4) * 346.5 = 346.5 / 4 = 86.625 cm^2 (or 693/8 cm^2).",
                "finalAnswer": "86.625 cm^2 (or 693/8 cm^2)",
                "unit": "cm^2",
                "has_diagram": False
            }
        ]
    }
