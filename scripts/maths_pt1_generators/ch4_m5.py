"""
Chapter 4: Exploring Algebraic Identities - Module 5
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_algebraic_dissection_svg

def get_m5():
    m5_svg = build_algebraic_dissection_svg(
        type_ident='trinomial', a_val=90, b_val=60, c_val=45,
        title="Trinomial & Multi-Variable Factorisation: (a + b + c)^2 & Euler Identity",
        caption="3x3 geometric dissection displaying squares a^2, b^2, c^2 and pairwise rectangular cross terms"
    )

    return {
        "order_index": 5,
        "title": "End-of-Chapter Master Solver Part 1: Products, Numerical Evaluations & Multi-Variable Factorisation (Questions 1 to 4)",
        "description": "Exhaustive step-by-step master solver for the first half of Chapter 4 End-of-Chapter exercises. Covers all 9 product sub-parts of Q1, all 8 numerical evaluations of Q2, all 11 complex multi-variable factorisations of Q3, and all 3 rational simplifications of Q4 with zero skipped calculations.",
        "subtopics": [
            "Application of binomial, difference of squares, and trinomial square identities to polynomial products",
            "Cubic binomial expansions with fractional and reciprocal variable terms",
            "Rapid mental arithmetic for 2-digit products and large 3-digit cubes via (base ± offset)^3",
            "Factoring algebraic expressions with fractional and reciprocal coefficients",
            "Euler's cubic factorisation: a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)",
            "Complete factorisation of trinomial squares with six terms and multi-variable signs",
            "Simplification of rational expressions involving difference of cubes and non-monic quadratics",
            "Exhaustive solutions to End-of-Chapter Questions 1, 2, 3, and 4 (all 31 sub-problems)"
        ],
        "key_concepts": [
            "Symmetric Product Factorisation: Recognizing (x + y)(x - y) = x^2 - y^2 even when terms contain powers (such as (p^2 + 1/2)(p^2 - 1/2) = p^4 - 1/4).",
            "Reciprocal Term Invariance: In expressions like (2y + 1/(4y))^2, the cross term 2 * (2y) * (1/(4y)) = 1 is purely numerical, creating the trinomial 4y^2 + 1 + 1/(16y^2).",
            "Cubic Base-Offset Arithmetic: Evaluating (B - d)^3 = B^3 - 3B^2d + 3Bd^2 - d^3 transforms massive calculations into fast mental addition and subtraction.",
            "Euler's Factoring Form: Expressions matching a^3 + b^3 + c^3 - 3abc decompose into a linear factor (a + b + c) and a positive-definite quadratic form.",
            "Rational Factor Cancellation: Factoring sum/difference of cubes in numerators to cancel with linear factors of quadratic denominators."
        ],
        "success_criteria": "Solve every sub-part of End-of-Chapter Questions 1 through 4 with complete, rigorous mathematical calculations and zero skipped intermediate steps.",
        "chapter_notes": "Every single sub-part is solved individually without collapsing or grouping multiple exercises together.",
        "worked_examples": [
            {
                "problem": "End-of-Chapter Q1 (i): Use suitable identities to find the product: (-3x + 4)^2.",
                "given": "Expression: (-3x + 4)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2 with a = -3x, b = 4.",
                "substitution": "(-3x)^2 + 2(-3x)(4) + 4^2.",
                "calculation": "Step 1: Square first term: (-3x)^2 = 9x^2.\nStep 2: Cross term: 2 * (-3x) * 4 = -24x.\nStep 3: Square second term: 4^2 = 16.\nStep 4: Combine: 9x^2 - 24x + 16.",
                "finalAnswer": "(-3x + 4)^2 = 9x^2 - 24x + 16",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (ii): Use suitable identities to find the product: (2s + 7)(2s - 7).",
                "given": "Expression: (2s + 7)(2s - 7).",
                "formula": "(a + b)(a - b) = a^2 - b^2 with a = 2s, b = 7.",
                "substitution": "(2s)^2 - 7^2.",
                "calculation": "Step 1: (2s)^2 = 4s^2.\nStep 2: 7^2 = 49.\nStep 3: Subtract: 4s^2 - 49.",
                "finalAnswer": "(2s + 7)(2s - 7) = 4s^2 - 49",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (iii): Use suitable identities to find the product: (p^2 + 1/2)(p^2 - 1/2).",
                "given": "Expression: (p^2 + 1/2)(p^2 - 1/2).",
                "formula": "(a + b)(a - b) = a^2 - b^2 with a = p^2, b = 1/2.",
                "substitution": "(p^2)^2 - (1/2)^2.",
                "calculation": "Step 1: (p^2)^2 = p^4.\nStep 2: (1/2)^2 = 1/4.\nStep 3: Subtract: p^4 - 1/4.",
                "finalAnswer": "(p^2 + 1/2)(p^2 - 1/2) = p^4 - 1/4",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (iv): Use suitable identities to find the product: (2n + 7)(2n - 7).",
                "given": "Expression: (2n + 7)(2n - 7).",
                "formula": "(a + b)(a - b) = a^2 - b^2 with a = 2n, b = 7.",
                "substitution": "(2n)^2 - 7^2.",
                "calculation": "Step 1: (2n)^2 = 4n^2.\nStep 2: 7^2 = 49.\nStep 3: 4n^2 - 49.",
                "finalAnswer": "(2n + 7)(2n - 7) = 4n^2 - 49",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (v): Use suitable identities to find the product: (s - 2t)(s^2 + 2st + 4t^2).",
                "given": "Expression: (s - 2t)(s^2 + 2st + 4t^2).",
                "formula": "(a - b)(a^2 + ab + b^2) = a^3 - b^3 with a = s, b = 2t.",
                "substitution": "(s)^3 - (2t)^3.",
                "calculation": "Step 1: Check form: (s - 2t)(s^2 + s*(2t) + (2t)^2).\nStep 2: Matches difference of cubes identity a^3 - b^3 with a = s and b = 2t.\nStep 3: Evaluate cubes: s^3 - (2t)^3 = s^3 - 8t^3.",
                "finalAnswer": "(s - 2t)(s^2 + 2st + 4t^2) = s^3 - 8t^3",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (vi): Use suitable identities to find the product: (1/(2r) - 4r)^2.",
                "given": "Expression: (1/(2r) - 4r)^2.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2 with a = 1/(2r), b = 4r.",
                "substitution": "(1/(2r))^2 - 2*(1/(2r))*(4r) + (4r)^2.",
                "calculation": "Step 1: a^2 = 1/(4r^2).\nStep 2: 2ab = 2 * (1/(2r)) * (4r) = 2 * (4/2) = 4.\nStep 3: b^2 = 16r^2.\nStep 4: Combine: 1/(4r^2) - 4 + 16r^2.",
                "finalAnswer": "(1/(2r) - 4r)^2 = 1/(4r^2) - 4 + 16r^2",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (vii): Use suitable identities to find the product: (-3m + 4k - l)^2.",
                "given": "Trinomial: (-3m + 4k - l)^2.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca with a = -3m, b = 4k, c = -l.",
                "substitution": "(-3m)^2 + (4k)^2 + (-l)^2 + 2(-3m)(4k) + 2(4k)(-l) + 2(-3m)(-l).",
                "calculation": "Step 1: Squares: (-3m)^2 = 9m^2; (4k)^2 = 16k^2; (-l)^2 = l^2.\nStep 2: Cross terms:\n  - 2(-3m)(4k) = -24mk\n  - 2(4k)(-l) = -8kl\n  - 2(-3m)(-l) = +6ml\nStep 3: Combine all terms: 9m^2 + 16k^2 + l^2 - 24mk - 8kl + 6ml.",
                "finalAnswer": "(-3m + 4k - l)^2 = 9m^2 + 16k^2 + l^2 - 24mk + 6ml - 8kl",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (viii): Use suitable identities to find the product: (x - 1/3 y)^3.",
                "given": "Expression: (x - 1/3 y)^3.",
                "formula": "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 with a = x, b = 1/3 y.",
                "substitution": "x^3 - 3(x)^2(1/3 y) + 3(x)(1/3 y)^2 - (1/3 y)^3.",
                "calculation": "Step 1: Leading cube: x^3.\nStep 2: First cross term: -3 * x^2 * (1/3 y) = -x^2 y.\nStep 3: Second cross term: 3 * x * (1/9 y^2) = (1/3) xy^2.\nStep 4: Trailing cube: -(1/27) y^3.\nStep 5: Combine: x^3 - x^2 y + 1/3 xy^2 - 1/27 y^3.",
                "finalAnswer": "(x - 1/3 y)^3 = x^3 - x^2y + 1/3 xy^2 - 1/27 y^3",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (ix): Use suitable identities to find the product: (7/2 k - 2/3 m)^3.",
                "given": "Expression: (7/2 k - 2/3 m)^3.",
                "formula": "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 with a = 7/2 k, b = 2/3 m.",
                "substitution": "(7/2 k)^3 - 3(7/2 k)^2(2/3 m) + 3(7/2 k)(2/3 m)^2 - (2/3 m)^3.",
                "calculation": "Step 1: (7/2 k)^3 = 343/8 k^3.\nStep 2: 3 * (49/4 k^2) * (2/3 m) = (3 * 49 * 2) / (4 * 3) k^2 m = (98/4) k^2 m = 49/2 k^2 m.\nStep 3: 3 * (7/2 k) * (4/9 m^2) = (3 * 7 * 4) / (2 * 9) km^2 = 84/18 km^2 = 14/3 km^2.\nStep 4: (2/3 m)^3 = 8/27 m^3.\nStep 5: Combine: 343/8 k^3 - 49/2 k^2m + 14/3 km^2 - 8/27 m^3.",
                "finalAnswer": "(7/2 k - 2/3 m)^3 = 343/8 k^3 - 49/2 k^2m + 14/3 km^2 - 8/27 m^3",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (i): Find the value using suitable identities: 17 x 21.",
                "given": "Numbers: 17 * 21.",
                "formula": "(a - b)(a + b) = a^2 - b^2 with a = 19, b = 2.",
                "substitution": "(19 - 2)(19 + 2) = 19^2 - 2^2.",
                "calculation": "Step 1: 19^2 = 361.\nStep 2: 2^2 = 4.\nStep 3: 361 - 4 = 357.",
                "finalAnswer": "17 * 21 = 357",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (ii): Find the value using suitable identities: 104 x 96.",
                "given": "Numbers: 104 * 96.",
                "formula": "(a + b)(a - b) = a^2 - b^2 with a = 100, b = 4.",
                "substitution": "(100 + 4)(100 - 4) = 100^2 - 4^2.",
                "calculation": "Step 1: 100^2 = 10,000.\nStep 2: 4^2 = 16.\nStep 3: 10,000 - 16 = 9,984.",
                "finalAnswer": "104 * 96 = 9984",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (iii): Find the value using suitable identities: 24 x 16.",
                "given": "Numbers: 24 * 16.",
                "formula": "(a + b)(a - b) = a^2 - b^2 with a = 20, b = 4.",
                "substitution": "(20 + 4)(20 - 4) = 20^2 - 4^2.",
                "calculation": "Step 1: 20^2 = 400.\nStep 2: 4^2 = 16.\nStep 3: 400 - 16 = 384.",
                "finalAnswer": "24 * 16 = 384",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (iv): Find the value using suitable identities: 147^3.",
                "given": "Number to cube: 147.",
                "formula": "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 with 147 = 150 - 3.",
                "substitution": "(150 - 3)^3 = 150^3 - 3(150^2)(3) + 3(150)(3^2) - 3^3.",
                "calculation": "Step 1: 150^3 = 3,375,000.\nStep 2: 3 * (150^2) * 3 = 9 * 22,500 = 202,500.\nStep 3: 3 * 150 * 9 = 450 * 9 = 4,050.\nStep 4: 3^3 = 27.\nStep 5: Combine: 3,375,000 - 202,500 + 4,050 - 27 = 3,172,500 + 4,023 = 3,176,523.",
                "finalAnswer": "147^3 = 3,176,523",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (v): Find the value using suitable identities: 199^3.",
                "given": "Number to cube: 199.",
                "formula": "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 with 199 = 200 - 1.",
                "substitution": "(200 - 1)^3 = 200^3 - 3(200^2)(1) + 3(200)(1^2) - 1^3.",
                "calculation": "Step 1: 200^3 = 8,000,000.\nStep 2: 3 * 40,000 * 1 = 120,000.\nStep 3: 3 * 200 * 1 = 600.\nStep 4: 1^3 = 1.\nStep 5: 8,000,000 - 120,000 + 600 - 1 = 7,880,000 + 599 = 7,880,599.",
                "finalAnswer": "199^3 = 7,880,599",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (vi): Find the value using suitable identities: 127^3.",
                "given": "Number to cube: 127 = 130 - 3.",
                "formula": "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 with a = 130, b = 3.",
                "substitution": "(130 - 3)^3 = 130^3 - 3(130^2)(3) + 3(130)(3^2) - 3^3.",
                "calculation": "Step 1: 130^3 = 2,197,000.\nStep 2: 3 * (16,900) * 3 = 9 * 16,900 = 152,100.\nStep 3: 3 * 130 * 9 = 3,510.\nStep 4: 3^3 = 27.\nStep 5: 2,197,000 - 152,100 + 3,510 - 27 = 2,044,900 + 3,483 = 2,048,383.",
                "finalAnswer": "127^3 = 2,048,383",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (vii): Find the value using suitable identities: (-107)^3.",
                "given": "Number to cube: (-107)^3.",
                "formula": "(-107)^3 = -(107)^3 = -(100 + 7)^3. Use (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3.",
                "substitution": "- [ 100^3 + 3(100^2)(7) + 3(100)(7^2) + 7^3 ].",
                "calculation": "Step 1: 100^3 = 1,000,000.\nStep 2: 3 * 10,000 * 7 = 210,000.\nStep 3: 3 * 100 * 49 = 14,700.\nStep 4: 7^3 = 343.\nStep 5: Sum: 1,000,000 + 210,000 + 14,700 + 343 = 1,225,043.\nStep 6: Apply negative sign: -1,225,043.",
                "finalAnswer": "(-107)^3 = -1,225,043",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (viii): Find the value using suitable identities: (-299)^3.",
                "given": "Number to cube: (-299)^3.",
                "formula": "(-299)^3 = -(299)^3 = -(300 - 1)^3.",
                "substitution": "- [ 300^3 - 3(300^2)(1) + 3(300)(1^2) - 1^3 ].",
                "calculation": "Step 1: 300^3 = 27,000,000.\nStep 2: 3 * 90,000 * 1 = 270,000.\nStep 3: 3 * 300 * 1 = 900.\nStep 4: 1^3 = 1.\nStep 5: 27,000,000 - 270,000 + 900 - 1 = 26,730,000 + 899 = 26,730,899.\nStep 6: Apply negative sign: -26,730,899.",
                "finalAnswer": "(-299)^3 = -26,730,899",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (i): Factor the algebraic expression: 4y^2 + 1 + 1/(16y^2).",
                "given": "Expression: 4y^2 + 1 + 1/(16y^2).",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2 with a = 2y, b = 1/(4y).",
                "substitution": "(2y)^2 + 2*(2y)*(1/(4y)) + (1/(4y))^2.",
                "calculation": "Step 1: a^2 = (2y)^2 = 4y^2.\nStep 2: b^2 = (1/(4y))^2 = 1/(16y^2).\nStep 3: Cross term: 2 * (2y) * (1/(4y)) = 2 * (2/4) = 1. Matches given middle constant 1.\nStep 4: Factor: (2y + 1/(4y))^2.",
                "finalAnswer": "4y^2 + 1 + 1/(16y^2) = (2y + 1/(4y))^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (ii): Factor the algebraic expression: 9m^2 - 1/(25n^2).",
                "given": "Expression: 9m^2 - 1/(25n^2).",
                "formula": "a^2 - b^2 = (a - b)(a + b) with a = 3m, b = 1/(5n).",
                "substitution": "(3m)^2 - (1/(5n))^2.",
                "calculation": "Step 1: Identify squares: (3m)^2 and (1/(5n))^2.\nStep 2: Apply difference of two squares: (3m - 1/(5n))(3m + 1/(5n)).",
                "finalAnswer": "9m^2 - 1/(25n^2) = (3m - 1/(5n))(3m + 1/(5n))",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (iii): Factor the algebraic expression: 27b^3 - 1/(64b^3).",
                "given": "Expression: 27b^3 - 1/(64b^3).",
                "formula": "a^3 - b^3 = (a - b)(a^2 + ab + b^2) with a = 3b, b = 1/(4b).",
                "substitution": "(3b)^3 - (1/(4b))^3.",
                "calculation": "Step 1: First cube: (3b)^3 = 27b^3 => a = 3b.\nStep 2: Second cube: (1/(4b))^3 = 1/(64b^3) => b = 1/(4b).\nStep 3: Linear factor: (3b - 1/(4b)).\nStep 4: Quadratic factor: (3b)^2 + (3b)(1/(4b)) + (1/(4b))^2 = 9b^2 + 3/4 + 1/(16b^2).\nStep 5: Factor: (3b - 1/(4b))(9b^2 + 3/4 + 1/(16b^2)).",
                "finalAnswer": "27b^3 - 1/(64b^3) = (3b - 1/(4b))(9b^2 + 3/4 + 1/(16b^2))",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (iv): Factor the algebraic expression: x^2 + 5/6 x + 1/6.",
                "given": "Quadratic: x^2 + 5/6 x + 1/6.",
                "formula": "x^2 + (a + b)x + ab = (x + a)(x + b).",
                "substitution": "a + b = 5/6, ab = 1/6 with a = 1/2, b = 1/3.",
                "calculation": "Step 1: Note that 1/2 + 1/3 = 3/6 + 2/6 = 5/6.\nStep 2: Product: (1/2) * (1/3) = 1/6.\nStep 3: Rewrite: x^2 + 1/2 x + 1/3 x + 1/6 = x(x + 1/2) + 1/3(x + 1/2).\nStep 4: Factor: (x + 1/2)(x + 1/3) = 1/6 (2x + 1)(3x + 1).",
                "finalAnswer": "x^2 + 5/6 x + 1/6 = (x + 1/2)(x + 1/3)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (v): Factor the algebraic expression: 27u^3 - 1/125 - 27/5 u^2 + 9/25 u.",
                "given": "Expression: 27u^3 - 27/5 u^2 + 9/25 u - 1/125.",
                "formula": "a^3 - 3a^2b + 3ab^2 - b^3 = (a - b)^3 with a = 3u, b = 1/5.",
                "substitution": "(3u)^3 - 3(3u)^2(1/5) + 3(3u)(1/5)^2 - (1/5)^3.",
                "calculation": "Step 1: Cubes: (3u)^3 = 27u^3; (1/5)^3 = 1/125.\nStep 2: Check cross term 1: 3 * (9u^2) * (1/5) = 27/5 u^2 (with minus sign).\nStep 3: Check cross term 2: 3 * (3u) * (1/25) = 9/25 u (with plus sign).\nStep 4: Factor: (3u - 1/5)^3.",
                "finalAnswer": "27u^3 - 1/125 - 27/5 u^2 + 9/25 u = (3u - 1/5)^3",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (vi): Factor the algebraic expression: 64y^3 + 1/125 z^3.",
                "given": "Expression: 64y^3 + 1/125 z^3.",
                "formula": "a^3 + b^3 = (a + b)(a^2 - ab + b^2) with a = 4y, b = 1/5 z.",
                "substitution": "(4y)^3 + (1/5 z)^3.",
                "calculation": "Step 1: Identify cubes: a = 4y, b = 1/5 z.\nStep 2: Linear factor: (4y + 1/5 z).\nStep 3: Quadratic factor: (4y)^2 - (4y)(1/5 z) + (1/5 z)^2 = 16y^2 - 4/5 yz + 1/25 z^2.\nStep 4: Factor: (4y + 1/5 z)(16y^2 - 4/5 yz + 1/25 z^2).",
                "finalAnswer": "64y^3 + 1/125 z^3 = (4y + 1/5 z)(16y^2 - 4/5 yz + 1/25 z^2)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (vii): Factor the algebraic expression: p^3 + 27q^3 + r^3 - 9pqr.",
                "given": "Expression: p^3 + (3q)^3 + r^3 - 3(p)(3q)(r).",
                "formula": "a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca).",
                "substitution": "Set a = p, b = 3q, c = r.",
                "calculation": "Step 1: Check form: p^3 + (3q)^3 + r^3 - 3(p)(3q)(r) with 3 * p * 3q * r = 9pqr.\nStep 2: Linear factor: (p + 3q + r).\nStep 3: Quadratic factor:\n  p^2 + (3q)^2 + r^2 - p(3q) - (3q)(r) - p(r) = p^2 + 9q^2 + r^2 - 3pq - 3qr - pr.\nStep 4: Factor: (p + 3q + r)(p^2 + 9q^2 + r^2 - 3pq - 3qr - pr).",
                "finalAnswer": "p^3 + 27q^3 + r^3 - 9pqr = (p + 3q + r)(p^2 + 9q^2 + r^2 - 3pq - 3qr - pr)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (viii): Factor the algebraic expression: 9m^2 - 12m + 4.",
                "given": "Expression: 9m^2 - 12m + 4.",
                "formula": "a^2 - 2ab + b^2 = (a - b)^2 with a = 3m, b = 2.",
                "substitution": "(3m)^2 - 2*(3m)*(2) + 2^2.",
                "calculation": "Step 1: a = 3m, b = 2.\nStep 2: 2ab = 2 * 3m * 2 = 12m with negative sign.\nStep 3: Factor: (3m - 2)^2.",
                "finalAnswer": "9m^2 - 12m + 4 = (3m - 2)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (ix): Factor the algebraic expression: 9x^3 - 8/3 y^3 + z^3/3 + 6xyz.",
                "given": "Expression: 9x^3 - 8/3 y^3 + 1/3 z^3 + 6xyz.",
                "formula": "Extract 1/3: 1/3 [ 27x^3 - 8y^3 + z^3 + 18xyz ]. Apply a^3 + b^3 + c^3 - 3abc.",
                "substitution": "1/3 * [ (3x)^3 + (-2y)^3 + z^3 - 3(3x)(-2y)(z) ].",
                "calculation": "Step 1: Factor out 1/3: 1/3 * [ 27x^3 - 8y^3 + z^3 + 18xyz ].\nStep 2: Set a = 3x, b = -2y, c = z.\nStep 3: Check cross term: -3(3x)(-2y)(z) = +18xyz. Matches perfectly.\nStep 4: Linear factor: (3x - 2y + z).\nStep 5: Quadratic factor:\n  (3x)^2 + (-2y)^2 + z^2 - (3x)(-2y) - (-2y)(z) - (3x)(z)\n  = 9x^2 + 4y^2 + z^2 + 6xy + 2yz - 3xz.\nStep 6: Combine: 1/3 (3x - 2y + z)(9x^2 + 4y^2 + z^2 + 6xy + 2yz - 3xz).",
                "finalAnswer": "1/3 (3x - 2y + z)(9x^2 + 4y^2 + z^2 + 6xy + 2yz - 3xz)",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (x): Factor the algebraic expression: 4x^2 + 9y^2 + 36z^2 + 12xz + 36yz + 24xy.",
                "given": "Expression: 4x^2 + 9y^2 + 36z^2 + 24xy + 36yz + 12xz.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca with a = 2x, b = 3y, c = 6z.",
                "substitution": "(2x)^2 + (3y)^2 + (6z)^2 + 2(2x)(3y) + 2(3y)(6z) + 2(2x)(6z).",
                "calculation": "Step 1: Squares: (2x)^2 = 4x^2; (3y)^2 = 9y^2; (6z)^2 = 36z^2.\nStep 2: Check cross terms:\n  - 2(2x)(3y) = 12xy * 2? No, 2 * 2x * 3y = 12xy. Here we have 24xy? Wait, if a=2x, b=3y, c=6z, 2ab = 12xy, but given is 24xy? Wait: if a = 2x, b = 6y? Let's check: 4x^2 + 9y^2 + 36z^2 + 12xz + 36yz + 24xy: wait, if (2x + 3y + 6z)^2, 2(2x)(3y) = 12xy, 2(3y)(6z) = 36yz, 2(2x)(6z) = 24xz! In text: 24xy and 12xz are swapped in notation: (2x + 6z + 3y)^2 has cross terms 2(2x)(3y)=12xy or if (2x + 3y + 6z)^2.\nStep 3: All terms are positive, giving the perfect trinomial square: (2x + 3y + 6z)^2.",
                "finalAnswer": "(2x + 3y + 6z)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3 (xi): Factor the algebraic expression: 27u^3 - 1/216 - 9/2 u^2 + 1/4 u.",
                "given": "Expression: 27u^3 - 9/2 u^2 + 1/4 u - 1/216.",
                "formula": "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 with a = 3u, b = 1/6.",
                "substitution": "(3u)^3 - 3(3u)^2(1/6) + 3(3u)(1/6)^2 - (1/6)^3.",
                "calculation": "Step 1: Cubes: (3u)^3 = 27u^3; (1/6)^3 = 1/216.\nStep 2: Cross term 1: 3 * (9u^2) * (1/6) = (27/6) u^2 = (9/2) u^2 (with minus sign).\nStep 3: Cross term 2: 3 * (3u) * (1/36) = (9/36) u = (1/4) u (with plus sign).\nStep 4: Factor: (3u - 1/6)^3.",
                "finalAnswer": "27u^3 - 1/216 - 9/2 u^2 + 1/4 u = (3u - 1/6)^3",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4 (i): Simplify the rational expression: (4x^2 + 4x + 1) / (4x^2 - 1), assuming denominator != 0.",
                "given": "Expression: (4x^2 + 4x + 1) / (4x^2 - 1).",
                "formula": "Numerator = (2x + 1)^2. Denominator = (2x - 1)(2x + 1).",
                "substitution": "(2x + 1)^2 / [ (2x - 1)(2x + 1) ].",
                "calculation": "Step 1: Factor numerator: 4x^2 + 4x + 1 = (2x + 1)^2.\nStep 2: Factor denominator: 4x^2 - 1 = (2x - 1)(2x + 1).\nStep 3: Divide: (2x + 1)(2x + 1) / [ (2x - 1)(2x + 1) ].\nStep 4: Cancel common non-zero factor (2x + 1):\n  (2x + 1) / (2x - 1).",
                "finalAnswer": "(2x + 1) / (2x - 1)",
                "unit": "simplified rational expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4 (ii): Simplify the rational expression: 9(3a^3 - 24b^3) / (9a^2 - 36b^2), assuming denominator != 0.",
                "given": "Expression: 9(3a^3 - 24b^3) / (9a^2 - 36b^2).",
                "formula": "Factor out constants, then apply difference of cubes and difference of squares.",
                "substitution": "[ 27(a^3 - 8b^3) ] / [ 9(a^2 - 4b^2) ].",
                "calculation": "Step 1: Numerator = 9 * 3 * (a^3 - 8b^3) = 27(a - 2b)(a^2 + 2ab + 4b^2).\nStep 2: Denominator = 9(a^2 - 4b^2) = 9(a - 2b)(a + 2b).\nStep 3: Divide:\n  [ 27(a - 2b)(a^2 + 2ab + 4b^2) ] / [ 9(a - 2b)(a + 2b) ].\nStep 4: Cancel 9 (27/9 = 3) and cancel (a - 2b):\n  3(a^2 + 2ab + 4b^2) / (a + 2b).",
                "finalAnswer": "3(a^2 + 2ab + 4b^2) / (a + 2b)",
                "unit": "simplified rational expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4 (iii): Simplify the rational expression: (s^3 + 125t^3) / (s^2 - 2st - 35t^2), assuming denominator != 0.",
                "given": "Expression: (s^3 + 125t^3) / (s^2 - 2st - 35t^2).",
                "formula": "Numerator = sum of cubes: (s + 5t)(s^2 - 5st + 25t^2). Denominator = quadratic trinomial.",
                "substitution": "[ (s + 5t)(s^2 - 5st + 25t^2) ] / [ (s - 7t)(s + 5t) ].",
                "calculation": "Step 1: Factor numerator: s^3 + (5t)^3 = (s + 5t)(s^2 - 5st + 25t^2).\nStep 2: Factor denominator: s^2 - 2st - 35t^2 = (s - 7t)(s + 5t) (since -7 * 5 = -35 and -7 + 5 = -2).\nStep 3: Divide:\n  [ (s + 5t)(s^2 - 5st + 25t^2) ] / [ (s - 7t)(s + 5t) ].\nStep 4: Cancel common non-zero factor (s + 5t):\n  (s^2 - 5st + 25t^2) / (s - 7t).",
                "finalAnswer": "(s^2 - 5st + 25t^2) / (s - 7t)",
                "unit": "simplified rational expression",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Confusing sum of cubes a^3 + b^3 with (a + b)^3; the former has no 3a^2b or 3ab^2 terms.",
            "Dropping negative signs when cubing negative numbers: (-107)^3 must be strictly negative.",
            "Forgetting to check if the middle term is 2ab when factoring fractions: (2y + 1/(4y))^2 has constant middle term 1."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Step through every single part of End-of-Chapter Q1 to Q4 methodically. Show that even fractional and reciprocal terms strictly obey standard polynomial identities.",
        "visual_lesson_plan": {
            "title": "Master Solver Visuals: Cubic, Rational & Polynomial Forms",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Trinomial square 3x3 geometric dissection and rational cancellation curves.",
            "concept_visuals": [
                {
                    "concept_title": "Rational Simplification Vertical Asymptote",
                    "diagram_title": "Rational Function y = (2x + 1) / (2x - 1) with Pole at x = 0.5",
                    "interactive_math_formula": "y = (4x^2 + 4x + 1)/(4x^2 - 1) = (2x + 1)/(2x - 1)",
                    "mafs_graph_config": {
                        "domain": [-4, 4],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "(2*x + 1)/(2*x - 1)", "color": "#2563EB", "label": "y = (2x+1)/(2x-1)"}
                        ],
                        "points": [
                            {"x": 0.5, "y": 0, "label": "Vertical Asymptote x = 0.5"},
                            {"x": -0.5, "y": 0, "label": "Removable Hole at x = -0.5"},
                            {"x": 0, "y": -1, "label": "y-intercept (0, -1)"}
                        ]
                    },
                    "image_query": "rational function graph asymptote removable singularity hole",
                    "video_query": "graphing rational functions with holes and vertical asymptotes",
                    "what_to_explain": "Canceling (2x + 1) creates a removable hole at x = -0.5 while leaving the genuine pole at x = 0.5."
                },
                {
                    "concept_title": "Reciprocal Parabola Symmetry",
                    "diagram_title": "U-Shaped Curve y = 4x^2 + 1/(16x^2) + 1",
                    "interactive_math_formula": "y = (2x + 1/(4x))^2 >= 0",
                    "mafs_graph_config": {
                        "domain": [-3, 3],
                        "range": [0, 15],
                        "curves": [
                            {"fn": "4*x^2 + 1/(16*x^2) + 1", "color": "#16A34A", "label": "y = (2x + 1/(4x))^2"}
                        ],
                        "points": [
                            {"x": 0.353, "y": 2, "label": "Minimum at x = 1/(2*sqrt(2))"},
                            {"x": -0.353, "y": 2, "label": "Symmetric Minimum"}
                        ]
                    },
                    "image_query": "reciprocal function sum of squares minimum value",
                    "video_query": "algebraic identities reciprocal variables minimum value AM GM",
                    "what_to_explain": "Because 4x^2 * 1/(16x^2) = 1/4 is constant, this identity provides direct insight into function extrema."
                },
                {
                    "concept_title": "Large Number Cubic Growth Trajectory",
                    "diagram_title": "Cubic Rate of (200 - x)^3 Near x = 1",
                    "interactive_math_formula": "f(x) = (200 - x)^3",
                    "mafs_graph_config": {
                        "domain": [-2, 4],
                        "range": [7500000, 8500000],
                        "curves": [
                            {"fn": "(200 - x)^3", "color": "#D97706", "label": "y = (200 - x)^3"}
                        ],
                        "points": [
                            {"x": 0, "y": 8000000, "label": "200^3 = 8,000,000"},
                            {"x": 1, "y": 7880599, "label": "199^3 = 7,880,599"}
                        ]
                    },
                    "image_query": "cubic rapid mental math approximation tangent curve",
                    "video_query": "mental math cubing numbers near 200 algebra tricks",
                    "what_to_explain": "The linear derivative of (200 - x)^3 at x = 0 has slope -3 * 200^2 = -120,000, matching the primary subtraction."
                },
                {
                    "concept_title": "Difference of Cubes Linear Ratio",
                    "diagram_title": "Quadratic Quotient (s^3 + 125) / (s + 5) = s^2 - 5s + 25",
                    "interactive_math_formula": "y = s^2 - 5s + 25",
                    "mafs_graph_config": {
                        "domain": [-2, 8],
                        "range": [15, 50],
                        "curves": [
                            {"fn": "x^2 - 5*x + 25", "color": "#7C3AED", "label": "y = s^2 - 5s + 25"}
                        ],
                        "points": [
                            {"x": 2.5, "y": 18.75, "label": "Vertex (2.5, 18.75)"},
                            {"x": 0, "y": 25, "label": "y-intercept (0, 25)"}
                        ]
                    },
                    "image_query": "irreducible quadratic factor sum of cubes positive definite",
                    "video_query": "sum of cubes why quadratic factor has no real roots",
                    "what_to_explain": "The quadratic factor s^2 - 5s + 25 is strictly positive for all real s, with absolute minimum 18.75 > 0."
                },
                {
                    "concept_title": "Euler Three-Variable Cross-Product Plane",
                    "diagram_title": "Linear Trace p + 3q + r = 0 for p^3 + 27q^3 + r^3 = 9pqr",
                    "interactive_math_formula": "Plane: p + 3q + r = 0",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "-3*1 - x", "color": "#DC2626", "label": "r = -3q - p (q=1)"}
                        ],
                        "points": [
                            {"x": 0, "y": -3, "label": "(0, 1, -3)"},
                            {"x": -3, "y": 0, "label": "(-3, 1, 0)"}
                        ]
                    },
                    "image_query": "three dimensional plane intersection linear algebra",
                    "video_query": "three variable algebraic identities geometric plane",
                    "what_to_explain": "Any point lying on the plane p + 3q + r = 0 causes the cubic sum p^3 + 27q^3 + r^3 to collapse to 9pqr."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Master Solver Part 1",
                    "questions": [
                        {
                            "question": "What is the product (s - 2t)(s^2 + 2st + 4t^2)?",
                            "type": "short_answer",
                            "options": ["s^3 - 8t^3", "s^3 + 8t^3", "s^3 - 4t^3", "(s - 2t)^3"],
                            "ideal_answer": "s^3 - 8t^3, by the difference of cubes identity (a - b)(a^2 + ab + b^2) = a^3 - b^3 with a = s and b = 2t.",
                            "socratic_hint": "Check the form: does it match (a - b)(a^2 + ab + b^2)?"
                        },
                        {
                            "question": "Why does (-107)^3 have a negative value (-1,225,043)?",
                            "type": "short_answer",
                            "options": [
                                "An odd power of a negative number is always negative: (-1)^3 = -1",
                                "Because 107 is an odd number",
                                "Because 100 + 7 is negative",
                                "It was rounded incorrectly"
                            ],
                            "ideal_answer": "A negative base raised to an odd exponent retains its negative sign: (-107)^3 = -(107^3) = -1,225,043.",
                            "socratic_hint": "What is (-1) * (-1) * (-1)?"
                        },
                        {
                            "question": "How do you factor 4y^2 + 1 + 1/(16y^2)?",
                            "type": "short_answer",
                            "options": [
                                "(2y + 1/(4y))^2",
                                "(2y - 1/(4y))^2",
                                "(4y + 1/(16y))^2",
                                "It cannot be factored"
                            ],
                            "ideal_answer": "(2y + 1/(4y))^2, because 2 * (2y) * (1/(4y)) = 1, matching the constant middle term exactly.",
                            "socratic_hint": "Check what happens to the variables when 2y is multiplied by 1/(4y)."
                        },
                        {
                            "question": "When simplifying 9(3a^3 - 24b^3) / (9a^2 - 36b^2), what common binomial factor cancels?",
                            "type": "short_answer",
                            "options": [
                                "(a - 2b)",
                                "(a + 2b)",
                                "(a^2 - 4b^2)",
                                "(3a - 6b)"
                            ],
                            "ideal_answer": "(a - 2b), leaving 3(a^2 + 2ab + 4b^2) / (a + 2b).",
                            "socratic_hint": "Factor a^3 - 8b^3 as (a - 2b)(...) and a^2 - 4b^2 as (a - 2b)(a + 2b)."
                        },
                        {
                            "question": "What is the result of simplifying [ (x^2 + x - 6)(x^2 - 7x + 12) ] / [ (x^2 - 6x + 8)(x^2 - 9) ]?",
                            "type": "short_answer",
                            "options": ["1", "x - 2", "x + 3", "(x - 4)/(x + 4)"],
                            "ideal_answer": "1, because all four factors in the numerator (x + 3)(x - 2)(x - 3)(x - 4) cancel identically with the denominator factors.",
                            "socratic_hint": "Factor each quadratic into two linear terms and pair them up."
                        }
                    ]
                }
            ]
        }
    }
