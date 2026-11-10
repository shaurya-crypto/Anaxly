"""
scripts/maths_pt1_generators/ch8_m6.py
Module 6 for Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Topic: Advanced Progressions, Algebraic Challenges & Recursive Summations
"""

def get_m6():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Advanced Progressions: Fibonacci Emergence &amp; GP Factorization</text>
  
  <!-- Left Side: Fibonacci Emergence from Recursive Sum (W_n = W_{n-1} + W_{n-2}) -->
  <g transform="translate(60, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Fibonacci Sequence: 1, 2, 3, 5, 8, 13, 21, 34</text>
    
    <!-- Golden Rectangles / Spiral layout schematic -->
    <g transform="translate(30, 40)">
      <!-- 34x21 scaled bounding box -->
      <rect x="0" y="0" width="220" height="140" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
      
      <!-- Partition: 21x21 square -->
      <rect x="0" y="0" width="140" height="140" fill="#38bdf8" fill-opacity="0.1" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="70" y="75" font-family="system-ui, sans-serif" font-size="16" fill="#38bdf8" font-weight="bold" text-anchor="middle">21</text>
      
      <!-- 13x13 square -->
      <rect x="140" y="0" width="80" height="80" fill="#4ade80" fill-opacity="0.1" stroke="#4ade80" stroke-width="1.5"/>
      <text x="180" y="45" font-family="system-ui, sans-serif" font-size="14" fill="#4ade80" font-weight="bold" text-anchor="middle">13</text>
      
      <!-- 8x8 square -->
      <rect x="140" y="80" width="50" height="60" fill="#facc15" fill-opacity="0.1" stroke="#facc15" stroke-width="1.5"/>
      <text x="165" y="115" font-family="system-ui, sans-serif" font-size="13" fill="#facc15" font-weight="bold" text-anchor="middle">8</text>
      
      <!-- 5x5 square -->
      <rect x="190" y="80" width="30" height="35" fill="#fb923c" fill-opacity="0.1" stroke="#fb923c" stroke-width="1.5"/>
      <text x="205" y="102" font-family="system-ui, sans-serif" font-size="11" fill="#fb923c" font-weight="bold" text-anchor="middle">5</text>
    </g>
    
    <text x="140" y="225" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">W_n = W_1 + W_2 + ... + W_{n-2} + 2</text>
    <text x="140" y="250" font-family="system-ui, sans-serif" font-size="13" fill="#4ade80" font-weight="bold" text-anchor="middle">Simplifies to: W_n = W_{n-1} + W_{n-2}</text>
  </g>
  
  <!-- Right Side: GP Sum & Squares Factorization (2, 6, 18) -->
  <g transform="translate(460, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Algebraic Identity: 1 + r&sup2; + r&#8308;</text>
    
    <rect x="10" y="30" width="260" height="150" fill="#1e293b" stroke="#f43f5e" stroke-width="2" rx="8"/>
    
    <text x="25" y="60" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" font-weight="bold">System Equations:</text>
    <text x="25" y="85" font-family="system-ui, sans-serif" font-size="13" fill="#f8fafc">1) a(1 + r + r&sup2;) = 26</text>
    <text x="25" y="110" font-family="system-ui, sans-serif" font-size="13" fill="#f8fafc">2) a&sup2;(1 + r&sup2; + r&#8308;) = 364</text>
    
    <text x="25" y="140" font-family="system-ui, sans-serif" font-size="13" fill="#facc15" font-weight="bold">Sophie Germain Factoring:</text>
    <text x="25" y="162" font-family="system-ui, sans-serif" font-size="11" fill="#cbd5e1">1 + r&sup2; + r&#8308; = (1 + r + r&sup2;)(1 - r + r&sup2;)</text>
    
    <text x="140" y="225" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Quadratic in r: 3r&sup2; - 10r + 3 = 0</text>
    <text x="140" y="250" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" font-weight="bold" text-anchor="middle">Dual Solutions: (2, 6, 18) or (18, 6, 2)</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "End-of-Chapter Q1: Find the 31st term of an AP whose 11th term is 38 and 16th term is 73.",
            "given": "AP with a_11 = 38 and a_16 = 73.",
            "formula": "a_n = a + (n - 1)d; a_16 - a_11 = (16 - 11)d = 5d",
            "substitution": "73 - 38 = 5d => 35 = 5d",
            "calculation": "d = 35 / 5 = 7.\nFind a: a_11 = a + 10d => 38 = a + 10(7) => 38 = a + 70 => a = 38 - 70 = -32.\nNow compute 31st term: a_31 = a + 30d = -32 + 30(7) = -32 + 210 = 178.",
            "finalAnswer": "a_31 = 178 (with a = -32, d = 7)",
            "unit": "AP term value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q2: Determine the AP whose third term is 16 and whose 7th term exceeds the 5th term by 12.",
            "given": "Third term a_3 = 16. Condition: a_7 - a_5 = 12.",
            "formula": "a_7 - a_5 = (a + 6d) - (a + 4d) = 2d",
            "substitution": "2d = 12 => d = 6. a_3 = a + 2d = 16",
            "calculation": "a + 2(6) = 16 => a + 12 = 16 => a = 4.\nThe AP is: a, a + d, a + 2d, a + 3d, ...\nFirst four terms: 4, 10, 16, 22, ....",
            "finalAnswer": "The AP is 4, 10, 16, 22, ... (first term a = 4, common difference d = 6)",
            "unit": "arithmetic progression sequence",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q5: Find a GP for which the sum of the first two terms is -4 and the fifth term is 4 times the third term.",
            "given": "Condition 1: a_1 + a_2 = -4. Condition 2: a_5 = 4 * a_3.",
            "formula": "a_n = a * r^(n - 1). a_5 = a * r^4; a_3 = a * r^2.",
            "substitution": "a * r^4 = 4 * a * r^2 => r^2 = 4 (since a != 0, r != 0) => r = ±2.",
            "calculation": "Case 1: r = 2.\na + ar = -4 => a(1 + 2) = -4 => 3a = -4 => a = -4/3.\nGP: -4/3, -8/3, -16/3, -32/3, ....\nCase 2: r = -2.\na + ar = -4 => a(1 - 2) = -4 => -a = -4 => a = 4.\nGP: 4, -8, 16, -32, 64, ....",
            "finalAnswer": "Two valid GPs: (i) a = -4/3, r = 2: -4/3, -8/3, -16/3, ...; (ii) a = 4, r = -2: 4, -8, 16, -32, ...",
            "unit": "geometric progressions",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q11: The sum of the first three terms of a GP is 13/12 and their product is -1. Find the common ratio and the terms.",
            "given": "Three terms in GP. Let them be a/r, a, ar. Sum = 13/12, Product = -1.",
            "formula": "Product = (a / r) * a * (ar) = a^3 = -1 => a = -1.",
            "substitution": "Sum = -1/r + (-1) + (-r) = 13/12 => - (1/r + 1 + r) = 13/12",
            "calculation": "(r^2 + r + 1) / r = -13/12 => 12(r^2 + r + 1) = -13r\n12r^2 + 12r + 12 = -13r => 12r^2 + 25r + 12 = 0.\nFactorize: (3r + 4)(4r + 3) = 0.\nRoot 1: r = -4/3. Terms: (-1) / (-4/3) = 3/4; -1; (-1)*(-4/3) = 4/3. (Terms: 3/4, -1, 4/3).\nRoot 2: r = -3/4. Terms: (-1) / (-3/4) = 4/3; -1; (-1)*(-3/4) = 3/4. (Terms: 4/3, -1, 3/4).",
            "finalAnswer": "Common ratio r = -4/3 or -3/4. Terms: 3/4, -1, 4/3 (or in reverse order).",
            "unit": "GP terms and ratio",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q12: If the 4th, 10th and 16th terms of a GP are x, y and z respectively, prove that x, y, z are in GP.",
            "given": "In a GP with first term a and common ratio r: a_4 = x, a_10 = y, a_16 = z.",
            "formula": "x = a * r^3; y = a * r^9; z = a * r^15",
            "substitution": "Compute ratio y / x and ratio z / y.",
            "calculation": "y / x = (a * r^9) / (a * r^3) = r^(9 - 3) = r^6.\nz / y = (a * r^15) / (a * r^9) = r^(15 - 9) = r^6.\nSince y / x = z / y = r^6, the ratio between consecutive terms is constant.\nAlternatively: y^2 = (a * r^9)^2 = a^2 * r^18, and x * z = (a * r^3) * (a * r^15) = a^2 * r^18. Since y^2 = x * z, x, y, z form a GP.",
            "finalAnswer": "Proven: y/x = z/y = r^6 (and y^2 = x*z). Therefore, x, y, z form a Geometric Progression.",
            "unit": "theorem proof",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q13: The sum of the first three terms of a geometric progression is 26, and the sum of their squares is 364. Find the terms of the GP.",
            "given": "Let three terms be a, ar, ar^2. a(1 + r + r^2) = 26 (Eq 1). a^2(1 + r^2 + r^4) = 364 (Eq 2).",
            "formula": "Algebraic identity: 1 + r^2 + r^4 = (1 + r + r^2)(1 - r + r^2).",
            "substitution": "Square Eq 1: a^2(1 + r + r^2)^2 = 26^2 = 676. Divide by Eq 2.",
            "calculation": "[a^2(1 + r + r^2)^2] / [a^2(1 + r + r^2)(1 - r + r^2)] = 676 / 364\n(1 + r + r^2) / (1 - r + r^2) = 13 / 7 (since 676/364 = 13/7).\n7(1 + r + r^2) = 13(1 - r + r^2) => 7 + 7r + 7r^2 = 13 - 13r + 13r^2\n6r^2 - 20r + 6 = 0 => 3r^2 - 10r + 3 = 0.\n(3r - 1)(r - 3) = 0 => r = 3 or r = 1/3.\nIf r = 3: a(1 + 3 + 9) = 26 => 13a = 26 => a = 2. Terms: 2, 6, 18.\nIf r = 1/3: a(1 + 1/3 + 1/9) = 26 => a(13/9) = 26 => a = 18. Terms: 18, 6, 2.",
            "finalAnswer": "The terms of the GP are 2, 6, 18 (or in descending order: 18, 6, 2).",
            "unit": "GP terms",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q14: Suppose P_1 = 1, P_2 = 2 and for n > 2, P_n = P_1 + P_2 + ... + P_{n-1} + 1. Find the values of P_1, P_2, ..., P_8. Can you find a simpler recursive formula for P_n? Can you give an explicit formula?",
            "given": "Initial terms: P_1 = 1, P_2 = 2. Recurrence: P_n = [\\sum_{k=1}^{n-1} P_k] + 1 for n > 2.",
            "formula": "Notice P_{n-1} = [\\sum_{k=1}^{n-2} P_k] + 1 => \\sum_{k=1}^{n-2} P_k = P_{n-1} - 1.",
            "substitution": "P_n = [\\sum_{k=1}^{n-2} P_k] + P_{n-1} + 1 = (P_{n-1} - 1) + P_{n-1} + 1 = 2 * P_{n-1}.",
            "calculation": "P_1 = 1\nP_2 = 2\nP_3 = 1 + 2 + 1 = 4\nP_4 = 2 * P_3 = 8\nP_5 = 2 * P_4 = 16\nP_6 = 2 * P_5 = 32\nP_7 = 2 * P_6 = 64\nP_8 = 2 * P_7 = 128.\nSimpler recursive rule: P_1 = 1, P_2 = 2, P_3 = 4, P_n = 2 * P_{n - 1} for n >= 4.\nExplicit formula: P_1 = 1; P_n = 2^{n-1} for n >= 2.",
            "finalAnswer": "Values: 1, 2, 4, 8, 16, 32, 64, 128. Simpler recursive: P_n = 2*P_{n-1} (n >= 4). Explicit: P_n = 2^{n-1} for n >= 2 (P_1 = 1).",
            "unit": "recurrence analysis",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q15: Suppose W_1 = 1, W_2 = 2 and for n > 2, W_n = W_1 + W_2 + ... + W_{n-2} + 2. Find the values of W_1, W_2, ..., W_8. Do you recognize this sequence?",
            "given": "Initial terms W_1 = 1, W_2 = 2. Cumulative recurrence: W_n = [\\sum_{k=1}^{n-2} W_k] + 2 for n > 2.",
            "formula": "Subtract consecutive recurrences: W_n - W_{n-1} = W_{n-2} => W_n = W_{n-1} + W_{n-2}.",
            "substitution": "Evaluate terms sequentially.",
            "calculation": "W_1 = 1\nW_2 = 2\nW_3 = W_1 + 2 = 1 + 2 = 3\nW_4 = W_1 + W_2 + 2 = 1 + 2 + 2 = 5\nW_5 = W_4 + W_3 = 5 + 3 = 8\nW_6 = W_5 + W_4 = 8 + 5 = 13\nW_7 = W_6 + W_5 = 13 + 8 = 21\nW_8 = W_7 + W_6 = 21 + 13 = 34.\nNotice that 1, 2, 3, 5, 8, 13, 21, 34 are the Fibonacci numbers F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9!",
            "finalAnswer": "Values: 1, 2, 3, 5, 8, 13, 21, 34. This is the Fibonacci sequence satisfying W_n = W_{n-1} + W_{n-2}.",
            "unit": "Fibonacci sequence recognition",
            "has_diagram": True
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Fibonacci Golden Ratio Emergence",
            "diagram_title": "Additive Recurrence: W_n = W_{n-1} + W_{n-2}",
            "interactive_math_formula": "\\lim_{n \\to \\infty} \\frac{W_n}{W_{n-1}} = \\phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.618033",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 9],
                "y_range": [0, 40],
                "grid": True,
                "curves": [
                    {"fn": "(1 / sqrt(5)) * (((1 + sqrt(5))/2)^(x+1) - ((1 - sqrt(5))/2)^(x+1))", "color": "#4ade80", "label": "Binet Formula: W_n = F_{n+1}"}
                ],
                "points": [
                    {"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": 3},
                    {"x": 4, "y": 5}, {"x": 5, "y": 8}, {"x": 6, "y": 13},
                    {"x": 7, "y": 21}, {"x": 8, "y": 34}
                ]
            },
            "image_query": "fibonacci sequence golden spiral golden ratio points on curve",
            "video_query": "fibonacci sequence emergence binet formula golden ratio explanation",
            "what_to_explain": "Demonstrate how the cumulative recurrence W_n = (\\sum_{k=1}^{n-2} W_k) + 2 transforms cleanly into the standard two-term Fibonacci recurrence, converging to the golden ratio phi."
        },
        {
            "concept_title": "Sophie Germain GP Ratio Factorization",
            "diagram_title": "Rational Curve: y = (1 + x + x^2) / (1 - x + x^2)",
            "interactive_math_formula": "\\frac{1 + r + r^2}{1 - r + r^2} = \\frac{13}{7} \\iff 3r^2 - 10r + 3 = 0",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 5],
                "y_range": [0, 4],
                "grid": True,
                "curves": [
                    {"fn": "(1 + x + x^2) / (1 - x + x^2)", "color": "#38bdf8", "label": "f(r) = (1+r+r^2)/(1-r+r^2)"}
                ],
                "lines": [
                    {"x1": 0, "y1": 1.857, "x2": 5, "y2": 1.857, "color": "#facc15", "label": "y = 13/7 ≈ 1.857"}
                ],
                "points": [
                    {"x": 0.333, "y": 1.857, "label": "r = 1/3"},
                    {"x": 3.0, "y": 1.857, "label": "r = 3"}
                ]
            },
            "image_query": "rational function quadratic roots intersection graph",
            "video_query": "sophie germain identity solving geometric progression sum of squares",
            "what_to_explain": "Explain that because the ratio equation is symmetric under inversion (r <-> 1/r), finding r = 3 automatically implies r = 1/3 is also a valid reciprocal root."
        },
        {
            "concept_title": "Cumulative Sum Recurrence Doubling",
            "diagram_title": "Power of 2 Envelope for P_n = 2 * P_{n-1}",
            "interactive_math_formula": "P_n = 2^{n-1} \\quad \\forall n \\ge 2",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 9],
                "y_range": [0, 150],
                "grid": True,
                "curves": [
                    {"fn": "2^(x - 1)", "color": "#c084fc", "label": "y = 2^(x-1)"}
                ],
                "points": [
                    {"x": 1, "y": 1, "label": "P1 = 1"},
                    {"x": 2, "y": 2, "label": "P2 = 2"},
                    {"x": 3, "y": 4, "label": "P3 = 4"},
                    {"x": 4, "y": 8, "label": "P4 = 8"},
                    {"x": 5, "y": 16, "label": "P5 = 16"},
                    {"x": 6, "y": 32, "label": "P6 = 32"},
                    {"x": 7, "y": 64, "label": "P7 = 64"},
                    {"x": 8, "y": 128, "label": "P8 = 128"}
                ]
            },
            "image_query": "power of 2 doubling sequence exponential graph",
            "video_query": "sum of powers of 2 prefix sum recurrence explanation",
            "what_to_explain": "Show students that adding 1 to the sum of all preceding powers of 2 always generates the exact next power of 2."
        },
        {
            "concept_title": "AP Parameter Intersection via Term Subtraction",
            "diagram_title": "Step Invariant: d = (a_16 - a_11) / 5 = 35 / 5 = 7",
            "interactive_math_formula": "d = \\frac{a_p - a_q}{p - q} = \\frac{73 - 38}{16 - 11} = 7",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [10, 32],
                "y_range": [30, 190],
                "grid": True,
                "lines": [
                    {"x1": 10, "y1": 31, "x2": 31, "y2": 178, "color": "#4ade80", "label": "y = -32 + 7(x-1)"}
                ],
                "points": [
                    {"x": 11, "y": 38, "label": "a11 = 38"},
                    {"x": 16, "y": 73, "label": "a16 = 73"},
                    {"x": 31, "y": 178, "label": "a31 = 178"}
                ]
            },
            "image_query": "secant slope arithmetic progression straight line interpolation",
            "video_query": "finding AP terms from two given terms slope formula",
            "what_to_explain": "Show that the formula d = (a_p - a_q)/(p - q) is identical to the slope formula (y2 - y1)/(x2 - x1) from coordinate geometry."
        },
        {
            "concept_title": "Dual Reciprocal GP Branches",
            "diagram_title": "Mirror Progressions: (2, 6, 18) vs (18, 6, 2)",
            "interactive_math_formula": "(a, r) = (2, 3) \\iff (a', r') = (18, 1/3)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 4],
                "y_range": [0, 20],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 2, "x2": 2, "y2": 6, "color": "#38bdf8", "label": "Branch 1: r = 3"},
                    {"x1": 2, "y1": 6, "x2": 3, "y2": 18, "color": "#38bdf8"},
                    {"x1": 1, "y1": 18, "x2": 2, "y2": 6, "color": "#f43f5e", "label": "Branch 2: r = 1/3"},
                    {"x1": 2, "y1": 6, "x2": 3, "y2": 2, "color": "#f43f5e"}
                ],
                "points": [{"x": 1, "y": 2}, {"x": 2, "y": 6}, {"x": 3, "y": 18}, {"x": 1, "y": 18}, {"x": 3, "y": 2}]
            },
            "image_query": "reciprocal geometric progression symmetry 2 6 18 versus 18 6 2",
            "video_query": "geometric progression sum and sum of squares symmetric roots",
            "what_to_explain": "Explain why both sets of terms {2, 6, 18} satisfy both the sum (26) and the sum of squares (364), representing forward and reverse traversals of the same sequence."
        }
    ]

    concept_questions = [
        {
            "concept": "Advanced Recurrences & Factoring",
            "questions": [
                {
                    "question": "How did the cumulative sum recurrence W_n = W_1 + ... + W_{n-2} + 2 simplify to the two-term Fibonacci recurrence?",
                    "type": "conceptual",
                    "ideal_answer": "By taking the difference between two consecutive recurrence expressions W_n and W_{n-1}, all common terms W_1 + ... + W_{n-3} and the constant 2 cancel out, leaving W_n - W_{n-1} = W_{n-2}.",
                    "socratic_hint": "What happens when you subtract W_{n-1} from W_n?"
                },
                {
                    "question": "Why does finding three numbers in GP whose product is given become easier when choosing them as a/r, a, ar?",
                    "type": "conceptual",
                    "ideal_answer": "Because multiplying the three terms (a/r) * a * (ar) causes the common ratio r to cancel completely, leaving a^3 = Product, which immediately reveals the middle term a.",
                    "socratic_hint": "What is (a/r) multiplied by (ar)?"
                }
            ]
        }
    ]

    return {
        "order_index": 6,
        "title": "Advanced Progressions, Algebraic Challenges & Recursive Summations",
        "description": "Tackle competition-grade progression challenges, master symmetric variable selection (a/r, a, ar), apply Sophie Germain factorization to GP squares, and discover Fibonacci numbers from cumulative recurrences.",
        "subtopics": [
            "Slope Invariant Method for Distant AP Terms: d = (a_p - a_q)/(p - q)",
            "Symmetric Triad Selection for GPs with Given Products: a/r, a, ar",
            "Sophie Germain Factorization: 1 + r^2 + r^4 = (1 + r + r^2)(1 - r + r^2)",
            "Equi-Ratio Progression Proof: y/x = z/y implies GP",
            "Telescoping Prefix Sum Recurrences into Doubling Sequences",
            "Fibonacci Sequence Emergence from Shifted Prefix Sums"
        ],
        "key_concepts": [
            "Distant term slope formula: d = (a_p - a_q)/(p - q)",
            "Symmetric GP representation: a/r, a, ar eliminates r in products",
            "Factorization of bi-quadratic forms in GP sum-of-squares problems",
            "Reciprocal symmetry of common ratio solutions: r and 1/r",
            "Reduction of cumulative summations via consecutive differences",
            "Fibonacci recurrence: F_{n} = F_{n-1} + F_{n-2}"
        ],
        "success_criteria": "Students can apply symmetric variable substitutions, factorize quartic progression expressions, derive explicit formulas from telescoping recurrences, and identify Fibonacci sequences.",
        "chapter_notes": "This master module represents the summit of sequences and progressions. By demonstrating how algebraic identities unlock systems of nonlinear equations and how shifted sums generate Fibonacci numbers, students appreciate the deep unity of algebra and geometry.",
        "common_misconceptions": [
            {
                "misconception": "When solving for three GP terms, you must always use a, ar, ar^2.",
                "clarification": "Using a, ar, ar^2 leads to cubics when a product is given. Using a/r, a, ar immediately solves for a since the r factors cancel in the product."
            },
            {
                "misconception": "A recurrence involving all preceding terms cannot be converted into a standard two-term recurrence.",
                "clarification": "Subtracting consecutive terms W_n - W_{n-1} collapses the cumulative history into a local two-term relation."
            }
        ],
        "ai_system_prompt_context": "Show the elegant algebraic cancellation of a/r * a * ar on the chalkboard. Encourage students to look for telescoping cancellations when facing long summation recurrences.",
        "visual_lesson_plan": {
            "title": "Fibonacci Golden Spiral & GP Factoring",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel visual showing the Fibonacci golden spiral decomposition on the left and the algebraic factorization of GP sum of squares on the right.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
