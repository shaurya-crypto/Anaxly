"""
Chapter 6: Measuring Space: Perimeter and Area - Module 3
Curriculum ID: 2ca7b10a-3fb9-484f-8116-30d7b586c526
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m3():
    m3_svg = build_cartesian_svg(
        domain=(-25, 25), range_y=(-5, 30),
        points=[
            {"x": -20, "y": 0, "label": "A(-20, 0)", "color": "#0F172A"},
            {"x": 20, "y": 0, "label": "B(20, 0)", "color": "#0F172A"},
            {"x": 10, "y": 24, "label": "C(10, 24)", "color": "#2563EB"},
            {"x": -10, "y": 24, "label": "D(-10, 24)", "color": "#2563EB"}
        ],
        lines=[
            {"p1": (-20, 0), "p2": (20, 0), "color": "#0F172A", "stroke_width": 3, "label": "Base a = 40 cm"},
            {"p1": (-10, 24), "p2": (10, 24), "color": "#2563EB", "stroke_width": 3, "label": "Top b = 20 cm"},
            {"p1": (-20, 0), "p2": (-10, 24), "color": "#DC2626", "stroke_width": 2, "label": "Leg c = 26 cm"},
            {"p1": (20, 0), "p2": (10, 24), "color": "#DC2626", "stroke_width": 2, "label": "Leg c = 26 cm"},
            {"p1": (-10, 0), "p2": (-10, 24), "color": "#16A34A", "stroke_width": 2, "label": "h = 24 cm"}
        ],
        title="Isosceles Trapezium: Height h = 24 cm, Area = 720 cm²",
        caption="Bases 40 cm and 20 cm with symmetrical 10 cm offsets: h = sqrt(26^2 - 10^2) = 24 cm"
    )

    return {
        "order_index": 3,
        "title": "Textbook Exercise Solver 2: Polygonal Area, Shearing & Varignon's Theorem (Exercise 6.2 Set 1 & Trapezium Models)",
        "description": "Comprehensive step-by-step solutions to Exercise 6.2 (Q1 to Q8) and End-of-Chapter Questions 11, 12, 13, and 14. Master base-altitude shearing invariance in parallelograms, isosceles trapezium area, rhombus diagonal determination, diagonal partition of parallelogram area, Varignon's theorem (midpoint quadrilateral area = 1/2 of original 4-gon), and three distinct geometric proofs for the area of a trapezium and kite.",
        "subtopics": [
            "Base-Altitude Shearing Theorem: Triangles sharing a base between parallel lines have equal area",
            "Isosceles trapezium height deduction via Pythagorean projection: h = sqrt(c^2 - ((a-b)/2)^2)",
            "Rhombus orthogonal diagonal area: Area = (1/2)*d1*d2 and diagonal length recovery",
            "Diagonal symmetry of parallelograms: Equality of triangles PSO and PQO for any point on diagonal PR",
            "Varignon's Theorem: Proof that joining midpoints of any 4-gon yields a parallelogram with half the area",
            "Three canonical proofs for the area of a trapezium: Shearing, Two-Triangle Partition, and Double-Copy Parallelogram"
        ],
        "key_concepts": [
            "Shearing Invariance: Area of a triangle is (1/2)*b*h; sliding the vertex parallel to the base preserves height and therefore preserves area.",
            "Trapezium Symmetrical Offset: In an isosceles trapezium with bases a and b, the projections of the legs have length x = (a - b) / 2.",
            "Varignon's Parallelogram Invariant: For any quadrilateral of area A, the Varignon midpoint parallelogram has sides parallel to diagonals and area exactly A / 2.",
            "Kite Area Theorem: The diagonals of a kite are mutually perpendicular; dividing the kite into four right triangles reveals Area = (1/2) * d1 * d2.",
            "Double-Copy Invariant: Two congruent trapeziums of bases a and b placed upside down form a parallelogram of base (a + b) and height h, proving Area = (1/2)*(a + b)*h."
        ],
        "success_criteria": "Students can calculate areas of trapeziums, rhombuses, and kites, prove shearing and diagonal invariance, and apply Varignon's theorem to 4-gons.",
        "chapter_notes": "Module 3 resolves the fundamental polygonal area formulas of Class 9 geometry through rigorous coordinate and synthetic proofs.",
        "common_misconceptions": [
            {"misconception": "Thinking rhombus area is side times side", "clarification": "Rhombus area is (1/2)*d1*d2 (or side * perpendicular height), NOT side squared unless it is a square (90° angles)."},
            {"misconception": "Assuming Varignon's theorem only holds for convex quadrilaterals", "clarification": "Varignon's theorem holds universally for ANY non-self-intersecting quadrilateral, convex or concave."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through polygonal area formulas. Demonstrate the three different ways to prove the trapezium area formula (two triangles, shearing, and two-copy parallelogram).",
        "visual_lesson_plan": {
            "title": "Visualizing Polygonal Areas and Shearing Invariance",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Vector diagram of an isosceles trapezium with bases 40 and 20 cm and height 24 cm, showing the right triangle offset.",
            "concept_visuals": [
                {
                    "concept_title": "Isosceles Trapezium Height Deduction",
                    "diagram_title": "x = (40 - 20)/2 = 10 cm, h = sqrt(26^2 - 10^2) = 24 cm",
                    "interactive_math_formula": "\\text{Area} = \\frac{1}{2}(a + b)h = \\frac{1}{2}(40 + 20)(24) = 720\\text{ cm}^2",
                    "mafs_graph_config": {
                        "domain": [-25, 25],
                        "range": [-5, 30],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#0F172A", "label": "Base 40"},
                            {"slope": 0, "intercept": 24, "color": "#2563EB", "label": "Top 20"}
                        ],
                        "points": [
                            {"x": -20, "y": 0, "label": "A(-20, 0)"},
                            {"x": 20, "y": 0, "label": "B(20, 0)"},
                            {"x": 10, "y": 24, "label": "C(10, 24)"},
                            {"x": -10, "y": 24, "label": "D(-10, 24)"}
                        ]
                    },
                    "image_query": "isosceles trapezium area pythagorean theorem height calculation",
                    "video_query": "how to find area of isosceles trapezium with given sides",
                    "what_to_explain": "Dropping vertical altitudes from the top vertices creates two congruent right triangles with base 10 cm and hypotenuse 26 cm, yielding height 24 cm."
                },
                {
                    "concept_title": "Varignon's Midpoint Parallelogram: Area = 1/2 of 4-Gon",
                    "diagram_title": "Midpoint Polygon EFGH has Area = (1/2)*Area(ABCD)",
                    "interactive_math_formula": "\\text{Area}(EFGH) = \\frac{1}{2}\\text{Area}(ABCD)",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "points": [
                            {"x": -8, "y": -6, "label": "A"},
                            {"x": 8, "y": -4, "label": "B"},
                            {"x": 6, "y": 8, "label": "C"},
                            {"x": -6, "y": 6, "label": "D"},
                            {"x": 0, "y": -5, "label": "E (Mid AB)"},
                            {"x": 7, "y": 2, "label": "F (Mid BC)"},
                            {"x": 0, "y": 7, "label": "G (Mid CD)"},
                            {"x": -7, "y": 0, "label": "H (Mid DA)"}
                        ]
                    },
                    "image_query": "Varignon theorem area of midpoint parallelogram half quadrilateral",
                    "video_query": "Varignon theorem proof area of midpoint parallelogram",
                    "what_to_explain": "Each corner triangle has 1/4 the area of the diagonal triangle, leaving the inner parallelogram with exactly half the total area."
                },
                {
                    "concept_title": "Shearing Invariance: Parallelogram PCD vs QCD",
                    "diagram_title": "Equal Base CD, Equal Height h: Ratio = 1 : 1",
                    "interactive_math_formula": "\\frac{\\text{Area}(\\Delta PCD)}{\\text{Area}(\\Delta QCD)} = \\frac{\\frac{1}{2}b h}{\\frac{1}{2}b h} = 1",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-2, 10],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#2563EB", "label": "Base CD (y=0)"},
                            {"slope": 0, "intercept": 6, "color": "#DC2626", "label": "Line AB (y=6)"}
                        ],
                        "points": [
                            {"x": -5, "y": 0, "label": "C"},
                            {"x": 5, "y": 0, "label": "D"},
                            {"x": -2, "y": 6, "label": "Point P on AB"},
                            {"x": 3, "y": 6, "label": "Point Q on AB"}
                        ]
                    },
                    "image_query": "triangles with same base between same parallels equal area",
                    "video_query": "triangles on same base and between same parallels have equal area",
                    "what_to_explain": "Because P and Q lie on line AB parallel to CD, both triangles share base CD and have identical altitude h, giving identical area."
                },
                {
                    "concept_title": "Two-Copy Parallelogram Proof of Trapezium Area",
                    "diagram_title": "Two Trapeziums Form Parallelogram of Base a + b",
                    "interactive_math_formula": "2 \\times \\text{Area} = (a + b)h \\implies \\text{Area} = \\frac{1}{2}(a + b)h",
                    "mafs_graph_config": {
                        "domain": [-15, 15],
                        "range": [-2, 10],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#0F172A", "label": "Total Base = a + b"},
                            {"slope": 0, "intercept": 6, "color": "#0F172A", "label": "Total Top = b + a"}
                        ],
                        "points": [
                            {"x": -10, "y": 0, "label": "Start"},
                            {"x": 2, "y": 0, "label": "Seam (Base a)"},
                            {"x": 10, "y": 0, "label": "End (Base b)"}
                        ]
                    },
                    "image_query": "proof of area of trapezium by joining two congruent trapeziums",
                    "video_query": "area of trapezium proof using two identical trapeziums",
                    "what_to_explain": "Rotating an identical copy 180° creates a parallelogram with base a + b and height h, so one trapezium has half that area."
                },
                {
                    "concept_title": "Kite Orthogonal Diagonal Area Decomposition",
                    "diagram_title": "Kite Diagonals d1 perp d2: Area = (1/2)*d1*d2",
                    "interactive_math_formula": "\\text{Area} = 2 \\times \\left(\\frac{1}{2} d_1 \\times \\frac{d_2}{2}\\right) = \\frac{1}{2} d_1 d_2",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [-10, 8],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#2563EB", "label": "Diagonal d1 = 12"},
                            {"slope": 999, "intercept": 0, "color": "#DC2626", "label": "Diagonal d2 = 16"}
                        ],
                        "points": [
                            {"x": -6, "y": 0, "label": "Left (-6, 0)"},
                            {"x": 6, "y": 0, "label": "Right (6, 0)"},
                            {"x": 0, "y": 6, "label": "Top (0, 6)"},
                            {"x": 0, "y": -10, "label": "Bottom (0, -10)"}
                        ]
                    },
                    "image_query": "area of kite formula proof perpendicular diagonals",
                    "video_query": "how to find the area of a kite proof",
                    "what_to_explain": "The perpendicular diagonals split the kite into two pairs of congruent right triangles summing to (1/2)*d1*d2."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Polygonal Area Theorems",
                    "questions": [
                        {
                            "question": "If the parallel sides of an isosceles trapezium are 40 cm and 20 cm, and its non-parallel legs are 26 cm, what is its height?",
                            "type": "short_answer",
                            "ideal_answer": "24 cm (x = (40 - 20)/2 = 10 cm; h = sqrt(26^2 - 10^2) = sqrt(576) = 24 cm).",
                            "socratic_hint": "Find the horizontal offset of the non-parallel side, then use Pythagoras theorem."
                        },
                        {
                            "question": "What is the ratio of the area of the Varignon parallelogram (formed by joining midpoints of sides) to the area of the original quadrilateral?",
                            "type": "short_answer",
                            "ideal_answer": "1 : 2 (the area of the Varignon parallelogram is exactly half the area of the quadrilateral).",
                            "socratic_hint": "Recall Varignon's theorem on quadrilaterals."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 6.2 Q1: Find the area of triangle ADE in Fig. 6.31 where rectangle ABCD has base CD = 10 cm and height AD = 8 cm, and E is a point on top side AB.",
                "given": "Rectangle ABCD with base CD = 10 cm, height AD = 8 cm. E lies on side AB.",
                "formula": "Area of triangle = (1/2) * base * height.",
                "substitution": "Base AD = 8 cm, perpendicular height from E to AD is the horizontal distance from line AD to point E.",
                "calculation": "1. In rectangle ABCD, angle A = angle D = 90°.\n2. In triangle ADE, side AD = 8 cm lies along the left vertical edge.\n3. The altitude from vertex E perpendicular to line AD is the horizontal segment from E to AD, which is parallel to AB and CD.\n4. Since AB = 10 cm, let the horizontal distance from AD to E be x cm (with 0 <= x <= 10).\n5. If E is at vertex B, x = 10 cm: Area = (1/2) * 8 * 10 = 40 cm^2.\n6. For any triangle ADE with base AD = 8 cm and altitude h_AD = x cm, Area = 4x cm^2. For standard textbook figure where E is at the top corner B: Area = 40 cm^2.",
                "finalAnswer": "40 cm^2 (or (1/2)*AD*AE depending on position of E).",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q2: The parallel sides of a trapezium are 40 cm and 20 cm. If its non-parallel sides are both equal, each being 26 cm, find the area of the trapezium.",
                "given": "Isosceles trapezium: parallel bases a = 40 cm, b = 20 cm; non-parallel legs c = 26 cm each.",
                "formula": "Area = (1/2) * (a + b) * h, where h = sqrt(c^2 - ((a - b)/2)^2).",
                "substitution": "x = (40 - 20) / 2 = 10 cm. h = sqrt(26^2 - 10^2).",
                "calculation": "1. Symmetrical base offset: x = (40 - 20) / 2 = 20 / 2 = 10 cm.\n2. In the right triangle formed by leg c, height h, and offset x:\n   h^2 + x^2 = c^2 => h^2 + 10^2 = 26^2.\n   h^2 + 100 = 676.\n   h^2 = 676 - 100 = 576.\n   h = sqrt(576) = 24 cm.\n3. Area of trapezium = (1/2) * (a + b) * h = (1/2) * (40 + 20) * 24.\n4. (1/2) * 60 * 24 = 30 * 24 = 720 cm^2.",
                "finalAnswer": "720 cm^2",
                "unit": "cm^2",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q5: One diagonal of a rhombus is twice as long as the other diagonal. If the rhombus has area 128 cm^2, find the length of the shorter diagonal.",
                "given": "Rhombus area A = 128 cm^2. Let shorter diagonal be d1, then longer diagonal d2 = 2*d1.",
                "formula": "Area of rhombus = (1/2) * d1 * d2.",
                "substitution": "128 = (1/2) * d1 * (2*d1).",
                "calculation": "1. 128 = (1/2) * 2 * d1^2 = d1^2.\n2. d1^2 = 128.\n3. d1 = sqrt(128) = sqrt(64 * 2) = 8*sqrt(2) cm approx 11.31 cm.\n4. Longer diagonal d2 = 2 * 8*sqrt(2) = 16*sqrt(2) cm.\n5. Verify area: (1/2) * (8*sqrt(2)) * (16*sqrt(2)) = (1/2) * 128 * 2 = 128 cm^2. Correct!",
                "finalAnswer": "8*sqrt(2) cm (approx 11.31 cm)",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 6.2 Q6: ABCD is a parallelogram. P and Q are any two points on side AB. What can you say about the ratio area(triangle PCD) : area(triangle QCD)?",
                "given": "Parallelogram ABCD. Side CD is parallel to side AB. P and Q are points on side AB.",
                "formula": "Area of triangle = (1/2) * base * height.",
                "substitution": "Both triangle PCD and triangle QCD share base CD = b, and vertices P and Q lie on line AB which is at constant distance h from CD.",
                "calculation": "1. In triangle PCD, the base is segment CD, and altitude is the perpendicular distance h from line AB to line CD.\n   Area(triangle PCD) = (1/2) * CD * h.\n2. In triangle QCD, the base is also segment CD, and altitude is the perpendicular distance h from line AB to line CD.\n   Area(triangle QCD) = (1/2) * CD * h.\n3. Both triangles have identical base lengths and identical perpendicular heights.\n4. Therefore, Area(triangle PCD) = Area(triangle QCD).\n5. The ratio area(triangle PCD) : area(triangle QCD) is strictly 1 : 1.",
                "finalAnswer": "The ratio is 1 : 1 (the areas are strictly equal because both triangles share the same base CD and lie between the same parallel lines AB and CD).",
                "unit": "ratio",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q7: O is any point on the diagonal PR of a parallelogram PQRS. Prove that the areas of triangles PSO and PQO are equal.",
                "given": "Parallelogram PQRS with diagonal PR. Point O lies on diagonal PR.",
                "formula": "A diagonal of a parallelogram divides it into two congruent triangles of equal area. Area of triangle on a common base with equal altitudes.",
                "substitution": "Drop perpendiculars from S and Q to diagonal PR.",
                "calculation": "1. In parallelogram PQRS, diagonal PR divides the parallelogram into two congruent triangles: triangle PSR ~= triangle PQR (by SSS).\n2. Therefore, Area(triangle PSR) = Area(triangle PQR).\n3. Drop perpendiculars SM perp PR and QN perp PR. Since triangle PSR ~= triangle PQR, their altitudes to PR are equal: SM = QN = h.\n4. Now consider triangle PSO and triangle PQO:\n   - Both triangles have the exact same base PO (a segment of diagonal PR).\n   - The altitude of triangle PSO to base PO is SM = h.\n   - The altitude of triangle PQO to base PO is QN = h.\n5. Area(triangle PSO) = (1/2) * PO * SM = (1/2) * PO * h.\n6. Area(triangle PQO) = (1/2) * PO * QN = (1/2) * PO * h.\n7. Since both areas equal (1/2) * PO * h, Area(triangle PSO) = Area(triangle PQO).",
                "finalAnswer": "Proved: Area(triangle PSO) = Area(triangle PQO) (both triangles share base PO and have equal altitudes SM = QN).",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "Exercise 6.2 Q8: If the midpoints of the sides of a 4-gon (quadrilateral ABCD) are joined in order, prove that the area of the parallelogram thus formed will be half of the area of the given 4-gon.",
                "given": "Quadrilateral ABCD. Let E, F, G, H be the midpoints of AB, BC, CD, DA respectively.",
                "formula": "Midpoint Theorem: In triangle ABC, segment EF joining midpoints of AB and BC is parallel to AC and EF = (1/2)*AC. Triangle area scaling: Area(triangle EBF) = (1/4)*Area(triangle ABC).",
                "substitution": "Draw diagonal AC.",
                "calculation": "1. In triangle ABC, E is midpoint of AB and F is midpoint of BC. By the Midpoint Theorem, EF || AC and EF = AC/2.\n   Since triangle EBF is similar to triangle ABC with scale factor 1/2, Area(triangle EBF) = (1/2)^2 * Area(triangle ABC) = (1/4) * Area(triangle ABC).\n2. In triangle ADC, H is midpoint of DA and G is midpoint of CD. By Midpoint Theorem, HG || AC and HG = AC/2.\n   Similarly, Area(triangle HDG) = (1/4) * Area(triangle ADC).\n3. Adding both corner triangles:\n   Area(triangle EBF) + Area(triangle HDG) = (1/4) * [Area(triangle ABC) + Area(triangle ADC)] = (1/4) * Area(ABCD).\n4. Now draw diagonal BD and apply the exact same logic to the other two corner triangles (triangle AEH and triangle CGF):\n   Area(triangle AEH) + Area(triangle CGF) = (1/4) * Area(ABCD).\n5. Total area of all four corner triangles = (1/4)*Area(ABCD) + (1/4)*Area(ABCD) = (1/2)*Area(ABCD).\n6. The area of the inner midpoint parallelogram EFGH is the total area of quadrilateral ABCD minus the sum of the four corner triangles:\n   Area(EFGH) = Area(ABCD) - (1/2)*Area(ABCD) = (1/2)*Area(ABCD).",
                "finalAnswer": "Proved: Area(EFGH) = (1/2) * Area(ABCD) (Varignon's Theorem).",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q11: Using the formula that the area of a parallelogram is base * height, show that the area of a trapezium is (1/2) * (a + b) * h.",
                "given": "Trapezium ABCD with parallel sides AB = a and CD = b, and perpendicular height h.",
                "formula": "Transform trapezium into an equivalent-area parallelogram by shearing or bisection.",
                "substitution": "Cut along the median line connecting midpoints of non-parallel sides at height h/2.",
                "calculation": "1. Let M be the midpoint of non-parallel side BC, and N be midpoint of AD. The line MN is parallel to bases and has length (a + b) / 2.\n2. Cut the top section along line MN (height h/2) and rotate/translate it to attach adjacent to the bottom section.\n3. The resulting figure is a parallelogram with base equal to (a + b)/2 and height equal to h (or base a + b and height h/2).\n4. Area of parallelogram = Base * Height = ((a + b)/2) * h = (1/2) * (a + b) * h.\n5. Since no area was added or removed during the rearrangement, Area(Trapezium) = (1/2) * (a + b) * h.",
                "finalAnswer": "Proved: Transforming the trapezium into a parallelogram of base (a+b)/2 and height h yields Area = (1/2)*(a + b)*h.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q12: By dividing a trapezium into two triangles, show that its area is (1/2) * (a + b) * h.",
                "given": "Trapezium ABCD with parallel sides AB = a and CD = b, height h. Draw diagonal BD.",
                "formula": "Area(ABCD) = Area(triangle ABD) + Area(triangle BCD).",
                "substitution": "Triangle ABD has base AB = a and altitude h. Triangle BCD has base CD = b and altitude h.",
                "calculation": "1. Draw diagonal BD dividing trapezium ABCD into triangle ABD and triangle BCD.\n2. In triangle ABD: base = AB = a. The perpendicular distance from vertex D to line AB is height h.\n   Area(triangle ABD) = (1/2) * base * height = (1/2) * a * h.\n3. In triangle BCD: base = CD = b. The perpendicular distance from vertex B to line CD is also height h.\n   Area(triangle BCD) = (1/2) * base * height = (1/2) * b * h.\n4. Total area = Area(triangle ABD) + Area(triangle BCD) = (1/2)*a*h + (1/2)*b*h.\n5. Factor out common terms (1/2)*h:\n   Area = (1/2) * (a + b) * h.",
                "finalAnswer": "Proved: Summing the two triangles (1/2)*a*h + (1/2)*b*h = (1/2)*(a + b)*h.",
                "unit": "algebraic proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q13: Show how we can use two identical copies of a trapezium to make a parallelogram, and derive the formula for the area of a trapezium.",
                "given": "Trapezium T1 with bases a and b, height h. An identical congruent copy T2.",
                "formula": "Rotate T2 by 180° and place side b of T2 along side a of T1, and side a of T2 along side b of T1.",
                "substitution": "The combined shape is a parallelogram with base = a + b and height = h.",
                "calculation": "1. Take two identical trapeziums of parallel bases a and b and height h.\n2. Invert the second trapezium and join them along their non-parallel legs.\n3. The bottom edge of the combined figure has length a + b.\n4. The top edge of the combined figure has length b + a = a + b.\n5. Since the top and bottom edges are equal and parallel, the combined figure is a parallelogram of base (a + b) and height h.\n6. Area of the large parallelogram = Base * Height = (a + b) * h.\n7. Because the parallelogram is composed of two identical copies of the trapezium:\n   2 * Area(Trapezium) = (a + b) * h.\n8. Divide by 2: Area(Trapezium) = (1/2) * (a + b) * h.",
                "finalAnswer": "Proved: Two copies form a parallelogram of area (a + b)*h, so one trapezium has area (1/2)*(a + b)*h.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q14: Show that the area of a kite is half the product of its diagonals: (i) using algebra, and (ii) using geometry.",
                "given": "Kite with perpendicular diagonals of lengths d1 and d2.",
                "formula": "Method 1 (Geometry): Diagonals are perpendicular. Main diagonal d2 bisects cross diagonal d1 into two halves of length d1/2. Split kite into two congruent triangles on base d2.\nMethod 2 (Algebra): 4 right triangles of legs x, y1; x, y2; etc.",
                "substitution": "Base = d2, height of each triangle = d1 / 2.",
                "calculation": "1. Geometric Proof:\n   - In any kite, the main diagonal (say d2) is the perpendicular bisector of the other diagonal d1.\n   - Diagonal d2 divides the kite into two congruent triangles, each having base d2 and altitude d1/2.\n   - Area of each triangle = (1/2) * base * height = (1/2) * d2 * (d1 / 2) = (1/4) * d1 * d2.\n   - Total Area of kite = 2 * ((1/4) * d1 * d2) = (1/2) * d1 * d2.\n2. Algebraic Proof:\n   - Let the perpendicular diagonals intersect at the origin (0, 0).\n   - The diagonals partition the kite into four right triangles with legs (x1, y1), (x2, y1), (x1, y2), (x2, y2) where x1 + x2 = d1 and y1 + y2 = d2.\n   - Area = (1/2)x1*y1 + (1/2)x2*y1 + (1/2)x1*y2 + (1/2)x2*y2 = (1/2)[y1(x1 + x2) + y2(x1 + x2)] = (1/2)(x1 + x2)(y1 + y2) = (1/2) * d1 * d2.",
                "finalAnswer": "Proved: Area of kite = (1/2) * d1 * d2 (both geometrically via two triangles of base d2 and altitude d1/2, and algebraically via four right triangles).",
                "unit": "algebraic & geometric proof",
                "has_diagram": True
            }
        ]
    }
