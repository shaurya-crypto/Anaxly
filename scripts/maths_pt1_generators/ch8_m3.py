"""
scripts/maths_pt1_generators/ch8_m3.py
Module 3 for Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Topic: Sum of First n Natural Numbers, AP Series Sum & Divisibility Applications
"""

def get_m3():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Sum of Arithmetic Progressions: Gauss Pairing &amp; Series Sum</text>
  
  <!-- Left Side: Gauss Pairing 2 x S_6 = 6 x 7 = 42 -->
  <g transform="translate(60, 90)">
    <text x="150" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Gauss Rectangular Pairing: 2 &times; S_n = n(n+1)</text>
    
    <!-- 6 rows, 7 columns dot rectangle -->
    <g transform="translate(25, 30)">
      <!-- Row 1: 1 cyan dot, 6 red dots -->
      <circle cx="20" cy="20" r="7" fill="#38bdf8"/>
      <circle cx="50" cy="20" r="7" fill="#f43f5e"/>
      <circle cx="80" cy="20" r="7" fill="#f43f5e"/>
      <circle cx="110" cy="20" r="7" fill="#f43f5e"/>
      <circle cx="140" cy="20" r="7" fill="#f43f5e"/>
      <circle cx="170" cy="20" r="7" fill="#f43f5e"/>
      <circle cx="200" cy="20" r="7" fill="#f43f5e"/>
      
      <!-- Row 2: 2 cyan, 5 red -->
      <circle cx="20" cy="50" r="7" fill="#38bdf8"/>
      <circle cx="50" cy="50" r="7" fill="#38bdf8"/>
      <circle cx="80" cy="50" r="7" fill="#f43f5e"/>
      <circle cx="110" cy="50" r="7" fill="#f43f5e"/>
      <circle cx="140" cy="50" r="7" fill="#f43f5e"/>
      <circle cx="170" cy="50" r="7" fill="#f43f5e"/>
      <circle cx="200" cy="50" r="7" fill="#f43f5e"/>
      
      <!-- Row 3: 3 cyan, 4 red -->
      <circle cx="20" cy="80" r="7" fill="#38bdf8"/>
      <circle cx="50" cy="80" r="7" fill="#38bdf8"/>
      <circle cx="80" cy="80" r="7" fill="#38bdf8"/>
      <circle cx="110" cy="80" r="7" fill="#f43f5e"/>
      <circle cx="140" cy="80" r="7" fill="#f43f5e"/>
      <circle cx="170" cy="80" r="7" fill="#f43f5e"/>
      <circle cx="200" cy="80" r="7" fill="#f43f5e"/>
      
      <!-- Row 4: 4 cyan, 3 red -->
      <circle cx="20" cy="110" r="7" fill="#38bdf8"/>
      <circle cx="50" cy="110" r="7" fill="#38bdf8"/>
      <circle cx="80" cy="110" r="7" fill="#38bdf8"/>
      <circle cx="110" cy="110" r="7" fill="#38bdf8"/>
      <circle cx="140" cy="110" r="7" fill="#f43f5e"/>
      <circle cx="170" cy="110" r="7" fill="#f43f5e"/>
      <circle cx="200" cy="110" r="7" fill="#f43f5e"/>
      
      <!-- Row 5: 5 cyan, 2 red -->
      <circle cx="20" cy="140" r="7" fill="#38bdf8"/>
      <circle cx="50" cy="140" r="7" fill="#38bdf8"/>
      <circle cx="80" cy="140" r="7" fill="#38bdf8"/>
      <circle cx="110" cy="140" r="7" fill="#38bdf8"/>
      <circle cx="140" cy="140" r="7" fill="#38bdf8"/>
      <circle cx="170" cy="140" r="7" fill="#f43f5e"/>
      <circle cx="200" cy="140" r="7" fill="#f43f5e"/>
      
      <!-- Row 6: 6 cyan, 1 red -->
      <circle cx="20" cy="170" r="7" fill="#38bdf8"/>
      <circle cx="50" cy="170" r="7" fill="#38bdf8"/>
      <circle cx="80" cy="170" r="7" fill="#38bdf8"/>
      <circle cx="110" cy="170" r="7" fill="#38bdf8"/>
      <circle cx="140" cy="170" r="7" fill="#38bdf8"/>
      <circle cx="170" cy="170" r="7" fill="#38bdf8"/>
      <circle cx="200" cy="170" r="7" fill="#f43f5e"/>
    </g>
    
    <text x="150" y="245" font-family="system-ui, sans-serif" font-size="14" fill="#f8fafc" text-anchor="middle">6 rows &times; 7 columns = 42 dots</text>
    <text x="150" y="270" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" font-weight="bold" text-anchor="middle">S_6 = 42 / 2 = 21</text>
  </g>
  
  <!-- Right Side: Sum Formula & Consecutive Partition of 100 -->
  <g transform="translate(460, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Decomposing 100 into Consecutive Integers</text>
    
    <!-- Partition 1: 5 terms (18 + 19 + 20 + 21 + 22 = 100) -->
    <rect x="10" y="35" width="260" height="90" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="25" y="65" font-family="system-ui, sans-serif" font-size="15" fill="#38bdf8" font-weight="bold">k = 5 consecutive terms:</text>
    <text x="25" y="95" font-family="system-ui, sans-serif" font-size="14" fill="#f8fafc">18 + 19 + 20 + 21 + 22 = 100</text>
    <text x="25" y="115" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8">Center = 20, 5 &times; 20 = 100</text>
    
    <!-- Partition 2: 8 terms (9 + 10 + ... + 16 = 100) -->
    <rect x="10" y="145" width="260" height="90" fill="#1e293b" stroke="#4ade80" stroke-width="2" rx="8"/>
    <text x="25" y="175" font-family="system-ui, sans-serif" font-size="15" fill="#4ade80" font-weight="bold">k = 8 consecutive terms:</text>
    <text x="25" y="205" font-family="system-ui, sans-serif" font-size="14" fill="#f8fafc">9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 = 100</text>
    <text x="25" y="225" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8">Pairs: (9+16) + (10+15) + ... = 4 &times; 25 = 100</text>
    
    <text x="140" y="270" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Only 2 solutions exist in positive integers!</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "Exercise 8.2 Q5 (i): How many 2-digit numbers are divisible by 3?",
            "given": "Range of 2-digit numbers: 10 to 99. Smallest 2-digit number divisible by 3 is a = 12. Largest is l = 99. Common difference d = 3.",
            "formula": "l = a + (n - 1)d",
            "substitution": "99 = 12 + (n - 1)*3",
            "calculation": "99 - 12 = 3(n - 1) => 87 = 3(n - 1) => n - 1 = 29 => n = 30.",
            "finalAnswer": "There are 30 two-digit numbers divisible by 3.",
            "unit": "count of numbers",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.2 Q5 (ii): Find the sum of all 2-digit numbers that are divisible by 3.",
            "given": "AP of two-digit multiples of 3: 12, 15, ..., 99 with n = 30, first term a = 12, last term l = 99.",
            "formula": "S_n = (n / 2) * (a + l)",
            "substitution": "S_30 = (30 / 2) * (12 + 99)",
            "calculation": "S_30 = 15 * 111 = 1665.",
            "finalAnswer": "1665",
            "unit": "sum of series",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.2 Q7: A child arranges marbles in rows so that the first row has 1 marble, the second has 2 marbles, the third has 3, and so on up to 25 rows. How many marbles does the child use in all?",
            "given": "Marbles per row form the sequence 1, 2, 3, ..., 25 (first 25 natural numbers). Here n = 25, a = 1, l = 25.",
            "formula": "S_n = n(n + 1) / 2",
            "substitution": "S_25 = 25 * (25 + 1) / 2 = 25 * 26 / 2",
            "calculation": "S_25 = 25 * 13 = 325.",
            "finalAnswer": "The child uses 325 marbles in all.",
            "unit": "marbles",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q3: How many three-digit numbers are divisible by 7? Also find their total sum.",
            "given": "Three-digit numbers range from 100 to 999. Smallest three-digit multiple of 7: 105 (since 105 = 7 * 15). Largest three-digit multiple of 7: 994 (since 999 / 7 = 142.71, 142 * 7 = 994). Common difference d = 7.",
            "formula": "l = a + (n - 1)d; S_n = (n / 2) * (a + l)",
            "substitution": "994 = 105 + (n - 1)*7 => 889 = 7(n - 1)",
            "calculation": "n - 1 = 889 / 7 = 127 => n = 128 three-digit numbers.\nSum S_128 = (128 / 2) * (105 + 994) = 64 * 1099 = 70,336.",
            "finalAnswer": "128 numbers; Total sum = 70,336",
            "unit": "numbers and sum",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q4: How many multiples of 4 lie between 10 and 250? Also determine the sum of all these multiples.",
            "given": "Range: strictly between 10 and 250. Smallest multiple of 4 > 10 is a = 12. Largest multiple of 4 < 250 is l = 248. Common difference d = 4.",
            "formula": "l = a + (n - 1)d; S_n = (n / 2) * (a + l)",
            "substitution": "248 = 12 + (n - 1)*4 => 236 = 4(n - 1)",
            "calculation": "n - 1 = 236 / 4 = 59 => n = 60 multiples.\nSum S_60 = (60 / 2) * (12 + 248) = 30 * 260 = 7,800.",
            "finalAnswer": "60 multiples; Total sum = 7,800",
            "unit": "count and sum",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q6: Find all possible ways of expressing 100 as the sum of consecutive natural numbers.",
            "given": "Sum S_k = 100 for k consecutive natural numbers starting from a (where a >= 1 and k >= 2).",
            "formula": "S_k = (k / 2) * [2a + (k - 1)*1] = 100 => k * (2a + k - 1) = 200",
            "substitution": "Notice that k and (2a + k - 1) have opposite parity (one is even, one is odd) because their difference is 2a - 1 (an odd integer). Factors of 200 = 2^3 * 5^2.",
            "calculation": "Possible odd factors of 200 are 1, 5, 25.\nCase 1: Odd factor = 1 => impossible since k >= 2 and 2a + k - 1 > 1.\nCase 2: k = 5 (odd factor), then 2a + 5 - 1 = 40 => 2a + 4 = 40 => 2a = 36 => a = 18.\nConsecutive sequence: 18 + 19 + 20 + 21 + 22 = 100 (Valid!).\nCase 3: 2a + k - 1 = 25 (odd factor), then k = 200 / 25 = 8.\nThen 2a + 8 - 1 = 25 => 2a + 7 = 25 => 2a = 18 => a = 9.\nConsecutive sequence: 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 = 100 (Valid!).\nCase 4: k = 25, then 2a + 24 = 8 => 2a = -16 (no positive integer solution).",
            "finalAnswer": "Exactly two ways: (i) 18 + 19 + 20 + 21 + 22 (5 terms); (ii) 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 (8 terms).",
            "unit": "consecutive partitions",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q8: The sum of the 4th and 8th terms of an AP is 24 and the sum of the 6th and 10th terms is 44. Find the first three terms of the AP.",
            "given": "a_4 + a_8 = 24 and a_6 + a_10 = 44.",
            "formula": "a_n = a + (n - 1)d",
            "substitution": "(a + 3d) + (a + 7d) = 24 => 2a + 10d = 24 => a + 5d = 12 (Eq 1).\n(a + 5d) + (a + 9d) = 44 => 2a + 14d = 44 => a + 7d = 22 (Eq 2).",
            "calculation": "Subtract Eq 1 from Eq 2: (a + 7d) - (a + 5d) = 22 - 12 => 2d = 10 => d = 5.\nSubstitute d = 5 into Eq 1: a + 5(5) = 12 => a + 25 = 12 => a = -13.\nFirst three terms: a_1 = -13, a_2 = -13 + 5 = -8, a_3 = -8 + 5 = -3.",
            "finalAnswer": "-13, -8, -3",
            "unit": "AP terms",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q9: Find the smallest value of n such that the sum of the first n natural numbers is greater than 1,000.",
            "given": "Sum of first n natural numbers S_n = n(n + 1) / 2 > 1000.",
            "formula": "n(n + 1) > 2000 => n^2 + n - 2000 > 0",
            "substitution": "Find root of n^2 + n - 2000 = 0: n = [-1 + sqrt(1 + 8000)] / 2 = [-1 + sqrt(8001)] / 2",
            "calculation": "sqrt(8001) ≈ 89.448.\nn ≈ (-1 + 89.448) / 2 ≈ 88.448 / 2 ≈ 44.224.\nSince n must be an integer, n >= 45.\nVerification: For n = 44: S_44 = 44 * 45 / 2 = 990 (not > 1000).\nFor n = 45: S_45 = 45 * 46 / 2 = 1035 (strictly > 1000).",
            "finalAnswer": "Smallest value is n = 45 (sum = 1035).",
            "unit": "natural number threshold",
            "has_diagram": False
        },
        {
            "problem": "Gauss Pairing Theorem: Derive the formula for the sum of the first n natural numbers S_n = 1 + 2 + 3 + ... + n and explain Gauss's reversal pairing method.",
            "given": "Series S = 1 + 2 + 3 + ... + (n - 1) + n.",
            "formula": "Write S forwards and backwards, then add column by column.",
            "substitution": "S = 1 + 2 + ... + n\nS = n + (n-1) + ... + 1\n2S = (n+1) + (n+1) + ... + (n+1) [n identical terms]",
            "calculation": "2S = n(n + 1) => S = n(n + 1) / 2.",
            "finalAnswer": "S_n = n(n + 1) / 2",
            "unit": "theorem derivation",
            "has_diagram": True
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Gauss Triangular Sum Parabola",
            "diagram_title": "Continuous Quadratic Envelope S(x) = x(x+1)/2",
            "interactive_math_formula": "S(n) = \\frac{n(n+1)}{2} = \\frac{1}{2}n^2 + \\frac{1}{2}n",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 50],
                "y_range": [0, 1200],
                "grid": True,
                "curves": [
                    {"fn": "0.5 * x * (x + 1)", "color": "#38bdf8", "label": "S(n) = n(n+1)/2"}
                ],
                "lines": [
                    {"x1": 0, "y1": 1000, "x2": 50, "y2": 1000, "color": "#f43f5e", "label": "Threshold = 1000"}
                ],
                "points": [
                    {"x": 44, "y": 990, "label": "S(44) = 990"},
                    {"x": 45, "y": 1035, "label": "S(45) = 1035 (Crossing Point)"}
                ]
            },
            "image_query": "gauss sum of natural numbers quadratic curve parabola",
            "video_query": "sum of first n natural numbers gauss pairing proof",
            "what_to_explain": "Show how the sum grows quadratically, crossing the 1000 threshold precisely between n=44 and n=45."
        },
        {
            "concept_title": "Divisibility Multiples Arithmetic Progression",
            "diagram_title": "Multiples of 7 between 100 and 1000",
            "interactive_math_formula": "a_k = 105 + 7(k - 1), \\quad k \\in \\{1, 2, \\dots, 128\\}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 130],
                "y_range": [0, 1050],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 105, "x2": 128, "y2": 994, "color": "#4ade80", "label": "y = 105 + 7(x-1)"}
                ],
                "points": [{"x": 1, "y": 105}, {"x": 128, "y": 994}]
            },
            "image_query": "multiples of 7 progression 105 to 994 line graph",
            "video_query": "how many numbers divisible by 7 between 100 and 1000",
            "what_to_explain": "Illustrate how identifying the first multiple (105) and last multiple (994) defines the finite interval containing exactly 128 evenly spaced points."
        },
        {
            "concept_title": "Sum of First n Odd Numbers",
            "diagram_title": "L-Shaped Gnomon Geometric Proof: 1 + 3 + ... + (2n-1) = n^2",
            "interactive_math_formula": "\\sum_{k=1}^n (2k - 1) = n^2",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 10],
                "y_range": [0, 100],
                "grid": True,
                "curves": [
                    {"fn": "x^2", "color": "#facc15", "label": "S_odd(n) = n^2"}
                ],
                "points": [{"x": 1, "y": 1}, {"x": 2, "y": 4}, {"x": 3, "y": 9}, {"x": 4, "y": 16}, {"x": 5, "y": 25}]
            },
            "image_query": "sum of odd numbers is a perfect square gnomon visual",
            "video_query": "visual proof sum of first n odd numbers equals n squared",
            "what_to_explain": "Demonstrate the geometric beauty of adding L-shaped borders (gnomons) of 3, 5, 7, 9 dots to an existing square to grow from 1^2 to 2^2, 3^2, etc."
        },
        {
            "concept_title": "Consecutive Partition Integer Factors",
            "diagram_title": "Factor Symmetry k * (2a + k - 1) = 200",
            "interactive_math_formula": "k \\in \\{5, 8\\} \\implies a \\in \\{18, 9\\}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 20],
                "y_range": [0, 50],
                "grid": True,
                "curves": [
                    {"fn": "200 / x", "color": "#c084fc", "label": "Hyperbola: xy = 200"}
                ],
                "points": [{"x": 5, "y": 40, "label": "k=5, 2a+k-1=40"}, {"x": 8, "y": 25, "label": "k=8, 2a+k-1=25"}]
            },
            "image_query": "expressing number as sum of consecutive integers number theory",
            "video_query": "how to find consecutive integer sums for 100",
            "what_to_explain": "Explain that finding consecutive sums reduces to finding odd divisors of 2N. The only non-trivial odd divisors of 200 are 5 and 25, producing exactly two valid integer partitions."
        },
        {
            "concept_title": "Partial Sums Difference Property",
            "diagram_title": "Recovering Term a_n = S_n - S_{n-1}",
            "interactive_math_formula": "a_n = S_n - S_{n-1} \\quad \\forall n \\ge 2",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 10],
                "y_range": [0, 150],
                "grid": True,
                "curves": [
                    {"fn": "2*x^2 + 3*x", "color": "#38bdf8", "label": "S_n = 2n^2 + 3n"}
                ],
                "lines": [
                    {"x1": 0, "y1": 1, "x2": 10, "y2": 41, "color": "#f43f5e", "label": "a_n = 4n + 1"}
                ],
                "points": [{"x": 5, "y": 65, "label": "S5 = 65"}, {"x": 4, "y": 44, "label": "S4 = 44"}]
            },
            "image_query": "relation between nth term and sum of n terms AP graph",
            "video_query": "finding nth term from sum of n terms formula S_n minus S_n-1",
            "what_to_explain": "Teach students that subtracting the cumulative sum up to (n-1) from the sum up to n isolates the individual nth term."
        }
    ]

    concept_questions = [
        {
            "concept": "Sum of Arithmetic Series",
            "questions": [
                {
                    "question": "Why is the sum of an AP quadratic in n while the nth term is linear in n?",
                    "type": "conceptual",
                    "ideal_answer": "Because summing n terms with average value (a + l)/2 multiplies an expression linear in n by the factor n, yielding an expression containing n^2.",
                    "socratic_hint": "What is the formula S_n = (n/2)[2a + (n-1)d] when you expand the brackets?"
                },
                {
                    "question": "How can you determine whether an expression for S_n represents a valid AP?",
                    "type": "conceptual",
                    "ideal_answer": "S_n must be of the form An^2 + Bn with zero constant term (since S_0 must equal 0). If there is a constant term (e.g. 3n^2 + 2n + 5), it is not an AP starting from n = 1.",
                    "socratic_hint": "What must the sum of zero terms equal?"
                }
            ]
        }
    ]

    return {
        "order_index": 3,
        "title": "Sum of First n Natural Numbers, AP Series Sum & Divisibility Applications",
        "description": "Derive Gauss's pairing formula for natural numbers, establish the general AP sum formula S_n = (n/2)[2a + (n-1)d], and solve divisibility bounds and consecutive integer partition problems.",
        "subtopics": [
            "Gauss's Reversal Pairing Proof: 2S = n(n+1)",
            "General AP Series Sum: S_n = (n/2)(a + l) and S_n = (n/2)[2a + (n-1)d]",
            "Divisibility Sequences: Multiples within Bounded Intervals",
            "Integer Partitions: Expressing Numbers as Consecutive Sums",
            "System Resolution of Term Sums (a_4 + a_8 = 24)",
            "Threshold Inversion: Smallest n for S_n > Bound"
        ],
        "key_concepts": [
            "Natural number sum formula: S_n = n(n+1)/2",
            "AP sum formulas: S_n = (n/2)(a + l) = (n/2)[2a + (n-1)d]",
            "Term recovery invariant: a_n = S_n - S_{n-1}",
            "Consecutive integer sums correspond to odd divisors of 2N",
            "Quadratic inequalities for series threshold criteria"
        ],
        "success_criteria": "Students can apply both sum formulas fluently, count and sum multiples within numerical ranges, deduce AP parameters from sum conditions, and solve consecutive partition problems.",
        "chapter_notes": "Summing an AP is one of the classic triumphs of school mathematics. Gauss's pairing technique unifies geometric dot arrays with symbolic algebra, providing a template for series summation.",
        "common_misconceptions": [
            {
                "misconception": "In divisibility problems, you just divide the endpoints by d and subtract.",
                "clarification": "Careless subtraction ignores whether the interval is inclusive or exclusive. One must always formulate the explicit AP, identify first term a and last term l, and solve l = a + (n-1)d.",
                "misconception": "S_n can have a constant term C != 0.",
                "clarification": "The sum of zero terms is 0. If S_n has a constant term, the first difference is not constant at n = 1."
            }
        ],
        "ai_system_prompt_context": "Highlight Gauss's pairing technique. Guide students to see that (first + last) equals (second + second-to-last), producing n/2 identical pairs.",
        "visual_lesson_plan": {
            "title": "Gauss Rectangular Array & AP Sum Formula",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel visual showing Gauss's 6x7 dot rectangle on the left and the consecutive partition of 100 on the right.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
