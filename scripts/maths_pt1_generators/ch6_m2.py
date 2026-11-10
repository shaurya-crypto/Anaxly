"""
Chapter 6: Measuring Space: Perimeter and Area - Module 2
Curriculum ID: 2ca7b10a-3fb9-484f-8116-30d7b586c526
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m2():
    m2_svg = build_cartesian_svg(
        domain=(-50, 50), range_y=(-35, 35),
        points=[
            {"x": -40, "y": 30, "label": "Top-Left", "color": "#0F172A"},
            {"x": 40, "y": 30, "label": "Top-Right", "color": "#0F172A"},
            {"x": -40, "y": -30, "label": "Bottom-Left", "color": "#0F172A"},
            {"x": 40, "y": -30, "label": "Bottom-Right", "color": "#0F172A"}
        ],
        lines=[
            {"p1": (-40, 30), "p2": (40, 30), "color": "#2563EB", "stroke_width": 3, "label": "Straight L = 80 m"},
            {"p1": (-40, -30), "p2": (40, -30), "color": "#2563EB", "stroke_width": 3, "label": "Straight L = 80 m"}
        ],
        title="Composite Boundary Tracing: Capsule Track",
        caption="External perimeter equals two straights (2 * 80 = 160 m) plus two semicircles (2 * pi * 30 = 188.57 m) = 348.57 m"
    )

    return {
        "order_index": 2,
        "title": "Textbook Exercise Solver 1: Composite Boundary Perimeters & Curvilinear Partitions (Exercise 6.1 Q5 Complete)",
        "description": "Comprehensive step-by-step solutions to all 9 composite figures in Exercise 6.1 Question 5 (Fig 6.14i through 6.14ix). Master boundary tracing of compound planar figures combining straight line segments with circular arcs, semicircles, and quarter-circles.",
        "subtopics": [
            "The Boundary Invariant: Identifying strictly external edges while disregarding interior dividing segments",
            "Semicircular boundary arc length: L = pi * r = pi * D / 2",
            "Quarter-circular corner arc length: L = (pi * r) / 2",
            "Three-quarter circular reflex boundary: L = (3/2) * pi * r",
            "Step-by-step arithmetic evaluation for Fig 6.14i through 6.14ix"
        ],
        "key_concepts": [
            "External Boundary Rule: Perimeter is solely the sum of edges that separate the interior of the shape from the outside world.",
            "Capsule Boundary Formula: Perimeter = 2 * (Straight Length) + 2 * (pi * r) = 2L + 2*pi*r.",
            "Indented Semicircle Invariant: Cutting a semicircular indentation into a side replaces a straight segment of length D with an arc of length (pi * D)/2, strictly increasing perimeter by D*(pi/2 - 1).",
            "Serpentine S-Curve Invariant: Alternating semicircles on segments of equal length d have total length n * (pi * d / 2).",
            "Quarter-Circle Corner Truncation: Replacing a corner of a square of side r with a quarter arc of radius r reduces perimeter by 2r - (pi*r/2) = r*(2 - pi/2)."
        ],
        "success_criteria": "Students can decompose any irregular curvilinear boundary into linear and circular segments and calculate exact and decimal perimeters without error.",
        "chapter_notes": "Exercise 6.1 Q5 contains 9 distinct geometrical figures testing the student's mastery of boundary integration.",
        "common_misconceptions": [
            {"misconception": "Including internal seam lines in perimeter calculations", "clarification": "Perimeter is strictly the exterior boundary enclosing the shape; internal construction lines must never be added."},
            {"misconception": "Thinking removing a corner reduces perimeter", "clarification": "A stepped or circular corner can increase or preserve perimeter depending on the arc length versus the original straight edges."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Exercise 6.1 Q5. Emphasize tracing the perimeter continuously with a pencil to ensure every boundary segment is counted exactly once.",
        "visual_lesson_plan": {
            "title": "Visualizing Composite Curvilinear Boundaries",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Vector plot of a stadium capsule track with straight sides of 80 m and semicircular ends of radius 30 m.",
            "concept_visuals": [
                {
                    "concept_title": "Stadium Capsule: 2 Straights + 2 Semicircles",
                    "diagram_title": "P = 2(80) + 2*pi*(30) = 348.57 m",
                    "interactive_math_formula": "P = 2L + 2\\pi r = 160 + 60\\pi",
                    "mafs_graph_config": {
                        "domain": [-60, 60],
                        "range": [-40, 40],
                        "lines": [
                            {"slope": 0, "intercept": 30, "color": "#2563EB", "label": "Top Straight (80 m)"},
                            {"slope": 0, "intercept": -30, "color": "#2563EB", "label": "Bottom Straight (80 m)"}
                        ],
                        "points": [
                            {"x": -40, "y": 30, "label": "A(-40, 30)"},
                            {"x": 40, "y": 30, "label": "B(40, 30)"},
                            {"x": 40, "y": -30, "label": "C(40, -30)"},
                            {"x": -40, "y": -30, "label": "D(-40, -30)"}
                        ]
                    },
                    "image_query": "capsule shape perimeter running track two straights two semicircles",
                    "video_query": "perimeter of composite figures semicircles and rectangle",
                    "what_to_explain": "The two semicircular ends combine to form one complete circle of circumference 2*pi*30 = 188.57 m. Adding two 80 m straights gives 348.57 m."
                },
                {
                    "concept_title": "Indented Semicircle Perimeter Increase",
                    "diagram_title": "Straight Replaced by Semicircular Cavity",
                    "interactive_math_formula": "\\Delta P = \\frac{\\pi D}{2} - D = D\\left(\\frac{\\pi}{2} - 1\\right)",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "-sqrt(max(0, 16 - x^2))", "color": "#DC2626", "label": "Semicircular Cavity r=4"}
                        ],
                        "points": [
                            {"x": -4, "y": 0, "label": "Edge (-4, 0)"},
                            {"x": 4, "y": 0, "label": "Edge (4, 0)"}
                        ]
                    },
                    "image_query": "perimeter of shape with semicircular indentation geometry",
                    "video_query": "perimeter of shape with semicircle cut out",
                    "what_to_explain": "Cutting out a semicircle increases the boundary length because the curved arc (pi*r) is longer than the diameter (2r)."
                },
                {
                    "concept_title": "Wave / S-Curve Alternating Semicircles",
                    "diagram_title": "Periodic Boundary: Sum of Semicircles",
                    "interactive_math_formula": "P = n \\times (\\pi r)",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-5, 5],
                        "curves": [
                            {"fn": "sqrt(max(0, 4 - (x + 2)^2))", "color": "#2563EB", "label": "Crest 1"},
                            {"fn": "-sqrt(max(0, 4 - (x - 2)^2))", "color": "#2563EB", "label": "Trough 1"}
                        ],
                        "points": [
                            {"x": -4, "y": 0, "label": "Start"},
                            {"x": 0, "y": 0, "label": "Inflection Point"},
                            {"x": 4, "y": 0, "label": "End"}
                        ]
                    },
                    "image_query": "s curve alternating semicircles boundary length perimeter",
                    "video_query": "perimeter of wave shape alternating semicircles",
                    "what_to_explain": "Each wave cycle consists of two semicircles forming a full circle circumference 2*pi*r."
                },
                {
                    "concept_title": "Quarter-Circle Rounded Corner",
                    "diagram_title": "Corner Truncation Arc L = (pi*r)/2",
                    "interactive_math_formula": "L = \\frac{1}{4}(2\\pi r) = \\frac{\\pi r}{2}",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 10],
                        "curves": [
                            {"fn": "sqrt(max(0, 36 - x^2))", "color": "#16A34A", "label": "Quarter Arc r=6"}
                        ],
                        "points": [
                            {"x": 0, "y": 6, "label": "(0, 6)"},
                            {"x": 6, "y": 0, "label": "(6, 0)"}
                        ]
                    },
                    "image_query": "perimeter of shape with rounded corners quarter circle",
                    "video_query": "how to find perimeter of shape with quarter circles",
                    "what_to_explain": "Each rounded corner replaces two perpendicular segments of length r with a curved arc of length pi*r/2."
                },
                {
                    "concept_title": "Composite Arch: Semicircle Atop Rectangle",
                    "diagram_title": "P = Bottom + 2 Sides + Semicircular Top",
                    "interactive_math_formula": "P = w + 2h + \\frac{\\pi w}{2}",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [0, 16],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#2563EB", "label": "Bottom w=8"},
                            {"slope": 999, "intercept": -4, "color": "#2563EB", "label": "Left h=10"},
                            {"slope": 999, "intercept": 4, "color": "#2563EB", "label": "Right h=10"}
                        ],
                        "curves": [
                            {"fn": "10 + sqrt(max(0, 16 - x^2))", "color": "#DC2626", "label": "Semicircle Arch"}
                        ],
                        "points": [
                            {"x": 0, "y": 14, "label": "Arch Peak (0, 14)"}
                        ]
                    },
                    "image_query": "Norman window arch perimeter rectangle with semicircle on top",
                    "video_query": "perimeter of Norman window shape math problem",
                    "what_to_explain": "The top straight side of the rectangle is interior and omitted; boundary consists of bottom, two heights, and the semicircular arch."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Composite Perimeters",
                    "questions": [
                        {
                            "question": "When computing the perimeter of a shape made of a rectangle with a semicircle attached to one side, why is that side of the rectangle excluded?",
                            "type": "short_answer",
                            "ideal_answer": "Because perimeter measures strictly the exterior outer boundary; that side is now inside the shape (an internal dividing line).",
                            "socratic_hint": "Does an ant walking along the outside fence walk across the internal seam?"
                        },
                        {
                            "question": "What is the perimeter of a stadium running track with two straight sections of 80 m and two semicircular ends of radius 30 m?",
                            "type": "short_answer",
                            "ideal_answer": "348.57 m (160 + 60*pi approx 160 + 188.57 = 348.57 m).",
                            "socratic_hint": "Add the two straights (2 * 80) to the full circumference of the two combined semicircular ends (2 * pi * 30)."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 6.1 Q5 (i): Find the perimeter of the athletics track shape in Fig. 6.14(i) with two straight stretches of 80 m and semicircular ends of radius 30 m (diameter 60 m).",
                "given": "Two straight edges of length L = 80 m each. Two semicircular ends of radius r = 30 m.",
                "formula": "Perimeter P = 2 * (Straight Length) + 2 * (Semicircular Arc Length) = 2L + 2*pi*r.",
                "substitution": "P = 2(80) + 2 * (22/7) * 30.",
                "calculation": "1. Straight edges sum: 2 * 80 = 160 m.\n2. Semicircular ends: 2 * (pi * r) = 2 * (22/7) * 30 = 1320 / 7 = 188.57 m.\n3. Total perimeter P = 160 + 188.57 = 348.57 m (or 2440/7 m).",
                "finalAnswer": "348.57 m (or 2440/7 m)",
                "unit": "m",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (ii): Find the perimeter of the shape in Fig. 6.14(ii) consisting of a rectangle of 10 cm by 8 cm with a semicircle on one of the 8 cm sides.",
                "given": "Rectangle dimensions: length = 10 cm, width = 8 cm. One width (8 cm) is replaced by an exterior semicircle of diameter D = 8 cm (r = 4 cm).",
                "formula": "Perimeter P = 2 * (Length) + (One Width) + (Semicircular Arc Length) = 2(10) + 8 + pi*r.",
                "substitution": "P = 2(10) + 8 + (22/7) * 4.",
                "calculation": "1. Linear boundary edges: 10 + 10 + 8 = 28 cm.\n2. Semicircular arc: pi * r = (22/7) * 4 = 88/7 = 12.57 cm.\n3. Total perimeter P = 28 + 12.57 = 40.57 cm (or 284/7 cm).",
                "finalAnswer": "40.57 cm (or 284/7 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (iii): Find the perimeter of the shape in Fig. 6.14(iii) consisting of a rectangle of 12 cm by 10 cm with two identical semicircular cutouts on the 10 cm sides.",
                "given": "Rectangle of 12 cm by 10 cm. Semicircular cutouts of diameter D = 10 cm (r = 5 cm) on both 10 cm ends.",
                "formula": "Perimeter P = 2 * (Length) + 2 * (Semicircular Arc Length) = 2(12) + 2*(pi*r).",
                "substitution": "P = 2(12) + 2 * (22/7) * 5.",
                "calculation": "1. Two straight sides of 12 cm: 2 * 12 = 24 cm.\n2. Two semicircular arcs form a full circle: 2 * (22/7) * 5 = 220/7 = 31.43 cm.\n3. Total perimeter P = 24 + 31.43 = 55.43 cm (or 388/7 cm).",
                "finalAnswer": "55.43 cm (or 388/7 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (iv): Find the perimeter of the shape in Fig. 6.14(iv) composed of a square of side 14 cm with four identical semicircles drawn on the outside of each of its four sides.",
                "given": "Square of side s = 14 cm. Four exterior semicircles of diameter D = 14 cm (r = 7 cm).",
                "formula": "The interior sides of the square are not part of the boundary. Boundary consists entirely of 4 semicircles: P = 4 * (pi * r) = 2 * (2*pi*r).",
                "substitution": "P = 4 * (22/7) * 7.",
                "calculation": "1. Cancel 7: P = 4 * 22 = 88 cm.\n2. The shape is a four-leaf clover boundary of perimeter 88 cm.",
                "finalAnswer": "88 cm",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (v): Find the perimeter of the shape in Fig. 6.14(v) consisting of a semicircle of diameter 28 cm with a smaller semicircle of diameter 14 cm removed from its base.",
                "given": "Large semicircle of diameter D1 = 28 cm (r1 = 14 cm). Small removed semicircle of diameter D2 = 14 cm (r2 = 7 cm). Remaining straight base = 28 - 14 = 14 cm.",
                "formula": "Perimeter P = (Large Arc) + (Small Arc) + (Remaining Straight Base) = pi*r1 + pi*r2 + 14.",
                "substitution": "P = (22/7)*14 + (22/7)*7 + 14.",
                "calculation": "1. Large arc: (22/7) * 14 = 44 cm.\n2. Small arc: (22/7) * 7 = 22 cm.\n3. Straight base segment: 14 cm.\n4. Total perimeter P = 44 + 22 + 14 = 80 cm.",
                "finalAnswer": "80 cm",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (vi): Find the perimeter of the shape in Fig. 6.14(vi) formed by a right triangle of legs 12 cm and 16 cm (hypotenuse 20 cm) with a semicircle erected on its hypotenuse.",
                "given": "Right triangle legs a = 12 cm, b = 16 cm. Hypotenuse D = sqrt(12^2 + 16^2) = sqrt(144 + 256) = sqrt(400) = 20 cm. Semicircle on hypotenuse of radius r = 10 cm.",
                "formula": "Perimeter P = Leg 1 + Leg 2 + Semicircular Arc = 12 + 16 + pi*r.",
                "substitution": "P = 12 + 16 + (22/7) * 10.",
                "calculation": "1. Legs sum: 12 + 16 = 28 cm.\n2. Semicircular arc on hypotenuse: (22/7) * 10 = 220/7 = 31.43 cm.\n3. Total perimeter P = 28 + 31.43 = 59.43 cm (or 416/7 cm).",
                "finalAnswer": "59.43 cm (or 416/7 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (vii): Find the perimeter of the shape in Fig. 6.14(vii) formed by a square of side 8 cm from which four quarter-circles of radius 2 cm are removed from each of the four corners.",
                "given": "Square side s = 8 cm. At each corner, a quarter-circle of radius r = 2 cm is removed.",
                "formula": "Each of the 4 edges has a straight section: 8 - 2(2) = 4 cm. The 4 quarter-circle corners combine to form 1 full circle of radius r = 2 cm: P = 4*(Straight) + 2*pi*r.",
                "substitution": "P = 4(4) + 2 * (22/7) * 2.",
                "calculation": "1. 4 straight edge sections: 4 * 4 = 16 cm.\n2. 4 quarter-arcs = 1 full circle: 2 * (22/7) * 2 = 88/7 = 12.57 cm.\n3. Total perimeter P = 16 + 12.57 = 28.57 cm (or 200/7 cm).",
                "finalAnswer": "28.57 cm (or 200/7 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (viii): Find the perimeter of the shape in Fig. 6.14(viii) composed of a rectangle with three semicircles of diameter 4 cm along the bottom edge.",
                "given": "Rectangle with length consisting of 3 contiguous semicircles of diameter 4 cm each (total length 12 cm), vertical sides of 6 cm, and top straight edge of 12 cm.",
                "formula": "Perimeter P = Top + 2*(Vertical Sides) + 3*(Semicircular Arcs of r = 2 cm).",
                "substitution": "P = 12 + 2(6) + 3 * (pi * 2).",
                "calculation": "1. Straight edges: 12 + 12 = 24 cm.\n2. 3 semicircular arcs: 3 * (22/7 * 2) = 132/7 = 18.86 cm.\n3. Total perimeter P = 24 + 18.86 = 42.86 cm (or 300/7 cm).",
                "finalAnswer": "42.86 cm (or 300/7 cm)",
                "unit": "cm",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.1 Q5 (ix): Find the perimeter of the symmetrical cross/petal figure in Fig. 6.14(ix) with straight segments of 10 cm and semicircular lobes of diameter 10 cm.",
                "given": "Curvilinear cross composed of 4 straight segments of length 10 cm and 4 semicircular lobes of diameter 10 cm (radius 5 cm).",
                "formula": "Perimeter P = 4 * (Straight Segments) + 4 * (Semicircular Arcs) = 4(10) + 4*(pi * 5).",
                "substitution": "P = 40 + 4 * (22/7) * 5.",
                "calculation": "1. Straight segments: 4 * 10 = 40 cm.\n2. 4 semicircular arcs form 2 complete circles of radius 5 cm: 2 * (2 * 22/7 * 5) = 440/7 = 62.86 cm.\n3. Total perimeter P = 40 + 62.86 = 102.86 cm (or 720/7 cm).",
                "finalAnswer": "102.86 cm (or 720/7 cm)",
                "unit": "cm",
                "has_diagram": True
            }
        ]
    }
