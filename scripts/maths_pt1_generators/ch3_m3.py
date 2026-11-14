"""
Chapter 3: The World of Numbers - Module 3
Curriculum ID: 09ca99d2-0489-48f2-8d39-8b26ca7885c9
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_number_line_points_svg

def get_m3():
    m3_svg = build_number_line_points_svg(
        points=[
            {"val": -1.25, "label": "-5/4 (-1.25)", "color": "#DC2626"},
            {"val": 0, "label": "0", "color": "#0F172A"},
            {"val": 0.667, "label": "2/3", "color": "#2563EB"},
            {"val": 1.5, "label": "1 1/2 (1.5)", "color": "#16A34A"}
        ],
        domain=(-2.0, 2.5),
        title="Rational Numbers on the Continuous Number Line",
        caption="Simultaneous plotting of proper, improper, and negative fractions: -5/4, 0, 2/3, 1 1/2"
    )

    return {
        "order_index": 3,
        "title": "Textbook Exercise Solver 2: Number Line Representation, Density & Rational Applications (Exercise 3.4 & End-of-Chapter Set 1)",
        "description": "Exhaustive step-by-step solutions to in-text Examples 4 to 6, Exercise 3.4 (all questions), and End-of-Chapter Questions 5 to 8. Master plotting fractions on the number line, proving the infinite density of rational numbers between any two limits, and solving real-world partition problems.",
        "subtopics": [
            "Plotting proper, improper, and mixed fractions on the real number line",
            "The Density Theorem: Between any two rational numbers a < b, there exist infinitely many rational numbers",
            "Two core methods for finding in-between rationals: Arithmetic Mean (a+b)/2 and Denominator Scaling (k+1)",
            "Step-by-step silk measurement and kurta cutting word problems",
            "Linear algebraic rational equations: x/3 + x/5 = 16/15"
        ],
        "key_concepts": [
            "Rational Partition Principle: To plot p/q, divide each unit integer interval into q equal segments.",
            "Density Invariant: For any two distinct rationals a < b, the midpoint m = (a + b)/2 is strictly between them: a < (a+b)/2 < b.",
            "Equal Sub-interval Invariant: To find n rational numbers between p/q and r/s with common denominator D, multiply numerator and denominator by n + 1.",
            "Micro-Interval Density: Between 3.1415 and 3.1416 lie infinite rationals such as 3.14151, 3.14155, 3.14159.",
            "Algebraic Balance: Rational coefficients sum via LCM: x/3 + x/5 = (5x + 3x)/15 = 8x/15."
        ],
        "success_criteria": "Students can plot rational numbers accurately on a number line, generate any required number of intermediate rational fractions, and solve fraction word problems with rigorous steps.",
        "chapter_notes": "Module 3 establishes that the collection of rational numbers is dense on the line, leaving no gaping intervals yet still leaving infinitesimal holes for irrationals.",
        "common_misconceptions": [
            {"misconception": "Believing there is a 'next' rational number after 1/2", "clarification": "Unlike integers, rational numbers have no immediate successor; between 1/2 and any chosen number lies another rational."},
            {"misconception": "Thinking only finite numbers exist between 3.1415 and 3.1416", "clarification": "By appending additional decimal digits (e.g. 3.14151, 3.141501, ...), infinitely many rational numbers can be created."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Exercise 3.4 and End-of-Chapter rational density problems. Emphasize the two standard techniques: the midpoint method and the common denominator multiplier (n+1) method.",
        "visual_lesson_plan": {
            "title": "Visualizing Rational Density and Measurement",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Interactive number line showing fractions -5/4, 2/3, and 1 1/2, alongside a zoomed-in view of infinite density between 3 and 4.",
            "concept_visuals": [
                {
                    "concept_title": "Rational Number Line Coordinates: 2/3, -5/4, 1 1/2",
                    "diagram_title": "Plotting Points on Real Line",
                    "interactive_math_formula": "x \\in \\{-1.25, 0.667, 1.5\\}",
                    "mafs_graph_config": {
                        "domain": [-2, 2.5],
                        "range": [-1, 1],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Real Axis"}
                        ],
                        "points": [
                            {"x": -1.25, "y": 0, "label": "-5/4 (-1.25)"},
                            {"x": 0, "y": 0, "label": "0"},
                            {"x": 0.667, "y": 0, "label": "2/3"},
                            {"x": 1.5, "y": 0, "label": "1 1/2 (1.5)"}
                        ]
                    },
                    "image_query": "locating positive and negative fractions on number line",
                    "video_query": "how to plot fractions and mixed numbers on a number line",
                    "what_to_explain": "-5/4 lies 1.25 units to the left of 0, 2/3 lies between 0 and 1, and 1 1/2 lies midway between 1 and 2."
                },
                {
                    "concept_title": "Rational Density: In-betweening -1/2 and 1/4",
                    "diagram_title": "Density on [-0.5, 0.25]: -3/8, -1/4, -1/8, 0, 1/8",
                    "interactive_math_formula": "-0.5 < -0.25 < 0 < 0.25",
                    "mafs_graph_config": {
                        "domain": [-0.6, 0.35],
                        "range": [-1, 1],
                        "points": [
                            {"x": -0.5, "y": 0, "label": "-1/2 (-4/8)"},
                            {"x": -0.375, "y": 0, "label": "-3/8"},
                            {"x": -0.25, "y": 0, "label": "-1/4 (-2/8)"},
                            {"x": -0.125, "y": 0, "label": "-1/8"},
                            {"x": 0, "y": 0, "label": "0"},
                            {"x": 0.125, "y": 0, "label": "1/8"},
                            {"x": 0.25, "y": 0, "label": "1/4 (2/8)"}
                        ]
                    },
                    "image_query": "finding rational numbers between two fractions number line",
                    "video_query": "density property of rational numbers visual explanation",
                    "what_to_explain": "Dividing the segment between -4/8 and 2/8 reveals multiple intermediate rationals."
                },
                {
                    "concept_title": "Micro-Interval Zoom: Between 3.1415 and 3.1416",
                    "diagram_title": "Magnified Scale of Ten-Thousandths",
                    "interactive_math_formula": "3.1415 < 3.14155 < 3.1416",
                    "mafs_graph_config": {
                        "domain": [3.14148, 3.14162],
                        "range": [-1, 1],
                        "points": [
                            {"x": 3.14150, "y": 0, "label": "3.14150"},
                            {"x": 3.14152, "y": 0, "label": "3.14152"},
                            {"x": 3.14155, "y": 0, "label": "3.14155 (Midpoint)"},
                            {"x": 3.14158, "y": 0, "label": "3.14158"},
                            {"x": 3.14160, "y": 0, "label": "3.14160"}
                        ]
                    },
                    "image_query": "magnified number line between two decimal places rational density",
                    "video_query": "finding numbers between two close decimals",
                    "what_to_explain": "No matter how close two numbers appear, infinite rational subdivisions exist between them."
                },
                {
                    "concept_title": "Practical Silk Measurement Division",
                    "diagram_title": "15 3/4 m divided by 2 1/4 m = 7 Kurtas",
                    "interactive_math_formula": "\\frac{63}{4} \\div \\frac{9}{4} = \\frac{63}{9} = 7",
                    "mafs_graph_config": {
                        "domain": [0, 18],
                        "range": [-1, 2],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Fabric Length (m)"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "0 m"},
                            {"x": 2.25, "y": 0, "label": "1 Kurta (2.25m)"},
                            {"x": 4.5, "y": 0, "label": "2 Kurtas"},
                            {"x": 9.0, "y": 0, "label": "4 Kurtas"},
                            {"x": 15.75, "y": 0, "label": "7 Kurtas (15.75m)"}
                        ]
                    },
                    "image_query": "fraction division cloth cutting word problem visual length",
                    "video_query": "dividing fractions word problem fabric measurement",
                    "what_to_explain": "Each kurta takes 9/4 m; 63/4 m of silk partitions into exactly 7 identical kurtas."
                },
                {
                    "concept_title": "Algebraic Balance: x/3 + x/5 = 16/15",
                    "diagram_title": "Summing Linear Rate Functions: 8x/15 = 16/15 -> x = 2",
                    "interactive_math_formula": "\\frac{8}{15}x = \\frac{16}{15} \\implies x = 2",
                    "mafs_graph_config": {
                        "domain": [0, 4],
                        "range": [0, 2],
                        "curves": [
                            {"fn": "(8/15)*x", "color": "#2563EB", "label": "y = (8/15)x"},
                            {"fn": "16/15", "color": "#DC2626", "label": "y = 16/15"}
                        ],
                        "points": [
                            {"x": 2, "y": 1.067, "label": "Solution (2, 16/15)"}
                        ]
                    },
                    "image_query": "solving linear equation with fractions graphical intersection",
                    "video_query": "solving linear equations with fractions step by step",
                    "what_to_explain": "The line y = 8x/15 intersects the horizontal line y = 16/15 at exactly x = 2."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Rational Number Density",
                    "questions": [
                        {
                            "question": "Can you ever find two distinct rational numbers with no rational number between them?",
                            "type": "short_answer",
                            "ideal_answer": "No, because the arithmetic mean (a + b)/2 is always a distinct rational number strictly between any two distinct rational numbers a and b.",
                            "socratic_hint": "Consider the midpoint of any segment connecting two distinct points."
                        },
                        {
                            "question": "To find 5 rational numbers between 3 and 4 using the denominator scaling method, what multiplier should you choose?",
                            "type": "short_answer",
                            "ideal_answer": "Multiply numerator and denominator by n + 1 = 5 + 1 = 6 (writing 3 = 18/6 and 4 = 24/6).",
                            "socratic_hint": "How many equal divisions do you need to create 5 intermediate points?"
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Textbook Example 4: Find a rational number between 1/3 and 1/2.",
                "given": "Fractions 1/3 and 1/2.",
                "formula": "Midpoint method: m = (a + b) / 2.",
                "substitution": "m = (1/3 + 1/2) / 2.",
                "calculation": "1. Common denominator for 1/3 + 1/2: LCM(3, 2) = 6.\n2. 1/3 = 2/6; 1/2 = 3/6.\n3. Sum = (2 + 3) / 6 = 5/6.\n4. Midpoint = (5/6) / 2 = 5/12.\n5. Verify: 1/3 = 4/12 < 5/12 < 6/12 = 1/2.",
                "finalAnswer": "5/12",
                "unit": "rational number",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.4 Q1: Represent the rational numbers 2/3, -5/4, and 1 1/2 on a single number line.",
                "given": "Numbers: 2/3, -5/4 = -1.25, 1 1/2 = 3/2 = 1.5.",
                "formula": "Draw a number line with integers -2, -1, 0, 1, 2. Partition units into subdivisions matching denominators.",
                "substitution": "2/3 is in [0, 1] divided into 3 parts; -5/4 is in [-2, -1] divided into 4 parts; 3/2 is midway between 1 and 2.",
                "calculation": "1. Mark 0 as reference origin.\n2. Divide segment between 0 and 1 into 3 equal parts; the 2nd tick is 2/3.\n3. Divide segment between -1 and -2 into 4 equal parts; count 1 part left of -1 (since -5/4 = -1 - 1/4) to locate -5/4.\n4. Divide segment between 1 and 2 into 2 equal parts; the midpoint is 1 1/2 = 3/2.",
                "finalAnswer": "All three points are marked on the number line: -5/4 at -1.25, 2/3 at ~0.67, and 1 1/2 at 1.5.",
                "unit": "number line representation",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.4 Q2: Find three distinct rational numbers that lie strictly between -1/2 and 1/4.",
                "given": "-1/2 and 1/4.",
                "formula": "Express with common denominator and scale: LCM(2, 4) = 4.",
                "substitution": "-1/2 = -2/4 = -4/8; 1/4 = 1/4 = 2/8.",
                "calculation": "1. Write -1/2 as -4/8 and 1/4 as 2/8.\n2. Integers strictly between -4 and 2 are: -3, -2, -1, 0, 1.\n3. Corresponding rational numbers with denominator 8:\n   -3/8, -2/8 = -1/4, -1/8, 0/8 = 0, 1/8.\n4. Any three of these lie strictly between -1/2 and 1/4: for example, -1/4, 0, and 1/8.",
                "finalAnswer": "-1/4, 0, and 1/8 (or -3/8, -1/8, 1/8)",
                "unit": "rational numbers",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.4 Q3: Simplify the expression: (-1/4) + (5/12).",
                "given": "(-1/4) + (5/12).",
                "formula": "LCM(4, 12) = 12.",
                "substitution": "Scale -1/4 = (-1 * 3) / 12 = -3/12.",
                "calculation": "1. -3/12 + 5/12 = (-3 + 5) / 12.\n2. 2/12 = 1/6.",
                "finalAnswer": "1/6",
                "unit": "simplified fraction",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.4 Q4: A tailor has 15 3/4 metres of fine silk. If making one kurta requires 2 1/4 metres of silk, exactly how many kurtas can he make?",
                "given": "Total silk = 15 3/4 metres = 63/4 m. Silk per kurta = 2 1/4 metres = 9/4 m.",
                "formula": "Number of kurtas = Total silk / Silk per kurta.",
                "substitution": "(63/4) / (9/4).",
                "calculation": "1. Convert mixed fractions to improper fractions:\n   15 3/4 = (15 * 4 + 3) / 4 = 63/4.\n   2 1/4 = (2 * 4 + 1) / 4 = 9/4.\n2. Divide: (63/4) / (9/4) = (63/4) * (4/9).\n3. Cancel 4: 63 / 9 = 7 kurtas exactly.",
                "finalAnswer": "7 kurtas",
                "unit": "kurtas",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.4 Q5: Find three rational numbers between 3.1415 and 3.1416.",
                "given": "Two rational numbers: 3.1415 and 3.1416.",
                "formula": "Append decimal digits: 3.1415 = 3.14150 and 3.1416 = 3.14160.",
                "substitution": "Select intermediate values between 3.14150 and 3.14160.",
                "calculation": "1. 3.14150 < 3.14152 < 3.14155 < 3.14158 < 3.14160.\n2. As fractions: 3.14152 = 314152/100000 = 78538/25000.\n3. 3.14155 = 314155/100000 = 62831/20000.\n4. 3.14158 = 314158/100000 = 157079/50000.",
                "finalAnswer": "3.14152, 3.14155, and 3.14158",
                "unit": "rational numbers",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.4 Q6: Can you think of other way(s) to find a rational number between any two rational numbers?",
                "given": "Two distinct rational numbers a and b with a < b.",
                "formula": "Method 1: Arithmetic Mean m = (a + b)/2. Method 2: Weighted average (m*a + n*b)/(m + n). Method 3: Equal denominator scaling.",
                "substitution": "Demonstrate with general rational forms a = p/q, b = r/s.",
                "calculation": "1. Method 1 (Mean): The midpoint (a + b)/2 is strictly between a and b because a < (a+b)/2 < b. Repeating this produces infinite nested rationals.\n2. Method 2 (Common Denominator Scaling): Write with common denominator D: a = P/D and b = Q/D. Multiply numerator and denominator by (k + 1) to create k intermediate integer numerators.\n3. Method 3 (Mediant): If a = p/q and b = r/s with positive denominators, the mediant (p + r)/(q + s) strictly lies between p/q and r/s.",
                "finalAnswer": "Three general methods exist: (1) Arithmetic Mean (a+b)/2, (2) Common Denominator Scaling by (n+1), and (3) The Mediant property (p+r)/(q+s).",
                "unit": "mathematical methods",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q5: Find 6 rational numbers between 3 and 4.",
                "given": "Numbers 3 and 4. Required: 6 rational numbers.",
                "formula": "To find n = 6 numbers, multiply by n + 1 = 7.",
                "substitution": "3 = (3 * 7) / 7 = 21/7. 4 = (4 * 7) / 7 = 28/7.",
                "calculation": "1. Write 3 as 21/7 and 4 as 28/7.\n2. The 6 consecutive integer numerators between 21 and 28 are 22, 23, 24, 25, 26, 27.\n3. The 6 rational numbers are: 22/7, 23/7, 24/7, 25/7, 26/7, 27/7.",
                "finalAnswer": "22/7, 23/7, 24/7, 25/7, 26/7, 27/7",
                "unit": "rational numbers",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q6: Find 5 rational numbers between 2/5 and 3/5.",
                "given": "Fractions 2/5 and 3/5. Required: 5 rational numbers.",
                "formula": "Multiply numerator and denominator by n + 1 = 5 + 1 = 6.",
                "substitution": "2/5 = (2 * 6) / (5 * 6) = 12/30. 3/5 = (3 * 6) / (5 * 6) = 18/30.",
                "calculation": "1. Numerators strictly between 12 and 18 are 13, 14, 15, 16, 17.\n2. Thus, the 5 rational numbers are: 13/30, 14/30 (= 7/15), 15/30 (= 1/2), 16/30 (= 8/15), 17/30.",
                "finalAnswer": "13/30, 7/15, 1/2, 8/15, 17/30",
                "unit": "rational numbers",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q7: Find 5 rational numbers between 1/6 and 2/5.",
                "given": "Fractions 1/6 and 2/5. Required: 5 rational numbers.",
                "formula": "LCM(6, 5) = 30. Convert to common denominator, then scale if necessary.",
                "substitution": "1/6 = 5/30; 2/5 = 12/30.",
                "calculation": "1. 1/6 = 5/30 and 2/5 = 12/30.\n2. Numerators strictly between 5 and 12 are 6, 7, 8, 9, 10, 11 (6 available numbers, more than enough!).\n3. Select any 5: 6/30 (= 1/5), 7/30, 8/30 (= 4/15), 9/30 (= 3/10), 10/30 (= 1/3).",
                "finalAnswer": "1/5, 7/30, 4/15, 3/10, 1/3",
                "unit": "rational numbers",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q8: If x/3 + x/5 = 16/15, find the rational number x.",
                "given": "Equation: x/3 + x/5 = 16/15.",
                "formula": "Combine fractions on LHS using LCM(3, 5) = 15.",
                "substitution": "(5x + 3x) / 15 = 16/15.",
                "calculation": "1. (5x + 3x) / 15 = 8x / 15.\n2. Equation becomes: 8x / 15 = 16/15.\n3. Multiply both sides by 15: 8x = 16.\n4. Divide by 8: x = 16 / 8 = 2.\n5. Verification: 2/3 + 2/5 = 10/15 + 6/15 = 16/15. Correct!",
                "finalAnswer": "2",
                "unit": "rational number",
                "has_diagram": True
            }
        ]
    }
