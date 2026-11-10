"""
Chapter 3: The World of Numbers - Module 4
Curriculum ID: 09ca99d2-0489-48f2-8d39-8b26ca7885c9
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_number_line_spiral_svg

def get_m4():
    m4_svg = build_number_line_spiral_svg(
        title="Theodorus Square Root Spiral: Geometric Construction of Surds",
        caption="Successive right triangles with unit perpendiculars yielding hypotenuses sqrt(2), sqrt(3), ..., sqrt(10)"
    )

    return {
        "order_index": 4,
        "title": "Textbook Exercise Solver 3: Irrational Numbers, Baudhayana Sutra, Root Spirals & Proof of Sqrt(5) (Exercise 3.5 Part 1 & End-of-Chapter Set 2)",
        "description": "Comprehensive step-by-step solutions to in-text Examples 7 & 8, Exercise 3.5 Q3 (all 6 parts), End-of-Chapter Q2 (rigorous proof of irrationality of sqrt(5)), and End-of-Chapter Q16 (Theodorus square root spiral). Master compass-and-straightedge geometric construction and classification.",
        "subtopics": [
            "Historical origins of surds: Baudhayana Sulbasutra (800 BCE) fire altar rope geometry",
            "Rigorous algebraic proof by contradiction: Irrationality of sqrt(2) and sqrt(5)",
            "Step-by-step compass construction of sqrt(2), sqrt(3), and sqrt(5) on the number line",
            "Classification of real numbers into rational fractions vs infinite non-periodic irrationals",
            "The Theodorus Square Root Spiral: Pythagorean chain of hypotenuses sqrt(2) to sqrt(17)"
        ],
        "key_concepts": [
            "Irrational Number Definition: A real number that cannot be expressed as p/q for any integers p, q (q != 0).",
            "Baudhayana Sulbasutra Surd Identity: sqrt(2) approx 1 + 1/3 + 1/(3*4) - 1/(3*4*34) = 577/408 approx 1.4142156.",
            "Fundamental Lemma of Primes: If a prime p divides a^2, then p must divide a.",
            "Pythagorean Hypotenuse Chain: In a right triangle with legs sqrt(n) and 1, the hypotenuse is sqrt((sqrt(n))^2 + 1^2) = sqrt(n + 1).",
            "Aperiodic Decimal Invariant: Infinite non-terminating and non-repeating decimals represent irrational numbers."
        ],
        "success_criteria": "Students can prove irrationality by contradiction, construct surds geometrically on the number line, classify decimal patterns, and compute square root spiral hypotenuses.",
        "chapter_notes": "Module 4 bridges rational arithmetic to the complete real continuum by proving that geometric lengths like diagonals of unit squares cannot be expressed as integer fractions.",
        "common_misconceptions": [
            {"misconception": "Believing 22/7 is the exact value of pi", "clarification": "Pi (3.14159...) is strictly irrational; 22/7 is merely a convenient rational approximation."},
            {"misconception": "Assuming all non-terminating decimals are irrational", "clarification": "Non-terminating repeating decimals (e.g. 0.333... = 1/3) are strictly rational; only non-terminating non-repeating decimals are irrational."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through irrational numbers. State Baudhayana's rule and provide the exact classical proof by contradiction for the irrationality of sqrt(5).",
        "visual_lesson_plan": {
            "title": "Constructing Irrational Numbers Geometrically",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Vector SVG diagram of the Theodorus square root spiral constructing hypotenuses sqrt(2) through sqrt(10).",
            "concept_visuals": [
                {
                    "concept_title": "Baudhayana Right Triangle: Unit Square Diagonal Sqrt(2)",
                    "diagram_title": "1^2 + 1^2 = (sqrt(2))^2",
                    "interactive_math_formula": "c = \\sqrt{1^2 + 1^2} = \\sqrt{2} \\approx 1.414",
                    "mafs_graph_config": {
                        "domain": [-0.5, 2],
                        "range": [-0.5, 2],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 1, "y": 0, "label": "A(1, 0)"},
                            {"x": 1, "y": 1, "label": "B(1, 1)"},
                            {"x": 1.414, "y": 0, "label": "P(sqrt(2), 0)"}
                        ]
                    },
                    "image_query": "square root 2 geometric construction unit square diagonal number line",
                    "video_query": "how to represent root 2 on number line using compass",
                    "what_to_explain": "Rotating the diagonal of length sqrt(2) with a compass down onto the number line locates the precise point sqrt(2) approx 1.414."
                },
                {
                    "concept_title": "Theodorus Square Root Spiral",
                    "diagram_title": "Iterated Hypotenuses sqrt(2), sqrt(3), ..., sqrt(17)",
                    "interactive_math_formula": "H_{n+1} = \\sqrt{H_n^2 + 1^2} = \\sqrt{n+1}",
                    "mafs_graph_config": {
                        "domain": [-3, 3],
                        "range": [-3, 3],
                        "points": [
                            {"x": 0, "y": 0, "label": "Center O"},
                            {"x": 1, "y": 0, "label": "1"},
                            {"x": 1, "y": 1, "label": "sqrt(2)"},
                            {"x": 0.585, "y": 1.63, "label": "sqrt(3)"},
                            {"x": 0, "y": 2, "label": "sqrt(4)=2"}
                        ]
                    },
                    "image_query": "square root spiral of Theodorus geometry diagram",
                    "video_query": "spiral of theodorus construction step by step",
                    "what_to_explain": "Each new triangle attaches a perpendicular leg of length 1 to the previous hypotenuse, systematically generating the square roots of all positive integers."
                },
                {
                    "concept_title": "Proof by Contradiction: Parity Conflict of Sqrt(5)",
                    "diagram_title": "a^2 = 5b^2 Divisibility Cascade",
                    "interactive_math_formula": "a = 5k \\implies 25k^2 = 5b^2 \\implies b^2 = 5k^2",
                    "mafs_graph_config": {
                        "domain": [0, 6],
                        "range": [0, 30],
                        "curves": [
                            {"fn": "5*x", "color": "#2563EB", "label": "Multiples of 5"}
                        ],
                        "points": [
                            {"x": 1, "y": 5, "label": "5 divides a"},
                            {"x": 2, "y": 10, "label": "5 divides b"},
                            {"x": 0, "y": 0, "label": "Contradiction: Common Factor 5"}
                        ]
                    },
                    "image_query": "proof by contradiction irrationality of root 5 algebra steps",
                    "video_query": "prove that root 5 is irrational step by step proof",
                    "what_to_explain": "Assuming a and b have no common factors leads to the impossible result that both a and b are divisible by 5."
                },
                {
                    "concept_title": "Classification: Periodic vs Aperiodic Decimals",
                    "diagram_title": "Periodic Rational (0.333...) vs Non-Periodic Irrational (1.010010001...)",
                    "interactive_math_formula": "1.01001000100001... \\notin \\mathbb{Q}",
                    "mafs_graph_config": {
                        "domain": [0, 2],
                        "range": [-1, 1],
                        "points": [
                            {"x": 0.333, "y": 0, "label": "1/3 = 0.333... (Rational)"},
                            {"x": 1.01, "y": 0, "label": "1.01001... (Irrational)"},
                            {"x": 1.414, "y": 0, "label": "sqrt(2) (Irrational)"}
                        ]
                    },
                    "image_query": "rational vs irrational decimal expansions number line comparison",
                    "video_query": "difference between rational and irrational decimals explained",
                    "what_to_explain": "A decimal pattern with an expanding gap between 1s never repeats a fixed block, making it definitively irrational."
                },
                {
                    "concept_title": "Construction of Sqrt(5) on Number Line",
                    "diagram_title": "Right Triangle with Legs 2 and 1: 2^2 + 1^2 = 5",
                    "interactive_math_formula": "c = \\sqrt{2^2 + 1^2} = \\sqrt{5} \\approx 2.236",
                    "mafs_graph_config": {
                        "domain": [0, 3],
                        "range": [-0.5, 1.5],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 2, "y": 0, "label": "A(2, 0)"},
                            {"x": 2, "y": 1, "label": "B(2, 1)"},
                            {"x": 2.236, "y": 0, "label": "P(sqrt(5), 0)"}
                        ]
                    },
                    "image_query": "how to locate root 5 on number line with base 2 and perpendicular 1",
                    "video_query": "locate root 5 on number line class 9 maths",
                    "what_to_explain": "Construct base OA = 2 units, perpendicular AB = 1 unit; hypotenuse OB = sqrt(2^2 + 1^2) = sqrt(5). Rotate arc to number line at 2.236."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Irrationality Proof Mechanism",
                    "questions": [
                        {
                            "question": "What is the key contradiction reached when proving sqrt(5) is irrational by assuming sqrt(5) = a/b in lowest terms?",
                            "type": "short_answer",
                            "ideal_answer": "It is proved that 5 divides both a and b, contradicting the initial assumption that a and b are coprime (share no common factors other than 1).",
                            "socratic_hint": "If a^2 = 5b^2, what does that tell you about the prime factor 5 in both a and b?"
                        },
                        {
                            "question": "Why is 1.01001000100001... irrational even though it shows a clear pattern?",
                            "type": "short_answer",
                            "ideal_answer": "Because the pattern is not periodic (it does not repeat a fixed finite block of digits indefinitely); the number of zeros increases each time.",
                            "socratic_hint": "Does it repeat a fixed block like '01' forever, or does the block change length?"
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Textbook Example 7: Prove that sqrt(2) is an irrational number using the method of contradiction.",
                "given": "Number sqrt(2).",
                "formula": "Proof by contradiction: Assume sqrt(2) = a/b where a, b in Z, b != 0, and gcd(a, b) = 1.",
                "substitution": "Square both sides: 2 = a^2 / b^2 => a^2 = 2b^2.",
                "calculation": "1. a^2 = 2b^2 implies that a^2 is an even integer.\n2. By prime divisor theorem, if a^2 is even, then a must be an even integer.\n3. Let a = 2k for some integer k.\n4. Substitute a = 2k into a^2 = 2b^2: (2k)^2 = 2b^2 => 4k^2 = 2b^2 => b^2 = 2k^2.\n5. b^2 = 2k^2 implies that b^2 is even, which means b must also be even.\n6. Since both a and b are even, they share a common factor of 2. This directly contradicts the assumption that gcd(a, b) = 1.\n7. Therefore, our assumption that sqrt(2) is rational is false.",
                "finalAnswer": "sqrt(2) is an irrational number (Proved by contradiction).",
                "unit": "mathematical proof",
                "has_diagram": True
            },
            {
                "problem": "Textbook Example 8: Construct the point representing sqrt(3) on the real number line using compass and straightedge.",
                "given": "Unit length on number line.",
                "formula": "Pythagoras theorem: (sqrt(2))^2 + 1^2 = 2 + 1 = 3 => Hypotenuse = sqrt(3).",
                "substitution": "Base = sqrt(2), Height = 1.",
                "calculation": "1. Construct sqrt(2) on the number line: OA = 1, perpendicular AB = 1, giving OB = sqrt(2). Project arc to point D on number line such that OD = sqrt(2).\n2. At point D (coordinate sqrt(2)), erect a perpendicular DE of unit length 1.\n3. Join OE: in right triangle ODE, OE^2 = OD^2 + DE^2 = (sqrt(2))^2 + 1^2 = 2 + 1 = 3.\n4. OE = sqrt(3) approx 1.732.\n5. With O as center and radius OE, draw an arc intersecting the number line at point P.\n6. Point P represents sqrt(3) on the number line.",
                "finalAnswer": "Point P at coordinate approx 1.732 on the number line represents sqrt(3).",
                "unit": "geometric construction",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.5 Q3 (i): Classify sqrt(81) as rational or irrational, and find its explicit fraction.",
                "given": "Number sqrt(81).",
                "formula": "sqrt(81) = 9.",
                "substitution": "9 = 9/1.",
                "calculation": "1. 9^2 = 81, so sqrt(81) = 9.\n2. 9 is an integer and can be written as 9/1, which is of the form p/q with integers p = 9, q = 1 != 0.",
                "finalAnswer": "Rational (explicit fraction: 9/1)",
                "unit": "classification",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.5 Q3 (ii): Classify sqrt(12) as rational or irrational.",
                "given": "Number sqrt(12).",
                "formula": "sqrt(12) = sqrt(4 * 3) = 2*sqrt(3).",
                "substitution": "2 is rational, sqrt(3) is irrational.",
                "calculation": "1. 12 is not a perfect square (3^2 = 9 < 12 < 4^2 = 16).\n2. sqrt(12) = 2*sqrt(3).\n3. Product of a non-zero rational number and an irrational number is always irrational.",
                "finalAnswer": "Irrational",
                "unit": "classification",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.5 Q3 (iii): Classify 0.33333... as rational or irrational, and find its explicit fraction.",
                "given": "Decimal 0.33333... (recurring).",
                "formula": "Let x = 0.333... Multiply by 10: 10x = 3.333...",
                "substitution": "Subtract x: 10x - x = 3.333... - 0.333...",
                "calculation": "1. 9x = 3.\n2. x = 3/9 = 1/3.\n3. Since 1/3 is a ratio of integers p = 1 and q = 3, it is rational.",
                "finalAnswer": "Rational (explicit fraction: 1/3)",
                "unit": "classification",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.5 Q3 (iv): Classify 0.123451234512345... as rational or irrational, and find its explicit fraction.",
                "given": "Decimal 0.1234512345... with repeating block '12345' of length 5.",
                "formula": "Let x = 0.12345... Multiply by 10^5 = 100000: 100000x = 12345.12345...",
                "substitution": "Subtract x: 99999x = 12345.",
                "calculation": "1. x = 12345 / 99999.\n2. Divide numerator and denominator by 3: 12345 / 3 = 4115, 99999 / 3 = 33333.\n3. x = 4115 / 33333.",
                "finalAnswer": "Rational (explicit fraction: 4115/33333)",
                "unit": "classification",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.5 Q3 (v): Classify 1.01001000100001... as rational or irrational.",
                "given": "Decimal: 1.01001000100001...",
                "formula": "A decimal is rational if and only if it terminates or eventually repeats a periodic fixed block of digits.",
                "substitution": "Examine the number of zeros between successive 1s: 1 zero, then 2 zeros, then 3 zeros, then 4 zeros, etc.",
                "calculation": "1. The gap between consecutive digits 1 increases strictly by 1 zero each time (1, 2, 3, 4, 5, ...).\n2. There is no fixed block of digits that repeats periodically.\n3. Because it is non-terminating and non-repeating (aperiodic), it cannot be expressed in the form p/q.",
                "finalAnswer": "Irrational (non-terminating and non-repeating pattern)",
                "unit": "classification",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.5 Q3 (vi): Classify 23.560185612239874790120 as rational or irrational.",
                "given": "Decimal: 23.560185612239874790120 (terminating decimal with finite digits).",
                "formula": "Every terminating decimal with n decimal places can be written as N / 10^n.",
                "substitution": "Count decimal places: 21 digits after decimal.",
                "calculation": "1. Since the decimal terminates after 21 digits, it has an exact integer numerator over 10^21.\n2. Rational form: 23560185612239874790120 / 10^21.\n3. Simplifying by dividing numerator and denominator by 10: 2356018561223987479012 / 10^20.",
                "finalAnswer": "Rational (terminating decimal: 2356018561223987479012 / 10^20)",
                "unit": "classification",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2: Prove that sqrt(5) is an irrational number.",
                "given": "Number sqrt(5).",
                "formula": "Assume to the contrary that sqrt(5) is rational: sqrt(5) = a/b with coprime integers a, b (b != 0, gcd(a, b) = 1).",
                "substitution": "5 = a^2 / b^2 => a^2 = 5b^2.",
                "calculation": "1. a^2 = 5b^2 implies that 5 divides a^2.\n2. Since 5 is a prime number, by Euclid's lemma, 5 must divide a.\n3. Therefore, we can write a = 5k for some integer k.\n4. Substitute a = 5k into a^2 = 5b^2: (5k)^2 = 5b^2 => 25k^2 = 5b^2 => b^2 = 5k^2.\n5. b^2 = 5k^2 implies that 5 divides b^2, which in turn means 5 must divide b.\n6. Since 5 divides both a and 5 divides b, a and b have at least 5 as a common factor.\n7. This contradicts our premise that gcd(a, b) = 1.\n8. Hence, our assumption is false, and sqrt(5) is an irrational number.",
                "finalAnswer": "sqrt(5) is an irrational number (Proved by contradiction).",
                "unit": "mathematical proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q16: Find the lengths of the hypotenuses of all the right triangles in the square root spiral (Fig. 3.14).",
                "given": "Theodorus spiral starting with right triangle T1 of legs 1 and 1, each subsequent triangle having legs equal to the previous hypotenuse and 1.",
                "formula": "H_1 = sqrt(1^2 + 1^2) = sqrt(2); H_{n} = sqrt(H_{n-1}^2 + 1^2) = sqrt((sqrt(n))^2 + 1) = sqrt(n + 1).",
                "substitution": "Compute hypotenuses sequentially for n = 1 to 16.",
                "calculation": "1. Triangle 1: H1 = sqrt(1^2 + 1^2) = sqrt(2).\n2. Triangle 2: H2 = sqrt((sqrt(2))^2 + 1^2) = sqrt(2 + 1) = sqrt(3).\n3. Triangle 3: H3 = sqrt((sqrt(3))^2 + 1^2) = sqrt(3 + 1) = sqrt(4) = 2.\n4. Triangle 4: H4 = sqrt(4 + 1) = sqrt(5).\n5. Triangle 5: H5 = sqrt(5 + 1) = sqrt(6).\n6. Triangle 6: H6 = sqrt(6 + 1) = sqrt(7).\n7. Triangle 7: H7 = sqrt(7 + 1) = sqrt(8) = 2*sqrt(2).\n8. Triangle 8: H8 = sqrt(8 + 1) = sqrt(9) = 3.\n9. Continuing up to Triangle 16: hypotenuses are sqrt(10), sqrt(11), sqrt(12), sqrt(13), sqrt(14), sqrt(15), sqrt(16) = 4, sqrt(17).",
                "finalAnswer": "The successive hypotenuses are sqrt(2), sqrt(3), 2, sqrt(5), sqrt(6), sqrt(7), sqrt(8), 3, sqrt(10), sqrt(11), sqrt(12), sqrt(13), sqrt(14), sqrt(15), 4, sqrt(17).",
                "unit": "surd lengths",
                "has_diagram": True
            }
        ]
    }
