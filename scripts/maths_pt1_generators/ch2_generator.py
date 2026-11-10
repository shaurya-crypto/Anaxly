"""
Chapter 2: Introduction to Linear Polynomials
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

import json
from .svg_builder import build_cartesian_svg, get_svg_wrapper

def get_ch2_modules():
    curriculum_id = "cd14fc20-13b7-4d96-98fb-956720dc0f23"
    
    # -------------------------------------------------------------
    # MODULE 1: Polynomial Fundamentals & Degree
    # -------------------------------------------------------------
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
        title="Linear Polynomial: P(x) = 2x + 3",
        caption="Straight line graph cutting y-axis at (0, 3) and x-axis at zero (-1.5, 0)"
    )

    m1 = {
        "order_index": 1,
        "title": "Theory of Polynomials: Variables, Degrees, Monomials to Trinomials & Linear Forms",
        "description": "Understand algebraic expressions, variables, coefficients, exponents, classification by number of terms and degree, constant polynomials, and the standard form of linear polynomials P(x) = ax + b.",
        "subtopics": [
            "Constants, variables, and algebraic combinations",
            "Definition of a Polynomial: Non-negative integer exponents",
            "Degree of a Polynomial: Highest power of the variable",
            "Classification by Degree: Constant (0), Linear (1), Quadratic (2), Cubic (3)",
            "Classification by Terms: Monomial, Binomial, Trinomial",
            "The Zero Polynomial and why its degree is undefined",
            "Standard form of a Linear Polynomial in one variable: P(x) = ax + b (a != 0)"
        ],
        "key_concepts": [
            "Polynomial Definition: An expression of the form a_n x^n + ... + a_1 x + a_0 where exponents of x are whole numbers (0, 1, 2, ...).",
            "Degree Invariant: The degree of a polynomial in one variable is the highest exponent of the variable with a non-zero coefficient.",
            "Linear Polynomial: A polynomial of degree exactly 1, having the general form P(x) = ax + b where a, b are real numbers and a != 0.",
            "Constant Polynomial: A polynomial containing only a constant term c = c*x^0 (degree 0). The zero polynomial 0 has an undefined degree.",
            "Coefficient Invariant: The real number multiplying each power of the variable."
        ],
        "success_criteria": "Student can identify polynomials, determine degrees of expressions, classify terms, and state standard linear forms.",
        "chapter_notes": """### 1.1 What is a Polynomial?
An algebraic expression consisting of variables and coefficients, where the exponent of each variable term is a **non-negative integer** (whole number $0, 1, 2, \\dots$).
- Expressions like $x^2 + 3x + 5$ or $4x - 7$ are polynomials.
- Expressions like $\\sqrt{x} = x^{1/2}$ or $\\frac{1}{x} = x^{-1}$ are **NOT polynomials** because their exponents are not non-negative integers.

### 1.2 Degree of a Polynomial
- The **degree** is the highest exponent of the variable with a non-zero coefficient.
  - $5x - 3$: degree is $1$ (**Linear**).
  - $3x^2 + 4x - 1$: degree is $2$ (**Quadratic**).
  - $7$: degree is $0$ because $7 = 7x^0$ (**Constant polynomial**).
  - $0$: degree is **undefined** (**Zero polynomial**).

### 1.3 Linear Polynomials
A polynomial of degree 1:
$$P(x) = ax + b \\quad (a \\ne 0)$$
- $a$ is the leading coefficient (slope on graph).
- $b$ is the constant term (y-intercept on graph).""",
        "worked_examples": [
            {
                "problem": "Which of the following expressions are polynomials? For those that are polynomials, state their degree: (i) 4x^3 - 5x + 7, (ii) 2/x + 3x, (iii) sqrt(3)*x + 5, (iv) 4*sqrt(x) + x, (v) 12.",
                "given": "Five algebraic expressions.",
                "formula": "A polynomial must have whole-number powers of x (0, 1, 2, ...). Degree = highest power.",
                "substitution": "(i) Powers 3, 1, 0; (ii) Power -1; (iii) Power 1; (iv) Power 1/2; (v) Power 0.",
                "calculation": "1. 4x^3 - 5x + 7: Exponents of x are 3, 1, 0 (all whole numbers) -> YES, polynomial. Highest power = 3 -> Degree 3 (Cubic).\n2. 2/x + 3x = 2x^(-1) + 3x: Exponent is -1 (negative integer) -> NOT a polynomial.\n3. sqrt(3)*x + 5: Coefficient is sqrt(3) (real number), power of x is 1 -> YES, polynomial. Degree = 1 (Linear).\n4. 4*sqrt(x) + x = 4x^(1/2) + x: Exponent is 1/2 (fraction) -> NOT a polynomial.\n5. 12 = 12x^0: Non-zero constant -> YES, polynomial. Degree = 0 (Constant polynomial).",
                "finalAnswer": "(i) Degree 3; (ii) Not a polynomial; (iii) Degree 1; (iv) Not a polynomial; (v) Degree 0.",
                "unit": "degree",
                "has_diagram": False
            },
            {
                "problem": "Write a monomial of degree 100, a binomial of degree 35, and explain why the degree of the zero polynomial is undefined.",
                "given": "Monomial (1 term), Binomial (2 terms), and the Zero polynomial 0.",
                "formula": "Degree = highest non-zero power of variable.",
                "substitution": "Monomial: c * x^100. Binomial: a * x^35 + b.",
                "calculation": "Step 1: A monomial has exactly one non-zero term. Degree 100 monomial: 5x^100 or -7x^100.\nStep 2: A binomial has exactly two non-zero terms. Degree 35 binomial: x^35 - 1 or 4x^35 + 2x.\nStep 3: Why degree of 0 is undefined:\nWe can write 0 as 0*x^1, 0*x^2, 0*x^100, etc. Since 0*x^n = 0 for ANY power n, no single highest non-zero power can be assigned. Therefore, by mathematical convention, the degree of the zero polynomial is undefined.",
                "finalAnswer": "Monomial: 5x^100; Binomial: x^35 - 1; Degree of 0 is undefined because 0*x^n = 0 for all n.",
                "unit": "dimensionless",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Confusing constant coefficients that have square roots (like sqrt(3)*x) with variable square roots (like sqrt(x)). The former is a polynomial; the latter is not!",
            "Stating that the degree of 0 is 0. The constant polynomial 5 has degree 0, but the zero polynomial 0 has undefined degree."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Start with the difference between variables and constants. Emphasize that powers must be whole numbers. Call write_chalkboard(action='draw_svg_diagram', content='Linear Polynomial: P(x) = 2x + 3').",
        "visual_lesson_plan": {
            "title": "Polynomial Degrees & Linear Anatomy",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Linear polynomial graph showing slope, y-intercept, and zero.",
            "concept_visuals": [
                {
                    "concept_title": "Polynomial Degrees & Classifications",
                    "diagram_title": "Linear Function P(x) = 2x + 3",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m1_svg,
                    "interactive_math_formula": "y = 2x + 3",
                    "mafs_graph_config": {"domain": [-2, 6], "range": [-2, 8], "lines": [{"formula": "2*x + 3"}]},
                    "image_query": "Linear function graph on cartesian plane slope intercept",
                    "video_query": "Introduction to polynomials and degrees animated",
                    "image_url": "/images/curriculum/ch2_linear_polynomial.png",
                    "what_to_make": "Linear polynomial graph showing slope, y-intercept, and zero.",
                    "what_to_explain": "Explain that degree 1 polynomials always produce straight lines.",
                    "timing_and_cue": "Introduce at 02:00 when defining degree."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Polynomial Degrees & Classifications",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the degree of the polynomial 7x^4 - 2x^2 + 5?",
                            "ideal_answer": "4, because the highest exponent of x with a non-zero coefficient is 4.",
                            "socratic_hint": "Find the term with the highest power of x."
                        },
                        {
                            "q_num": "Q2",
                            "type": "1-mark MCQ",
                            "question": "Is 3/x + 4 a polynomial?",
                            "ideal_answer": "No, because 3/x = 3x^(-1), which has a negative exponent (-1). Exponents must be whole numbers.",
                            "socratic_hint": "Rewrite 1/x using negative index notation."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Short Answer",
                            "question": "What is the degree of a non-zero constant polynomial like -15?",
                            "ideal_answer": "The degree is 0, because -15 can be written as -15 * x^0.",
                            "socratic_hint": "What power of x equals 1 for all x != 0?"
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Short Answer",
                            "question": "Classify 4x^3 - 7x by degree and by number of terms.",
                            "ideal_answer": "By degree: Cubic (degree 3). By number of terms: Binomial (2 terms).",
                            "socratic_hint": "What is the highest power, and how many distinct terms are separated by the minus sign?"
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Short Answer",
                            "question": "Why is the degree of the zero polynomial undefined?",
                            "ideal_answer": "Because 0 can be written as 0*x^n for any whole number n. Since no unique highest power exists, its degree is undefined.",
                            "socratic_hint": "If you multiply 0 by x to any power, what is the result?"
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 2: Linear Functions, Zeroes & Slope
    # -------------------------------------------------------------
    m2_svg = build_cartesian_svg(
        domain=(-4, 6), range_y=(-4, 8),
        points=[
            {"x": 0, "y": 2, "label": "y-intercept (0, 2)", "color": "#16A34A", "sub": "(0, 2)"},
            {"x": -1.333, "y": 0, "label": "Zero (-4/3, 0)", "color": "#DC2626", "sub": "(-1.33, 0)"},
            {"x": 2, "y": 5, "label": "P(2, 5)", "color": "#2563EB", "sub": "(2, 5)"},
            {"x": 0, "y": 4, "label": "Parallel Line (0, 4)", "color": "#7C3AED", "sub": "(0, 4)"},
        ],
        lines=[
            {"p1": (-3, -2.5), "p2": (3.5, 7.25), "color": "#2563EB", "stroke_width": 2.5, "label": "y = 1.5x + 2"},
            {"p1": (-3, -0.5), "p2": (2.5, 7.75), "color": "#7C3AED", "stroke_width": 2, "dash": "4,4", "label": "y = 1.5x + 4"},
        ],
        title="Slope, Zeroes & Parallel Line Families",
        caption="Slope m = 1.5 indicates rate of increase; parallel lines share identical slope m"
    )

    m2 = {
        "order_index": 2,
        "title": "Linear Functions, Zeroes, Slope (m), and y-Intercepts",
        "description": "Master zeroes of linear polynomials (x = -b/a), input-output mappings, geometric interpretation of slope m (rise over run) and y-intercept b, and parallel line families.",
        "subtopics": [
            "Input-Output mapping: Evaluating P(x) for given domain inputs",
            "Zero of a Polynomial: The x-value where P(x) = 0",
            "Geometric meaning of a zero: The x-intercept of the line",
            "Slope-Intercept Form: y = mx + c (slope m and y-intercept c)",
            "Rate of change: Rise over Run (Delta y / Delta x)",
            "Parallel lines: Equal slopes (m1 = m2) with differing y-intercepts",
            "Solving linear equations ax + b = c step-by-step"
        ],
        "key_concepts": [
            "Zero of Linear Polynomial: The linear polynomial P(x) = ax + b (a != 0) has exactly ONE zero, given by x = -b/a.",
            "Geometric Zero: The real zero of P(x) is the x-coordinate of the point where the graph cuts the x-axis.",
            "Slope Invariant: In y = mx + c, m represents the constant rate of change (slope); every increase of 1 in x causes y to increase by m.",
            "y-Intercept Invariant: The value of y when x = 0 is c, giving intersection point (0, c).",
            "Parallel Lines Invariant: Two lines in the coordinate plane are parallel if and only if they have the same slope."
        ],
        "success_criteria": "Student can calculate zeroes, graph linear functions, interpret slope as a physical rate of change, and identify parallel lines.",
        "chapter_notes": """### 2.1 The Zero of a Linear Polynomial
A real number $k$ is a **zero** of polynomial $P(x)$ if $P(k) = 0$.
For a linear polynomial $P(x) = ax + b$ ($a \\ne 0$):
$$ax + b = 0 \\implies ax = -b \\implies x = -\\frac{b}{a}$$
- Every linear polynomial in one variable has **exactly one zero**.

### 2.2 Slope and y-Intercept ($y = mx + c$)
- **Slope ($m$)**: Ratio of vertical change to horizontal change:
  $$m = \\frac{\\Delta y}{\\Delta x} = \\frac{y_2 - y_1}{x_2 - x_1}$$
- **y-Intercept ($c$)**: Point $(0, c)$ where line crosses the vertical axis.
- **Parallel Family**: Lines with identical $m$ but different $c$ are parallel and never intersect.""",
        "worked_examples": [
            {
                "problem": "Find the zero of the linear polynomial P(x) = 3x - 5 and verify geometrically by finding its x-intercept and y-intercept.",
                "given": "P(x) = 3x - 5.",
                "formula": "Zero occurs when P(x) = 0. x-intercept: (x, 0). y-intercept: (0, P(0)).",
                "substitution": "Set 3x - 5 = 0.",
                "calculation": "Step 1: Set P(x) = 0:\n3x - 5 = 0\nStep 2: Add 5 to both sides:\n3x = 5\nStep 3: Divide by 3:\nx = 5 / 3 ≈ 1.67.\nStep 4: Find y-intercept:\nP(0) = 3(0) - 5 = -5 -> Point is (0, -5).\nStep 5: Geometric interpretation:\nThe graph is a straight line cutting the x-axis at (5/3, 0) and the y-axis at (0, -5). The zero is x = 5/3.",
                "finalAnswer": "The zero of P(x) is x = 5/3 (approx 1.67). x-intercept is (5/3, 0) and y-intercept is (0, -5).",
                "unit": "dimensionless",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m2_svg
            }
        ],
        "common_misconceptions": [
            "Confusing the zero of a polynomial with the value of the polynomial at x = 0 (the zero is the root x = -b/a, whereas P(0) = b is the y-intercept).",
            "Thinking that a linear polynomial can have more than one zero."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Socratic transition from equation solving to graphing. Emphasize that the zero is where the line hits the x-axis.",
        "visual_lesson_plan": {
            "title": "Zeroes & Slope Visualization",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Graph showing straight line intersecting both axes with slope triangle.",
            "concept_visuals": [
                {
                    "concept_title": "Slope and Zeroes",
                    "diagram_title": "Linear Function Slope and Zero",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m2_svg,
                    "interactive_math_formula": "x = -\\frac{b}{a} \\quad \\text{(Zero)}",
                    "mafs_graph_config": {"domain": [-4, 6], "range": [-4, 8], "lines": [{"formula": "1.5*x + 2"}]},
                    "image_query": "Linear equation slope intercept zero graph",
                    "video_query": "Zero of a linear polynomial geometric meaning",
                    "image_url": "/images/curriculum/ch2_slope_zeroes.png",
                    "what_to_make": "Straight line showing x-intercept at zero and y-intercept at constant term.",
                    "what_to_explain": "Show that the zero is where the graph crosses the horizontal axis.",
                    "timing_and_cue": "Introduce at 03:00 during zero derivation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Slope and Zeroes",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the zero of the linear polynomial P(x) = 4x + 12?",
                            "ideal_answer": "x = -3, because 4(-3) + 12 = -12 + 12 = 0.",
                            "socratic_hint": "Set 4x + 12 = 0 and solve for x."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What is the slope and y-intercept of the line y = -3x + 7?",
                            "ideal_answer": "Slope m = -3 (decreases by 3 units for every 1 unit increase in x); y-intercept is (0, 7).",
                            "socratic_hint": "Compare y = -3x + 7 with the standard form y = mx + c."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Short Answer",
                            "question": "Why do the lines y = 2x + 1 and y = 2x - 5 never intersect?",
                            "ideal_answer": "Because both lines have the exact same slope m = 2. Lines with equal slopes are parallel in the Euclidean plane and never meet.",
                            "socratic_hint": "Look at the coefficients of x in both equations."
                        },
                        {
                            "q_num": "Q4",
                            "type": "3-mark Short Answer",
                            "question": "How many zeroes does a non-zero constant polynomial like P(x) = 8 have?",
                            "ideal_answer": "Zero (none), because P(x) is always 8 and can never equal 0 for any value of x. Its graph y = 8 is parallel to the x-axis and never touches it.",
                            "socratic_hint": "Can the constant 8 ever equal 0?"
                        },
                        {
                            "q_num": "Q5",
                            "type": "2-mark Short Answer",
                            "question": "If a line passes through (0, 0) and (3, 6), find its equation.",
                            "ideal_answer": "Slope m = (6 - 0)/(3 - 0) = 2. Since y-intercept is 0, the equation is y = 2x.",
                            "socratic_hint": "Compute slope m = delta y / delta x and set c = 0."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 3: Textbook Exercise Solver 1: Examples 1 to 6 & Exercise 2.1
    # -------------------------------------------------------------
    m3_svg = build_cartesian_svg(
        domain=(-2, 10), range_y=(-2, 12),
        points=[
            {"x": 1, "y": 4, "label": "Square (1, 4)", "color": "#2563EB", "sub": "P = 4"},
            {"x": 2, "y": 8, "label": "Square (2, 8)", "color": "#2563EB", "sub": "P = 8"},
            {"x": 3, "y": 12, "label": "Square (3, 12)", "color": "#2563EB", "sub": "P = 12"},
        ],
        lines=[
            {"p1": (0, 0), "p2": (3, 12), "color": "#2563EB", "stroke_width": 2.5, "label": "P(x) = 4x"}
        ],
        title="Perimeter of Square as a Linear Polynomial",
        caption="Textbook Example 4: P(x) = 4x with constant growth rate of 4 units per unit side"
    )

    m3 = {
        "order_index": 3,
        "title": "Textbook Exercise Solver 1: Examples 1 to 6 & Exercise 2.1 (Degrees & Polynomial Models)",
        "description": "Complete step-by-step solutions for Textbook Examples 1 to 6 and all questions of Exercise 2.1: box totals, garden fencing costs, bent wire rectangles, square perimeter growth, chess club fees, two-number equations, polynomial degree checks, and coefficients.",
        "subtopics": [
            "Example 1: Raju's pen and pencil boxes (4x + 5y)",
            "Example 2: Rectangular garden fencing cost (100l + 80w + 50lw)",
            "Example 3: Bent wire 20 cm rectangles: area expression x(10 - x) = 10x - x^2",
            "Example 4: Square perimeter 4x as a linear polynomial and side variations",
            "Example 5: Chess club fee table (200 + 50m) as linear pattern",
            "Example 6: Two numbers sum 64 with difference 10: solving 2x + 10 = 64",
            "Exercise 2.1 Q1: Degrees of 2x^2-5x+3, y^3+2y-1, -9, 4z-3",
            "Exercise 2.1 Q2: Writing polynomials of degrees 1, 2, and 3",
            "Exercise 2.1 Q3: Coefficients of x^2 and x^3 in x^4 - 3x^3 + 6x^2 - 2x + 7"
        ],
        "key_concepts": [
            "Algebraic Modeling: Translating physical real-world quantities into variables and polynomials.",
            "Linear Pattern Invariant: A sequence of values where each step increases by a constant common difference is governed by a linear polynomial.",
            "Degree Determination: The degree is the exponent of the variable term with the highest power."
        ],
        "success_criteria": "Student can model physical scenarios with polynomials and determine degrees and coefficients with 100% accuracy.",
        "chapter_notes": """### Step-by-Step Exercise Solver: Examples 1 to 6 & Exercise 2.1
Full calculations following Topper layout with zero skipped steps.""",
        "worked_examples": [
            {
                "problem": "Textbook Example 1: Raju went to a shop where red boxes have 4 pens each and blue boxes have 5 pencils each. If Raju bought x red boxes and y blue boxes, write an expression for the total number of writing instruments he bought.",
                "given": "Pens per red box = 4, pencils per blue box = 5. Number of red boxes = x, number of blue boxes = y.",
                "formula": "Total items = (Pens/box * red boxes) + (Pencils/box * blue boxes).",
                "substitution": "Total = 4*x + 5*y.",
                "calculation": "1. Pens from x red boxes = 4 * x = 4x.\n2. Pencils from y blue boxes = 5 * y = 5y.\n3. Total number of writing instruments = 4x + 5y.\n4. Note: This is an algebraic expression in TWO variables (x and y).",
                "finalAnswer": "Total writing instruments = 4x + 5y.",
                "unit": "items",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 2: A rectangular garden of length l metres and width w metres has to be fenced and decorated. Wire fence along length costs Rs 100/m, wooden fence along width costs Rs 80/m, and special seeds throughout garden cost Rs 50/m^2. What is the total cost?",
                "given": "Length = l metres, Width = w metres. Wire cost = Rs 100/m (2 lengths), wooden fence = Rs 80/m (2 widths), seed cost = Rs 50/m^2 (area).",
                "formula": "Total Cost = (Cost of length fences) + (Cost of width fences) + (Cost of seeds * Area).",
                "substitution": "Cost = 2 * (100 * l) + 2 * (80 * w) + 50 * (l * w).",
                "calculation": "1. Cost of fencing both lengths = 2 * (100 * l) = 200l rupees.\n2. Cost of fencing both widths = 2 * (80 * w) = 160w rupees.\n3. Area of rectangular garden = length * width = l * w sq metres.\n4. Cost of sowing seeds = 50 * lw rupees.\n5. Summing all expenses: Total Cost = 200l + 160w + 50lw rupees.",
                "finalAnswer": "Total cost = 200l + 160w + 50lw rupees.",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 3: A wire of length 20 cm is bent to form a rectangle. If the length is x cm, write an expression for the area of the rectangle. What value does the expression take when x = 6 cm?",
                "given": "Perimeter of rectangle = 20 cm. Length = x cm.",
                "formula": "Perimeter = 2(length + width) => width = 20/2 - x = 10 - x. Area = length * width.",
                "substitution": "Area A(x) = x * (10 - x). Evaluate at x = 6.",
                "calculation": "Step 1: Find width in terms of x:\n2(x + width) = 20 => x + width = 10 => width = (10 - x) cm.\nStep 2: Express Area as a polynomial:\nArea = x(10 - x) = 10x - x^2 sq cm (degree 2 quadratic polynomial).\nStep 3: Evaluate at x = 6 cm:\nA(6) = 10(6) - (6)^2 = 60 - 36 = 24 sq cm.",
                "finalAnswer": "Expression for Area: 10x - x^2 sq cm; Area at x = 6 cm is 24 sq cm.",
                "unit": "cm^2",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 4: The perimeter of a square of side x is 4x. Find the perimeter for x = 1 cm, 1.5 cm, 2 cm, 2.5 cm, 3 cm. By how much does the perimeter increase each time the side increases by 0.5 cm?",
                "given": "Perimeter function P(x) = 4x.",
                "formula": "P(x) = 4x. Delta P = P(x + 0.5) - P(x).",
                "substitution": "Evaluate P(x) at x = 1, 1.5, 2, 2.5, 3.",
                "calculation": "1. P(1.0) = 4(1.0) = 4.0 cm.\n2. P(1.5) = 4(1.5) = 6.0 cm.\n3. P(2.0) = 4(2.0) = 8.0 cm.\n4. P(2.5) = 4(2.5) = 10.0 cm.\n5. P(3.0) = 4(3.0) = 12.0 cm.\nStep 6: Compute increment:\nDelta P = 4(x + 0.5) - 4x = 4x + 2.0 - 4x = 2.0 cm.\nEach 0.5 cm increase in side length causes an exact 2.0 cm increase in perimeter.",
                "finalAnswer": "Perimeters are 4, 6, 8, 10, 12 cm. Perimeter increases by 2.0 cm for every 0.5 cm increase in side length.",
                "unit": "cm",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m3_svg
            },
            {
                "problem": "Textbook Example 5: A chess club charges a joining fee of Rs 200 plus Rs 50 for every match played. If m is the number of matches played, write the total cost function and find the amount paid for 5 matches.",
                "given": "Fixed joining fee = Rs 200, cost per match = Rs 50. Number of matches = m.",
                "formula": "Total Cost C(m) = Fixed fee + (rate * m).",
                "substitution": "C(m) = 200 + 50m. Evaluate at m = 5.",
                "calculation": "Step 1: Write cost function:\nC(m) = 200 + 50m rupees.\nStep 2: Evaluate for m = 5 matches:\nC(5) = 200 + 50(5) = 200 + 250 = 450 rupees.\nStep 3: This represents a linear pattern because the cost increases by a constant Rs 50 for every additional match.",
                "finalAnswer": "Cost function C(m) = 200 + 50m; Cost for 5 matches = Rs 450.",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 6: The sum of two numbers is 64. One of the numbers is 10 more than the other. What are the two numbers?",
                "given": "Sum of numbers = 64. Larger number = smaller number + 10.",
                "formula": "Let smaller number = x. Larger number = x + 10. Equation: x + (x + 10) = 64.",
                "substitution": "2x + 10 = 64.",
                "calculation": "Step 1: Set up the linear equation:\nx + x + 10 = 64\n2x + 10 = 64\nStep 2: Subtract 10 from both sides:\n2x = 64 - 10 = 54\nStep 3: Divide by 2:\nx = 54 / 2 = 27 (smaller number).\nStep 4: Compute larger number:\nLarger number = x + 10 = 27 + 10 = 37.\nStep 5: Verification:\nSum = 27 + 37 = 64. Verified!",
                "finalAnswer": "The two numbers are 27 and 37.",
                "unit": "dimensionless",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q1: Find the degrees of the following polynomials: (i) 2x^2 - 5x + 3, (ii) y^3 + 2y - 1, (iii) -9, (iv) 4z - 3.",
                "given": "Four polynomial expressions.",
                "formula": "Degree = highest exponent of the variable with a non-zero coefficient.",
                "substitution": "(i) Exponents 2, 1, 0; (ii) Exponents 3, 1, 0; (iii) Constant -9*x^0; (iv) Exponents 1, 0.",
                "calculation": "1. 2x^2 - 5x + 3: Highest exponent of x is 2 -> Degree = 2 (Quadratic).\n2. y^3 + 2y - 1: Highest exponent of y is 3 -> Degree = 3 (Cubic).\n3. -9 = -9x^0: Highest exponent is 0 -> Degree = 0 (Constant polynomial).\n4. 4z - 3: Highest exponent of z is 1 -> Degree = 1 (Linear).",
                "finalAnswer": "(i) Degree 2; (ii) Degree 3; (iii) Degree 0; (iv) Degree 1.",
                "unit": "degree",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.1 Q2 & Q3: (Q2) Write polynomials of degrees 1, 2, and 3. (Q3) What are the coefficients of x^2 and x^3 in the polynomial x^4 - 3x^3 + 6x^2 - 2x + 7?",
                "given": "Q2: Requirements for degree 1, 2, 3. Q3: P(x) = x^4 - 3x^3 + 6x^2 - 2x + 7.",
                "formula": "Coefficient = numerical multiplier of each corresponding variable term.",
                "substitution": "In P(x): Term with x^3 is -3x^3; term with x^2 is +6x^2.",
                "calculation": "Part Q2:\n- Degree 1 (Linear): 7x - 4.\n- Degree 2 (Quadratic): 3x^2 + 5x - 2.\n- Degree 3 (Cubic): 2x^3 - x^2 + 4.\n\nPart Q3:\n- The term containing x^3 is -3x^3, so the coefficient of x^3 is -3.\n- The term containing x^2 is +6x^2, so the coefficient of x^2 is +6.\n- (Leading coefficient of x^4 is 1; coefficient of x is -2; constant term is 7).",
                "finalAnswer": "Q2: Examples: 7x - 4 (deg 1), 3x^2 + 5x - 2 (deg 2), 2x^3 - x^2 + 4 (deg 3). Q3: Coefficient of x^3 is -3; coefficient of x^2 is 6.",
                "unit": "dimensionless",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting the negative sign in coefficients: reporting coefficient of x^3 as 3 instead of -3.",
            "Confusing the number of terms (monomial, binomial) with the degree."
        ],
        "ai_system_prompt_context": "SOCRATIC DIRECTIVE: Pose Example 3 to the student: 'If the perimeter of a rectangle is fixed at 20 cm, how does changing length affect area?'",
        "visual_lesson_plan": {
            "title": "Exercise 2.1 & Models Visuals",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Square perimeter growth graph showing direct proportionality.",
            "concept_visuals": [
                {
                    "concept_title": "Direct Variation & Perimeter Models",
                    "diagram_title": "Square Perimeter Growth P(x) = 4x",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m3_svg,
                    "interactive_math_formula": "P(x) = 4x",
                    "mafs_graph_config": {"domain": [-2, 10], "range": [-2, 12], "lines": [{"formula": "4*x"}]},
                    "image_query": "Linear proportionality graph cartesian plane",
                    "video_query": "Linear patterns and algebraic modeling animation",
                    "image_url": "/images/curriculum/ch2_perimeter_growth.png",
                    "what_to_make": "Direct variation graph passing through origin with slope 4.",
                    "what_to_explain": "Explain that every unit step in side length increases perimeter by 4 units.",
                    "timing_and_cue": "Introduce at 03:30 during Example 4 explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Direct Variation & Perimeter Models",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the degree of the polynomial 5x - 8?",
                            "ideal_answer": "1, because the highest power of x is 1.",
                            "socratic_hint": "What is the exponent of x in 5x?"
                        },
                        {
                            "q_num": "Q2",
                            "type": "1-mark MCQ",
                            "question": "In the polynomial 4x^3 - 7x^2 + 2x - 9, what is the coefficient of x^2?",
                            "ideal_answer": "-7. Remember to include the negative sign.",
                            "socratic_hint": "What number multiplies x^2, including its sign?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Short Answer",
                            "question": "A taxi charges a fixed Rs 50 plus Rs 12 per km. Write the total fare polynomial for x km.",
                            "ideal_answer": "F(x) = 12x + 50.",
                            "socratic_hint": "Combine the variable cost per km with the fixed booking fee."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Short Answer",
                            "question": "Is the area of a circle with radius r, A = pi*r^2, a linear polynomial?",
                            "ideal_answer": "No, it is a quadratic polynomial because the exponent of r is 2.",
                            "socratic_hint": "What is the power of the variable r?"
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Short Answer",
                            "question": "If two numbers add up to 50 and their difference is 14, find the numbers using a linear equation.",
                            "ideal_answer": "Let numbers be x and x + 14. Then x + (x + 14) = 50 => 2x = 36 => x = 18. Numbers are 18 and 32.",
                            "socratic_hint": "Write the larger number in terms of the smaller number, then set their sum to 50."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 4: Textbook Exercise Solver 2: Exercise 2.2, Examples 7-8 & Exercise 2.3
    # -------------------------------------------------------------
    m4_svg = build_cartesian_svg(
        domain=(-2, 14), range_y=(-10, 110),
        points=[
            {"x": 0, "y": 100, "label": "Initial (0, 100)", "color": "#16A34A", "sub": "Rs 100"},
            {"x": 12, "y": 40, "label": "Target (12, 40)", "color": "#DC2626", "sub": "Rs 40"},
            {"x": 20, "y": 0, "label": "Zero (20, 0)", "color": "#2563EB", "sub": "Day 20"},
        ],
        lines=[
            {"p1": (0, 100), "p2": (20, 0), "color": "#DC2626", "stroke_width": 2.5, "label": "A(d) = 100 - 5d"}
        ],
        title="Linear Decay: Bela's Pocket Money",
        caption="Textbook Example 7: Amount remaining A(d) = 100 - 5d reaches Rs 40 on Day 12"
    )

    m4 = {
        "order_index": 4,
        "title": "Textbook Exercise Solver 2: Exercise 2.2, Examples 7-8 & Exercise 2.3 (Decay & Step Models)",
        "description": "Complete step-by-step solutions for Exercise 2.2, Textbook Examples 7 and 8, and Exercise 2.3: polynomial evaluations, Salil's age problem, integer ratios, linear decay of pocket money, auto-rickshaw step pricing, and bank savings growth.",
        "subtopics": [
            "Exercise 2.2 Q1: Value of linear polynomial 5x - 3 at x = 0, -1, 2",
            "Exercise 2.2 Q2: Value of quadratic polynomial 7s^2 - 4s + 6 at s = 0, -3, 4",
            "Exercise 2.2 Q3: Salil and mother's age word problem (3x + 5 + x + 5 = 70)",
            "Exercise 2.2 Q4: Difference between positive integers is 63, ratio 2:5",
            "Example 7: Bela's pocket money decay A(d) = 100 - 5d = 40 (d = 12 days)",
            "Example 8: Auto-rickshaw fare with initial flat rate: Rs 25 for first 2 km, Rs 15/km after",
            "Exercise 2.3 Q1: Savings bank account initial Rs 500 + Rs 150/month linear model"
        ],
        "key_concepts": [
            "Polynomial Evaluation: Substituting specific numerical values for variables to determine polynomial output.",
            "Linear Decay Rate: When a quantity decreases by a constant amount each unit of time, its slope is negative: y = y0 - mt.",
            "Piecewise / Step Function Modeling: Handling initial flat fees where mileage rates apply only after an initial threshold."
        ],
        "success_criteria": "Student can evaluate polynomials, solve linear word problems with age and ratio models, and model linear decay and step charges.",
        "chapter_notes": """### Step-by-Step Solver: Exercise 2.2, Examples 7-8 & Exercise 2.3
Exhaustive calculations following Topper format with zero skipped steps.""",
        "worked_examples": [
            {
                "problem": "Exercise 2.2 Q1: Find the value of the linear polynomial P(x) = 5x - 3 if: (i) x = 0, (ii) x = -1, (iii) x = 2.",
                "given": "P(x) = 5x - 3.",
                "formula": "Evaluate P(x) by direct substitution.",
                "substitution": "Substitute x = 0, x = -1, and x = 2 into 5x - 3.",
                "calculation": "1. For x = 0:\nP(0) = 5(0) - 3 = 0 - 3 = -3.\n\n2. For x = -1:\nP(-1) = 5(-1) - 3 = -5 - 3 = -8.\n\n3. For x = 2:\nP(2) = 5(2) - 3 = 10 - 3 = 7.",
                "finalAnswer": "(i) P(0) = -3; (ii) P(-1) = -8; (iii) P(2) = 7.",
                "unit": "dimensionless",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q2: Find the value of the quadratic polynomial Q(s) = 7s^2 - 4s + 6 if: (i) s = 0, (ii) s = -3, (iii) s = 4.",
                "given": "Q(s) = 7s^2 - 4s + 6.",
                "formula": "Evaluate Q(s) by direct substitution.",
                "substitution": "Substitute s = 0, s = -3, and s = 4.",
                "calculation": "1. For s = 0:\nQ(0) = 7(0)^2 - 4(0) + 6 = 0 - 0 + 6 = 6.\n\n2. For s = -3:\nQ(-3) = 7(-3)^2 - 4(-3) + 6\n= 7(9) - (-12) + 6 = 63 + 12 + 6 = 81.\n\n3. For s = 4:\nQ(4) = 7(4)^2 - 4(4) + 6\n= 7(16) - 16 + 6 = 112 - 16 + 6 = 102.",
                "finalAnswer": "(i) Q(0) = 6; (ii) Q(-3) = 81; (iii) Q(4) = 102.",
                "unit": "dimensionless",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q3: The present age of Salil's mother is three times Salil's present age. After 5 years, their ages will add up to 70 years. Find their present ages.",
                "given": "Let Salil's present age = x years. Mother's present age = 3x years. After 5 years, sum of ages = 70 years.",
                "formula": "Salil in 5 yrs = x + 5; Mother in 5 yrs = 3x + 5. Equation: (x + 5) + (3x + 5) = 70.",
                "substitution": "4x + 10 = 70.",
                "calculation": "Step 1: Set up equation:\n(x + 5) + (3x + 5) = 70\n4x + 10 = 70\nStep 2: Subtract 10 from both sides:\n4x = 70 - 10 = 60\nStep 3: Divide by 4:\nx = 60 / 4 = 15 years (Salil's present age).\nStep 4: Compute Mother's age:\nMother's age = 3x = 3 * 15 = 45 years.\nStep 5: Verification:\nIn 5 years: Salil = 20, Mother = 50. Sum = 20 + 50 = 70 years. Verified!",
                "finalAnswer": "Salil's present age = 15 years; Mother's present age = 45 years.",
                "unit": "years",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.2 Q4: The difference between two positive integers is 63. The ratio of the two integers is 2:5. What are the two integers?",
                "given": "Ratio of integers = 2:5. Difference = 63.",
                "formula": "Let the two integers be 2k and 5k where k is a positive integer. Equation: 5k - 2k = 63.",
                "substitution": "3k = 63.",
                "calculation": "Step 1: Write terms in common multiplier k:\nSmaller integer = 2k; Larger integer = 5k.\nStep 2: Set up difference equation:\n5k - 2k = 63\n3k = 63\nStep 3: Solve for k:\nk = 63 / 3 = 21.\nStep 4: Calculate integers:\nSmaller integer = 2k = 2 * 21 = 42.\nLarger integer = 5k = 5 * 21 = 105.\nStep 5: Verification:\nDifference = 105 - 42 = 63. Ratio = 42/105 = 2/5. Verified!",
                "finalAnswer": "The two integers are 42 and 105.",
                "unit": "dimensionless",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 7: Bela has Rs 100 for pocket money. She spends Rs 5 every day. After how many days will she be left with Rs 40?",
                "given": "Initial money A0 = Rs 100, daily spend rate = Rs 5/day. Target remaining amount = Rs 40.",
                "formula": "Remaining money A(d) = 100 - 5d. Set A(d) = 40.",
                "substitution": "100 - 5d = 40.",
                "calculation": "Step 1: Write linear decay function:\nA(d) = 100 - 5d\nStep 2: Set A(d) = 40:\n100 - 5d = 40\nStep 3: Subtract 100 from both sides:\n-5d = 40 - 100 = -60\nStep 4: Divide by -5:\nd = -60 / -5 = 12 days.\nStep 5: Verification:\nMoney spent in 12 days = 12 * 5 = 60 rupees.\nRemaining money = 100 - 60 = 40 rupees. Verified!",
                "finalAnswer": "Bela will be left with Rs 40 after 12 days.",
                "unit": "days",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m4_svg
            },
            {
                "problem": "Textbook Example 8: An auto-rickshaw fare starts at Rs 25 and remains the same for the initial 2 km. Then it increases by Rs 15 per km. What will be the fare for a travel of 10 km?",
                "given": "Initial fare = Rs 25 for first 2 km. Additional distance rate = Rs 15/km. Total distance = 10 km.",
                "formula": "For d > 2: Fare F(d) = 25 + 15*(d - 2).",
                "substitution": "d = 10 km. F(10) = 25 + 15*(10 - 2).",
                "calculation": "Step 1: Identify distance beyond initial 2 km:\nAdditional distance = 10 - 2 = 8 km.\nStep 2: Compute cost of additional distance:\n8 km * Rs 15/km = Rs 120.\nStep 3: Add initial flat fare:\nTotal Fare = 25 + 120 = Rs 145.\nStep 4: Complete algebraic form:\nF(d) = 25 + 15d - 30 = 15d - 5 (for d >= 2).\nAt d = 10: 15(10) - 5 = 150 - 5 = 145 rupees.",
                "finalAnswer": "Total fare for 10 km = Rs 145.",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.3 Q1: A student has Rs 500 in her savings bank account. She gets Rs 150 every month as pocket money. How much money will she have at the end of every month from the second month onwards? Find a linear expression to represent the amount she will have in the nth month.",
                "given": "Initial deposit = Rs 500. Monthly deposit = Rs 150. Month number = n.",
                "formula": "Total savings S(n) = Initial amount + (monthly deposit * n).",
                "substitution": "S(n) = 500 + 150n.",
                "calculation": "Step 1: Set up linear function:\nS(n) = 500 + 150n rupees.\nStep 2: Evaluate for initial months:\n- End of Month 1: S(1) = 500 + 150(1) = Rs 650.\n- End of Month 2: S(2) = 500 + 150(2) = Rs 800.\n- End of Month 3: S(3) = 500 + 150(3) = Rs 950.\n- End of Month 4: S(4) = 500 + 150(4) = Rs 1100.\nStep 3: This sequence forms an arithmetic progression with common difference Rs 150.",
                "finalAnswer": "Linear expression: S(n) = 500 + 150n rupees. Savings at ends of months 2, 3, 4 are Rs 800, Rs 950, Rs 1100.",
                "unit": "rupees",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting to subtract the base 2 km in Example 8 and calculating 25 + 15*10 instead of 25 + 15*8.",
            "Misinterpreting decay: writing 100 + 5d instead of 100 - 5d."
        ],
        "ai_system_prompt_context": "SOCRATIC DIRECTIVE: Challenge student on auto-rickshaw problem: 'Why do we multiply 15 by (10 - 2) rather than 10?'",
        "visual_lesson_plan": {
            "title": "Decay & Rate Functions Visuals",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Decay line graph of money remaining over days.",
            "concept_visuals": [
                {
                    "concept_title": "Linear Decay & Step Models",
                    "diagram_title": "Pocket Money Depletion A(d) = 100 - 5d",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m4_svg,
                    "interactive_math_formula": "A(d) = 100 - 5d",
                    "mafs_graph_config": {"domain": [-2, 14], "range": [-10, 110], "lines": [{"formula": "100 - 5*x"}]},
                    "image_query": "Linear decay rate graph cartesian plane",
                    "video_query": "Linear decay and rate of change animation",
                    "image_url": "/images/curriculum/ch2_linear_decay.png",
                    "what_to_make": "Downward sloping line cutting y-axis at 100 and reaching target 40 at day 12.",
                    "what_to_explain": "Explain that negative slope represents continuous spending/decay.",
                    "timing_and_cue": "Introduce at 03:00 during Example 7 explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Linear Decay & Step Models",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "If P(x) = 3x - 7, what is P(3)?",
                            "ideal_answer": "P(3) = 3(3) - 7 = 9 - 7 = 2.",
                            "socratic_hint": "Replace x with 3 and simplify."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "A tank holds 500 L of water and leaks 15 L per hour. Write the volume function V(t).",
                            "ideal_answer": "V(t) = 500 - 15t, where t is time in hours.",
                            "socratic_hint": "Subtract the leaked volume (15 * t) from the initial volume 500."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Short Answer",
                            "question": "In the auto-rickshaw problem, why is the formula 25 + 15(d - 2) and not 25 + 15d?",
                            "ideal_answer": "Because the first 2 km are already covered by the initial fixed fare of Rs 25. The additional Rs 15/km applies only to the distance travelled beyond 2 km.",
                            "socratic_hint": "How many kilometers does the Rs 25 flat charge cover?"
                        },
                        {
                            "q_num": "Q4",
                            "type": "3-mark Short Answer",
                            "question": "If father is 4 times as old as son, and their ages sum to 60, find their ages.",
                            "ideal_answer": "x + 4x = 60 => 5x = 60 => x = 12. Son is 12 years old, father is 48 years old.",
                            "socratic_hint": "Set son's age as x, father's age as 4x."
                        },
                        {
                            "q_num": "Q5",
                            "type": "2-mark Short Answer",
                            "question": "After how many days will Bela's money (A(d) = 100 - 5d) be completely exhausted?",
                            "ideal_answer": "Set A(d) = 0 => 100 - 5d = 0 => 5d = 100 => d = 20 days.",
                            "socratic_hint": "Find the zero of the polynomial 100 - 5d."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 5: Textbook Exercise Solver 3: Examples 9-11 & Exercises 2.4-2.5
    # -------------------------------------------------------------
    m5_svg = build_cartesian_svg(
        domain=(-2, 25), range_y=(-50, 650),
        points=[
            {"x": 10, "y": 350, "label": "Plan A (10, 350)", "color": "#2563EB", "sub": "Rs 350"},
            {"x": 20, "y": 550, "label": "Plan B (20, 550)", "color": "#2563EB", "sub": "Rs 550"},
            {"x": 0, "y": 150, "label": "Fixed b (0, 150)", "color": "#16A34A", "sub": "b = 150"},
        ],
        lines=[
            {"p1": (0, 150), "p2": (24, 630), "color": "#2563EB", "stroke_width": 2.5, "label": "y = 20x + 150"}
        ],
        title="Telecom & Learning Platform Cost Models",
        caption="Textbook Example 11: Two-point line solution y = 20x + 150 with fixed fee b = 150 and rate a = 20"
    )

    m5 = {
        "order_index": 5,
        "title": "Textbook Exercise Solver 3: Examples 9 to 11 & Exercises 2.4-2.5 (Two-Point Rate Systems)",
        "description": "Complete step-by-step solutions for Examples 9, 10, 11 and Exercises 2.4 and 2.5: journey cost tables, water tank evaporation, plant growth models, mobile phone depreciation, and solving two-point simultaneous equations y = ax + b.",
        "subtopics": [
            "Example 9: Journey cost function C(d) = 100 + 60d table and rate of change",
            "Example 10: Water tank evaporation h(t) = 3 - 0.5t table",
            "Exercise 2.4 Q1: Plant growth h(t) = 1.75 + 0.5t (height after 7 months = 5.25 ft)",
            "Exercise 2.4 Q2: Mobile phone depreciation (initial Rs 10000 decreasing by Rs 800/year)",
            "Example 11: Telecom internet bill y = ax + b (10 GB -> Rs 350, 20 GB -> Rs 550 -> a = 20, b = 150)",
            "Exercise 2.5 Q1: Learning platform fee y = ax + b (10 modules -> Rs 400, 14 modules -> Rs 500 -> a = 25, b = 150)",
            "Exercise 2.5 Q2: Gym court fee two-point rate system"
        ],
        "key_concepts": [
            "Slope as Marginal Rate: In y = ax + b, coefficient a is the marginal cost per additional unit consumed.",
            "Intercept as Fixed Overhead: Constant term b represents the unavoidable base fee before any usage.",
            "Two-Point Linear Determination: Two distinct data points (x1, y1) and (x2, y2) uniquely determine the parameters a and b."
        ],
        "success_criteria": "Student can determine linear equations from two data points and interpret slope and intercept in economic and physical contexts.",
        "chapter_notes": """### Step-by-Step Solver: Examples 9 to 11 & Exercises 2.4-2.5
Exhaustive calculations following Topper format with zero skipped steps.""",
        "worked_examples": [
            {
                "problem": "Textbook Example 9: The cost of a journey is given by C(d) = 100 + 60d, where C is cost in rupees and d is distance in km. Make a table of values for d = 0 to 5 km and explain why this is a linear pattern.",
                "given": "C(d) = 100 + 60d.",
                "formula": "Evaluate C(d) at integer values of d.",
                "substitution": "Substitute d = 0, 1, 2, 3, 4, 5.",
                "calculation": "1. d = 0: C(0) = 100 + 60(0) = Rs 100.\n2. d = 1: C(1) = 100 + 60(1) = Rs 160.\n3. d = 2: C(2) = 100 + 60(2) = Rs 220.\n4. d = 3: C(3) = 100 + 60(3) = Rs 280.\n5. d = 4: C(4) = 100 + 60(4) = Rs 340.\n6. d = 5: C(5) = 100 + 60(5) = Rs 400.\nAnalysis: As d increases by 1 km, the cost increases by a constant fixed amount of Rs 60. This constant rate of change defines a linear pattern.",
                "finalAnswer": "Costs for d = 0 to 5 km are Rs 100, 160, 220, 280, 340, 400. Constant rate of change = Rs 60/km.",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 10: The height of water in a cylindrical tank is 3 m at the start of summer. The height h(t) in metres at the end of t months is given by h(t) = 3 - 0.5t. Make a table of values for t = 0 to 4 months and determine when the tank is empty.",
                "given": "h(t) = 3 - 0.5t metres.",
                "formula": "Evaluate h(t) at t = 0, 1, 2, 3, 4. Empty tank occurs when h(t) = 0.",
                "substitution": "Substitute t = 0, 1, 2, 3, 4; set 3 - 0.5t = 0.",
                "calculation": "1. t = 0: h(0) = 3 - 0.5(0) = 3.0 m.\n2. t = 1: h(1) = 3 - 0.5(1) = 2.5 m.\n3. t = 2: h(2) = 3 - 0.5(2) = 2.0 m.\n4. t = 3: h(3) = 3 - 0.5(3) = 1.5 m.\n5. t = 4: h(4) = 3 - 0.5(4) = 1.0 m.\nStep 6: Determine when empty:\n3 - 0.5t = 0 => 0.5t = 3 => t = 3 / 0.5 = 6 months.",
                "finalAnswer": "Heights: 3.0m, 2.5m, 2.0m, 1.5m, 1.0m. Tank will be completely empty after 6 months.",
                "unit": "months",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.4 Q1: Suppose a plant has height 1.75 feet and it grows by 0.5 feet each month. (i) Find its height after 7 months. (ii) Make a table of values for t = 0 to 10 months. (iii) Find an expression relating h and t, and explain why it represents linear growth.",
                "given": "Initial height h0 = 1.75 ft. Growth rate = 0.5 ft/month.",
                "formula": "h(t) = h0 + rate * t = 1.75 + 0.5t.",
                "substitution": "h(t) = 1.75 + 0.5t. Evaluate at t = 7.",
                "calculation": "Step 1: Write height function:\nh(t) = 1.75 + 0.5t feet.\nStep 2: Evaluate for t = 7 months:\nh(7) = 1.75 + 0.5(7) = 1.75 + 3.5 = 5.25 feet.\nStep 3: Table of values (t = 0 to 4 shown):\nt=0: 1.75 ft; t=1: 2.25 ft; t=2: 2.75 ft; t=3: 3.25 ft; t=4: 3.75 ft; t=10: 1.75 + 5 = 6.75 ft.\nStep 4: Why linear:\nThe rate of growth is constant (0.5 ft/month) for every month. In the polynomial h(t) = 0.5t + 1.75, the variable t has degree 1.",
                "finalAnswer": "(i) Height after 7 months = 5.25 feet; (ii) Table values increase by 0.5 ft each month up to 6.75 ft at month 10; (iii) h(t) = 1.75 + 0.5t represents linear growth due to constant growth rate.",
                "unit": "feet",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 11: A telecom company charges a fixed monthly fee and an additional cost per GB of internet used. A student observes that using 10 GB costs Rs 350, and using 20 GB costs Rs 550. If y = ax + b, find the values of a and b.",
                "given": "Points (x1, y1) = (10, 350) and (x2, y2) = (20, 550). Linear model: y = ax + b.",
                "formula": "Slope a = (y2 - y1) / (x2 - x1). Intercept b = y1 - a*x1.",
                "substitution": "a = (550 - 350) / (20 - 10); b = 350 - a(10).",
                "calculation": "Step 1: Set up system of two linear equations:\nEquation 1: 350 = 10a + b\nEquation 2: 550 = 20a + b\n\nStep 2: Subtract Equation 1 from Equation 2:\n(20a + b) - (10a + b) = 550 - 350\n10a = 200\na = 200 / 10 = 20.\n(The cost per GB is Rs 20).\n\nStep 3: Substitute a = 20 into Equation 1 to find b:\n350 = 10(20) + b\n350 = 200 + b\nb = 350 - 200 = 150.\n(The fixed monthly fee is Rs 150).\n\nStep 4: Verification with second point (20, 550):\ny(20) = 20(20) + 150 = 400 + 150 = 550. Verified!",
                "finalAnswer": "a = 20 (Rs 20 per GB), b = 150 (Rs 150 fixed monthly fee). Equation: y = 20x + 150.",
                "unit": "rupees",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m5_svg
            },
            {
                "problem": "Exercise 2.5 Q1: A learning platform charges a fixed monthly fee and an additional cost per digital learning module accessed. A student observes that accessing 10 modules costs Rs 400, and accessing 14 modules costs Rs 500. If y = ax + b, find the values of a and b.",
                "given": "Points (10, 400) and (14, 500). Relation y = ax + b where x = modules, y = total bill.",
                "formula": "Slope a = (y2 - y1) / (x2 - x1). Intercept b = y1 - a*x1.",
                "substitution": "a = (500 - 400) / (14 - 10); b = 400 - a(10).",
                "calculation": "Step 1: Set up simultaneous equations:\nEquation 1: 10a + b = 400\nEquation 2: 14a + b = 500\n\nStep 2: Subtract Equation 1 from Equation 2:\n(14a + b) - (10a + b) = 500 - 400\n4a = 100\na = 100 / 4 = 25.\n(Cost per module = Rs 25).\n\nStep 3: Substitute a = 25 into Equation 1 to find b:\n10(25) + b = 400\n250 + b = 400\nb = 400 - 250 = 150.\n(Fixed monthly platform fee = Rs 150).\n\nStep 4: Verification with second point (14, 500):\ny(14) = 25(14) + 150 = 350 + 150 = 500. Verified!",
                "finalAnswer": "a = 25 (Rs 25 per module) and b = 150 (Rs 150 fixed fee). Relation: y = 25x + 150.",
                "unit": "rupees",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m5_svg
            }
        ],
        "common_misconceptions": [
            "Dividing total bill by total units directly without subtracting fixed overhead b first.",
            "Swapping slope a and intercept b in final formula."
        ],
        "ai_system_prompt_context": "SOCRATIC DIRECTIVE: Ask student: 'Why does dividing 400 by 10 give 40, but the actual cost per module is 25?' Emphasize fixed fee b.",
        "visual_lesson_plan": {
            "title": "Two-Point Rate Systems Visuals",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Two-point linear determination graph showing slope and intercept.",
            "concept_visuals": [
                {
                    "concept_title": "Two-Point Rate Systems",
                    "diagram_title": "Telecom & Platform Two-Point Solver",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m5_svg,
                    "interactive_math_formula": "y = 20x + 150",
                    "mafs_graph_config": {"domain": [-2, 25], "range": [-50, 650], "points": [[10, 350], [20, 550]], "lines": [{"formula": "20*x + 150"}]},
                    "image_query": "Two point line cartesian plane slope intercept",
                    "video_query": "Finding linear equation from two points animation",
                    "image_url": "/images/curriculum/ch2_two_point_systems.png",
                    "what_to_make": "Line passing through (10, 350) and (20, 550) meeting y-axis at (0, 150).",
                    "what_to_explain": "Show that the slope gives cost per unit and the y-intercept gives the fixed subscription fee.",
                    "timing_and_cue": "Introduce at 03:00 during Example 11 explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Two-Point Rate Systems",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "In the model y = 25x + 150, what does 150 represent?",
                            "ideal_answer": "The fixed monthly charge (overhead cost) incurred even if 0 modules are accessed.",
                            "socratic_hint": "What is the bill when x = 0?"
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Find the slope of the line passing through (2, 5) and (6, 17).",
                            "ideal_answer": "Slope a = (17 - 5) / (6 - 2) = 12 / 4 = 3.",
                            "socratic_hint": "Use the formula a = (y2 - y1) / (x2 - x1)."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Short Answer",
                            "question": "If electricity costs Rs 100 fixed plus Rs 8 per unit, what is the bill for 45 units?",
                            "ideal_answer": "Bill = 100 + 8(45) = 100 + 360 = Rs 460.",
                            "socratic_hint": "Substitute x = 45 into y = 8x + 100."
                        },
                        {
                            "q_num": "Q4",
                            "type": "3-mark Short Answer",
                            "question": "A line has slope 4 and passes through (3, 15). Find its y-intercept.",
                            "ideal_answer": "y = mx + c => 15 = 4(3) + c => 15 = 12 + c => c = 3. Point is (0, 3).",
                            "socratic_hint": "Substitute the point into y = mx + c and solve for c."
                        },
                        {
                            "q_num": "Q5",
                            "type": "2-mark Short Answer",
                            "question": "Why is the graph of a constant rate of change always a straight line?",
                            "ideal_answer": "Because the derivative/slope (delta y / delta x) is constant everywhere, meaning the angle of inclination never changes.",
                            "socratic_hint": "What geometric shape has a single constant steepness throughout?"
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 6: Textbook Exercise Solver 4: Graphing & End-of-Chapter
    # -------------------------------------------------------------
    m6_svg = build_cartesian_svg(
        domain=(-4, 6), range_y=(-6, 12),
        lines=[
            {"p1": (-2, -8), "p2": (2.5, 10), "color": "#2563EB", "stroke_width": 2, "label": "y = 4x"},
            {"p1": (-3, -6), "p2": (5, 10), "color": "#16A34A", "stroke_width": 2, "label": "y = 2x"},
            {"p1": (-4, -4), "p2": (6, 6), "color": "#D97706", "stroke_width": 2, "label": "y = x"},
            {"p1": (-2, -7), "p2": (3, 8), "color": "#7C3AED", "stroke_width": 1.8, "dash": "3,3", "label": "y = 3x - 1"},
            {"p1": (-2, -5), "p2": (3, 10), "color": "#7C3AED", "stroke_width": 1.8, "dash": "3,3", "label": "y = 3x + 1"},
        ],
        title="Family of Linear Graphs: Slopes & Parallel Shifts",
        caption="Textbook Examples 12-16 & Exercise 2.6: Comparing steepness (a) and vertical shifts (b)"
    )

    m6 = {
        "order_index": 6,
        "title": "Textbook Exercise Solver 4: Graphing Sets & End-of-Chapter Review (Q1 to Q10)",
        "description": "Complete step-by-step solutions for Textbook Graphing Examples 12-16, Exercise 2.6 sets (i)-(v), and all End-of-Chapter Exercises: role of parameters a and b, graphing parallel families, polynomial evaluations, and degree verification.",
        "subtopics": [
            "Graphing Examples 12-13: Lines through origin y = 3x and y = -2x",
            "Graphing Examples 14-15: Family of slopes y = x/2, x, 2x and reflection y = -x, -3x",
            "Graphing Example 16: Parallel lines y = 2x - 1, 2x + 1, 2x + 5",
            "Exercise 2.6 Sets (i)-(v): Plotting y = 4x, 2x, x; y = -6x, -3x, -x; y = 5x, -5x; parallel y = 3x - 1, 3x, 3x + 1",
            "End-of-Chapter Q1: Degree 3 polynomial with coefficient of x^2 equal to -7",
            "End-of-Chapter Q2: Values of polynomials: (i) 5x^2 - 3x + 7 at x = 1; (ii) 4t^3 - t^2 + 6 at t = a",
            "End-of-Chapter Review: Zeroes and algebraic invariants"
        ],
        "key_concepts": [
            "Slope Modulation: Increasing |a| rotates the line towards the vertical axis (steeper); decreasing |a| flattens the line towards the horizontal axis.",
            "Sign of Slope: Positive a slopes upward from left to right; negative a slopes downward from left to right.",
            "Intercept Shift: Changing b shifts the line vertically without altering its direction (parallel translation)."
        ],
        "success_criteria": "Student can sketch and explain any family of linear graphs and solve all end-of-chapter polynomial review questions.",
        "chapter_notes": """### Step-by-Step Solver: Graphing Sets & End-of-Chapter Review
Complete mathematical solutions following Topper guidelines.""",
        "worked_examples": [
            {
                "problem": "Textbook Examples 12 & 13: (Ex 12) Plot points (-1, -3), (0, 0), (1, 3), (3, 9), (4, 12). Guess the line equation. (Ex 13) Plot (-3, 6), (-2, 4), (0, 0), (1, -2), (2, -4), (3, -6). Guess the line equation.",
                "given": "Two sets of collinear points passing through origin (0, 0).",
                "formula": "Line through origin: y = mx where m = y / x for any point (x, y) != (0, 0).",
                "substitution": "Ex 12: m = 3 / 1 = 3. Ex 13: m = (-2) / 1 = -2.",
                "calculation": "Part Ex 12:\n1. For each point: 3/1 = 3; 9/3 = 3; 12/4 = 3; -3/-1 = 3.\n2. The ratio y / x is constantly 3.\n3. Therefore, the equation of the line is y = 3x.\n\nPart Ex 13:\n1. For each point: 6/-3 = -2; 4/-2 = -2; -2/1 = -2; -4/2 = -2; -6/3 = -2.\n2. The ratio y / x is constantly -2.\n3. Therefore, the equation of the line is y = -2x.",
                "finalAnswer": "Example 12 equation is y = 3x; Example 13 equation is y = -2x.",
                "unit": "dimensionless",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m6_svg
            },
            {
                "problem": "Exercise 2.6 Q1 (Sets i, iv, v): Draw the graphs and reflect on the roles of a and b: (i) y = 4x, y = 2x, y = x; (iv) y = 3x - 1, y = 3x, y = 3x + 1; (v) y = -2x - 3, y = -2x, y = 2x + 3.",
                "given": "Three families of linear equations.",
                "formula": "Standard form y = ax + b. Role of a: slope/steepness. Role of b: vertical translation/intercept.",
                "substitution": "Set (i): a = 4, 2, 1 with b = 0. Set (iv): a = 3 with b = -1, 0, 1. Set (v): a = -2, -2, +2.",
                "calculation": "Analysis for Set (i):\n1. All three lines have b = 0, so they all pass through the origin (0, 0).\n2. As coefficient a increases from 1 to 2 to 4, the lines become progressively STEEPER (closer to vertical y-axis).\n3. Conclusion: The parameter 'a' dictates the angle of inclination and steepness.\n\nAnalysis for Set (iv):\n1. All three lines have identical slope a = 3. Therefore, they are mutually PARALLEL.\n2. y = 3x passes through (0, 0); y = 3x + 1 is shifted 1 unit UPWARD (cuts y-axis at (0, 1)); y = 3x - 1 is shifted 1 unit DOWNWARD (cuts y-axis at (0, -1)).\n3. Conclusion: The parameter 'b' translates the line vertically without changing its slope.\n\nAnalysis for Set (v):\n1. y = -2x - 3 and y = -2x are parallel to each other (both slope -2, sloping downward).\n2. y = 2x + 3 has opposite slope (+2), so it slopes upward and intersects the other lines.",
                "finalAnswer": "Role of 'a': Controls steepness and orientation (positive upward, negative downward). Role of 'b': Controls vertical translation (parallel shift of the graph).",
                "unit": "dimensionless",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m6_svg
            },
            {
                "problem": "End-of-Chapter Q1: Write a polynomial of degree 3 in the variable x, in which the coefficient of the x^2 term is -7.",
                "given": "Degree must be 3, variable x, coefficient of x^2 must be -7.",
                "formula": "General form: P(x) = a3*x^3 + a2*x^2 + a1*x + a0 where a3 != 0 and a2 = -7.",
                "substitution": "Let a3 = 4, a2 = -7, a1 = 5, a0 = 2.",
                "calculation": "1. Degree 3 requires the highest power of x to be 3 with a non-zero coefficient (e.g. 4x^3 or x^3).\n2. The x^2 term must specifically be -7x^2.\n3. Other terms (x and constant) can be any real numbers.\n4. Example polynomial: P(x) = 4x^3 - 7x^2 + 5x - 1.\n5. Another valid example: P(x) = x^3 - 7x^2 + 2.",
                "finalAnswer": "Example polynomial: P(x) = 4x^3 - 7x^2 + 5x - 1 (or any polynomial where highest power is 3 and x^2 coefficient is -7).",
                "unit": "dimensionless",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2: Find the values of the following polynomials at the indicated values of the variables: (i) P(x) = 5x^2 - 3x + 7 if x = 1; (ii) Q(t) = 4t^3 - t^2 + 6 if t = a.",
                "given": "(i) P(x) = 5x^2 - 3x + 7 at x = 1; (ii) Q(t) = 4t^3 - t^2 + 6 at t = a.",
                "formula": "Direct variable substitution.",
                "substitution": "(i) Substitute x = 1 into P(x); (ii) Substitute t = a into Q(t).",
                "calculation": "Part (i):\nP(1) = 5(1)^2 - 3(1) + 7\n= 5(1) - 3 + 7 = 5 - 3 + 7 = 2 + 7 = 9.\n\nPart (ii):\nQ(a) = 4(a)^3 - (a)^2 + 6\n= 4a^3 - a^2 + 6.",
                "finalAnswer": "(i) P(1) = 9; (ii) Q(a) = 4a^3 - a^2 + 6.",
                "unit": "dimensionless",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Believing that changing b changes the angle of the line (it ONLY translates the line vertically).",
            "Assuming that a higher slope means a line with negative values cannot be steep (steepness is determined by |a|, the absolute value)."
        ],
        "ai_system_prompt_context": "CHALKBOARD DIRECTIVE: Call write_chalkboard(action='draw_svg_diagram', content='Family of Linear Graphs: Slopes & Parallel Shifts'). Emphasize how a and b control geometry.",
        "visual_lesson_plan": {
            "title": "Family of Linear Graphs Visuals",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Multi-line graph showing varying slopes a and parallel translations b.",
            "concept_visuals": [
                {
                    "concept_title": "Slope and Intercept Modulation",
                    "diagram_title": "Family of Linear Graphs",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m6_svg,
                    "interactive_math_formula": "y = ax + b",
                    "mafs_graph_config": {"domain": [-4, 6], "range": [-6, 12], "lines": [{"formula": "4*x"}, {"formula": "2*x"}, {"formula": "1*x"}]},
                    "image_query": "Family of linear functions cartesian plane",
                    "video_query": "Effect of slope and intercept on linear graphs animation",
                    "image_url": "/images/curriculum/ch2_family_of_lines.png",
                    "what_to_make": "Set of lines intersecting at origin and set of parallel lines with vertical offsets.",
                    "what_to_explain": "Show that changing a rotates the line, and changing b shifts the line up/down.",
                    "timing_and_cue": "Introduce at 03:00 during graphing explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Slope and Intercept Modulation",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "Which of the following lines is parallel to y = 5x - 3?",
                            "ideal_answer": "y = 5x + 9, because both have the identical slope m = 5.",
                            "socratic_hint": "Look for the equation that has the exact same coefficient of x."
                        },
                        {
                            "q_num": "Q2",
                            "type": "1-mark MCQ",
                            "question": "Which line is steeper: y = 2x or y = 7x?",
                            "ideal_answer": "y = 7x, because |7| > |2|, meaning it rises 7 units vertically for every 1 unit horizontally.",
                            "socratic_hint": "Which line has a larger rate of change?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Short Answer",
                            "question": "What is the angle of inclination of a line with negative slope?",
                            "ideal_answer": "It forms an obtuse angle (> 90 degrees) with the positive direction of the x-axis.",
                            "socratic_hint": "Think about whether the line points downward as you move from left to right."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Short Answer",
                            "question": "Find the point where the line y = 3x - 12 intersects the x-axis.",
                            "ideal_answer": "Set y = 0 => 3x - 12 = 0 => 3x = 12 => x = 4. The point is (4, 0).",
                            "socratic_hint": "What is the value of y at the x-intercept?"
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Short Answer",
                            "question": "Explain the geometric transformation between the graphs of y = 2x and y = 2x + 5.",
                            "ideal_answer": "The graph of y = 2x + 5 is a rigid vertical translation (shift) of the graph of y = 2x by exactly 5 units upward along the y-axis.",
                            "socratic_hint": "How does adding a constant to an equation shift its graph?"
                        }
                    ]
                }
            ]
        }
    }

    return [m1, m2, m3, m4, m5, m6]
