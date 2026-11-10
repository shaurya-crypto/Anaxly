"""
Chapter 3: The World of Numbers - Module 6
Curriculum ID: 09ca99d2-0489-48f2-8d39-8b26ca7885c9
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m6():
    m6_svg = build_cartesian_svg(
        domain=(-4, 4), range_y=(-4, 4),
        points=[
            {"x": 1, "y": -1, "label": "(1, -1)", "color": "#2563EB", "sub": "ab = -1"},
            {"x": 2, "y": -0.5, "label": "(2, -0.5)", "color": "#2563EB", "sub": "ab = -1"},
            {"x": -1, "y": 1, "label": "(-1, 1)", "color": "#DC2626", "sub": "ab = -1"},
            {"x": -2, "y": 0.5, "label": "(-2, 0.5)", "color": "#DC2626", "sub": "ab = -1"}
        ],
        lines=[
            {"p1": (-4, 0), "p2": (4, 0), "color": "#64748B", "stroke_width": 1.5},
            {"p1": (0, -4), "p2": (0, 4), "color": "#64748B", "stroke_width": 1.5}
        ],
        title="Theoretical Invariant: a + 1/b = 0 implies ab = -1 < 0",
        caption="The hyperbola ab = -1 lies strictly in Quadrants 2 and 4, proving ab is unconditionally negative"
    )

    return {
        "order_index": 6,
        "title": "Textbook Exercise Solver 5: Successive Magnification, Theoretical Invariants & End-of-Chapter Master Challenges (End-of-Chapter Complete)",
        "description": "Exhaustive step-by-step solutions to End-of-Chapter Questions 4, 9, 10, 13, 14, and 15. Master successive magnification on the number line, rigorous algebraic proofs of product negativity (ab = -1), the 4th-decimal place termination theorem, integer spacing lemmas (k2 - k1 > n+1), and the zero-sum of squares theorem.",
        "subtopics": [
            "Successive magnification method: Locating 0.532 and 1.15 on the number line",
            "Sign Invariant Theorem: Proving ab = -1 < 0 from a + 1/b = 0 without numerical values",
            "Termination Invariant: p/10^4 representation and necessary denominator divisibility (2^4 or 5^4)",
            "The Spacing Lemma: Why k2 - k1 > n + 1 is necessary to embed n rational numbers",
            "Trivariate Zero Theorem: Proving x = y = z = 0 from x + y + z = 0 and xy + yz + zx = 0 via x^2 + y^2 + z^2 = 0",
            "Rigorous proof that the arithmetic mean (a + b)/2 lies strictly between a and b"
        ],
        "key_concepts": [
            "Successive Magnification: Visualizing decimal fractions by zooming into 10-fold subdivisions of intervals.",
            "Reciprocal Sign Theorem: a + 1/b = 0 <=> a = -1/b <=> a*b = -1. Because -1 < 0, the product ab must be strictly negative.",
            "Decimal Factorization Invariant: If the last non-zero digit is at decimal place k, the denominator in lowest terms must have max(m, n) = k, meaning it MUST be divisible by either 2^k or 5^k.",
            "Lattice Spacing Lemma: Between two integers k1 and k2, there exist exactly (k2 - k1 - 1) distinct integers. To have at least n integers, (k2 - k1 - 1) >= n <=> k2 - k1 > n + 1.",
            "Sum of Squares Tautology: (x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx). When both linear sum and pairwise product sum are 0, x^2 + y^2 + z^2 = 0, which for real numbers forces x = y = z = 0.",
            "Strict Intermediate Mean: For real numbers a < b, adding a yields 2a < a + b => a < (a+b)/2; adding b yields a + b < 2b => (a+b)/2 < b."
        ],
        "success_criteria": "Students can apply successive magnification to visualize decimal points, construct rigorous algebraic proofs of sign and divisibility invariants, and solve high-level competitive board challenges.",
        "chapter_notes": "Module 6 concludes Chapter 3 with mathematical proofs and deep analytical challenges from the Ganita Manjari Grade 9 Part 1 textbook.",
        "common_misconceptions": [
            {"misconception": "Thinking x^2 + y^2 + z^2 = 0 can have non-zero real solutions", "clarification": "The square of any real number is non-negative (x^2 >= 0); the only way a sum of non-negative reals equals zero is if each term is individually zero."},
            {"misconception": "Confusing (k2 - k1) with the count of strictly intermediate integers", "clarification": "The number of integers strictly between k1 and k2 is (k2 - k1 - 1), not (k2 - k1). For example, between 1 and 3 there is only 3 - 1 - 1 = 1 integer (the number 2)."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through the advanced theoretical problems of Chapter 3. Provide complete algebraic derivations without skipping steps.",
        "visual_lesson_plan": {
            "title": "Visualizing Theoretical Invariants and Successive Magnification",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Interactive coordinate plot of the hyperbola ab = -1 in Quadrants 2 and 4, proving the sign invariant.",
            "concept_visuals": [
                {
                    "concept_title": "Sign Invariant: ab = -1 Hyperbola",
                    "diagram_title": "Hyperbolic Branching in Q2 and Q4",
                    "interactive_math_formula": "ab = -1 < 0",
                    "mafs_graph_config": {
                        "domain": [-4, 4],
                        "range": [-4, 4],
                        "curves": [
                            {"fn": "-1/x", "color": "#2563EB", "label": "b = -1/a"}
                        ],
                        "points": [
                            {"x": 1, "y": -1, "label": "(1, -1)"},
                            {"x": 2, "y": -0.5, "label": "(2, -0.5)"},
                            {"x": -1, "y": 1, "label": "(-1, 1)"},
                            {"x": -2, "y": 0.5, "label": "(-2, 0.5)"}
                        ]
                    },
                    "image_query": "hyperbola in second and fourth quadrants negative product",
                    "video_query": "algebraic proof of sign product of rational numbers",
                    "what_to_explain": "Since a + 1/b = 0 leads to ab = -1, the curve exists exclusively in Quadrants 2 and 4 where the product of coordinates is negative."
                },
                {
                    "concept_title": "Successive Magnification: Locating 0.532",
                    "diagram_title": "Three-Stage Zoom: [0, 1] -> [0.5, 0.6] -> [0.53, 0.54]",
                    "interactive_math_formula": "0.53 < 0.532 < 0.54",
                    "mafs_graph_config": {
                        "domain": [0.530, 0.540],
                        "range": [-1, 1],
                        "points": [
                            {"x": 0.530, "y": 0, "label": "0.530"},
                            {"x": 0.532, "y": 0, "label": "0.532 (Target)"},
                            {"x": 0.535, "y": 0, "label": "0.535"},
                            {"x": 0.540, "y": 0, "label": "0.540"}
                        ]
                    },
                    "image_query": "successive magnification method locating decimals on number line",
                    "video_query": "visualize number line representation by successive magnification",
                    "what_to_explain": "Each magnification step magnifies a sub-interval ten-fold until the third decimal place digit 2 is located."
                },
                {
                    "concept_title": "Sum of Squares Zero Invariant: x^2 + y^2 + z^2 = 0",
                    "diagram_title": "Degenerate Sphere at Origin",
                    "interactive_math_formula": "x^2 + y^2 + z^2 = 0 \\implies x=0, y=0, z=0",
                    "mafs_graph_config": {
                        "domain": [-2, 2],
                        "range": [-2, 2],
                        "points": [
                            {"x": 0, "y": 0, "label": "Unique Real Solution (0, 0, 0)"}
                        ]
                    },
                    "image_query": "sum of squares equals zero unique solution origin point",
                    "video_query": "if x2 plus y2 plus z2 equals 0 then x equals y equals z equals 0",
                    "what_to_explain": "Because real squares are non-negative, the only way their sum can be zero is if every individual term is 0."
                },
                {
                    "concept_title": "Integer Lattice Spacing Lemma: k2 - k1 > n + 1",
                    "diagram_title": "Embedding n Points in an Integer Gap",
                    "interactive_math_formula": "k_2 - k_1 \\ge n + 2",
                    "mafs_graph_config": {
                        "domain": [6, 12],
                        "range": [-1, 1],
                        "points": [
                            {"x": 7, "y": 0, "label": "k1 = 7"},
                            {"x": 8, "y": 0, "label": "Int 1"},
                            {"x": 9, "y": 0, "label": "Int 2"},
                            {"x": 10, "y": 0, "label": "k2 = 10 (k2-k1=3, n=2)"}
                        ]
                    },
                    "image_query": "integer number line points between two integers formula",
                    "video_query": "number of integers between two numbers formula proof",
                    "what_to_explain": "Between k1 and k2 there are exactly (k2 - k1 - 1) internal integers, requiring k2 - k1 > n + 1 to host n numbers."
                },
                {
                    "concept_title": "Arithmetic Mean Invariant: a < (a+b)/2 < b",
                    "diagram_title": "Strict Bisection of Rational Segment",
                    "interactive_math_formula": "a < \\frac{a+b}{2} < b",
                    "mafs_graph_config": {
                        "domain": [0, 4],
                        "range": [-1, 1],
                        "points": [
                            {"x": 1, "y": 0, "label": "a"},
                            {"x": 2, "y": 0, "label": "Midpoint (a+b)/2"},
                            {"x": 3, "y": 0, "label": "b"}
                        ]
                    },
                    "image_query": "midpoint between two numbers on number line proof",
                    "video_query": "prove that a plus b over 2 lies between a and b",
                    "what_to_explain": "The average of two numbers is equidistant from both endpoints and strictly interior to the interval."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Theoretical Number Properties",
                    "questions": [
                        {
                            "question": "If a and b are non-zero rational numbers and a + 1/b = 0, what is the value of the product ab?",
                            "type": "short_answer",
                            "ideal_answer": "ab = -1 (which is strictly negative).",
                            "socratic_hint": "Subtract 1/b to the RHS: a = -1/b, then multiply both sides by b."
                        },
                        {
                            "question": "Why does x^2 + y^2 + z^2 = 0 force x = 0, y = 0, and z = 0 for real numbers?",
                            "type": "short_answer",
                            "ideal_answer": "Because the square of any real number is non-negative (>= 0); the sum of non-negative terms can only equal zero if each term is zero.",
                            "socratic_hint": "Can a non-zero real number have a negative square?"
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "End-of-Chapter Q4 (i): Locate the rational number 0.532 on the number line using the method of successive magnification.",
                "given": "Number 0.532.",
                "formula": "Step 1: Identify unit interval. Step 2: Divide into tenths. Step 3: Divide into hundredths. Step 4: Divide into thousandths.",
                "substitution": "0 < 0.532 < 1.",
                "calculation": "1. Magnification 1: 0.532 lies between integers 0 and 1. Divide [0, 1] into 10 equal parts of length 0.1. 0.532 lies in [0.5, 0.6].\n2. Magnification 2: Zoom into interval [0.5, 0.6]. Divide into 10 equal parts of length 0.01: 0.50, 0.51, 0.52, 0.53, 0.54, ..., 0.60. 0.532 lies in [0.53, 0.54].\n3. Magnification 3: Zoom into interval [0.53, 0.54]. Divide into 10 equal parts of length 0.001: 0.530, 0.531, 0.532, 0.533, ..., 0.540.\n4. The 2nd mark to the right of 0.530 is exactly 0.532.",
                "finalAnswer": "0.532 is located at the 2nd division mark in the magnified interval [0.53, 0.54].",
                "unit": "number line coordinate",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q4 (ii): Locate the rational number 1.15 on the number line using the method of successive magnification.",
                "given": "Number 1.15.",
                "formula": "Successive subdivision: units -> tenths -> hundredths.",
                "substitution": "1 < 1.15 < 2.",
                "calculation": "1. 1.15 lies between integers 1 and 2.\n2. Divide [1, 2] into 10 equal parts: 1.15 lies between 1.1 and 1.2.\n3. Magnify interval [1.1, 1.2] and divide into 10 equal parts of width 0.01: 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, ..., 1.20.\n4. The 5th tick mark to the right of 1.10 is exactly 1.15.",
                "finalAnswer": "1.15 is located exactly at the midpoint of the magnified interval [1.1, 1.2].",
                "unit": "number line coordinate",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q9: Let a and b be two non-zero rational numbers such that a + 1/b = 0. Without assigning numerical values, determine whether ab is positive or negative. Justify your answer.",
                "given": "Non-zero rationals a, b with a + 1/b = 0.",
                "formula": "Isolate a: a = -1/b, then multiply by b.",
                "substitution": "a = -1/b => a * b = (-1/b) * b.",
                "calculation": "1. Given: a + 1/b = 0.\n2. Subtract 1/b from both sides: a = -1/b.\n3. Since b != 0, multiply both sides by b: a * b = -1.\n4. -1 is a negative number (-1 < 0).\n5. Therefore, the product ab is unconditionally negative, regardless of the choice of non-zero rational numbers a and b.",
                "finalAnswer": "ab is negative (ab = -1 < 0).",
                "unit": "algebraic proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q10: A rational number has a terminating decimal expansion whose last non-zero digit occurs in the 4th decimal place. Show that it can be written as p/10^4 where p is not divisible by 10. Is it necessary that the denominator in lowest form is divisible by 2^4 or 5^4? Give reasons.",
                "given": "A terminating decimal with last non-zero digit at 4th decimal place: x = 0.d1 d2 d3 d4 where d4 != 0.",
                "formula": "x = (d1*10^3 + d2*10^2 + d3*10 + d4) / 10^4 = p / 10^4.",
                "substitution": "p is an integer with units digit d4 != 0.",
                "calculation": "1. Part 1: Multiplying x by 10^4 gives 10^4 * x = p, where p is an integer. Because the 4th decimal digit d4 is non-zero, the units digit of p is d4 != 0. Since the units digit is not 0, p cannot be divisible by 10.\n2. Part 2: Divisibility of denominator in lowest form:\n   Write p / 10^4 = p / (2^4 * 5^4).\n   To simplify to lowest form, we cancel any common prime factors between p and the denominator.\n   Since p is not divisible by 10, p cannot be simultaneously divisible by both 2 and 5.\n   Case A: If p is divisible by 2^k (with k <= 4), then 5^4 remains untouched in the denominator. In lowest form, the denominator is (2^(4-k)) * 5^4, which is divisible by 5^4.\n   Case B: If p is divisible by 5^k, then 2^4 remains untouched in the denominator. In lowest form, the denominator is 2^4 * (5^(4-k)), which is divisible by 2^4.\n   Case C: If p is coprime to both 2 and 5, the denominator in lowest form is 2^4 * 5^4, which is divisible by both.\n3. Conclusion: In all possible cases, the denominator in lowest form MUST be divisible by either 2^4 or 5^4.",
                "finalAnswer": "Yes, it is necessary that the denominator in lowest form is divisible by 2^4 or 5^4 (or both), because cancelling common factors cannot eliminate both 2^4 and 5^4 simultaneously.",
                "unit": "number theory proof",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q13: Let a = 7/12 and b = 5/6. Express both in form k1/m and k2/m with k2 - k1 > 6. Write five distinct rationals between a and b. Explain why k2 - k1 > n + 1 is necessary to find n rational numbers.",
                "given": "a = 7/12, b = 5/6 = 10/12. Required: 5 rational numbers between them.",
                "formula": "To obtain k2 - k1 > 6, choose an appropriate common denominator m.",
                "substitution": "With m = 24: a = 14/24, b = 20/24 => k2 - k1 = 20 - 14 = 6 (not strictly > 6). With m = 36: a = 21/36, b = 30/36 => k2 - k1 = 30 - 21 = 9 > 6.",
                "calculation": "1. Let m = 36.\n   a = 7/12 = (7 * 3) / 36 = 21/36 => k1 = 21.\n   b = 5/6 = (5 * 6) / 36 = 30/36 => k2 = 30.\n2. Difference: k2 - k1 = 30 - 21 = 9 > 6, satisfying the given condition.\n3. Intermediate integers between 21 and 30 are: 22, 23, 24, 25, 26, 27, 28, 29.\n4. Five distinct rational numbers with denominator 36:\n   22/36 (= 11/18), 23/36, 24/36 (= 2/3), 25/36, 26/36 (= 13/18).\n5. Theoretical Explanation: Between two integers k1 and k2, the number of strictly intermediate integers is (k2 - k1 - 1). For at least n integers to exist, we must have:\n   k2 - k1 - 1 >= n  <=>  k2 - k1 >= n + 1.\n   If k2 - k1 = n + 1, there are exactly n integers. If k2 - k1 <= n, there are at most n - 1 integers, which is strictly insufficient. Thus, k2 - k1 > n is strictly necessary.",
                "finalAnswer": "Fractions: 22/36, 23/36, 2/3, 25/36, 13/36 (with m = 36). The condition k2 - k1 > n + 1 ensures at least n distinct integer numerators exist strictly between k1 and k2.",
                "unit": "density proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q14: Three rational numbers x, y, z satisfy x + y + z = 0 and xy + yz + zx = 0. Show that all the rational numbers x, y, z must be simultaneously zero.",
                "given": "x + y + z = 0 and xy + yz + zx = 0 for x, y, z in Q.",
                "formula": "Algebraic identity: (x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx).",
                "substitution": "Substitute x + y + z = 0 and xy + yz + zx = 0 into the identity.",
                "calculation": "1. (0)^2 = x^2 + y^2 + z^2 + 2(0).\n2. 0 = x^2 + y^2 + z^2.\n3. Since x, y, z are real (and rational) numbers, the square of any real number is non-negative:\n   x^2 >= 0, y^2 >= 0, z^2 >= 0.\n4. The sum of three non-negative real numbers can equal 0 if and only if each term is simultaneously equal to zero:\n   x^2 = 0, y^2 = 0, z^2 = 0.\n5. Therefore, x = 0, y = 0, and z = 0 simultaneously.",
                "finalAnswer": "x = y = z = 0 simultaneously (Proved via x^2 + y^2 + z^2 = (x+y+z)^2 - 2(xy+yz+zx) = 0).",
                "unit": "algebraic proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q15: Show that the rational number (a + b)/2 lies strictly between the rational numbers a and b (with a < b).",
                "given": "Rational numbers a and b with a < b.",
                "formula": "Midpoint m = (a + b) / 2.",
                "substitution": "Prove: (1) a < (a + b)/2 and (2) (a + b)/2 < b.",
                "calculation": "1. Proof of part (1):\n   Given a < b.\n   Add a to both sides of the inequality:\n   a + a < a + b => 2a < a + b.\n   Divide both sides by 2 (since 2 > 0, the inequality direction is preserved):\n   a < (a + b) / 2.\n2. Proof of part (2):\n   Given a < b.\n   Add b to both sides of the inequality:\n   a + b < b + b => a + b < 2b.\n   Divide both sides by 2:\n   (a + b) / 2 < b.\n3. Combining parts (1) and (2):\n   a < (a + b) / 2 < b.\n4. Furthermore, since a and b are rational numbers, their sum (a + b) is rational, and division by 2 yields a rational number.",
                "finalAnswer": "Proved: a < (a + b)/2 < b for all rational numbers a < b.",
                "unit": "algebraic inequality proof",
                "has_diagram": True
            }
        ]
    }
