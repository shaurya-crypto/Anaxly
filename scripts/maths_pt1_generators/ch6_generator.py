"""
Chapter 6: Measuring Space: Perimeter and Area
Curriculum ID: 2ca7b10a-3fb9-484f-8116-30d7b586c526
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

import json
from .svg_builder import build_running_track_svg, build_heron_triangle_svg, get_svg_wrapper

def get_ch6_modules():
    curriculum_id = "2ca7b10a-3fb9-484f-8116-30d7b586c526"
    
    # -------------------------------------------------------------
    # MODULE 1: Circle Perimeter, π & 400m Running Track Staggers
    # -------------------------------------------------------------
    m1_svg = build_running_track_svg(
        title="400m Running Track: Lane Geometry & Stagger",
        caption="Two straightaways of 84.39m and two semicircles of radius 36.5m. Lane stagger Δ = 2πw ≈ 7.67m"
    )

    m1 = {
        "order_index": 1,
        "title": "Circle Circumference, The Transcendental π Ratio & 400m Athletic Track Staggers",
        "description": "Formulate the constant ratio C/D = π across all circles. Derive the circumference formula C = 2πr = πd. Analyze standard 400m athletic track geometry, proving why outer runners must start ahead with exact stagger Δ = 2πw.",
        "subtopics": [
            "Empirical discovery of the invariant ratio: Circumference / Diameter = π",
            "Rational approximations of π: Archimedean 22/7, Aryabhata's 62832/20000 = 3.1416",
            "Formulas: C = 2πr and C = πd with dimensional consistency",
            "Wheel revolutions and distance traveled: Distance = Revolutions * Circumference",
            "400m Athletic Track Architecture: Two straightaways (84.39m) + two semicircles (radius 36.5m)",
            "Derivation of the Lane Stagger Formula: Δ = 2πw for lane width w"
        ],
        "key_concepts": [
            "Pi Invariant: The ratio of the perimeter of ANY circle to its diameter is an irrational mathematical constant π ≈ 3.14159265... or 22/7.",
            "Distance-Revolution Relationship: In one complete revolution of a rolling circular wheel of radius r, the linear distance traversed along the ground equals exactly its circumference: d = 2πr.",
            "Standard Athletic Track Geometry: Consists of two straight lengths 2L and two semicircles of radius r that form a complete circle of circumference 2πr. Total inner perimeter = 2L + 2πr = 400 m.",
            "Universal Lane Stagger Formula: For any lane k of width w, its radius is r_k = r_1 + (k - 1)w. The perimeter is P_k = 2L + 2π[r_1 + (k - 1)w] = P_1 + 2π(k - 1)w. The stagger between consecutive lanes is strictly Δ = 2πw, which is completely independent of the track radius!"
        ],
        "success_criteria": "Calculate circle circumferences, solve wheel revolution problems, and derive and calculate track staggers using Δ = 2πw.",
        "chapter_notes": "The 400m track problem in Ganita Manjari is one of the finest real-world applications in the curriculum. Point out that the stagger 2πw depends ONLY on lane width, not on the radius or straight length.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 6.1 Q1 & Q3: (Q1) The perimeter of a circle is 44 cm. What is its radius? (Q3) A bicycle wheel has a diameter of 70 cm. How many revolutions will it make to travel a distance of 1.1 km?",
                "given": "Q1: Perimeter C = 44 cm, use π = 22/7. Q3: Diameter d = 70 cm, Total distance = 1.1 km = 1100 m = 110,000 cm.",
                "formula": "Q1: C = 2πr => r = C / (2π). Q3: Circumference C = πd, Revolutions N = Total Distance / C.",
                "substitution": "Q1: r = 44 / [2 * (22/7)]. Q3: C = (22/7) * 70 cm. N = 110,000 / C.",
                "calculation": "Part (Q1):\\nStep 1: Apply circumference formula: C = 2 * (22/7) * r.\\nStep 2: Substitute C = 44:\\n  44 = (44/7) * r\\nStep 3: Solve for r:\\n  r = 44 * (7/44) = 7 cm.\\n\\nPart (Q3):\\nStep 1: Compute circumference of bicycle wheel:\\n  C = π * d = (22/7) * 70 = 22 * 10 = 220 cm = 2.2 m.\\nStep 2: Convert total distance to centimetres:\\n  1.1 km = 1.1 * 1000 m = 1100 m = 110,000 cm.\\nStep 3: Calculate number of revolutions:\\n  N = Total Distance / Circumference\\n  N = 110,000 cm / 220 cm = 500 revolutions.",
                "finalAnswer": "Q1: Radius = 7 cm; Q3: 500 revolutions",
                "unit": "centimetres and revolutions",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m1_svg
            },
            {
                "problem": "Textbook Exercise 6.1 Q4: A standard 400m running track has lane widths of 1.22 m. Find the starting stagger for Lane 2, Lane 3, and Lane 8 compared to Lane 1 in a 400m race.",
                "given": "Lane width w = 1.22 m, use π = 22/7.",
                "formula": "Stagger for Lane k relative to Lane 1: S_k = 2π * (k - 1) * w.",
                "substitution": "S_k = 2 * (22/7) * (k - 1) * 1.22 m = (44/7) * 1.22 * (k - 1) = 7.66857 * (k - 1) m.",
                "calculation": "Step 1: Compute the base single-lane stagger Δ = 2πw:\\n  Δ = 2 * (22/7) * 1.22 = (44 * 1.22) / 7 = 53.68 / 7 approx 7.67 m.\\nStep 2: Stagger for Lane 2 (k = 2):\\n  S_2 = 1 * Δ = 7.67 m.\\nStep 3: Stagger for Lane 3 (k = 3):\\n  S_3 = 2 * Δ = 2 * 7.6686 = 15.34 m.\\nStep 4: Stagger for Lane 8 (k = 8):\\n  S_8 = 7 * Δ = 7 * (53.68 / 7) = 53.68 m.",
                "finalAnswer": "Lane 2 Stagger = 7.67 m; Lane 3 Stagger = 15.34 m; Lane 8 Stagger = 53.68 m",
                "unit": "metres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Believing the stagger depends on the radius of the curve. The track stagger Δ = 2πw is entirely independent of the radius r!",
            "Forgetting to convert units (e.g., dividing kilometres by centimetres without converting to identical units)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Start with the athletic track broadcast visual. Ask why runners in outer lanes start ahead. Guide them through the algebra showing that the straightaways cancel out, leaving exactly 2πw. Call write_chalkboard(action='draw_svg_diagram', content='400m Running Track').",
        "visual_lesson_plan": {
            "title": "Running Track & Circumference Geometry",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Vector diagram of a 400m running track with concentric lanes and stagger markers.",
            "concept_visuals": [
                {
                    "concept_title": "Athletic Track Stagger Geometry",
                    "diagram_title": "400m Track Staggers",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m1_svg,
                    "interactive_math_formula": "Delta = 2*pi*w",
                    "mafs_graph_config": {"domain": [-10, 10], "range": [-6, 6]},
                    "image_query": "400m athletic running track lane staggers geometry blueprint",
                    "video_query": "Why runners start at different positions 400m track math explained",
                    "image_url": "/images/curriculum/ch6_running_track.png",
                    "what_to_make": "Athletic track with lanes, straight lengths, and curved semicircles.",
                    "what_to_explain": "Demonstrate why each lane adds 2πw to the total perimeter.",
                    "timing_and_cue": "Display at 02:00 during track intuition."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Perimeter & Track Geometry",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the ratio of the circumference of a circle to its radius?",
                            "ideal_answer": "2π (approximately 6.283).",
                            "socratic_hint": "Circumference is 2πr: divide by r."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why does the lane stagger Δ = 2πw on a standard track not depend on the radius of the inner curve?",
                            "ideal_answer": "Because the difference in perimeters is 2π(r + w) - 2πr = 2πr + 2πw - 2πr = 2πw. The radius term cancels out completely.",
                            "socratic_hint": "Expand 2π(r + w) and subtract 2πr."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "A circular wire of radius 14 cm is cut and bent into the shape of a square. Find the side length of the square.",
                            "ideal_answer": "Perimeter of wire = 2πr = 2 * (22/7) * 14 = 88 cm. Perimeter of square = 4s = 88 cm => Side s = 88 / 4 = 22 cm.",
                            "socratic_hint": "The length of wire remains constant: equate circle circumference to square perimeter."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "How many times does a wheel of radius 35 cm rotate in covering a distance of 154 metres?",
                            "ideal_answer": "Circumference = 2 * (22/7) * 35 = 220 cm = 2.2 m. Revolutions = 154 / 2.2 = 70 revolutions.",
                            "socratic_hint": "Divide total distance by the circumference of the wheel."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Two circles have concentric perimeters. The difference between their radii is 7 cm and the difference between their circumferences is 44 cm. Verify whether this relationship holds for any pair of circles where r_2 - r_1 = 7 cm.",
                            "ideal_answer": "C_2 - C_1 = 2πr_2 - 2πr_1 = 2π(r_2 - r_1) = 2 * (22/7) * 7 = 44 cm. Yes, it holds universally for ANY two concentric circles whose radii differ by 7 cm.",
                            "socratic_hint": "Factor out 2π from the difference of circumferences."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 2: Plane Polygon Areas, Heron's Formula & Trapeziums
    # -------------------------------------------------------------
    m2_svg = build_heron_triangle_svg(
        a=13, b=14, c=15,
        title="Heron's Formula: Triangle with Sides 13, 14, 15",
        caption="Semi-perimeter s = 21 cm. Area = √[21 × 8 × 7 × 6] = √7056 = 84 cm²"
    )

    m2 = {
        "order_index": 2,
        "title": "Planar Polygon Areas: Heron’s Formula, Trapezium Altitudes & Median Triangulations",
        "description": "Calculate areas of non-right triangles using Heron's Formula Area = √[s(s-a)(s-b)(s-c)]. Deduce heights and areas of isosceles trapeziums without trigonometric functions. Prove that a median bisects a triangle into two equal areas.",
        "subtopics": [
            "Limitations of Area = (1/2)*base*height when the altitude is unknown",
            "Derivation and statement of Heron's Formula for any triangle with sides a, b, c",
            "Semi-perimeter concept: s = (a + b + c) / 2",
            "Calculating the altitude to the longest side using Heron's Area: h = 2*Area / base",
            "Isosceles trapezium area: decomposing into a central rectangle and two congruent right triangles",
            "Median Area Invariant: A median divides a triangle into two triangles of equal area"
        ],
        "key_concepts": [
            "Heron's Area Formula: Area = √[s(s - a)(s - b)(s - c)] where s = (a + b + c)/2. Works for any triangle with known side lengths without needing an angle or perpendicular height.",
            "Altitude Extraction via Area: Once the area A is found from Heron's formula, the perpendicular height corresponding to any side b is given by h_b = 2A / b.",
            "Trapezium Height Extraction: In an isosceles trapezium with parallel sides a and b (a > b) and equal non-parallel sides c, the base of each flanking right triangle is (a - b)/2. The height is h = √[c^2 - ((a - b)/2)^2]. Area = (1/2)(a + b)h.",
            "Median Area Bisection Theorem: In triangle ABC with median AD, Area(triangle ABD) = Area(triangle ACD) because both triangles share the exact same base length (BD = DC) and the exact same perpendicular height from vertex A."
        ],
        "success_criteria": "Apply Heron's formula accurately, compute heights of trapeziums, and prove median area bisection.",
        "chapter_notes": "Break down prime factorizations under the square root in Heron's formula instead of computing huge products like 7056 directly.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 6.2 Q3: Find the area of a triangle whose sides are 13 cm, 14 cm, and 15 cm. Also find the length of the altitude to the longest side.",
                "given": "Triangle with side lengths a = 13 cm, b = 14 cm, c = 15 cm.",
                "formula": "Heron's Formula: s = (a + b + c)/2, Area = sqrt[s(s-a)(s-b)(s-c)]. Altitude h = 2*Area / base.",
                "substitution": "s = (13 + 14 + 15)/2 = 42/2 = 21 cm. Factors: s-a = 8, s-b = 7, s-c = 6.",
                "calculation": "Step 1: Compute semi-perimeter:\\n  s = (13 + 14 + 15) / 2 = 42 / 2 = 21 cm.\\nStep 2: Compute individual differences:\\n  s - a = 21 - 13 = 8 cm\\n  s - b = 21 - 14 = 7 cm\\n  s - c = 21 - 15 = 6 cm.\\nStep 3: Substitute into Heron's Formula:\\n  Area = sqrt[21 * 8 * 7 * 6].\\nStep 4: Factorize under the square root into prime powers:\\n  21 = 3 * 7\\n  8 = 2^3\\n  7 = 7\\n  6 = 2 * 3\\n  Product = (3 * 7) * (2^3) * 7 * (2 * 3) = 2^4 * 3^2 * 7^2.\\nStep 5: Extract square root:\\n  Area = 2^2 * 3 * 7 = 4 * 3 * 7 = 84 cm^2.\\nStep 6: Compute altitude to longest side (c = 15 cm):\\n  Area = (1/2) * base * height\\n  84 = (1/2) * 15 * h\\n  h = (2 * 84) / 15 = 168 / 15 = 11.2 cm.",
                "finalAnswer": "Area = 84 cm^2; Altitude to longest side = 11.2 cm",
                "unit": "square centimetres and centimetres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m2_svg
            },
            {
                "problem": "Textbook Exercise 6.2 Q2: The parallel sides of a trapezium are 40 cm and 20 cm. If its non-parallel sides are both equal, each being 26 cm, find the area of the trapezium.",
                "given": "Isosceles trapezium: Parallel sides a = 40 cm, b = 20 cm. Equal non-parallel sides c = 26 cm.",
                "formula": "Height h = sqrt[c^2 - ((a - b)/2)^2]. Area = (1/2) * (a + b) * h.",
                "substitution": "Base offset = (40 - 20) / 2 = 20 / 2 = 10 cm. h = sqrt(26^2 - 10^2).",
                "calculation": "Step 1: Draw altitudes from the ends of the shorter parallel side (20 cm) down to the longer parallel side (40 cm).\\nStep 2: This partitions the 40 cm base into three segments:\\n  A middle rectangle of base 20 cm, and two flanking right triangles of base x = (40 - 20)/2 = 10 cm each.\\nStep 3: In each right triangle, the hypotenuse is 26 cm and one leg is 10 cm:\\n  h^2 + 10^2 = 26^2\\n  h^2 + 100 = 676\\n  h^2 = 576\\n  h = sqrt(576) = 24 cm.\\nStep 4: Compute area of the trapezium:\\n  Area = (1/2) * (sum of parallel sides) * height\\n  Area = (1/2) * (40 + 20) * 24\\n  Area = (1/2) * 60 * 24 = 30 * 24 = 720 cm^2.",
                "finalAnswer": "Area of trapezium = 720 cm^2 (Height = 24 cm)",
                "unit": "square centimetres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Attempting to multiply 21 * 8 * 7 * 6 directly into 7056 and making multiplication or long division square root errors instead of pairing prime factors.",
            "Using the non-parallel side length (26 cm) directly as the height in the trapezium area formula."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Teach prime factor pairing under the square root for Heron's formula. Show that every factor pairs up nicely in textbook problems. Call write_chalkboard(action='draw_svg_diagram', content='Heron Triangle Area').",
        "visual_lesson_plan": {
            "title": "Heron's Formula & Trapezium Altitudes",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Triangle with sides 13, 14, 15 and altitude to base.",
            "concept_visuals": [
                {
                    "concept_title": "Heron's Area Calculation",
                    "diagram_title": "Triangle (13, 14, 15) Area",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m2_svg,
                    "interactive_math_formula": "Area = sqrt[s(s-a)(s-b)(s-c)]",
                    "mafs_graph_config": {"domain": [-1, 16], "range": [-1, 14]},
                    "image_query": "Heron formula triangle area semiperimeter proof diagram",
                    "video_query": "Herons formula area of a triangle step by step proof",
                    "image_url": "/images/curriculum/ch6_heron_triangle.png",
                    "what_to_make": "Triangle with side labels and semiperimeter calculation.",
                    "what_to_explain": "Walk through factor pairing: 2^4 * 3^2 * 7^2.",
                    "timing_and_cue": "Show during prime factorization step."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Heron's Formula & Polygons",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "In Heron's formula, if sides are in cm, what are the units of s?",
                            "ideal_answer": "cm (centimetres), because s is a length (semi-perimeter).",
                            "socratic_hint": "Is s a length or an area?"
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What happens to Heron's formula if the triangle is degenerate (i.e., a + b = c)?",
                            "ideal_answer": "Then s - c = 0, so the area becomes 0, correctly indicating that three collinear points enclose zero area.",
                            "socratic_hint": "What is the value of s - c when c = a + b?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Find the area of an equilateral triangle with side length 8 cm using Heron's formula.",
                            "ideal_answer": "s = (8+8+8)/2 = 12. s - a = 4. Area = sqrt[12 * 4 * 4 * 4] = sqrt[3 * 4 * 64] = 16 * sqrt(3) cm^2.",
                            "socratic_hint": "Compute s = 12 and (s - 8) = 4 for all three sides."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "A trapezium has parallel sides 10 cm and 20 cm and height 6 cm. What is its area?",
                            "ideal_answer": "Area = (1/2) * (10 + 20) * 6 = (1/2) * 30 * 6 = 90 cm^2.",
                            "socratic_hint": "Use Area = (1/2)(a + b)h."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "The perimeter of a triangular park is 300 m and its sides are in the ratio 3 : 5 : 7. Find its area.",
                            "ideal_answer": "Let sides be 3x, 5x, 7x. 3x + 5x + 7x = 300 => 15x = 300 => x = 20 m. Sides: a = 60 m, b = 100 m, c = 140 m. s = 150 m. Area = sqrt[150 * (150-60) * (150-100) * (150-140)] = sqrt[150 * 90 * 50 * 10] = sqrt[150 * 50 * 900] = sqrt[7500 * 900] = sqrt[25 * 300 * 900] = 5 * 30 * 10 * sqrt(3) = 1500 * sqrt(3) m^2 approx 2598 m^2.",
                            "socratic_hint": "Find the side lengths using the ratio, then compute semi-perimeter s = 150 m."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 3: Sectors, Segments, Quadrants & Clock Sweeps
    # -------------------------------------------------------------
    m3_svg = get_svg_wrapper(
        '<circle cx="290" cy="180" r="100" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,3"/>'
        '<path d="M 290 180 L 390 180 A 100 100 0 0 0 340 93.4 Z" fill="rgba(37,99,235,0.18)" stroke="#2563EB" stroke-width="2"/>'
        '<line x1="290" y1="180" x2="390" y2="180" stroke="#2563EB" stroke-width="2"/>'
        '<line x1="290" y1="180" x2="340" y2="93.4" stroke="#2563EB" stroke-width="2"/>'
        '<line x1="390" y1="180" x2="340" y2="93.4" stroke="#DC2626" stroke-width="2"/>'
        '<circle cx="290" cy="180" r="4" fill="#0F172A"/>'
        '<text x="275" y="195" fill="#0F172A" font-size="12" font-weight="700">O</text>'
        '<text x="398" y="185" fill="#2563EB" font-size="12" font-weight="700">A</text>'
        '<text x="345" y="85" fill="#2563EB" font-size="12" font-weight="700">B</text>'
        '<text x="320" y="160" fill="#2563EB" font-size="11" font-weight="700">θ = 60°</text>'
        '<text x="365" y="130" fill="#DC2626" font-size="10" font-weight="700">Segment</text>',
        title="Circular Sector & Segment Geometry (r = 7 cm, θ = 60°)",
        caption="Sector Area = (θ/360)πr² = 77/3 cm². Segment Area = Sector Area - Triangle OAB Area"
    )

    m3 = {
        "order_index": 3,
        "title": "Circle Sectors & Segments: Fractional Areas, Arc Lengths & Clock Hand Sweeps",
        "description": "Formulate sectors and segments of circles. Derive sector area A = (θ/360)πr² and arc length l = (θ/360)2πr. Calculate minor and major segment areas by subtracting triangle areas, and solve real-world clock sweep problems.",
        "subtopics": [
            "Definition of sector (region enclosed by two radii and an arc)",
            "Definition of segment (region enclosed by a chord and an arc)",
            "Derivation of Sector Area formula: Proportion of full 360-degree circle",
            "Derivation of Arc Length formula: l = (θ/360) * 2πr",
            "Minor segment area: Area(Sector) - Area(Triangle OAB)",
            "Area swept by the minute hand of a clock: Rate of 6 degrees per minute"
        ],
        "key_concepts": [
            "Proportionality Principle: A sector with central angle θ represents exactly the fraction (θ / 360) of the entire circle's area πr².",
            "Arc Length Formula: The curved boundary of a sector is l = (θ / 360) * 2πr. Notice that Area = (1/2) * l * r.",
            "Segment Area Decomposition: Area(Minor Segment) = Area(Sector OAB) - Area(Triangle OAB). For θ = 60 deg, triangle OAB is equilateral with area (√3 / 4)r²; for θ = 90 deg, it is a right triangle with area (1/2)r².",
            "Clock Angular Speed Invariant: The minute hand travels 360 degrees in 60 minutes, which is exactly 6 degrees per minute. In t minutes, the angle swept is θ = 6t degrees."
        ],
        "success_criteria": "Calculate sector areas, arc lengths, segment areas, and areas swept by rotating hands of a clock.",
        "chapter_notes": "Students often forget to subtract the triangle area when calculating the area of a segment. Make the distinction between sector (pie slice) and segment (bread crust) vivid.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 6.3 Q1 & Q2: (Q1) Find the area of a sector of a circle with radius 7 cm if the angle of the sector is 60 deg. (Q2) Find the area of a quadrant of a circle whose circumference is 44 cm.",
                "given": "Q1: r = 7 cm, θ = 60 deg. Q2: Circumference C = 44 cm, Quadrant means θ = 90 deg.",
                "formula": "Sector Area = (θ / 360) * πr².",
                "substitution": "Q1: (60 / 360) * (22/7) * 7²; Q2: C = 44 => r = 7 cm. Area = (1/4) * (22/7) * 7².",
                "calculation": "Part (Q1):\\nStep 1: Apply sector formula:\\n  Area = (60 / 360) * (22/7) * (7)^2\\nStep 2: Simplify fraction:\\n  60 / 360 = 1 / 6\\nStep 3: Simplify product:\\n  Area = (1 / 6) * (22/7) * 49 = (1 / 6) * (22 * 7) = (1 / 6) * 154 = 154 / 6 = 77 / 3 cm^2 approx 25.67 cm^2.\\n\\nPart (Q2):\\nStep 1: Find radius from circumference:\\n  2πr = 44 => 2 * (22/7) * r = 44 => r = 7 cm.\\nStep 2: A quadrant is a sector of angle 90 deg (one-fourth of circle):\\n  Area = (1/4) * πr² = (1/4) * (22/7) * 49 = (1/4) * 154 = 38.5 cm^2.",
                "finalAnswer": "Q1: 77/3 cm^2 (approx 25.67 cm^2); Q2: 38.5 cm^2",
                "unit": "square centimetres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m3_svg
            },
            {
                "problem": "Textbook Exercise 6.3 Q3: The length of the minute hand of a clock is 14 cm. Find the area swept by the minute hand in 5 minutes.",
                "given": "Radius r = length of minute hand = 14 cm. Time elapsed = 5 minutes.",
                "formula": "Angular speed of minute hand = 360 deg / 60 min = 6 deg/min. Sector Area = (θ / 360) * πr².",
                "substitution": "θ = 5 * 6 deg = 30 deg. r = 14 cm. Area = (30 / 360) * (22/7) * (14)^2.",
                "calculation": "Step 1: Calculate angle swept in 5 minutes:\\n  In 60 minutes, the hand sweeps 360 deg.\\n  In 1 minute, it sweeps 360 / 60 = 6 deg.\\n  In 5 minutes, θ = 5 * 6 = 30 deg.\\nStep 2: Calculate sector area:\\n  Area = (30 / 360) * (22/7) * (14 * 14)\\nStep 3: Simplify fraction:\\n  30 / 360 = 1 / 12\\nStep 4: Compute area:\\n  Area = (1 / 12) * (22 * 2 * 14) = (1 / 12) * 616 = 616 / 12 = 154 / 3 cm^2 approx 51.33 cm^2.",
                "finalAnswer": "Area swept in 5 minutes = 154/3 cm^2 (approx 51.33 cm^2)",
                "unit": "square centimetres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Calculating the hour hand speed instead of the minute hand. The hour hand moves at 0.5 degrees per minute, while the minute hand moves at 6 degrees per minute.",
            "Confusing sector (pie slice) with segment (region between chord and arc)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Use a physical clock dial to show how 5 minutes corresponds to the number 1 on the dial, which is 30 degrees (360/12). Call write_chalkboard(action='draw_svg_diagram', content='Circular Sector & Segment').",
        "visual_lesson_plan": {
            "title": "Sectors, Segments & Clock Geometry",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Circle with sector, triangle, and segment shaded.",
            "concept_visuals": [
                {
                    "concept_title": "Sector and Segment Decomposition",
                    "diagram_title": "Sector vs Segment",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m3_svg,
                    "interactive_math_formula": "Area_segment = Area_sector - Area_triangle",
                    "mafs_graph_config": {"domain": [-5, 5], "range": [-5, 5]},
                    "image_query": "Area of sector and segment of circle geometry diagram",
                    "video_query": "Area of sector and segment of a circle explained",
                    "image_url": "/images/curriculum/ch6_sector_segment.png",
                    "what_to_make": "Circle showing sector and segment distinction.",
                    "what_to_explain": "Walk through Area_segment = Area_sector - Area_triangle.",
                    "timing_and_cue": "Show before deriving segment formula."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Sectors & Segments",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What angle does the minute hand of a clock sweep in 15 minutes?",
                            "ideal_answer": "90 degrees, because 15 * 6 = 90 degrees.",
                            "socratic_hint": "Multiply 15 minutes by 6 degrees per minute."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What is the relation between the area of a sector of a circle and its arc length l?",
                            "ideal_answer": "Area = (1/2) * l * r, analogous to the area of a triangle with base l and height r.",
                            "socratic_hint": "Compare (θ/360)*πr² with (1/2) * [(θ/360)*2πr] * r."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Find the arc length of a sector of radius 21 cm with angle 60 deg.",
                            "ideal_answer": "l = (60/360) * 2 * (22/7) * 21 = (1/6) * 132 = 22 cm.",
                            "socratic_hint": "Use l = (θ/360) * 2πr."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "In a circle of radius 10 cm, a chord subtends a right angle at the centre. Find the area of the minor segment. (Use π = 3.14)",
                            "ideal_answer": "Sector Area = (90/360) * 3.14 * 100 = 78.5 cm^2. Triangle Area = (1/2) * 10 * 10 = 50 cm^2. Minor Segment Area = 78.5 - 50 = 28.5 cm^2.",
                            "socratic_hint": "Subtract the area of the right triangle from the quarter-circle area."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "A chord of a circle of radius 12 cm subtends an angle of 120 deg at the centre. Find the area of the corresponding segment of the circle. (Use π = 3.14 and √3 = 1.732)",
                            "ideal_answer": "Sector Area = (120/360) * 3.14 * 144 = 1/3 * 452.16 = 150.72 cm^2. Triangle Area = 1/2 * r^2 * sin(120 deg) = 1/2 * 144 * (√3/2) = 36 * 1.732 = 62.35 cm^2. Segment Area = 150.72 - 62.35 = 88.37 cm^2.",
                            "socratic_hint": "Calculate the sector area, then find the triangle area using altitude or (1/2)r^2 sin(120 deg)."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 4: Brahmagupta's Formula & Hippocrates' Lunes
    # -------------------------------------------------------------
    m4_svg = get_svg_wrapper(
        '<rect x="190" y="80" width="200" height="200" fill="#F8FAFC" stroke="#0F172A" stroke-width="2"/>'
        '<path d="M 190 180 A 100 100 0 0 1 390 180 A 100 100 0 0 1 190 180 Z" fill="rgba(37,99,235,0.15)"/>'
        '<path d="M 290 80 A 100 100 0 0 1 290 280 A 100 100 0 0 1 290 80 Z" fill="rgba(16,185,129,0.15)"/>'
        '<text x="290" y="65" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">Four-Petal Flower in Square</text>'
        '<text x="290" y="310" fill="#64748B" font-size="11" text-anchor="middle">Area of 4 Petals = 2 × (π/2 - 1) a² ≈ 0.5708 a²</text>',
        title="Brahmagupta's Formula, Hippocrates' Lunes & Four-Petal Flowers",
        caption="Higher-order curved area calculations in Ganita Manjari Chapter 6"
    )

    m4 = {
        "order_index": 4,
        "title": "Higher-Order Geometry: Brahmagupta’s Formula, Hippocrates’ Lunes & Shaded Semicircular Petals",
        "description": "Explore ancient Indian and Greek geometric triumphs: Brahmagupta's formula for the area of a cyclic quadrilateral, Hippocrates' proof that the area of two circular lunes equals the area of an inscribed right triangle, and four-petal flower shading inside squares.",
        "subtopics": [
            "Brahmagupta's Theorem: Area = √[(s-a)(s-b)(s-c)(s-d)] for cyclic quadrilaterals",
            "Why Brahmagupta's formula reduces directly to Heron's formula when d = 0",
            "Hippocrates' Lunes: The first exact geometric quadrature of a curved area",
            "Proof that the area of the two crescent lunes equals the area of the right triangle",
            "Four-petal flower inside a square of side a formed by four semicircles",
            "Exact calculation of the shaded petal area: (π - 2)/2 * a^2"
        ],
        "key_concepts": [
            "Brahmagupta's Area Formula: For any cyclic quadrilateral with sides a, b, c, d and semi-perimeter s = (a + b + c + d)/2, Area = √[(s - a)(s - b)(s - c)(s - d)].",
            "Heron-Brahmagupta Continuity: If one side shrinks to length zero (d = 0), the cyclic quadrilateral becomes a triangle inscribed in a circle, and Brahmagupta's formula smoothly degenerates into Heron's formula: √[s(s - a)(s - b)(s - c)].",
            "Hippocrates' Quadrature Invariant: By the Pythagorean theorem, the semicircle on the hypotenuse has an area equal to the sum of the semicircles on the two legs. Subtracting the circular segments proves that the sum of the areas of the two crescent lunes is IDENTICALLY EQUAL to the area of the right triangle!",
            "Four-Petal Flower Formula: Semicircles drawn on all 4 sides of a square overlap to create 4 petals. Total petal area = 2 * (Area of 4 semicircles) - Area of Square = 2 * [2 * (1/2)π(a/2)²] - a² = (π - 2)/2 * a² ≈ 0.5708 a²."
        ],
        "success_criteria": "Calculate areas of cyclic quadrilaterals using Brahmagupta's formula, prove Hippocrates' lunes theorem, and solve composite petal designs.",
        "chapter_notes": "Hippocrates' lunes and Brahmagupta's formula connect Grade 9 geometry to the profound history of mathematics. Students find the exact equivalence of curved lunes to a flat triangle astonishing.",
        "worked_examples": [
            {
                "problem": "Brahmagupta's Formula Application: A cyclic quadrilateral has side lengths a = 3 cm, b = 4 cm, c = 5 cm, and d = 6 cm. Calculate its exact area.",
                "given": "Cyclic quadrilateral with sides a = 3 cm, b = 4 cm, c = 5 cm, d = 6 cm.",
                "formula": "Brahmagupta's Formula: s = (a + b + c + d)/2, Area = sqrt[(s-a)(s-b)(s-c)(s-d)].",
                "substitution": "s = (3 + 4 + 5 + 6)/2 = 18/2 = 9 cm. Differences: 9-3=6, 9-4=5, 9-5=4, 9-6=3.",
                "calculation": "Step 1: Compute semi-perimeter:\\n  s = (3 + 4 + 5 + 6) / 2 = 18 / 2 = 9 cm.\\nStep 2: Compute differences:\\n  s - a = 9 - 3 = 6\\n  s - b = 9 - 4 = 5\\n  s - c = 9 - 5 = 4\\n  s - d = 9 - 6 = 3.\\nStep 3: Substitute into Brahmagupta's Formula:\\n  Area = sqrt[6 * 5 * 4 * 3].\\nStep 4: Factorize under the radical:\\n  6 * 5 * 4 * 3 = (2 * 3) * 5 * (2^2) * 3 = 2^3 * 3^2 * 5 = 8 * 9 * 5 = 360.\\nStep 5: Simplify square root:\\n  Area = sqrt[36 * 10] = 6 * sqrt(10) cm^2 approx 6 * 3.162 = 18.97 cm^2.",
                "finalAnswer": "Area = 6*sqrt(10) cm^2 (approx 18.97 cm^2)",
                "unit": "square centimetres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m4_svg
            },
            {
                "problem": "End-of-Chapter Curved Composite Problem: Semicircles are drawn on each of the four sides of a square of side 14 cm as diameters. Find the area of the four-petal flower formed inside the square. (Use π = 22/7)",
                "given": "Square of side a = 14 cm. Semicircles on all 4 sides with radius r = 14/2 = 7 cm.",
                "formula": "Area of 4 Petals = Area of 4 Semicircles - Area of Square.",
                "substitution": "Area of 4 semicircles = 4 * (1/2) * (22/7) * (7)^2. Area of square = 14^2.",
                "calculation": "Step 1: Calculate area of the square:\\n  Area_square = a^2 = 14 * 14 = 196 cm^2.\\nStep 2: Calculate area of one semicircle of diameter 14 cm (radius 7 cm):\\n  Area_semicircle = (1/2) * π * r^2 = (1/2) * (22/7) * 49 = 11 * 7 = 77 cm^2.\\nStep 3: Total area of all 4 semicircles:\\n  Total_semicircles = 4 * 77 = 308 cm^2.\\nStep 4: The 4 semicircles completely cover the square, and their overlaps form the 4 shaded petals:\\n  Area of 4 Petals = Total area of 4 semicircles - Area of square\\n  Area of 4 Petals = 308 - 196 = 112 cm^2.",
                "finalAnswer": "Area of four-petal flower = 112 cm^2",
                "unit": "square centimetres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Attempting to apply Brahmagupta's formula to a non-cyclic quadrilateral. It is strictly valid ONLY for cyclic quadrilaterals!",
            "Double-counting petal overlaps in composite flower problems."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Teach the inclusion-exclusion principle with overlapping areas. When four semicircles are added together, the petals are counted twice while the blank corners are counted once, so subtracting the square isolates the petals. Call write_chalkboard(action='draw_svg_diagram', content='Four-Petal Flower').",
        "visual_lesson_plan": {
            "title": "Brahmagupta & Curved Composite Areas",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Square with four overlapping semicircles forming flower petals.",
            "concept_visuals": [
                {
                    "concept_title": "Four-Petal Flower Dissection",
                    "diagram_title": "Four-Petal Shaded Region",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m4_svg,
                    "interactive_math_formula": "Area = 4*Area_semicircle - Area_square = 112 cm^2",
                    "mafs_graph_config": {"domain": [-1, 15], "range": [-1, 15]},
                    "image_query": "Area of four petal flower shaded region inside square geometry",
                    "video_query": "Area of shaded flower petals in a square math trick",
                    "image_url": "/images/curriculum/ch6_four_petals.png",
                    "what_to_make": "Square with shaded petals and unshaded corner regions.",
                    "what_to_explain": "Walk through Inclusion-Exclusion: 4 * 77 - 196 = 112 cm^2.",
                    "timing_and_cue": "Show before flower petal calculation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Advanced Curved Areas",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "Can Brahmagupta's formula be applied to find the area of an arbitrary non-cyclic rhombus?",
                            "ideal_answer": "No, Brahmagupta's formula holds only for cyclic quadrilaterals (a rhombus is only cyclic if it is a square).",
                            "socratic_hint": "Are all quadrilaterals cyclic?"
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What is the remarkable geometric conclusion of Hippocrates' lunes theorem?",
                            "ideal_answer": "That the sum of the areas of two curved crescent lunes equals the exact rectilinear area of the inscribed right-angled triangle.",
                            "socratic_hint": "What simple flat polygon does the area of the curved crescents equal?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "If a cyclic quadrilateral has sides 2, 3, 4, and 5 cm, find its semi-perimeter s.",
                            "ideal_answer": "s = (2 + 3 + 4 + 5) / 2 = 14 / 2 = 7 cm.",
                            "socratic_hint": "Sum all four sides and divide by 2."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "In a square of side 10 cm, find the unshaded corner area when 4 semicircles form a 4-petal flower. (Use π = 3.14)",
                            "ideal_answer": "Area of petals = 2 * (3.14/2 - 1) * 100 = 2 * 0.57 * 100 = 57 cm^2. Corner unshaded area = 100 - 57 = 43 cm^2.",
                            "socratic_hint": "Subtract the petal area from the total square area."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Show that the maximum area of a quadrilateral with given sides a, b, c, d is achieved when the quadrilateral is cyclic.",
                            "ideal_answer": "By Bretschneider's formula, the area of any quadrilateral is sqrt[(s-a)(s-b)(s-c)(s-d) - abcd*cos^2((A+C)/2)]. Since cos^2 is non-negative, the area is maximized when the subtracted term is zero: cos((A+C)/2) = 0 => (A+C)/2 = 90 deg => A + C = 180 deg, which is the exact condition for the quadrilateral to be cyclic (Brahmagupta's formula).",
                            "socratic_hint": "Recall that opposite angles in a cyclic quadrilateral sum to 180 degrees."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 5: Textbook Exercise Solver 1: Ex 6.1 & 6.2
    # -------------------------------------------------------------
    m5_svg = build_running_track_svg(
        title="Exercise Solver 1: Perimeters, Wheels, Tracks & Trapeziums",
        caption="Full step-by-step solutions for Exercises 6.1 and 6.2 with complete working"
    )

    m5 = {
        "order_index": 5,
        "title": "Textbook Exercise Solver 1: Exercises 6.1 & 6.2 (Circumference, Tracks & Heron’s Area)",
        "description": "Complete step-by-step solutions for every problem in Exercise 6.1 (circle perimeters, rolling wheel revolutions, and track staggers) and Exercise 6.2 (trapezium areas, altitudes, and Heron's formula calculations) with zero skipped steps.",
        "subtopics": [
            "Exercise 6.1 Q1 & Q2: Exact circumference evaluations for radii 7 cm, 10 cm, 14 cm",
            "Exercise 6.1 Q3: Revolutions of rolling circular objects over long distances",
            "Exercise 6.1 Q4 & Q5: Multi-lane track staggers and inner/outer boundaries",
            "Exercise 6.2 Q1: Triangle area enclosed within rectangle boundaries",
            "Exercise 6.2 Q2: Isosceles trapezium height derivation and area calculation",
            "Exercise 6.2 Q3 to Q5: Heron's formula applications on scalene triangles"
        ],
        "key_concepts": [
            "Dimensional Accuracy Invariant: Every perimeter must be expressed in linear units (cm, m, km); every area must be expressed in square units (cm², m²).",
            "Unit Standardization: Convert all dimensions to identical units before multiplying or dividing (e.g. 1.1 km -> 110,000 cm).",
            "Height-Hypotenuse Separation: Never confuse the slant height (non-parallel side) with the vertical altitude."
        ],
        "success_criteria": "Solve every question in Exercises 6.1 and 6.2 with 100% accuracy and complete working.",
        "chapter_notes": "Make students write Given -> Formula -> Substitution -> Calculation -> Boxed Answer for every exercise problem.",
        "worked_examples": [
            {
                "problem": "Exercise 6.1 Q2: Calculate, correct to 3 significant figures, the circumference of a circle with: (i) radius 7 cm, (ii) radius 10 cm, (iii) radius 14 cm.",
                "given": "Radii: (i) r = 7 cm, (ii) r = 10 cm, (iii) r = 14 cm. Use π = 22/7 or 3.142.",
                "formula": "C = 2πr.",
                "substitution": "(i) 2 * (22/7) * 7; (ii) 2 * 3.1416 * 10; (iii) 2 * (22/7) * 14.",
                "calculation": "Part (i):\\nC = 2 * (22/7) * 7 = 44 cm (or 44.0 cm to 3 sig figs).\\n\\nPart (ii):\\nC = 2 * 3.14159 * 10 = 62.83 cm => 62.8 cm (to 3 sig figs).\\n\\nPart (iii):\\nC = 2 * (22/7) * 14 = 2 * 22 * 2 = 88 cm (or 88.0 cm to 3 sig figs).",
                "finalAnswer": "(i) 44.0 cm; (ii) 62.8 cm; (iii) 88.0 cm",
                "unit": "centimetres",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.2 Q1: In rectangle ABCD with length AB = 10 cm and width BC = 8 cm, E is a point on BC such that BE = 3 cm. Find the area of triangle ADE.",
                "given": "Rectangle ABCD: AB = 10 cm, BC = AD = 8 cm. Point E is on BC with BE = 3 cm, so EC = 8 - 3 = 5 cm.",
                "formula": "Area(triangle ADE) = Area(Rectangle ABCD) - Area(triangle ABE) - Area(triangle CDE).",
                "substitution": "Area_rect = 10 * 8 = 80 cm^2. Area(ABE) = 1/2 * 10 * 3. Area(CDE) = 1/2 * 10 * 5.",
                "calculation": "Step 1: Total area of rectangle ABCD = AB * BC = 10 * 8 = 80 cm^2.\\nStep 2: Area of right-angled triangle ABE:\\n  Area(ABE) = (1/2) * base * height = (1/2) * AB * BE = (1/2) * 10 * 3 = 15 cm^2.\\nStep 3: Area of right-angled triangle CDE:\\n  Since BC = 8 cm and BE = 3 cm, EC = 8 - 3 = 5 cm. CD = AB = 10 cm.\\n  Area(CDE) = (1/2) * CD * EC = (1/2) * 10 * 5 = 25 cm^2.\\nStep 4: Subtract right triangle areas from rectangle area:\\n  Area(triangle ADE) = Area(ABCD) - [Area(ABE) + Area(CDE)]\\n  Area(triangle ADE) = 80 - (15 + 25) = 80 - 40 = 40 cm^2.\\nStep 5: Alternatively, using base AD = 8 cm and perpendicular height = 10 cm:\\n  Area = (1/2) * 8 * 10 = 40 cm^2.",
                "finalAnswer": "Area of triangle ADE = 40 cm^2",
                "unit": "square centimetres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m5_svg
            }
        ],
        "common_misconceptions": [
            "Attempting to calculate triangle ADE without subtracting complementary corner triangles or failing to identify the altitude.",
            "Dropping significant figure requirements in Exercise 6.1 Q2."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Emphasize complementary subtraction: when finding the area of an awkward triangle inside a rectangle, finding the area of the corner right triangles and subtracting them from the total rectangle is foolproof. Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 1: Perimeters').",
        "visual_lesson_plan": {
            "title": "Exercise Solver 1 Solutions",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Rectangle ABCD with point E on BC and triangle ADE highlighted.",
            "concept_visuals": [
                {
                    "concept_title": "Complementary Area Method",
                    "diagram_title": "Triangle ADE in Rectangle",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m5_svg,
                    "interactive_math_formula": "Area = 80 - 15 - 25 = 40 cm^2",
                    "mafs_graph_config": {"domain": [-1, 12], "range": [-1, 10]},
                    "image_query": "Area of triangle inside rectangle complementary area geometry",
                    "video_query": "Find area of shaded triangle inside rectangle problem",
                    "image_url": "/images/curriculum/ch6_exercise_solver1.png",
                    "what_to_make": "Rectangle with triangle ADE.",
                    "what_to_explain": "Explain why Area = (1/2) * base * height = (1/2) * 8 * 10 = 40 cm^2.",
                    "timing_and_cue": "Display during complementary area calculation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Exercise Solver 1 Mastery",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the circumference of a circle with diameter 28 cm? (Use π = 22/7)",
                            "ideal_answer": "88 cm, because C = πd = (22/7) * 28 = 88 cm.",
                            "socratic_hint": "Multiply diameter 28 by 22/7."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why is the area of any triangle inscribed between parallel lines on the same base constant?",
                            "ideal_answer": "Because both the base length and the perpendicular distance (height) between the two parallel lines remain constant, and Area = (1/2)*base*height.",
                            "socratic_hint": "Does the perpendicular height change between parallel lines?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Find the area of a right-angled triangle whose hypotenuse is 10 cm and one leg is 6 cm.",
                            "ideal_answer": "Other leg = sqrt(10^2 - 6^2) = sqrt(100 - 36) = sqrt(64) = 8 cm. Area = (1/2) * 6 * 8 = 24 cm^2.",
                            "socratic_hint": "Find the third side using Pythagoras, then apply (1/2)*base*height."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "A runner on an 8-lane track runs in Lane 4. What is the radius of the curve in Lane 4 if the inner radius is 36.5 m and each lane is 1.22 m wide?",
                            "ideal_answer": "r_4 = r_1 + (4 - 1)*w = 36.5 + 3*(1.22) = 36.5 + 3.66 = 40.16 m.",
                            "socratic_hint": "Add 3 lane widths to the inner radius."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Find the perimeter of a semicircular protractor whose diameter is 14 cm. (Use π = 22/7)",
                            "ideal_answer": "Perimeter = curved boundary + straight diameter = πr + d = (22/7)*7 + 14 = 22 + 14 = 36 cm.",
                            "socratic_hint": "Remember that a closed protractor includes the flat diameter edge plus the curved semicircle!"
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 6: Textbook Exercise Solver 2: Ex 6.3 & Review
    # -------------------------------------------------------------
    m6_svg = get_svg_wrapper(
        '<circle cx="290" cy="180" r="100" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.5"/>'
        '<path d="M 290 180 L 390 180 A 100 100 0 0 0 290 80 Z" fill="rgba(245,158,11,0.2)" stroke="#F59E0B" stroke-width="2"/>'
        '<line x1="290" y1="180" x2="390" y2="180" stroke="#F59E0B" stroke-width="2"/>'
        '<line x1="290" y1="180" x2="290" y2="80" stroke="#F59E0B" stroke-width="2"/>'
        '<line x1="390" y1="180" x2="290" y2="80" stroke="#DC2626" stroke-width="2"/>'
        '<circle cx="290" cy="180" r="4" fill="#0F172A"/>'
        '<text x="270" y="195" fill="#0F172A" font-size="12" font-weight="700">O</text>'
        '<text x="398" y="185" fill="#F59E0B" font-size="12" font-weight="700">A</text>'
        '<text x="290" y="70" fill="#F59E0B" font-size="12" font-weight="700">B</text>'
        '<text x="350" y="125" fill="#DC2626" font-size="11" font-weight="700">Segment</text>',
        title="Exercise Solver 2: Sectors, Segments & End-of-Chapter Review",
        caption="Complete solutions for Exercise 6.3 and End-of-Chapter Q1 through Q12"
    )

    m6 = {
        "order_index": 6,
        "title": "Textbook Exercise Solver 2: Exercise 6.3 & End-of-Chapter Review (Q1 to Q12)",
        "description": "Comprehensive solutions for Exercise 6.3 (sectors, quadrants, minute hand areas) and End-of-Chapter synthesis questions Q1 through Q12 (composite flower beds, pasture grazing circles, and cyclic quad areas) with zero skipped steps.",
        "subtopics": [
            "Exercise 6.3 Q4 & Q5: Segment areas corresponding to chords subtending 60 deg and 90 deg",
            "End-of-Chapter Q1 to Q4: Algebraic identity areas and geometric dissections",
            "End-of-Chapter Q5 to Q8: Horse grazing in square fields with rope radius r",
            "End-of-Chapter Q9 & Q10: Circular brooch and umbrella wire ribs geometry",
            "End-of-Chapter Q11 & Q12: Brahmagupta's formula and Hippocrates' lunes problems"
        ],
        "key_concepts": [
            "Horse Grazing Problem Invariant: A horse tied with a rope of length r at the corner of a square field can graze an area equal to a QUADRANT: Area = (1/4)πr². If rope length increases from r_1 to r_2, the increase in grazing area is (1/4)π(r_2² - r_1²).",
            "Brooch Wire Length: A circular brooch made with silver wire has circumference 2πr plus 5 diameters (10 radii). Total wire length = 2πr + 5(2r) = 2πr + 10r.",
            "Umbrella Sector Distribution: An umbrella has 8 ribs forming 8 equal sectors. Each sector has central angle θ = 360 / 8 = 45 degrees. Area of each sector = (1/8)πr²."
        ],
        "success_criteria": "Solve every problem in Exercise 6.3 and End-of-Chapter Q1 to Q12 with full step-by-step working.",
        "chapter_notes": "The horse grazing problem and the silver brooch problem appear constantly on CBSE exams. Ensure students clearly distinguish between wire length (perimeter) and sector area.",
        "worked_examples": [
            {
                "problem": "End-of-Chapter Horse Grazing Problem: A horse is tied to a peg at one corner of a square grass field of side 15 m by means of a 5 m long rope. Find: (i) The area of that part of the field in which the horse can graze. (ii) The increase in the grazing area if the rope were 10 m long instead of 5 m. (Use π = 3.14)",
                "given": "Square field of side 15 m. Rope length r_1 = 5 m. Extended rope length r_2 = 10 m.",
                "formula": "Corner of square field has angle 90 deg. Grazing area = Area of quadrant = (1/4) * πr².",
                "substitution": "(i) Area_1 = (1/4) * 3.14 * (5)^2; (ii) Increase = Area_2 - Area_1 = (1/4) * 3.14 * (10^2 - 5^2).",
                "calculation": "Part (i):\\nStep 1: The corner of a square is a right angle (θ = 90 deg).\\nStep 2: The grazing region is a sector of angle 90 deg (a quadrant of radius 5 m):\\n  Area_1 = (90 / 360) * π * r_1^2 = (1/4) * 3.14 * 25\\n  Area_1 = 78.5 / 4 = 19.625 m^2.\\n\\nPart (ii):\\nStep 1: When rope is lengthened to r_2 = 10 m, the new grazing area is:\\n  Area_2 = (1/4) * 3.14 * (10)^2 = (1/4) * 314 = 78.5 m^2.\\nStep 2: Compute the increase in grazing area:\\n  Increase = Area_2 - Area_1 = 78.5 - 19.625 = 58.875 m^2.\\n(Alternatively: (1/4) * 3.14 * (100 - 25) = (1/4) * 3.14 * 75 = 235.5 / 4 = 58.875 m^2).",
                "finalAnswer": "(i) Grazing area = 19.625 m^2; (ii) Increase in grazing area = 58.875 m^2",
                "unit": "square metres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m6_svg
            },
            {
                "problem": "End-of-Chapter Silver Brooch Problem: A brooch is made with silver wire in the form of a circle with diameter 35 mm. The wire is also used in making 5 diameters which divide the circle into 10 equal sectors. Find: (i) The total length of the silver wire required. (ii) The area of each sector of the brooch. (Use π = 22/7)",
                "given": "Diameter d = 35 mm => Radius r = 35/2 mm. Number of diameters = 5. Number of sectors = 10.",
                "formula": "(i) Total Wire Length = Circumference + 5 * Diameter = πd + 5d. (ii) Sector Area = (1/10) * πr².",
                "substitution": "(i) Length = (22/7) * 35 + 5 * 35; (ii) Area = (1/10) * (22/7) * (35/2)^2.",
                "calculation": "Part (i):\\nStep 1: Compute circumference of brooch:\\n  C = π * d = (22/7) * 35 = 22 * 5 = 110 mm.\\nStep 2: Compute total length of 5 diameters:\\n  Length_diameters = 5 * d = 5 * 35 = 175 mm.\\nStep 3: Total silver wire length:\\n  Total = C + Length_diameters = 110 + 175 = 285 mm.\\n\\nPart (ii):\\nStep 1: The 5 diameters divide the circle into 10 equal sectors:\\n  Central angle θ = 360 / 10 = 36 deg (or 1/10 of the circle).\\nStep 2: Compute area of the full circle:\\n  Area_circle = π * r^2 = (22/7) * (35/2) * (35/2) = (11 * 5 * 35) / 2 = 1925 / 2 = 962.5 mm^2.\\nStep 3: Compute area of one sector:\\n  Area_sector = Area_circle / 10 = 962.5 / 10 = 96.25 mm^2 (or 385/4 mm^2).",
                "finalAnswer": "(i) Total wire length = 285 mm; (ii) Area of each sector = 385/4 mm^2 = 96.25 mm^2",
                "unit": "millimetres and square millimetres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting to add the 5 diameters to the outer circumference when calculating the total silver wire length.",
            "Using 15 m (field side) instead of the rope length (5 m or 10 m) as the radius in the horse grazing problem."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Teach students to read real-world word problems like architectural specifications. Break them down: What material forms the boundary? What forms the spokes? Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 2: Sectors').",
        "visual_lesson_plan": {
            "title": "Exercise Solver 2 Solutions",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Brooch with 10 sectors and horse grazing quadrant.",
            "concept_visuals": [
                {
                    "concept_title": "Real-World Circular Models",
                    "diagram_title": "Brooch & Grazing Quadrant",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m6_svg,
                    "interactive_math_formula": "Wire = pi*d + 5d = 285 mm",
                    "mafs_graph_config": {"domain": [-20, 20], "range": [-20, 20]},
                    "image_query": "Circular brooch with silver wire sectors math problem diagram",
                    "video_query": "Horse tied to peg square field area problem solved",
                    "image_url": "/images/curriculum/ch6_exercise_solver2.png",
                    "what_to_make": "Brooch with 5 diameters and horse grazing corner sector.",
                    "what_to_explain": "Walk through wire length calculation: 110 + 175 = 285 mm.",
                    "timing_and_cue": "Show before brooch calculation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Real-World Geometry Mastery",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "An umbrella has 8 ribs equally spaced. What is the central angle of each sector?",
                            "ideal_answer": "45 degrees, because 360 / 8 = 45 degrees.",
                            "socratic_hint": "Divide 360 degrees by 8."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "In the horse grazing problem, why does the side of the field (15 m) not affect the grazing area when the rope is 5 m?",
                            "ideal_answer": "Because the 5 m rope is shorter than the 15 m side, so the horse's movement is constrained entirely by the rope radius, not the field perimeter.",
                            "socratic_hint": "Can the horse reach the other corner with a 5 m rope?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Find the area of a sector of a circle of radius 6 cm whose central angle is 60 deg. (Use π = 3.14)",
                            "ideal_answer": "Area = (60/360) * 3.14 * 36 = (1/6) * 113.04 = 18.84 cm^2.",
                            "socratic_hint": "Apply Area = (θ/360)*πr²."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "A round table cover has 6 equal designs. If the radius is 28 cm, find the central angle of each design segment.",
                            "ideal_answer": "360 / 6 = 60 degrees per design segment.",
                            "socratic_hint": "Divide 360 degrees by 6."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "To warn ships for underwater rocks, a lighthouse spreads a red coloured light over a sector of angle 80 deg to a distance of 16.5 km. Find the area of the sea over which the ships are warned. (Use π = 3.14)",
                            "ideal_answer": "Area = (80 / 360) * 3.14 * (16.5)^2 = (2 / 9) * 3.14 * 272.25 = (2 / 9) * 854.865 = 1709.73 / 9 = 189.97 km^2.",
                            "socratic_hint": "Use sector area formula with θ = 80 deg and r = 16.5 km."
                        }
                    ]
                }
            ]
        }
    }

    return [m1, m2, m3, m4, m5, m6]
