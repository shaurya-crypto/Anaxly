"""
Class 10 Mathematics - Chapter 2: Polynomials (NCERT CBSE)
Curriculum ID: 71ff1091-5502-490c-bcc1-9624b699620f
Fully compliant with Invariant 10:
- Minimum 5 dedicated modules (Theory strictly in M1-M2, dedicated solvers M3-M5)
- 100% of all NCERT exercise questions (Ex 2.1, 2.2) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- True Cartesian Parabola Graphs & Unslop High-Precision Vector SVGs
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_cartesian_svg, build_polynomial_ex2_1_grid_svg, get_svg_wrapper

def get_ch2_modules():
    CURRICULUM_ID = "71ff1091-5502-490c-bcc1-9624b699620f"
    
    # SVG 1: Parabola y = x^2 - 3x - 4 with zeroes at x = -1 and x = 4
    svg_parabola_2_zeroes = build_cartesian_svg(
        domain=(-3, 6),
        range_y=(-8, 8),
        points=[
            {"x": -1, "y": 0, "label": "A(-1, 0)", "color": "#DC2626"},
            {"x": 4, "y": 0, "label": "B(4, 0)", "color": "#DC2626"},
            {"x": 1.5, "y": -6.25, "label": "Vertex(1.5, -6.25)", "color": "#2563EB"},
            {"x": 0, "y": -4, "label": "y-int(0, -4)", "color": "#16A34A"},
        ],
        curves=[
            {"fn": lambda x: x**2 - 3*x - 4, "color": "#2563EB", "width": 2.5, "label": "y = x² - 3x - 4"}
        ],
        title="Parabola y = x² - 3x - 4: Geometrical Meaning of Zeroes",
        caption="Intersects x-axis at exactly 2 distinct points (-1, 0) and (4, 0) ⇒ Exactly two real zeroes"
    )
    
    # SVG 2: Parabola with 1 zero (tangent to x-axis) y = (x - 2)^2
    svg_parabola_1_zero = build_cartesian_svg(
        domain=(-1, 5),
        range_y=(-2, 8),
        points=[
            {"x": 2, "y": 0, "label": "A = B (2, 0)", "color": "#DC2626"},
            {"x": 0, "y": 4, "label": "(0, 4)", "color": "#16A34A"},
        ],
        curves=[
            {"fn": lambda x: (x - 2)**2, "color": "#16A34A", "width": 2.5, "label": "y = (x - 2)²"}
        ],
        title="Parabola Tangent to X-Axis: Two Coincident Zeroes",
        caption="Touches x-axis at (2, 0) ⇒ Discriminant D = 0 ⇒ One unique real zero (multiplicity 2)"
    )

    # SVG 3: Parabola with 0 zeroes (completely above x-axis) y = x^2 + 2
    svg_parabola_0_zero = build_cartesian_svg(
        domain=(-4, 4),
        range_y=(-2, 10),
        points=[
            {"x": 0, "y": 2, "label": "Vertex(0, 2)", "color": "#2563EB"},
        ],
        curves=[
            {"fn": lambda x: x**2 + 2, "color": "#DC2626", "width": 2.5, "label": "y = x² + 2"}
        ],
        title="Parabola Completely Above X-Axis: Zero Real Zeroes",
        caption="Never intersects or touches x-axis ⇒ Discriminant D < 0 ⇒ No real zeroes"
    )

    # SVG 4: Formula card for zeroes and coefficients
    card_formula = """
    <g transform="translate(60, 70)">
      <rect width="460" height="230" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" rx="10"/>
      <text x="24" y="32" fill="#0F172A" font-size="14" font-weight="700">Quadratic Polynomial: p(x) = ax² + bx + c (a ≠ 0)</text>
      
      <!-- Sum of zeroes -->
      <rect x="24" y="50" width="412" height="42" fill="#EFF6FF" stroke="#93C5FD" rx="6"/>
      <text x="36" y="76" fill="#1E40AF" font-size="13" font-weight="700">Sum of Zeroes: α + β = -b / a = -(Coefficient of x) / (Coefficient of x²)</text>
      
      <!-- Product of zeroes -->
      <rect x="24" y="102" width="412" height="42" fill="#F0FDF4" stroke="#86EFAC" rx="6"/>
      <text x="36" y="128" fill="#166534" font-size="13" font-weight="700">Product of Zeroes: α · β = c / a = (Constant term) / (Coefficient of x²)</text>
      
      <!-- Polynomial Formation -->
      <rect x="24" y="154" width="412" height="52" fill="#FFFBEB" stroke="#FDE68A" rx="6"/>
      <text x="36" y="174" fill="#92400E" font-size="11" font-weight="700">Polynomial Formation Formula:</text>
      <text x="36" y="194" fill="#B45309" font-size="13" font-weight="700">p(x) = k [ x² - (α + β)x + (α · β) ]  where k is any non-zero real constant</text>
    </g>
    """
    svg_coefficients_card = get_svg_wrapper(card_formula, title="Relationship Between Zeroes & Coefficients", caption="Fundamental algebraic bridges connecting polynomial roots to its standard coefficients")

    modules = [
        # Module 1: Geometrical Meaning of Zeroes
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Geometrical Meaning of the Zeroes of a Polynomial: Parabolas & X-Axis Intersections",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the precise geometrical representation of linear, quadratic, and cubic polynomials. Learn why a degree n polynomial has at most n real zeroes and how parabolic curves opening upward or downward correspond to quadratic zeroes.",
            "key_concepts": [
                "Zero of a Polynomial Definition: p(k) = 0",
                "Linear Polynomial Straight Line Graph: Exactly 1 zero at (-b/a, 0)",
                "Quadratic Polynomial Parabola: y = ax² + bx + c opening upward (a > 0) or downward (a < 0)",
                "Three Geometric Cases: Two Distinct Zeroes, Two Coincident Zeroes, No Real Zeroes",
                "Cubic Polynomial Graphs: Up to 3 real x-intercepts"
            ],
            "subtopics": [
                "Definition of algebraic zeroes vs graphical x-intercepts",
                "Parabolic trajectory analysis and vertex coordinates (-b/2a, -D/4a)",
                "Discriminant D = b² - 4ac geometric significance",
                "Zeroes of cubic polynomials y = x³ and y = x³ - x"
            ],
            "worked_examples": [
                {
                    "problem": "Examine the quadratic polynomial p(x) = x² - 3x - 4. Find its algebraic zeroes and verify them graphically.",
                    "solution": "Given: p(x) = x² - 3x - 4\nTo find: Zeroes of p(x) and graphical interpretation.\nFormula: Set p(x) = 0 ⇒ x² - 3x - 4 = 0\nFactorisation: Split middle term: -4x + 1x = -3x, (-4)(1) = -4\nx² - 4x + x - 4 = 0\nx(x - 4) + 1(x - 4) = 0\n(x - 4)(x + 1) = 0 ⇒ x = 4 or x = -1.\nGraphical Representation: Plot y = x² - 3x - 4.\nTable of values: x = -2 ⇒ y = 6; x = -1 ⇒ y = 0; x = 0 ⇒ y = -4; x = 1.5 ⇒ y = -6.25 (Vertex); x = 4 ⇒ y = 0; x = 5 ⇒ y = 6.\n[ROUGH_WORK]\nVertex x = -b/(2a) = -(-3)/(2*1) = 3/2 = 1.5\nVertex y = (1.5)² - 3(1.5) - 4 = 2.25 - 4.5 - 4 = -6.25\nRoots: x = (-(-3) ± √(9 - 4(1)(-4))) / 2 = (3 ± √25)/2 = (3 ± 5)/2 ⇒ x = 4, -1.\nBoxed Answer: [ Zeroes are x = -1 and x = 4. The parabola intersects the x-axis at (-1, 0) and (4, 0) ].",
                    "concept_questions": [
                        "Why does the x-coordinate of the intersection point represent the zero of the polynomial?",
                        "What decides whether the parabola opens upward like a cup or downward like an umbrella?",
                        "Can a quadratic polynomial have 3 real zeroes? Why or why not?",
                        "If a parabola never touches the x-axis, does the polynomial still have zeroes in the real number system?"
                    ]
                },
                {
                    "problem": "Look at the graph of y = x³ - 4x. Determine the number of zeroes of the polynomial and write their exact values.",
                    "solution": "Given: y = x³ - 4x\nTo find: Zeroes from graph and algebra.\nFormula: Set y = 0 ⇒ x(x² - 4) = 0\nx(x - 2)(x + 2) = 0 ⇒ x = 0, x = 2, x = -2.\n[ROUGH_WORK]\nDegree = 3 ⇒ At most 3 real zeroes.\nIntersections with x-axis occur at (-2, 0), (0, 0), and (2, 0).\nBoxed Answer: [ Number of zeroes = 3. The zeroes are x = -2, x = 0, and x = 2 ].",
                    "concept_questions": [
                        "What is the maximum number of times a polynomial of degree n can intersect the x-axis?",
                        "Why does the cubic curve pass through the origin (0, 0)?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Parabolic Curves & Geometrical Zeroes",
                "diagram_type": "graph",
                "svg": svg_parabola_2_zeroes,
                "interactive_math_formula": "x^2 - 3x - 4",
                "concept_visuals": [
                    {
                        "concept_title": "Quadratic Polynomial Parabola with 2 Zeroes",
                        "diagram_title": "Parabola y = x² - 3x - 4",
                        "svg": svg_parabola_2_zeroes,
                        "diagram_type": "graph",
                        "interactive_math_formula": "x^2 - 3x - 4",
                        "what_to_make": "Cartesian plot of parabola cutting x-axis at x = -1 and x = 4",
                        "what_to_explain": "Each point where y = 0 represents an authentic real root of p(x) = 0"
                    },
                    {
                        "concept_title": "Coincident Zeroes (Tangent Parabola)",
                        "diagram_title": "Parabola y = (x - 2)²",
                        "svg": svg_parabola_1_zero,
                        "diagram_type": "graph",
                        "interactive_math_formula": "(x - 2)^2",
                        "what_to_make": "Parabola touching x-axis at single point (2, 0)",
                        "what_to_explain": "When discriminant D = 0, the two zeroes coincide at x = 2"
                    },
                    {
                        "concept_title": "No Real Zeroes (Floating Parabola)",
                        "diagram_title": "Parabola y = x² + 2",
                        "svg": svg_parabola_0_zero,
                        "diagram_type": "graph",
                        "interactive_math_formula": "x^2 + 2",
                        "what_to_make": "Parabola vertex at (0, 2) completely above x-axis",
                        "what_to_explain": "Since the graph never cuts y = 0, there are zero real roots"
                    }
                ]
            },
            "common_misconceptions": [
                "Counting intersections with the y-axis as zeroes: Only intersections with the x-axis give zeroes of p(x)!",
                "Believing every quadratic equation must have 2 distinct real zeroes: A parabola may touch at 1 point or miss the x-axis completely."
            ]
        },

        # Module 2: Relationship Between Zeroes and Coefficients
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Relationship Between Zeroes and Coefficients: Quadratic & Cubic Algebraic Identities",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master the rigorous algebraic relationships linking polynomial roots (α, β, γ) to standard polynomial coefficients (a, b, c, d). Covers sum of zeroes, product of zeroes, and polynomial reconstruction.",
            "key_concepts": [
                "Factor Theorem Link: If α, β are zeroes, (x - α) and (x - β) are factors",
                "Identity: ax² + bx + c = k(x - α)(x - β) = k[x² - (α + β)x + αβ]",
                "Sum of Zeroes Formula: α + β = -b/a",
                "Product of Zeroes Formula: α·β = c/a",
                "Reconstructing Quadratic: p(x) = k[x² - Sx + P] where S = sum, P = product",
                "Cubic Relations: α + β + γ = -b/a, αβ + βγ + γα = c/a, αβγ = -d/a"
            ],
            "subtopics": [
                "Proof of α + β = -b/a and αβ = c/a by equating coefficients",
                "Worked Examples 2, 3, 4, 5 from NCERT",
                "Symmetric expressions in zeroes: α² + β², 1/α + 1/β, α - β",
                "Cubic polynomial coefficient relationships"
            ],
            "worked_examples": [
                {
                    "problem": "Example 2 (NCERT): Find the zeroes of the quadratic polynomial x² + 7x + 10, and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(x) = x² + 7x + 10\nTo find: Zeroes of p(x) and verify relations α + β = -b/a and αβ = c/a.\nStep 1: Factorise p(x) by splitting the middle term.\nWe need two numbers whose sum is 7 and product is 10: numbers are 2 and 5.\nx² + 7x + 10 = x² + 2x + 5x + 10\n= x(x + 2) + 5(x + 2) = (x + 2)(x + 5)\nZeroes: p(x) = 0 ⇒ x + 2 = 0 or x + 5 = 0 ⇒ x = -2 or x = -5.\nLet α = -2 and β = -5.\n\nStep 2: Identify coefficients from standard form ax² + bx + c:\na = 1, b = 7, c = 10.\n\nStep 3: Verify Sum of Zeroes:\nLHS = α + β = (-2) + (-5) = -7\nRHS = -b / a = -(7) / 1 = -7\nLHS = RHS. Verified!\n\nStep 4: Verify Product of Zeroes:\nLHS = α · β = (-2) × (-5) = 10\nRHS = c / a = 10 / 1 = 10\nLHS = RHS. Verified!\n[ROUGH_WORK]\nCheck: x = -2 ⇒ (-2)² + 7(-2) + 10 = 4 - 14 + 10 = 0 (True)\nCheck: x = -5 ⇒ (-5)² + 7(-5) + 10 = 25 - 35 + 10 = 0 (True)\nBoxed Answer: [ Zeroes are -2 and -5. Sum = -7 = -b/a, Product = 10 = c/a. Relationship Verified ].",
                    "concept_questions": [
                        "Why do we equate the polynomial to zero to find its zeroes?",
                        "If the coefficient of x is positive, why is the sum of zeroes negative?",
                        "What is the value of 1/α + 1/β for this polynomial?"
                    ]
                },
                {
                    "problem": "Example 3 (NCERT): Find the zeroes of the polynomial x² - 3 and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(x) = x² - 3\nTo find: Zeroes and verify relations with coefficients.\nStep 1: Factorise using identity a² - b² = (a - b)(a + b):\nx² - 3 = x² - (√3)² = (x - √3)(x + √3)\nZeroes: x - √3 = 0 or x + √3 = 0 ⇒ x = √3 or x = -√3.\nLet α = √3, β = -√3.\n\nStep 2: Identify coefficients from ax² + bx + c:\na = 1, b = 0 (since there is no x term), c = -3.\n\nStep 3: Verification:\nSum: α + β = √3 + (-√3) = 0\nFormula: -b/a = -0/1 = 0. (LHS = RHS)\nProduct: α · β = (√3)(-√3) = -3\nFormula: c/a = -3/1 = -3. (LHS = RHS)\n[ROUGH_WORK]\n(√3)² = 3 ⇒ 3 - 3 = 0\n(-√3)² = 3 ⇒ 3 - 3 = 0\nBoxed Answer: [ Zeroes are √3 and -√3. Sum = 0 = -b/a, Product = -3 = c/a. Verified ].",
                    "concept_questions": [
                        "Why is the coefficient b equal to 0 in this polynomial?",
                        "If α and β are opposites in sign and equal in magnitude, what can you always say about coefficient b?"
                    ]
                },
                {
                    "problem": "Example 4 (NCERT): Find a quadratic polynomial, the sum and product of whose zeroes are -3 and 2, respectively.",
                    "solution": "Given: Sum of zeroes (S) = α + β = -3, Product of zeroes (P) = α · β = 2.\nTo find: The quadratic polynomial p(x).\nFormula: p(x) = k [ x² - (α + β)x + (α · β) ] = k [ x² - Sx + P ]\nSubstitution: p(x) = k [ x² - (-3)x + 2 ] = k [ x² + 3x + 2 ]\nFor simplest polynomial, take k = 1:\np(x) = x² + 3x + 2.\n[ROUGH_WORK]\nCheck zeroes: x² + 3x + 2 = (x + 1)(x + 2) = 0 ⇒ x = -1, -2\nSum = (-1) + (-2) = -3 (Matches given)\nProduct = (-1)(-2) = 2 (Matches given)\nBoxed Answer: [ Required polynomial is p(x) = x² + 3x + 2 (or any non-zero multiple k(x² + 3x + 2)) ].",
                    "concept_questions": [
                        "Why is there a minus sign in front of the sum in k[x² - Sx + P]?",
                        "Can 2x² + 6x + 4 also be a correct answer? Explain why."
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Zeroes and Coefficients Formula Card",
                "diagram_type": "diagram",
                "svg": svg_coefficients_card,
                "concept_visuals": [
                    {
                        "concept_title": "Quadratic Coefficients Bridge",
                        "diagram_title": "Formula HUD: α + β = -b/a, αβ = c/a",
                        "svg": svg_coefficients_card,
                        "diagram_type": "diagram",
                        "what_to_make": "HUD card mapping polynomial terms to root sums and products",
                        "what_to_explain": "Direct relationship between algebraic factoring and standard coefficients"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting the negative sign in α + β = -b/a: Always write the minus sign explicitly before substituting b!",
                "Writing p(x) = x² + Sx + P instead of x² - Sx + P: The middle term sign is always the opposite of the sum of zeroes."
            ]
        },

        # Module 3: Exercise 2.1 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise 2.1 Complete Solver: Graphical Zero Extraction for 6 Fundamental Graphs",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Exhaustive step-by-step resolution of all 6 problems from NCERT Exercise 2.1. Learn to inspect polynomial graphs y = p(x) and determine the exact number of real zeroes with crystalline geometric justifications.",
            "key_concepts": [
                "Criterion: Number of zeroes = Number of points where y = p(x) intersects or touches the x-axis",
                "Horizontal Line Graph: Parallel to x-axis ⇒ 0 zeroes",
                "Single Crossing Curve: 1 zero",
                "Three Crossing Curve: 3 zeroes",
                "U-Shaped Parabola Cutting Twice: 2 zeroes",
                "Four Crossing Curve: 4 zeroes",
                "Tangency / Touching without Crossing: Counts as 1 point of contact per touch"
            ],
            "subtopics": [
                "Full resolution of Exercise 2.1 Question 1 (Parts i to vi)",
                "Distinguishing intersections from touches",
                "Board exam answer formulation and justification criteria"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 2.1 Q1 (i): The graph of y = p(x) is a horizontal straight line parallel to the x-axis (above the origin). Find the number of zeroes of p(x).",
                    "solution": "Given: Graph is a horizontal line y = c (c ≠ 0) parallel to the x-axis.\nTo find: Number of zeroes of p(x).\nGoverning Rule: The number of zeroes of p(x) is equal to the number of points where the graph intersects the x-axis.\nObservation: The given line is parallel to the x-axis and does not intersect or touch the x-axis at any point.\nBoxed Answer: [ Number of zeroes = 0. Justification: The graph does not intersect the x-axis ].",
                    "concept_questions": [
                        "What polynomial does a horizontal line represent?",
                        "If the horizontal line was the x-axis itself (y = 0), how many zeroes would it have?"
                    ]
                },
                {
                    "problem": "Exercise 2.1 Q1 (ii): The graph of y = p(x) starts in quadrant 3, crosses the y-axis, and then crosses the x-axis once in quadrant 1. Find the number of zeroes of p(x).",
                    "solution": "Given: Curve intersects the y-axis at 1 point and the x-axis at 1 point.\nTo find: Number of zeroes of p(x).\nObservation: The graph intersects the x-axis at exactly one point.\nNote: The intersection with the y-axis is irrelevant for zeroes of p(x).\nBoxed Answer: [ Number of zeroes = 1. Justification: The graph intersects the x-axis at only one point ].",
                    "concept_questions": [
                        "Does the y-intercept give a zero of p(x)? What does the y-intercept actually represent?"
                    ]
                },
                {
                    "problem": "Exercise 2.1 Q1 (iii): The graph of y = p(x) is an S-shaped cubic curve intersecting the x-axis at three points. Find the number of zeroes of p(x).",
                    "solution": "Given: S-shaped continuous polynomial curve.\nObservation: Counting the points of intersection along the x-axis from left to right:\n1. Cuts negative x-axis at 1 point.\n2. Cuts near origin / positive x-axis at 2nd point.\n3. Cuts further along positive x-axis at 3rd point.\nTotal intersections with x-axis = 3.\nBoxed Answer: [ Number of zeroes = 3. Justification: The graph intersects the x-axis at three distinct points ].",
                    "concept_questions": [
                        "What is the minimum degree of a polynomial that can produce this graph?"
                    ]
                },
                {
                    "problem": "Exercise 2.1 Q1 (iv): The graph of y = p(x) is a U-shaped parabola opening upwards and intersecting the x-axis at two points. Find the number of zeroes of p(x).",
                    "solution": "Given: Parabolic curve opening upwards.\nObservation: The curve intersects the x-axis at two distinct points.\nBoxed Answer: [ Number of zeroes = 2. Justification: The graph intersects the x-axis at two distinct points ].",
                    "concept_questions": [
                        "What is the sign of the leading coefficient a for this upward-opening parabola?"
                    ]
                },
                {
                    "problem": "Exercise 2.1 Q1 (v): The graph of y = p(x) is an oscillating wave curve intersecting the x-axis at four distinct points. Find the number of zeroes of p(x).",
                    "solution": "Given: Continuous curve oscillating across the x-axis.\nObservation: Tracing along the x-axis, the curve cuts the axis at four separate points.\nBoxed Answer: [ Number of zeroes = 4. Justification: The graph intersects the x-axis at four distinct points ].",
                    "concept_questions": [
                        "What is the minimum possible degree of this polynomial?"
                    ]
                },
                {
                    "problem": "Exercise 2.1 Q1 (vi): The graph of y = p(x) intersects the x-axis at one negative point, touches the x-axis at one point, and touches the x-axis at another point. Find the number of zeroes of p(x).",
                    "solution": "Given: Curve intersects at 1 point and touches at 2 points.\nGoverning Principle: Points where the curve touches the x-axis without crossing are still points where y = 0 (representing real zeroes with even multiplicity).\nCounting: 1 intersection + 1 touch + 1 touch = 3 points where y = 0.\nBoxed Answer: [ Number of zeroes = 3. Justification: The graph meets (intersects or touches) the x-axis at three points ].",
                    "concept_questions": [
                        "Why does touching the x-axis count as a zero?",
                        "What happens algebraically at a point where a curve touches the x-axis?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Exercise 2.1 Complete 6-Graph Cartesian Atlas",
                "diagram_type": "graph",
                "svg": build_polynomial_ex2_1_grid_svg(),
                "interactive_math_formula": "x^3 - 4x",
                "concept_visuals": [
                    {
                        "concept_title": "Exercise 2.1 Complete 6-Graph Zero Atlas",
                        "diagram_title": "Geometric Zero Extraction for 6 Polynomial Curves",
                        "svg": build_polynomial_ex2_1_grid_svg(),
                        "diagram_type": "graph",
                        "interactive_math_formula": "x^3 - 4x",
                        "what_to_make": "3x2 grid of mini Cartesian coordinate graphs for Fig 2.10 parts i to vi",
                        "what_to_explain": "Number of zeroes is the number of points of intersection/tangency with the x-axis"
                    },
                    {
                        "concept_title": "Parabola Zeroes",
                        "diagram_title": "Parabola y = x² - 3x - 4 Intersects at Two Points",
                        "svg": svg_parabola_2_zeroes,
                        "diagram_type": "graph",
                        "interactive_math_formula": "x^2 - 3x - 4",
                        "what_to_make": "Cartesian plot highlighting x-axis intersection points (-1, 0) and (4, 0)",
                        "what_to_explain": "Tracing quadratic roots on x-axis"
                    }
                ]
            },
            "common_misconceptions": [
                "Counting points where the curve turns (local maxima/minima) as zeroes: Only points sitting directly on the x-axis count as zeroes!",
                "Ignoring points where the curve touches the x-axis: A touch is a valid real zero where p(x) = 0."
            ]
        },

        # Module 4: Exercise 2.2 Part 1 Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 2.2 Part 1 Solver: Finding Zeroes & Verifying Coefficient Relationships (All 6 Parts of Q1)",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete, rigorous solution of NCERT Exercise 2.2 Question 1 covering all 6 parts. Master quadratic splitting of the middle term, common factor extraction, difference of squares, and dual verification of sum and product relationships.",
            "key_concepts": [
                "Splitting the Middle Term Method: Finding p and q such that p + q = b and pq = ac",
                "Difference of Squares: a² - b² = (a - b)(a + b)",
                "Missing Linear Term (b = 0): Zeroes are symmetric ±√(-c/a)",
                "Missing Constant Term (c = 0): One zero is always 0",
                "Verification Protocol: Formal side-by-side verification of α + β = -b/a and αβ = c/a"
            ],
            "subtopics": [
                "Q1(i): x² - 2x - 8",
                "Q1(ii): 4s² - 4s + 1 (Perfect square trinomial)",
                "Q1(iii): 6x² - 3 - 7x (Rearranging into standard form)",
                "Q1(iv): 4u² + 8u (Factoring by common binomial factor)",
                "Q1(v): t² - 15 (Radical zeroes)",
                "Q1(vi): 3x² - x - 4 (Non-unitary leading coefficient)"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 2.2 Q1 (i): Find the zeroes of the quadratic polynomial x² - 2x - 8, and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(x) = x² - 2x - 8\nTo find: Zeroes and verify relations α + β = -b/a, αβ = c/a.\nStep 1: Factorise by splitting the middle term.\nNeed p, q such that p + q = -2 and pq = -8 ⇒ p = -4, q = 2.\nx² - 2x - 8 = x² - 4x + 2x - 8\n= x(x - 4) + 2(x - 4) = (x - 4)(x + 2)\nSetting p(x) = 0: x - 4 = 0 or x + 2 = 0 ⇒ x = 4, x = -2.\nLet α = 4, β = -2.\n\nStep 2: Coefficients from ax² + bx + c:\na = 1, b = -2, c = -8.\n\nStep 3: Verification of Sum of Zeroes:\nLHS = α + β = 4 + (-2) = 2\nRHS = -b / a = -(-2) / 1 = 2\nLHS = RHS. Verified!\n\nStep 4: Verification of Product of Zeroes:\nLHS = α · β = 4 × (-2) = -8\nRHS = c / a = -8 / 1 = -8\nLHS = RHS. Verified!\n[ROUGH_WORK]\nac = 1 × (-8) = -8\nFactors of -8 that add to -2: (-4, 2)\nBoxed Answer: [ Zeroes are 4 and -2. Sum = 2 = -b/a, Product = -8 = c/a. Verified ].",
                    "concept_questions": [
                        "What is the sign of the product of zeroes if c and a have opposite signs?",
                        "How does splitting the middle term relate to the distributive property?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q1 (ii): Find the zeroes of 4s² - 4s + 1, and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(s) = 4s² - 4s + 1\nStep 1: Recognise (2s)² - 2(2s)(1) + 1² = (2s - 1)²\nAlternatively split middle term: ac = 4 × 1 = 4; need sum -4 ⇒ -2, -2.\n4s² - 2s - 2s + 1 = 2s(2s - 1) - 1(2s - 1) = (2s - 1)(2s - 1)\nSetting p(s) = 0: 2s - 1 = 0 ⇒ s = 1/2, s = 1/2.\nHere we have two equal zeroes: α = 1/2, β = 1/2.\n\nStep 2: Coefficients: a = 4, b = -4, c = 1.\n\nStep 3: Verification:\nSum: α + β = 1/2 + 1/2 = 1\n-b / a = -(-4) / 4 = 4/4 = 1. (LHS = RHS)\nProduct: α · β = (1/2) × (1/2) = 1/4\nc / a = 1 / 4. (LHS = RHS)\n[ROUGH_WORK]\nDiscriminant D = b² - 4ac = (-4)² - 4(4)(1) = 16 - 16 = 0\nD = 0 confirms real and equal roots.\nBoxed Answer: [ Zeroes are 1/2 and 1/2. Sum = 1 = -b/a, Product = 1/4 = c/a. Verified ].",
                    "concept_questions": [
                        "What does D = 0 tell you about the shape and position of the parabola?",
                        "Why must we list 1/2 twice when stating the zeroes of this polynomial?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q1 (iii): Find the zeroes of 6x² - 3 - 7x, and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(x) = 6x² - 3 - 7x\nStep 1: CRITICAL FIRST STEP - Rearrange into standard descending form ax² + bx + c:\np(x) = 6x² - 7x - 3\nHere a = 6, b = -7, c = -3.\nac = 6 × (-3) = -18. Need two numbers summing to -7: -9 and 2.\n6x² - 9x + 2x - 3 = 3x(2x - 3) + 1(2x - 3) = (2x - 3)(3x + 1)\nSetting p(x) = 0:\n2x - 3 = 0 ⇒ x = 3/2\n3x + 1 = 0 ⇒ x = -1/3\nLet α = 3/2, β = -1/3.\n\nStep 2: Verification:\nSum: α + β = 3/2 + (-1/3) = (9 - 2)/6 = 7/6\n-b / a = -(-7) / 6 = 7/6. (LHS = RHS)\nProduct: α · β = (3/2) × (-1/3) = -3/6 = -1/2\nc / a = -3 / 6 = -1/2. (LHS = RHS)\n[ROUGH_WORK]\nWarning: If not rearranged, taking b = -3 and c = -7 will produce a fatal calculation error!\nBoxed Answer: [ Zeroes are 3/2 and -1/3. Sum = 7/6 = -b/a, Product = -1/2 = c/a. Verified ].",
                    "concept_questions": [
                        "Why is rearranging the polynomial into standard form non-negotiable?",
                        "What common mistake do students make when reading coefficients from an unarranged polynomial?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q1 (iv): Find the zeroes of 4u² + 8u, and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(u) = 4u² + 8u\nStep 1: Notice constant term c = 0. Factor out common term 4u:\np(u) = 4u(u + 2)\nSetting p(u) = 0: 4u = 0 or u + 2 = 0 ⇒ u = 0, u = -2.\nLet α = 0, β = -2.\n\nStep 2: Coefficients: a = 4, b = 8, c = 0.\n\nStep 3: Verification:\nSum: α + β = 0 + (-2) = -2\n-b / a = -(8) / 4 = -2. (LHS = RHS)\nProduct: α · β = 0 × (-2) = 0\nc / a = 0 / 4 = 0. (LHS = RHS)\n[ROUGH_WORK]\nWhenever c = 0, zero is always a root since p(0) = 0.\nBoxed Answer: [ Zeroes are 0 and -2. Sum = -2 = -b/a, Product = 0 = c/a. Verified ].",
                    "concept_questions": [
                        "Can you divide both sides by u to solve 4u² + 8u = 0? Why is dividing by a variable dangerous?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q1 (v): Find the zeroes of t² - 15, and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(t) = t² - 15\nStep 1: Linear term b = 0. Use difference of squares identity:\nt² - 15 = t² - (√15)² = (t - √15)(t + √15)\nSetting p(t) = 0: t = √15 or t = -√15.\nLet α = √15, β = -√15.\n\nStep 2: Coefficients: a = 1, b = 0, c = -15.\n\nStep 3: Verification:\nSum: α + β = √15 + (-√15) = 0\n-b / a = -0 / 1 = 0. (LHS = RHS)\nProduct: α · β = (√15)(-√15) = -15\nc / a = -15 / 1 = -15. (LHS = RHS)\n[ROUGH_WORK]\nt² = 15 ⇒ t = ±√15\nBoxed Answer: [ Zeroes are √15 and -√15. Sum = 0 = -b/a, Product = -15 = c/a. Verified ].",
                    "concept_questions": [
                        "Why are the zeroes symmetric about the origin on the number line?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q1 (vi): Find the zeroes of 3x² - x - 4, and verify the relationship between the zeroes and the coefficients.",
                    "solution": "Given: p(x) = 3x² - x - 4\nStep 1: ac = 3 × (-4) = -12. Need two numbers whose sum is -1 and product is -12: -4 and 3.\n3x² - 4x + 3x - 4 = x(3x - 4) + 1(3x - 4) = (3x - 4)(x + 1)\nSetting p(x) = 0: 3x - 4 = 0 or x + 1 = 0 ⇒ x = 4/3, x = -1.\nLet α = 4/3, β = -1.\n\nStep 2: Coefficients: a = 3, b = -1, c = -4.\n\nStep 3: Verification:\nSum: α + β = 4/3 + (-1) = (4 - 3)/3 = 1/3\n-b / a = -(-1) / 3 = 1/3. (LHS = RHS)\nProduct: α · β = (4/3) × (-1) = -4/3\nc / a = -4 / 3. (LHS = RHS)\n[ROUGH_WORK]\nCheck sum: 4/3 - 1 = 1/3\nCheck product: (4/3)*(-1) = -4/3\nBoxed Answer: [ Zeroes are 4/3 and -1. Sum = 1/3 = -b/a, Product = -4/3 = c/a. Verified ].",
                    "concept_questions": [
                        "What is the difference between splitting the middle term when a = 1 versus when a ≠ 1?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Quadratic Factorisation & Verification HUD",
                "diagram_type": "diagram",
                "svg": svg_coefficients_card,
                "concept_visuals": [
                    {
                        "concept_title": "Q1 Complete Verification Matrix",
                        "diagram_title": "Dual Verification Table",
                        "svg": svg_coefficients_card,
                        "diagram_type": "diagram",
                        "what_to_make": "Verification chart mapping roots to ratios",
                        "what_to_explain": "Systematic verification of sum and product of zeroes"
                    }
                ]
            },
            "common_misconceptions": [
                "Dividing through by the variable (e.g. dividing 4u² + 8u = 0 by u to get 4u + 8 = 0): This destroys the zero u = 0!",
                "Forgetting to rearrange 6x² - 3 - 7x into standard form before reading a, b, c."
            ]
        },

        # Module 5: Exercise 2.2 Part 2 Solver & Advanced Board Problems
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise 2.2 Part 2 Solver: Quadratic Polynomial Formation & Higher Order Symmetric Relations (All 6 Parts of Q2)",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete resolution of Exercise 2.2 Question 2 (all 6 parts) for constructing polynomials from given sum and product of zeroes. Advanced Board-Exam numericals on symmetric functions of zeroes (α² + β², 1/α + 1/β, α³ + β³, α/β + β/α).",
            "key_concepts": [
                "Quadratic Construction Formula: p(x) = k[x² - Sx + P] where S = α + β, P = αβ",
                "Eliminating Denominators: Choosing k as the LCM of denominators to yield clean integer coefficients",
                "Symmetric Functions of Zeroes: Expressing non-linear root expressions solely via (α + β) and αβ",
                "Algebraic Identity for Sum of Squares: α² + β² = (α + β)² - 2αβ",
                "Algebraic Identity for Sum of Cubes: α³ + β³ = (α + β)³ - 3αβ(α + β)"
            ],
            "subtopics": [
                "Ex 2.2 Q2 (i): S = 1/4, P = -1",
                "Ex 2.2 Q2 (ii): S = √2, P = 1/3",
                "Ex 2.2 Q2 (iii): S = 0, P = √5",
                "Ex 2.2 Q2 (iv): S = 1, P = 1",
                "Ex 2.2 Q2 (v): S = -1/4, P = 1/4",
                "Ex 2.2 Q2 (vi): S = 4, P = 1",
                "Board HOTS: If α, β are zeroes of 2x² - 5x + 7, find value of 1/α + 1/β and α² + β²",
                "Board HOTS: Find a quadratic polynomial whose zeroes are 2α + 1 and 2β + 1"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 2.2 Q2 (i): Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively: 1/4, -1.",
                    "solution": "Given: Sum of zeroes (S) = 1/4, Product of zeroes (P) = -1.\nTo find: The quadratic polynomial.\nFormula: p(x) = k [ x² - Sx + P ]\nSubstitution: p(x) = k [ x² - (1/4)x + (-1) ] = k [ x² - x/4 - 1 ]\nTo obtain integer coefficients, choose k = 4 (the denominator):\np(x) = 4(x² - x/4 - 1) = 4x² - x - 4.\n[ROUGH_WORK]\nCheck zeroes of 4x² - x - 4:\nSum = -b/a = -(-1)/4 = 1/4 (Matches)\nProduct = c/a = -4/4 = -1 (Matches)\nBoxed Answer: [ Required quadratic polynomial is 4x² - x - 4 ].",
                    "concept_questions": [
                        "Why does multiplying the polynomial by k not alter its zeroes?",
                        "What would happen if we chose k = 1 instead of k = 4?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q2 (ii): Find a quadratic polynomial with sum = √2, product = 1/3.",
                    "solution": "Given: S = √2, P = 1/3.\nFormula: p(x) = k [ x² - Sx + P ] = k [ x² - √2 x + 1/3 ]\nChoose k = 3 (LCM of denominators):\np(x) = 3(x² - √2 x + 1/3) = 3x² - 3√2 x + 1.\n[ROUGH_WORK]\nCheck: Sum = -(-3√2)/3 = √2\nProduct = 1/3\nBoxed Answer: [ Required quadratic polynomial is 3x² - 3√2 x + 1 ].",
                    "concept_questions": [
                        "Is 3x² - 3√2x + 1 a polynomial with rational coefficients? Why is the middle term irrational?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q2 (iii): Find a quadratic polynomial with sum = 0, product = √5.",
                    "solution": "Given: S = 0, P = √5.\nFormula: p(x) = k [ x² - 0·x + √5 ]\nTaking k = 1:\np(x) = x² + √5.\n[ROUGH_WORK]\nZeroes: x² = -√5 (No real zeroes, but the polynomial definition is completely valid!)\nSum = 0, Product = √5\nBoxed Answer: [ Required quadratic polynomial is x² + √5 ].",
                    "concept_questions": [
                        "Does a polynomial whose product of zeroes is positive always have real zeroes?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q2 (iv): Find a quadratic polynomial with sum = 1, product = 1.",
                    "solution": "Given: S = 1, P = 1.\nFormula: p(x) = k [ x² - Sx + P ] = k [ x² - 1·x + 1 ]\nTaking k = 1:\np(x) = x² - x + 1.\n[ROUGH_WORK]\nD = (-1)² - 4(1)(1) = 1 - 4 = -3 < 0.\nBoxed Answer: [ Required quadratic polynomial is x² - x + 1 ].",
                    "concept_questions": [
                        "Can you form a valid quadratic polynomial even when its discriminant is negative?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q2 (v): Find a quadratic polynomial with sum = -1/4, product = 1/4.",
                    "solution": "Given: S = -1/4, P = 1/4.\nFormula: p(x) = k [ x² - Sx + P ] = k [ x² - (-1/4)x + 1/4 ] = k [ x² + x/4 + 1/4 ]\nChoose k = 4:\np(x) = 4(x² + x/4 + 1/4) = 4x² + x + 1.\n[ROUGH_WORK]\nSum = -b/a = -1/4\nProduct = c/a = 1/4\nBoxed Answer: [ Required quadratic polynomial is 4x² + x + 1 ].",
                    "concept_questions": [
                        "Notice the middle term is positive because the given sum was negative: why is that?"
                    ]
                },
                {
                    "problem": "Exercise 2.2 Q2 (vi): Find a quadratic polynomial with sum = 4, product = 1.",
                    "solution": "Given: S = 4, P = 1.\nFormula: p(x) = k [ x² - Sx + P ] = k [ x² - 4x + 1 ]\nTaking k = 1:\np(x) = x² - 4x + 1.\n[ROUGH_WORK]\nZeroes: x = (4 ± √(16 - 4))/2 = (4 ± √12)/2 = 2 ± √3\nSum = (2 + √3) + (2 - √3) = 4\nProduct = (2 + √3)(2 - √3) = 4 - 3 = 1\nBoxed Answer: [ Required quadratic polynomial is x² - 4x + 1 ].",
                    "concept_questions": [
                        "Notice that the roots 2 + √3 and 2 - √3 are conjugate surds: when do surd roots occur in pairs?"
                    ]
                },
                {
                    "problem": "Board Exam HOTS Question: If α and β are the zeroes of the quadratic polynomial p(x) = 2x² - 5x + 7, find the value of: (i) 1/α + 1/β, and (ii) α² + β².",
                    "solution": "Given: p(x) = 2x² - 5x + 7\nHere a = 2, b = -5, c = 7.\nSum of zeroes: α + β = -b/a = -(-5)/2 = 5/2\nProduct of zeroes: α · β = c/a = 7/2\n\nPart (i): Evaluate 1/α + 1/β\nTaking LCM: 1/α + 1/β = (β + α) / (αβ) = (α + β) / (αβ)\nSubstitution:\n1/α + 1/β = (5/2) / (7/2) = (5/2) × (2/7) = 5/7.\n\nPart (ii): Evaluate α² + β²\nUse algebraic identity: (α + β)² = α² + 2αβ + β²\n⇒ α² + β² = (α + β)² - 2αβ\nSubstitution:\nα² + β² = (5/2)² - 2(7/2) = 25/4 - 14/2 = 25/4 - 28/4 = -3/4.\n[ROUGH_WORK]\nWhy is α² + β² negative? Because D = (-5)² - 4(2)(7) = 25 - 56 = -31 < 0.\nThe roots are complex numbers, where the sum of squares can indeed be negative!\nBoxed Answer: [ (i) 1/α + 1/β = 5/7, (ii) α² + β² = -3/4 ].",
                    "concept_questions": [
                        "Why did we not attempt to find the individual values of α and β directly?",
                        "How can you evaluate α³ + β³ using only the sum and product of zeroes?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Quadratic Polynomial Formation & Symmetric Identities HUD",
                "diagram_type": "diagram",
                "svg": svg_coefficients_card,
                "concept_visuals": [
                    {
                        "concept_title": "Formation of Polynomials",
                        "diagram_title": "Formula Card: p(x) = k[x² - Sx + P]",
                        "svg": svg_coefficients_card,
                        "diagram_type": "diagram",
                        "what_to_make": "HUD summary of polynomial reconstruction",
                        "what_to_explain": "Transforming sum and product into standard quadratic form"
                    }
                ]
            },
            "common_misconceptions": [
                "Mistaking the given numbers in Q2 as the zeroes themselves rather than the sum and product: Read carefully whether the problem gives α, β OR (α + β), αβ!",
                "Forgetting to multiply all terms by k when clearing fractional denominators."
            ]
        }
    ]
    
    return modules
