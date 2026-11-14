"""
Chapter 2: Introduction to Linear Polynomials - Module 6
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m6():
    m6_svg = build_cartesian_svg(
        domain=(-6, 6), range_y=(-6, 8),
        points=[
            {"x": 0, "y": 0, "label": "Origin (0, 0)", "color": "#0F172A", "sub": "(0, 0)"},
            {"x": 0, "y": 5, "label": "Intercept (0, 5)", "color": "#2563EB", "sub": "(0, 5)"},
            {"x": 0, "y": 1, "label": "Intercept (0, 1)", "color": "#059669", "sub": "(0, 1)"},
            {"x": 0, "y": -1, "label": "Intercept (0, -1)", "color": "#D97706", "sub": "(0, -1)"}
        ],
        lines=[
            {"p1": (-3, -7), "p2": (2, 3), "color": "#D97706", "stroke_width": 2, "label": "y = 2x - 1"},
            {"p1": (-3, -5), "p2": (3, 7), "color": "#059669", "stroke_width": 2, "label": "y = 2x + 1"},
            {"p1": (-5, -5), "p2": (1, 7), "color": "#2563EB", "stroke_width": 2, "label": "y = 2x + 5"}
        ],
        title="Parallel Family of Lines with Identical Slope a = 2",
        caption="Lines y = 2x + b for b = -1, 1, 5 demonstrating equal inclination and varying y-intercepts"
    )

    return {
        "order_index": 6,
        "title": "Textbook Exercise Solver 4: Linear Graphing, Slope-Intercept Invariance & Comprehensive Chapter Challenges (Exercise 2.6 & End-of-Chapter Complete)",
        "description": "Comprehensive step-by-step solutions to in-text Examples 14 to 16, Exercise 2.6, and all End-of-Chapter Questions 1 through 14. Master graphing families of lines y = ax, varying slope and intercept, word problems with digits and savings, work-distance modeling, and parallel polynomial functions.",
        "subtopics": [
            "Graphing families of lines y = ax through origin with varying positive and negative slopes",
            "Geometric meaning of slope a and y-intercept b in y = ax + b",
            "Parallelism condition: identical slope a with distinct y-intercepts b",
            "Exhaustive solutions to Exercise 2.6 Q1 (parts i through v)",
            "Step-by-step algebraic modeling for End-of-Chapter Questions 1 to 14 (digits, matchstick patterns, work-force, Kelvin-Fahrenheit, polynomial identification)"
        ],
        "key_concepts": [
            "Slope-Intercept Invariance: In y = ax + b, a governs the rate of rise (steepness/direction) and b sets the vertical translation (cutting the y-axis at (0, b)).",
            "Origin Line Invariance: When b = 0, y = ax always passes through the origin (0, 0); positive a slopes upward, negative a slopes downward.",
            "Parallel Lines Invariance: Two straight lines are parallel if and only if they possess identical slopes a1 = a2 with different intercepts b1 != b2.",
            "Two-Digit Reversal Invariance: An integer 10t + u reversed is 10u + t; their sum is always a multiple of 11: 11(t + u).",
            "Matchstick Geometric Progression: Hexagons sharing one common edge require 6 + 5(n - 1) = 5n + 1 matchsticks for n stages."
        ],
        "success_criteria": "Students can sketch any linear equation y = ax + b, identify slope and y-intercept by inspection, test for parallelism, and solve authentic word problems without skipping algebraic steps.",
        "chapter_notes": "Module 6 completes Chapter 2 by resolving every single problem from Exercise 2.6 and End-of-Chapter exercises with rigorous given, formula, substitution, calculation, and boxed final answers.",
        "common_misconceptions": [
            {"misconception": "Confusing slope with y-intercept", "clarification": "In y = ax + b, the multiplier of x is always the slope a (steepness), while the constant b is the point on the y-axis (0, b)."},
            {"misconception": "Believing parallel lines have equal intercepts", "clarification": "Parallel lines have equal slopes (a1 = a2), but must have different intercepts (b1 != b2); identical intercepts make them the exact same line."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through the complete Exercise 2.6 and End-of-Chapter problem sets. Draw clear coordinate axes on the digital chalkboard, highlighting slope 'a' as vertical rise per unit run and 'b' as the y-axis intercept.",
        "visual_lesson_plan": {
            "title": "Visualizing Linear Families, Parallel Lines & Word Models",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Interactive coordinate grid illustrating the family of parallel lines y = 2x - 1, y = 2x + 1, and y = 2x + 5.",
            "concept_visuals": [
                {
                    "concept_title": "Family of Direct Proportion Lines (y = ax, a > 0)",
                    "diagram_title": "Interactive Slopes y = 0.5x, x, 2x, 4x",
                    "interactive_math_formula": "y = ax",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "0.5*x", "color": "#9333EA", "label": "y = 0.5x"},
                            {"fn": "x", "color": "#2563EB", "label": "y = x"},
                            {"fn": "2*x", "color": "#059669", "label": "y = 2x"},
                            {"fn": "4*x", "color": "#DC2626", "label": "y = 4x"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 1, "y": 1, "label": "(1, 1)"},
                            {"x": 1, "y": 2, "label": "(1, 2)"},
                            {"x": 1, "y": 4, "label": "(1, 4)"}
                        ]
                    },
                    "image_query": "family of lines passing through origin varying slope graph",
                    "video_query": "how slope affects line steepness linear equation",
                    "what_to_explain": "As the coefficient a increases from 0.5 to 4, the line rotates counter-clockwise towards the y-axis, becoming steeper while anchoring at the origin (0, 0)."
                },
                {
                    "concept_title": "Family of Negative Slope Lines (y = -ax, a > 0)",
                    "diagram_title": "Downward Lines y = -x, -3x, -6x",
                    "interactive_math_formula": "y = -ax",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-6, 6],
                        "curves": [
                            {"fn": "-1*x", "color": "#2563EB", "label": "y = -x"},
                            {"fn": "-3*x", "color": "#D97706", "label": "y = -3x"},
                            {"fn": "-6*x", "color": "#DC2626", "label": "y = -6x"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 1, "y": -1, "label": "(1, -1)"},
                            {"x": 1, "y": -3, "label": "(1, -3)"},
                            {"x": -1, "y": 3, "label": "(-1, 3)"}
                        ]
                    },
                    "image_query": "negative slope lines coordinate plane graph",
                    "video_query": "negative slope straight lines linear graphs",
                    "what_to_explain": "Lines with negative slopes slant downwards from top-left to bottom-right, representing decay or decreasing rates."
                },
                {
                    "concept_title": "Parallel Lines via y-Intercept Translation: y = 2x + b",
                    "diagram_title": "Parallel Bundle y = 2x - 1, 2x + 1, 2x + 5",
                    "interactive_math_formula": "y = 2x + b",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-4, 8],
                        "curves": [
                            {"fn": "2*x - 1", "color": "#D97706", "label": "y = 2x - 1"},
                            {"fn": "2*x + 1", "color": "#059669", "label": "y = 2x + 1"},
                            {"fn": "2*x + 5", "color": "#2563EB", "label": "y = 2x + 5"}
                        ],
                        "points": [
                            {"x": 0, "y": -1, "label": "(0, -1)"},
                            {"x": 0, "y": 1, "label": "(0, 1)"},
                            {"x": 0, "y": 5, "label": "(0, 5)"}
                        ]
                    },
                    "image_query": "parallel lines same slope different y intercepts graph",
                    "video_query": "parallel lines slope intercept form algebra",
                    "what_to_explain": "All three lines have identical slope 2, ensuring they remain equidistant and never intersect. The parameter b shifts the line vertically."
                },
                {
                    "concept_title": "Axis Intercepts of General Linear Equations",
                    "diagram_title": "Intercepts of y = x + 3, 2x + 5, 3x - 2",
                    "interactive_math_formula": "y = ax + b",
                    "mafs_graph_config": {
                        "domain": [-6, 6],
                        "range": [-4, 8],
                        "curves": [
                            {"fn": "x + 3", "color": "#2563EB", "label": "y = x + 3"},
                            {"fn": "2*x + 5", "color": "#059669", "label": "y = 2x + 5"},
                            {"fn": "3*x - 2", "color": "#DC2626", "label": "y = 3x - 2"}
                        ],
                        "points": [
                            {"x": 0, "y": 3, "label": "(0, 3)"},
                            {"x": 0, "y": 5, "label": "(0, 5)"},
                            {"x": 0, "y": -2, "label": "(0, -2)"},
                            {"x": -3, "y": 0, "label": "(-3, 0)"}
                        ]
                    },
                    "image_query": "linear equations cutting x and y axes intercepts graph",
                    "video_query": "x and y intercepts of linear equations step by step",
                    "what_to_explain": "Setting x = 0 reveals the y-intercept (0, b), while setting y = 0 reveals the root or x-intercept (-b/a, 0)."
                },
                {
                    "concept_title": "Physical Modeling: Work Done vs Distance (W = 3d)",
                    "diagram_title": "Work Line W = 3d",
                    "interactive_math_formula": "W = 3d",
                    "mafs_graph_config": {
                        "domain": [0, 5],
                        "range": [0, 15],
                        "curves": [
                            {"fn": "3*x", "color": "#2563EB", "label": "W = 3d"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "O(0, 0)"},
                            {"x": 1, "y": 3, "label": "(1, 3)"},
                            {"x": 2, "y": 6, "label": "(2, 6)"},
                            {"x": 3, "y": 9, "label": "(3, 9)"}
                        ]
                    },
                    "image_query": "work force distance direct proportionality linear graph",
                    "video_query": "work done force distance physics linear graph",
                    "what_to_explain": "Under a constant force of 3 units, work is directly proportional to distance. At distance 2 units, the work done is exactly 6 units."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Parallel Lines Slope Invariant",
                    "questions": [
                        {
                            "question": "What mathematical property guarantees that two lines y = a1*x + b1 and y = a2*x + b2 are parallel?",
                            "type": "short_answer",
                            "ideal_answer": "They are parallel if and only if their slopes are equal (a1 = a2) and their y-intercepts are distinct (b1 != b2).",
                            "socratic_hint": "Think about the angle of inclination of the two lines relative to the x-axis."
                        },
                        {
                            "question": "If a line y = ax + b passes through the origin (0, 0), what must be the value of b?",
                            "type": "short_answer",
                            "ideal_answer": "b must equal 0, giving the direct proportion form y = ax.",
                            "socratic_hint": "Substitute x = 0 and y = 0 into y = ax + b."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Textbook Example 14: Draw the graphs of y = (1/2)x, y = x, and y = 2x by selecting suitable points on these lines.",
                "given": "Three linear equations: y = 0.5x, y = x, y = 2x.",
                "formula": "To plot y = ax, find at least two points (x, y) satisfying the equation and join them with a straight line through origin (0, 0).",
                "substitution": "For y = 0.5x: (0, 0) and (4, 2). For y = x: (0, 0) and (2, 2). For y = 2x: (0, 0) and (2, 4).",
                "calculation": "1. All three lines pass through (0, 0) since when x = 0, y = a(0) = 0.\n2. When x = 4, y = 0.5(4) = 2, giving (4, 2).\n3. When x = 2, y = 1(2) = 2, giving (2, 2).\n4. When x = 2, y = 2(2) = 4, giving (2, 4).\n5. Comparing steepness: y = 2x is steepest, y = x has slope 1 (45° angle), and y = 0.5x is least steep.",
                "finalAnswer": "All three lines are straight lines passing through the origin (0, 0). The line y = 2x has the greatest slope (steepest), followed by y = x, and y = 0.5x is the least steep.",
                "unit": "linear graphs",
                "has_diagram": True
            },
            {
                "problem": "Textbook Example 15: Draw the graphs of y = (-1/3)x, y = -x, and y = -3x by selecting suitable points.",
                "given": "Three linear equations with negative slopes: y = -x/3, y = -x, y = -3x.",
                "formula": "Equation y = -ax has slope -a. Plot (0, 0) and one other point (x, y).",
                "substitution": "For y = -x/3: (0, 0) and (3, -1). For y = -x: (0, 0) and (2, -2). For y = -3x: (0, 0) and (1, -3).",
                "calculation": "1. For y = -x/3, at x = 3, y = -3/3 = -1.\n2. For y = -x, at x = 2, y = -2.\n3. For y = -3x, at x = 1, y = -3(1) = -3.\n4. All lines pass through origin (0, 0) and tilt downwards from left to right (negative slope). As |a| increases, the line becomes steeper towards the y-axis.",
                "finalAnswer": "The graphs are straight lines passing through (0, 0) in the 2nd and 4th quadrants. y = -3x is the steepest downward line, followed by y = -x, and y = -x/3 is the flattest.",
                "unit": "linear graphs",
                "has_diagram": True
            },
            {
                "problem": "Textbook Example 16: Draw the graphs of y = 2x - 1, y = 2x + 1, and y = 2x + 5 on the same coordinate axes and compare them.",
                "given": "Equations y = 2x - 1, y = 2x + 1, y = 2x + 5.",
                "formula": "In y = ax + b, slope is a and y-intercept is b at point (0, b). If slope a is identical, lines are parallel.",
                "substitution": "Slope a = 2 for all three lines. Intercepts: b1 = -1, b2 = 1, b3 = 5.",
                "calculation": "1. For y = 2x - 1: x = 0 gives y = -1; x = 1 gives y = 1. Points: (0, -1), (1, 1).\n2. For y = 2x + 1: x = 0 gives y = 1; x = 1 gives y = 3. Points: (0, 1), (1, 3).\n3. For y = 2x + 5: x = 0 gives y = 5; x = 1 gives y = 7. Points: (0, 5), (1, 7).\n4. Since slope a = 2 is identical for all three, the lines have identical direction and angle of inclination. They are strictly parallel lines separated by vertical shifts.",
                "finalAnswer": "The three lines are mutually parallel straight lines with slope 2, cutting the y-axis at (0, -1), (0, 1), and (0, 5) respectively.",
                "unit": "parallel lines",
                "has_diagram": True
            },
            {
                "problem": "Exercise 2.6 Q1 (i): Draw the graphs of y = 4x, y = 2x, y = x and reflect on the role of 'a' and 'b'.",
                "given": "Lines y = 4x, y = 2x, y = x.",
                "formula": "In y = ax + b, intercept b = 0 implies all lines pass through origin (0, 0). Slope a indicates steepness.",
                "substitution": "a1 = 4, a2 = 2, a3 = 1, with b = 0 for all.",
                "calculation": "1. Point on y = 4x: (1, 4).\n2. Point on y = 2x: (1, 2).\n3. Point on y = x: (1, 1).\n4. Reflection: Since b = 0, every line passes through (0, 0). As a increases from 1 to 4, the slope increases and the line rotates counterclockwise, becoming steeper.",
                "finalAnswer": "All three lines pass through (0, 0). The role of 'a' is the slope (steepness): greater 'a' yields a steeper line. Here b = 0, so the y-intercept is 0.",
                "unit": "slope reflection",
                "has_diagram": True
            },
            {
                "problem": "Exercise 2.6 Q1 (ii): Draw the graphs of y = -6x, y = -3x, y = -x and reflect on the role of 'a' and 'b'.",
                "given": "Lines y = -6x, y = -3x, y = -x.",
                "formula": "y = ax + b with negative slope a < 0 and intercept b = 0.",
                "substitution": "a = -6, -3, -1 and b = 0.",
                "calculation": "1. Point on y = -6x: (1, -6).\n2. Point on y = -3x: (1, -3).\n3. Point on y = -x: (1, -1).\n4. Reflection: Since b = 0, all pass through (0, 0). The negative slopes mean lines trend downwards from left to right. As the magnitude |a| increases from 1 to 6, the line gets closer to the y-axis (steeper negative gradient).",
                "finalAnswer": "Lines pass through the origin (0, 0). Negative 'a' indicates downward slope; larger magnitude |a| produces a steeper downward line.",
                "unit": "slope reflection",
                "has_diagram": True
            },
            {
                "problem": "Exercise 2.6 Q1 (iii): Draw the graphs of y = 5x and y = -5x and reflect on the role of 'a' and 'b'.",
                "given": "Lines y = 5x and y = -5x.",
                "formula": "Symmetric slopes a = 5 and a = -5 with intercept b = 0.",
                "substitution": "Points: (1, 5) on y = 5x; (1, -5) on y = -5x.",
                "calculation": "1. Both lines pass through (0, 0).\n2. y = 5x rises rapidly in Quadrants 1 and 3.\n3. y = -5x falls rapidly in Quadrants 2 and 4.\n4. Reflection: The two lines are mirror reflections of each other across both the x-axis and y-axis. The parameter 'a' determines direction: positive gives upward growth, negative gives downward decay.",
                "finalAnswer": "Lines y = 5x and y = -5x pass through (0, 0) and are symmetrical reflections of each other across the coordinate axes.",
                "unit": "slope reflection",
                "has_diagram": True
            },
            {
                "problem": "Exercise 2.6 Q1 (iv): Draw the graphs of y = 3x - 1, y = 3x, and y = 3x + 1 and reflect on the role of 'a' and 'b'.",
                "given": "Lines y = 3x - 1, y = 3x, y = 3x + 1.",
                "formula": "y = ax + b where slope a = 3 is identical and y-intercept b takes values -1, 0, 1.",
                "substitution": "a = 3 for all lines; b = -1, 0, 1.",
                "calculation": "1. Points for y = 3x - 1: (0, -1), (1, 2).\n2. Points for y = 3x: (0, 0), (1, 3).\n3. Points for y = 3x + 1: (0, 1), (1, 4).\n4. Reflection: Equal slopes (a = 3) mean the lines are parallel. The parameter 'b' vertically translates the line: b = 1 shifts the line up by 1 unit, b = -1 shifts it down by 1 unit.",
                "finalAnswer": "The lines are strictly parallel with identical slope 3. The parameter 'b' represents the vertical shift or y-intercept.",
                "unit": "parallel lines",
                "has_diagram": True
            },
            {
                "problem": "Exercise 2.6 Q1 (v): Draw the graphs of y = -2x - 3, y = -2x, and y = 2x + 3 and reflect on the role of 'a' and 'b'.",
                "given": "Lines y = -2x - 3, y = -2x, y = 2x + 3.",
                "formula": "Compare slopes a and intercepts b.",
                "substitution": "Line 1: a = -2, b = -3. Line 2: a = -2, b = 0. Line 3: a = 2, b = 3.",
                "calculation": "1. Line 1 (y = -2x - 3) and Line 2 (y = -2x) have identical slope a = -2, so they are parallel to each other.\n2. Line 3 (y = 2x + 3) has slope a = 2, which is positive, so it intersects both Line 1 and Line 2.\n3. Reflection: Identical slope produces parallel lines. Opposite signs of slope produce lines that slant in opposite directions.",
                "finalAnswer": "y = -2x - 3 and y = -2x are parallel lines (slope -2). y = 2x + 3 has positive slope +2 and intersects the other two lines.",
                "unit": "slope reflection",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q1: Write a polynomial of degree 3 in the variable x, in which the coefficient of the x^2 term is -7.",
                "given": "Degree = 3, variable = x, coefficient of x^2 is -7.",
                "formula": "General cubic polynomial: p(x) = ax^3 + bx^2 + cx + d where a != 0 and b = -7.",
                "substitution": "Let a = 1, b = -7, c = 2, d = 5.",
                "calculation": "1. Highest power of x must be 3, so a != 0.\n2. Coefficient of x^2 must be exactly -7.\n3. A valid example is p(x) = x^3 - 7x^2 + 2x + 5.",
                "finalAnswer": "p(x) = x^3 - 7x^2 + 2x + 5 (or any cubic polynomial with -7x^2).",
                "unit": "polynomial",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (i): Find the value of p(x) = 5x^2 - 3x + 7 if x = 1.",
                "given": "p(x) = 5x^2 - 3x + 7, x = 1.",
                "formula": "p(1) = 5(1)^2 - 3(1) + 7.",
                "substitution": "Substitute x = 1 into p(x).",
                "calculation": "1. 5(1)^2 = 5(1) = 5.\n2. -3(1) = -3.\n3. p(1) = 5 - 3 + 7 = 2 + 7 = 9.",
                "finalAnswer": "9",
                "unit": "numerical value",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2 (ii): Find the value of p(t) = 4t^3 - t^2 + 6 if t = a.",
                "given": "p(t) = 4t^3 - t^2 + 6, t = a.",
                "formula": "Substitute t = a into the polynomial expression.",
                "substitution": "p(a) = 4(a)^3 - (a)^2 + 6.",
                "calculation": "1. Replace every occurrence of variable t with symbol a.\n2. 4(a)^3 - (a)^2 + 6 = 4a^3 - a^2 + 6.",
                "finalAnswer": "4a^3 - a^2 + 6",
                "unit": "algebraic expression",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3: If we multiply a number by 5/2 and add 2/3 to the product, we get -7/12. Find the number.",
                "given": "(5/2)x + 2/3 = -7/12.",
                "formula": "Linear equation: ax + b = c => ax = c - b => x = (c - b) / a.",
                "substitution": "(5/2)x = -7/12 - 2/3.",
                "calculation": "1. Make common denominator for RHS: 2/3 = 8/12.\n2. RHS = -7/12 - 8/12 = -15/12 = -5/4.\n3. (5/2)x = -5/4.\n4. Multiply both sides by 2/5: x = (-5/4) * (2/5) = -2/4 = -1/2.",
                "finalAnswer": "-1/2",
                "unit": "rational number",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4: A positive number is 5 times another number. If 21 is added to both the numbers, then one of the new numbers becomes twice the other new number. What are the numbers?",
                "given": "Let smaller number be x, then larger number is 5x. When 21 is added: 5x + 21 and x + 21.",
                "formula": "Condition: 5x + 21 = 2(x + 21).",
                "substitution": "5x + 21 = 2x + 42.",
                "calculation": "1. Subtract 2x from both sides: 5x - 2x + 21 = 42 => 3x + 21 = 42.\n2. Subtract 21: 3x = 21.\n3. Divide by 3: x = 7.\n4. The other number is 5x = 5(7) = 35.\n5. Verification: 35 + 21 = 56; 7 + 21 = 28; 56 = 2 * 28. Correct!",
                "finalAnswer": "7 and 35",
                "unit": "numbers",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q5 (i): If you have Rs 800 and you save Rs 250 every month, express this as a linear pattern and find the amount you have after 6 months.",
                "given": "Initial amount b = 800, monthly addition a = 250.",
                "formula": "Linear relationship: A(m) = 250m + 800, where m is months.",
                "substitution": "Substitute m = 6: A(6) = 250(6) + 800.",
                "calculation": "1. 250 * 6 = 1500.\n2. 1500 + 800 = 2300.",
                "finalAnswer": "Rs 2300 (Pattern: A = 250m + 800)",
                "unit": "Rs",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q5 (ii): Find the amount you have after 2 years.",
                "given": "Pattern A(m) = 250m + 800, time = 2 years = 24 months.",
                "formula": "A(24) = 250(24) + 800.",
                "substitution": "m = 24.",
                "calculation": "1. 250 * 24 = 6000.\n2. 6000 + 800 = 6800.",
                "finalAnswer": "Rs 6800",
                "unit": "Rs",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q6: The digits of a two-digit number differ by 3. If the digits are interchanged, and the resulting number is added to the original number, we get 143. Find both numbers.",
                "given": "Let tens digit be t and units digit be u. Digits differ by 3: |t - u| = 3. Sum of number and reversed number is 143.",
                "formula": "Original number N = 10t + u. Reversed number R = 10u + t. Sum N + R = 11(t + u).",
                "substitution": "11(t + u) = 143 => t + u = 13.",
                "calculation": "1. From sum: t + u = 13.\n2. Case 1: t - u = 3.\n   Adding: 2t = 16 => t = 8 => u = 13 - 8 = 5. Number = 85.\n   Reversed = 58. Sum = 85 + 58 = 143.\n3. Case 2: u - t = 3.\n   Adding: 2u = 16 => u = 8 => t = 5. Number = 58.\n   Reversed = 85. Sum = 58 + 85 = 143.",
                "finalAnswer": "85 or 58",
                "unit": "two-digit numbers",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q7 (i): Draw the graph of y = -3x + 4, identify its slope and y-intercept, and find where it cuts the y-axis.",
                "given": "Equation: y = -3x + 4.",
                "formula": "In y = ax + b, slope = a, y-intercept = b, y-intercept point = (0, b).",
                "substitution": "a = -3, b = 4.",
                "calculation": "1. Compare with y = ax + b: slope a = -3, y-intercept b = 4.\n2. Setting x = 0 gives y = 4, so line cuts y-axis at (0, 4).\n3. Setting y = 0 gives -3x + 4 = 0 => x = 4/3, cutting x-axis at (4/3, 0).",
                "finalAnswer": "Slope = -3, y-intercept = 4, cuts y-axis at (0, 4).",
                "unit": "slope and intercept",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q7 (ii): Draw the graph of 2y = 4x + 7, identify its slope and y-intercept, and find where it cuts the y-axis.",
                "given": "Equation: 2y = 4x + 7.",
                "formula": "Divide by 2 to write in slope-intercept form: y = ax + b.",
                "substitution": "y = (4/2)x + 7/2 = 2x + 3.5.",
                "calculation": "1. Slope a = 2.\n2. y-intercept b = 7/2 = 3.5.\n3. Setting x = 0 gives y = 7/2, so line cuts y-axis at (0, 7/2) or (0, 3.5).",
                "finalAnswer": "Slope = 2, y-intercept = 7/2 (or 3.5), cuts y-axis at (0, 7/2).",
                "unit": "slope and intercept",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q7 (iii): Draw the graph of 5y = 6x - 10, identify its slope and y-intercept, and find where it cuts the y-axis.",
                "given": "Equation: 5y = 6x - 10.",
                "formula": "Divide by 5 to get y = (6/5)x - 2.",
                "substitution": "Slope a = 6/5 = 1.2, intercept b = -2.",
                "calculation": "1. Slope a = 6/5.\n2. y-intercept b = -10/5 = -2.\n3. Point of intersection with y-axis: (0, -2).",
                "finalAnswer": "Slope = 6/5, y-intercept = -2, cuts y-axis at (0, -2).",
                "unit": "slope and intercept",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q7 (iv): Draw the graph of 3y = 6x - 11, identify slope and y-intercept, find where it cuts y-axis, and state if any of the lines in Q7 are parallel.",
                "given": "3y = 6x - 11.",
                "formula": "y = (6/3)x - 11/3 = 2x - 11/3.",
                "substitution": "Slope a = 2, intercept b = -11/3.",
                "calculation": "1. Slope a = 2, y-intercept b = -11/3.\n2. Cuts y-axis at (0, -11/3).\n3. Comparing all slopes from Q7:\n   (i) slope = -3\n   (ii) slope = 2\n   (iii) slope = 6/5\n   (iv) slope = 2.\n4. Lines (ii) and (iv) both have slope 2, but different y-intercepts (7/2 vs -11/3). Therefore, lines (ii) and (iv) are parallel to each other.",
                "finalAnswer": "Slope = 2, y-intercept = -11/3, cuts y-axis at (0, -11/3). Lines (ii) and (iv) are parallel because both have slope a = 2.",
                "unit": "parallelism",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q8 (i): The relation between Kelvin (x K) and Fahrenheit (y °F) is y = (9/5)(x - 273) + 32. Find Fahrenheit temperature if x = 313 K.",
                "given": "y = (9/5)(x - 273) + 32, x = 313 K.",
                "formula": "Substitute x = 313 into the linear conversion formula.",
                "substitution": "y = (9/5)(313 - 273) + 32.",
                "calculation": "1. 313 - 273 = 40.\n2. (9/5) * 40 = 9 * 8 = 72.\n3. y = 72 + 32 = 104 °F.",
                "finalAnswer": "104 °F",
                "unit": "°F",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q8 (ii): If the temperature is 158 °F, find the temperature in Kelvin.",
                "given": "y = 158 °F, equation: y = (9/5)(x - 273) + 32.",
                "formula": "158 - 32 = (9/5)(x - 273) => x - 273 = (5/9) * 126.",
                "substitution": "126 * 5 / 9 = 14 * 5 = 70.",
                "calculation": "1. 158 - 32 = 126.\n2. 126 / 9 = 14.\n3. 14 * 5 = 70.\n4. x - 273 = 70 => x = 273 + 70 = 343 K.",
                "finalAnswer": "343 K",
                "unit": "K",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q9: Constant force = 3 units. Express work w and distance d as a linear equation, draw its graph, and find work done when distance is 2 units.",
                "given": "Constant force F = 3 units, Work = Force * Distance.",
                "formula": "w = 3d.",
                "substitution": "For d = 2: w = 3(2).",
                "calculation": "1. Linear equation: w = 3d.\n2. At d = 0, w = 0 (origin).\n3. At d = 1, w = 3.\n4. At d = 2, w = 3 * 2 = 6 units.\n5. On the coordinate graph with d on horizontal axis and w on vertical axis, the point (2, 6) lies directly on the straight line w = 3d.",
                "finalAnswer": "Equation: w = 3d. Work done for distance 2 units is 6 units.",
                "unit": "work units",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q10: A linear polynomial p(x) passes through (1, 5) and (3, 11). (i) Find p(x). (ii) Find where it cuts axes. (iii) Verify graphically.",
                "given": "Points (1, 5) and (3, 11) lie on p(x) = ax + b.",
                "formula": "Slope a = (y2 - y1) / (x2 - x1); b = y1 - a*x1.",
                "substitution": "a = (11 - 5) / (3 - 1) = 6 / 2 = 3. b = 5 - 3(1) = 2.",
                "calculation": "1. Slope a = 3, so p(x) = 3x + 2.\n2. y-intercept: At x = 0, y = 2, so it cuts y-axis at (0, 2).\n3. x-intercept: At y = 0, 3x + 2 = 0 => x = -2/3, so it cuts x-axis at (-2/3, 0).\n4. Verification: p(1) = 3(1) + 2 = 5; p(3) = 3(3) + 2 = 11. Points match.",
                "finalAnswer": "p(x) = 3x + 2; cuts y-axis at (0, 2) and x-axis at (-2/3, 0).",
                "unit": "linear polynomial",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q11: Let p(x) = ax + b and q(x) = cx + d be linear polynomials such that: (i) p(0) = 5; (ii) p(x) - q(x) cuts x-axis at (3, 0); (iii) p(x) + q(x) = 6x + 4. Find p(x) and q(x).",
                "given": "p(0) = 5 => b = 5. p(x) + q(x) = (a + c)x + (b + d) = 6x + 4. [p(x) - q(x)] at x = 3 is 0.",
                "formula": "Compare coefficients of p(x) + q(x) and use root of p(x) - q(x).",
                "substitution": "b = 5. Since b + d = 4 => d = 4 - 5 = -1. a + c = 6 => c = 6 - a.",
                "calculation": "1. p(0) = a(0) + b = 5 => b = 5.\n2. p(x) + q(x) = (a + c)x + (b + d) = 6x + 4 for all x.\n   Therefore, a + c = 6 and b + d = 4.\n   Since b = 5, d = 4 - 5 = -1.\n3. Difference: p(x) - q(x) = (a - c)x + (b - d) = (a - c)x + (5 - (-1)) = (a - c)x + 6.\n4. Given p(3) - q(3) = 0 => 3(a - c) + 6 = 0 => 3(a - c) = -6 => a - c = -2.\n5. Solve system:\n   a + c = 6\n   a - c = -2\n   Adding both equations: 2a = 4 => a = 2.\n   Then c = 6 - 2 = 4.\n6. Thus: p(x) = 2x + 5, q(x) = 4x - 1.",
                "finalAnswer": "p(x) = 2x + 5 and q(x) = 4x - 1",
                "unit": "polynomial pair",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q12: Matchstick hexagons pattern. Stage 1 has 1 hexagon (6 sticks), Stage 2 has 2 hexagons (11 sticks), Stage 3 has 3 hexagons (16 sticks). (i) Next 2 stages? (ii) Table (iii) nth stage rule (iv) 15th stage? (v) Can 200 matchsticks form a stage?",
                "given": "Stage 1: 6 sticks. Stage 2: 11 sticks. Stage 3: 16 sticks.",
                "formula": "Common difference d = 11 - 6 = 5. Pattern rule S(n) = 5n + 1.",
                "substitution": "S(4) = 5(4) + 1 = 21; S(5) = 5(5) + 1 = 26; S(15) = 5(15) + 1.",
                "calculation": "1. Stage 4 requires 21 matchsticks; Stage 5 requires 26 matchsticks.\n2. Table: Stage: 1, 2, 3, 4, 5, ..., n; Sticks: 6, 11, 16, 21, 26, ..., 5n + 1.\n3. General rule for nth stage: S(n) = 5n + 1.\n4. For n = 15: S(15) = 5(15) + 1 = 75 + 1 = 76 matchsticks.\n5. Can 200 sticks form a stage? Set 5n + 1 = 200 => 5n = 199 => n = 199/5 = 39.8, which is not an integer. Therefore, 200 matchsticks cannot form any stage.",
                "finalAnswer": "(i) 21 and 26 sticks; (iii) Rule: 5n + 1; (iv) 76 sticks; (v) No, 199 is not divisible by 5.",
                "unit": "pattern analysis",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q13: p(x) passes through (2, 3) and (6, 11). q(x) passes through (4, -1) and is parallel to p(x). Find p(x), q(x), and where they meet the x-axis.",
                "given": "p(x) passes through (2, 3) and (6, 11). q(4) = -1, q(x) is parallel to p(x).",
                "formula": "Parallel lines have identical slope: a_q = a_p. X-intercept is where y = 0 => x = -b/a.",
                "substitution": "a_p = (11 - 3) / (6 - 2) = 8 / 4 = 2.",
                "calculation": "1. For p(x): slope a = 2. b_p = 3 - 2(2) = 3 - 4 = -1. So p(x) = 2x - 1.\n2. For q(x): Since parallel, a_q = 2. With point (4, -1): -1 = 2(4) + d => -1 = 8 + d => d = -9. So q(x) = 2x - 9.\n3. Meeting x-axis:\n   For p(x): 2x - 1 = 0 => x = 1/2 => Point (1/2, 0).\n   For q(x): 2x - 9 = 0 => x = 9/2 = 4.5 => Point (9/2, 0).",
                "finalAnswer": "p(x) = 2x - 1 (x-int: (1/2, 0)); q(x) = 2x - 9 (x-int: (9/2, 0)).",
                "unit": "parallel polynomials",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q14: What do all linear functions of the form f(x) = ax + a, a > 0, have in common?",
                "given": "Function f(x) = ax + a with a > 0.",
                "formula": "Factorize: f(x) = a(x + 1). Find roots and intercepts.",
                "substitution": "Set f(x) = 0: a(x + 1) = 0.",
                "calculation": "1. Since a > 0, dividing by a gives x + 1 = 0 => x = -1.\n2. Thus, f(-1) = a(-1) + a = 0 for every positive value of a.\n3. This means all graphs of f(x) = ax + a pass through the fixed point (-1, 0) on the x-axis.\n4. Additionally, slope = a and y-intercept = a, so for every such line, the numerical value of its slope is identical to its y-intercept.",
                "finalAnswer": "All lines of the form f(x) = ax + a pass through the common point (-1, 0) on the x-axis, and their slope is always equal to their y-intercept (both equal to a).",
                "unit": "invariant property",
                "has_diagram": True
            }
        ]
    }
