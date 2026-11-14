"""
Chapter 4: Exploring Algebraic Identities - Module 1
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_algebraic_dissection_svg

def get_m1():
    m1_svg = build_algebraic_dissection_svg(
        type_ident='a_plus_b_sq', a_val=130, b_val=60,
        title="Geometric Proof: (a + b)^2 = a^2 + 2ab + b^2",
        caption="Large square decomposed into a^2 (blue), two ab rectangles (green), and b^2 (purple)"
    )

    return {
        "order_index": 1,
        "title": "Geometric Proofs of Binomial Squares: (a + b)^2, Area Dissections, Mental Arithmetic & Section 4.1",
        "description": "Understand algebraic identities through geometric dissections. Visualize (a + b)^2 as the area of a square of side (a + b) decomposed into four sub-regions: a^2, two ab rectangles, and b^2. Master rapid mental arithmetic using binomial squares and solve 100% of textbook examples and Exercise 4.1 problems.",
        "subtopics": [
            "Difference between conditional algebraic equations and universal algebraic identities",
            "Geometric proof of (a + b)^2 = a^2 + 2ab + b^2 via Euclidean area models",
            "Partitioning a square of side (a + b) into four sub-regions: a^2, two ab rectangles, and b^2",
            "Consecutive square number patterns and algebraic invariant formulation",
            "Application to mental arithmetic: (10 + x)^2, (100 + x)^2, and (200 + x)^2 expansions",
            "Expansion of fractional and decimal coefficients without skipped arithmetic",
            "Avoiding the universal freshman error: (a + b)^2 != a^2 + b^2"
        ],
        "key_concepts": [
            "Algebraic Identity Definition: An equality that is true for ALL real values of the variables involved, unlike conditional equations which hold only for specific values.",
            "Square of a Binomial Sum: (a + b)^2 = a^2 + 2ab + b^2. Geometrically represents a square of side length (a + b) partitioned into an a*a square, two a*b rectangles, and a b*b square.",
            "Area Conservation Principle: The total area of a composite figure equals the exact sum of the areas of its non-overlapping constituent geometric pieces.",
            "Cross-Term Mandate: The 2ab term (twice the product of the terms) is strictly required by the distributive law (a + b)(a + b) = a(a + b) + b(a + b) = a^2 + ab + ba + b^2.",
            "Mental Arithmetic Decomposition: Evaluating numbers like 43^2, 64^2, 105^2, and 205^2 by decomposing them into (base + offset)^2."
        ],
        "success_criteria": "State and prove (a + b)^2 geometrically, expand any binomial with integer, fractional, or decimal coefficients, and calculate squares of numbers mentally with complete step-by-step mathematical reasoning.",
        "chapter_notes": "Identities are universal mathematical invariants. In Ganita Manjari Chapter 4, every identity is introduced through geometric intuition before formal algebraic manipulation. Never let students omit the cross term 2ab.",
        "worked_examples": [
            {
                "problem": "Textbook Example 1: Consider any three consecutive square numbers (e.g., 1, 4, 9, or 25, 36, 49). Add the smallest and largest squares, and subtract twice the middle square. Explain why the result is always 2 using an algebraic identity.",
                "given": "Consecutive square numbers: (n - 1)^2, n^2, and (n + 1)^2.",
                "formula": "(n - 1)^2 + (n + 1)^2 - 2(n^2). Use (a - b)^2 = a^2 - 2ab + b^2 and (a + b)^2 = a^2 + 2ab + b^2.",
                "substitution": "Substitute expansions: [(n^2 - 2n(1) + 1^2) + (n^2 + 2n(1) + 1^2)] - 2n^2.",
                "calculation": "Step 1: Write the sum of the smallest and largest squares: (n - 1)^2 + (n + 1)^2.\nStep 2: Expand using binomial square identities: (n^2 - 2n + 1) + (n^2 + 2n + 1) = 2n^2 + 2.\nStep 3: Subtract twice the middle square: (2n^2 + 2) - 2(n^2) = 2n^2 + 2 - 2n^2 = 2.\nStep 4: Verify with numerical examples:\n  - For n = 2: 1 + 9 - 2(4) = 10 - 8 = 2.\n  - For n = 6: 25 + 49 - 2(36) = 74 - 72 = 2.\nStep 5: Conclude that because the algebraic expression simplifies identically to the constant 2, the result is invariant for all real numbers n.",
                "finalAnswer": "The result is always 2 for all consecutive squares, proven identically by (n - 1)^2 + (n + 1)^2 - 2n^2 = 2",
                "unit": "algebraic proof",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 2: Let a = -2 and b = -3. Verify that (a + b)^2 = a^2 + 2ab + b^2 for negative values of variables.",
                "given": "Values: a = -2, b = -3.",
                "formula": "LHS = (a + b)^2; RHS = a^2 + 2ab + b^2.",
                "substitution": "LHS = (-2 + (-3))^2; RHS = (-2)^2 + 2(-2)(-3) + (-3)^2.",
                "calculation": "Step 1: Evaluate LHS: a + b = -2 + (-3) = -5.\nStep 2: Compute LHS square: (-5)^2 = 25.\nStep 3: Evaluate RHS individual terms:\n  - a^2 = (-2)^2 = 4\n  - 2ab = 2 * (-2) * (-3) = 2 * 6 = 12\n  - b^2 = (-3)^2 = 9\nStep 4: Sum the RHS terms: 4 + 12 + 9 = 25.\nStep 5: Compare LHS and RHS: LHS = 25, RHS = 25. Thus LHS = RHS.",
                "finalAnswer": "LHS = RHS = 25, confirming the identity holds universally for negative numbers",
                "unit": "numerical verification",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 3: Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (5x + 2y)^2.",
                "given": "Binomial: (5x + 2y)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, where a = 5x and b = 2y.",
                "substitution": "(5x + 2y)^2 = (5x)^2 + 2*(5x)*(2y) + (2y)^2.",
                "calculation": "Step 1: Identify terms: a = 5x, b = 2y.\nStep 2: Square the first term: a^2 = (5x)^2 = 25x^2.\nStep 3: Compute the cross term: 2ab = 2 * (5x) * (2y) = 20xy.\nStep 4: Square the second term: b^2 = (2y)^2 = 4y^2.\nStep 5: Combine all terms: 25x^2 + 20xy + 4y^2.",
                "finalAnswer": "(5x + 2y)^2 = 25x^2 + 20xy + 4y^2",
                "unit": "algebraic expression",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m1_svg
            },
            {
                "problem": "Textbook Example 4: Calculate 43^2 without multiplying directly, using the square of a binomial.",
                "given": "Number to square: 43.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, decomposing 43 = 40 + 3.",
                "substitution": "43^2 = (40 + 3)^2 = 40^2 + 2*(40)*(3) + 3^2.",
                "calculation": "Step 1: Decompose 43 into tens and units: 43 = 40 + 3.\nStep 2: Identify a = 40 and b = 3.\nStep 3: Compute 40^2 = 1600.\nStep 4: Compute 2 * 40 * 3 = 240.\nStep 5: Compute 3^2 = 9.\nStep 6: Sum the components: 1600 + 240 + 9 = 1849.",
                "finalAnswer": "43^2 = 1849",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q1 (i): Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (7x + 4y)^2.",
                "given": "Expression: (7x + 4y)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with a = 7x and b = 4y.",
                "substitution": "(7x + 4y)^2 = (7x)^2 + 2*(7x)*(4y) + (4y)^2.",
                "calculation": "Step 1: Set a = 7x and b = 4y.\nStep 2: Square first term: (7x)^2 = 49x^2.\nStep 3: Compute cross term: 2 * (7x) * (4y) = 56xy.\nStep 4: Square second term: (4y)^2 = 16y^2.\nStep 5: Combine terms: 49x^2 + 56xy + 16y^2.",
                "finalAnswer": "(7x + 4y)^2 = 49x^2 + 56xy + 16y^2",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q1 (ii): Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (7/5 x + 3/2 y)^2.",
                "given": "Fractional expression: (7/5 x + 3/2 y)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with a = 7/5 x and b = 3/2 y.",
                "substitution": "(7/5 x + 3/2 y)^2 = (7/5 x)^2 + 2*(7/5 x)*(3/2 y) + (3/2 y)^2.",
                "calculation": "Step 1: Square first term: (7/5 x)^2 = (49/25) x^2.\nStep 2: Compute cross term: 2 * (7/5) * (3/2) * xy = 2 * (21/10) xy = (42/10) xy = (21/5) xy.\nStep 3: Square second term: (3/2 y)^2 = (9/4) y^2.\nStep 4: Combine all terms: 49/25 x^2 + 21/5 xy + 9/4 y^2.",
                "finalAnswer": "(7/5 x + 3/2 y)^2 = 49/25 x^2 + 21/5 xy + 9/4 y^2",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q1 (iii): Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (2.5p + 1.5q)^2.",
                "given": "Decimal expression: (2.5p + 1.5q)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with a = 2.5p and b = 1.5q.",
                "substitution": "(2.5p + 1.5q)^2 = (2.5p)^2 + 2*(2.5p)*(1.5q) + (1.5q)^2.",
                "calculation": "Step 1: Square first term: (2.5p)^2 = 6.25 p^2.\nStep 2: Compute cross term: 2 * 2.5 * 1.5 * pq = 5.0 * 1.5 pq = 7.5 pq.\nStep 3: Square second term: (1.5q)^2 = 2.25 q^2.\nStep 4: Combine all terms: 6.25 p^2 + 7.5 pq + 2.25 q^2.",
                "finalAnswer": "(2.5p + 1.5q)^2 = 6.25 p^2 + 7.5 pq + 2.25 q^2",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q1 (iv): Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (3/4 s + 8t)^2.",
                "given": "Expression: (3/4 s + 8t)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with a = 3/4 s and b = 8t.",
                "substitution": "(3/4 s + 8t)^2 = (3/4 s)^2 + 2*(3/4 s)*(8t) + (8t)^2.",
                "calculation": "Step 1: Square first term: (3/4 s)^2 = (9/16) s^2.\nStep 2: Compute cross term: 2 * (3/4) * 8 * st = (3/2) * 8 * st = 12 st.\nStep 3: Square second term: (8t)^2 = 64 t^2.\nStep 4: Combine all terms: 9/16 s^2 + 12st + 64t^2.",
                "finalAnswer": "(3/4 s + 8t)^2 = 9/16 s^2 + 12st + 64t^2",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q1 (v): Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (1/3 x + 2y)^2.",
                "given": "Expression: (1/3 x + 2y)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with a = 1/3 x and b = 2y.",
                "substitution": "(1/3 x + 2y)^2 = (1/3 x)^2 + 2*(1/3 x)*(2y) + (2y)^2.",
                "calculation": "Step 1: Square first term: (1/3 x)^2 = (1/9) x^2.\nStep 2: Compute cross term: 2 * (1/3) * 2 * xy = (4/3) xy.\nStep 3: Square second term: (2y)^2 = 4y^2.\nStep 4: Combine all terms: 1/9 x^2 + 4/3 xy + 4y^2.",
                "finalAnswer": "(1/3 x + 2y)^2 = 1/9 x^2 + 4/3 xy + 4y^2",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q1 (vi): Using the identity (a + b)^2 = a^2 + 2ab + b^2, expand (1/4 x + 1/5 y)^2.",
                "given": "Expression: (1/4 x + 1/5 y)^2.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with a = 1/4 x and b = 1/5 y.",
                "substitution": "(1/4 x + 1/5 y)^2 = (1/4 x)^2 + 2*(1/4 x)*(1/5 y) + (1/5 y)^2.",
                "calculation": "Step 1: Square first term: (1/4 x)^2 = (1/16) x^2.\nStep 2: Compute cross term: 2 * (1/4) * (1/5) * xy = (2/20) xy = (1/10) xy.\nStep 3: Square second term: (1/5 y)^2 = (1/25) y^2.\nStep 4: Combine all terms: 1/16 x^2 + 1/10 xy + 1/25 y^2.",
                "finalAnswer": "(1/4 x + 1/5 y)^2 = 1/16 x^2 + 1/10 xy + 1/25 y^2",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q2 (i): Using the identity (a + b)^2 = a^2 + 2ab + b^2, find the value of (64)^2.",
                "given": "Number to square: 64.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with 64 = 60 + 4.",
                "substitution": "(60 + 4)^2 = 60^2 + 2*(60)*(4) + 4^2.",
                "calculation": "Step 1: Decompose 64 = 60 + 4.\nStep 2: Evaluate 60^2 = 3600.\nStep 3: Evaluate cross term 2 * 60 * 4 = 480.\nStep 4: Evaluate 4^2 = 16.\nStep 5: Sum components: 3600 + 480 + 16 = 4096.",
                "finalAnswer": "64^2 = 4096",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q2 (ii): Using the identity (a + b)^2 = a^2 + 2ab + b^2, find the value of (105)^2.",
                "given": "Number to square: 105.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with 105 = 100 + 5.",
                "substitution": "(100 + 5)^2 = 100^2 + 2*(100)*(5) + 5^2.",
                "calculation": "Step 1: Decompose 105 = 100 + 5.\nStep 2: Evaluate 100^2 = 10,000.\nStep 3: Evaluate cross term 2 * 100 * 5 = 1,000.\nStep 4: Evaluate 5^2 = 25.\nStep 5: Sum components: 10,000 + 1,000 + 25 = 11,025.",
                "finalAnswer": "105^2 = 11,025",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 4.1 Q2 (iii): Using the identity (a + b)^2 = a^2 + 2ab + b^2, find the value of (205)^2.",
                "given": "Number to square: 205.",
                "formula": "(a + b)^2 = a^2 + 2ab + b^2, with 205 = 200 + 5.",
                "substitution": "(200 + 5)^2 = 200^2 + 2*(200)*(5) + 5^2.",
                "calculation": "Step 1: Decompose 205 = 200 + 5.\nStep 2: Evaluate 200^2 = 40,000.\nStep 3: Evaluate cross term 2 * 200 * 5 = 2,000.\nStep 4: Evaluate 5^2 = 25.\nStep 5: Sum components: 40,000 + 2,000 + 25 = 42,025.",
                "finalAnswer": "205^2 = 42,025",
                "unit": "integer",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Writing (a + b)^2 = a^2 + b^2, completely dropping the cross-term 2ab. In geometric terms, this discards two entire rectangular corridors!",
            "Squaring fractional coefficients incorrectly, e.g., (3/4 s)^2 written as 3/16 s^2 instead of squaring both numerator and denominator to get 9/16 s^2.",
            "Decomposing numbers awkwardly (e.g. 64 as 62 + 2 instead of 60 + 4), which defeats the mental arithmetic advantage of base-10 zeroes."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Start with a square sheet of paper partitioned into 4 zones. Emphasize that the cross-term 2ab comes from the two congruent rectangular strips. Call write_chalkboard(action='draw_svg_diagram', content='Geometric Proof: (a + b)^2'). Always emphasize that identities hold for ALL numbers.",
        "visual_lesson_plan": {
            "title": "Geometric Model of (a + b)^2",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Dissected square showing regions a^2, ab, ab, and b^2.",
            "concept_visuals": [
                {
                    "concept_title": "Square of a Binomial Dissection",
                    "diagram_title": "Geometric Proof: (a + b)^2",
                    "interactive_math_formula": "(a + b)^2 = a^2 + 2ab + b^2",
                    "mafs_graph_config": {
                        "domain": [-1, 7],
                        "range": [-1, 7],
                        "curves": [
                            {"fn": "x^2", "color": "#2563EB", "label": "y = x^2"},
                            {"fn": "(x + 2)^2", "color": "#16A34A", "label": "y = (x + 2)^2 = x^2 + 4x + 4"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "(0,0)"},
                            {"x": 2, "y": 16, "label": "x=2, y=16"},
                            {"x": -2, "y": 0, "label": "Vertex (-2,0)"}
                        ]
                    },
                    "image_query": "algebra geometric area dissection model square square of binomial",
                    "video_query": "geometric visual proof binomial square expansion animated",
                    "what_to_explain": "Notice how expanding (x + 2)^2 produces the parabola shifted horizontally by 2 units, with minimum at (-2,0) and y-intercept at (0,4)."
                },
                {
                    "concept_title": "Mental Arithmetic Base-10 Decomposition Curve",
                    "diagram_title": "Parabolic Growth of (100 + x)^2",
                    "interactive_math_formula": "f(x) = (100 + x)^2 = 10000 + 200x + x^2",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [8000, 13000],
                        "curves": [
                            {"fn": "10000 + 200*x + x^2", "color": "#D97706", "label": "(100 + x)^2"},
                            {"fn": "10000 + 200*x", "color": "#94A3B8", "label": "Linear Tangent 10000 + 200x"}
                        ],
                        "points": [
                            {"x": 0, "y": 10000, "label": "100^2 = 10000"},
                            {"x": 4, "y": 10816, "label": "104^2 = 10816"},
                            {"x": 5, "y": 11025, "label": "105^2 = 11025"}
                        ]
                    },
                    "image_query": "rapid mental math base 10 squaring identities graph",
                    "video_query": "mental math Vedic math squaring numbers using algebra identities",
                    "what_to_explain": "For small x relative to 100, (100 + x)^2 is dominated by the linear term 10000 + 200x, with x^2 adding a small correction."
                },
                {
                    "concept_title": "Fractional Binomial Scaling Surface",
                    "diagram_title": "Scaling Behavior of (ax + by)^2",
                    "interactive_math_formula": "f(x) = (0.75x + 2)^2",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-1, 25],
                        "curves": [
                            {"fn": "(0.75*x + 2)^2", "color": "#7C3AED", "label": "y = (3/4 x + 2)^2"},
                            {"fn": "0.5625*x^2", "color": "#3B82F6", "label": "Leading Term 9/16 x^2"}
                        ],
                        "points": [
                            {"x": 0, "y": 4, "label": "y-intercept (0, 4)"},
                            {"x": -2.67, "y": 0, "label": "Root (-8/3, 0)"}
                        ]
                    },
                    "image_query": "fractional coefficient quadratic algebra function",
                    "video_query": "graphing quadratic functions fractional coefficients",
                    "what_to_explain": "The coefficient of x^2 is (3/4)^2 = 9/16, which flattens the parabola while shifting the vertex to x = -8/3."
                },
                {
                    "concept_title": "Cross-Term Growth Dynamics",
                    "diagram_title": "Contribution of Cross-Term 2ab vs Squares a^2 + b^2",
                    "interactive_math_formula": "Ratio: 2ab / (a^2 + b^2) <= 1",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 100],
                        "curves": [
                            {"fn": "2*x*5", "color": "#059669", "label": "Cross Term 2ab (b=5)"},
                            {"fn": "x^2 + 25", "color": "#DC2626", "label": "Sum of Squares a^2 + b^2 (b=5)"}
                        ],
                        "points": [
                            {"x": 5, "y": 50, "label": "Equal at a = b = 5"}
                        ]
                    },
                    "image_query": "AM GM inequality quadratic identity cross term",
                    "video_query": "why cross term matters algebra identities geometric intuition",
                    "what_to_explain": "By the AM-GM inequality, 2ab <= a^2 + b^2 for all real numbers, with equality holding if and only if a = b."
                },
                {
                    "concept_title": "Two-Variable Linear Parameter Grid",
                    "diagram_title": "Expansion Surface (x + y)^2 - x^2 - y^2 = 2xy",
                    "interactive_math_formula": "Delta(x, y) = 2xy",
                    "mafs_graph_config": {
                        "domain": [-4, 4],
                        "range": [-16, 16],
                        "curves": [
                            {"fn": "2*x*2", "color": "#F59E0B", "label": "y=2: Delta = 4x"},
                            {"fn": "2*x*3", "color": "#10B981", "label": "y=3: Delta = 6x"},
                            {"fn": "-2*x*2", "color": "#EF4444", "label": "y=-2: Delta = -4x"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Origin (0,0)"},
                            {"x": 2, "y": 8, "label": "Delta(2,2) = 8"}
                        ]
                    },
                    "image_query": "bivariate polynomial contours cross product term",
                    "video_query": "bivariate algebraic functions expansion",
                    "what_to_explain": "The cross term is linearly dependent on each variable individually, producing a bilinear saddle shape in 3D."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Identities vs Equations",
                    "questions": [
                        {
                            "question": "What is the fundamental difference between an algebraic identity and an algebraic equation?",
                            "type": "short_answer",
                            "options": [
                                "An identity is true for all possible values of its variables; an equation is true only for specific solutions",
                                "An equation has an equals sign; an identity does not",
                                "An identity only works for positive integers",
                                "There is no difference"
                            ],
                            "ideal_answer": "An identity holds true for every real value assigned to the variables, whereas a conditional equation is satisfied only by specific values (roots).",
                            "socratic_hint": "Test x = 0, 1, -5 in x^2 - 1 = 0 versus (x + 1)^2 = x^2 + 2x + 1. Which one is always true?"
                        },
                        {
                            "question": "If you evaluate (a + b)^2 by setting a = 10 and b = 2, what numerical value does the cross-term 2ab contribute?",
                            "type": "short_answer",
                            "options": ["40", "20", "100", "4"],
                            "ideal_answer": "40 (calculated as 2 * 10 * 2 = 40).",
                            "socratic_hint": "Multiply 2 by both a and b."
                        },
                        {
                            "question": "Why is (a + b)^2 = a^2 + b^2 mathematically incorrect for non-zero numbers?",
                            "type": "short_answer",
                            "options": [
                                "It completely omits the two ab rectangular regions created by the distributive law",
                                "Because a and b must always be negative",
                                "Because squares can never be added together",
                                "It is actually correct for all numbers"
                            ],
                            "ideal_answer": "By the distributive law, (a + b)(a + b) = a^2 + ab + ba + b^2 = a^2 + 2ab + b^2. Dropping 2ab discards two entire rectangular areas.",
                            "socratic_hint": "Draw a square of side 5 + 3. Is an 8x8 square equal to 5x5 + 3x3?"
                        },
                        {
                            "question": "How do you rapidly compute 105^2 using the identity (a + b)^2?",
                            "type": "short_answer",
                            "options": [
                                "Decompose into (100 + 5)^2 = 10000 + 1000 + 25 = 11025",
                                "Multiply 105 by 10 and add 5",
                                "100^2 + 5^2 = 10025",
                                "105 * 105 by long multiplication"
                            ],
                            "ideal_answer": "(100 + 5)^2 = 100^2 + 2(100)(5) + 5^2 = 10000 + 1000 + 25 = 11025.",
                            "socratic_hint": "Split 105 into a friendly round number (100) and a single digit (5)."
                        },
                        {
                            "question": "What is the expanded form of (7/5 x + 3/2 y)^2?",
                            "type": "short_answer",
                            "options": [
                                "49/25 x^2 + 21/5 xy + 9/4 y^2",
                                "49/25 x^2 + 9/4 y^2",
                                "7/5 x^2 + 21/10 xy + 3/2 y^2",
                                "49/5 x^2 + 42/10 xy + 9/2 y^2"
                            ],
                            "ideal_answer": "49/25 x^2 + 21/5 xy + 9/4 y^2.",
                            "socratic_hint": "Square both numerators and denominators for the squared terms, and compute 2 * (7/5) * (3/2)."
                        }
                    ]
                }
            ]
        }
    }
