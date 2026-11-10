"""
Chapter 2: Introduction to Linear Polynomials - Module 1
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m1():
    m1_svg = build_cartesian_svg(
        domain=(-2, 6), range_y=(-2, 8),
        points=[
            {"x": 0, "y": 3, "label": "Intercept (0, 3)", "color": "#16A34A", "sub": "(0, 3)"},
            {"x": 2, "y": 7, "label": "Point (2, 7)", "color": "#2563EB", "sub": "(2, 7)"},
            {"x": -1.5, "y": 0, "label": "Zero (-1.5, 0)", "color": "#DC2626", "sub": "(-1.5, 0)"},
        ],
        lines=[
            {"p1": (-2, -1), "p2": (2.5, 8), "color": "#2563EB", "stroke_width": 2.5, "label": "P(x) = 2x + 3"}
        ],
        title="Linear Polynomial Anatomy: P(x) = 2x + 3",
        caption="Straight line graph showing y-intercept at (0, 3) and zero at (-1.5, 0)"
    )

    return {
        "order_index": 1,
        "title": "Theory of Polynomials: Variables, Degrees, Monomials to Trinomials & Linear Forms",
        "description": "Understand algebraic expressions, variables, coefficients, exponents, classification by number of terms and degree, constant polynomials, the zero polynomial, and standard linear polynomials P(x) = ax + b. Solve 100% of in-text examples and Exercise 2.1 questions.",
        "subtopics": [
            "Constants, variables, and algebraic combinations",
            "Definition of a Polynomial: Non-negative integer exponents",
            "Degree of a Polynomial: Highest power of the variable with non-zero coefficient",
            "Classification by Degree: Constant (0), Linear (1), Quadratic (2), Cubic (3)",
            "Classification by Terms: Monomial (1), Binomial (2), Trinomial (3)",
            "The Zero Polynomial and why its degree is undefined",
            "Standard form of a Linear Polynomial in one variable: P(x) = ax + b (a != 0)",
            "Complete step-by-step solutions to in-text Examples 1 to 4 and Exercise 2.1 Q1 to Q5"
        ],
        "key_concepts": [
            "Polynomial Definition: An expression of the form a_n x^n + ... + a_1 x + a_0 where exponents of x are whole numbers (0, 1, 2, ...).",
            "Degree Invariant: The degree of a polynomial in one variable is the highest exponent of the variable with a non-zero coefficient.",
            "Linear Polynomial: A polynomial of degree exactly 1, having the general form P(x) = ax + b where a, b are real numbers and a != 0.",
            "Constant Polynomial: A polynomial containing only a constant term c = c*x^0 (degree 0). The zero polynomial 0 has an undefined degree.",
            "Coefficient Invariant: The real number multiplying each power of the variable; if a term is missing, its coefficient is 0."
        ],
        "success_criteria": "Student can identify polynomials, determine degrees of expressions, classify terms, state standard linear forms, and find coefficients of any given term.",
        "chapter_notes": "A polynomial must have non-negative integer exponents. Terms like 1/x = x^(-1) or sqrt(x) = x^(1/2) violate this rule and are not polynomials.",
        "worked_examples": [
            {
                "problem": "Textbook Example 1: Raju went to a shop where red boxes contain 4 pens each. Express the total number of pens Raju gets if he buys x red boxes.",
                "given": "Each red box contains 4 pens. Number of boxes bought = x.",
                "formula": "Total Pens = (Number of pens per box) * (Number of boxes) = 4 * x.",
                "substitution": "Total pens = 4x.",
                "calculation": "Step 1: Identify the rate: 4 pens/box.\nStep 2: Multiply by the variable number of boxes, x: 4 * x = 4x.\nStep 3: Recognize that 4x is a monomial of degree 1 (a linear polynomial in x).",
                "finalAnswer": "Total pens = 4x (a linear monomial of degree 1)",
                "unit": "pens",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 2: A rectangular garden has length l metres and width w metres. Express the perimeter of the garden as an algebraic expression.",
                "given": "Length = l metres, Width = w metres.",
                "formula": "Perimeter P = 2 * (Length + Width) = 2l + 2w.",
                "substitution": "P = 2l + 2w.",
                "calculation": "Step 1: The perimeter is the total boundary distance: l + w + l + w.\nStep 2: Group like terms: (l + l) + (w + w) = 2l + 2w.\nStep 3: Recognize this as a linear binomial in two variables l and w.",
                "finalAnswer": "Perimeter = 2l + 2w metres",
                "unit": "metres",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 3: A wire of length 20 cm is bent to form a rectangle of length x cm. Express its breadth y in terms of x.",
                "given": "Total wire length (perimeter) = 20 cm. Length of rectangle = x cm.",
                "formula": "Perimeter = 2(x + y) = 20.",
                "substitution": "2x + 2y = 20 => x + y = 10 => y = 10 - x.",
                "calculation": "Step 1: Set up the perimeter equation: 2(x + y) = 20.\nStep 2: Divide both sides by 2: x + y = 10.\nStep 3: Solve for breadth y: y = 10 - x.\nStep 4: Note that y is a linear polynomial in x with slope -1 and y-intercept 10.",
                "finalAnswer": "Breadth y = 10 - x cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 4: The perimeter of a square of side x is 4x. Find the perimeter when side x = 3.5 cm.",
                "given": "Side length x = 3.5 cm. Perimeter function P(x) = 4x.",
                "formula": "P(x) = 4x.",
                "substitution": "P(3.5) = 4 * 3.5.",
                "calculation": "Step 1: Substitute x = 3.5 into P(x) = 4x.\nStep 2: 4 * 3.5 = 14.\nStep 3: State the unit: 14 cm.",
                "finalAnswer": "Perimeter = 14 cm",
                "unit": "cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q1 (i): Find the degree of the polynomial: 2x^2 - 5x + 3.",
                "given": "Polynomial: 2x^2 - 5x + 3.",
                "formula": "Degree = highest exponent of variable x with non-zero coefficient.",
                "substitution": "Exponents of x are 2, 1, 0. Highest exponent = 2.",
                "calculation": "Step 1: Identify terms and powers: 2x^2 (power 2), -5x^1 (power 1), 3x^0 (power 0).\nStep 2: The highest power is 2.\nStep 3: Therefore, the degree of the polynomial is 2 (Quadratic).",
                "finalAnswer": "Degree = 2 (Quadratic)",
                "unit": "degree",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q1 (ii): Find the degree of the polynomial: y^3 + 2y - 1.",
                "given": "Polynomial: y^3 + 2y - 1.",
                "formula": "Degree = highest exponent of variable y.",
                "substitution": "Exponents of y are 3, 1, 0. Highest exponent = 3.",
                "calculation": "Step 1: The highest power of y with a non-zero coefficient is 3 (from y^3).\nStep 2: Therefore, the degree is 3 (Cubic).",
                "finalAnswer": "Degree = 3 (Cubic)",
                "unit": "degree",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q1 (iii): Find the degree of the polynomial: -9.",
                "given": "Polynomial: -9.",
                "formula": "A non-zero constant c can be written as c * x^0.",
                "substitution": "-9 = -9 * x^0.",
                "calculation": "Step 1: -9 has no variable term, so power of x is 0.\nStep 2: Therefore, the degree of any non-zero constant polynomial is 0.",
                "finalAnswer": "Degree = 0 (Constant polynomial)",
                "unit": "degree",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q1 (iv): Find the degree of the polynomial: 4z - 3.",
                "given": "Polynomial: 4z - 3.",
                "formula": "Degree = highest exponent of variable z.",
                "substitution": "Exponents of z are 1 and 0. Highest exponent = 1.",
                "calculation": "Step 1: 4z = 4z^1. The highest power of z is 1.\nStep 2: Therefore, the degree is 1 (Linear).",
                "finalAnswer": "Degree = 1 (Linear)",
                "unit": "degree",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q2: Write one example each of polynomials of degrees 1, 2, and 3.",
                "given": "Required: Polynomials of degrees 1, 2, and 3.",
                "formula": "Degree 1: ax + b (a != 0); Degree 2: ax^2 + bx + c (a != 0); Degree 3: ax^3 + bx^2 + cx + d (a != 0).",
                "substitution": "Degree 1: 3x - 5; Degree 2: 2x^2 + 4x - 7; Degree 3: x^3 - 6x + 2.",
                "calculation": "Step 1: Degree 1 (Linear): 3x - 5 (highest power is 1).\nStep 2: Degree 2 (Quadratic): 2x^2 + 4x - 7 (highest power is 2).\nStep 3: Degree 3 (Cubic): x^3 - 6x + 2 (highest power is 3).",
                "finalAnswer": "Degree 1: 3x - 5; Degree 2: 2x^2 + 4x - 7; Degree 3: x^3 - 6x + 2",
                "unit": "polynomial examples",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q3: What are the coefficients of x^2 and x^3 in the polynomial x^4 - 3x^3 + 6x^2 - 2x + 7?",
                "given": "Polynomial: P(x) = x^4 - 3x^3 + 6x^2 - 2x + 7.",
                "formula": "The coefficient of x^n is the multiplying constant preceding x^n, including its sign.",
                "substitution": "x^3 term is -3x^3; x^2 term is +6x^2.",
                "calculation": "Step 1: Locate the x^3 term: -3x^3. Its coefficient is -3.\nStep 2: Locate the x^2 term: +6x^2. Its coefficient is 6.",
                "finalAnswer": "Coefficient of x^3 = -3; Coefficient of x^2 = 6",
                "unit": "coefficients",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q4 & Q5: (Q4) What is the coefficient of z in the polynomial 4z^3 + 5z^2 - 11? (Q5) What is the constant term of the polynomial 9x^3 + 5x^2 - 8x - 1?",
                "given": "Polynomials: (Q4) 4z^3 + 5z^2 - 11; (Q5) 9x^3 + 5x^2 - 8x - 1.",
                "formula": "If a power of variable is absent, its coefficient is 0. The constant term is the term independent of variable (x^0 term).",
                "substitution": "(Q4) 4z^3 + 5z^2 + 0z - 11; (Q5) Constant term = -1.",
                "calculation": "Step 1: In 4z^3 + 5z^2 - 11, the variable z (z^1) is not present. Therefore, coefficient of z is 0.\nStep 2: In 9x^3 + 5x^2 - 8x - 1, the term independent of x is -1. Therefore, the constant term is -1.",
                "finalAnswer": "(Q4) Coefficient of z = 0; (Q5) Constant term = -1",
                "unit": "numerical values",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Believing an absent variable has coefficient 1. If z is missing, its coefficient is 0, not 1!",
            "Ignoring the negative sign attached to a coefficient, writing 3 instead of -3 for -3x^3."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Ground variables in real-life measurements (boxes of pens, perimeter of gardens). Emphasize that exponents must be whole numbers.",
        "visual_lesson_plan": {
            "title": "Polynomial Degrees & Linear Anatomy",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Linear polynomial graph showing slope, y-intercept, and zero.",
            "concept_visuals": [
                {
                    "concept_title": "Linear Function P(x) = 2x + 3 Anatomy",
                    "diagram_title": "Slope and Intercept Representation",
                    "interactive_math_formula": "P(x) = 2x + 3",
                    "mafs_graph_config": {
                        "domain": [-4, 4],
                        "range": [-4, 10],
                        "curves": [
                            {"fn": "2*x + 3", "color": "#2563EB", "label": "P(x) = 2x + 3"}
                        ],
                        "points": [
                            {"x": 0, "y": 3, "label": "y-intercept (0, 3)"},
                            {"x": -1.5, "y": 0, "label": "Zero (-1.5, 0)"},
                            {"x": 2, "y": 7, "label": "Point (2, 7)"}
                        ]
                    },
                    "image_query": "Linear polynomial cartesian plane slope intercept zero",
                    "video_query": "Introduction to polynomials and degrees animated",
                    "what_to_explain": "Explain that degree 1 polynomials produce straight lines with slope 2 and y-intercept 3."
                },
                {
                    "concept_title": "Polynomial Degree Hierarchy",
                    "diagram_title": "Degree Curves Comparison (Linear, Quadratic, Cubic)",
                    "interactive_math_formula": "y = x, y = x^2, y = x^3",
                    "mafs_graph_config": {
                        "domain": [-2.5, 2.5],
                        "range": [-4, 6],
                        "curves": [
                            {"fn": "x", "color": "#2563EB", "label": "Degree 1: Linear y=x"},
                            {"fn": "x^2", "color": "#16A34A", "label": "Degree 2: Quadratic y=x^2"},
                            {"fn": "x^3", "color": "#D97706", "label": "Degree 3: Cubic y=x^3"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "(0, 0)"},
                            {"x": 1, "y": 1, "label": "(1, 1)"}
                        ]
                    },
                    "image_query": "polynomial degree curves comparison linear quadratic cubic",
                    "video_query": "polynomial degree comparison graph visual",
                    "what_to_explain": "Higher degrees introduce curvature and additional turns in the graph."
                },
                {
                    "concept_title": "Constant Polynomial Horizon",
                    "diagram_title": "Horizontal Line y = -9 (Degree 0)",
                    "interactive_math_formula": "P(x) = -9",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-12, 2],
                        "curves": [
                            {"fn": "-9", "color": "#7C3AED", "label": "y = -9 (Degree 0)"}
                        ],
                        "points": [
                            {"x": 0, "y": -9, "label": "(0, -9)"}
                        ]
                    },
                    "image_query": "constant polynomial horizontal line degree zero",
                    "video_query": "what is constant polynomial degree zero explained",
                    "what_to_explain": "A degree 0 polynomial is constant everywhere, producing a horizontal line parallel to the x-axis."
                },
                {
                    "concept_title": "Perimeter Linear Function P(x) = 4x",
                    "diagram_title": "Square Perimeter Proportionality",
                    "interactive_math_formula": "P(x) = 4x",
                    "mafs_graph_config": {
                        "domain": [0, 6],
                        "range": [0, 24],
                        "curves": [
                            {"fn": "4*x", "color": "#059669", "label": "Perimeter P(x) = 4x"}
                        ],
                        "points": [
                            {"x": 3.5, "y": 14, "label": "x=3.5 cm, P=14 cm"}
                        ]
                    },
                    "image_query": "direct proportionality linear graph square perimeter",
                    "video_query": "linear relationships direct variation graphs",
                    "what_to_explain": "Square perimeter grows in strict direct proportion to side length x."
                },
                {
                    "concept_title": "Complementary Breadth Line y = 10 - x",
                    "diagram_title": "Wire Partitioning Locus (x + y = 10)",
                    "interactive_math_formula": "y = 10 - x",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 10],
                        "curves": [
                            {"fn": "10 - x", "color": "#DC2626", "label": "y = 10 - x"}
                        ],
                        "points": [
                            {"x": 5, "y": 5, "label": "Square (5, 5)"},
                            {"x": 0, "y": 10, "label": "(0, 10)"},
                            {"x": 10, "y": 0, "label": "(10, 0)"}
                        ]
                    },
                    "image_query": "linear constraint line perimeter wire rectangle",
                    "video_query": "perimeter constraint linear equation graphing",
                    "what_to_explain": "As length x increases from 0 to 10, breadth y decreases linearly to preserve perimeter 20."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Polynomial Degrees & Classifications",
                    "questions": [
                        {
                            "question": "What is the degree of the polynomial 2x^2 - 5x + 3?",
                            "type": "short_answer",
                            "options": ["2", "1", "3", "0"],
                            "ideal_answer": "2, because the highest exponent of x is 2.",
                            "socratic_hint": "Find the highest power of x with a non-zero coefficient."
                        },
                        {
                            "question": "What is the coefficient of z in 4z^3 + 5z^2 - 11?",
                            "type": "short_answer",
                            "options": ["0", "1", "-11", "5"],
                            "ideal_answer": "0, because the term z^1 is absent from the expression.",
                            "socratic_hint": "If a term is not written, what is multiplying it?"
                        },
                        {
                            "question": "Why is the degree of a non-zero constant like -9 equal to 0?",
                            "type": "short_answer",
                            "options": [
                                "Because -9 can be written as -9 * x^0",
                                "Because -9 is negative",
                                "Because -9 has no meaning",
                                "It is actually undefined"
                            ],
                            "ideal_answer": "-9 = -9 * x^0, so the highest power of the variable is 0.",
                            "socratic_hint": "What power of x equals 1?"
                        },
                        {
                            "question": "If a wire of length 20 cm is bent into a rectangle of length x, what is its breadth y?",
                            "type": "short_answer",
                            "options": ["10 - x", "20 - x", "20 - 2x", "10/x"],
                            "ideal_answer": "10 - x, derived from 2(x + y) = 20 => x + y = 10.",
                            "socratic_hint": "Divide the perimeter by 2 to find length + breadth."
                        },
                        {
                            "question": "What is the constant term of 9x^3 + 5x^2 - 8x - 1?",
                            "type": "short_answer",
                            "options": ["-1", "1", "9", "-8"],
                            "ideal_answer": "-1, including its negative sign.",
                            "socratic_hint": "Find the term without any variable x."
                        }
                    ]
                }
            ]
        }
    }
