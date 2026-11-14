"""
Chapter 4: Exploring Algebraic Identities - Module 4
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_algebraic_dissection_svg

def get_m4():
    m4_svg = build_algebraic_dissection_svg(
        type_ident='algebra_tiles', a_val=110, b_val=50, c_val=40,
        title="Cubic Volume & Rational Dissection: (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
        caption="3D cubic decomposition partitioned into a^3, three a^2b blocks, three ab^2 blocks, and b^3"
    )

    return {
        "order_index": 4,
        "title": "Cubic Polynomial Identities (a ± b)^3, a^3 ± b^3, Rational Expressions & Section 4.5",
        "description": "Explore 3-dimensional cubic identities (a + b)^3, (a - b)^3, sum and difference of cubes a^3 ± b^3, and the three-variable conditional identity a^3 + b^3 + c^3 - 3abc. Simplify complex rational expressions by algebraic factorisation and canceling non-zero common factors, covering 100% of textbook examples and Exercise 4.5.",
        "subtopics": [
            "Geometric interpretation of a cube of edge (a + b) decomposed into 8 constituent prisms",
            "Expansion of (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 = a^3 + b^3 + 3ab(a + b)",
            "Expansion of (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 = a^3 - b^3 - 3ab(a - b)",
            "Sum and difference of cubes: a^3 + b^3 = (a + b)(a^2 - ab + b^2) and a^3 - b^3 = (a - b)(a^2 + ab + b^2)",
            "Three-variable cubic identity: a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)",
            "Conditional identity: If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc",
            "Simplifying rational algebraic expressions P(x)/Q(x) via complete factorisation",
            "Complete step-by-step solutions to in-text Examples 13 to 18 and Exercises 4.5 Q1 (all 6 parts)"
        ],
        "key_concepts": [
            "Cubic Volume Decomposition: A cube of side (a + b) has volume (a + b)^3 comprising 8 sub-blocks: one a^3 cube, three a^2 * b rectangular slabs, three a * b^2 rectangular columns, and one b^3 cube.",
            "Factored Sum/Difference of Cubes: a^3 + b^3 = (a + b)(a^2 - ab + b^2). The quadratic factor (a^2 - ab + b^2) is an irreducible quadratic over the reals with negative discriminant.",
            "Euler's Three-Variable Identity: a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) = (1/2)(a + b + c)[(a - b)^2 + (b - c)^2 + (c - a)^2].",
            "Conditional Zero Invariant: If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc without needing to calculate cubes individually.",
            "Rational Expression Simplification: A rational expression P(x)/Q(x) is simplified by completely factoring both numerator and denominator and cancelling common factor polynomials, provided the cancelled factor does not equal zero."
        ],
        "success_criteria": "Expand and factor cubic expressions, apply conditional cubic identities to multi-variable constraints, and simplify rational expressions to their lowest terms.",
        "chapter_notes": "Rational expression simplification requires explicitly noting the domain restriction that the denominator must not vanish (e.g. Q(x) != 0).",
        "worked_examples": [
            {
                "problem": "Textbook Example 13: What is the side of the cube whose volume is p^3 + 6p^2q + 12pq^2 + 8q^3 cubic units?",
                "given": "Volume expression: V = p^3 + 6p^2q + 12pq^2 + 8q^3.",
                "formula": "V = s^3 = a^3 + 3a^2b + 3ab^2 + b^3 = (a + b)^3.",
                "substitution": "p^3 + 3(p)^2(2q) + 3(p)(2q)^2 + (2q)^3 with a = p and b = 2q.",
                "calculation": "Step 1: Check leading cube: p^3 = (p)^3 => a = p.\nStep 2: Check trailing cube: 8q^3 = (2q)^3 => b = 2q.\nStep 3: Check first cross term: 3 * a^2 * b = 3 * (p)^2 * (2q) = 6p^2q. Matches.\nStep 4: Check second cross term: 3 * a * b^2 = 3 * (p) * (2q)^2 = 3 * p * 4q^2 = 12pq^2. Matches.\nStep 5: Write as a binomial cube: V = (p + 2q)^3.\nStep 6: Since volume V = side^3, the side length is p + 2q.",
                "finalAnswer": "Side of the cube = p + 2q units",
                "unit": "linear units",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m4_svg
            },
            {
                "problem": "Textbook Example 14: Factorise 8n^3 - 60n^2m + 150nm^2 - 125m^3.",
                "given": "Cubic polynomial: 8n^3 - 60n^2m + 150nm^2 - 125m^3.",
                "formula": "a^3 - 3a^2b + 3ab^2 - b^3 = (a - b)^3.",
                "substitution": "(2n)^3 - 3(2n)^2(5m) + 3(2n)(5m)^2 - (5m)^3 with a = 2n, b = 5m.",
                "calculation": "Step 1: Identify cubes: a^3 = 8n^3 = (2n)^3 => a = 2n; b^3 = 125m^3 = (5m)^3 => b = 5m.\nStep 2: Check cross term 1: 3 * a^2 * b = 3 * (4n^2) * (5m) = 60n^2m. Sign is negative (-60n^2m).\nStep 3: Check cross term 2: 3 * a * b^2 = 3 * (2n) * (25m^2) = 150nm^2. Sign is positive (+150nm^2).\nStep 4: Combine into binomial cube: (2n - 5m)^3.",
                "finalAnswer": "8n^3 - 60n^2m + 150nm^2 - 125m^3 = (2n - 5m)^3",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 15: The sum of three numbers is 10, their product is 25, and the sum of their squares is 38. Use algebraic identities to find the sum of their cubes (x^3 + y^3 + z^3).",
                "given": "x + y + z = 10, xyz = 25, x^2 + y^2 + z^2 = 38.",
                "formula": "Identity 1: (x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx).\nIdentity 2: x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - (xy + yz + zx)).",
                "substitution": "10^2 = 38 + 2(xy + yz + zx); x^3 + y^3 + z^3 - 3(25) = 10 * [38 - (xy + yz + zx)].",
                "calculation": "Step 1: Find xy + yz + zx:\n  100 = 38 + 2(xy + yz + zx)\n  2(xy + yz + zx) = 100 - 38 = 62\n  xy + yz + zx = 31.\nStep 2: Apply the cubic identity:\n  x^3 + y^3 + z^3 - 3(25) = (10) * [38 - 31]\n  x^3 + y^3 + z^3 - 75 = 10 * 7 = 70.\nStep 3: Solve for x^3 + y^3 + z^3:\n  x^3 + y^3 + z^3 = 70 + 75 = 145.",
                "finalAnswer": "x^3 + y^3 + z^3 = 145",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 16: Simplify the rational expression (x^2 - 16) / (5x^2 + 5x - 100), assuming the denominator is not zero.",
                "given": "Rational expression: (x^2 - 16) / (5x^2 + 5x - 100).",
                "formula": "Numerator: a^2 - b^2 = (a - b)(a + b). Denominator: extract 5, then factor quadratic.",
                "substitution": "Numerator = (x - 4)(x + 4); Denominator = 5(x^2 + x - 20) = 5(x + 5)(x - 4).",
                "calculation": "Step 1: Factor numerator: x^2 - 16 = (x - 4)(x + 4).\nStep 2: Factor denominator:\n  5x^2 + 5x - 100 = 5(x^2 + x - 20).\n  Factors of -20 adding to +1 are +5 and -4: (x + 5)(x - 4).\n  Denominator = 5(x + 5)(x - 4).\nStep 3: Form the rational fraction:\n  [(x - 4)(x + 4)] / [5(x + 5)(x - 4)].\nStep 4: Cancel common non-zero factor (x - 4):\n  (x + 4) / [5(x + 5)] = (x + 4) / (5x + 25).",
                "finalAnswer": "(x^2 - 16) / (5x^2 + 5x - 100) = (x + 4) / (5(x + 5))",
                "unit": "simplified rational expression",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 17: Saira has arranged a square of side x units, 8 rectangular strips of sides x units and width 1 unit, and 15 squares of side 1 unit to form a bigger rectangle. Find the length and breadth of the rectangle in terms of x.",
                "given": "1 square of area x^2, 8 strips of area x each, 15 unit squares of area 1 each. Total Area = x^2 + 8x + 15.",
                "formula": "Area = Length * Breadth = (x + a)(x + b) with a + b = 8 and ab = 15.",
                "substitution": "x^2 + 8x + 15 = x^2 + 3x + 5x + 15.",
                "calculation": "Step 1: Find factors of 15 that sum to 8: 3 and 5 (since 3 * 5 = 15 and 3 + 5 = 8).\nStep 2: Factor the trinomial:\n  x^2 + 3x + 5x + 15 = x(x + 3) + 5(x + 3) = (x + 3)(x + 5).\nStep 3: Interpret geometrically:\n  Length = x + 5 units, Breadth = x + 3 units.",
                "finalAnswer": "Length = x + 5 units, Breadth = x + 3 units",
                "unit": "algebraic dimensions",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 18: A rectangular pool is such that its breadth is 4 metres less than its length and its area is 96 sq. metres. Find the length and breadth of the pool.",
                "given": "Let length = x metres. Breadth = x - 4 metres. Area = 96 sq. metres.",
                "formula": "Area = length * breadth => x(x - 4) = 96.",
                "substitution": "x^2 - 4x - 96 = 0.",
                "calculation": "Step 1: Expand and set to zero: x^2 - 4x - 96 = 0.\nStep 2: Find factors of -96 that add to -4: -12 and +8 (since (-12) * 8 = -96 and -12 + 8 = -4).\nStep 3: Split middle term: x^2 - 12x + 8x - 96 = x(x - 12) + 8(x - 12) = (x - 12)(x + 8) = 0.\nStep 4: Solve roots: x - 12 = 0 => x = 12; or x + 8 = 0 => x = -8.\nStep 5: Physical restriction: Length cannot be negative, so ignore x = -8. Thus length x = 12 metres.\nStep 6: Compute breadth: x - 4 = 12 - 4 = 8 metres.\nStep 7: Check: 12 * 8 = 96 sq. metres.",
                "finalAnswer": "Length = 12 metres, Breadth = 8 metres",
                "unit": "metres",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (i): Simplify the rational expression: (3p^2 - 3pq - 18q^2) / (p^2 + 3pq - 10q^2), assuming denominator != 0.",
                "given": "Expression: (3p^2 - 3pq - 18q^2) / (p^2 + 3pq - 10q^2).",
                "formula": "Extract common factor in numerator, factor both quadratics.",
                "substitution": "Numerator = 3(p^2 - pq - 6q^2) = 3(p - 3q)(p + 2q); Denominator = (p + 5q)(p - 2q).",
                "calculation": "Step 1: Factor numerator:\n  3(p^2 - pq - 6q^2) = 3(p - 3q)(p + 2q).\nStep 2: Factor denominator:\n  Factors of -10 that add to +3 are +5 and -2: (p + 5q)(p - 2q).\nStep 3: Form fraction:\n  3(p - 3q)(p + 2q) / [(p + 5q)(p - 2q)].\nStep 4: Since factors are (p + 2q) and (p - 2q), no further polynomial factors cancel over real variables.",
                "finalAnswer": "3(p - 3q)(p + 2q) / ((p + 5q)(p - 2q))",
                "unit": "simplified rational expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (ii): Simplify the rational expression: (n^3 - 3n^2m + 3nm^2 - m^3) / (5m^2 - 10mn + 5n^2), assuming denominator != 0.",
                "given": "Expression: (n^3 - 3n^2m + 3nm^2 - m^3) / (5m^2 - 10mn + 5n^2).",
                "formula": "Numerator = (n - m)^3. Denominator = 5(n^2 - 2nm + m^2) = 5(n - m)^2.",
                "substitution": "(n - m)^3 / [5(n - m)^2].",
                "calculation": "Step 1: Recognise numerator as the binomial cube: (n - m)^3.\nStep 2: In denominator, factor out 5: 5(m^2 - 2mn + n^2) = 5(n - m)^2.\nStep 3: Divide numerator by denominator: (n - m)^3 / [5(n - m)^2].\nStep 4: Cancel (n - m)^2: (n - m) / 5.",
                "finalAnswer": "(n - m) / 5",
                "unit": "simplified rational expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (iii): Simplify: (w^3 - v^3 + x^3 + 3wvx) / (w^2 + v^2 + x^2 - 2wv - 2vx + 2wx), assuming denominator != 0.",
                "given": "Expression: (w^3 + (-v)^3 + x^3 - 3(w)(-v)(x)) / ((w - v + x)^2).",
                "formula": "a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca).",
                "substitution": "Let a = w, b = -v, c = x. Denominator = (w - v + x)^2.",
                "calculation": "Step 1: Set a = w, b = -v, c = x.\nStep 2: Numerator = a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca).\n  = (w - v + x)(w^2 + v^2 + x^2 - w(-v) - (-v)x - wx) = (w - v + x)(w^2 + v^2 + x^2 + wv + vx - wx).\nStep 3: Expand (w - v + x)^2: w^2 + v^2 + x^2 - 2wv - 2vx + 2wx. This matches the denominator exactly!\nStep 4: Divide numerator by denominator:\n  [(w - v + x)(w^2 + v^2 + x^2 + wv + vx - wx)] / [(w - v + x)^2].\nStep 5: Cancel one factor of (w - v + x):\n  (w^2 + v^2 + x^2 + wv + vx - wx) / (w - v + x).",
                "finalAnswer": "(w^2 + v^2 + x^2 + wv + vx - wx) / (w - v + x)",
                "unit": "simplified rational expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (iv): Simplify: (4y^2 - 20yz + 25z^2) / (25z^2 - 4y^2), assuming denominator != 0.",
                "given": "Expression: (4y^2 - 20yz + 25z^2) / (25z^2 - 4y^2).",
                "formula": "Numerator = (2y - 5z)^2. Denominator = (5z - 2y)(5z + 2y).",
                "substitution": "(2y - 5z)^2 / [(5z - 2y)(5z + 2y)].",
                "calculation": "Step 1: Numerator is a perfect square: (2y - 5z)^2 = (5z - 2y)^2.\nStep 2: Denominator is difference of squares: (5z - 2y)(5z + 2y).\nStep 3: Write fraction: (5z - 2y)^2 / [(5z - 2y)(5z + 2y)].\nStep 4: Cancel (5z - 2y):\n  (5z - 2y) / (5z + 2y).",
                "finalAnswer": "(5z - 2y) / (5z + 2y)",
                "unit": "simplified rational expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (v): Simplify: [ (x^2 + x - 6)(x^2 - 7x + 12) ] / [ (x^2 - 6x + 8)(x^2 - 9) ], assuming denominator != 0.",
                "given": "Expression: [ (x^2 + x - 6)(x^2 - 7x + 12) ] / [ (x^2 - 6x + 8)(x^2 - 9) ].",
                "formula": "Factor all four quadratic polynomials completely.",
                "substitution": "[ (x + 3)(x - 2) * (x - 3)(x - 4) ] / [ (x - 2)(x - 4) * (x - 3)(x + 3) ].",
                "calculation": "Step 1: Factor x^2 + x - 6 = (x + 3)(x - 2).\nStep 2: Factor x^2 - 7x + 12 = (x - 3)(x - 4).\nStep 3: Factor x^2 - 6x + 8 = (x - 2)(x - 4).\nStep 4: Factor x^2 - 9 = (x - 3)(x + 3).\nStep 5: Assemble numerator: (x + 3)(x - 2)(x - 3)(x - 4).\nStep 6: Assemble denominator: (x - 2)(x - 4)(x - 3)(x + 3).\nStep 7: Notice that every factor in the numerator has an identical counterpart in the denominator: (x + 3), (x - 2), (x - 3), and (x - 4) all cancel completely.\nStep 8: The quotient is 1.",
                "finalAnswer": "1",
                "unit": "constant",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (vi): Simplify: (p^4 - 16) / (p^2 - 4p + 4), assuming denominator != 0.",
                "given": "Expression: (p^4 - 16) / (p^2 - 4p + 4).",
                "formula": "Numerator = difference of squares applied twice. Denominator = perfect square.",
                "substitution": "[ (p^2 - 4)(p^2 + 4) ] / (p - 2)^2 = [ (p - 2)(p + 2)(p^2 + 4) ] / (p - 2)^2.",
                "calculation": "Step 1: Factor p^4 - 16 as (p^2)^2 - 4^2 = (p^2 - 4)(p^2 + 4).\nStep 2: Factor p^2 - 4 as (p - 2)(p + 2).\nStep 3: Numerator = (p - 2)(p + 2)(p^2 + 4).\nStep 4: Factor denominator: p^2 - 4p + 4 = (p - 2)^2.\nStep 5: Divide: [(p - 2)(p + 2)(p^2 + 4)] / [(p - 2)(p - 2)].\nStep 6: Cancel one factor of (p - 2): (p + 2)(p^2 + 4) / (p - 2).",
                "finalAnswer": "(p + 2)(p^2 + 4) / (p - 2)",
                "unit": "simplified rational expression",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Canceling individual terms across a plus sign (e.g. canceling x^2 in (x^2 - 16)/(5x^2 + ...) without factoring).",
            "Confusing (a + b)^3 = a^3 + b^3 + 3ab(a + b) with a^3 + b^3.",
            "Forgetting domain restrictions where the rational expression is undefined (Q(x) = 0)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Introduce 3D cubic volume by showing 8 component prisms. For rational expressions, strictly enforce the rule: FACTOR FIRST, CANCEL FACTORS, NEVER CANCEL TERMS.",
        "visual_lesson_plan": {
            "title": "Cubic Volume Dissection & Rational Curves",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Cubic block decomposition of (a + b)^3 showing 8 sub-blocks.",
            "concept_visuals": [
                {
                    "concept_title": "Cubic Function Growth and Inflection",
                    "diagram_title": "Cubic Curve y = x^3 vs Shifted Binomial Cube y = (x - 2)^3",
                    "interactive_math_formula": "y = (x - 2)^3 = x^3 - 6x^2 + 12x - 8",
                    "mafs_graph_config": {
                        "domain": [-2, 5],
                        "range": [-10, 15],
                        "curves": [
                            {"fn": "x^3", "color": "#2563EB", "label": "y = x^3"},
                            {"fn": "(x - 2)^3", "color": "#16A34A", "label": "y = (x - 2)^3"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Inflection (0,0)"},
                            {"x": 2, "y": 0, "label": "Shifted Inflection (2,0)"},
                            {"x": 0, "y": -8, "label": "y-intercept (0,-8)"}
                        ]
                    },
                    "image_query": "cubic polynomial function graph inflection point",
                    "video_query": "graphing cubic functions shifts transformations",
                    "what_to_explain": "Expanding (x - 2)^3 shifts the central inflection point from (0,0) to (2,0) while retaining pure cubic monotonicity."
                },
                {
                    "concept_title": "Sum and Difference of Cubes Factor Graph",
                    "diagram_title": "Real Root of Difference of Cubes: y = x^3 - 8 = (x - 2)(x^2 + 2x + 4)",
                    "interactive_math_formula": "y = x^3 - 8",
                    "mafs_graph_config": {
                        "domain": [-3, 4],
                        "range": [-15, 15],
                        "curves": [
                            {"fn": "x^3 - 8", "color": "#D97706", "label": "y = x^3 - 8"}
                        ],
                        "points": [
                            {"x": 2, "y": 0, "label": "Unique Real Root x = 2"},
                            {"x": 0, "y": -8, "label": "y-intercept (0, -8)"}
                        ]
                    },
                    "image_query": "difference of cubes root irreducible quadratic factor",
                    "video_query": "difference of cubes factoring formula proof",
                    "what_to_explain": "The quadratic factor x^2 + 2x + 4 has negative discriminant Delta = -12 < 0, guaranteeing exactly one real root at x = 2."
                },
                {
                    "concept_title": "Rational Expression Hole & Asymptote",
                    "diagram_title": "Rational Function y = (x + 4) / [5(x + 5)] with Hole at x = 4",
                    "interactive_math_formula": "f(x) = (x^2 - 16) / (5x^2 + 5x - 100)",
                    "mafs_graph_config": {
                        "domain": [-10, 8],
                        "range": [-3, 3],
                        "curves": [
                            {"fn": "(x + 4)/(5*(x + 5))", "color": "#7C3AED", "label": "Simplified y = (x+4)/(5x+25)"}
                        ],
                        "points": [
                            {"x": -5, "y": 0, "label": "Vertical Asymptote x = -5"},
                            {"x": 4, "y": 0.178, "label": "Removable Discontinuity (4, 8/45)"},
                            {"x": -4, "y": 0, "label": "Root (-4, 0)"}
                        ]
                    },
                    "image_query": "rational function graph removable discontinuity hole asymptote",
                    "video_query": "rational functions holes vs vertical asymptotes calculus",
                    "what_to_explain": "Canceling (x - 4) removes the zero in the denominator, creating a removable discontinuity (hole) at x = 4."
                },
                {
                    "concept_title": "Three-Variable Conditional Plane",
                    "diagram_title": "Slice x + y + z = 0 where x^3 + y^3 + z^3 = 3xyz",
                    "interactive_math_formula": "If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-15, 15],
                        "curves": [
                            {"fn": "3*x*2*(-x-2)", "color": "#DC2626", "label": "3abc curve along constraint"}
                        ],
                        "points": [
                            {"x": 1, "y": -18, "label": "a=1, b=2, c=-3: 3abc = -18"}
                        ]
                    },
                    "image_query": "Euler algebraic identity conditional three variables",
                    "video_query": "algebraic proof if a+b+c=0 then a3+b3+c3=3abc",
                    "what_to_explain": "When the sum of three numbers is zero, their cubic sum collapses to three times their product."
                },
                {
                    "concept_title": "Pool Dimension Parabola & Physical Root",
                    "diagram_title": "Area Function A(x) = x(x - 4) = 96",
                    "interactive_math_formula": "x^2 - 4x - 96 = 0 => x = 12",
                    "mafs_graph_config": {
                        "domain": [-12, 16],
                        "range": [-110, 30],
                        "curves": [
                            {"fn": "x^2 - 4*x - 96", "color": "#059669", "label": "y = x^2 - 4x - 96"}
                        ],
                        "points": [
                            {"x": 12, "y": 0, "label": "Physical Length x = 12 m"},
                            {"x": -8, "y": 0, "label": "Extraneous Root x = -8 m"},
                            {"x": 2, "y": -100, "label": "Vertex (2, -100)"}
                        ]
                    },
                    "image_query": "quadratic word problem rectangle dimensions roots",
                    "video_query": "solving word problems with quadratic equations length and width",
                    "what_to_explain": "Quadratic equations often produce two mathematical solutions, but physical dimensions reject negative lengths."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Cubic Identities and Rational Expressions",
                    "questions": [
                        {
                            "question": "How many constituent prisms are formed when a cube of edge (a + b) is partitioned?",
                            "type": "short_answer",
                            "options": ["8", "6", "4", "12"],
                            "ideal_answer": "8 constituent blocks: 1 cube of a^3, 3 blocks of a^2b, 3 blocks of ab^2, and 1 cube of b^3.",
                            "socratic_hint": "(a + b) along all three dimensions gives 2 x 2 x 2 = 8 prisms."
                        },
                        {
                            "question": "What is the factored form of the difference of cubes a^3 - b^3?",
                            "type": "short_answer",
                            "options": [
                                "(a - b)(a^2 + ab + b^2)",
                                "(a - b)^3",
                                "(a - b)(a^2 - ab + b^2)",
                                "(a + b)(a^2 - ab + b^2)"
                            ],
                            "ideal_answer": "a^3 - b^3 = (a - b)(a^2 + ab + b^2).",
                            "socratic_hint": "The first factor carries the minus sign (a - b), and all terms in the quadratic factor are positive."
                        },
                        {
                            "question": "If x + y + z = 0, what does x^3 + y^3 + z^3 equal?",
                            "type": "short_answer",
                            "options": ["3xyz", "0", "xyz", "3(x + y + z)"],
                            "ideal_answer": "3xyz, because x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx) = 0 * (...) = 0.",
                            "socratic_hint": "Substitute (x + y + z) = 0 into the 3-variable identity."
                        },
                        {
                            "question": "What is the cardinal rule when simplifying rational algebraic expressions?",
                            "type": "short_answer",
                            "options": [
                                "Factor the numerator and denominator completely first, then cancel common factors",
                                "Cancel common terms across addition signs",
                                "Cross-multiply immediately",
                                "Square both numerator and denominator"
                            ],
                            "ideal_answer": "Completely factor both numerator and denominator into products of prime polynomials, and cancel common non-zero polynomial factors. Never cancel individual terms!",
                            "socratic_hint": "Can you cancel 4 in (4 + x)/4?"
                        },
                        {
                            "question": "Why did Example 18 reject x = -8 as a solution for the pool length?",
                            "type": "short_answer",
                            "options": [
                                "Length is a physical distance which cannot be negative",
                                "Because -8 does not satisfy x^2 - 4x - 96 = 0",
                                "Because 96 is positive",
                                "It was a mistake in the textbook"
                            ],
                            "ideal_answer": "In physical geometry, length must be strictly positive (x > 0). While -8 satisfies the quadratic equation algebraically, it is geometrically extraneous.",
                            "socratic_hint": "Can a swimming pool have a length of -8 metres?"
                        }
                    ]
                }
            ]
        }
    }
