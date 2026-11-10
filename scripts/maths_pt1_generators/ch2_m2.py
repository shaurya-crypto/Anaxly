"""
Chapter 2: Introduction to Linear Polynomials - Module 2
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m2():
    m2_svg = build_cartesian_svg(
        domain=(-4, 6), range_y=(-6, 8),
        points=[
            {"x": 0, "y": -5, "label": "y-intercept (0, -5)", "color": "#16A34A", "sub": "(0, -5)"},
            {"x": 1.67, "y": 0, "label": "Zero (5/3, 0)", "color": "#DC2626", "sub": "(5/3, 0)"},
            {"x": 3, "y": 4, "label": "Point (3, 4)", "color": "#2563EB", "sub": "(3, 4)"},
        ],
        lines=[
            {"p1": (-0.33, -6), "p2": (4, 7), "color": "#2563EB", "stroke_width": 2.5, "label": "P(x) = 3x - 5"}
        ],
        title="Zero of a Linear Polynomial: P(x) = 3x - 5",
        caption="The zero x = 5/3 is the exact x-coordinate where the graph cuts the horizontal axis"
    )

    return {
        "order_index": 2,
        "title": "Linear Functions, Zeroes, Slope (m), and Geometric Intercepts",
        "description": "Master linear input-output models, algebraic zeroes of linear polynomials, geometric interpretation as x-intercepts, rate of change (slope m), and initial values (y-intercept b). Solve in-text Examples 5 to 8 and zero-determination problems.",
        "subtopics": [
            "Input-output machine representation of polynomials",
            "Definition of a Zero (Root) of a Polynomial: P(k) = 0",
            "General formula for the zero of a linear polynomial: x = -b/a (a != 0)",
            "Geometric interpretation: Zeroes are the x-intercepts of the graph y = P(x)",
            "Unique zero theorem: Every linear polynomial in one variable has exactly ONE real zero",
            "Slope m as constant rate of change and y-intercept b as starting state",
            "Step-by-step solutions to in-text Examples 5 to 8 and root verifications"
        ],
        "key_concepts": [
            "Zero of a Polynomial: A real number k is called a zero of polynomial P(x) if and only if P(k) = 0.",
            "Linear Zero Invariant: For P(x) = ax + b with a != 0, the unique zero is given by x = -b/a.",
            "Geometric x-Intercept Invariant: The zero of P(x) is the precise point (-b/a, 0) where the graph of y = P(x) intersects the horizontal x-axis.",
            "Rate of Change (Slope m): In P(x) = mx + c, m represents how much P(x) changes for each unit increase in x.",
            "Starting State (y-Intercept c): The value of P(0) = c, representing the baseline or fixed initial fee."
        ],
        "success_criteria": "Student can find the zero of any linear polynomial algebraically, locate it geometrically as the x-intercept, and model real-world linear rates of change.",
        "chapter_notes": "A linear polynomial ax + b (a != 0) always has exactly one real zero. A non-zero constant polynomial c has no zeroes.",
        "worked_examples": [
            {
                "problem": "Textbook Example 5: A chess club charges a joining fee of Rs 200 plus Rs 50 per month. Find the linear expression for the cost after m months, and calculate the cost for 6 months.",
                "given": "Fixed joining fee = Rs 200. Monthly fee = Rs 50. Number of months = m.",
                "formula": "Cost C(m) = Fixed Fee + (Monthly Rate * m) = 200 + 50m.",
                "substitution": "C(6) = 200 + 50 * 6.",
                "calculation": "Step 1: Write the cost function: C(m) = 50m + 200.\nStep 2: Here slope m = 50 (rate per month) and y-intercept = 200 (initial fee).\nStep 3: Substitute m = 6: C(6) = 200 + 300 = Rs 500.",
                "finalAnswer": "C(m) = 50m + 200; Cost for 6 months = Rs 500",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 6: The sum of two numbers is 64. One of the numbers is 3 times the other. Find the two numbers using a linear equation.",
                "given": "Let the smaller number be x. The larger number is 3x. Their sum is 64.",
                "formula": "x + 3x = 64.",
                "substitution": "4x = 64 => x = 64 / 4.",
                "calculation": "Step 1: Set up the linear equation: x + 3x = 64.\nStep 2: Combine like terms: 4x = 64.\nStep 3: Solve for x: x = 16.\nStep 4: Compute the larger number: 3x = 3 * 16 = 48.\nStep 5: Verify: 16 + 48 = 64.",
                "finalAnswer": "The two numbers are 16 and 48",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 7: Bela has Rs 100 for pocket money. She spends Rs 5 every day. Write a linear expression for the money remaining after d days, and find how many days her money will last.",
                "given": "Initial money = Rs 100. Daily expenditure = Rs 5. Days = d.",
                "formula": "Money remaining M(d) = 100 - 5d. Exhaustion occurs when M(d) = 0.",
                "substitution": "100 - 5d = 0 => 5d = 100.",
                "calculation": "Step 1: Linear expression: M(d) = 100 - 5d.\nStep 2: Set M(d) = 0 to find when money runs out: 100 - 5d = 0.\nStep 3: 5d = 100 => d = 20 days.\nStep 4: Geometrically, d = 20 is the zero of the polynomial M(d).",
                "finalAnswer": "M(d) = 100 - 5d; Her money will last for 20 days",
                "unit": "days",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 8: An auto-rickshaw fare starts at Rs 25 for the first km and is Rs 12 for each subsequent km. Express the total fare F for a distance of k kilometres (for k >= 1), and compute the fare for 8 km.",
                "given": "First km fare = Rs 25. Subsequent rate = Rs 12/km. Distance = k km.",
                "formula": "F(k) = 25 + 12 * (k - 1) = 12k + 13.",
                "substitution": "F(8) = 12 * 8 + 13.",
                "calculation": "Step 1: For k km, the first km costs Rs 25, leaving (k - 1) km at Rs 12/km.\nStep 2: F(k) = 25 + 12(k - 1) = 25 + 12k - 12 = 12k + 13.\nStep 3: For k = 8: F(8) = 12 * 8 + 13 = 96 + 13 = Rs 109.",
                "finalAnswer": "F(k) = 12k + 13; Fare for 8 km = Rs 109",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Derivation: Find the zero of the general linear polynomial P(x) = ax + b (where a != 0), and prove that it is unique.",
                "given": "Linear polynomial P(x) = ax + b, a != 0.",
                "formula": "P(x) = 0 => ax + b = 0.",
                "substitution": "ax = -b => x = -b/a.",
                "calculation": "Step 1: Set P(x) equal to zero: ax + b = 0.\nStep 2: Subtract b from both sides: ax = -b.\nStep 3: Since a != 0, we can divide by a: x = -b/a.\nStep 4: Uniqueness proof: Suppose there were two zeroes x1 and x2. Then ax1 + b = 0 and ax2 + b = 0. Subtracting gives a(x1 - x2) = 0. Since a != 0, x1 - x2 = 0 => x1 = x2. Hence the zero is strictly unique.",
                "finalAnswer": "Unique zero x = -b/a",
                "unit": "algebraic proof",
                "has_diagram": False
            },
            {
                "problem": "Problem: Find the zero of the linear polynomial P(x) = 3x - 5, and verify geometrically on the Cartesian plane.",
                "given": "Polynomial P(x) = 3x - 5.",
                "formula": "Set P(x) = 0 => 3x - 5 = 0.",
                "substitution": "3x = 5 => x = 5/3.",
                "calculation": "Step 1: Set 3x - 5 = 0.\nStep 2: 3x = 5 => x = 5/3 = 1.666...\nStep 3: Verification: P(5/3) = 3(5/3) - 5 = 5 - 5 = 0.\nStep 4: Geometric meaning: The graph of y = 3x - 5 cuts the x-axis at the point (5/3, 0).",
                "finalAnswer": "Zero is x = 5/3 (Point (5/3, 0))",
                "unit": "rational coordinate",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m2_svg
            },
            {
                "problem": "Problem: Find the zero of Q(x) = -4x + 12, and state its slope and y-intercept.",
                "given": "Polynomial Q(x) = -4x + 12.",
                "formula": "Q(x) = 0 => -4x + 12 = 0.",
                "substitution": "4x = 12 => x = 12 / 4 = 3.",
                "calculation": "Step 1: Set -4x + 12 = 0 => 4x = 12 => x = 3.\nStep 2: Slope m is the coefficient of x: m = -4 (downward sloping).\nStep 3: y-intercept is Q(0) = 12 (Point (0, 12)).\nStep 4: Verification: Q(3) = -4(3) + 12 = -12 + 12 = 0.",
                "finalAnswer": "Zero is x = 3; Slope m = -4; y-intercept = (0, 12)",
                "unit": "linear parameters",
                "has_diagram": False
            },
            {
                "problem": "Problem: Why does the non-zero constant polynomial P(x) = 7 have NO zeroes, while the zero polynomial P(x) = 0 has infinitely many zeroes?",
                "given": "Constant polynomial P(x) = 7 and Zero polynomial P(x) = 0.",
                "formula": "A zero requires P(x) = 0.",
                "substitution": "7 = 0 (impossible); 0 = 0 (always true).",
                "calculation": "Step 1: For P(x) = 7: No matter what real value x takes, P(x) is always 7. Since 7 != 0, there is no real number x for which P(x) = 0. Hence P(x) = 7 has no zero.\nStep 2: For P(x) = 0: For EVERY real number x, P(x) is identically 0. Therefore, every real number is a zero of the zero polynomial.",
                "finalAnswer": "P(x) = 7 has no zeroes; P(x) = 0 has infinitely many zeroes (every real number is a zero)",
                "unit": "conceptual proof",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Confusing the zero of a polynomial with the value of the polynomial at x = 0. The zero is the input x that makes P(x) = 0, not P(0)!",
            "Forgetting that slope m = -b/a is the negative ratio of constant to leading coefficient."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Connect the algebraic solution ax + b = 0 directly to the visual graph cutting the horizontal axis at (-b/a, 0). Show that a linear graph can cross the axis only once.",
        "visual_lesson_plan": {
            "title": "Linear Functions, Slopes & Zero Intersections",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Graph of P(x) = 3x - 5 showing x-intercept at 5/3 and y-intercept at -5.",
            "concept_visuals": [
                {
                    "concept_title": "Zero of a Polynomial as x-Intercept",
                    "diagram_title": "Graph y = 3x - 5 Crossing the x-axis at x = 5/3",
                    "interactive_math_formula": "y = 3x - 5",
                    "mafs_graph_config": {
                        "domain": [-2, 5],
                        "range": [-8, 8],
                        "curves": [
                            {"fn": "3*x - 5", "color": "#2563EB", "label": "y = 3x - 5"}
                        ],
                        "points": [
                            {"x": 1.667, "y": 0, "label": "Zero (5/3, 0)"},
                            {"x": 0, "y": -5, "label": "y-intercept (0, -5)"}
                        ]
                    },
                    "image_query": "linear function zero x intercept cartesian plane graph",
                    "video_query": "finding zeroes of linear polynomials geometrically",
                    "what_to_explain": "The zero x = 5/3 is the point where the line crosses the horizontal axis (y = 0)."
                },
                {
                    "concept_title": "Negative Slope Decay Function",
                    "diagram_title": "Money Depletion M(d) = 100 - 5d",
                    "interactive_math_formula": "M(d) = 100 - 5d",
                    "mafs_graph_config": {
                        "domain": [0, 25],
                        "range": [0, 120],
                        "curves": [
                            {"fn": "100 - 5*x", "color": "#DC2626", "label": "M(d) = 100 - 5d"}
                        ],
                        "points": [
                            {"x": 0, "y": 100, "label": "Start: Rs 100"},
                            {"x": 20, "y": 0, "label": "Exhausted: Day 20"}
                        ]
                    },
                    "image_query": "linear decay graph negative slope balance over time",
                    "video_query": "negative slope linear real world word problems",
                    "what_to_explain": "A negative slope of -5 indicates that the balance decreases by Rs 5 each day, reaching zero on day 20."
                },
                {
                    "concept_title": "Auto Fare Piecewise Linearity",
                    "diagram_title": "Fare Function F(k) = 12k + 13",
                    "interactive_math_formula": "F(k) = 12k + 13",
                    "mafs_graph_config": {
                        "domain": [1, 10],
                        "range": [20, 140],
                        "curves": [
                            {"fn": "12*x + 13", "color": "#16A34A", "label": "F(k) = 12k + 13"}
                        ],
                        "points": [
                            {"x": 1, "y": 25, "label": "1 km = Rs 25"},
                            {"x": 8, "y": 109, "label": "8 km = Rs 109"}
                        ]
                    },
                    "image_query": "taxi fare linear graph slope intercept word problem",
                    "video_query": "modeling taxi fare with linear functions algebra",
                    "what_to_explain": "The line has slope 12 (subsequent km rate) with a baseline offset reflecting the first-km flat rate."
                },
                {
                    "concept_title": "Zero Invariant Comparison",
                    "diagram_title": "Parallel Lines with Identical Slopes but Distinct Zeroes",
                    "interactive_math_formula": "y = 2x, y = 2x - 4, y = 2x + 4",
                    "mafs_graph_config": {
                        "domain": [-4, 4],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "2*x", "color": "#2563EB", "label": "y = 2x (Zero x=0)"},
                            {"fn": "2*x - 4", "color": "#D97706", "label": "y = 2x - 4 (Zero x=2)"},
                            {"fn": "2*x + 4", "color": "#7C3AED", "label": "y = 2x + 4 (Zero x=-2)"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "(0, 0)"},
                            {"x": 2, "y": 0, "label": "(2, 0)"},
                            {"x": -2, "y": 0, "label": "(-2, 0)"}
                        ]
                    },
                    "image_query": "parallel linear graphs different intercepts zeroes",
                    "video_query": "parallel lines slopes and intercepts explained",
                    "what_to_explain": "Shifting the line vertically by changing constant b shifts its zero horizontally by -b/m."
                },
                {
                    "concept_title": "Steepness Variation through Origin",
                    "diagram_title": "Lines y = mx for Slopes m = 0.5, 1, 2, 4",
                    "interactive_math_formula": "y = mx",
                    "mafs_graph_config": {
                        "domain": [-3, 3],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "0.5*x", "color": "#94A3B8", "label": "m = 0.5"},
                            {"fn": "x", "color": "#10B981", "label": "m = 1"},
                            {"fn": "2*x", "color": "#2563EB", "label": "m = 2"},
                            {"fn": "4*x", "color": "#DC2626", "label": "m = 4"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Common Zero (0, 0)"}
                        ]
                    },
                    "image_query": "slope rotation fan lines through origin algebra",
                    "video_query": "how slope affects line steepness rotating around origin",
                    "what_to_explain": "Increasing the slope m rotates the line counterclockwise, making it steeper while preserving root at x = 0."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Linear Zeroes and Slope",
                    "questions": [
                        {
                            "question": "What is the zero of the linear polynomial P(x) = ax + b (where a != 0)?",
                            "type": "short_answer",
                            "options": ["-b/a", "b/a", "-a/b", "b"],
                            "ideal_answer": "-b/a, found by solving ax + b = 0 => ax = -b => x = -b/a.",
                            "socratic_hint": "Subtract b from both sides, then divide by a."
                        },
                        {
                            "question": "Geometrically, what does the zero of a polynomial represent?",
                            "type": "short_answer",
                            "options": [
                                "The x-coordinate of the point where the graph intersects the x-axis",
                                "The y-intercept of the line",
                                "The slope of the line",
                                "The highest point on the curve"
                            ],
                            "ideal_answer": "The x-coordinate of the point where the graph crosses the x-axis (where y = 0).",
                            "socratic_hint": "On the x-axis, what is the value of y?"
                        },
                        {
                            "question": "How many real zeroes can a linear polynomial in one variable have?",
                            "type": "short_answer",
                            "options": ["Exactly one", "At most two", "Infinitely many", "Zero"],
                            "ideal_answer": "Exactly one, because a straight line with non-zero slope intersects the x-axis at exactly one point.",
                            "socratic_hint": "Can a non-horizontal straight line cross the x-axis more than once?"
                        },
                        {
                            "question": "If Bela starts with Rs 100 and spends Rs 5 each day, on which day does her money reach zero?",
                            "type": "short_answer",
                            "options": ["Day 20", "Day 25", "Day 15", "Day 100"],
                            "ideal_answer": "Day 20, because 100 - 5(20) = 0.",
                            "socratic_hint": "Divide 100 by 5."
                        },
                        {
                            "question": "Does the constant polynomial P(x) = 7 have any zeroes?",
                            "type": "short_answer",
                            "options": ["No, it has no zeroes", "Yes, x = 7", "Yes, x = 0", "Infinitely many"],
                            "ideal_answer": "No, because 7 can never equal 0 for any value of x.",
                            "socratic_hint": "Can 7 ever equal 0?"
                        }
                    ]
                }
            ]
        }
    }
