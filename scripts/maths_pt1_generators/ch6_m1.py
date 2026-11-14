"""
Chapter 6: Measuring Space: Perimeter and Area - Module 1
Curriculum ID: 2ca7b10a-3fb9-484f-8116-30d7b586c526
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_running_track_svg

def get_m1():
    m1_svg = build_running_track_svg(
        title="400 m Standard Athletics Track & Stagger Invariant",
        caption="Two straight stretches of 84.39 m and two semicircular bends requiring 2*pi*w = 7.67 m lane stagger"
    )

    return {
        "order_index": 1,
        "title": "Linear & Circular Perimeters: Circumference, Arc Length & Athletics Track Stagger (Exercise 6.1 Set 1 & Wheel Revolutions)",
        "description": "Comprehensive step-by-step solutions to in-text examples, Exercise 6.1 (Q1 to Q4), and End-of-Chapter Questions 7 and 9. Master circumference calculations C = 2*pi*r, arc lengths L = (theta/360)*2*pi*r, perimeter of sectors, wheel rotation distance, and 400 m relay track stagger geometry.",
        "subtopics": [
            "Geometric definition of perimeter and the universal circumference ratio C / D = pi",
            "Radius recovery from circumference: r = C / (2*pi)",
            "Circular arc length formula: L = (theta / 360) * 2*pi*r",
            "Complete boundary perimeter of a circular sector: P = L + 2r",
            "Wheel kinematics: Distance = Revolutions * Circumference and revolutions per kilometre",
            "Track stagger geometry: Why outer lane runners start ahead by 2*pi*w"
        ],
        "key_concepts": [
            "Pi Invariant: The ratio of the circumference of any circle to its diameter is the constant irrational number pi approx 22/7 approx 3.14159.",
            "Arc Length Invariant: An arc subtending angle theta at the centre occupies theta/360 fraction of the total circumference.",
            "Sector Perimeter Structure: A circular sector is bounded by one curved arc and two straight radii: P = (theta/360)*2*pi*r + 2r.",
            "Wheel Rolling Law: In one complete rotation without slipping, a wheel translates horizontally by exactly its circumference C = 2*pi*r.",
            "Track Stagger Theorem: For two semicircular bends of radius r and r + w, the difference in track perimeter is 2*pi*(r + w) - 2*pi*r = 2*pi*w."
        ],
        "success_criteria": "Students can calculate circle circumferences and arc lengths, compute perimeters of sectors, calculate vehicle travel from wheel dimensions, and explain race track stagger geometry.",
        "chapter_notes": "Module 1 builds metric understanding of 1D boundary lengths across linear and circular geometry, connecting mathematical ratios to athletic tracks.",
        "common_misconceptions": [
            {"misconception": "Forgetting the two straight radii when finding sector perimeter", "clarification": "The perimeter of a sector includes the curved arc PLUS the two straight bounding edges: P = L + 2r."},
            {"misconception": "Thinking track stagger depends on the radius of the track", "clarification": "The stagger 2*pi*w depends solely on the lane width w, completely independent of the bend radius r."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Chapter 6 Module 1. Draw the 400m track and circular sectors on the digital chalkboard, emphasizing boundary tracing.",
        "visual_lesson_plan": {
            "title": "Visualizing Circular Perimeters and Athletics Tracks",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Vector athletics track diagram with lane staggers marked alongside a circular sector diagram.",
            "concept_visuals": [
                {
                    "concept_title": "Athletics Track Lane Stagger: 2*pi*w",
                    "diagram_title": "Concentric Semicircular Bends with Width w = 1.22 m",
                    "interactive_math_formula": "\\Delta C = 2\\pi(r + w) - 2\\pi r = 2\\pi w \\approx 7.67\\text{ m}",
                    "mafs_graph_config": {
                        "domain": [-15, 15],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Lane 1 (r=8)"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""},
                            {"fn": "sqrt(100 - x^2)", "color": "#DC2626", "label": "Lane 2 (r=10)"},
                            {"fn": "-sqrt(100 - x^2)", "color": "#DC2626", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 8, "label": "Lane 1 Start"},
                            {"x": 0, "y": 10, "label": "Lane 2 Staggered Start (+7.67m)"}
                        ]
                    },
                    "image_query": "400m running track stagger start geometry diagram lanes",
                    "video_query": "how to calculate running track curve stagger math",
                    "what_to_explain": "Running on Lane 2 adds 2*pi*w extra distance on the bends; to ensure equal race distance, Lane 2 starts 2*pi*w ahead."
                },
                {
                    "concept_title": "Wheel Kinematics: Distance per Revolution",
                    "diagram_title": "Rolling Wheel: Translation d = 2*pi*r",
                    "interactive_math_formula": "d = 2\\pi r \\times N",
                    "mafs_graph_config": {
                        "domain": [0, 20],
                        "range": [-2, 6],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Ground Line"}
                        ],
                        "points": [
                            {"x": 0, "y": 2.8, "label": "Start: x = 0"},
                            {"x": 17.6, "y": 2.8, "label": "1 Turn: x = 1.76 m (r=28cm)"}
                        ]
                    },
                    "image_query": "rolling wheel circumference linear distance translation diagram",
                    "video_query": "distance travelled by wheel in one revolution formula",
                    "what_to_explain": "In one rotation, every point on the circumference contacts the ground once, translating the hub forward by 2*pi*r."
                },
                {
                    "concept_title": "Sector Perimeter: Arc + Two Radii",
                    "diagram_title": "P = (75/360)*2*pi*(14) + 2(14) = 46.33 cm",
                    "interactive_math_formula": "P = \\frac{\\theta}{360^\\circ}(2\\pi r) + 2r",
                    "mafs_graph_config": {
                        "domain": [0, 16],
                        "range": [0, 16],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 14, "y": 0, "label": "Radius 1 (14 cm)"},
                            {"x": 3.62, "y": 13.52, "label": "Radius 2 (75°)"}
                        ]
                    },
                    "image_query": "perimeter of sector of circle arc length plus two radii",
                    "video_query": "how to find perimeter of a sector of a circle",
                    "what_to_explain": "The complete boundary perimeter includes both straight radial legs of 14 cm plus the 18.33 cm circular arc."
                },
                {
                    "concept_title": "Linear Ratio: Circumference vs Diameter",
                    "diagram_title": "C = pi * D (Constant Slope pi = 3.14)",
                    "interactive_math_formula": "C = \\pi D",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 32],
                        "curves": [
                            {"fn": "3.14159*x", "color": "#2563EB", "label": "C = pi * D"}
                        ],
                        "points": [
                            {"x": 1, "y": 3.14, "label": "D=1, C=3.14"},
                            {"x": 7, "y": 22, "label": "D=7, C=22"},
                            {"x": 10, "y": 31.42, "label": "D=10, C=31.42"}
                        ]
                    },
                    "image_query": "circumference vs diameter linear graph slope pi",
                    "video_query": "why pi is ratio of circumference to diameter",
                    "what_to_explain": "Circumference is strictly proportional to diameter; the slope of the line is the universal constant pi."
                },
                {
                    "concept_title": "Arc Length Proportion: L(theta)",
                    "diagram_title": "Fraction of Circumference: 60° (1/6) vs 120° (1/3)",
                    "interactive_math_formula": "L = 2\\pi r \\left(\\frac{\\theta}{360^\\circ}\\right)",
                    "mafs_graph_config": {
                        "domain": [0, 360],
                        "range": [0, 45],
                        "curves": [
                            {"fn": "(44/360)*x", "color": "#2563EB", "label": "L(theta) for r=7"}
                        ],
                        "points": [
                            {"x": 60, "y": 7.33, "label": "60°: L = 7.33 cm"},
                            {"x": 90, "y": 11, "label": "90°: L = 11 cm"},
                            {"x": 180, "y": 22, "label": "180°: L = 22 cm"},
                            {"x": 360, "y": 44, "label": "360°: Full C = 44 cm"}
                        ]
                    },
                    "image_query": "arc length as function of central angle degrees graph",
                    "video_query": "how to calculate arc length of a circle given angle",
                    "what_to_explain": "As central angle theta increases linearly, arc length scales proportionally as a fraction of the total circumference."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Circumference and Arc Length",
                    "questions": [
                        {
                            "question": "What is the perimeter of a circle whose radius is 7 cm (using pi = 22/7)?",
                            "type": "short_answer",
                            "ideal_answer": "44 cm (C = 2 * (22/7) * 7 = 44 cm).",
                            "socratic_hint": "Use C = 2 * pi * r."
                        },
                        {
                            "question": "Why must runners in outer lanes on a circular track start ahead of the runner in the inner lane?",
                            "type": "short_answer",
                            "ideal_answer": "Because the outer lane has a larger radius and therefore a longer circumference (by 2*pi*w per full lap); the forward stagger compensates for this extra curve distance.",
                            "socratic_hint": "Compare the perimeter of a circle of radius r with a circle of radius r + w."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Textbook Example 1: In a standard 400 m athletics track with two straight stretches and two semicircular bends, calculate the stagger needed for a runner in Lane 2 if lane width is 1.22 m.",
                "given": "Lane width w = 1.22 m. Both runners complete two semicircular bends (one full circle).",
                "formula": "Difference in bend perimeter: Delta C = 2*pi*(r + w) - 2*pi*r = 2*pi*w.",
                "substitution": "Delta C = 2 * (22/7) * 1.22.",
                "calculation": "1. The two straight stretches are identical in length for all lanes (84.39 m each).\n2. The two semicircular bends together form a complete circle of circumference 2*pi*r for Lane 1, and 2*pi*(r + w) for Lane 2.\n3. Difference in total running distance = 2*pi*(r + w) - 2*pi*r = 2*pi*w.\n4. Delta C = 2 * 3.14159 * 1.22 = 7.665 m approx 7.67 m.\n5. Therefore, the runner in Lane 2 must start 7.67 metres ahead of Lane 1.",
                "finalAnswer": "7.67 m (Stagger = 2*pi*w = 2 * 3.1416 * 1.22 m).",
                "unit": "metres",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q1: The perimeter of a circle is 44 cm. What is its radius? (Use pi = 22/7)",
                "given": "Circumference C = 44 cm.",
                "formula": "C = 2*pi*r => r = C / (2*pi).",
                "substitution": "r = 44 / (2 * 22/7).",
                "calculation": "1. 2 * 22/7 = 44/7.\n2. r = 44 / (44/7) = 44 * (7/44) = 7 cm.",
                "finalAnswer": "7 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.1 Q2 (i): Calculate, correct to 3 significant figures, the circumference of a circle with radius 7 cm.",
                "given": "Radius r = 7 cm.",
                "formula": "C = 2*pi*r.",
                "substitution": "C = 2 * (22/7) * 7.",
                "calculation": "1. Cancel 7: C = 2 * 22 = 44 cm.\n2. Correct to 3 significant figures: 44.0 cm.",
                "finalAnswer": "44.0 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.1 Q2 (ii): Calculate, correct to 3 significant figures, the circumference of a circle with radius 10 cm.",
                "given": "Radius r = 10 cm.",
                "formula": "C = 2*pi*r.",
                "substitution": "C = 2 * 3.14159 * 10.",
                "calculation": "1. 2 * 10 = 20.\n2. 20 * 3.14159 = 62.8318 cm.\n3. Rounding to 3 significant figures: 62.8 cm.",
                "finalAnswer": "62.8 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.1 Q2 (iii): Calculate, correct to 3 significant figures, the circumference of a circle with radius 12 cm.",
                "given": "Radius r = 12 cm.",
                "formula": "C = 2*pi*r.",
                "substitution": "C = 2 * 3.14159 * 12.",
                "calculation": "1. 2 * 12 = 24.\n2. 24 * 3.14159 = 75.398 cm.\n3. Rounding to 3 significant figures: 75.4 cm.",
                "finalAnswer": "75.4 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.1 Q3 (i): Calculate the length of the arc of a circle if the radius is 3.5 cm and the angle at the centre is 60°.",
                "given": "Radius r = 3.5 cm = 7/2 cm, angle theta = 60°.",
                "formula": "L = (theta / 360) * 2*pi*r.",
                "substitution": "L = (60 / 360) * 2 * (22/7) * (7/2).",
                "calculation": "1. 60 / 360 = 1/6.\n2. 2 * (22/7) * (7/2) = 22 cm.\n3. L = (1/6) * 22 = 22/6 = 11/3 = 3.67 cm.",
                "finalAnswer": "11/3 cm (approx 3.67 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q3 (ii): Calculate the length of the arc of a circle if the radius is 6.3 m and the angle at the centre is 120°.",
                "given": "Radius r = 6.3 m = 63/10 m, angle theta = 120°.",
                "formula": "L = (theta / 360) * 2*pi*r.",
                "substitution": "L = (120 / 360) * 2 * (22/7) * (63/10).",
                "calculation": "1. 120 / 360 = 1/3.\n2. 63 / 7 = 9.\n3. 2 * 22 * 9 = 44 * 9 = 396.\n4. 396 / 10 = 39.6 m.\n5. L = (1/3) * 39.6 = 13.2 m.",
                "finalAnswer": "13.2 m",
                "unit": "m",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.1 Q4: Find the perimeter of a sector of a circle of radius 14 cm and sector angle 75°.",
                "given": "Radius r = 14 cm, sector angle theta = 75°.",
                "formula": "Perimeter P = Arc Length + 2*Radius = (theta / 360) * 2*pi*r + 2r.",
                "substitution": "L = (75 / 360) * 2 * (22/7) * 14; P = L + 2(14).",
                "calculation": "1. Simplify fraction: 75 / 360 = 5 / 24.\n2. 2 * (22/7) * 14 = 2 * 22 * 2 = 88 cm.\n3. L = (5 / 24) * 88 = (5 * 11) / 3 = 55 / 3 = 18.33 cm.\n4. P = L + 2r = 55/3 + 28 = 55/3 + 84/3 = 139/3 cm approx 46.33 cm.",
                "finalAnswer": "139/3 cm (approx 46.33 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q7: If the wheel of a bicycle has a diameter of 60 cm, find how far a cyclist will have travelled after the wheel has rotated 100 times.",
                "given": "Diameter D = 60 cm = 0.6 m, number of rotations N = 100.",
                "formula": "Distance d = N * Circumference = N * (pi * D).",
                "substitution": "d = 100 * (22/7) * 0.6.",
                "calculation": "1. Circumference C = pi * D = (22/7) * 0.6 = 13.2 / 7 = 1.8857 m.\n2. Distance for 100 turns: d = 100 * 1.8857 = 188.57 m.\n3. In cm: 100 * (22/7 * 60) = 132000 / 7 = 18857.14 cm = 188.57 m.",
                "finalAnswer": "188.57 m (or 1320/7 m)",
                "unit": "m",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q9: The wheel of a car has an outer radius of 28 cm. Calculate how far the car travels after one complete turn, and how many times the wheel turns during a journey of 1 km.",
                "given": "Radius r = 28 cm = 0.28 m. Total journey = 1 km = 1000 m.",
                "formula": "Distance per turn C = 2*pi*r. Number of turns N = Total Distance / C.",
                "substitution": "C = 2 * (22/7) * 28; N = 100000 cm / C.",
                "calculation": "1. Distance in 1 turn: C = 2 * (22/7) * 28 = 2 * 22 * 4 = 176 cm = 1.76 m.\n2. Total journey = 1000 m = 100,000 cm.\n3. Number of turns: N = 100000 / 176 = 12500 / 22 = 6250 / 11 approx 568.18 turns.\n4. The wheel turns approximately 568 times.",
                "finalAnswer": "Distance in 1 turn = 1.76 m; Number of turns in 1 km = 6250/11 approx 568 turns.",
                "unit": "m and turns",
                "has_diagram": True
            }
        ]
    }
