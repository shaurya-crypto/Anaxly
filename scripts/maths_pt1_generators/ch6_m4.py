"""
Chapter 6: Measuring Space: Perimeter and Area - Module 4
Curriculum ID: 2ca7b10a-3fb9-484f-8116-30d7b586c526
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_heron_triangle_svg

def get_m4():
    m4_svg = build_heron_triangle_svg(
        a=13, b=14, c=15,
        title="Heron's Formula: Area = sqrt(s(s-a)(s-b)(s-c))",
        caption="Triangle with integer sides 13, 14, 15 and semiperimeter s = 21 yielding exact integer area = 84"
    )

    return {
        "order_index": 4,
        "title": "Textbook Exercise Solver 3: Triangle Medians, Dissections & Heron's Formula (Exercise 6.2 Set 2 & Heron's Triangles)",
        "description": "Comprehensive step-by-step solutions to Exercise 6.2 (Q3, Q4, Q9, Q10, Q11) and End-of-Chapter Questions 2, 3, 4, 5, 6, 10, 15 (parts i to iii), 16, and 20. Master triangle median area bisection, Heron's formula calculations (3:5:7 ratio, 7-24-25 right triangle in two ways), isosceles triangle areas, area scaling with scale factor k (Area ratio k^2), and triangle fraction shading.",
        "subtopics": [
            "Heron's formula derivation and calculation: Area = sqrt(s(s-a)(s-b)(s-c))",
            "Median Area Invariant: A median divides a triangle into two triangles of equal area",
            "Ratio of areas under point P on median: Area(PAB) = Area(PAC)",
            "Area scaling theorem: Scaling linear dimensions by k multiplies area by k^2",
            "Quadratic proof of rectangle congruence given equal perimeter and equal area",
            "Trisection base segments and fraction shaded geometric deductions"
        ],
        "key_concepts": [
            "Heron's Formula Invariant: Any triangle with known side lengths a, b, c has area determined by semiperimeter s = (a+b+c)/2 via K = sqrt(s(s-a)(s-b)(s-c)).",
            "Median Equal Area Invariant: In triangle ABC with median AD, Area(ABD) = Area(ACD) because both share equal bases BD = CD and have the same altitude from A.",
            "Difference Area Invariant: For point P on median AD, Area(PBD) = Area(PCD). Subtracting gives Area(PAB) = Area(PAC).",
            "Pythagorean Double Method: For a 7-24-25 triangle, Area = (1/2)*7*24 = 84 cm^2; Heron's formula confirms sqrt(28*21*4*1) = 84 cm^2.",
            "Isoperimetric Rectangle Uniqueness: If 2(x + y) = P and xy = A, x and y are the unique roots of t^2 - (P/2)t + A = 0, proving all rectangles with identical area and perimeter are congruent.",
            "Quadratic Area Scaling Law: A shape scaled by linear factor k contains exactly k^2 congruent copies of the original shape."
        ],
        "success_criteria": "Students can apply Heron's formula to find areas of triangles from side lengths or ratios, prove median area equality, calculate area ratios under linear scaling, and solve competitive board dissection problems.",
        "chapter_notes": "Module 4 covers the full depth of triangular area calculations from ancient Indian and Alexandrian geometry through modern scaling laws.",
        "common_misconceptions": [
            {"misconception": "Believing a median bisects the perimeter of a triangle", "clarification": "A median bisects the AREA of a triangle, but generally does NOT bisect its perimeter unless the triangle is isosceles."},
            {"misconception": "Doubling triangle side lengths doubles the area", "clarification": "Doubling all side lengths multiplies the area by 2^2 = 4, allowing 4 congruent copies to fit inside."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Heron's formula and median proofs. Show all prime factor groupings inside the square root to make simplification intuitive.",
        "visual_lesson_plan": {
            "title": "Visualizing Triangular Areas and Dissections",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Vector triangle with sides 13, 14, 15 showing the median and altitude for Heron's formula.",
            "concept_visuals": [
                {
                    "concept_title": "Heron's Triangle: Integer Sides 13, 14, 15",
                    "diagram_title": "s = 21, Area = sqrt(21 * 8 * 7 * 6) = 84",
                    "interactive_math_formula": "K = \\sqrt{21 \\times 8 \\times 7 \\times 6} = \\sqrt{7056} = 84",
                    "mafs_graph_config": {
                        "domain": [-2, 16],
                        "range": [-2, 14],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#0F172A", "label": "Base c = 14"},
                            {"slope": 999, "intercept": 5, "color": "#16A34A", "label": "Altitude h = 12"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "A(0, 0)"},
                            {"x": 14, "y": 0, "label": "B(14, 0)"},
                            {"x": 5, "y": 12, "label": "C(5, 12) [b=13, a=15]"}
                        ]
                    },
                    "image_query": "Heron formula triangle sides 13 14 15 integer area 84",
                    "video_query": "how to use Heron's formula to find area of triangle step by step",
                    "what_to_explain": "Factoring inside the radical: 21*8*7*6 = (3*7)*(2^3)*7*(2*3) = 2^4 * 3^2 * 7^2, yielding exact integer area 4 * 3 * 7 = 84."
                },
                {
                    "concept_title": "Median Area Bisection Invariant",
                    "diagram_title": "Median AD Bisects Area: Area(ABD) = Area(ACD)",
                    "interactive_math_formula": "\\text{Area}(\\Delta ABD) = \\frac{1}{2} BD \\times h = \\frac{1}{2} CD \\times h = \\text{Area}(\\Delta ACD)",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [-2, 10],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#0F172A", "label": "Base BC"},
                            {"slope": 999, "intercept": 0, "color": "#DC2626", "label": "Median AD"}
                        ],
                        "points": [
                            {"x": 0, "y": 8, "label": "A(0, 8)"},
                            {"x": -6, "y": 0, "label": "B(-6, 0)"},
                            {"x": 6, "y": 0, "label": "C(6, 0)"},
                            {"x": 0, "y": 0, "label": "Midpoint D(0, 0)"}
                        ]
                    },
                    "image_query": "median of a triangle divides it into two triangles of equal area proof",
                    "video_query": "prove that median of triangle divides it into two equal areas",
                    "what_to_explain": "Because D is the midpoint of BC, BD = CD. Both triangles share vertex A and have identical perpendicular altitude h."
                },
                {
                    "concept_title": "7-24-25 Right Triangle: Double Method Area",
                    "diagram_title": "Base*Height/2 = 84 cm² vs Heron's = 84 cm²",
                    "interactive_math_formula": "\\frac{1}{2}(7)(24) = 84 = \\sqrt{28(21)(4)(1)}",
                    "mafs_graph_config": {
                        "domain": [-2, 26],
                        "range": [-2, 10],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#2563EB", "label": "Leg 24 cm"},
                            {"slope": 999, "intercept": 0, "color": "#2563EB", "label": "Leg 7 cm"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Right Angle (0, 0)"},
                            {"x": 24, "y": 0, "label": "(24, 0)"},
                            {"x": 0, "y": 7, "label": "(0, 7)"}
                        ]
                    },
                    "image_query": "7 24 25 right triangle area calculation Heron formula",
                    "video_query": "find area of 7 24 25 triangle two ways",
                    "what_to_explain": "Method 1 uses perpendicular legs (1/2)*7*24 = 84. Method 2 uses semiperimeter s = 28 in Heron's formula, confirming 84."
                },
                {
                    "concept_title": "Area Scaling Matrix: 4 Copies Fit in 2x Scaled Shape",
                    "diagram_title": "Linear 2x implies Area 4x (4 Congruent Sub-triangles)",
                    "interactive_math_formula": "\\text{Area}(2A, 2B, 2C) = 2^2 \\times \\text{Area}(A, B, C) = 4K",
                    "mafs_graph_config": {
                        "domain": [-4, 16],
                        "range": [-2, 12],
                        "points": [
                            {"x": 0, "y": 0, "label": "A"},
                            {"x": 12, "y": 0, "label": "B"},
                            {"x": 6, "y": 10.39, "label": "C"},
                            {"x": 6, "y": 0, "label": "Mid 1"},
                            {"x": 9, "y": 5.2, "label": "Mid 2"},
                            {"x": 3, "y": 5.2, "label": "Mid 3"}
                        ]
                    },
                    "image_query": "triangle partitioned into four congruent triangles midpoint area scaling",
                    "video_query": "why area scales by square of scale factor geometry",
                    "what_to_explain": "Connecting the three midpoints partitions the triangle into 4 identical congruent copies, proving Area scales by 2^2 = 4."
                },
                {
                    "concept_title": "Trisection Segment Equal Area Invariant",
                    "diagram_title": "Three Triangles with Equal Bases on Trisection Line",
                    "interactive_math_formula": "\\text{Area}_1 = \\text{Area}_2 = \\text{Area}_3 = \\frac{1}{3}\\text{Area}_{\\text{total}}",
                    "mafs_graph_config": {
                        "domain": [-2, 14],
                        "range": [-2, 10],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#0F172A", "label": "Trisected Base"}
                        ],
                        "points": [
                            {"x": 6, "y": 8, "label": "Common Vertex V"},
                            {"x": 0, "y": 0, "label": "0"},
                            {"x": 4, "y": 0, "label": "Trisection Point 1"},
                            {"x": 8, "y": 0, "label": "Trisection Point 2"},
                            {"x": 12, "y": 0, "label": "End"}
                        ]
                    },
                    "image_query": "lines from vertex to points of trisection equal triangle areas",
                    "video_query": "trisection of base of triangle equal areas proof",
                    "what_to_explain": "Each of the 3 sub-triangles has base length b/3 and common height h, so each has area exactly (1/3)*Total Area."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Heron's Formula & Triangle Areas",
                    "questions": [
                        {
                            "question": "If the sides of a triangle are in the ratio 3 : 5 : 7 and its perimeter is 300 m, what is its area using Heron's formula?",
                            "type": "short_answer",
                            "ideal_answer": "1500*sqrt(3) m^2 (sides are 60, 100, 140 m; s = 150 m; Area = sqrt(150 * 90 * 50 * 10) = 1500*sqrt(3)).",
                            "socratic_hint": "Find the sides first: 3x + 5x + 7x = 300 => x = 20."
                        },
                        {
                            "question": "If two rectangles have the exact same perimeter and the exact same area, must they be congruent?",
                            "type": "short_answer",
                            "ideal_answer": "Yes, because their sides are the unique solutions to the quadratic equation t^2 - (P/2)t + A = 0.",
                            "socratic_hint": "Set up equations x + y = P/2 and xy = A and consider the quadratic they satisfy."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 6.2 Q3: Find the area of a triangle, given that its sides are 8 cm and 11 cm long, and its perimeter is 32 cm.",
                "given": "Sides a = 8 cm, b = 11 cm, perimeter P = 32 cm.",
                "formula": "Third side c = P - (a + b). Heron's formula: K = sqrt(s(s-a)(s-b)(s-c)) with s = P/2.",
                "substitution": "c = 32 - (8 + 11) = 32 - 19 = 13 cm. s = 32 / 2 = 16 cm.",
                "calculation": "1. Third side c = 13 cm.\n2. Semiperimeter s = 16 cm.\n3. Compute factors:\n   s - a = 16 - 8 = 8\n   s - b = 16 - 11 = 5\n   s - c = 16 - 13 = 3.\n4. K = sqrt(16 * 8 * 5 * 3).\n5. Simplify: sqrt(16) * sqrt(8 * 5 * 3) = 4 * sqrt(4 * 2 * 15) = 4 * 2 * sqrt(30) = 8*sqrt(30) cm^2.\n6. Numerical value: 8 * 5.477 = 43.82 cm^2.",
                "finalAnswer": "8*sqrt(30) cm^2 (approx 43.82 cm^2)",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q4: The sides of a triangular plot are in the ratio 3 : 5 : 7; its perimeter is 300 m. Find its area.",
                "given": "Sides ratio 3 : 5 : 7, perimeter P = 300 m.",
                "formula": "Let sides be 3x, 5x, 7x. 3x + 5x + 7x = 300. Heron's formula: K = sqrt(s(s-a)(s-b)(s-c)).",
                "substitution": "15x = 300 => x = 20 m. Sides: a = 60 m, b = 100 m, c = 140 m. s = 300 / 2 = 150 m.",
                "calculation": "1. Sides: a = 60 m, b = 100 m, c = 140 m.\n2. Semiperimeter s = 150 m.\n3. Factors:\n   s - a = 150 - 60 = 90\n   s - b = 150 - 100 = 50\n   s - c = 150 - 140 = 10.\n4. K = sqrt(150 * 90 * 50 * 10).\n5. Factor powers of 10: 150 * 90 * 50 * 10 = (15 * 9 * 5 * 1) * 10^4 = (675) * 10000 = 6,750,000.\n6. 675 = 225 * 3 = 15^2 * 3.\n7. K = sqrt(15^2 * 3 * 100^2) = 15 * 100 * sqrt(3) = 1500*sqrt(3) m^2.\n8. Numerical value: 1500 * 1.732 = 2598.08 m^2.",
                "finalAnswer": "1500*sqrt(3) m^2 (approx 2598.08 m^2)",
                "unit": "m^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q9: In triangle ABC, the midpoint of BC is D. Median AD is drawn. P is any point on AD. Show that the ratio of the areas of triangle PAB and triangle PAC is 1 : 1.",
                "given": "Triangle ABC with median AD (D is midpoint of BC). P is any point on AD.",
                "formula": "A median of a triangle divides it into two triangles of equal area.",
                "substitution": "In triangle ABC, AD is median. In triangle PBC, PD is median.",
                "calculation": "1. In triangle ABC, AD is the median from vertex A to side BC.\n   Therefore, Area(triangle ABD) = Area(triangle ACD) ... (Equation 1).\n2. In triangle PBC, PD is the median from vertex P to side BC (since D is midpoint of BC).\n   Therefore, Area(triangle PBD) = Area(triangle PCD) ... (Equation 2).\n3. Subtract Equation 2 from Equation 1:\n   Area(triangle ABD) - Area(triangle PBD) = Area(triangle ACD) - Area(triangle PCD).\n4. Notice from the figure that:\n   Area(triangle ABD) - Area(triangle PBD) = Area(triangle PAB).\n   Area(triangle ACD) - Area(triangle PCD) = Area(triangle PAC).\n5. Therefore, Area(triangle PAB) = Area(triangle PAC).\n6. The ratio Area(triangle PAB) : Area(triangle PAC) is strictly 1 : 1.",
                "finalAnswer": "1 : 1 (Proved: Area(triangle PAB) = Area(triangle PAC)).",
                "unit": "ratio",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q10: In Fig. 6.33, triangle ABC has median AD and midpoints creating shaded regions. What is the ratio of the area of triangle PAB to triangle PBC?",
                "given": "Triangle ABC with median AD and point P on AD dividing AD in a specific ratio m:n.",
                "formula": "Area of triangles sharing vertex P with collinear bases on AD.",
                "substitution": "Let AP : PD = k.",
                "calculation": "1. As established in Q9, Area(triangle PAB) = Area(triangle PAC).\n2. In triangle ABD, P divides altitude line AD into segments AP and PD.\n3. The ratio of Area(triangle PAB) to Area(triangle PBD) is AP : PD.\n4. Since Area(triangle PBC) = 2 * Area(triangle PBD), the ratio Area(triangle PAB) : Area(triangle PBC) = (1/2)*(AP / PD).\n5. If P is the centroid G (where AG : GD = 2 : 1), then Area(triangle GAB) = (1/3)*Total Area and Area(triangle GBC) = (1/3)*Total Area, so ratio is 1 : 1.",
                "finalAnswer": "Ratio is 1 : 1 when P is the centroid G (each forming 1/3 of the total area of triangle ABC).",
                "unit": "ratio",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q11: In Fig. 6.34, D is midpoint of BC in triangle ABC. P is a point on AD. Line CQ is parallel to PD intersecting AB at Q. Prove that Area(triangle BPQ) = Area(triangle ABD).",
                "given": "D is midpoint of BC in triangle ABC. P lies on median AD. CQ || PD with Q on AB. PQ is joined.",
                "formula": "Triangles on the same base between parallel lines have equal area: Area(triangle PDQ) = Area(triangle PDC) because PD || CQ.",
                "substitution": "Base PD is parallel to line QC.",
                "calculation": "1. Given PD || QC. Both triangle PDQ and triangle PDC share the exact same base PD and lie between parallel lines PD and QC.\n2. Therefore, Area(triangle PDQ) = Area(triangle PDC).\n3. In triangle ABC, D is the midpoint of BC, so median AD gives Area(triangle ABD) = (1/2)*Area(triangle ABC).\n4. In triangle PBC, PD is the median to BC, so Area(triangle PBD) = Area(triangle PDC).\n5. Substituting step 2 into step 4: Area(triangle PBD) = Area(triangle PDQ).\n6. Adding Area(triangle PBD) to Area(triangle PBQ) demonstrates the required area equivalence: Area(triangle BPQ) = Area(triangle ABD).",
                "finalAnswer": "Proved: Since PD || QC, Area(triangle PDQ) = Area(triangle PDC) = Area(triangle PBD), confirming Area(triangle BPQ) = Area(triangle ABD).",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q2: An isosceles triangle has perimeter 40 cm; the equal sides are 15 cm each. Find the area of the triangle.",
                "given": "Isosceles triangle: equal sides a = 15 cm, b = 15 cm, perimeter P = 40 cm.",
                "formula": "Base c = P - (a + b) = 40 - 30 = 10 cm. Height h = sqrt(a^2 - (c/2)^2). Area = (1/2)*c*h.",
                "substitution": "c = 10 cm. Half-base = 5 cm. h = sqrt(15^2 - 5^2).",
                "calculation": "1. Base c = 40 - (15 + 15) = 10 cm.\n2. In right triangle formed by altitude, leg 15 cm, and half-base 5 cm:\n   h = sqrt(15^2 - 5^2) = sqrt(225 - 25) = sqrt(200) = 10*sqrt(2) cm.\n3. Area = (1/2) * base * height = (1/2) * 10 * 10*sqrt(2) = 50*sqrt(2) cm^2.\n4. Numerical value: 50 * 1.4142 = 70.71 cm^2.",
                "finalAnswer": "50*sqrt(2) cm^2 (approx 70.71 cm^2)",
                "unit": "cm^2",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3: An isosceles triangle has base 10 cm, and its area is 60 cm^2. What are the lengths of the equal sides?",
                "given": "Base b = 10 cm, Area A = 60 cm^2.",
                "formula": "Area = (1/2) * base * height => height h = 2*A / base. Equal side leg = sqrt(h^2 + (base/2)^2).",
                "substitution": "h = (2 * 60) / 10 = 120 / 10 = 12 cm. Half-base = 5 cm.",
                "calculation": "1. Altitude h = 12 cm.\n2. In right triangle formed by altitude, half-base (5 cm), and equal side s:\n   s^2 = h^2 + (b/2)^2 = 12^2 + 5^2.\n3. s^2 = 144 + 25 = 169.\n4. s = sqrt(169) = 13 cm.",
                "finalAnswer": "13 cm each",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4: The area of a right-angled triangle is 54 sq. cm. One of its legs has length 12 cm. Find its perimeter.",
                "given": "Right-angled triangle: Area = 54 cm^2, leg a = 12 cm.",
                "formula": "Area = (1/2) * a * b => b = 2*Area / a. Hypotenuse c = sqrt(a^2 + b^2). Perimeter P = a + b + c.",
                "substitution": "b = (2 * 54) / 12 = 108 / 12 = 9 cm.",
                "calculation": "1. Other leg b = 9 cm.\n2. Hypotenuse c = sqrt(12^2 + 9^2) = sqrt(144 + 81) = sqrt(225) = 15 cm.\n3. Perimeter P = a + b + c = 12 + 9 + 15 = 36 cm.",
                "finalAnswer": "36 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q5: The sides of a triangle are in the ratio 2 : 3 : 4, and its perimeter is 45 cm. Find its area.",
                "given": "Sides ratio 2 : 3 : 4, perimeter P = 45 cm.",
                "formula": "2x + 3x + 4x = 45 => 9x = 45 => x = 5 cm. Sides: a = 10 cm, b = 15 cm, c = 20 cm. Heron's formula: K = sqrt(s(s-a)(s-b)(s-c)).",
                "substitution": "s = 45 / 2 = 22.5 cm. Factors: s-a = 12.5, s-b = 7.5, s-c = 2.5.",
                "calculation": "1. Sides: a = 10 cm, b = 15 cm, c = 20 cm.\n2. Semiperimeter s = 45/2 = 22.5 cm.\n3. Factors in fraction form:\n   s = 45/2\n   s - a = 45/2 - 20/2 = 25/2\n   s - b = 45/2 - 30/2 = 15/2\n   s - c = 45/2 - 40/2 = 5/2.\n4. Product inside radical:\n   (45/2) * (25/2) * (15/2) * (5/2) = (45 * 25 * 15 * 5) / 16.\n5. Simplify numerator: 45 = 9 * 5, 25 = 5^2, 15 = 3 * 5.\n   Numerator = (9 * 5) * 25 * (3 * 5) * 5 = 9 * 25 * 25 * 15 = (3^2) * (25^2) * 15.\n6. Square root: sqrt((3^2 * 25^2 * 15) / 16) = (3 * 25 * sqrt(15)) / 4 = (75*sqrt(15)) / 4 cm^2.\n7. Numerical value: (75 * 3.873) / 4 = 290.47 / 4 = 72.62 cm^2.",
                "finalAnswer": "(75*sqrt(15)) / 4 cm^2 (approx 72.62 cm^2)",
                "unit": "cm^2",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q6: The sides of a triangle have lengths 7 cm, 24 cm, 25 cm. Find the area of the triangle in two different ways.",
                "given": "Sides: a = 7 cm, b = 24 cm, c = 25 cm.",
                "formula": "Method 1: Check Pythagoras 7^2 + 24^2 = 49 + 576 = 625 = 25^2 => Right triangle, Area = (1/2)*a*b.\nMethod 2: Heron's formula: K = sqrt(s(s-a)(s-b)(s-c)).",
                "substitution": "s = (7 + 24 + 25) / 2 = 56 / 2 = 28 cm.",
                "calculation": "1. Method 1 (Right Triangle Formula):\n   Since 7^2 + 24^2 = 49 + 576 = 625 = 25^2, triangle is right-angled with legs 7 cm and 24 cm.\n   Area = (1/2) * 7 * 24 = 7 * 12 = 84 cm^2.\n2. Method 2 (Heron's Formula):\n   s = 28 cm.\n   s - a = 28 - 7 = 21\n   s - b = 28 - 24 = 4\n   s - c = 28 - 25 = 3.\n   K = sqrt(28 * 21 * 4 * 3).\n   Factor: 28 = 4 * 7; 21 = 3 * 7.\n   Product = (4 * 7) * (3 * 7) * 4 * 3 = 4^2 * 3^2 * 7^2.\n   K = sqrt(4^2 * 3^2 * 7^2) = 4 * 3 * 7 = 84 cm^2.\n3. Both independent methods give exactly 84 cm^2.",
                "finalAnswer": "84 cm^2 (Both methods yield identical area: (1/2)*7*24 = 84 and Heron's sqrt(28*21*4*3) = 84).",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q10: Two rectangles have the same area and the same perimeter. Does this mean that they are congruent to each other?",
                "given": "Two rectangles R1 (sides x1, y1) and R2 (sides x2, y2) with Area(R1) = Area(R2) = A and Perimeter(R1) = Perimeter(R2) = P.",
                "formula": "Semiperimeter s = P / 2 = x + y. Area A = x * y. x and y are roots of t^2 - st + A = 0.",
                "substitution": "Quadratic roots: t = (s +- sqrt(s^2 - 4A)) / 2.",
                "calculation": "1. In rectangle R1 with sides x1 and y1:\n   x1 + y1 = P / 2 and x1 * y1 = A.\n2. By Vieta's formulas, x1 and y1 are the two roots of the quadratic equation:\n   t^2 - (P/2)t + A = 0.\n3. In rectangle R2 with sides x2 and y2:\n   x2 + y2 = P / 2 and x2 * y2 = A.\n   Therefore, x2 and y2 are ALSO the roots of the exact same quadratic equation t^2 - (P/2)t + A = 0.\n4. By the Fundamental Theorem of Algebra, a degree-2 polynomial has at most two roots.\n5. Therefore, the unordered set of side lengths {x1, y1} is identical to the unordered set of side lengths {x2, y2}.\n6. Because both rectangles have the exact same length and width, they are congruent to each other.",
                "finalAnswer": "Yes, they MUST be congruent. The dimensions of any rectangle are uniquely determined by the roots of the quadratic equation t^2 - (P/2)t + A = 0.",
                "unit": "algebraic proof",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q15 (i, ii, iii): Three problems about fitting congruent shapes together: (i) Rectangle scaling 2, (ii) Triangle scaling 2, (iii) Triangle scaling 3.",
                "given": "(i) Rectangle ABCD (a, b) vs PQRS (2a, 2b). (ii) Triangle (a, b, c) vs (2a, 2b, 2c). (iii) Triangle (a, b, c) vs (3a, 3b, 3c).",
                "formula": "Area scaling law: Area(k * S) = k^2 * Area(S).",
                "substitution": "k = 2 => k^2 = 4; k = 3 => k^2 = 9.",
                "calculation": "1. Part (i): Area(PQRS) = (2a)*(2b) = 4ab = 4 * Area(ABCD). 4 copies of rectangle ABCD can be arranged in a 2x2 grid to fit perfectly into PQRS without overlap.\n2. Part (ii): For triangle PQR with sides 2a, 2b, 2c, by Heron's formula each factor scales by 2, so area scales by sqrt(2*2*2*2) = 4. 4 copies of triangle ABC fit perfectly inside triangle PQR by connecting the three midpoints (creating 3 upright corner triangles and 1 inverted central triangle).\n3. Part (iii): For triangle PQR with sides 3a, 3b, 3c, scale factor k = 3, so Area = 3^2 = 9 times. Dividing each side into 3 equal segments and drawing parallel grid lines partitions triangle PQR into 1 + 3 + 5 = 9 identical copies of triangle ABC.",
                "finalAnswer": "(i) Area ratio is 4, exactly 4 copies fit; (ii) Area ratio is 4, exactly 4 copies fit; (iii) Area ratio is 9, exactly 9 copies fit.",
                "unit": "scaling proofs",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q16: What fraction of the triangle in Fig. 6.43 and what fraction of the square in Fig. 6.44 is shaded?",
                "given": "Fig. 6.43: Triangle with midpoints connected. Fig. 6.44: Square with corner lines connecting to centre.",
                "formula": "Midpoint triangle partition: Area = 1/4 of total. Square diagonal symmetry.",
                "substitution": "Fraction = Shaded Area / Total Area.",
                "calculation": "1. In Fig. 6.43, connecting the midpoints of the three sides of a triangle divides it into 4 mutually congruent triangles, each having 1/4 of the total area. The shaded central triangle represents exactly 1/4 of the total area.\n2. In Fig. 6.44, the square is partitioned symmetrically into 4 congruent quadrants or triangles along diagonals. Two of the four equal triangles are shaded.\n   Shaded fraction = 2 / 4 = 1/2.",
                "finalAnswer": "Fig. 6.43: 1/4 of the triangle is shaded; Fig. 6.44: 1/2 of the square is shaded.",
                "unit": "fractions",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q20: Show that the areas of the shaded blue triangle and the shaded red triangle in Fig. 6.48 are equal (lines from vertex to trisection points of opposite side).",
                "given": "Triangle with base divided into three equal segments (points of trisection). Lines drawn from opposite vertex to trisection points.",
                "formula": "Triangles with equal bases and the same altitude have equal areas: Area = (1/2) * base * height.",
                "substitution": "Base segment 1 = Base segment 2 = Base segment 3 = b / 3.",
                "calculation": "1. Let base BC of triangle ABC be trisected at points D and E, so BD = DE = EC = b / 3.\n2. Lines AD and AE are drawn from vertex A to the trisection points.\n3. This creates three adjacent triangles: triangle ABD, triangle ADE, and triangle AEC.\n4. All three triangles share the common vertex A, meaning they all have the exact same perpendicular height h dropped from A to line BC.\n5. Area(triangle ABD) = (1/2) * BD * h = (1/2) * (b/3) * h.\n6. Area(triangle ADE) = (1/2) * DE * h = (1/2) * (b/3) * h.\n7. Area(triangle AEC) = (1/2) * EC * h = (1/2) * (b/3) * h.\n8. Therefore, all three sub-triangles (including the shaded blue and red triangles) have identical area equal to (1/3) of the total area of triangle ABC.\n9. They can be cut and translated directly since their bases and heights are identical.",
                "finalAnswer": "Proved: Both triangles have base length b/3 and common height h, so each has area (1/6)*b*h = (1/3)*Area(ABC).",
                "unit": "geometric proof",
                "has_diagram": True
            }
        ]
    }
