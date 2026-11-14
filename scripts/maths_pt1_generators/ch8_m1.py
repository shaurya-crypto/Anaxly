"""
scripts/maths_pt1_generators/ch8_m1.py
Module 1 for Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Topic: Number Patterns, Sequences, Triangular Numbers & Explicit/Recursive Rules
"""

def get_m1():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Triangular &amp; Square Numbers: Dot Patterns</text>
  
  <!-- Left Side: Triangular Numbers T1 to T4 -->
  <g transform="translate(60, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Triangular Numbers: T_n = n(n+1)/2</text>
    
    <!-- T1 = 1 -->
    <circle cx="30" cy="180" r="8" fill="#38bdf8"/>
    <text x="30" y="220" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle">T_1 = 1</text>
    
    <!-- T2 = 3 -->
    <circle cx="85" cy="160" r="8" fill="#38bdf8"/>
    <circle cx="75" cy="180" r="8" fill="#38bdf8"/>
    <circle cx="95" cy="180" r="8" fill="#38bdf8"/>
    <text x="85" y="220" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle">T_2 = 3</text>
    
    <!-- T3 = 6 -->
    <circle cx="160" cy="140" r="8" fill="#38bdf8"/>
    <circle cx="150" cy="160" r="8" fill="#38bdf8"/>
    <circle cx="170" cy="160" r="8" fill="#38bdf8"/>
    <circle cx="140" cy="180" r="8" fill="#38bdf8"/>
    <circle cx="160" cy="180" r="8" fill="#38bdf8"/>
    <circle cx="180" cy="180" r="8" fill="#38bdf8"/>
    <text x="160" y="220" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle">T_3 = 6</text>
    
    <!-- T4 = 10 -->
    <circle cx="255" cy="120" r="8" fill="#38bdf8"/>
    <circle cx="245" cy="140" r="8" fill="#38bdf8"/>
    <circle cx="265" cy="140" r="8" fill="#38bdf8"/>
    <circle cx="235" cy="160" r="8" fill="#38bdf8"/>
    <circle cx="255" cy="160" r="8" fill="#38bdf8"/>
    <circle cx="275" cy="160" r="8" fill="#38bdf8"/>
    <circle cx="225" cy="180" r="8" fill="#38bdf8"/>
    <circle cx="245" cy="180" r="8" fill="#38bdf8"/>
    <circle cx="265" cy="180" r="8" fill="#38bdf8"/>
    <circle cx="285" cy="180" r="8" fill="#38bdf8"/>
    <text x="255" y="220" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle">T_4 = 10</text>
    
    <text x="150" y="270" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Sequence: 1, 3, 6, 10, 15, 21, ...</text>
  </g>
  
  <!-- Right Side: Two Consecutive Triangular Numbers form a Square Number -->
  <g transform="translate(450, 90)">
    <text x="150" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Geometric Identity: T_{n-1} + T_n = n&sup2;</text>
    
    <!-- 4x4 grid showing T3 (red) + T4 (blue) = 4^2 = 16 -->
    <g transform="translate(50, 40)">
      <!-- Blue dots for T4 (lower triangle and diagonal) -->
      <circle cx="30" cy="30" r="9" fill="#38bdf8"/>
      
      <circle cx="30" cy="70" r="9" fill="#38bdf8"/>
      <circle cx="70" cy="70" r="9" fill="#38bdf8"/>
      
      <circle cx="30" cy="110" r="9" fill="#38bdf8"/>
      <circle cx="70" cy="110" r="9" fill="#38bdf8"/>
      <circle cx="110" cy="110" r="9" fill="#38bdf8"/>
      
      <circle cx="30" cy="150" r="9" fill="#38bdf8"/>
      <circle cx="70" cy="150" r="9" fill="#38bdf8"/>
      <circle cx="110" cy="150" r="9" fill="#38bdf8"/>
      <circle cx="150" cy="150" r="9" fill="#38bdf8"/>
      
      <!-- Red dots for T3 (upper triangle) -->
      <circle cx="70" cy="30" r="9" fill="#f43f5e"/>
      <circle cx="110" cy="30" r="9" fill="#f43f5e"/>
      <circle cx="150" cy="30" r="9" fill="#f43f5e"/>
      
      <circle cx="110" cy="70" r="9" fill="#f43f5e"/>
      <circle cx="150" cy="70" r="9" fill="#f43f5e"/>
      
      <circle cx="150" cy="110" r="9" fill="#f43f5e"/>
    </g>
    
    <text x="150" y="245" font-family="system-ui, sans-serif" font-size="14" fill="#f8fafc" text-anchor="middle">T_3 (6 red) + T_4 (10 blue) = 16 = 4&sup2;</text>
    <text x="150" y="270" font-family="system-ui, sans-serif" font-size="13" fill="#4ade80" font-weight="bold" text-anchor="middle">Every Square is the sum of two consecutive Triangles!</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "Exercise 8.1 Q1 (i): Find the first five terms of the sequence in which the nth term is given by the explicit rule t_n = 3n - 4 for n >= 1.",
            "given": "Explicit rule t_n = 3n - 4, index n in {1, 2, 3, 4, 5}.",
            "formula": "Substitute n = 1, 2, 3, 4, 5 directly into t_n = 3n - 4.",
            "substitution": "t_1 = 3(1)-4; t_2 = 3(2)-4; t_3 = 3(3)-4; t_4 = 3(4)-4; t_5 = 3(5)-4.",
            "calculation": "t_1 = 3 - 4 = -1; t_2 = 6 - 4 = 2; t_3 = 9 - 4 = 5; t_4 = 12 - 4 = 8; t_5 = 15 - 4 = 11.",
            "finalAnswer": "-1, 2, 5, 8, 11",
            "unit": "sequence terms",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.1 Q1 (ii): Find the first five terms of the sequence in which the nth term is given by t_n = 2 - 5n for n >= 1.",
            "given": "Explicit rule t_n = 2 - 5n, index n in {1, 2, 3, 4, 5}.",
            "formula": "Substitute n = 1, 2, 3, 4, 5 into t_n = 2 - 5n.",
            "substitution": "t_1 = 2 - 5(1); t_2 = 2 - 5(2); t_3 = 2 - 5(3); t_4 = 2 - 5(4); t_5 = 2 - 5(5).",
            "calculation": "t_1 = 2 - 5 = -3; t_2 = 2 - 10 = -8; t_3 = 2 - 15 = -13; t_4 = 2 - 20 = -18; t_5 = 2 - 25 = -23.",
            "finalAnswer": "-3, -8, -13, -18, -23",
            "unit": "sequence terms",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.1 Q1 (iii): Find the first five terms of the sequence in which the nth term is given by t_n = n^2 - 2n + 3 for n >= 1.",
            "given": "Explicit quadratic rule t_n = n^2 - 2n + 3.",
            "formula": "Substitute n = 1, 2, 3, 4, 5.",
            "substitution": "t_1 = 1^2 - 2(1) + 3; t_2 = 2^2 - 2(2) + 3; t_3 = 3^2 - 2(3) + 3; t_4 = 4^2 - 2(4) + 3; t_5 = 5^2 - 2(5) + 3.",
            "calculation": "t_1 = 1 - 2 + 3 = 2; t_2 = 4 - 4 + 3 = 3; t_3 = 9 - 6 + 3 = 6; t_4 = 16 - 8 + 3 = 11; t_5 = 25 - 10 + 3 = 18.",
            "finalAnswer": "2, 3, 6, 11, 18",
            "unit": "sequence terms",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.1 Q2: Find the 10th and 15th terms of the sequence t_n = 5n - 3 for n >= 1.",
            "given": "Explicit rule t_n = 5n - 3.",
            "formula": "t_n = 5n - 3",
            "substitution": "For n = 10: t_10 = 5(10) - 3. For n = 15: t_15 = 5(15) - 3.",
            "calculation": "t_10 = 50 - 3 = 47. t_15 = 75 - 3 = 72.",
            "finalAnswer": "t_10 = 47, t_15 = 72",
            "unit": "sequence terms",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.1 Q3: Determine whether 97 and 172 are terms of the sequence t_n = 5n - 3 for n >= 1.",
            "given": "Sequence t_n = 5n - 3. Candidate values 97 and 172.",
            "formula": "5n - 3 = Value => 5n = Value + 3 => n = (Value + 3) / 5. The value is a term if and only if n is a positive integer.",
            "substitution": "Case 1: 5n - 3 = 97 => 5n = 100. Case 2: 5n - 3 = 172 => 5n = 175.",
            "calculation": "Case 1: n = 100 / 5 = 20 (a positive integer, so 97 is the 20th term). Case 2: n = 175 / 5 = 35 (a positive integer, so 172 is the 35th term).",
            "finalAnswer": "Both 97 (20th term) and 172 (35th term) are terms of the sequence.",
            "unit": "term membership verification",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.1 Q4: Which term of the sequence t_n = 5n - 3 for n >= 1 is 607?",
            "given": "t_n = 607 with rule t_n = 5n - 3.",
            "formula": "5n - 3 = 607 => 5n = 607 + 3",
            "substitution": "5n = 610",
            "calculation": "n = 610 / 5 = 122.",
            "finalAnswer": "607 is the 122nd term (n = 122).",
            "unit": "term position index",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.1 Q5: A sequence is given by the recursive rule t_1 = -5, t_{n+1} = t_n + 3 for n >= 1. Find the first five terms of the sequence. Is 52 a term of this sequence? If so, which term is it?",
            "given": "Recursive rule: t_1 = -5, t_{n+1} = t_n + 3.",
            "formula": "Successive addition of 3: t_n = t_1 + (n - 1)d = -5 + (n - 1)*3 = 3n - 8.",
            "substitution": "t_1 = -5; t_2 = -5 + 3 = -2; t_3 = -2 + 3 = 1; t_4 = 1 + 3 = 4; t_5 = 4 + 3 = 7. Set 3n - 8 = 52.",
            "calculation": "3n = 52 + 8 = 60 => n = 60 / 3 = 20.",
            "finalAnswer": "First five terms: -5, -2, 1, 4, 7. Yes, 52 is the 20th term.",
            "unit": "terms and term position",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.1 Q6 (Tribonacci Sequence): Let T_1 = 1, T_2 = 2, T_3 = 4, and T_n = T_{n-1} + T_{n-2} + T_{n-3} for n >= 4. Find T_4, T_5, T_6, T_7, and T_8.",
            "given": "Initial terms T_1 = 1, T_2 = 2, T_3 = 4. 3-step recursive recurrence T_n = T_{n-1} + T_{n-2} + T_{n-3}.",
            "formula": "T_n = sum of previous three terms.",
            "substitution": "T_4 = 4 + 2 + 1; T_5 = T_4 + 4 + 2; T_6 = T_5 + T_4 + 4; T_7 = T_6 + T_5 + T_4; T_8 = T_7 + T_6 + T_5.",
            "calculation": "T_4 = 4 + 2 + 1 = 7.\nT_5 = 7 + 4 + 2 = 13.\nT_6 = 13 + 7 + 4 = 24.\nT_7 = 24 + 13 + 7 = 44.\nT_8 = 44 + 24 + 13 = 81.",
            "finalAnswer": "T_4 = 7, T_5 = 13, T_6 = 24, T_7 = 44, T_8 = 81",
            "unit": "recurrence sequence terms",
            "has_diagram": False
        },
        {
            "problem": "In-Text Example 1: Consider the expression u_n = 2n - 1. Find the 53rd term and the 101st term. Also, determine which term is the odd number 137.",
            "given": "Odd numbers sequence rule u_n = 2n - 1.",
            "formula": "u_n = 2n - 1",
            "substitution": "u_53 = 2(53) - 1; u_101 = 2(101) - 1; 2n - 1 = 137.",
            "calculation": "u_53 = 106 - 1 = 105.\nu_101 = 202 - 1 = 201.\n2n = 137 + 1 = 138 => n = 69.",
            "finalAnswer": "u_53 = 105, u_101 = 201; 137 is the 69th term.",
            "unit": "sequence terms",
            "has_diagram": False
        },
        {
            "problem": "In-Text Example 3 & 4 (Nonlinear Recursive Rules): (i) Find the first 4 terms of a_1 = 3, a_n = 2a_{n-1} + 1. (ii) Find the first 4 terms of b_1 = 2, b_n = (b_{n-1})^2 - 1.",
            "given": "Recurrences: (i) a_1 = 3, a_n = 2a_{n-1} + 1; (ii) b_1 = 2, b_n = (b_{n-1})^2 - 1.",
            "formula": "Sequential evaluation for n = 2, 3, 4.",
            "substitution": "(i) a_2 = 2(3)+1, a_3 = 2(7)+1, a_4 = 2(15)+1. (ii) b_2 = 2^2-1, b_3 = 3^2-1, b_4 = 8^2-1.",
            "calculation": "(i) a_1 = 3, a_2 = 7, a_3 = 15, a_4 = 31.\n(ii) b_1 = 2, b_2 = 3, b_3 = 8, b_4 = 63.",
            "finalAnswer": "(i) 3, 7, 15, 31; (ii) 2, 3, 8, 63",
            "unit": "recursive terms",
            "has_diagram": False
        },
        {
            "problem": "Textbook Activity: Triangular Numbers & Square Numbers Identity: Verify algebraically and geometrically that the sum of two consecutive triangular numbers T_{n-1} and T_n equals the square number n^2.",
            "given": "Triangular number formula T_n = n(n+1)/2. Previous triangular number T_{n-1} = (n-1)n/2.",
            "formula": "T_{n-1} + T_n = \\frac{(n-1)n}{2} + \\frac{n(n+1)}{2}",
            "substitution": "T_{n-1} + T_n = \\frac{n^2 - n + n^2 + n}{2}",
            "calculation": "= \\frac{2n^2}{2} = n^2. Example: T_3 + T_4 = 6 + 10 = 16 = 4^2.",
            "finalAnswer": "T_{n-1} + T_n = n^2 holds identically for all positive integers n >= 2.",
            "unit": "algebraic identity",
            "has_diagram": True
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Triangular Numbers Dot Lattice",
            "diagram_title": "Triangular Progression: T_n = n(n+1)/2",
            "interactive_math_formula": "T_n = \\sum_{k=1}^n k = \\frac{n(n+1)}{2}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 25],
                "grid": True,
                "curves": [
                    {"fn": "0.5 * x * (x + 1)", "color": "#38bdf8", "label": "T(x) = x(x+1)/2"}
                ],
                "points": [
                    {"x": 1, "y": 1, "label": "T1 = 1"},
                    {"x": 2, "y": 3, "label": "T2 = 3"},
                    {"x": 3, "y": 6, "label": "T3 = 6"},
                    {"x": 4, "y": 10, "label": "T4 = 10"},
                    {"x": 5, "y": 15, "label": "T5 = 15"}
                ]
            },
            "image_query": "triangular numbers dot pattern sequence diagram",
            "video_query": "triangular numbers geometric dot proof n times n plus 1 over 2",
            "what_to_explain": "Show how each triangular number adds a new row of dots at the base, creating a quadratic curve T_n = n(n+1)/2."
        },
        {
            "concept_title": "Geometric Composition of Square Numbers",
            "diagram_title": "Partitioning n^2 into Consecutive Triangular Numbers T_{n-1} + T_n",
            "interactive_math_formula": "n^2 = T_{n-1} + T_n = \\frac{n(n-1)}{2} + \\frac{n(n+1)}{2}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 5],
                "y_range": [0, 20],
                "grid": True,
                "curves": [
                    {"fn": "x^2", "color": "#facc15", "label": "Square Numbers n^2"},
                    {"fn": "0.5 * x * (x + 1)", "color": "#38bdf8", "label": "T_n"},
                    {"fn": "0.5 * (x - 1) * x", "color": "#f43f5e", "label": "T_{n-1}"}
                ],
                "points": [{"x": 4, "y": 16, "label": "4^2 = 6 + 10"}]
            },
            "image_query": "sum of two consecutive triangular numbers is a square diagram",
            "video_query": "visual proof triangular numbers sum to square number",
            "what_to_explain": "Demonstrate the visual pairing where two triangular dot shapes fit together along their diagonals to form a complete n-by-n square grid."
        },
        {
            "concept_title": "Linear Sequence Rate of Change",
            "diagram_title": "Discrete Points on Continuous Line: t_n = 5n - 3",
            "interactive_math_formula": "t_n = 5n - 3 \\iff y = 5x - 3",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 30],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": -3, "x2": 6, "y2": 27, "color": "#4ade80", "label": "y = 5x - 3"}
                ],
                "points": [
                    {"x": 1, "y": 2, "label": "t1 = 2"},
                    {"x": 2, "y": 7, "label": "t2 = 7"},
                    {"x": 3, "y": 12, "label": "t3 = 12"},
                    {"x": 4, "y": 17, "label": "t4 = 17"},
                    {"x": 5, "y": 22, "label": "t5 = 22"}
                ]
            },
            "image_query": "linear sequence discrete points on straight line graph",
            "video_query": "sequences as linear functions slope common difference",
            "what_to_explain": "Explain that an explicit linear formula t_n = mn + c defines discrete points sampled at positive integer x-coordinates along a straight line with slope m."
        },
        {
            "concept_title": "Tribonacci Rapid Growth Dynamics",
            "diagram_title": "3-Step Recurrence: T_n = T_{n-1} + T_{n-2} + T_{n-3}",
            "interactive_math_formula": "T_n \\approx C \\cdot (1.839)^n",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 9],
                "y_range": [0, 90],
                "grid": True,
                "points": [
                    {"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": 4},
                    {"x": 4, "y": 7}, {"x": 5, "y": 13}, {"x": 6, "y": 24},
                    {"x": 7, "y": 44}, {"x": 8, "y": 81}
                ],
                "curves": [
                    {"fn": "0.7 * (1.839)^x", "color": "#c084fc", "label": "Exponential Envelope ~ 1.839^n"}
                ]
            },
            "image_query": "tribonacci sequence growth curve graph",
            "video_query": "tribonacci sequence recurrence relation explanation",
            "what_to_explain": "Contrast single-step linear recurrence with higher-order linear recurrences like Tribonacci, which display explosive pseudo-exponential growth with constant ratio ~1.839."
        },
        {
            "concept_title": "Quadratic vs Linear Sequence Divergence",
            "diagram_title": "Comparing Second Differences: Linear (constant 1st diff) vs Quadratic (constant 2nd diff)",
            "interactive_math_formula": "t_n = n^2 - 2n + 3 \\implies \\Delta^2 t_n = 2",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 25],
                "grid": True,
                "curves": [
                    {"fn": "x^2 - 2*x + 3", "color": "#fb923c", "label": "Quadratic: n^2 - 2n + 3"},
                    {"fn": "3*x - 4", "color": "#38bdf8", "label": "Linear: 3n - 4"}
                ],
                "points": [{"x": 1, "y": 2}, {"x": 2, "y": 3}, {"x": 3, "y": 6}, {"x": 4, "y": 11}, {"x": 5, "y": 18}]
            },
            "image_query": "linear vs quadratic sequence difference method graph",
            "video_query": "method of differences finding nth term of quadratic sequence",
            "what_to_explain": "Show that while linear sequences have constant first differences, quadratic sequences have variable first differences but constant second differences."
        }
    ]

    concept_questions = [
        {
            "concept": "Sequences & Explicit Rules",
            "questions": [
                {
                    "question": "What is the difference between an explicit rule and a recursive rule for a sequence?",
                    "type": "conceptual",
                    "ideal_answer": "An explicit rule calculates the nth term directly from its position index n without knowing previous terms. A recursive rule defines the nth term using one or more preceding terms and requires given initial conditions.",
                    "socratic_hint": "If you want to find the 100th term, which rule allows you to calculate it in one step?"
                },
                {
                    "question": "Why must the position index n always be a positive integer {1, 2, 3, ...}?",
                    "type": "conceptual",
                    "ideal_answer": "Because sequence terms represent an ordered list of items in position 1st, 2nd, 3rd, and so on. A fractional or negative position is meaningless in an ordered list.",
                    "socratic_hint": "Can a person finish in 2.5th place in a race?"
                }
            ]
        }
    ]

    return {
        "order_index": 1,
        "title": "Number Patterns, Sequences, Triangular Numbers & Explicit/Recursive Rules",
        "description": "Investigate geometric number patterns including triangular and square numbers, formulate general explicit rules t_n = f(n), solve recursive recurrences, and determine term membership.",
        "subtopics": [
            "Geometric Dot Patterns: Triangular and Square Numbers",
            "The Geometric Identity: T_{n-1} + T_n = n^2",
            "Explicit Formula for the nth Term: t_n = f(n)",
            "Recursive Rules: Initial Values and Term Transitions",
            "Higher-Order Recurrences: The Tribonacci Sequence",
            "Term Membership Testing via Integer Inversion"
        ],
        "key_concepts": [
            "Triangular number formula: T_n = n(n+1)/2",
            "Square number decomposition into two consecutive triangles",
            "Explicit vs recursive generation",
            "Integer position constraint: n in N = {1, 2, 3, ...}",
            "Differences: constant 1st difference implies linear, constant 2nd implies quadratic"
        ],
        "success_criteria": "Students can formulate explicit rules for number patterns, compute terms from multi-step recursive relations, and test whether given values belong to a sequence.",
        "chapter_notes": "Sequences form the bridge between pattern recognition and formal algebra. Visualizing triangular and square numbers provides intuitive proof of formulas before symbolic algebraic manipulations.",
        "common_misconceptions": [
            {
                "misconception": "Any calculated value of n confirms a term belongs to the sequence.",
                "clarification": "The position index n MUST be a positive integer (1, 2, 3...). If n is a fraction (e.g. 14.4) or negative, the number is NOT in the sequence."
            },
            {
                "misconception": "A recursive rule can generate terms without an initial condition.",
                "clarification": "A recursive relation cannot determine specific numbers without at least one anchor value (such as t_1)."
            }
        ],
        "ai_system_prompt_context": "Start by drawing dot patterns of triangular numbers. Guide students to discover why T_3 + T_4 = 16 = 4^2 geometrically before showing algebraic substitution.",
        "visual_lesson_plan": {
            "title": "Triangular Dot Lattices & Sequence Recurrences",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel diagram showing triangular number dot patterns and the geometric combination of two triangles into a square.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
