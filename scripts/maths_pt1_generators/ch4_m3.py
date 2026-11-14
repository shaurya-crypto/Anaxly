"""
Chapter 4: Exploring Algebraic Identities - Module 3
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_algebraic_dissection_svg

def get_m3():
    m3_svg = build_algebraic_dissection_svg(
        type_ident='algebra_tiles', a_val=120, b_val=40, c_val=40,
        title="Algebra Tiles Factorisation: x^2 + 7x + 12 = (x + 3)(x + 4)",
        caption="Inner grid formed by one x^2 tile, seven x-tiles, and twelve unit tiles"
    )

    return {
        "order_index": 3,
        "title": "Quadratic Trinomial Factorisation: Algebra Tiles, Splitting the Middle Term & Section 4.4",
        "description": "Visualize quadratic factorisation through physical algebra tiles and master the analytic method of splitting the middle term. Factorise monic and non-monic quadratics x^2 + (a+b)x + ab and acx^2 + (ad+bc)x + bd, and solve 100% of textbook examples and Exercise 4.4 problems.",
        "subtopics": [
            "Geometric representation of quadratic polynomials using algebra tiles (x^2, x, and unit tiles)",
            "Factorisation of monic quadratics: x^2 + (a + b)x + ab = (x + a)(x + b)",
            "Finding factor pairs whose product equals the constant term and sum equals the linear coefficient",
            "General quadratic factorisation: (ax + b)(cx + d) = acx^2 + (ad + bc)x + bd",
            "Sign patterns in quadratic factorisation (positive product vs negative sum)",
            "Application of identities to mental arithmetic and non-standard algebraic products",
            "Complete step-by-step solutions to in-text Examples 10 to 12 and Exercises 4.4 Q1, Q2, Q3, and Think & Reflect"
        ],
        "key_concepts": [
            "Algebra Tiles Invariant: An algebraic expression factors into two linear binomials if and only if its constituent tiles (x^2, x-tiles, and 1-tiles) can be arranged into a perfect non-overlapping rectangle.",
            "Sum-Product Rule: To factor x^2 + Bx + C, find two integers a and b such that a * b = C and a + b = B. Then x^2 + Bx + C = (x + a)(x + b).",
            "Splitting the Middle Term (ac-Method): For ax^2 + bx + c, find two numbers p and q such that p * q = a * c and p + q = b. Split bx into px + qx and factor by grouping.",
            "Sign Rule for Quadratics: If the constant term C > 0, both factors share the sign of B. If C < 0, the factors have opposite signs, with the larger factor sharing the sign of B.",
            "Composite Identity Multiplication: Using identities to evaluate products like 23 x 17 as (20 + 3)(20 - 3) = 400 - 9 = 391."
        ],
        "success_criteria": "Factor any monic or non-monic quadratic expression using the sum-product rule or middle-term splitting, verify factorisations using algebra tiles, and evaluate numerical products rapidly.",
        "chapter_notes": "Emphasize the geometric meaning of factoring as finding the length and breadth of a rectangle whose area is the quadratic trinomial.",
        "worked_examples": [
            {
                "problem": "Textbook Example 10: Factorise x^2 + 7x + 12 using the identity (x + a)(x + b) = x^2 + (a + b)x + ab.",
                "given": "Quadratic trinomial: x^2 + 7x + 12.",
                "formula": "x^2 + (a + b)x + ab = (x + a)(x + b).",
                "substitution": "Here a + b = 7 and ab = 12.",
                "calculation": "Step 1: List factor pairs of 12: (1, 12), (2, 6), (3, 4).\nStep 2: Check their sums: 1 + 12 = 13; 2 + 6 = 8; 3 + 4 = 7. The pair (3, 4) matches the coefficient of x.\nStep 3: Set a = 3 and b = 4.\nStep 4: Rewrite: x^2 + 3x + 4x + 12 = x(x + 3) + 4(x + 3) = (x + 3)(x + 4).",
                "finalAnswer": "x^2 + 7x + 12 = (x + 3)(x + 4)",
                "unit": "factored form",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m3_svg
            },
            {
                "problem": "Textbook Example 11: Factorise x^2 + 11x + 30.",
                "given": "Trinomial: x^2 + 11x + 30.",
                "formula": "x^2 + (a + b)x + ab = (x + a)(x + b).",
                "substitution": "a + b = 11 and ab = 30.",
                "calculation": "Step 1: Factor pairs of 30: (1, 30), (2, 15), (3, 10), (5, 6).\nStep 2: Check sums: 1+30=31; 2+15=17; 3+10=13; 5+6=11. The pair is 5 and 6.\nStep 3: Rewrite: x^2 + 5x + 6x + 30 = x(x + 5) + 6(x + 5) = (x + 5)(x + 6).",
                "finalAnswer": "x^2 + 11x + 30 = (x + 5)(x + 6)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 12: Factorise x^2 - 5x + 6.",
                "given": "Trinomial: x^2 - 5x + 6.",
                "formula": "x^2 + (a + b)x + ab = (x + a)(x + b).",
                "substitution": "a + b = -5 and ab = 6.",
                "calculation": "Step 1: Since ab = +6 (positive) and a + b = -5 (negative), both numbers must be negative.\nStep 2: Negative factor pairs of 6: (-1, -6) and (-2, -3).\nStep 3: Check sums: -1 + (-6) = -7; -2 + (-3) = -5. The pair is -2 and -3.\nStep 4: Factor: (x - 2)(x - 3).",
                "finalAnswer": "x^2 - 5x + 6 = (x - 2)(x - 3)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q1 (i): Fill in the blanks: s^2 - 11s + 24 = (________) (________).",
                "given": "Quadratic: s^2 - 11s + 24.",
                "formula": "s^2 + (a + b)s + ab = (s + a)(s + b).",
                "substitution": "a + b = -11, ab = 24.",
                "calculation": "Step 1: Find factors of 24 with sum -11: (-3) * (-8) = 24 and (-3) + (-8) = -11.\nStep 2: Therefore, s^2 - 11s + 24 = (s - 3)(s - 8).",
                "finalAnswer": "s^2 - 11s + 24 = (s - 3)(s - 8)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q1 (ii): Fill in the blanks: (________) (x + 1) = (3x^2 - 4x - 7).",
                "given": "Product: 3x^2 - 4x - 7, one factor is (x + 1).",
                "formula": "Divide 3x^2 - 4x - 7 by (x + 1) or split middle term.",
                "substitution": "3x^2 - 4x - 7 = 3x^2 + 3x - 7x - 7 = 3x(x + 1) - 7(x + 1).",
                "calculation": "Step 1: Product of outer terms: 3 * (-7) = -21. Sum = -4.\nStep 2: Numbers are +3 and -7.\nStep 3: Split: 3x^2 + 3x - 7x - 7 = 3x(x + 1) - 7(x + 1) = (3x - 7)(x + 1).\nStep 4: The missing factor is (3x - 7).",
                "finalAnswer": "(3x - 7)(x + 1) = 3x^2 - 4x - 7",
                "unit": "algebraic equation",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q1 (iii): Fill in the blanks: 10x^2 - 11x - 6 = (2x - ___) (___ + 2).",
                "given": "Equation: 10x^2 - 11x - 6 = (2x - p)(qx + 2).",
                "formula": "Expand RHS: 2q x^2 + (4 - pq)x - 2p.",
                "substitution": "Compare with 10x^2 - 11x - 6: 2q = 10 => q = 5; -2p = -6 => p = 3.",
                "calculation": "Step 1: From the leading term: 2x * qx = 10x^2 => q = 5.\nStep 2: From the constant term: (-p) * 2 = -6 => p = 3.\nStep 3: Verify the linear coefficient: 2x * 2 + (-3) * 5x = 4x - 15x = -11x. Matches given -11x perfectly.\nStep 4: Thus the blanks are 3 and 5x.",
                "finalAnswer": "10x^2 - 11x - 6 = (2x - 3)(5x + 2)",
                "unit": "completed identity",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q1 (iv): Fill in the blanks: 6x^2 + 7x + 2 = (____________) (___________).",
                "given": "Trinomial: 6x^2 + 7x + 2.",
                "formula": "Splitting the middle term: ac = 6 * 2 = 12, b = 7.",
                "substitution": "Factors of 12 summing to 7 are 3 and 4.",
                "calculation": "Step 1: Rewrite middle term: 7x = 3x + 4x.\nStep 2: 6x^2 + 3x + 4x + 2 = 3x(2x + 1) + 2(2x + 1).\nStep 3: Factor out (2x + 1): (2x + 1)(3x + 2).",
                "finalAnswer": "6x^2 + 7x + 2 = (2x + 1)(3x + 2)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (i): Find the product (41)^2 without multiplying directly.",
                "given": "Number: 41.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2 with 41 = 40 + 1.",
                "substitution": "(40 + 1)^2 = 40^2 + 2*(40)*(1) + 1^2.",
                "calculation": "Step 1: 40^2 = 1600.\nStep 2: 2 * 40 * 1 = 80.\nStep 3: 1^2 = 1.\nStep 4: 1600 + 80 + 1 = 1681.",
                "finalAnswer": "(41)^2 = 1681",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (ii): Find the product (27)^2 without multiplying directly.",
                "given": "Number: 27.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2 with 27 = 30 - 3.",
                "substitution": "(30 - 3)^2 = 30^2 - 2*(30)*(3) + 3^2.",
                "calculation": "Step 1: 30^2 = 900.\nStep 2: 2 * 30 * 3 = 180.\nStep 3: 3^2 = 9.\nStep 4: 900 - 180 + 9 = 729.",
                "finalAnswer": "(27)^2 = 729",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (iii): Find the product (23 x 17) without multiplying directly.",
                "given": "Product: 23 * 17.",
                "formula": "(a + b)(a - b) = a^2 - b^2 with 23 = 20 + 3 and 17 = 20 - 3.",
                "substitution": "(20 + 3)(20 - 3) = 20^2 - 3^2.",
                "calculation": "Step 1: Identify average: (23 + 17)/2 = 20; offset = 3.\nStep 2: 20^2 = 400.\nStep 3: 3^2 = 9.\nStep 4: 400 - 9 = 391.",
                "finalAnswer": "23 * 17 = 391",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (iv): Find the product (135)^2 without multiplying directly.",
                "given": "Number: 135.",
                "formula": "a^2 = (a + 5)(a - 5) + 25 with a = 135.",
                "substitution": "(135 + 5)(135 - 5) + 25 = 140 * 130 + 25.",
                "calculation": "Step 1: 140 * 130 = 14 * 13 * 100 = 182 * 100 = 18,200.\nStep 2: Add 5^2 = 25.\nStep 3: 18,200 + 25 = 18,225.",
                "finalAnswer": "(135)^2 = 18,225",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (v): Find the product (97)^2 without multiplying directly.",
                "given": "Number: 97.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2 with 97 = 100 - 3.",
                "substitution": "(100 - 3)^2 = 100^2 - 2*(100)*(3) + 3^2.",
                "calculation": "Step 1: 100^2 = 10,000.\nStep 2: 2 * 100 * 3 = 600.\nStep 3: 3^2 = 9.\nStep 4: 10,000 - 600 + 9 = 9400 + 9 = 9409.",
                "finalAnswer": "(97)^2 = 9409",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (vi): Find the product (18 x 29) without multiplying directly.",
                "given": "Product: 18 * 29.",
                "formula": "18 * (30 - 1) = 18 * 30 - 18 * 1.",
                "substitution": "18 * 30 - 18 = 540 - 18.",
                "calculation": "Step 1: Decompose 29 as 30 - 1.\nStep 2: Distribute 18: 18 * 30 = 540.\nStep 3: Subtract 18: 540 - 18 = 522.",
                "finalAnswer": "18 * 29 = 522",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (vii): Find the product (34 x 43) without multiplying directly.",
                "given": "Product: 34 * 43.",
                "formula": "(x + a)(x + b) = x^2 + (a + b)x + ab with x = 40, a = -6, b = 3.",
                "substitution": "(40 - 6)(40 + 3) = 40^2 + (-6 + 3)*40 + (-6)*(3).",
                "calculation": "Step 1: Set base x = 40, a = -6, b = 3.\nStep 2: 40^2 = 1600.\nStep 3: (-6 + 3) * 40 = -3 * 40 = -120.\nStep 4: (-6) * 3 = -18.\nStep 5: 1600 - 120 - 18 = 1480 - 18 = 1462.",
                "finalAnswer": "34 * 43 = 1462",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q2 (viii): Find the product (205)^2 without multiplying directly.",
                "given": "Number: 205.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2 with 205 = 200 + 5.",
                "substitution": "(200 + 5)^2 = 200^2 + 2*(200)*(5) + 5^2.",
                "calculation": "Step 1: 200^2 = 40,000.\nStep 2: 2 * 200 * 5 = 2,000.\nStep 3: 5^2 = 25.\nStep 4: 40,000 + 2,000 + 25 = 42,025.",
                "finalAnswer": "(205)^2 = 42,025",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q3 (i): Factor the following: 9a^2 + b^2 + 4c^2 - 6ab + 12ac - 4bc.",
                "given": "Expression: 9a^2 + b^2 + 4c^2 - 6ab + 12ac - 4bc.",
                "formula": "(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx.",
                "substitution": "(3a)^2 + (-b)^2 + (2c)^2 + 2(3a)(-b) + 2(-b)(2c) + 2(3a)(2c).",
                "calculation": "Step 1: Squares: (3a)^2, b^2, (2c)^2.\nStep 2: Sign check: -6ab and -4bc are negative, while 12ac is positive. Thus b has the opposite sign to a and c.\nStep 3: Set x = 3a, y = -b, z = 2c.\nStep 4: Check cross terms: 2(3a)(-b) = -6ab; 2(-b)(2c) = -4bc; 2(3a)(2c) = 12ac. All match.\nStep 5: Factor: (3a - b + 2c)^2.",
                "finalAnswer": "9a^2 + b^2 + 4c^2 - 6ab + 12ac - 4bc = (3a - b + 2c)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q3 (ii): Factor the following: 16s^2 + 25t^2 - 40st.",
                "given": "Expression: 16s^2 - 40st + 25t^2.",
                "formula": "a^2 - 2ab + b^2 = (a - b)^2 with a = 4s, b = 5t.",
                "substitution": "(4s)^2 - 2*(4s)*(5t) + (5t)^2.",
                "calculation": "Step 1: First square: (4s)^2 = 16s^2.\nStep 2: Second square: (5t)^2 = 25t^2.\nStep 3: Middle term: 2 * (4s) * (5t) = 40st with negative sign => -40st.\nStep 4: Factor: (4s - 5t)^2.",
                "finalAnswer": "16s^2 + 25t^2 - 40st = (4s - 5t)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q3 (iii): Factor the following: r^2 - r - 42.",
                "given": "Trinomial: r^2 - r - 42.",
                "formula": "r^2 + (a + b)r + ab = (r + a)(r + b).",
                "substitution": "a * b = -42, a + b = -1.",
                "calculation": "Step 1: Factors of -42 with difference -1: (-7) * 6 = -42 and -7 + 6 = -1.\nStep 2: Rewrite middle term: r^2 - 7r + 6r - 42 = r(r - 7) + 6(r - 7).\nStep 3: Factor: (r - 7)(r + 6).",
                "finalAnswer": "r^2 - r - 42 = (r - 7)(r + 6)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q3 (iv): Factor the following: 49g^2 + 14gh + h^2.",
                "given": "Expression: 49g^2 + 14gh + h^2.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2 with a = 7g, b = h.",
                "substitution": "(7g)^2 + 2*(7g)*(h) + h^2.",
                "calculation": "Step 1: First square: (7g)^2 = 49g^2.\nStep 2: Second square: h^2.\nStep 3: Cross term: 2 * 7g * h = 14gh.\nStep 4: Factor: (7g + h)^2.",
                "finalAnswer": "49g^2 + 14gh + h^2 = (7g + h)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q3 (v): Factor the following: 64u^2 + 121v^2 + 4w^2 - 176uv - 32uw + 44vw.",
                "given": "Expression: 64u^2 + 121v^2 + 4w^2 - 176uv - 32uw + 44vw.",
                "formula": "(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx.",
                "substitution": "(8u)^2 + (-11v)^2 + (-2w)^2 + 2(8u)(-11v) + 2(-11v)(-2w) + 2(8u)(-2w).",
                "calculation": "Step 1: Squares: (8u)^2, (11v)^2, (2w)^2.\nStep 2: Sign check: -176uv is negative, -32uw is negative, +44vw is positive. Since the product of v and w terms is positive (+44vw), -11v and -2w have the same sign (negative), while 8u is positive.\nStep 3: Check cross terms:\n  - 2(8u)(-11v) = -176uv\n  - 2(-11v)(-2w) = +44vw\n  - 2(8u)(-2w) = -32uw\nStep 4: Factor: (8u - 11v - 2w)^2.",
                "finalAnswer": "64u^2 + 121v^2 + 4w^2 - 176uv - 32uw + 44vw = (8u - 11v - 2w)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Think & Reflect: James and Reshma were expanding (a - b)^2 (a + b). James: (a^2 - 2ab + b^2)(a + b). Reshma: (a - b)[(a - b)(a + b)] = (a - b)(a^2 - b^2). According to you, who is correct and why?",
                "given": "Product: (a - b)^2 (a + b).",
                "formula": "Associative and distributive properties of polynomial multiplication.",
                "substitution": "James expands the first factor; Reshma groups the second and third factors.",
                "calculation": "Step 1: Evaluate James' method:\n  (a^2 - 2ab + b^2)(a + b) = a^3 + a^2b - 2a^2b - 2ab^2 + ab^2 + b^3 = a^3 - a^2b - ab^2 + b^3.\nStep 2: Evaluate Reshma's method:\n  (a - b)[(a - b)(a + b)] = (a - b)(a^2 - b^2) = a^3 - ab^2 - a^2b + b^3 = a^3 - a^2b - ab^2 + b^3.\nStep 3: Compare results: Both methods yield identical final expressions.\nStep 4: Efficiency analysis: Reshma's method is superior and faster because applying the difference of two squares (a - b)(a + b) = a^2 - b^2 produces a binomial (a^2 - b^2) rather than a trinomial (a^2 - 2ab + b^2), requiring only 4 partial products instead of 6.",
                "finalAnswer": "Both students are completely correct. Reshma's method is more elegant and computationally efficient because difference of squares yields fewer intermediate cross-terms",
                "unit": "critical mathematical analysis",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Failing to observe the signs when finding factor pairs: picking numbers that multiply to C but add to -B instead of +B.",
            "In non-monic quadratics ax^2 + bx + c, attempting to find factors of c alone rather than factors of the product a * c.",
            "Thinking that grouping terms differently alters the final algebraic product, violating associativity."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Introduce algebra tiles visually. Connect the geometric area of x^2 + 7x + 12 to the sides (x + 3) and (x + 4). Then transition to the analytic middle-term splitting method.",
        "visual_lesson_plan": {
            "title": "Algebra Tiles & Quadratic Trinomial Geometry",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Algebra tile arrangement forming a rectangle of dimensions (x + 3) by (x + 4).",
            "concept_visuals": [
                {
                    "concept_title": "Quadratic Zeroes and Intercept Geometry",
                    "diagram_title": "Parabola y = x^2 + 7x + 12 Intersecting the x-axis",
                    "interactive_math_formula": "y = (x + 3)(x + 4) = x^2 + 7x + 12",
                    "mafs_graph_config": {
                        "domain": [-6, 1],
                        "range": [-2, 14],
                        "curves": [
                            {"fn": "x^2 + 7*x + 12", "color": "#2563EB", "label": "y = x^2 + 7x + 12"}
                        ],
                        "points": [
                            {"x": -3, "y": 0, "label": "Root x = -3"},
                            {"x": -4, "y": 0, "label": "Root x = -4"},
                            {"x": -3.5, "y": -0.25, "label": "Vertex (-3.5, -0.25)"},
                            {"x": 0, "y": 12, "label": "y-intercept (0, 12)"}
                        ]
                    },
                    "image_query": "quadratic trinomial roots parabola zero intersections",
                    "video_query": "factoring quadratics graphical meaning roots x intercepts",
                    "what_to_explain": "Factoring x^2 + 7x + 12 into (x + 3)(x + 4) reveals the exact x-intercepts at x = -3 and x = -4."
                },
                {
                    "concept_title": "Split the Middle Term Splitting Trajectory",
                    "diagram_title": "Splitting 7x into 3x and 4x",
                    "interactive_math_formula": "ac = 12, b = 7 => p = 3, q = 4",
                    "mafs_graph_config": {
                        "domain": [0, 5],
                        "range": [0, 25],
                        "curves": [
                            {"fn": "3*x", "color": "#16A34A", "label": "Component 3x"},
                            {"fn": "4*x", "color": "#D97706", "label": "Component 4x"},
                            {"fn": "7*x", "color": "#2563EB", "label": "Sum 7x"}
                        ],
                        "points": [
                            {"x": 1, "y": 7, "label": "3 + 4 = 7"}
                        ]
                    },
                    "image_query": "algebra splitting the middle term factoring steps diagram",
                    "video_query": "how to split middle term quadratic polynomials step by step",
                    "what_to_explain": "Splitting the linear term allows common binomial factors to be extracted by grouping."
                },
                {
                    "concept_title": "Non-Monic Quadratic Parabola",
                    "diagram_title": "Parabola y = 6x^2 + 7x + 2 = (2x + 1)(3x + 2)",
                    "interactive_math_formula": "Roots: x = -1/2, x = -2/3",
                    "mafs_graph_config": {
                        "domain": [-2, 1],
                        "range": [-1, 6],
                        "curves": [
                            {"fn": "6*x^2 + 7*x + 2", "color": "#7C3AED", "label": "y = 6x^2 + 7x + 2"}
                        ],
                        "points": [
                            {"x": -0.5, "y": 0, "label": "x = -1/2"},
                            {"x": -0.667, "y": 0, "label": "x = -2/3"},
                            {"x": 0, "y": 2, "label": "y-intercept (0, 2)"}
                        ]
                    },
                    "image_query": "non monic quadratic factorisation parabola roots",
                    "video_query": "factoring non monic quadratic equations ac method",
                    "what_to_explain": "For non-monic quadratics, the roots are fractions given by the zeroes of 2x + 1 = 0 and 3x + 2 = 0."
                },
                {
                    "concept_title": "Sign Pattern Matrix in Quadratics",
                    "diagram_title": "Parabola y = x^2 - 5x + 6 (Positive Constant, Negative Sum)",
                    "interactive_math_formula": "Roots: x = 2, x = 3",
                    "mafs_graph_config": {
                        "domain": [0, 5],
                        "range": [-1, 6],
                        "curves": [
                            {"fn": "x^2 - 5*x + 6", "color": "#DC2626", "label": "y = (x - 2)(x - 3)"}
                        ],
                        "points": [
                            {"x": 2, "y": 0, "label": "Root x = 2"},
                            {"x": 3, "y": 0, "label": "Root x = 3"},
                            {"x": 2.5, "y": -0.25, "label": "Vertex (2.5, -0.25)"}
                        ]
                    },
                    "image_query": "quadratic signs rule roots parabola shift",
                    "video_query": "signs in quadratic factorisation explained visually",
                    "what_to_explain": "When the constant is positive and the linear coefficient is negative, both roots are positive, shifting the parabola into the right half-plane."
                },
                {
                    "concept_title": "Algebra Tiles Area Rectangle Proportion",
                    "diagram_title": "Tile Ratio: Area / Dimensions",
                    "interactive_math_formula": "Area = L * W = (x + 3)(x + 4)",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 100],
                        "curves": [
                            {"fn": "(x + 3)*(x + 4)", "color": "#059669", "label": "Total Area (x+3)(x+4)"}
                        ],
                        "points": [
                            {"x": 1, "y": 20, "label": "At x=1: Area = 20"},
                            {"x": 2, "y": 30, "label": "At x=2: Area = 30"}
                        ]
                    },
                    "image_query": "algebra tiles manipulatives physical math area model",
                    "video_query": "using algebra tiles to teach factoring quadratics",
                    "what_to_explain": "Evaluating the area function at physical integer dimensions shows consistent geometric conservation."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Quadratic Factorisation",
                    "questions": [
                        {
                            "question": "What two conditions must numbers a and b satisfy to factor x^2 + 11x + 30 into (x + a)(x + b)?",
                            "type": "short_answer",
                            "options": [
                                "Their sum a + b must equal 11, and their product ab must equal 30",
                                "Their difference must equal 11",
                                "Their ratio must equal 11/30",
                                "They must both equal 11"
                            ],
                            "ideal_answer": "a + b = 11 and a * b = 30. The numbers are 5 and 6.",
                            "socratic_hint": "Expand (x + a)(x + b) = x^2 + (a + b)x + ab and compare coefficients."
                        },
                        {
                            "question": "If a quadratic expression has a positive constant term and a negative linear term (like x^2 - 5x + 6), what can you deduce about its factors?",
                            "type": "short_answer",
                            "options": [
                                "Both numbers must be negative",
                                "Both numbers must be positive",
                                "One is positive and one is negative",
                                "The quadratic cannot be factored"
                            ],
                            "ideal_answer": "Both numbers must be negative, because a negative times a negative gives a positive product (+6), and a negative plus a negative gives a negative sum (-5).",
                            "socratic_hint": "What two signs multiply to give a plus, but add to give a minus?"
                        },
                        {
                            "question": "When factoring 6x^2 + 7x + 2 by splitting the middle term, what product do you look for?",
                            "type": "short_answer",
                            "options": [
                                "The product a * c = 6 * 2 = 12",
                                "The constant term 2 only",
                                "The leading coefficient 6 only",
                                "7 * 2 = 14"
                            ],
                            "ideal_answer": "The product of the leading coefficient and the constant term, a * c = 6 * 2 = 12. Then find two factors of 12 that add to 7 (namely 3 and 4).",
                            "socratic_hint": "Remember the ac-method for non-monic quadratics."
                        },
                        {
                            "question": "In Exercise 4.4, why did Reshma group (a - b)^2 (a + b) as (a - b)[(a - b)(a + b)]?",
                            "type": "short_answer",
                            "options": [
                                "To use the difference of two squares (a - b)(a + b) = a^2 - b^2, making the expansion simpler",
                                "Because James' answer was wrong",
                                "Because (a - b)^2 cannot be expanded directly",
                                "To turn the cubic into a linear equation"
                            ],
                            "ideal_answer": "Grouping (a - b)(a + b) immediately gives (a^2 - b^2), leaving a straightforward binomial multiplication (a - b)(a^2 - b^2) with fewer terms to combine.",
                            "socratic_hint": "Look at the middle two factors: what identity do they form?"
                        },
                        {
                            "question": "How do you evaluate 23 x 17 mentally using identities?",
                            "type": "short_answer",
                            "options": [
                                "Write as (20 + 3)(20 - 3) = 20^2 - 3^2 = 400 - 9 = 391",
                                "Multiply 23 by 10 and add 7",
                                "Round 23 to 20 and 17 to 20 to get 400",
                                "Use long division"
                            ],
                            "ideal_answer": "(20 + 3)(20 - 3) = 20^2 - 3^2 = 400 - 9 = 391.",
                            "socratic_hint": "Both numbers are equally distant from 20."
                        }
                    ]
                }
            ]
        }
    }
