"""
Chapter 4: Exploring Algebraic Identities - Module 6
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_algebraic_dissection_svg

def get_m6():
    m6_svg = build_algebraic_dissection_svg(
        type_ident='a_plus_b_sq', a_val=120, b_val=60,
        title="Geometric Applications & Board-Level Proofs: Area & Volume Decompositions",
        caption="Outer square (40 + 2s)^2 with inner playground 40^2 removed to yield path area 160s + 4s^2"
    )

    return {
        "order_index": 6,
        "title": "End-of-Chapter Master Solver Part 2: Geometric Applications, Word Problems & Advanced Algebraic Proofs (Questions 5 to 13)",
        "description": "Complete step-by-step solutions to End-of-Chapter Questions 5 through 13. Master geometric applications of identities to 2D rectangular areas, 3D cuboid volumes, perimeter borders, reciprocal number equations, common-factor factor theorem proofs, Euler cubic invariants, and consecutive integer divisibility.",
        "subtopics": [
            "Decomposing area expressions into linear binomials representing length and breadth",
            "Decomposing cubic volume polynomials into three linear factors representing dimensions of a cuboid",
            "Border strip area around a square: A(s) = (40 + 2s)^2 - 40^2 = 160s + 4s^2",
            "Reciprocal number equation: x + 1/x = 10/3 transformed into standard quadratic form",
            "Ancient unit hasta and polynomial division for pool dimensions",
            "Factor theorem application to find unknown coefficients: showing p = r in px^2 + 5x + r",
            "Proof of a^3 + b^3 + c^3 - 3abc = -25 given sum and pairwise sum of products",
            "Divisibility proof: n^3 - n = (n - 1)n(n + 1) is always divisible by 6 for all natural numbers n",
            "Conditional zero cubic evaluations: x^3 + y^3 - 12xy + 64 = 0 and x^3 - 8y^3 - 36xy - 216 = 0"
        ],
        "key_concepts": [
            "Geometric Factorisation of Area: An area expression of degree 2 represents a rectangle with length and breadth given by its algebraic factors.",
            "Volume Decomposition: A volume expression of degree 3 represents a cuboid with length, breadth, and height given by its three irreducible linear factors.",
            "Border Strip Symmetry: Adding a uniform border of width s to a square of side L increases both horizontal and vertical dimensions by 2s, yielding total area (L + 2s)^2.",
            "Reciprocal Quadratic Symmetry: If x satisfies x + 1/x = C, then both x and 1/x are reciprocal roots of the quadratic equation x^2 - Cx + 1 = 0.",
            "Factor Theorem Invariant: If (x - a) is a factor of P(x), then P(a) = 0. Simultaneous roots determine relations between polynomial coefficients.",
            "Consecutive Integer Divisibility Principle: The product of k consecutive integers is always divisible by k! (k factorial). Specifically, (n - 1)n(n + 1) is divisible by 3! = 6.",
            "Conditional Cubic Zero Identity: When the linear sum of three terms vanishes (A + B + C = 0), the cubic combination A^3 + B^3 + C^3 - 3ABC vanishes identically."
        ],
        "success_criteria": "State and prove all advanced algebraic identities, solve geometric word problems and reciprocal equations, and rigorously execute multi-step divisibility and factor theorem proofs.",
        "chapter_notes": "Conclude Chapter 4 by demonstrating how algebraic identities unify geometry, arithmetic, number theory, and coordinate algebra into a single coherent framework.",
        "worked_examples": [
            {
                "problem": "End-of-Chapter Q5 (i): Find possible expressions for the length and breadth of a rectangle whose area is given by 25a^2 - 30ab + 9b^2 square units.",
                "given": "Area expression: A = 25a^2 - 30ab + 9b^2.",
                "formula": "Area = Length * Breadth. a^2 - 2ab + b^2 = (a - b)^2.",
                "substitution": "(5a)^2 - 2(5a)(3b) + (3b)^2.",
                "calculation": "Step 1: Check if the quadratic is a perfect square trinomial:\n  - First term: (5a)^2 = 25a^2\n  - Last term: (3b)^2 = 9b^2\n  - Cross term: 2 * (5a) * (3b) = 30ab with negative sign => -30ab.\nStep 2: Factor into a binomial square: (5a - 3b)^2 = (5a - 3b)(5a - 3b).\nStep 3: State the dimensions:\n  Length = 5a - 3b units, Breadth = 5a - 3b units (the rectangle is a square).",
                "finalAnswer": "Length = (5a - 3b) units, Breadth = (5a - 3b) units",
                "unit": "linear units",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q5 (ii): Find possible expressions for the length and breadth of a rectangle whose area is given by 36s^2 - 49t^2 square units.",
                "given": "Area expression: A = 36s^2 - 49t^2.",
                "formula": "Area = Length * Breadth. a^2 - b^2 = (a + b)(a - b).",
                "substitution": "(6s)^2 - (7t)^2.",
                "calculation": "Step 1: Identify terms as squares: (6s)^2 and (7t)^2.\nStep 2: Apply the difference of two squares identity:\n  36s^2 - 49t^2 = (6s + 7t)(6s - 7t).\nStep 3: State the dimensions:\n  Length = (6s + 7t) units, Breadth = (6s - 7t) units.",
                "finalAnswer": "Length = (6s + 7t) units, Breadth = (6s - 7t) units",
                "unit": "linear units",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q6 (i): Find possible expressions for the length, breadth, and height of a cuboid whose volume is given by 6a^2 - 24b^2 cubic units.",
                "given": "Volume: V = 6a^2 - 24b^2.",
                "formula": "Volume = Length * Breadth * Height.",
                "substitution": "6 * (a^2 - 4b^2) = 6 * [a^2 - (2b)^2].",
                "calculation": "Step 1: Factor out the common numerical factor: 6(a^2 - 4b^2).\nStep 2: Factor the difference of squares: a^2 - (2b)^2 = (a - 2b)(a + 2b).\nStep 3: Complete factorization: V = 6 * (a - 2b) * (a + 2b).\nStep 4: Identify the three dimensions:\n  Possible dimensions: Height = 6 units, Length = (a + 2b) units, Breadth = (a - 2b) units.",
                "finalAnswer": "Dimensions: 6, (a + 2b), and (a - 2b) units",
                "unit": "linear units",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q6 (ii): Find possible expressions for the length, breadth, and height of a cuboid whose volume is given by 3ps^2 - 15ps + 12p cubic units.",
                "given": "Volume: V = 3ps^2 - 15ps + 12p.",
                "formula": "Extract common monomial factor 3p, then factor the quadratic trinomial.",
                "substitution": "3p * (s^2 - 5s + 4).",
                "calculation": "Step 1: Factor out 3p: 3p(s^2 - 5s + 4).\nStep 2: Factor the quadratic s^2 - 5s + 4:\n  Factors of 4 that sum to -5 are -1 and -4 (since (-1)*(-4) = 4 and -1 + (-4) = -5).\n  s^2 - 5s + 4 = (s - 1)(s - 4).\nStep 3: Combine factors: V = 3p * (s - 1) * (s - 4).\nStep 4: State the dimensions: Length = 3p units, Breadth = (s - 1) units, Height = (s - 4) units.",
                "finalAnswer": "Dimensions: 3p, (s - 1), and (s - 4) units",
                "unit": "linear units",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q7: The village playground is shaped as a square of side 40 metres. A path of width s metres is created around the playground for people to walk. Find an expression for the area of the path in terms of s.",
                "given": "Inner playground: square of side 40 m. Path width = s metres surrounding all four sides.",
                "formula": "Area of path = Area of outer square - Area of inner playground.",
                "substitution": "Outer side = 40 + 2s; Inner side = 40. Area = (40 + 2s)^2 - 40^2.",
                "calculation": "Step 1: Determine the side of the enlarged outer square:\n  The path adds width s on both sides, so Outer side = 40 + s + s = 40 + 2s metres.\nStep 2: Write the area of the path:\n  A(s) = (40 + 2s)^2 - 40^2.\nStep 3: Apply the difference of two squares identity a^2 - b^2 = (a - b)(a + b):\n  A(s) = [ (40 + 2s) - 40 ] * [ (40 + 2s) + 40 ]\n  = (2s) * (80 + 2s)\n  = 4s(40 + s) = 160s + 4s^2.\nStep 4: Alternatively, expand directly:\n  (40 + 2s)^2 - 40^2 = 1600 + 2(40)(2s) + (2s)^2 - 1600 = 160s + 4s^2.",
                "finalAnswer": "Area of the path = 4s^2 + 160s sq. metres (or 4s(s + 40) sq. metres)",
                "unit": "sq. metres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m6_svg
            },
            {
                "problem": "End-of-Chapter Q8: If a number plus its reciprocal equals 10/3, find the number.",
                "given": "Let the number be x. Equation: x + 1/x = 10/3, with x != 0.",
                "formula": "Multiply through by 3x to form a standard quadratic equation: 3x^2 - 10x + 3 = 0.",
                "substitution": "3x^2 - 9x - x + 3 = 0.",
                "calculation": "Step 1: Multiply both sides by 3x:\n  3x * (x + 1/x) = 3x * (10/3)\n  3x^2 + 3 = 10x\n  3x^2 - 10x + 3 = 0.\nStep 2: Split the middle term:\n  Product ac = 3 * 3 = 9, sum b = -10. The numbers are -9 and -1.\n  3x^2 - 9x - x + 3 = 0.\nStep 3: Factor by grouping:\n  3x(x - 3) - 1(x - 3) = 0\n  (3x - 1)(x - 3) = 0.\nStep 4: Solve roots:\n  Either 3x - 1 = 0 => x = 1/3;\n  Or x - 3 = 0 => x = 3.\nStep 5: Verify:\n  - If x = 3: 3 + 1/3 = 10/3 (valid).\n  - If x = 1/3: 1/3 + 3 = 10/3 (valid).\nStep 6: Conclude that both 3 and 1/3 are valid reciprocal solutions.",
                "finalAnswer": "The number is 3 or 1/3",
                "unit": "rational number",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q9: A rectangular pool has area 2x^2 + 7x + 3 square hastas. If its width is 2x + 1 hastas, find its length. (Hasta was an ancient unit used to measure length).",
                "given": "Area = 2x^2 + 7x + 3 square hastas, Width = 2x + 1 hastas.",
                "formula": "Area = Width * Length => Length = (2x^2 + 7x + 3) / (2x + 1).",
                "substitution": "Factor 2x^2 + 7x + 3 by splitting the middle term.",
                "calculation": "Step 1: In 2x^2 + 7x + 3, product ac = 2 * 3 = 6, sum = 7. Factors are 6 and 1.\nStep 2: Split middle term:\n  2x^2 + 6x + x + 3 = 2x(x + 3) + 1(x + 3) = (2x + 1)(x + 3).\nStep 3: Divide by width (2x + 1):\n  Length = [ (2x + 1)(x + 3) ] / (2x + 1) = x + 3 hastas.\nStep 4: Check: (2x + 1)(x + 3) = 2x^2 + 6x + x + 3 = 2x^2 + 7x + 3.",
                "finalAnswer": "Length = x + 3 hastas",
                "unit": "hastas",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q10: If both (x - 2) and (x - 1/2) are factors of px^2 + 5x + r, show that p = r.",
                "given": "Polynomial P(x) = px^2 + 5x + r. Factors: (x - 2) and (x - 1/2).",
                "formula": "Factor Theorem: If (x - a) is a factor of P(x), then P(a) = 0.",
                "substitution": "P(2) = 0 and P(1/2) = 0.",
                "calculation": "Step 1: Set P(2) = 0:\n  p(2)^2 + 5(2) + r = 0\n  4p + 10 + r = 0\n  4p + r = -10  --- (Equation 1)\nStep 2: Set P(1/2) = 0:\n  p(1/2)^2 + 5(1/2) + r = 0\n  p/4 + 5/2 + r = 0\n  Multiply through by 4:\n  p + 10 + 4r = 0\n  p + 4r = -10  --- (Equation 2)\nStep 3: Equate Equation 1 and Equation 2 (since both equal -10):\n  4p + r = p + 4r.\nStep 4: Rearrange terms:\n  4p - p = 4r - r\n  3p = 3r\n  Divide both sides by 3:\n  p = r.\nStep 5: Substitute p = r into Equation 1 to find the values:\n  4p + p = -10 => 5p = -10 => p = -2, r = -2.",
                "finalAnswer": "p = r (both equal to -2), rigorously proven using the Factor Theorem",
                "unit": "algebraic proof",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q11: If a + b + c = 5 and ab + bc + ca = 10, then prove that a^3 + b^3 + c^3 - 3abc = -25.",
                "given": "a + b + c = 5, ab + bc + ca = 10.",
                "formula": "a^3 + b^3 + c^3 - 3abc = (a + b + c)[a^2 + b^2 + c^2 - (ab + bc + ca)].\nAlso (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca).",
                "substitution": "5^2 = a^2 + b^2 + c^2 + 2(10); a^3 + b^3 + c^3 - 3abc = (5)[ (a^2 + b^2 + c^2) - 10 ].",
                "calculation": "Step 1: Find a^2 + b^2 + c^2 using the trinomial square identity:\n  (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)\n  5^2 = a^2 + b^2 + c^2 + 2(10)\n  25 = a^2 + b^2 + c^2 + 20\n  a^2 + b^2 + c^2 = 25 - 20 = 5.\nStep 2: Substitute into the cubic factorisation formula:\n  a^3 + b^3 + c^3 - 3abc = (a + b + c)[ (a^2 + b^2 + c^2) - (ab + bc + ca) ]\n  = (5) * [ 5 - 10 ]\n  = 5 * (-5)\n  = -25.\nStep 3: Thus the statement is proven completely.",
                "finalAnswer": "a^3 + b^3 + c^3 - 3abc = -25 (Proven)",
                "unit": "algebraic proof",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q12: By factoring the expression, check that n^3 - n is always divisible by 6 for all natural numbers n. Give complete mathematical reasons.",
                "given": "Expression: n^3 - n for any natural number n in N.",
                "formula": "Factorisation: n^3 - n = n(n^2 - 1) = (n - 1) * n * (n + 1).",
                "substitution": "Product of three consecutive natural numbers: (n - 1), n, and (n + 1).",
                "calculation": "Step 1: Factor out n: n(n^2 - 1).\nStep 2: Apply difference of squares to (n^2 - 1): n(n - 1)(n + 1) = (n - 1) * n * (n + 1).\nStep 3: Observe that (n - 1), n, (n + 1) are three consecutive integers.\nStep 4: Divisibility by 2:\n  In any two consecutive integers, at least one is even. Therefore, the product contains at least one multiple of 2, so 2 divides n^3 - n.\nStep 5: Divisibility by 3:\n  In any three consecutive integers, exactly one must be a multiple of 3 (since every third integer is divisible by 3). Therefore, 3 divides n^3 - n.\nStep 6: Divisibility by 6:\n  Since 2 and 3 are coprime (gcd(2, 3) = 1), any integer divisible by both 2 and 3 is divisible by their product 2 * 3 = 6.\nStep 7: Check examples:\n  - For n = 2: 2^3 - 2 = 8 - 2 = 6 = 6 * 1 (divisible by 6).\n  - For n = 3: 3^3 - 3 = 27 - 3 = 24 = 6 * 4 (divisible by 6).\n  - For n = 4: 4^3 - 4 = 64 - 4 = 60 = 6 * 10 (divisible by 6).\n  - For n = 5: 5^3 - 5 = 125 - 5 = 120 = 6 * 20 (divisible by 6).",
                "finalAnswer": "n^3 - n = (n - 1)n(n + 1) is always divisible by 6 for all natural numbers n, because the product of any three consecutive integers is always divisible by both 2 and 3",
                "unit": "number theoretic proof",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q13 (i): Find the value of x^3 + y^3 - 12xy + 64, when x + y = -4.",
                "given": "Expression: x^3 + y^3 - 12xy + 64. Condition: x + y = -4.",
                "formula": "If a + b + c = 0, then a^3 + b^3 + c^3 - 3abc = 0.",
                "substitution": "Rewrite as x^3 + y^3 + 4^3 - 3(x)(y)(4) with a = x, b = y, c = 4.",
                "calculation": "Step 1: Express 64 as a cube: 64 = 4^3.\nStep 2: Express 12xy as 3 * x * y * 4.\nStep 3: The expression becomes: x^3 + y^3 + 4^3 - 3(x)(y)(4).\nStep 4: Check the sum of the terms: a + b + c = x + y + 4.\nStep 5: Substitute the given condition x + y = -4:\n  x + y + 4 = -4 + 4 = 0.\nStep 6: By the conditional cubic identity, if a + b + c = 0, then a^3 + b^3 + c^3 - 3abc = 0.\nStep 7: Therefore, x^3 + y^3 - 12xy + 64 = 0.",
                "finalAnswer": "x^3 + y^3 - 12xy + 64 = 0",
                "unit": "constant",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q13 (ii): Find the value of x^3 - 8y^3 - 36xy - 216, when x = 2y + 6.",
                "given": "Expression: x^3 - 8y^3 - 36xy - 216. Condition: x = 2y + 6.",
                "formula": "If a + b + c = 0, then a^3 + b^3 + c^3 - 3abc = 0.",
                "substitution": "x^3 + (-2y)^3 + (-6)^3 - 3(x)(-2y)(-6) with a = x, b = -2y, c = -6.",
                "calculation": "Step 1: Rewrite all terms as cubes and cross products:\n  - First term: x^3 = (x)^3\n  - Second term: -8y^3 = (-2y)^3\n  - Constant term: -216 = (-6)^3\n  - Cross term: -3 * (x) * (-2y) * (-6) = -3 * 12xy = -36xy.\nStep 2: Check the sum of the terms: a + b + c = x + (-2y) + (-6) = x - 2y - 6.\nStep 3: From the given condition, x = 2y + 6 => x - 2y - 6 = 0.\nStep 4: Since a + b + c = 0, the identity guarantees:\n  a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) = 0 * (...) = 0.\nStep 5: Thus, x^3 - 8y^3 - 36xy - 216 = 0.",
                "finalAnswer": "x^3 - 8y^3 - 36xy - 216 = 0",
                "unit": "constant",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting that a square playground with a path of width s increases each dimension by 2s (one on each side), not s.",
            "Discarding one of the reciprocal roots: x + 1/x = 10/3 has TWO valid solutions, 3 and 1/3, since reciprocals come in pairs.",
            "Claiming n^3 - n is only divisible by 6 for even n: it is divisible by 6 for EVERY natural number n, even or odd."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Present these advanced board-level problems as triumphant crowning syntheses of Chapter 4. Emphasize the beauty of the conditional cubic identity a + b + c = 0 => a^3 + b^3 + c^3 = 3abc.",
        "visual_lesson_plan": {
            "title": "Geometric Applications & Advanced Proof Landscapes",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Concentric squares showing village playground (40x40) surrounded by path width s.",
            "concept_visuals": [
                {
                    "concept_title": "Playground Border Path Area Parabola",
                    "diagram_title": "Path Area A(s) = 4s^2 + 160s as a Function of Width s",
                    "interactive_math_formula": "A(s) = 4s^2 + 160s = 4s(s + 40)",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 2000],
                        "curves": [
                            {"fn": "4*x^2 + 160*x", "color": "#2563EB", "label": "Path Area A(s)"},
                            {"fn": "160*x", "color": "#94A3B8", "label": "Linear Approx 160s"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "No Path s=0"},
                            {"x": 2, "y": 336, "label": "Width 2m: Area = 336 m^2"},
                            {"x": 5, "y": 900, "label": "Width 5m: Area = 900 m^2"}
                        ]
                    },
                    "image_query": "concentric square border path geometry area quadratic",
                    "video_query": "finding area of border around a square or rectangle algebra",
                    "what_to_explain": "Notice how the quadratic term 4s^2 represents the four small corner squares of side s, while 160s represents the four 40 x s side strips."
                },
                {
                    "concept_title": "Reciprocal Function Dual Intersections",
                    "diagram_title": "Intersections of y = x + 1/x with Horizontal Line y = 10/3",
                    "interactive_math_formula": "f(x) = x + 1/x",
                    "mafs_graph_config": {
                        "domain": [0.1, 5],
                        "range": [1, 6],
                        "curves": [
                            {"fn": "x + 1/x", "color": "#16A34A", "label": "y = x + 1/x"},
                            {"fn": "3.333", "color": "#DC2626", "label": "y = 10/3 = 3.333"}
                        ],
                        "points": [
                            {"x": 3, "y": 3.333, "label": "Root x = 3"},
                            {"x": 0.333, "y": 3.333, "label": "Root x = 1/3"},
                            {"x": 1, "y": 2, "label": "Global Minimum (1, 2)"}
                        ]
                    },
                    "image_query": "reciprocal function hyperbola minimum roots intersections",
                    "video_query": "solving x plus 1 over x equals number algebra graph",
                    "what_to_explain": "Because f(1/x) = f(x), the curve is symmetric about the line y = x, guaranteeing that roots always appear as reciprocal pairs."
                },
                {
                    "concept_title": "Consecutive Integer Divisibility Curve",
                    "diagram_title": "Discrete Divisibility Sequence f(n) = n(n - 1)(n + 1) / 6",
                    "interactive_math_formula": "g(n) = (n^3 - n)/6 is always an integer",
                    "mafs_graph_config": {
                        "domain": [0, 8],
                        "range": [0, 90],
                        "curves": [
                            {"fn": "(x^3 - x)/6", "color": "#D97706", "label": "Quotient (n^3 - n)/6"}
                        ],
                        "points": [
                            {"x": 1, "y": 0, "label": "n=1: 0"},
                            {"x": 2, "y": 1, "label": "n=2: 6/6 = 1"},
                            {"x": 3, "y": 4, "label": "n=3: 24/6 = 4"},
                            {"x": 4, "y": 10, "label": "n=4: 60/6 = 10"},
                            {"x": 5, "y": 20, "label": "n=5: 120/6 = 20"}
                        ]
                    },
                    "image_query": "divisibility consecutive integers number theory graph",
                    "video_query": "proof that n cubed minus n is divisible by 6 for all natural numbers",
                    "what_to_explain": "The sequence of values 0, 1, 4, 10, 20 are the tetrahedral numbers, confirming integer outputs for all natural n."
                },
                {
                    "concept_title": "Conditional Cubic Zero Plane",
                    "diagram_title": "Identity Surface: a^3 + b^3 + c^3 - 3abc = 0",
                    "interactive_math_formula": "A + B + C = 0 => A^3 + B^3 + C^3 - 3ABC = 0",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "x^3 + (-x-1)^3 + 1", "color": "#7C3AED", "label": "Identity check along A+B+C=0"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Zero Invariant Point (0, -1, 1)"},
                            {"x": 2, "y": 0, "label": "Zero Invariant Point (2, -3, 1)"}
                        ]
                    },
                    "image_query": "algebraic identity zero constraint curve surface",
                    "video_query": "conditional cubic identity problems IIT CBSE olympiad",
                    "what_to_explain": "Whenever the linear sum of terms is zero, the non-linear cubic combination collapses to zero identically."
                },
                {
                    "concept_title": "Factor Theorem Parabolic Coincidence",
                    "diagram_title": "Parabola y = -2x^2 + 5x - 2 with Roots at x = 2 and x = 0.5",
                    "interactive_math_formula": "P(x) = -2x^2 + 5x - 2 = -(x - 2)(2x - 1)",
                    "mafs_graph_config": {
                        "domain": [-1, 4],
                        "range": [-6, 2],
                        "curves": [
                            {"fn": "-2*x^2 + 5*x - 2", "color": "#059669", "label": "P(x) = -2x^2 + 5x - 2"}
                        ],
                        "points": [
                            {"x": 2, "y": 0, "label": "Root x = 2"},
                            {"x": 0.5, "y": 0, "label": "Root x = 1/2"},
                            {"x": 1.25, "y": 1.125, "label": "Vertex (1.25, 1.125)"}
                        ]
                    },
                    "image_query": "factor theorem roots parabola x intercepts",
                    "video_query": "factor theorem finding unknown coefficients p and r",
                    "what_to_explain": "Having roots at x = 2 and x = 1/2 forces p = r = -2, producing a downward-opening parabola with vertex at (1.25, 1.125)."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Master Solver Part 2",
                    "questions": [
                        {
                            "question": "What is the area of a path of width s surrounding a square playground of side 40 metres?",
                            "type": "short_answer",
                            "options": [
                                "4s^2 + 160s sq. metres",
                                "160s sq. metres",
                                "40s + s^2 sq. metres",
                                "(40 + s)^2 sq. metres"
                            ],
                            "ideal_answer": "4s^2 + 160s sq. metres (or 4s(s + 40) sq. metres), obtained from (40 + 2s)^2 - 40^2.",
                            "socratic_hint": "Remember that the border adds width s on BOTH sides of the playground."
                        },
                        {
                            "question": "What are the two numbers that satisfy x + 1/x = 10/3?",
                            "type": "short_answer",
                            "options": ["3 and 1/3", "10 and 3", "2 and 1/2", "3 and -3"],
                            "ideal_answer": "3 and 1/3, since both are reciprocal roots of 3x^2 - 10x + 3 = 0.",
                            "socratic_hint": "Multiply through by 3x to form a quadratic equation."
                        },
                        {
                            "question": "Why is n^3 - n always divisible by 6 for any natural number n?",
                            "type": "short_answer",
                            "options": [
                                "It factors into (n - 1)n(n + 1), which is the product of three consecutive integers (always divisible by both 2 and 3)",
                                "Because n is always a multiple of 6",
                                "Because 6 is a perfect number",
                                "It is only divisible by 6 when n is even"
                            ],
                            "ideal_answer": "n^3 - n = (n - 1)n(n + 1) is the product of three consecutive integers. Among any three consecutive integers, at least one is divisible by 2 and exactly one is divisible by 3. Since gcd(2, 3) = 1, their product is always divisible by 6.",
                            "socratic_hint": "Factor n^3 - n completely and think about consecutive numbers."
                        },
                        {
                            "question": "If both (x - 2) and (x - 1/2) are factors of px^2 + 5x + r, what is the relation between p and r?",
                            "type": "short_answer",
                            "options": ["p = r", "p = -r", "p = 2r", "p + r = 5"],
                            "ideal_answer": "p = r (in fact, both equal -2), by substituting roots x = 2 and x = 1/2 into the factor theorem equations.",
                            "socratic_hint": "Set P(2) = 0 and P(1/2) = 0, then equate both expressions."
                        },
                        {
                            "question": "Given a + b + c = 5 and ab + bc + ca = 10, what is the value of a^3 + b^3 + c^3 - 3abc?",
                            "type": "short_answer",
                            "options": ["-25", "25", "0", "50"],
                            "ideal_answer": "-25, calculated as (a + b + c)[(a + b + c)^2 - 3(ab + bc + ca)] = 5 * [25 - 30] = 5 * (-5) = -25.",
                            "socratic_hint": "Recall that a^2 + b^2 + c^2 - (ab + bc + ca) = (a + b + c)^2 - 3(ab + bc + ca)."
                        }
                    ]
                }
            ]
        }
    }
