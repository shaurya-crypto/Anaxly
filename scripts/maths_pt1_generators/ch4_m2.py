"""
Chapter 4: Exploring Algebraic Identities - Module 2
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_algebraic_dissection_svg

def get_m2():
    m2_svg = build_algebraic_dissection_svg(
        type_ident='a_minus_b_sq', a_val=130, b_val=50,
        title="Geometric Proof: (a - b)^2 = a^2 - 2ab + b^2",
        caption="Outer square a^2 with two ab rectangles removed, adding back overlapped b^2"
    )

    return {
        "order_index": 2,
        "title": "Difference of Binomials (a - b)^2, Trinomial Squares (a + b + c)^2, Difference of Squares & Sections 4.2 & 4.3",
        "description": "Master the difference of binomials (a - b)^2, trinomial square identity (a + b + c)^2, and difference of squares a^2 - b^2 = (a - b)(a + b). Explore Śhrīdharāchārya's ancient rapid squaring method a^2 = (a + b)(a - b) + b^2 and factorise complex multi-variable polynomials with 100% textbook coverage.",
        "subtopics": [
            "Geometric subtraction model for (a - b)^2 = a^2 - 2ab + b^2",
            "Trinomial square expansion: (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca",
            "Handling negative terms in trinomial squares via sign distribution",
            "Recognising perfect square trinomials in reverse for factorisation",
            "Factoring algebraic expressions with fractional coefficients and common factors",
            "Difference of two squares a^2 - b^2 = (a + b)(a - b) and Śhrīdharāchārya's 750 CE algorithm",
            "Complete step-by-step solutions to in-text Examples 5 to 9, Exercises 4.2, and Exercises 4.3"
        ],
        "key_concepts": [
            "Square of a Difference: (a - b)^2 = a^2 - 2ab + b^2. Geometrically, removing two strips of area ab from a square of side a subtracts the corner square b^2 twice, requiring b^2 to be added back.",
            "Trinomial Square Identity: (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca. Partitions a 3x3 geometric square into 3 square regions and 6 rectangular regions (3 pairs of congruent rectangles).",
            "Sign Invariance in Factoring: Since (-x)^2 = x^2, a negative cross-term indicates that one of the constituent terms has opposite sign.",
            "Common Factor Extraction Invariant: Always inspect for a greatest common numerical or variable factor (e.g. factoring out 2 in 50p^2 + 60pq + 18q^2) before applying binomial identities.",
            "Śhrīdharāchārya's Squaring Method (750 CE): a^2 = (a + b)(a - b) + b^2. Choosing b such that (a + b) or (a - b) is a multiple of 10 transforms squaring into single-digit mental multiplication."
        ],
        "success_criteria": "Expand and factor any binomial or trinomial square, correctly distribute positive and negative signs, and apply Śhrīdharāchārya's rule to evaluate squares of numbers mentally.",
        "chapter_notes": "Pay special attention to Exercises 4.2 Q1 (v) and (vi) where non-integer leading coefficients require pulling out a rational factor (1/3 or 1/5) before factoring.",
        "worked_examples": [
            {
                "problem": "Textbook Example 5: Factor the algebraic expression x^2 + 4x + 4 using identities.",
                "given": "Expression: x^2 + 4x + 4.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "x^2 + 2(x)(2) + 2^2 with a = x and b = 2.",
                "calculation": "Step 1: Check if the first term is a square: x^2 = (x)^2, so a = x.\nStep 2: Check if the last term is a square: 4 = 2^2, so b = 2.\nStep 3: Check the middle term: 2ab = 2 * (x) * (2) = 4x. This matches the given middle term.\nStep 4: Write in factored form: (x + 2)^2 = (x + 2)(x + 2).",
                "finalAnswer": "x^2 + 4x + 4 = (x + 2)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 6: Factor 36x^2 + 12x + 1.",
                "given": "Expression: 36x^2 + 12x + 1.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(6x)^2 + 2(6x)(1) + 1^2 with a = 6x and b = 1.",
                "calculation": "Step 1: Identify first square: 36x^2 = (6x)^2, so a = 6x.\nStep 2: Identify last square: 1 = 1^2, so b = 1.\nStep 3: Check middle term: 2ab = 2 * (6x) * (1) = 12x. Matches exactly.\nStep 4: Factor: (6x + 1)^2.",
                "finalAnswer": "36x^2 + 12x + 1 = (6x + 1)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 7: Factor 50p^2 + 60pq + 18q^2 by taking out common factors.",
                "given": "Expression: 50p^2 + 60pq + 18q^2.",
                "formula": "Extract GCF, then apply a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "2 * [25p^2 + 30pq + 9q^2] = 2 * [(5p)^2 + 2(5p)(3q) + (3q)^2].",
                "calculation": "Step 1: Observe that 50 is not a perfect square integer, but all coefficients (50, 60, 18) are even.\nStep 2: Factor out the common numerical factor 2: 2(25p^2 + 30pq + 9q^2).\nStep 3: In the bracketed trinomial, set a = 5p and b = 3q.\nStep 4: Check cross term: 2 * (5p) * (3q) = 30pq. Matches perfectly.\nStep 5: Factor the bracket: 2(5p + 3q)^2.",
                "finalAnswer": "50p^2 + 60pq + 18q^2 = 2(5p + 3q)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 8: Calculate 29^2 without multiplying directly, using the identity for (a - b)^2.",
                "given": "Number to square: 29.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2, with 29 = 30 - 1.",
                "substitution": "(30 - 1)^2 = 30^2 - 2*(30)*(1) + 1^2.",
                "calculation": "Step 1: Express 29 as the difference from a multiple of 10: 29 = 30 - 1.\nStep 2: Identify a = 30 and b = 1.\nStep 3: Evaluate 30^2 = 900.\nStep 4: Evaluate cross term: 2 * 30 * 1 = 60.\nStep 5: Evaluate 1^2 = 1.\nStep 6: Combine: 900 - 60 + 1 = 840 + 1 = 841.",
                "finalAnswer": "29^2 = 841",
                "unit": "integer",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m2_svg
            },
            {
                "problem": "Textbook Example 9: Use the trinomial square identity to calculate 119^2.",
                "given": "Number to square: 119.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca, with 119 = 100 + 10 + 9.",
                "substitution": "(100 + 10 + 9)^2 = 100^2 + 10^2 + 9^2 + 2(100)(10) + 2(100)(9) + 2(10)(9).",
                "calculation": "Step 1: Decompose 119 into hundreds, tens, and units: 100 + 10 + 9.\nStep 2: Compute individual squares: 100^2 = 10,000; 10^2 = 100; 9^2 = 81. Sum of squares = 10,181.\nStep 3: Compute pairwise cross terms:\n  - 2 * 100 * 10 = 2,000\n  - 2 * 100 * 9 = 1,800\n  - 2 * 10 * 9 = 180\n  Sum of cross terms = 2,000 + 1,800 + 180 = 3,980.\nStep 4: Sum all components: 10,181 + 3,980 = 14,161.",
                "finalAnswer": "119^2 = 14,161",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q1 (i): Factor completely: 9x^2 + 24xy + 16y^2.",
                "given": "Expression: 9x^2 + 24xy + 16y^2.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(3x)^2 + 2*(3x)*(4y) + (4y)^2 with a = 3x, b = 4y.",
                "calculation": "Step 1: Identify terms: a^2 = (3x)^2 => a = 3x; b^2 = (4y)^2 => b = 4y.\nStep 2: Verify cross term: 2 * (3x) * (4y) = 24xy. Matches given middle term.\nStep 3: Write in factored form: (3x + 4y)^2.",
                "finalAnswer": "9x^2 + 24xy + 16y^2 = (3x + 4y)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q1 (ii): Factor completely: 4s^2 + 20st + 25t^2.",
                "given": "Expression: 4s^2 + 20st + 25t^2.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(2s)^2 + 2*(2s)*(5t) + (5t)^2 with a = 2s, b = 5t.",
                "calculation": "Step 1: Identify terms: a = 2s, b = 5t.\nStep 2: Check cross term: 2 * 2s * 5t = 20st. Matches middle term.\nStep 3: Factor: (2s + 5t)^2.",
                "finalAnswer": "4s^2 + 20st + 25t^2 = (2s + 5t)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q1 (iii): Factor completely: 49x^2 + 28xy + 4y^2.",
                "given": "Expression: 49x^2 + 28xy + 4y^2.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(7x)^2 + 2*(7x)*(2y) + (2y)^2 with a = 7x, b = 2y.",
                "calculation": "Step 1: Identify terms: a = 7x, b = 2y.\nStep 2: Check cross term: 2 * 7x * 2y = 28xy. Matches.\nStep 3: Factor: (7x + 2y)^2.",
                "finalAnswer": "49x^2 + 28xy + 4y^2 = (7x + 2y)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q1 (iv): Factor completely: 64p^2 + (32/3) pq + (4/9) q^2.",
                "given": "Expression: 64p^2 + (32/3) pq + (4/9) q^2.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(8p)^2 + 2*(8p)*(2/3 q) + (2/3 q)^2 with a = 8p, b = 2/3 q.",
                "calculation": "Step 1: Identify first square: 64p^2 = (8p)^2 => a = 8p.\nStep 2: Identify last square: (4/9)q^2 = (2/3 q)^2 => b = 2/3 q.\nStep 3: Check middle term: 2 * (8p) * (2/3 q) = (32/3) pq. Matches exactly.\nStep 4: Factor: (8p + 2/3 q)^2.",
                "finalAnswer": "64p^2 + 32/3 pq + 4/9 q^2 = (8p + 2/3 q)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q1 (v): Factor completely: 3a^2 + 4ab + (4/3) b^2.",
                "given": "Expression: 3a^2 + 4ab + (4/3) b^2.",
                "formula": "Extract common factor 1/3, then apply a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(1/3) * [9a^2 + 12ab + 4b^2] = (1/3) * [(3a)^2 + 2(3a)(2b) + (2b)^2].",
                "calculation": "Step 1: Notice 3 is not a perfect square. Factor out 1/3: 1/3 * (9a^2 + 12ab + 4b^2).\nStep 2: In the brackets, a = 3a and b = 2b.\nStep 3: Check middle term: 2 * 3a * 2b = 12ab. Matches.\nStep 4: Factor the quadratic: 1/3 * (3a + 2b)^2.",
                "finalAnswer": "3a^2 + 4ab + 4/3 b^2 = 1/3 (3a + 2b)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q1 (vi): Factor completely: (9/5) s^2 + 6sv + 5v^2.",
                "given": "Expression: (9/5) s^2 + 6sv + 5v^2.",
                "formula": "Extract common factor 1/5, then apply a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(1/5) * [9s^2 + 30sv + 25v^2] = (1/5) * [(3s)^2 + 2(3s)(5v) + (5v)^2].",
                "calculation": "Step 1: Factor out 1/5: 1/5 * (9s^2 + 30sv + 25v^2).\nStep 2: Identify terms: a = 3s and b = 5v.\nStep 3: Check middle term: 2 * (3s) * (5v) = 30sv. Matches.\nStep 4: Factor: 1/5 * (3s + 5v)^2.",
                "finalAnswer": "9/5 s^2 + 6sv + 5v^2 = 1/5 (3s + 5v)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q2 (i): Find the value of (79)^2 using the identity (a - b)^2 = a^2 - 2ab + b^2.",
                "given": "Number: 79 = 80 - 1.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "(80 - 1)^2 = 80^2 - 2*(80)*(1) + 1^2.",
                "calculation": "Step 1: 80^2 = 6400.\nStep 2: 2 * 80 * 1 = 160.\nStep 3: 1^2 = 1.\nStep 4: Evaluate: 6400 - 160 + 1 = 6240 + 1 = 6241.",
                "finalAnswer": "79^2 = 6241",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q2 (ii): Find the value of (193)^2 using the identity (a - b)^2 = a^2 - 2ab + b^2.",
                "given": "Number: 193 = 200 - 7.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "(200 - 7)^2 = 200^2 - 2*(200)*(7) + 7^2.",
                "calculation": "Step 1: 200^2 = 40,000.\nStep 2: 2 * 200 * 7 = 2,800.\nStep 3: 7^2 = 49.\nStep 4: Evaluate: 40,000 - 2,800 + 49 = 37,200 + 49 = 37,249.",
                "finalAnswer": "193^2 = 37,249",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q2 (iii): Find the value of (299)^2 using the identity (a - b)^2 = a^2 - 2ab + b^2.",
                "given": "Number: 299 = 300 - 1.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "(300 - 1)^2 = 300^2 - 2*(300)*(1) + 1^2.",
                "calculation": "Step 1: 300^2 = 90,000.\nStep 2: 2 * 300 * 1 = 600.\nStep 3: 1^2 = 1.\nStep 4: Evaluate: 90,000 - 600 + 1 = 89,400 + 1 = 89,401.",
                "finalAnswer": "299^2 = 89,401",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q1 (i): Find 117^2 using a suitable identity.",
                "given": "Number: 117 = 100 + 17 (or 120 - 3).",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2, with 120 - 3.",
                "substitution": "(120 - 3)^2 = 120^2 - 2*(120)*(3) + 3^2.",
                "calculation": "Step 1: 120^2 = 14,400.\nStep 2: 2 * 120 * 3 = 720.\nStep 3: 3^2 = 9.\nStep 4: Evaluate: 14,400 - 720 + 9 = 13,680 + 9 = 13,689.",
                "finalAnswer": "117^2 = 13,689",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q1 (ii): Find 78^2 using a suitable identity.",
                "given": "Number: 78 = 80 - 2.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "(80 - 2)^2 = 80^2 - 2*(80)*(2) + 2^2.",
                "calculation": "Step 1: 80^2 = 6400.\nStep 2: 2 * 80 * 2 = 320.\nStep 3: 2^2 = 4.\nStep 4: Evaluate: 6400 - 320 + 4 = 6080 + 4 = 6084.",
                "finalAnswer": "78^2 = 6084",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q1 (iii): Find 198^2 using a suitable identity.",
                "given": "Number: 198 = 200 - 2.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "(200 - 2)^2 = 200^2 - 2*(200)*(2) + 2^2.",
                "calculation": "Step 1: 200^2 = 40,000.\nStep 2: 2 * 200 * 2 = 800.\nStep 3: 2^2 = 4.\nStep 4: Evaluate: 40,000 - 800 + 4 = 39,200 + 4 = 39,204.",
                "finalAnswer": "198^2 = 39,204",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q1 (iv): Find 214^2 using a suitable identity.",
                "given": "Number: 214 = 200 + 14.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2.",
                "substitution": "(200 + 14)^2 = 200^2 + 2*(200)*(14) + 14^2.",
                "calculation": "Step 1: 200^2 = 40,000.\nStep 2: 2 * 200 * 14 = 5,600.\nStep 3: 14^2 = 196.\nStep 4: Evaluate: 40,000 + 5,600 + 196 = 45,796.",
                "finalAnswer": "214^2 = 45,796",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q1 (v): Find 1104^2 using a suitable identity.",
                "given": "Number: 1104 = 1100 + 4.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2.",
                "substitution": "(1100 + 4)^2 = 1100^2 + 2*(1100)*(4) + 4^2.",
                "calculation": "Step 1: 1100^2 = 1,210,000.\nStep 2: 2 * 1100 * 4 = 8,800.\nStep 3: 4^2 = 16.\nStep 4: Evaluate: 1,210,000 + 8,800 + 16 = 1,218,816.",
                "finalAnswer": "1104^2 = 1,218,816",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q1 (vi): Find 1120^2 using a suitable identity.",
                "given": "Number: 1120 = 1100 + 20.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2.",
                "substitution": "(1100 + 20)^2 = 1100^2 + 2*(1100)*(20) + 20^2.",
                "calculation": "Step 1: 1100^2 = 1,210,000.\nStep 2: 2 * 1100 * 20 = 44,000.\nStep 3: 20^2 = 400.\nStep 4: Evaluate: 1,210,000 + 44,000 + 400 = 1,254,400.",
                "finalAnswer": "1120^2 = 1,254,400",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q2 (i): Factor using suitable identities: 16y^2 - 24y + 9.",
                "given": "Expression: 16y^2 - 24y + 9.",
                "formula": "a^2 - 2ab + b^2 = (a - b)^2.",
                "substitution": "(4y)^2 - 2*(4y)*(3) + 3^2 with a = 4y, b = 3.",
                "calculation": "Step 1: a^2 = (4y)^2 => a = 4y.\nStep 2: b^2 = 3^2 => b = 3.\nStep 3: 2ab = 2 * (4y) * 3 = 24y. Sign is negative.\nStep 4: Factor: (4y - 3)^2.",
                "finalAnswer": "16y^2 - 24y + 9 = (4y - 3)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q2 (ii): Factor using suitable identities: (9/4) s^2 + 6st + 4t^2.",
                "given": "Expression: (9/4) s^2 + 6st + 4t^2.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "(3/2 s)^2 + 2*(3/2 s)*(2t) + (2t)^2 with a = 3/2 s, b = 2t.",
                "calculation": "Step 1: a = 3/2 s, b = 2t.\nStep 2: Cross term: 2 * (3/2 s) * (2t) = 6st. Matches.\nStep 3: Factor: (3/2 s + 2t)^2.",
                "finalAnswer": "9/4 s^2 + 6st + 4t^2 = (3/2 s + 2t)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q2 (iii): Factor: m^2/9 + mk/3 + k^2/4 + 3nk + 2mn + 9n^2.",
                "given": "Six-term expression: m^2/9 + k^2/4 + 9n^2 + mk/3 + 3nk + 2mn.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca.",
                "substitution": "(m/3)^2 + (k/2)^2 + (3n)^2 + 2(m/3)(k/2) + 2(k/2)(3n) + 2(m/3)(3n).",
                "calculation": "Step 1: Identify squares: a = m/3, b = k/2, c = 3n.\nStep 2: Check cross terms:\n  - 2ab = 2 * (m/3) * (k/2) = mk/3\n  - 2bc = 2 * (k/2) * (3n) = 3nk\n  - 2ca = 2 * (3n) * (m/3) = 2mn\nStep 3: All terms match the given expression exactly.\nStep 4: Factor: (m/3 + k/2 + 3n)^2.",
                "finalAnswer": "(m/3 + k/2 + 3n)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q2 (iv): Factor: p^2/16 - 2 + 16/p^2.",
                "given": "Expression: (p/4)^2 - 2 + (4/p)^2.",
                "formula": "a^2 - 2ab + b^2 = (a - b)^2 with a = p/4, b = 4/p.",
                "substitution": "(p/4)^2 - 2*(p/4)*(4/p) + (4/p)^2.",
                "calculation": "Step 1: Identify a = p/4, b = 4/p.\nStep 2: Compute cross term: 2 * (p/4) * (4/p) = 2. Negative sign gives -2.\nStep 3: Factor: (p/4 - 4/p)^2.",
                "finalAnswer": "p^2/16 - 2 + 16/p^2 = (p/4 - 4/p)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q2 (v): Factor: 9a^2 + 4b^2 + c^2 - 12ab + 6ac - 4bc.",
                "given": "Expression: 9a^2 + 4b^2 + c^2 - 12ab + 6ac - 4bc.",
                "formula": "(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx.",
                "substitution": "(3a)^2 + (-2b)^2 + (c)^2 + 2(3a)(-2b) + 2(-2b)(c) + 2(3a)(c).",
                "calculation": "Step 1: Squares: (3a)^2, (2b)^2, (c)^2.\nStep 2: Analyze negative cross terms: -12ab and -4bc are negative, while 6ac is positive. This means 3a and c share the same sign, while 2b has the opposite sign.\nStep 3: Choose x = 3a, y = -2b, z = c.\nStep 4: Verify cross terms: 2(3a)(-2b) = -12ab; 2(-2b)(c) = -4bc; 2(3a)(c) = 6ac.\nStep 5: Factor: (3a - 2b + c)^2.",
                "finalAnswer": "(3a - 2b + c)^2",
                "unit": "factored form",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q3 (i): Expand using (a + b + c)^2: (p + 3q + 7r)^2.",
                "given": "Trinomial: (p + 3q + 7r)^2.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca.",
                "substitution": "p^2 + (3q)^2 + (7r)^2 + 2(p)(3q) + 2(3q)(7r) + 2(p)(7r).",
                "calculation": "Step 1: Squares: p^2, 9q^2, 49r^2.\nStep 2: Cross terms: 2(p)(3q) = 6pq; 2(3q)(7r) = 42qr; 2(p)(7r) = 14pr.\nStep 3: Combine all terms: p^2 + 9q^2 + 49r^2 + 6pq + 42qr + 14pr.",
                "finalAnswer": "p^2 + 9q^2 + 49r^2 + 6pq + 42qr + 14pr",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q3 (ii): Expand using (a + b + c)^2: (3x - 2y + 4z)^2.",
                "given": "Trinomial: (3x - 2y + 4z)^2.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca with a = 3x, b = -2y, c = 4z.",
                "substitution": "(3x)^2 + (-2y)^2 + (4z)^2 + 2(3x)(-2y) + 2(-2y)(4z) + 2(3x)(4z).",
                "calculation": "Step 1: Squares: 9x^2 + 4y^2 + 16z^2.\nStep 2: Cross terms: 2(3x)(-2y) = -12xy; 2(-2y)(4z) = -16yz; 2(3x)(4z) = 24xz.\nStep 3: Combine: 9x^2 + 4y^2 + 16z^2 - 12xy - 16yz + 24xz.",
                "finalAnswer": "9x^2 + 4y^2 + 16z^2 - 12xy - 16yz + 24xz",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q4: Is this an identity? (a + b - c)^2 + (a - b + c)^2 + (a - b - c)^2 = 2a^2 + 2b^2 + 2c^2. Justify your answer.",
                "given": "Proposed equation: (a + b - c)^2 + (a - b + c)^2 + (a - b - c)^2 = 2a^2 + 2b^2 + 2c^2.",
                "formula": "Expand each trinomial using (x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx.",
                "substitution": "LHS = (a^2+b^2+c^2 + 2ab - 2bc - 2ca) + (a^2+b^2+c^2 - 2ab - 2bc + 2ca) + (a^2+b^2+c^2 - 2ab + 2bc + 2ca).",
                "calculation": "Step 1: Sum the squared terms: 3a^2 + 3b^2 + 3c^2.\nStep 2: Sum the cross terms:\n  - ab terms: 2ab - 2ab - 2ab = -2ab.\n  - bc terms: -2bc - 2bc + 2bc = -2bc.\n  - ca terms: -2ca + 2ca + 2ca = +2ca.\nStep 3: LHS simplifies to 3a^2 + 3b^2 + 3c^2 - 2ab - 2bc + 2ca.\nStep 4: Compare with RHS = 2a^2 + 2b^2 + 2c^2. Since 3a^2 + 3b^2 + 3c^2 - 2ab - 2bc + 2ca != 2a^2 + 2b^2 + 2c^2 for all a,b,c (for example at a=1,b=1,c=1: LHS = 1 + 1 + 1 = 3, while RHS = 2(1)+2(1)+2(1) = 6 != 3).\nStep 5: Conclude that it is NOT an identity.",
                "finalAnswer": "No, it is not an identity because LHS = 3a^2 + 3b^2 + 3c^2 - 2ab - 2bc + 2ca != 2a^2 + 2b^2 + 2c^2",
                "unit": "mathematical justification",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Think & Reflect 1: Using Śhrīdharāchārya's identity a^2 = (a + b)(a - b) + b^2 with b = 5, evaluate: (i) 35^2, (ii) 65^2, (iii) 85^2, (iv) 105^2. State the general pattern.",
                "given": "Numbers: 35, 65, 85, 105. Identity: a^2 = (a + 5)(a - 5) + 25.",
                "formula": "a^2 = (a + 5)(a - 5) + 25. For any two-digit number ending in 5, (10n + 5)^2 = 100n(n + 1) + 25.",
                "substitution": "(i) 40*30 + 25; (ii) 70*60 + 25; (iii) 90*80 + 25; (iv) 110*100 + 25.",
                "calculation": "Part (i): 35^2 = (35 + 5)(35 - 5) + 5^2 = 40 * 30 + 25 = 1200 + 25 = 1225.\nPart (ii): 65^2 = (65 + 5)(65 - 5) + 5^2 = 70 * 60 + 25 = 4200 + 25 = 4225.\nPart (iii): 85^2 = (85 + 5)(85 - 5) + 5^2 = 90 * 80 + 25 = 7200 + 25 = 7225.\nPart (iv): 105^2 = (105 + 5)(105 - 5) + 5^2 = 110 * 100 + 25 = 11000 + 25 = 11025.\nGeneral Pattern: Any number ending in 5 with tens part n has square equal to [n * (n + 1)] followed by 25.",
                "finalAnswer": "(i) 35^2 = 1225; (ii) 65^2 = 4225; (iii) 85^2 = 7225; (iv) 105^2 = 11025. Pattern: n(n+1) followed by 25",
                "unit": "integers and algebraic rule",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Think & Reflect 2: Geometrically justify the algebraic identity (a + b + c)(a + b - c) = (a + b)^2 - c^2 using the difference of squares model.",
                "given": "Expression: (a + b + c)(a + b - c).",
                "formula": "(X + c)(X - c) = X^2 - c^2, letting X = a + b.",
                "substitution": "((a + b) + c)((a + b) - c) = (a + b)^2 - c^2.",
                "calculation": "Step 1: Group the first two terms: let X = (a + b).\nStep 2: The product becomes (X + c)(X - c).\nStep 3: By the difference of squares identity, (X + c)(X - c) = X^2 - c^2.\nStep 4: Substitute back X = (a + b): (a + b)^2 - c^2.\nStep 5: Geometrically, take a square of side (a + b) and remove a corner square of side c. The remaining L-shaped region can be cut and rearranged into a rectangle of length (a + b + c) and width (a + b - c).",
                "finalAnswer": "(a + b + c)(a + b - c) = (a + b)^2 - c^2, proven via difference of squares on X = a + b",
                "unit": "geometric proof",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting to add back b^2 in (a - b)^2 = a^2 - 2ab + b^2, yielding negative areas or incorrect arithmetic.",
            "Misinterpreting signs in trinomial expansions like (3x - 2y + 4z)^2 by making all cross terms negative.",
            "Failing to factor out a common numerical constant first in expressions like 50p^2 + 60pq + 18q^2."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Present (a - b)^2 by subtracting two strips of width b from an a*a square, showing the overlapping b^2 region that must be added back. Then introduce Śhrīdharāchārya's 750 CE algorithm.",
        "visual_lesson_plan": {
            "title": "Geometric Model of (a - b)^2 & Trinomial Dissection",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Dissected square for (a - b)^2 showing overlap correction b^2.",
            "concept_visuals": [
                {
                    "concept_title": "Geometric Subtraction Model (a - b)^2",
                    "diagram_title": "Area Overlap Correction b^2",
                    "interactive_math_formula": "(a - b)^2 = a^2 - 2ab + b^2",
                    "mafs_graph_config": {
                        "domain": [-1, 6],
                        "range": [-1, 25],
                        "curves": [
                            {"fn": "(x - 3)^2", "color": "#2563EB", "label": "y = (x - 3)^2 = x^2 - 6x + 9"},
                            {"fn": "x^2", "color": "#94A3B8", "label": "y = x^2"}
                        ],
                        "points": [
                            {"x": 3, "y": 0, "label": "Vertex (3,0)"},
                            {"x": 0, "y": 9, "label": "y-intercept (0,9)"}
                        ]
                    },
                    "image_query": "algebra difference of squares geometric subtraction area model",
                    "video_query": "geometric visual proof a minus b squared animated",
                    "what_to_explain": "Notice how removing two strips of width 3 creates an overlap of 3^2 = 9 that must be added back, shifting the vertex to (3,0)."
                },
                {
                    "concept_title": "Difference of Two Squares Linearity",
                    "diagram_title": "Symmetric Roots of y = x^2 - b^2",
                    "interactive_math_formula": "y = (x - b)(x + b) = x^2 - b^2",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-16, 20],
                        "curves": [
                            {"fn": "x^2 - 9", "color": "#16A34A", "label": "y = x^2 - 9 = (x - 3)(x + 3)"},
                            {"fn": "x^2 - 16", "color": "#D97706", "label": "y = x^2 - 16 = (x - 4)(x + 4)"}
                        ],
                        "points": [
                            {"x": -3, "y": 0, "label": "Root (-3, 0)"},
                            {"x": 3, "y": 0, "label": "Root (3, 0)"},
                            {"x": 0, "y": -9, "label": "Vertex (0, -9)"}
                        ]
                    },
                    "image_query": "difference of squares parabola roots symmetry",
                    "video_query": "difference of two squares geometric visual transformation",
                    "what_to_explain": "The difference of squares parabola is symmetric about the y-axis, with roots at x = +b and x = -b."
                },
                {
                    "concept_title": "Śhrīdharāchārya Rapid Squaring Path",
                    "diagram_title": "Squaring via a^2 = (a - b)(a + b) + b^2",
                    "interactive_math_formula": "f(b) = (a - b)(a + b) + b^2",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 100],
                        "curves": [
                            {"fn": "(50 - x)*(50 + x) + x^2", "color": "#7C3AED", "label": "Constant 50^2 = 2500"}
                        ],
                        "points": [
                            {"x": 0, "y": 50, "label": "Direct Square b=0"},
                            {"x": 5, "y": 50, "label": "Offset b=5: 55*45 + 25 = 2500"}
                        ]
                    },
                    "image_query": "ancient Indian mathematics Shridharacharya algebra squaring",
                    "video_query": "Shridharacharya rapid mental squaring method history mathematics",
                    "what_to_explain": "The identity proves that no matter which offset b is chosen, (a + b)(a - b) + b^2 exactly reproduces a^2."
                },
                {
                    "concept_title": "Trinomial Dissection 3D Projection",
                    "diagram_title": "Six-Region Partitioning of (a + b + c)^2",
                    "interactive_math_formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)",
                    "mafs_graph_config": {
                        "domain": [0, 8],
                        "range": [0, 64],
                        "curves": [
                            {"fn": "(x + 2 + 1)^2", "color": "#059669", "label": "y = (x + 3)^2"},
                            {"fn": "x^2 + 4 + 1", "color": "#DC2626", "label": "Sum of Squares x^2 + 5"}
                        ],
                        "points": [
                            {"x": 2, "y": 25, "label": "At x=2: (2+3)^2 = 25"},
                            {"x": 2, "y": 9, "label": "Sum of squares = 9 (Gap = 16)"}
                        ]
                    },
                    "image_query": "trinomial square 3x3 grid geometric dissection model",
                    "video_query": "trinomial square expansion geometric visualization",
                    "what_to_explain": "The difference between (a + b + c)^2 and a^2 + b^2 + c^2 is 2(ab + bc + ca), accounting for the 6 rectangular corridors."
                },
                {
                    "concept_title": "Sign Variation Contour in Trinomials",
                    "diagram_title": "Cross Term Sign Behavior for (x - y + z)^2",
                    "interactive_math_formula": "Signs: +x^2 + y^2 + z^2 - 2xy - 2yz + 2xz",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "-2*x*3", "color": "#EA580C", "label": "-2xy (y=3)"},
                            {"fn": "2*x*2", "color": "#0284C7", "label": "+2xz (z=2)"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Origin (0,0)"}
                        ]
                    },
                    "image_query": "algebra sign distribution trinomial squares",
                    "video_query": "how to handle negative signs in trinomial square expansions",
                    "what_to_explain": "A single negative variable causes exactly two of the three cross terms to become negative."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Difference of Binomials and Trinomials",
                    "questions": [
                        {
                            "question": "In the geometric proof of (a - b)^2, why must b^2 be added back?",
                            "type": "short_answer",
                            "options": [
                                "Because the corner region of area b^2 was subtracted twice when removing both ab strips",
                                "Because areas can never be subtracted",
                                "Because b is always a negative length",
                                "It is just an arbitrary convention"
                            ],
                            "ideal_answer": "Removing two rectangular strips of area ab from a square of area a^2 subtracts the overlapping corner square b^2 twice. It must be added back once to obtain the correct net area.",
                            "socratic_hint": "Look at the corner where the horizontal and vertical strips cross."
                        },
                        {
                            "question": "How many total sub-regions are created when a square of side (a + b + c) is partitioned?",
                            "type": "short_answer",
                            "options": ["9 (3 squares and 6 rectangles)", "6", "3", "12"],
                            "ideal_answer": "9 non-overlapping regions: 3 squares (a^2, b^2, c^2) and 6 rectangles (two of ab, two of bc, and two of ca).",
                            "socratic_hint": "A 3-part partition along both dimensions yields 3 x 3 = 9 regions."
                        },
                        {
                            "question": "How did Śhrīdharāchārya calculate 65^2 in 750 CE using an identity?",
                            "type": "short_answer",
                            "options": [
                                "By writing (65 + 5)(65 - 5) + 5^2 = 70 * 60 + 25 = 4225",
                                "By long multiplication: 65 * 65",
                                "By adding 65 sixty-five times",
                                "By subtracting 25 from 65^2"
                            ],
                            "ideal_answer": "Using a^2 = (a + 5)(a - 5) + 25 = 70 * 60 + 25 = 4200 + 25 = 4225.",
                            "socratic_hint": "Round 65 up to 70 and down to 60, then add 5^2."
                        },
                        {
                            "question": "When factoring 50p^2 + 60pq + 18q^2, what is the crucial first step?",
                            "type": "short_answer",
                            "options": [
                                "Factor out the greatest common numerical factor, 2",
                                "Take square roots of 50 and 18 directly",
                                "Subtract 60pq from both sides",
                                "Multiply the entire expression by 2"
                            ],
                            "ideal_answer": "Extract the common factor 2 to get 2(25p^2 + 30pq + 9q^2), exposing the perfect square trinomial (5p + 3q)^2.",
                            "socratic_hint": "Are 50 and 18 perfect square integers? What factor divides all three coefficients?"
                        },
                        {
                            "question": "In the expansion of (3x - 2y + 4z)^2, which cross terms carry a negative sign?",
                            "type": "short_answer",
                            "options": [
                                "The xy and yz terms (-12xy and -16yz)",
                                "All three cross terms",
                                "Only the xz term",
                                "None of the terms"
                            ],
                            "ideal_answer": "The terms involving -2y, specifically 2(3x)(-2y) = -12xy and 2(-2y)(4z) = -16yz. The xz term is positive (+24xz).",
                            "socratic_hint": "Only the term with y is negative, so any product with y will have a negative sign."
                        }
                    ]
                }
            ]
        }
    }
