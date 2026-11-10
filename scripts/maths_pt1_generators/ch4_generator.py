"""
Chapter 4: Exploring Algebraic Identities
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

import json
from .svg_builder import build_algebraic_dissection_svg, get_svg_wrapper

def get_ch4_modules():
    curriculum_id = "cef5b4c4-9fad-4f5b-8201-372cce5f4f61"
    
    # -------------------------------------------------------------
    # MODULE 1: Square Dissections & Identities (a + b)^2
    # -------------------------------------------------------------
    m1_svg = build_algebraic_dissection_svg(
        type_ident='a_plus_b_sq', a_val=130, b_val=60,
        title="Geometric Proof: (a + b)^2 = a^2 + 2ab + b^2",
        caption="Large square decomposed into a^2 (blue), two ab rectangles (green), and b^2 (purple)"
    )

    m1 = {
        "order_index": 1,
        "title": "Geometric Proofs of Binomial Squares: (a + b)^2, Area Dissections & Mental Arithmetic",
        "description": "Understand algebraic identities through geometric dissections. Visualize (a + b)^2 as the area of a square of side (a + b) decomposed into four sub-regions: a^2, two ab rectangles, and b^2. Master rapid mental arithmetic using binomial squares.",
        "subtopics": [
            "Difference between algebraic equations and algebraic identities",
            "Geometric proof of (a + b)^2 = a^2 + 2ab + b^2 via Euclidean area models",
            "Dissection of a square of side (a + b) into four sub-regions: a^2, ab, ab, and b^2",
            "Application to mental arithmetic: (100 + x)^2 and (x + y)^2 expansions",
            "Expansion of fractional and decimal coefficients",
            "Avoiding the universal freshman error: (a + b)^2 != a^2 + b^2"
        ],
        "key_concepts": [
            "Algebraic Identity Definition: An equality that is true for ALL real values of the variables involved, unlike conditional equations which hold only for specific values.",
            "Square of a Binomial Sum: (a + b)^2 = a^2 + 2ab + b^2. Geometrically represents a square of side length (a + b) partitioned into an a*a square, two a*b rectangles, and a b*b square.",
            "Area Conservation Principle: The total area of a composite figure equals the sum of the areas of its non-overlapping constituent parts.",
            "Cross-Term Mandate: The 2ab term (twice the product of the terms) is strictly required by the distributive law (a + b)(a + b) = a(a + b) + b(a + b) = a^2 + ab + ba + b^2.",
            "Mental Arithmetic Decomposition: Evaluating numbers like 104^2 by decomposing them into (100 + 4)^2 = 100^2 + 2(100)(4) + 4^2."
        ],
        "success_criteria": "State and prove (a + b)^2 geometrically, expand any binomial with integer, fractional, or decimal coefficients, and calculate squares of large numbers mentally.",
        "chapter_notes": "Identities are universal mathematical invariants. In Ganita Manjari Chapter 4, every identity is introduced through geometric intuition before formal algebraic manipulation. Never let students omit the cross term 2ab.",
        "worked_examples": [
            {
                "problem": "Textbook Example 1: Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (3x + 2y)^2.",
                "given": "Binomial expression: (3x + 2y)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with a = 3x and b = 2y.",
                "substitution": "(3x + 2y)^2 = (3x)^2 + 2*(3x)*(2y) + (2y)^2.",
                "calculation": "Step 1: Identify terms: a = 3x, b = 2y.\nStep 2: Compute first square: a^2 = (3x)^2 = 3^2 * x^2 = 9x^2.\nStep 3: Compute cross term: 2ab = 2 * (3x) * (2y) = (2 * 3 * 2) * (x * y) = 12xy.\nStep 4: Compute second square: b^2 = (2y)^2 = 2^2 * y^2 = 4y^2.\nStep 5: Combine all terms: 9x^2 + 12xy + 4y^2.",
                "finalAnswer": "(3x + 2y)^2 = 9x^2 + 12xy + 4y^2",
                "unit": "algebraic expression",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m1_svg
            },
            {
                "problem": "Textbook Example 2: Find the value of (104)^2 without multiplying directly.",
                "given": "Number to square: 104.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, decomposing 104 = 100 + 4.",
                "substitution": "(100 + 4)^2 = (100)^2 + 2*(100)*(4) + (4)^2.",
                "calculation": "Step 1: Write 104 as a sum of a base of ten and a small integer: 104 = 100 + 4.\nStep 2: Here a = 100 and b = 4.\nStep 3: Evaluate a^2 = 100^2 = 10,000.\nStep 4: Evaluate 2ab = 2 * 100 * 4 = 800.\nStep 5: Evaluate b^2 = 4^2 = 16.\nStep 6: Sum the components: 10,000 + 800 + 16 = 10,816.",
                "finalAnswer": "(104)^2 = 10,816",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q1 (ii) & (iii): Expand (ii) (7/5 x + 3/2 y)^2 and (iii) (2.5p + 1.5q)^2.",
                "given": "Fractional binomial (7/5 x + 3/2 y)^2 and decimal binomial (2.5p + 1.5q)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2.",
                "substitution": "Part (ii): (7/5 x)^2 + 2*(7/5 x)*(3/2 y) + (3/2 y)^2.\nPart (iii): (2.5p)^2 + 2*(2.5p)*(1.5q) + (1.5q)^2.",
                "calculation": "Part (ii):\nStep 1: (7/5 x)^2 = 49/25 x^2.\nStep 2: 2 * (7/5 x) * (3/2 y) = 2 * (21/10) xy = 21/5 xy.\nStep 3: (3/2 y)^2 = 9/4 y^2.\nSum: 49/25 x^2 + 21/5 xy + 9/4 y^2.\n\nPart (iii):\nStep 1: (2.5p)^2 = 6.25 p^2.\nStep 2: 2 * 2.5p * 1.5q = 5.0 * 1.5 pq = 7.5 pq.\nStep 3: (1.5q)^2 = 2.25 q^2.\nSum: 6.25 p^2 + 7.5 pq + 2.25 q^2.",
                "finalAnswer": "Part (ii): 49/25 x^2 + 21/5 xy + 9/4 y^2; Part (iii): 6.25 p^2 + 7.5 pq + 2.25 q^2",
                "unit": "algebraic expressions",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q2: Find the values using the identity (a + b)^2: (i) (64)^2, (ii) (105)^2, (iii) (205)^2.",
                "given": "Numbers: 64 = 60 + 4, 105 = 100 + 5, 205 = 200 + 5.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2.",
                "substitution": "(i) (60+4)^2 = 60^2 + 2(60)(4) + 4^2; (ii) (100+5)^2 = 100^2 + 2(100)(5) + 5^2; (iii) (200+5)^2 = 200^2 + 2(200)(5) + 5^2.",
                "calculation": "(i) 60^2 + 2(60)(4) + 4^2 = 3600 + 480 + 16 = 4096.\n(ii) 100^2 + 2(100)(5) + 5^2 = 10000 + 1000 + 25 = 11025.\n(iii) 200^2 + 2(200)(5) + 5^2 = 40000 + 2000 + 25 = 42025.",
                "finalAnswer": "(i) 64^2 = 4096; (ii) 105^2 = 11025; (iii) 205^2 = 42025",
                "unit": "integers",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Writing (a + b)^2 = a^2 + b^2, completely dropping the cross-term 2ab. In geometric terms, this discards two entire rectangular corridors!",
            "Squaring fractional coefficients incorrectly, e.g., (3/4 s)^2 written as 3/16 s^2 instead of squaring both numerator and denominator to get 9/16 s^2."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Start with a square sheet of paper partitioned into 4 zones. Emphasize that the cross-term 2ab comes from the two congruent rectangular strips. Call write_chalkboard(action='draw_svg_diagram', content='Geometric Proof: (a + b)^2').",
        "visual_lesson_plan": {
            "title": "Geometric Model of (a + b)^2",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Dissected square showing regions a^2, ab, ab, and b^2.",
            "concept_visuals": [
                {
                    "concept_title": "Square of a Binomial Dissection",
                    "diagram_title": "Geometric Proof: (a + b)^2",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m1_svg,
                    "interactive_math_formula": "(a + b)^2 = a^2 + 2ab + b^2",
                    "mafs_graph_config": {"domain": [-1, 10], "range": [-1, 10], "polygons": [{"points": [[0,0], [7,0], [7,7], [0,7]], "color": "#2563EB"}]},
                    "image_query": "Algebraic identity visual proof square dissection area model",
                    "video_query": "Visual proof of binomial expansion square dissection animated",
                    "image_url": "/images/curriculum/ch4_binomial_square.png",
                    "what_to_make": "Square of side a+b dissected into four rectangles/squares.",
                    "what_to_explain": "Walk the student through the four areas and sum them up.",
                    "timing_and_cue": "Display immediately during Stage 1 intuition."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Square of a Binomial Dissection",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the missing middle term in (5x + 3y)^2 = 25x^2 + [____] + 9y^2?",
                            "ideal_answer": "30xy, because the middle term is 2ab = 2*(5x)*(3y) = 30xy.",
                            "socratic_hint": "Recall the formula 2ab: multiply twice the first term by the second term."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why is (a + b)^2 strictly greater than a^2 + b^2 for positive real numbers a and b?",
                            "ideal_answer": "Because (a + b)^2 = a^2 + 2ab + b^2. When a > 0 and b > 0, the cross-term 2ab > 0, so the sum exceeds a^2 + b^2 by exactly 2ab.",
                            "socratic_hint": "Look at the algebraic expansion: what extra term exists beyond a^2 and b^2?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Compute 103^2 mentally using the (a + b)^2 identity.",
                            "ideal_answer": "103^2 = (100 + 3)^2 = 100^2 + 2(100)(3) + 3^2 = 10000 + 600 + 9 = 10609.",
                            "socratic_hint": "Decompose 103 as 100 + 3 and apply a^2 + 2ab + b^2."
                        },
                        {
                            "q_num": "Q4",
                            "type": "1-mark True/False",
                            "question": "True or False: An algebraic identity holds true for only two specific values of the variable.",
                            "ideal_answer": "False. An identity is an equality that holds true for ALL real values of the variables.",
                            "socratic_hint": "What is the fundamental difference between an identity and an equation?"
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "If x + 1/x = 5, find the exact value of x^2 + 1/x^2.",
                            "ideal_answer": "Squaring both sides: (x + 1/x)^2 = 5^2 => x^2 + 2(x)(1/x) + 1/x^2 = 25 => x^2 + 2 + 1/x^2 = 25 => x^2 + 1/x^2 = 23.",
                            "socratic_hint": "Square both sides of the given equation and notice that x * (1/x) cancels out to 1."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 2: (a - b)^2 and Trinomial (a + b + c)^2
    # -------------------------------------------------------------
    m2_svg = build_algebraic_dissection_svg(
        type_ident='trinomial', a_val=90, b_val=60, c_val=40,
        title="Trinomial Square: (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca",
        caption="Partitioning of side (a+b+c) into 9 sub-rectangles: 3 squares and 6 pairwise rectangles"
    )

    m2 = {
        "order_index": 2,
        "title": "Difference of Binomials (a - b)^2 & Trinomial Expansions (a + b + c)^2",
        "description": "Master the difference of squares, the square of a difference (a - b)^2, and the expansion of the square of a trinomial (a + b + c)^2. Learn how sign patterns propagate across pairwise cross-terms 2ab, 2bc, 2ca.",
        "subtopics": [
            "Geometric interpretation of (a - b)^2 = a^2 - 2ab + b^2",
            "Difference of two squares identity: a^2 - b^2 = (a - b)(a + b)",
            "Derivation of the trinomial square identity via substitution d = b + c",
            "The 9-region geometric dissection for (a + b + c)^2",
            "Handling negative terms in trinomials: (a - b - c)^2",
            "Reverse factorization: identifying trinomial squares from 6-term expressions"
        ],
        "key_concepts": [
            "Square of a Difference: (a - b)^2 = a^2 - 2ab + b^2. The cross term is subtracted because it represents subtracting two overlapping strips from a^2, which removes b^2 twice, necessitating adding +b^2 back.",
            "Difference of Two Squares: a^2 - b^2 = (a - b)(a + b). Converts a difference of powers into a product of linear binomials.",
            "Trinomial Square Formula: (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca. Consists of 3 squared terms (always positive) and 3 pairwise cross-terms.",
            "Sign Propagation Rule: When expanding (x - y + z)^2, rewrite as [x + (-y) + z]^2. The sign of each cross-term is the algebraic product of the signs of its constituent terms.",
            "Square Root Inspection for Factorization: In 4x^2 + 9y^2 + 16z^2 + 12xy - 24yz - 16xz, inspection of negative terms identifies which variable carries the negative sign."
        ],
        "success_criteria": "Expand any trinomial with arbitrary signs, factor 6-term expressions into perfect trinomial squares, and apply a^2 - b^2 to fast arithmetic.",
        "chapter_notes": "Pay intense attention to negative signs in trinomials. Students frequently forget to square negative terms into positive values or botch the cross-term signs.",
        "worked_examples": [
            {
                "problem": "Textbook Examples 4 & 5: (Ex 4) Expand (5x - 3y)^2. (Ex 5) Evaluate (98)^2 without direct multiplication.",
                "given": "Expression (5x - 3y)^2 and number 98 = 100 - 2.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "(Ex 4) (5x)^2 - 2*(5x)*(3y) + (3y)^2.\n(Ex 5) (100 - 2)^2 = 100^2 - 2*(100)*(2) + 2^2.",
                "calculation": "Ex 4:\nStep 1: a = 5x, b = 3y.\nStep 2: a^2 = (5x)^2 = 25x^2.\nStep 3: 2ab = 2 * (5x) * (3y) = 30xy.\nStep 4: b^2 = (3y)^2 = 9y^2.\nCombine: 25x^2 - 30xy + 9y^2.\n\nEx 5:\nStep 1: 100^2 = 10,000.\nStep 2: 2 * 100 * 2 = 400.\nStep 3: 2^2 = 4.\nStep 4: 10,000 - 400 + 4 = 9,604.",
                "finalAnswer": "Ex 4: 25x^2 - 30xy + 9y^2; Ex 5: 98^2 = 9,604",
                "unit": "algebraic expression and integer",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 8: Expand (2x + 3y + 4z)^2.",
                "given": "Trinomial: a = 2x, b = 3y, c = 4z.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca.",
                "substitution": "(2x)^2 + (3y)^2 + (4z)^2 + 2(2x)(3y) + 2(3y)(4z) + 2(4z)(2x).",
                "calculation": "Step 1: Compute square of each term:\n(2x)^2 = 4x^2\n(3y)^2 = 9y^2\n(4z)^2 = 16z^2\nStep 2: Compute pairwise cross-terms:\n2ab = 2 * 2x * 3y = 12xy\n2bc = 2 * 3y * 4z = 24yz\n2ca = 2 * 4z * 2x = 16xz\nStep 3: Sum all 6 terms:\n4x^2 + 9y^2 + 16z^2 + 12xy + 24yz + 16xz.",
                "finalAnswer": "(2x + 3y + 4z)^2 = 4x^2 + 9y^2 + 16z^2 + 12xy + 24yz + 16xz",
                "unit": "algebraic expression",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m2_svg
            },
            {
                "problem": "Textbook Example 9: Expand (4a - 2b - 3c)^2.",
                "given": "Trinomial with negative terms: [4a + (-2b) + (-3c)]^2.",
                "formula": "(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx.",
                "substitution": "(4a)^2 + (-2b)^2 + (-3c)^2 + 2(4a)(-2b) + 2(-2b)(-3c) + 2(-3c)(4a).",
                "calculation": "Step 1: Squares of each term (always positive):\n(4a)^2 = 16a^2\n(-2b)^2 = 4b^2\n(-3c)^2 = 9c^2\nStep 2: Cross terms with signs:\n2 * (4a) * (-2b) = -16ab\n2 * (-2b) * (-3c) = +12bc (negative * negative = positive)\n2 * (-3c) * (4a) = -24ca\nStep 3: Combine all terms:\n16a^2 + 4b^2 + 9c^2 - 16ab + 12bc - 24ca.",
                "finalAnswer": "16a^2 + 4b^2 + 9c^2 - 16ab + 12bc - 24ca",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 10: Factorise 4x^2 + 9y^2 + 16z^2 + 12xy - 24yz - 16xz.",
                "given": "6-term quadratic expression: 4x^2 + 9y^2 + 16z^2 + 12xy - 24yz - 16xz.",
                "formula": "a^2 + b^2 + c^2 + 2ab + 2bc + 2ca = (a + b + c)^2.",
                "substitution": "(2x)^2 + (3y)^2 + (-4z)^2 + 2(2x)(3y) + 2(3y)(-4z) + 2(-4z)(2x).",
                "calculation": "Step 1: Identify base squared terms: 4x^2 = (2x)^2, 9y^2 = (3y)^2, 16z^2 = (4z)^2.\nStep 2: Analyze negative cross-terms: The terms -24yz and -16xz are negative, while +12xy is positive.\nStep 3: The common variable in both negative terms is z. Therefore, the z term carries the negative sign: c = -4z (or x and y are negative, which gives equivalent (-2x - 3y + 4z)^2).\nStep 4: Verify cross terms:\n2 * (2x) * (3y) = +12xy (Matches!)\n2 * (3y) * (-4z) = -24yz (Matches!)\n2 * (-4z) * (2x) = -16xz (Matches!)\nStep 5: Write the factorized form: (2x + 3y - 4z)^2.",
                "finalAnswer": "(2x + 3y - 4z)^2 or (2x + 3y - 4z)(2x + 3y - 4z)",
                "unit": "factorized expression",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Writing (-2b)^2 as -4b^2. The square of any real number (positive or negative) is ALWAYS non-negative: (-2b)^2 = +4b^2.",
            "Failing to deduce which variable is negative in reverse factorization by not finding the common variable between the two negative cross terms."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Teach reverse factorization like a detective solving a crime: look at the negative cross terms, identify the common letter, and that letter holds the negative sign. Call write_chalkboard(action='draw_svg_diagram', content='Trinomial Square: (a + b + c)^2').",
        "visual_lesson_plan": {
            "title": "Trinomial Dissection & Sign Analysis",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Dissected square representing (a + b + c)^2.",
            "concept_visuals": [
                {
                    "concept_title": "Trinomial Square Area Model",
                    "diagram_title": "Geometric Proof: (a + b + c)^2",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m2_svg,
                    "interactive_math_formula": "(a+b+c)^2 = a^2+b^2+c^2+2ab+2bc+2ca",
                    "mafs_graph_config": {"domain": [-1, 10], "range": [-1, 10], "polygons": [{"points": [[0,0], [9,0], [9,9], [0,9]], "color": "#7C3AED"}]},
                    "image_query": "Trinomial square 9 area dissection geometric diagram",
                    "video_query": "Visual proof of a plus b plus c whole square animated",
                    "image_url": "/images/curriculum/ch4_trinomial_square.png",
                    "what_to_make": "3x3 partition of square into 9 regions.",
                    "what_to_explain": "Explain why there are 3 squares along the diagonal and 3 pairs of matching rectangles off-diagonal.",
                    "timing_and_cue": "Show at 03:30 during trinomial explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Trinomial Expansions & Signs",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "How many total terms are there in the expanded form of (a + b + c)^2 before combining like terms?",
                            "ideal_answer": "6 terms (3 squared terms: a^2, b^2, c^2, and 3 cross-terms: 2ab, 2bc, 2ca).",
                            "socratic_hint": "Count the 3 pure squares plus the 3 pairwise cross terms."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "In the expansion of (x - y - z)^2, which cross-term will have a positive sign?",
                            "ideal_answer": "+2yz, because (-y) * (-z) produces a positive product, making 2(-y)(-z) = +2yz.",
                            "socratic_hint": "What is the product of two negative numbers?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Evaluate 198^2 using the identity (a - b)^2.",
                            "ideal_answer": "198^2 = (200 - 2)^2 = 200^2 - 2(200)(2) + 2^2 = 40000 - 800 + 4 = 39204.",
                            "socratic_hint": "Decompose 198 as 200 - 2 and calculate a^2 - 2ab + b^2."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Conceptual",
                            "question": "In factoring 9x^2 + 16y^2 + 25z^2 - 24xy - 40yz + 30xz, which term carries the negative sign?",
                            "ideal_answer": "The y term (4y). The two negative terms are -24xy and -40yz, both of which share the common variable y.",
                            "socratic_hint": "Find the variable that appears in BOTH negative cross terms."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "If a + b + c = 9 and ab + bc + ca = 26, find the value of a^2 + b^2 + c^2.",
                            "ideal_answer": "(a+b+c)^2 = a^2+b^2+c^2 + 2(ab+bc+ca) => 9^2 = a^2+b^2+c^2 + 2(26) => 81 = a^2+b^2+c^2 + 52 => a^2+b^2+c^2 = 81 - 52 = 29.",
                            "socratic_hint": "Substitute the given values into the trinomial square identity and solve for a^2+b^2+c^2."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 3: Quadratic Trinomials & Splitting Middle Term
    # -------------------------------------------------------------
    m3_svg = build_algebraic_dissection_svg(
        type_ident='algebra_tiles', a_val=120, b_val=40,
        title="Algebra Tiles: Factorisation of x^2 + 7x + 12 = (x + 3)(x + 4)",
        caption="1 large x^2 tile (blue), 7 unit-x strips (green), and 12 unit squares (amber)"
    )

    m3 = {
        "order_index": 3,
        "title": "Quadratic Trinomial Factorisation: Algebra Tiles, (x + a)(x + b) & Splitting the Middle Term",
        "description": "Understand the geometry of factoring non-perfect square trinomials using algebra tiles. Formulate the identity (x + a)(x + b) = x^2 + (a + b)x + ab and master the rigorous algorithm of splitting the middle term for Ax^2 + Bx + C.",
        "subtopics": [
            "Geometric tile modeling of quadratic expressions x^2 + bx + c",
            "Derivation of the identity (x + a)(x + b) = x^2 + (a + b)x + ab",
            "Finding two numbers p and q such that p + q = B and p * q = A * C",
            "Factorization of monic quadratics: x^2 + 7x + 12 and x^2 - 5x + 6",
            "Factorization of non-monic quadratics: 6x^2 + 17x + 5 and 2x^2 - 7x - 15",
            "Common monomial factor extraction before applying splitting methods"
        ],
        "key_concepts": [
            "Binomial Product Identity: (x + a)(x + b) = x^2 + (a + b)x + ab. Notice the coefficient of x is the SUM (a + b), and the constant term is the PRODUCT (ab).",
            "Algebra Tile Conservation: Arranging 1 x-square tile, (a + b) x-strips, and ab unit squares into a seamless large rectangle of dimensions (x + a) by (x + b).",
            "The AC Method Algorithm: To factor Ax^2 + Bx + C, find two integers p and q such that p * q = A * C and p + q = B. Then split Bx as px + qx and factor by grouping.",
            "Sign Rule for AC Method: If AC > 0, p and q have the SAME sign (both positive if B > 0, both negative if B < 0). If AC < 0, p and q have OPPOSITE signs, with the larger magnitude matching the sign of B.",
            "Greatest Common Divisor (GCD) Invariant: Always extract any common numerical factor before attempting the AC method."
        ],
        "success_criteria": "Factor any quadratic trinomial Ax^2 + Bx + C using the AC splitting method, visualize the factorization as an algebra tile rectangle, and explain sign choices.",
        "chapter_notes": "Splitting the middle term is the single most tested skill in Class 9 algebra. Ensure students write down the exact search for p and q with their sum and product explicitly verified.",
        "worked_examples": [
            {
                "problem": "Textbook Examples 11 & 12: Factorise (Ex 11) x^2 + 7x + 12 and (Ex 12) x^2 - 5x + 6.",
                "given": "(Ex 11) x^2 + 7x + 12 (A=1, B=7, C=12); (Ex 12) x^2 - 5x + 6 (A=1, B=-5, C=6).",
                "formula": "x^2 + (p + q)x + pq = (x + p)(x + q).",
                "substitution": "(Ex 11) p=3, q=4 => p+q=7, pq=12.\n(Ex 12) p=-2, q=-3 => p+q=-5, pq=6.",
                "calculation": "Ex 11:\nStep 1: Product pq = 12, Sum p + q = 7.\nStep 2: Factor pairs of 12: (1, 12) sum 13; (2, 6) sum 8; (3, 4) sum 7 (Matches!).\nStep 3: Split middle term: x^2 + 3x + 4x + 12.\nStep 4: Factor by grouping: x(x + 3) + 4(x + 3) = (x + 3)(x + 4).\n\nEx 12:\nStep 1: Product pq = 6, Sum p + q = -5.\nStep 2: Since product > 0 and sum < 0, both numbers must be negative.\nStep 3: Pairs: (-1, -6) sum -7; (-2, -3) sum -5 (Matches!).\nStep 4: Split middle term: x^2 - 2x - 3x + 6.\nStep 5: Factor by grouping: x(x - 2) - 3(x - 2) = (x - 2)(x - 3).",
                "finalAnswer": "Ex 11: (x + 3)(x + 4); Ex 12: (x - 2)(x - 3)",
                "unit": "factored polynomials",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m3_svg
            },
            {
                "problem": "Textbook Example 13: Factorise 6x^2 + 17x + 5 by splitting the middle term.",
                "given": "Quadratic trinomial: A = 6, B = 17, C = 5.",
                "formula": "AC Method: Find p, q such that p * q = A * C and p + q = B.",
                "substitution": "A * C = 6 * 5 = 30. B = 17. Looking for p, q such that pq = 30 and p + q = 17.",
                "calculation": "Step 1: Calculate target product: A * C = 6 * 5 = 30.\nStep 2: List pairs of factors of 30:\n  - 1 and 30: sum = 31\n  - 2 and 15: sum = 2 + 15 = 17 (Matches target B = 17!)\nStep 3: Split the middle term 17x as 2x + 15x:\n  6x^2 + 17x + 5 = 6x^2 + 2x + 15x + 5.\nStep 4: Group in pairs:\n  (6x^2 + 2x) + (15x + 5).\nStep 5: Factor common monomial from each pair:\n  2x(3x + 1) + 5(3x + 1).\nStep 6: Factor out the common binomial (3x + 1):\n  (2x + 5)(3x + 1).",
                "finalAnswer": "6x^2 + 17x + 5 = (2x + 5)(3x + 1)",
                "unit": "factored quadratic",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 14: Factorise 2x^2 - 7x - 15.",
                "given": "Quadratic trinomial: A = 2, B = -7, C = -15.",
                "formula": "AC Method: p * q = A * C = 2 * (-15) = -30, and p + q = -7.",
                "substitution": "Pairs of -30: p = -10, q = 3, because (-10)*(3) = -30 and (-10) + 3 = -7.",
                "calculation": "Step 1: Target product = 2 * (-15) = -30. Target sum = -7.\nStep 2: Find factor pairs of -30 with sum -7:\n  - (1, -30) sum -29\n  - (2, -15) sum -13\n  - (3, -10) sum 3 + (-10) = -7 (Matches!)\nStep 3: Split the middle term -7x as -10x + 3x:\n  2x^2 - 7x - 15 = 2x^2 - 10x + 3x - 15.\nStep 4: Factor by grouping:\n  2x(x - 5) + 3(x - 5).\nStep 5: Extract common factor (x - 5):\n  (x - 5)(2x + 3).",
                "finalAnswer": "2x^2 - 7x - 15 = (x - 5)(2x + 3)",
                "unit": "factored quadratic",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.4 Q1: Fill in the blanks: (i) s^2 - 11s + 24 = (________)(________); (ii) (________)(x + 1) = 3x^2 - 4x - 7; (iii) 10x^2 - 11x - 6 = (2x - ___)(___ + 2).",
                "given": "Three factoring relations with blanks.",
                "formula": "Splitting the middle term and algebraic division.",
                "substitution": "(i) pq = 24, p+q = -11 => -3, -8; (ii) Divide (3x^2 - 4x - 7) by (x + 1); (iii) (2x - 3)(5x + 2).",
                "calculation": "Part (i):\nTarget product = 24, sum = -11. Factors are -3 and -8 since (-3)*(-8) = 24 and -3 + (-8) = -11.\nThus s^2 - 11s + 24 = (s - 3)(s - 8).\n\nPart (ii):\nTo factor 3x^2 - 4x - 7, A*C = 3*(-7) = -21, B = -4. Numbers are -7 and 3.\n3x^2 + 3x - 7x - 7 = 3x(x + 1) - 7(x + 1) = (3x - 7)(x + 1).\nBlank is (3x - 7).\n\nPart (iii):\n10x^2 - 11x - 6: A*C = -60, B = -11. Numbers are -15 and 4.\n10x^2 - 15x + 4x - 6 = 5x(2x - 3) + 2(2x - 3) = (2x - 3)(5x + 2).\nBlanks are 3 and 5x.",
                "finalAnswer": "(i) (s - 3)(s - 8); (ii) (3x - 7); (iii) (2x - 3)(5x + 2)",
                "unit": "algebraic factors",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Picking factor pairs that add up to +B when the sign required is -B (e.g., using 10 and -3 instead of -10 and 3).",
            "Forgetting to multiply A by C when A != 1. Looking only for factors of C is a fatal error in non-monic quadratics."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Emphasize that when A != 1, we ALWAYS multiply A * C first. Have the student write down both the target product and target sum before guessing factors. Call write_chalkboard(action='draw_svg_diagram', content='Algebra Tiles: Factorisation').",
        "visual_lesson_plan": {
            "title": "Algebra Tiles & Factoring Rectangles",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Algebra tiles forming a rectangle representing x^2 + 7x + 12 = (x + 3)(x + 4).",
            "concept_visuals": [
                {
                    "concept_title": "Geometric Algebra Tiles",
                    "diagram_title": "Factoring x^2 + 7x + 12",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m3_svg,
                    "interactive_math_formula": "x^2 + 7x + 12 = (x + 3)(x + 4)",
                    "mafs_graph_config": {"domain": [-1, 8], "range": [-1, 8], "polygons": [{"points": [[0,0], [7,0], [7,5], [0,5]], "color": "#10B981"}]},
                    "image_query": "Algebra tiles quadratic factorization rectangle visual proof",
                    "video_query": "Factoring quadratic polynomials with algebra tiles animated",
                    "image_url": "/images/curriculum/ch4_algebra_tiles.png",
                    "what_to_make": "Rectangle constructed from x^2, x-strips, and unit squares.",
                    "what_to_explain": "Explain how the length is (x + 4) and the width is (x + 3).",
                    "timing_and_cue": "Present at 03:00 when introducing (x + a)(x + b)."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Quadratic Factorisation",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "To factor 3x^2 - 2x - 8 using the AC method, what is the target product p * q?",
                            "ideal_answer": "-24, because A * C = 3 * (-8) = -24.",
                            "socratic_hint": "Multiply the leading coefficient A by the constant term C."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "If AC is negative, what can you deduce about the signs of the two splitting numbers p and q?",
                            "ideal_answer": "They must have opposite signs (one positive, one negative), and the one with the larger absolute value matches the sign of B.",
                            "socratic_hint": "When does the product of two real numbers become negative?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Factor x^2 - 13x + 36 completely.",
                            "ideal_answer": "Product = 36, sum = -13. The numbers are -9 and -4. Factorization: (x - 9)(x - 4).",
                            "socratic_hint": "Find two negative numbers whose product is 36 and sum is -13."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Find the product 23 * 17 without direct multiplication using identities.",
                            "ideal_answer": "23 * 17 = (20 + 3)(20 - 3) = 20^2 - 3^2 = 400 - 9 = 391.",
                            "socratic_hint": "Rewrite 23 and 17 as symmetric offsets around 20."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Factorise completely: 12x^2 - 7x + 1.",
                            "ideal_answer": "A*C = 12*1 = 12. B = -7. Factors are -3 and -4. 12x^2 - 3x - 4x + 1 = 3x(4x - 1) - 1(4x - 1) = (4x - 1)(3x - 1).",
                            "socratic_hint": "Find two negative factors of 12 that add to -7 and group terms."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 4: Cubic Expansions & Conditional Identity
    # -------------------------------------------------------------
    m4_svg = build_algebraic_dissection_svg(
        type_ident='a_plus_b_sq', a_val=140, b_val=70,
        title="Cubic Expansion: (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
        caption="3D Cube decomposition into 8 sub-solids: a^3, three a^2*b slabs, three a*b^2 prisms, and b^3"
    )

    m4 = {
        "order_index": 4,
        "title": "Cubic Polynomial Identities: (a ± b)^3, Sum & Difference of Cubes, and the Conditional Theorem",
        "description": "Expand cubic binomials (a ± b)^3, discover the sum and difference of cubes a^3 ± b^3, master the 3-variable cubic identity a^3 + b^3 + c^3 - 3abc, and apply the conditional theorem when a + b + c = 0.",
        "subtopics": [
            "Geometric 3D decomposition of a cube of edge (a + b) into 8 sub-solids",
            "Derivations of (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 = a^3 + b^3 + 3ab(a + b)",
            "Derivation of (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 = a^3 - b^3 - 3ab(a - b)",
            "Factor forms: a^3 + b^3 = (a + b)(a^2 - ab + b^2) and a^3 - b^3 = (a - b)(a^2 + ab + b^2)",
            "The Ramanujan-Euler identity: a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)",
            "The Conditional Identity: If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc"
        ],
        "key_concepts": [
            "Cubic Binomial Expansion: (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3. In 3D space, this partitions a cube of edge (a + b) into 1 a-cube, 3 square slabs of dimension a*a*b, 3 rod prisms of dimension a*b*b, and 1 b-cube.",
            "Condensed Factor Form: (a + b)^3 = a^3 + b^3 + 3ab(a + b), which allows fast evaluation when the sum (a + b) and product ab are known.",
            "Alternating Sign Pattern in (a - b)^3: Signs alternate +, -, +, -: a^3 - 3a^2b + 3ab^2 - b^3.",
            "Sum/Difference of Cubes Invariant: In a^3 + b^3 = (a + b)(a^2 - ab + b^2), the middle term in the second factor has a MINUS sign (-ab). In a^3 - b^3 = (a - b)(a^2 + ab + b^2), the middle term has a PLUS sign (+ab).",
            "Conditional Cubic Theorem: If a + b + c = 0, then the factor (a + b + c) vanishes, reducing a^3 + b^3 + c^3 - 3abc to 0, which immediately implies a^3 + b^3 + c^3 = 3abc."
        ],
        "success_criteria": "Expand any cubic binomial, factor expressions using sum/difference of cubes, and evaluate cubic sums without cubing when the terms add to zero.",
        "chapter_notes": "The conditional identity is an authentic CBSE Class 9 favorite. Emphasize that checking whether a + b + c = 0 should always be the student's very first reflex when asked to compute large cubes.",
        "worked_examples": [
            {
                "problem": "Textbook Examples 15 & 16: (Ex 15) Expand (3x + 4y)^3. (Ex 16) Expand (5p - 3q)^3.",
                "given": "Cubic binomials: (3x + 4y)^3 and (5p - 3q)^3.",
                "formula": "(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3; (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3.",
                "substitution": "Ex 15: a=3x, b=4y => (3x)^3 + 3(3x)^2(4y) + 3(3x)(4y)^2 + (4y)^3.\nEx 16: a=5p, b=3q => (5p)^3 - 3(5p)^2(3q) + 3(5p)(3q)^2 - (3q)^3.",
                "calculation": "Ex 15:\nStep 1: (3x)^3 = 27x^3.\nStep 2: 3 * (9x^2) * (4y) = 108x^2y.\nStep 3: 3 * (3x) * (16y^2) = 144xy^2.\nStep 4: (4y)^3 = 64y^3.\nSum: 27x^3 + 108x^2y + 144xy^2 + 64y^3.\n\nEx 16:\nStep 1: (5p)^3 = 125p^3.\nStep 2: -3 * (25p^2) * (3q) = -225p^2q.\nStep 3: +3 * (5p) * (9q^2) = +135pq^2.\nStep 4: -(3q)^3 = -27q^3.\nSum: 125p^3 - 225p^2q + 135pq^2 - 27q^3.",
                "finalAnswer": "Ex 15: 27x^3 + 108x^2y + 144xy^2 + 64y^3; Ex 16: 125p^3 - 225p^2q + 135pq^2 - 27q^3",
                "unit": "cubic polynomials",
                "has_diagram": False
            },
            {
                "problem": "Conditional Identity Application: Without actually calculating the cubes, find the value of (-12)^3 + (7)^3 + (5)^3.",
                "given": "a = -12, b = 7, c = 5.",
                "formula": "If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc.",
                "substitution": "Check sum: a + b + c = (-12) + 7 + 5 = 0. Therefore sum of cubes = 3 * (-12) * (7) * (5).",
                "calculation": "Step 1: Verify condition: a + b + c = -12 + 7 + 5 = -12 + 12 = 0.\nStep 2: Since the condition holds, apply the theorem: a^3 + b^3 + c^3 = 3abc.\nStep 3: Substitute: 3 * (-12) * 7 * 5.\nStep 4: Simplify multiplication: 3 * (-12) = -36. 7 * 5 = 35.\nStep 5: Multiply: -36 * 35 = -1260.",
                "finalAnswer": "(-12)^3 + 7^3 + 5^3 = -1,260",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 17: Saira arranges a square of side x units, 8 rectangular strips of sides x units and width 1 unit, and 15 squares of side 1 unit to form a bigger rectangle. Find the length and width.",
                "given": "Components: 1 x^2 tile, 8 x-strips, 15 unit squares. Total Area = x^2 + 8x + 15.",
                "formula": "Area = Length * Width => Factor x^2 + 8x + 15.",
                "substitution": "Product = 15, Sum = 8. Numbers are 3 and 5.",
                "calculation": "Step 1: Total area = x^2 + 8x + 15.\nStep 2: Find two integers that multiply to 15 and add to 8: 3 and 5.\nStep 3: Factor the trinomial: x^2 + 3x + 5x + 15 = x(x + 3) + 5(x + 3) = (x + 3)(x + 5).\nStep 4: The dimensions of the constructed large rectangle are (x + 5) units by (x + 3) units.",
                "finalAnswer": "Length = (x + 5) units, Width = (x + 3) units",
                "unit": "linear units",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 18: A rectangular swimming pool has an area given by A(t) = t^2 + 2ts - 48s^2. If the length is (t + 8s), find the width, and evaluate the area when t = 20 m and s = 2 m.",
                "given": "Area = t^2 + 2ts - 48s^2, Length = t + 8s, t = 20 m, s = 2 m.",
                "formula": "Width = Area / Length. Factor t^2 + 2ts - 48s^2.",
                "substitution": "Product = -48, Sum = 2. Numbers are 8 and -6. Dimensions: (t + 8s)(t - 6s).",
                "calculation": "Step 1: Factor numerator: t^2 + 2ts - 48s^2 = (t + 8s)(t - 6s).\nStep 2: Divide by length: Width = (t + 8s)(t - 6s) / (t + 8s) = t - 6s.\nStep 3: Substitute numerical values t = 20, s = 2:\n  Length = 20 + 8(2) = 20 + 16 = 36 m.\n  Width = 20 - 6(2) = 20 - 12 = 8 m.\nStep 4: Compute Area = 36 * 8 = 288 m^2.",
                "finalAnswer": "Width = (t - 6s) metres; Area = 288 m^2",
                "unit": "metres and square metres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Writing (a + b)^3 = a^3 + b^3, ignoring the middle terms 3a^2b + 3ab^2 entirely.",
            "Applying the conditional identity 3abc without checking if a + b + c = 0 first. If the sum is non-zero, this identity is completely invalid!"
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Use a physical 3D cube model. Show how expanding from 2D squares to 3D cubes increases the number of cross terms. Emphasize checking a + b + c = 0. Call write_chalkboard(action='draw_svg_diagram', content='Cubic Expansion: (a + b)^3').",
        "visual_lesson_plan": {
            "title": "Cubic Dissection & Factor Forms",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Dissected cube showing volume breakdown into 8 sub-solids.",
            "concept_visuals": [
                {
                    "concept_title": "Cubic Dissection & Volumes",
                    "diagram_title": "Volume of (a + b)^3",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m4_svg,
                    "interactive_math_formula": "(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
                    "mafs_graph_config": {"domain": [-1, 10], "range": [-1, 10], "polygons": [{"points": [[0,0], [6,0], [8,3], [2,3]], "color": "#F59E0B"}]},
                    "image_query": "Cubic expansion geometric proof 3d cube dissection volume",
                    "video_query": "Visualizing cubic identities with 3D blocks animated",
                    "image_url": "/images/curriculum/ch4_cubic_dissection.png",
                    "what_to_make": "Isometric cube showing 8 constituent solids.",
                    "what_to_explain": "Explain that 3a^2b represents 3 slabs and 3ab^2 represents 3 rods.",
                    "timing_and_cue": "Show during 3D intuition explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Cubic Identities & Factorisation",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the coefficient of x^2 in the expansion of (2x + 1)^3?",
                            "ideal_answer": "12, because the term is 3*(2x)^2*(1) = 3 * 4x^2 * 1 = 12x^2.",
                            "socratic_hint": "Look at the 3a^2b term in the expansion."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Under what exact condition is a^3 + b^3 + c^3 = 3abc?",
                            "ideal_answer": "When a + b + c = 0 (or when a = b = c).",
                            "socratic_hint": "Look at the factor (a + b + c) in the 3-variable cubic identity."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Calculate 102^3 using the identity (a + b)^3.",
                            "ideal_answer": "102^3 = (100 + 2)^3 = 100^3 + 3(100)^2(2) + 3(100)(2)^2 + 2^3 = 1000000 + 60000 + 1200 + 8 = 1061208.",
                            "socratic_hint": "Decompose 102 as 100 + 2 and calculate each term."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Factor completely: 8x^3 + 27y^3.",
                            "ideal_answer": "(2x)^3 + (3y)^3 = (2x + 3y)[(2x)^2 - (2x)(3y) + (3y)^2] = (2x + 3y)(4x^2 - 6xy + 9y^2).",
                            "socratic_hint": "Use the sum of cubes identity a^3 + b^3 = (a + b)(a^2 - ab + b^2)."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Without calculating cubes, find the value of (28)^3 + (-15)^3 + (-13)^3.",
                            "ideal_answer": "Check sum: 28 + (-15) + (-13) = 28 - 28 = 0. Since sum is 0, sum of cubes = 3 * 28 * (-15) * (-13) = 84 * 195 = 16,380.",
                            "socratic_hint": "Add the three base numbers together: what do they sum to?"
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 5: Textbook Exercise Solver 1: Ex 4.1, 4.2 & 4.3
    # -------------------------------------------------------------
    m5_svg = build_algebraic_dissection_svg(
        type_ident='a_plus_b_sq', a_val=130, b_val=60,
        title="Exercise Solver 1: Complete Expansions & Factorisations",
        caption="Full step-by-step solutions for Exercises 4.1, 4.2, and 4.3 with zero skipped steps"
    )

    m5 = {
        "order_index": 5,
        "title": "Textbook Exercise Solver 1: Exercises 4.1, 4.2 & 4.3 (Complete Solutions)",
        "description": "Exhaustive step-by-step solutions for every question in Exercise 4.1 (binomial squares), Exercise 4.2 (factorisation and differences), and Exercise 4.3 (trinomial expansions and fractional factorisations) with zero skipped calculations.",
        "subtopics": [
            "Exercise 4.1 Q1 (i to vi): Fractional and decimal binomial expansions",
            "Exercise 4.1 Q2 (i to iii): Numerical evaluations using (a + b)^2",
            "Exercise 4.2 Q1 (i to vi): Complete factorisations of perfect square trinomials",
            "Exercise 4.2 Q2 (i to iii): Numerical evaluations using (a - b)^2",
            "Exercise 4.3 Q1 (i to vi): Multi-digit square evaluations using identities",
            "Exercise 4.3 Q2 (i to v): Complex trinomial and fractional factorisations"
        ],
        "key_concepts": [
            "Algorithmic Substitution Invariant: Never write an answer directly. Always write Given -> Identify a and b -> State Formula -> Substitute with parentheses -> Simplify step-by-step -> State Final Answer.",
            "Common Factor Extraction: In expressions like 3a^2 + 4ab + 4/3 b^2, factor out 1/3 first: 1/3 (9a^2 + 12ab + 4b^2) = 1/3 (3a + 2b)^2.",
            "Fractional Invariant: In (x/3 + y/2)^2, compute (x/3)^2 = x^2/9, 2*(x/3)*(y/2) = xy/3, and (y/2)^2 = y^2/4."
        ],
        "success_criteria": "Solve every question in Exercises 4.1, 4.2, and 4.3 with 100% precision and complete working.",
        "chapter_notes": "Every single sub-part of every exercise is fully addressed here. No homework left as exercise for the student.",
        "worked_examples": [
            {
                "problem": "Exercise 4.1 Q1 (iv, v, vi): Expand (iv) (3/4 s + 8t)^2, (v) (x/4 + 2y)^2, (vi) (x/3 + y/2)^2.",
                "given": "Three fractional binomial squares.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2.",
                "substitution": "(iv) (3/4 s)^2 + 2(3/4 s)(8t) + (8t)^2; (v) (x/4)^2 + 2(x/4)(2y) + (2y)^2; (vi) (x/3)^2 + 2(x/3)(y/2) + (y/2)^2.",
                "calculation": "Part (iv):\n(3/4 s)^2 = 9/16 s^2.\n2 * (3/4 s) * (8t) = (3/2 s) * 8t = 12 st.\n(8t)^2 = 64 t^2.\nResult: 9/16 s^2 + 12st + 64t^2.\n\nPart (v):\n(x/4)^2 = x^2/16.\n2 * (x/4) * (2y) = xy.\n(2y)^2 = 4y^2.\nResult: x^2/16 + xy + 4y^2.\n\nPart (vi):\n(x/3)^2 = x^2/9.\n2 * (x/3) * (y/2) = xy/3.\n(y/2)^2 = y^2/4.\nResult: x^2/9 + 1/3 xy + y^2/4.",
                "finalAnswer": "(iv) 9/16 s^2 + 12st + 64t^2; (v) x^2/16 + xy + 4y^2; (vi) x^2/9 + 1/3 xy + y^2/4",
                "unit": "algebraic expansions",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q1: Factor completely: (i) 9x^2 + 24xy + 16y^2; (ii) 4s^2 + 20st + 25t^2; (iii) 49x^2 + 28xy + 4y^2; (iv) 64p^2 + 32/3 pq + 4/9 q^2; (v) 3a^2 + 4ab + 4/3 b^2; (vi) 9/5 s^2 + 6sv + 5v^2.",
                "given": "Six quadratic trinomials to factorize.",
                "formula": "a^2 + 2ab + b^2 = (a + b)^2.",
                "substitution": "Express each as (first)^2 + 2*(first)*(second) + (second)^2.",
                "calculation": "(i) (3x)^2 + 2(3x)(4y) + (4y)^2 = (3x + 4y)^2.\n(ii) (2s)^2 + 2(2s)(5t) + (5t)^2 = (2s + 5t)^2.\n(iii) (7x)^2 + 2(7x)(2y) + (2y)^2 = (7x + 2y)^2.\n(iv) (8p)^2 + 2(8p)(2/3 q) + (2/3 q)^2 = (8p + 2/3 q)^2.\n(v) Factor out 1/3: 1/3 [9a^2 + 12ab + 4b^2] = 1/3 [(3a)^2 + 2(3a)(2b) + (2b)^2] = 1/3 (3a + 2b)^2.\n(vi) Factor out 1/5: 1/5 [9s^2 + 30sv + 25v^2] = 1/5 [(3s)^2 + 2(3s)(5v) + (5v)^2] = 1/5 (3s + 5v)^2.",
                "finalAnswer": "(i) (3x + 4y)^2; (ii) (2s + 5t)^2; (iii) (7x + 2y)^2; (iv) (8p + 2/3 q)^2; (v) 1/3 (3a + 2b)^2; (vi) 1/5 (3s + 5v)^2",
                "unit": "factored expressions",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.2 Q2: Find the values using the identity (a - b)^2: (i) (79)^2, (ii) (193)^2, (iii) (299)^2.",
                "given": "Numbers: 79 = 80 - 1, 193 = 200 - 7, 299 = 300 - 1.",
                "formula": "(a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "(i) (80-1)^2; (ii) (200-7)^2; (iii) (300-1)^2.",
                "calculation": "(i) 80^2 - 2(80)(1) + 1^2 = 6400 - 160 + 1 = 6241.\n(ii) 200^2 - 2(200)(7) + 7^2 = 40000 - 2800 + 49 = 37249.\n(iii) 300^2 - 2(300)(1) + 1^2 = 90000 - 600 + 1 = 89401.",
                "finalAnswer": "(i) 79^2 = 6,241; (ii) 193^2 = 37,249; (iii) 299^2 = 89,401",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q1: Find the following squares using suitable identities: (i) 117^2, (ii) 78^2, (iii) 198^2, (iv) 214^2, (v) 1104^2, (vi) 1120^2.",
                "given": "Six numbers to square using identities.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2 or (a - b)^2 = a^2 - 2ab + b^2.",
                "substitution": "Decompose into friendly tens/hundreds bases.",
                "calculation": "(i) 117^2 = (100 + 17)^2 = 10000 + 3400 + 289 = 13689.\n(ii) 78^2 = (80 - 2)^2 = 6400 - 320 + 4 = 6084.\n(iii) 198^2 = (200 - 2)^2 = 40000 - 800 + 4 = 39204.\n(iv) 214^2 = (200 + 14)^2 = 40000 + 5600 + 196 = 45796.\n(v) 1104^2 = (1100 + 4)^2 = 1210000 + 8800 + 16 = 1218816.\n(vi) 1120^2 = (1100 + 20)^2 = 1210000 + 44000 + 400 = 1254400.",
                "finalAnswer": "(i) 13,689; (ii) 6,084; (iii) 39,204; (iv) 45,796; (v) 1,218,816; (vi) 1,254,400",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q2: Factor using suitable identities: (i) 16y^2 - 24y + 9; (ii) 9/4 s^2 - 6st + 4t^2; (iii) m^2/9 + mk/3 + k^2/4 + 3nk + 2mn + 9n^2; (iv) p^2 - 2 + 1/p^2; (v) 9a^2 + 4b^2 + c^2 - 12ab + 6ac - 4bc.",
                "given": "Five expressions to factor.",
                "formula": "(a - b)^2, (a + b + c)^2, and reciprocal squares.",
                "substitution": "Identify squares and match cross terms.",
                "calculation": "(i) (4y)^2 - 2(4y)(3) + 3^2 = (4y - 3)^2.\n(ii) (3/2 s)^2 - 2(3/2 s)(2t) + (2t)^2 = (3/2 s - 2t)^2.\n(iii) Rearrange as 6 terms: (m/3)^2 + (k/2)^2 + (3n)^2 + 2(m/3)(k/2) + 2(k/2)(3n) + 2(m/3)(3n) = (m/3 + k/2 + 3n)^2.\n(iv) p^2 - 2(p)(1/p) + (1/p)^2 = (p - 1/p)^2.\n(v) 9a^2 + 4b^2 + c^2 - 12ab - 4bc + 6ac: b is negative because -12ab and -4bc share b.\n= (3a)^2 + (-2b)^2 + c^2 + 2(3a)(-2b) + 2(-2b)(c) + 2(3a)(c) = (3a - 2b + c)^2.",
                "finalAnswer": "(i) (4y - 3)^2; (ii) (3/2 s - 2t)^2; (iii) (m/3 + k/2 + 3n)^2; (iv) (p - 1/p)^2; (v) (3a - 2b + c)^2",
                "unit": "factored algebraic expressions",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.3 Q3: Expand the trinomial (2x - y + z)^2 in full detail.",
                "given": "Trinomial: [2x + (-y) + z]^2.",
                "formula": "(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca.",
                "substitution": "(2x)^2 + (-y)^2 + z^2 + 2(2x)(-y) + 2(-y)(z) + 2(z)(2x).",
                "calculation": "Step 1: Compute pure squares: (2x)^2 = 4x^2, (-y)^2 = y^2, z^2 = z^2.\nStep 2: Compute cross terms:\n2 * (2x) * (-y) = -4xy\n2 * (-y) * z = -2yz\n2 * z * 2x = +4xz\nStep 3: Combine all 6 terms:\n4x^2 + y^2 + z^2 - 4xy - 2yz + 4xz.",
                "finalAnswer": "(2x - y + z)^2 = 4x^2 + y^2 + z^2 - 4xy - 2yz + 4xz",
                "unit": "expanded polynomial",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting to check the middle term when factoring p^2 - 2 + 1/p^2: students fail to realize that 2 is actually 2 * p * (1/p).",
            "Dropping fractions or failing to multiply cross-terms carefully in trinomials like (m/3 + k/2 + 3n)^2."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Guide students through complex multi-term factorisations by first matching the 3 square terms, then validating the 3 cross terms one by one. Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 1').",
        "visual_lesson_plan": {
            "title": "Comprehensive Solutions: Ex 4.1 to 4.3",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Summary chart comparing binomial square, difference of squares, and trinomial square.",
            "concept_visuals": [
                {
                    "concept_title": "Identities Reference Chart",
                    "diagram_title": "Identities Comparison",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m5_svg,
                    "interactive_math_formula": "(a+b)^2, (a-b)^2, (a+b+c)^2",
                    "mafs_graph_config": {"domain": [-1, 10], "range": [-1, 10]},
                    "image_query": "Algebraic identities summary comparison chart visual guide",
                    "video_query": "Algebraic identities practice problems step by step",
                    "image_url": "/images/curriculum/ch4_exercise_solver1.png",
                    "what_to_make": "Overview of all 3 core identities.",
                    "what_to_explain": "Review each identity's structure and sign distribution.",
                    "timing_and_cue": "Display at start of exercise solver session."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Exercise Solver Mastery",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the factored form of 4x^2 + 12xy + 9y^2?",
                            "ideal_answer": "(2x + 3y)^2.",
                            "socratic_hint": "Check if it matches (a + b)^2 with a = 2x and b = 3y."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why is (x - 1/x)^2 = x^2 - 2 + 1/x^2?",
                            "ideal_answer": "Because the cross term is -2 * x * (1/x) = -2 * 1 = -2, where x and 1/x cancel out.",
                            "socratic_hint": "Notice that x and 1/x are reciprocals whose product is 1."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Evaluate 299^2 using identities.",
                            "ideal_answer": "299^2 = (300 - 1)^2 = 300^2 - 2(300)(1) + 1^2 = 90000 - 600 + 1 = 89401.",
                            "socratic_hint": "Decompose 299 as 300 - 1."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Conceptual",
                            "question": "How can you identify if a 6-term quadratic expression is a perfect trinomial square?",
                            "ideal_answer": "It must have 3 non-negative square terms (a^2, b^2, c^2) and 3 cross-terms matching exactly ±2ab, ±2bc, ±2ca.",
                            "socratic_hint": "Check the counts of square terms and cross-terms."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "If x^2 + 1/x^2 = 51, find the value of x - 1/x.",
                            "ideal_answer": "(x - 1/x)^2 = x^2 - 2 + 1/x^2 = (x^2 + 1/x^2) - 2 = 51 - 2 = 49. Taking the square root, x - 1/x = ±7.",
                            "socratic_hint": "Write down the expansion of (x - 1/x)^2 and substitute x^2 + 1/x^2 = 51."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 6: Textbook Exercise Solver 2: Ex 4.4, 4.5 & Review
    # -------------------------------------------------------------
    m6_svg = build_algebraic_dissection_svg(
        type_ident='trinomial', a_val=100, b_val=50, c_val=30,
        title="Exercise Solver 2: Rational Expressions & Cubic Identities",
        caption="Complete step-by-step solutions for Exercises 4.4, 4.5, and End-of-Chapter problems"
    )

    m6 = {
        "order_index": 6,
        "title": "Textbook Exercise Solver 2: Exercises 4.4, 4.5 & End-of-Chapter Review (Complete Solutions)",
        "description": "Complete solutions for Exercise 4.4 (mental products and trinomials), Exercise 4.5 (rational algebraic expressions simplification), and all End-of-Chapter comprehensive synthesis problems with full step-by-step working.",
        "subtopics": [
            "Exercise 4.4 Q2 (i to viii): Mental products using identities without direct multiplication",
            "Exercise 4.5 Q1 (i to vi): Simplifying rational algebraic expressions via factoring",
            "End-of-Chapter Q1 (i to ix): Advanced products using cubic and quadratic identities",
            "End-of-Chapter Q2 (i to viii): Mental evaluations of multi-digit numbers and cubes",
            "End-of-Chapter Q3 & Q4: Factorization of cubic sums, differences, and conditional triples",
            "End-of-Chapter Q5: Real-world modeling problems (areas, perimeters, dimensions)"
        ],
        "key_concepts": [
            "Rational Expression Simplification Principle: Never cancel terms across a plus or minus sign. Factor the numerator completely, factor the denominator completely, and cancel only IDENTICAL common binomial or polynomial factors.",
            "Difference of Cubes in Fractions: In (p^4 - 16)/(p^2 - 4p + 4), factor numerator as (p^2 - 4)(p^2 + 4) = (p - 2)(p + 2)(p^2 + 4), and denominator as (p - 2)^2, canceling one (p - 2) factor.",
            "Mental Product Symmetries: Evaluating 104 * 96 by recognizing it as symmetric offsets around 100: (100 + 4)(100 - 4) = 100^2 - 4^2 = 10000 - 16 = 9984."
        ],
        "success_criteria": "Simplify complex rational algebraic expressions, expand multi-term cubics, and solve all end-of-chapter synthesis problems.",
        "chapter_notes": "Rational expressions frequently cause students to make illegal cancellations. Hammer home that ONLY multiplicative factors can be canceled.",
        "worked_examples": [
            {
                "problem": "Exercise 4.4 Q2: Use identities to find the following products without direct multiplication: (i) (41)^2, (ii) (27)^2, (iii) 23 * 17, (iv) (135)^2, (v) (97)^2, (vi) 18 * 29, (vii) 34 * 43, (viii) (205)^2.",
                "given": "Eight arithmetic products to evaluate.",
                "formula": "(a + b)^2, (a - b)^2, (a + b)(a - b), and (x + a)(x + b).",
                "substitution": "Decompose into convenient bases.",
                "calculation": "(i) 41^2 = (40 + 1)^2 = 1600 + 80 + 1 = 1681.\n(ii) 27^2 = (30 - 3)^2 = 900 - 180 + 9 = 729.\n(iii) 23 * 17 = (20 + 3)(20 - 3) = 20^2 - 3^2 = 400 - 9 = 391.\n(iv) 135^2 = (130 + 5)^2 = 16900 + 1300 + 25 = 18225.\n(v) 97^2 = (100 - 3)^2 = 10000 - 600 + 9 = 9409.\n(vi) 18 * 29: Use (20 - 2)(30 - 1) or (x + a)(x + b) with base 20: (20 - 2)(20 + 9) = 20^2 + (-2 + 9)(20) + (-2)(9) = 400 + 140 - 18 = 522.\n(vii) 34 * 43 = (40 - 6)(40 + 3) = 40^2 + (-6 + 3)(40) + (-6)(3) = 1600 - 120 - 18 = 1462.\n(viii) 205^2 = (200 + 5)^2 = 40000 + 2000 + 25 = 42025.",
                "finalAnswer": "(i) 1681; (ii) 729; (iii) 391; (iv) 18225; (v) 9409; (vi) 522; (vii) 1462; (viii) 42025",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (i, ii): Simplify the following rational expressions: (i) (3p^2 - 3pq - 18q^2) / (p^2 + 3pq - 10q^2); (ii) (n^3 - 3n^2m + 3nm^2 - m^3) / (5m^2 - 10mn + 5n^2).",
                "given": "Two rational algebraic expressions.",
                "formula": "Factor numerators and denominators completely, then cancel common factors.",
                "substitution": "Part (i): 3(p^2 - pq - 6q^2) / (p + 5q)(p - 2q); Part (ii): (n - m)^3 / 5(n - m)^2.",
                "calculation": "Part (i):\nStep 1: Numerator = 3(p^2 - pq - 6q^2) = 3(p - 3q)(p + 2q).\nStep 2: Denominator = p^2 + 3pq - 10q^2 = (p + 5q)(p - 2q).\nStep 3: Expression = 3(p - 3q)(p + 2q) / [(p + 5q)(p - 2q)].\n(Note: No factors cancel between (p+2q) and (p-2q); the expression is in lowest factored form).\n\nPart (ii):\nStep 1: Numerator = n^3 - 3n^2m + 3nm^2 - m^3 = (n - m)^3.\nStep 2: Denominator = 5(m^2 - 2mn + n^2) = 5(n - m)^2.\nStep 3: Divide numerator by denominator:\n  (n - m)^3 / [5(n - m)^2] = (n - m) / 5.",
                "finalAnswer": "Part (i): 3(p - 3q)(p + 2q) / [(p + 5q)(p - 2q)]; Part (ii): (n - m) / 5",
                "unit": "simplified rational expressions",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.5 Q1 (iv, v, vi): Simplify: (iv) (4y^2 - 20yz + 25z^2) / (25z^2 - 4y^2); (v) [(x^2 + x - 6)(x^2 - 7x + 12)] / [(x^2 - 6x + 8)(x^2 - 9)]; (vi) (p^4 - 16) / (p^2 - 4p + 4).",
                "given": "Three multi-term rational expressions.",
                "formula": "Differences of squares, perfect squares, and trinomial splitting.",
                "substitution": "Factor all 4 polynomials in each part.",
                "calculation": "Part (iv):\nNumerator: (2y - 5z)^2.\nDenominator: 25z^2 - 4y^2 = -(4y^2 - 25z^2) = -(2y - 5z)(2y + 5z).\nDivide: (2y - 5z)^2 / [-(2y - 5z)(2y + 5z)] = -(2y - 5z) / (2y + 5z) = (5z - 2y) / (5z + 2y).\n\nPart (v):\nNumerator 1: x^2 + x - 6 = (x + 3)(x - 2).\nNumerator 2: x^2 - 7x + 12 = (x - 3)(x - 4).\nDenominator 1: x^2 - 6x + 8 = (x - 2)(x - 4).\nDenominator 2: x^2 - 9 = (x - 3)(x + 3).\nMultiply and cancel:\n  [(x + 3)(x - 2)(x - 3)(x - 4)] / [(x - 2)(x - 4)(x - 3)(x + 3)] = 1.\nEvery single factor cancels identically! Value = 1.\n\nPart (vi):\nNumerator: p^4 - 16 = (p^2 - 4)(p^2 + 4) = (p - 2)(p + 2)(p^2 + 4).\nDenominator: p^2 - 4p + 4 = (p - 2)^2.\nCancel one (p - 2): (p + 2)(p^2 + 4) / (p - 2).",
                "finalAnswer": "Part (iv): (5z - 2y) / (5z + 2y); Part (v): 1; Part (vi): (p + 2)(p^2 + 4) / (p - 2)",
                "unit": "simplified expressions",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1 (v) & Q2 (ii, v): (Q1 v) Find product (s - 2t)(s^2 + 2st + 4t^2). (Q2 ii) 104 * 96. (Q2 v) (199)^3.",
                "given": "Cubic factor form, symmetric difference of squares, and cube of 199.",
                "formula": "(a - b)(a^2 + ab + b^2) = a^3 - b^3; (a + b)(a - b) = a^2 - b^2; (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3.",
                "substitution": "Q1 v: a = s, b = 2t; Q2 ii: (100 + 4)(100 - 4); Q2 v: (200 - 1)^3.",
                "calculation": "Q1 (v):\nNotice the pattern: (s - 2t)[s^2 + s*(2t) + (2t)^2] is the difference of cubes identity a^3 - b^3.\n= s^3 - (2t)^3 = s^3 - 8t^3.\n\nQ2 (ii):\n104 * 96 = (100 + 4)(100 - 4) = 100^2 - 4^2 = 10,000 - 16 = 9,984.\n\nQ2 (v):\n199^3 = (200 - 1)^3 = 200^3 - 3(200)^2(1) + 3(200)(1)^2 - 1^3\n= 8,000,000 - 3(40,000) + 3(200) - 1\n= 8,000,000 - 120,000 + 600 - 1\n= 7,880,000 + 599 = 7,880,599.",
                "finalAnswer": "Q1 (v): s^3 - 8t^3; Q2 (ii): 9,984; Q2 (v): 7,880,599",
                "unit": "algebraic expression and integers",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Canceling individual terms across addition signs in rational expressions, e.g. canceling x^2 from numerator and denominator in (x^2 + 1)/(x^2 + 2).",
            "Assuming 199^3 = 200^3 - 1^3 = 8,000,000 - 1 = 7,999,999, dropping all cross terms."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Teach rational expressions by emphasizing factoring first, putting parentheses around entire binomials, and only crossing out matching parenthesized blocks. Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 2').",
        "visual_lesson_plan": {
            "title": "Rational Expressions & Synthesis",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Rational expression factor cancellation diagram.",
            "concept_visuals": [
                {
                    "concept_title": "Rational Simplification Workflow",
                    "diagram_title": "Factoring & Cancellation",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m6_svg,
                    "interactive_math_formula": "P(x)/Q(x) = [A(x)*B(x)] / [A(x)*C(x)] = B(x)/C(x)",
                    "mafs_graph_config": {"domain": [-5, 5], "range": [-5, 5]},
                    "image_query": "Simplifying rational expressions canceling common factors algebra",
                    "video_query": "Simplifying rational algebraic expressions step by step tutorial",
                    "image_url": "/images/curriculum/ch4_exercise_solver2.png",
                    "what_to_make": "Workflow diagram showing factoring before cancellation.",
                    "what_to_explain": "Stress that only multiplicative common factors cancel.",
                    "timing_and_cue": "Show before working on rational expression problems."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Rational Expressions & Advanced Identities",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "Can you cancel x from (x + 5) / (x + 3)?",
                            "ideal_answer": "No, because x is a term within an addition, not a common multiplicative factor of the entire numerator and denominator.",
                            "socratic_hint": "Try plugging in x = 1: does (1+5)/(1+3) equal 5/3?"
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What is the result of simplifying (x^2 - 9) / (x - 3)?",
                            "ideal_answer": "(x - 3)(x + 3) / (x - 3) = x + 3 (for x != 3).",
                            "socratic_hint": "Factor the numerator as a difference of two squares."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Evaluate 104 * 96 mentally using identities.",
                            "ideal_answer": "(100 + 4)(100 - 4) = 100^2 - 4^2 = 10000 - 16 = 9984.",
                            "socratic_hint": "Express 104 and 96 as offsets from 100 and apply (a+b)(a-b) = a^2 - b^2."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Find the product (x - 3)(x^2 + 3x + 9) using an identity.",
                            "ideal_answer": "It matches (a - b)(a^2 + ab + b^2) = a^3 - b^3, so the product is x^3 - 3^3 = x^3 - 27.",
                            "socratic_hint": "Compare with the difference of cubes factor formula."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "If x + y + z = 0, prove that (x + y)^3 + (y + z)^3 + (z + x)^3 = 3(x + y)(y + z)(z + x).",
                            "ideal_answer": "Let A = x + y, B = y + z, C = z + x. Then A + B + C = 2(x + y + z) = 2(0) = 0. By the conditional cubic theorem, since A + B + C = 0, A^3 + B^3 + C^3 = 3ABC. Substituting back gives 3(x + y)(y + z)(z + x).",
                            "socratic_hint": "Define A = x+y, B = y+z, C = z+x and check their sum A + B + C."
                        }
                    ]
                }
            ]
        }
    }

    return [m1, m2, m3, m4, m5, m6]
