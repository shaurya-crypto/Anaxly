"""
Chapter 2: Introduction to Linear Polynomials - Module 3
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m3():
    m3_svg = build_cartesian_svg(
        domain=(-2, 6), range_y=(-5, 15),
        points=[
            {"x": 0, "y": -3, "label": "P(0) = -3", "color": "#16A34A", "sub": "(0, -3)"},
            {"x": -1, "y": -8, "label": "P(-1) = -8", "color": "#DC2626", "sub": "(-1, -8)"},
            {"x": 2, "y": 7, "label": "P(2) = 7", "color": "#2563EB", "sub": "(2, 7)"},
        ],
        lines=[
            {"p1": (-1.5, -10.5), "p2": (3, 12), "color": "#2563EB", "stroke_width": 2.5, "label": "P(x) = 5x - 3"}
        ],
        title="Polynomial Evaluations: P(x) = 5x - 3",
        caption="Evaluating polynomial values at x = 0, -1, and 2 directly on the Cartesian locus"
    )

    return {
        "order_index": 3,
        "title": "Textbook Exercise Solver 1: Evaluation of Polynomials & Word Problems (Exercise 2.2 Complete)",
        "description": "Exhaustive step-by-step solutions to 100% of Exercise 2.2 questions. Evaluate linear and quadratic polynomials at positive, negative, and zero inputs, and solve real-world word problems involving ages, ratios, and coin denominations.",
        "subtopics": [
            "Evaluating polynomial P(x) at specific real values x = c",
            "Linear evaluation: 5x - 3 at x = 0, -1, and 2",
            "Quadratic evaluation: 7s^2 - 4s + 6 at s = 0, -3, and 4",
            "Translating word problems into linear algebraic equations",
            "Salil and his mother's age relationship problem",
            "Integer ratio and difference problems: 2:5 ratio with difference 63",
            "Multi-coin denomination problem: Ruby's 2-rupee and 5-rupee coins totaling Rs 77",
            "Complete step-by-step solutions to Exercise 2.2 Q1, Q2, Q3, Q4, and Q5"
        ],
        "key_concepts": [
            "Value of a Polynomial: The numerical value obtained by substituting x = k into P(x), denoted by P(k).",
            "Linear Equation Formulation: Translating verbal conditions into the algebraic form ax + b = c.",
            "Ratio Multiplier Principle: If two quantities are in ratio p:q, they can be represented as px and qx for some non-zero multiplier x.",
            "Value of Denominations: Total Money = Sum of (Coin Value * Number of Coins)."
        ],
        "success_criteria": "Student can evaluate any polynomial at given inputs and formulate and solve linear word problems with complete step-by-step calculations.",
        "chapter_notes": "Pay special attention to negative inputs in quadratic terms: (-3)^2 = +9, so 7(-3)^2 = 7 * 9 = 63.",
        "worked_examples": [
            {
                "problem": "Exercise 2.2 Q1 (i): Find the value of the linear polynomial P(x) = 5x - 3 if x = 0.",
                "given": "Polynomial P(x) = 5x - 3, input x = 0.",
                "formula": "Substitute x = 0 into P(x).",
                "substitution": "P(0) = 5(0) - 3.",
                "calculation": "Step 1: Multiply: 5 * 0 = 0.\nStep 2: Subtract 3: 0 - 3 = -3.",
                "finalAnswer": "P(0) = -3",
                "unit": "integer",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m3_svg
            },
            {
                "problem": "Exercise 2.2 Q1 (ii): Find the value of the linear polynomial P(x) = 5x - 3 if x = -1.",
                "given": "Polynomial P(x) = 5x - 3, input x = -1.",
                "formula": "Substitute x = -1 into P(x).",
                "substitution": "P(-1) = 5(-1) - 3.",
                "calculation": "Step 1: Multiply: 5 * (-1) = -5.\nStep 2: Subtract 3: -5 - 3 = -8.",
                "finalAnswer": "P(-1) = -8",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q1 (iii): Find the value of the linear polynomial P(x) = 5x - 3 if x = 2.",
                "given": "Polynomial P(x) = 5x - 3, input x = 2.",
                "formula": "Substitute x = 2 into P(x).",
                "substitution": "P(2) = 5(2) - 3.",
                "calculation": "Step 1: Multiply: 5 * 2 = 10.\nStep 2: Subtract 3: 10 - 3 = 7.",
                "finalAnswer": "P(2) = 7",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q2 (i): Find the value of the quadratic polynomial Q(s) = 7s^2 - 4s + 6 if s = 0.",
                "given": "Polynomial Q(s) = 7s^2 - 4s + 6, input s = 0.",
                "formula": "Substitute s = 0 into Q(s).",
                "substitution": "Q(0) = 7(0)^2 - 4(0) + 6.",
                "calculation": "Step 1: 7 * 0 = 0; 4 * 0 = 0.\nStep 2: Q(0) = 0 - 0 + 6 = 6.",
                "finalAnswer": "Q(0) = 6",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q2 (ii): Find the value of the quadratic polynomial Q(s) = 7s^2 - 4s + 6 if s = -3.",
                "given": "Polynomial Q(s) = 7s^2 - 4s + 6, input s = -3.",
                "formula": "Substitute s = -3 into Q(s).",
                "substitution": "Q(-3) = 7(-3)^2 - 4(-3) + 6.",
                "calculation": "Step 1: Compute (-3)^2 = +9.\nStep 2: 7 * 9 = 63.\nStep 3: -4 * (-3) = +12.\nStep 4: Sum all terms: 63 + 12 + 6 = 81.",
                "finalAnswer": "Q(-3) = 81",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q2 (iii): Find the value of the quadratic polynomial Q(s) = 7s^2 - 4s + 6 if s = 4.",
                "given": "Polynomial Q(s) = 7s^2 - 4s + 6, input s = 4.",
                "formula": "Substitute s = 4 into Q(s).",
                "substitution": "Q(4) = 7(4)^2 - 4(4) + 6.",
                "calculation": "Step 1: Compute 4^2 = 16.\nStep 2: 7 * 16 = 112.\nStep 3: -4 * 4 = -16.\nStep 4: Combine: 112 - 16 + 6 = 96 + 6 = 102.",
                "finalAnswer": "Q(4) = 102",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q3: The present age of Salil's mother is three times Salil's present age. After 5 years, their ages will add up to 70 years. Find their present ages.",
                "given": "Let Salil's present age = x years. Mother's present age = 3x years. In 5 years, sum of ages = 70.",
                "formula": "Salil's age in 5 yrs: (x + 5); Mother's age in 5 yrs: (3x + 5). Sum: (x + 5) + (3x + 5) = 70.",
                "substitution": "4x + 10 = 70.",
                "calculation": "Step 1: Form equation: (x + 5) + (3x + 5) = 70.\nStep 2: Combine terms: 4x + 10 = 70.\nStep 3: Subtract 10 from both sides: 4x = 60.\nStep 4: Divide by 4: x = 15.\nStep 5: Compute mother's age: 3x = 3 * 15 = 45.\nStep 6: Check: In 5 years, Salil is 20, Mother is 50. 20 + 50 = 70 (valid).",
                "finalAnswer": "Salil's present age = 15 years; Mother's present age = 45 years",
                "unit": "years",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q4: The difference between two positive integers is 63. The ratio of the two integers is 2:5. Find the two integers.",
                "given": "Ratio of integers = 2:5. Difference = 63.",
                "formula": "Let smaller integer = 2x, larger integer = 5x. Difference: 5x - 2x = 63.",
                "substitution": "3x = 63 => x = 63 / 3.",
                "calculation": "Step 1: Set up equation: 5x - 2x = 63.\nStep 2: 3x = 63 => x = 21.\nStep 3: Smaller integer = 2x = 2 * 21 = 42.\nStep 4: Larger integer = 5x = 5 * 21 = 105.\nStep 5: Check difference: 105 - 42 = 63 (valid).",
                "finalAnswer": "The two integers are 42 and 105",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q5: Ruby has 3 times as many two-rupee coins as she has five-rupee coins. If she has in all a sum of Rs 77, how many coins of each denomination does she have?",
                "given": "Let number of 5-rupee coins = x. Number of 2-rupee coins = 3x. Total money = Rs 77.",
                "formula": "Total Money = 5 * (number of Rs 5 coins) + 2 * (number of Rs 2 coins) = 77.",
                "substitution": "5(x) + 2(3x) = 77.",
                "calculation": "Step 1: Value of 5-rupee coins = 5x rupees.\nStep 2: Value of 2-rupee coins = 2 * (3x) = 6x rupees.\nStep 3: Total value = 5x + 6x = 11x rupees.\nStep 4: Set equal to Rs 77: 11x = 77.\nStep 5: Divide by 11: x = 7.\nStep 6: Number of 5-rupee coins = x = 7.\nStep 7: Number of 2-rupee coins = 3x = 3 * 7 = 21.\nStep 8: Check total value: 7 * 5 + 21 * 2 = 35 + 42 = Rs 77 (valid).",
                "finalAnswer": "Seven 5-rupee coins and twenty-one 2-rupee coins",
                "unit": "coins",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting that 2-rupee coins contribute 2 * (3x) = 6x rupees, rather than just 3x rupees.",
            "Adding 5 only to Salil and forgetting to add 5 to the mother when computing ages 5 years later."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Guide students from pure algebraic evaluation into multi-variable word problem formulation. Show that the same linear equations govern ages, ratios, and currency.",
        "visual_lesson_plan": {
            "title": "Polynomial Evaluations & Word Problem Geometry",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Graph of P(x) = 5x - 3 showing evaluation points (0, -3), (-1, -8), and (2, 7).",
            "concept_visuals": [
                {
                    "concept_title": "Evaluation Points on Linear Locus",
                    "diagram_title": "Plot of P(x) = 5x - 3",
                    "interactive_math_formula": "y = 5x - 3",
                    "mafs_graph_config": {
                        "domain": [-3, 4],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "5*x - 3", "color": "#2563EB", "label": "P(x) = 5x - 3"}
                        ],
                        "points": [
                            {"x": 0, "y": -3, "label": "P(0) = -3"},
                            {"x": -1, "y": -8, "label": "P(-1) = -8"},
                            {"x": 2, "y": 7, "label": "P(2) = 7"}
                        ]
                    },
                    "image_query": "evaluating linear functions table of values coordinates",
                    "video_query": "how to evaluate polynomials at given values algebra",
                    "what_to_explain": "Evaluating P(x) at specific x inputs produces coordinates (x, P(x)) lying directly on the line."
                },
                {
                    "concept_title": "Quadratic Evaluation Curve Q(s) = 7s^2 - 4s + 6",
                    "diagram_title": "Steep Quadratic Growth",
                    "interactive_math_formula": "Q(s) = 7s^2 - 4s + 6",
                    "mafs_graph_config": {
                        "domain": [-4, 5],
                        "range": [0, 110],
                        "curves": [
                            {"fn": "7*x^2 - 4*x + 6", "color": "#16A34A", "label": "Q(s) = 7s^2 - 4s + 6"}
                        ],
                        "points": [
                            {"x": 0, "y": 6, "label": "Q(0) = 6"},
                            {"x": -3, "y": 81, "label": "Q(-3) = 81"},
                            {"x": 4, "y": 102, "label": "Q(4) = 102"}
                        ]
                    },
                    "image_query": "quadratic polynomial evaluation points parabola graph",
                    "video_query": "evaluating quadratic functions with negative inputs",
                    "what_to_explain": "Negative inputs (-3) become positive when squared, driving rapid growth to Q(-3) = 81."
                },
                {
                    "concept_title": "Salil and Mother Age Growth Lines",
                    "diagram_title": "Parallel Age Trajectories over Time t",
                    "interactive_math_formula": "S(t) = 15 + t, M(t) = 45 + t",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [10, 60],
                        "curves": [
                            {"fn": "15 + x", "color": "#2563EB", "label": "Salil S(t) = 15 + t"},
                            {"fn": "45 + x", "color": "#D97706", "label": "Mother M(t) = 45 + t"}
                        ],
                        "points": [
                            {"x": 0, "y": 15, "label": "Salil Now: 15"},
                            {"x": 0, "y": 45, "label": "Mother Now: 45"},
                            {"x": 5, "y": 20, "label": "Salil in 5 yrs: 20"},
                            {"x": 5, "y": 50, "label": "Mother in 5 yrs: 50"}
                        ]
                    },
                    "image_query": "age word problem linear graphs parallel lines algebra",
                    "video_query": "solving age problems with linear equations algebra",
                    "what_to_explain": "Because time advances equally for both individuals, their age trajectories are parallel lines with slope 1."
                },
                {
                    "concept_title": "Ratio Difference Ray 2x vs 5x",
                    "diagram_title": "Linear Divergence of Ratio 2:5",
                    "interactive_math_formula": "y = 5x - 2x = 3x",
                    "mafs_graph_config": {
                        "domain": [0, 25],
                        "range": [0, 70],
                        "curves": [
                            {"fn": "3*x", "color": "#7C3AED", "label": "Difference Delta = 3x"}
                        ],
                        "points": [
                            {"x": 21, "y": 63, "label": "At x=21: Delta = 63"}
                        ]
                    },
                    "image_query": "ratio word problem difference linear function graph",
                    "video_query": "solving ratio and proportion word problems algebra",
                    "what_to_explain": "The difference between 5x and 2x is 3x, requiring multiplier x = 21 to reach 63."
                },
                {
                    "concept_title": "Coin Value Accumulation Function",
                    "diagram_title": "Ruby's Coin Value V(x) = 11x",
                    "interactive_math_formula": "V(x) = 5x + 6x = 11x",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 90],
                        "curves": [
                            {"fn": "11*x", "color": "#059669", "label": "Total Money V(x) = 11x"}
                        ],
                        "points": [
                            {"x": 7, "y": 77, "label": "7 sets = Rs 77"}
                        ]
                    },
                    "image_query": "coin word problem linear equation slope intercept",
                    "video_query": "how to solve coin word problems algebra 1",
                    "what_to_explain": "Each 5-rupee coin is paired with three 2-rupee coins, forming an 11-rupee packet."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Exercise 2.2 Mastery",
                    "questions": [
                        {
                            "question": "What is the value of 5x - 3 when x = -1?",
                            "type": "short_answer",
                            "options": ["-8", "-2", "2", "8"],
                            "ideal_answer": "-8, from 5(-1) - 3 = -5 - 3 = -8.",
                            "socratic_hint": "Multiply 5 by -1 first, then subtract 3."
                        },
                        {
                            "question": "In Salil's age problem, why is the equation (x + 5) + (3x + 5) = 70?",
                            "type": "short_answer",
                            "options": [
                                "Because 5 years must be added to BOTH Salil's age and his mother's age",
                                "Because 5 is added only to Salil",
                                "Because 5 years ago they were younger",
                                "It is an arbitrary assumption"
                            ],
                            "ideal_answer": "As 5 years pass, both Salil and his mother age by 5 years, so their future ages are (x + 5) and (3x + 5).",
                            "socratic_hint": "Does only one person grow older as time passes?"
                        },
                        {
                            "question": "If two numbers are in the ratio 2:5 and differ by 63, what is the value of the common multiplier x?",
                            "type": "short_answer",
                            "options": ["21", "63", "9", "31.5"],
                            "ideal_answer": "21, from 5x - 2x = 3x = 63 => x = 21.",
                            "socratic_hint": "5x - 2x = 3x. Divide 63 by 3."
                        },
                        {
                            "question": "How many total 2-rupee coins does Ruby have?",
                            "type": "short_answer",
                            "options": ["21", "7", "14", "28"],
                            "ideal_answer": "21, since she has 3 times as many 2-rupee coins as 5-rupee coins (3 * 7 = 21).",
                            "socratic_hint": "Multiply x = 7 by 3."
                        },
                        {
                            "question": "What is the value of 7s^2 - 4s + 6 at s = -3?",
                            "type": "short_answer",
                            "options": ["81", "69", "57", "93"],
                            "ideal_answer": "81, from 7(9) - 4(-3) + 6 = 63 + 12 + 6 = 81.",
                            "socratic_hint": "Remember that (-3)^2 = +9, and -4 * (-3) = +12."
                        }
                    ]
                }
            ]
        }
    }
