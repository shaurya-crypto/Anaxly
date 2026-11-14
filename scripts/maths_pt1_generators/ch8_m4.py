"""
scripts/maths_pt1_generators/ch8_m4.py
Module 4 for Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Topic: Geometric Progressions (GP): Common Ratio, Exponential Growth & Decay
"""

def get_m4():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Geometric Progression: Constant Ratio &amp; Exponential Scaling</text>
  
  <!-- Left Side: Growing Pattern of Squares (Textbook Fig. 8.6: 3, 6, 12, 24) -->
  <g transform="translate(60, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Doubling Squares Pattern: r = 2</text>
    
    <!-- Stage 1: 3 squares -->
    <g transform="translate(10, 160)">
      <rect x="0" y="0" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="16" y="0" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="0" y="16" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <text x="16" y="50" font-family="system-ui, sans-serif" font-size="12" fill="#4ade80" text-anchor="middle">t_1 = 3</text>
    </g>
    
    <!-- Stage 2: 6 squares -->
    <g transform="translate(70, 140)">
      <rect x="0" y="0" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="16" y="0" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="32" y="0" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="0" y="16" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="16" y="16" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="32" y="16" width="16" height="16" fill="#4ade80" stroke="#0f172a" stroke-width="1.5"/>
      <text x="24" y="70" font-family="system-ui, sans-serif" font-size="12" fill="#4ade80" text-anchor="middle">t_2 = 6</text>
    </g>
    
    <!-- Stage 3: 12 squares -->
    <g transform="translate(150, 110)">
      <rect x="0" y="0" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="14" y="0" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="28" y="0" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="42" y="0" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="0" y="14" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="14" y="14" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="28" y="14" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="42" y="14" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="0" y="28" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="14" y="28" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="28" y="28" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <rect x="42" y="28" width="14" height="14" fill="#4ade80" stroke="#0f172a" stroke-width="1"/>
      <text x="28" y="100" font-family="system-ui, sans-serif" font-size="12" fill="#4ade80" text-anchor="middle">t_3 = 12</text>
    </g>
    
    <!-- Stage 4: 24 squares label -->
    <g transform="translate(240, 70)">
      <rect x="0" y="0" width="70" height="140" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" rx="4"/>
      <text x="35" y="70" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle" font-weight="bold">24 Squares</text>
      <text x="35" y="140" font-family="system-ui, sans-serif" font-size="12" fill="#38bdf8" text-anchor="middle">t_4 = 24</text>
    </g>
    
    <text x="150" y="250" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Constant multiplier r = 6/3 = 12/6 = 2</text>
    <text x="150" y="275" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" font-weight="bold" text-anchor="middle">General Term: t_n = 3 &times; 2^{n-1}</text>
  </g>
  
  <!-- Right Side: Exponential Curve vs Alternating GP -->
  <g transform="translate(460, 90)">
    <text x="150" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Continuous Exponential vs Alternating GP</text>
    
    <!-- Curve y = 2 * 1.8^x -->
    <line x1="20" y1="200" x2="300" y2="200" stroke="#475569" stroke-width="2"/>
    <line x1="40" y1="20" x2="40" y2="220" stroke="#475569" stroke-width="2"/>
    
    <!-- Growth curve (cyan) -->
    <path d="M40,195 Q140,185 220,130 T280,30" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <text x="230" y="25" font-family="system-ui, sans-serif" font-size="12" fill="#38bdf8" font-weight="bold">r &gt; 1 (Growth)</text>
    
    <!-- Alternating points (r = -0.5, oscillates above and below zero) -->
    <line x1="40" y1="120" x2="280" y2="120" stroke="#64748b" stroke-dasharray="3,3"/>
    <circle cx="60" cy="50" r="5" fill="#f43f5e"/>
    <circle cx="100" cy="155" r="5" fill="#f43f5e"/>
    <circle cx="140" cy="100" r="5" fill="#f43f5e"/>
    <circle cx="180" cy="130" r="5" fill="#f43f5e"/>
    <circle cx="220" cy="115" r="5" fill="#f43f5e"/>
    <text x="180" y="165" font-family="system-ui, sans-serif" font-size="12" fill="#f43f5e">r &lt; 0 (Oscillating Decay)</text>
    
    <text x="150" y="250" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Exponential behavior depends on sign and magnitude of r</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "Exercise 8.3 Q1 (i & ii): Check whether the following sequences are geometric progressions and determine their common ratios: (i) 2, 4, 8, 16, ... (ii) 5, 25, 125, 625, ....",
            "given": "Sequences: (i) 2, 4, 8, 16, ...; (ii) 5, 25, 125, 625, ...",
            "formula": "A sequence is a GP if the ratio of consecutive terms is constant: t_2/t_1 = t_3/t_2 = ... = r.",
            "substitution": "(i) 4/2 = 2; 8/4 = 2; 16/8 = 2. (ii) 25/5 = 5; 125/25 = 5; 625/125 = 5.",
            "calculation": "In both cases, consecutive ratios are strictly constant.",
            "finalAnswer": "(i) GP with common ratio r = 2; (ii) GP with common ratio r = 5.",
            "unit": "common ratio verification",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.3 Q1 (iii & iv): Check whether the following sequences are geometric progressions and determine their common ratios: (iii) 1, -3, 9, -27, ... (iv) 1/2, 1/4, 1/8, 1/16, ....",
            "given": "Sequences: (iii) 1, -3, 9, -27, ...; (iv) 1/2, 1/4, 1/8, 1/16, ...",
            "formula": "Check ratio invariance: r = t_{k+1} / t_k.",
            "substitution": "(iii) (-3)/1 = -3; 9/(-3) = -3; (-27)/9 = -3. (iv) (1/4)/(1/2) = 1/2; (1/8)/(1/4) = 1/2; (1/16)/(1/8) = 1/2.",
            "calculation": "Both sequences maintain constant consecutive ratios.",
            "finalAnswer": "(iii) Alternating GP with r = -3; (iv) Decaying GP with r = 1/2.",
            "unit": "common ratio verification",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.3 Q2 (i, ii, iii): Write the first five terms of the GP where: (i) a = 4, r = 3; (ii) a = 100, r = -1/2; (iii) a = -2, r = 2.",
            "given": "Parameters (a, r) for three geometric progressions.",
            "formula": "t_n = a * r^(n - 1)",
            "substitution": "(i) 4, 4*3, 4*3^2, 4*3^3, 4*3^4. (ii) 100, 100*(-0.5), 100*(-0.5)^2, 100*(-0.5)^3, 100*(-0.5)^4. (iii) -2, -2*2, -2*2^2, -2*2^3, -2*2^4.",
            "calculation": "(i) 4, 12, 36, 108, 324.\n(ii) 100, -50, 25, -12.5, 6.25.\n(iii) -2, -4, -8, -16, -32.",
            "finalAnswer": "(i) 4, 12, 36, 108, 324; (ii) 100, -50, 25, -12.5, 6.25; (iii) -2, -4, -8, -16, -32",
            "unit": "GP terms",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.3 Q3: For the GP: 3, 9, 27, ..., which term of the sequence is 730? Is 730 a term of this GP?",
            "given": "GP: 3, 9, 27, ... First term a = 3, common ratio r = 9/3 = 3. Candidate term = 730.",
            "formula": "t_n = a * r^(n - 1) = 3 * 3^(n - 1) = 3^n",
            "substitution": "Set 3^n = 730 and solve for integer n.",
            "calculation": "Let us compute consecutive integer powers of 3:\n3^1 = 3, 3^2 = 9, 3^3 = 27, 3^4 = 81, 3^5 = 243, 3^6 = 729, 3^7 = 2187.\nNotice that 729 is the 6th term, and the next term is 2187. There is no positive integer n for which 3^n = 730.",
            "finalAnswer": "730 is NOT a term of this GP (3^6 = 729 and 3^7 = 2187).",
            "unit": "term membership verification",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.3 Q4: Which term of the GP: 2, 6, 18, ... is 4374? Write the explicit formula as well as the recursive formula for the nth term.",
            "given": "GP: 2, 6, 18, ... First term a = 2, common ratio r = 6/2 = 3. Target term t_n = 4374.",
            "formula": "Explicit formula: t_n = a * r^(n - 1) = 2 * 3^(n - 1). Recursive formula: t_1 = 2, t_n = 3 * t_{n - 1} for n >= 2.",
            "substitution": "2 * 3^(n - 1) = 4374 => 3^(n - 1) = 4374 / 2",
            "calculation": "3^(n - 1) = 2187.\nSince 3^7 = 2187, we have n - 1 = 7 => n = 8.",
            "finalAnswer": "4374 is the 8th term. Explicit: t_n = 2 * 3^(n-1); Recursive: t_1 = 2, t_n = 3 * t_{n-1} (n >= 2).",
            "unit": "term index and formulas",
            "has_diagram": False
        },
        {
            "problem": "In-Text Example 9: Check whether the sequence 5, 15/4, 45/16, 135/64, ... is a geometric progression and determine its nth term.",
            "given": "Sequence: t_1 = 5, t_2 = 15/4, t_3 = 45/16, t_4 = 135/64.",
            "formula": "Compute ratios: r_1 = t_2 / t_1; r_2 = t_3 / t_2; r_3 = t_4 / t_3.",
            "substitution": "r_1 = (15/4) / 5 = 15/20 = 3/4.\nr_2 = (45/16) / (15/4) = (45/16) * (4/15) = 3/4.\nr_3 = (135/64) / (45/16) = (135/64) * (16/45) = 3/4.",
            "calculation": "The ratio is constantly 3/4. Therefore it is a GP with a = 5 and r = 3/4.\nThe nth term is t_n = a * r^(n - 1) = 5 * (3/4)^(n - 1).",
            "finalAnswer": "Yes, GP with a = 5, r = 3/4. General term: t_n = 5 * (3/4)^(n - 1).",
            "unit": "GP verification and formula",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q10: Which term of the GP: 2, 8, 32, ... is 131072? Write the explicit formula as well as the recursive formula for the nth term.",
            "given": "GP: 2, 8, 32, ... First term a = 2, common ratio r = 8/2 = 4. Target term = 131072.",
            "formula": "t_n = a * r^(n - 1) = 2 * 4^(n - 1)",
            "substitution": "2 * 4^(n - 1) = 131072 => 4^(n - 1) = 131072 / 2 = 65536",
            "calculation": "Express 65536 as a power of 4: 4^1 = 4, 4^2 = 16, 4^4 = 256, 4^8 = 65536.\nTherefore, 4^(n - 1) = 4^8 => n - 1 = 8 => n = 9.\nRecursive rule: t_1 = 2, t_n = 4 * t_{n - 1} for n >= 2.",
            "finalAnswer": "131072 is the 9th term. Explicit: t_n = 2 * 4^(n-1); Recursive: t_1 = 2, t_n = 4 * t_{n-1} (n >= 2).",
            "unit": "term index and rules",
            "has_diagram": False
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Geometric Progression Exponential Curve",
            "diagram_title": "Explosive Growth: t_n = 2 * 3^{n-1}",
            "interactive_math_formula": "t_n = a \\cdot r^{n-1} \\iff y = a \\cdot r^{x-1}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 9],
                "y_range": [0, 4500],
                "grid": True,
                "curves": [
                    {"fn": "2 * 3^(x - 1)", "color": "#38bdf8", "label": "t_n = 2 * 3^(n-1)"}
                ],
                "points": [
                    {"x": 1, "y": 2, "label": "t1 = 2"},
                    {"x": 2, "y": 6, "label": "t2 = 6"},
                    {"x": 3, "y": 18, "label": "t3 = 18"},
                    {"x": 4, "y": 54, "label": "t4 = 54"},
                    {"x": 8, "y": 4374, "label": "t8 = 4374"}
                ]
            },
            "image_query": "exponential growth geometric progression curve steep rise",
            "video_query": "geometric progression exponential growth rate animation",
            "what_to_explain": "Contrast the explosive curvature of a GP with the constant straight line of an AP. Each unit increase in n scales the value by the factor r."
        },
        {
            "concept_title": "Decaying Geometric Progression",
            "diagram_title": "Fractional Ratio Decay: t_n = 5 * (3/4)^{n-1}",
            "interactive_math_formula": "0 < r < 1 \\implies \\lim_{n \\to \\infty} a \\cdot r^{n-1} = 0",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 10],
                "y_range": [0, 6],
                "grid": True,
                "curves": [
                    {"fn": "5 * (0.75)^(x - 1)", "color": "#4ade80", "label": "t_n = 5 * (0.75)^(n-1)"}
                ],
                "points": [
                    {"x": 1, "y": 5, "label": "t1 = 5"},
                    {"x": 2, "y": 3.75, "label": "t2 = 3.75"},
                    {"x": 3, "y": 2.81, "label": "t3 = 2.81"},
                    {"x": 4, "y": 2.11, "label": "t4 = 2.11"}
                ]
            },
            "image_query": "exponential decay geometric sequence curve approaching zero",
            "video_query": "geometric sequence fractional common ratio decay to zero",
            "what_to_explain": "Explain that when 0 < r < 1, the terms diminish monotonically, approaching zero asymptotically without ever becoming negative."
        },
        {
            "concept_title": "Alternating Oscillations (Negative Ratio r < 0)",
            "diagram_title": "Damped Oscillation: t_n = 100 * (-0.5)^{n-1}",
            "interactive_math_formula": "t_n = 100 \\cdot (-0.5)^{n-1}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 8],
                "y_range": [-60, 110],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": 8, "y2": 0, "color": "#64748b", "label": "y = 0 Axis"}
                ],
                "points": [
                    {"x": 1, "y": 100, "color": "#38bdf8", "label": "t1 = 100"},
                    {"x": 2, "y": -50, "color": "#f43f5e", "label": "t2 = -50"},
                    {"x": 3, "y": 25, "color": "#38bdf8", "label": "t3 = 25"},
                    {"x": 4, "y": -12.5, "color": "#f43f5e", "label": "t4 = -12.5"},
                    {"x": 5, "y": 6.25, "color": "#38bdf8", "label": "t5 = 6.25"}
                ]
            },
            "image_query": "alternating geometric progression oscillating points around axis",
            "video_query": "negative common ratio geometric progression oscillation",
            "what_to_explain": "Show how a negative common ratio forces terms to alternate signs every single step (+, -, +, -, +), creating an oscillatory sequence."
        },
        {
            "concept_title": "Constant Consecutive Ratio Invariance",
            "diagram_title": "Signature Property: t_{n+1} / t_n = r",
            "interactive_math_formula": "\\frac{t_{n+1}}{t_n} = r = \\text{constant} \\quad \\forall n \\ge 1",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 7],
                "y_range": [0, 6],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 3, "x2": 7, "y2": 3, "color": "#facc15", "label": "r = 3 (Ratio Invariant)"}
                ],
                "points": [{"x": 1, "y": 3}, {"x": 2, "y": 3}, {"x": 3, "y": 3}, {"x": 4, "y": 3}, {"x": 5, "y": 3}]
            },
            "image_query": "constant ratio geometric progression invariant horizontal line",
            "video_query": "testing for geometric progression constant quotient",
            "what_to_explain": "Emphasize that the test for a GP is division: the quotient of any term by its immediate predecessor must be identical across the entire sequence."
        },
        {
            "concept_title": "Non-Membership Integer Inversion: 730 vs Powers of 3",
            "diagram_title": "Gap Between Powers: 3^6 = 729 vs 730 vs 3^7 = 2187",
            "interactive_math_formula": "3^6 = 729 < 730 < 2187 = 3^7",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [5.5, 7.5],
                "y_range": [700, 2250],
                "grid": True,
                "curves": [
                    {"fn": "3^x", "color": "#c084fc", "label": "y = 3^x"}
                ],
                "points": [
                    {"x": 6, "y": 729, "label": "3^6 = 729 (Term 6)"},
                    {"x": 6.002, "y": 730, "color": "#f43f5e", "label": "730 (Not an Integer Exponent)"},
                    {"x": 7, "y": 2187, "label": "3^7 = 2187 (Term 7)"}
                ]
            },
            "image_query": "discrete power gap integers sequence non membership",
            "video_query": "how to check if a number is in a geometric sequence",
            "what_to_explain": "Demonstrate that 730 misses 3^6 = 729 by just 1 unit, but because sequence indices must be whole integers, 730 cannot be a term of the sequence."
        }
    ]

    concept_questions = [
        {
            "concept": "GP Definition & Common Ratio",
            "questions": [
                {
                    "question": "Can the common ratio r of a geometric progression be negative or equal to zero?",
                    "type": "conceptual",
                    "ideal_answer": "The common ratio r CAN be negative (causing alternating signs). However, r cannot be zero because dividing by zero is undefined, and subsequent terms would all collapse to zero without an invertible ratio.",
                    "socratic_hint": "What would happen to the quotient t_{n+1} / t_n if r were 0?"
                },
                {
                    "question": "Why is the nth term formula a * r^(n - 1) instead of a * r^n?",
                    "type": "conceptual",
                    "ideal_answer": "Because the first term is a * r^0 = a * 1 = a. The common ratio is applied starting from the second term, meaning the nth term has been multiplied by r exactly (n - 1) times.",
                    "socratic_hint": "How many times do you multiply by r to get from t_1 to t_1?"
                }
            ]
        }
    ]

    return {
        "order_index": 4,
        "title": "Geometric Progressions (GP): Common Ratio, Exponential Growth & Decay",
        "description": "Formulate Geometric Progressions through constant multiplicative scaling, distinguish growth, decay, and alternating oscillations, and master the general term t_n = a * r^(n-1).",
        "subtopics": [
            "Definition of GP: Constant Ratio Invariant t_{n+1}/t_n = r",
            "Common Ratio Regimes: r > 1 (Growth), 0 < r < 1 (Decay), r < 0 (Alternating)",
            "Explicit Formula: t_n = a * r^(n - 1)",
            "Recursive Formula: t_1 = a, t_n = r * t_{n - 1}",
            "Term Membership Testing via Exponent Inversion",
            "Logarithmic and Power Decomposition in Progressions"
        ],
        "key_concepts": [
            "GP defining condition: t_{k+1} / t_k = r",
            "nth term formula: t_n = a * r^(n - 1)",
            "Exponential nature: linear growth in index n produces geometric scaling in value",
            "Sign alternation when r < 0",
            "Strict integer exponent requirement for sequence membership"
        ],
        "success_criteria": "Students can verify whether sequences are GPs, determine common ratios, generate terms from explicit and recursive rules, and solve exponential term index equations.",
        "chapter_notes": "A GP is the multiplicative counterpart of an AP. While an AP adds d at every step, a GP multiplies by r. This fundamental duality between addition and multiplication underlies much of modern mathematics.",
        "common_misconceptions": [
            {
                "misconception": "The nth term of a GP is a * r^n.",
                "clarification": "The first term is a * r^0 = a. Therefore the nth term is a * r^(n - 1)."
            },
            {
                "misconception": "A sequence with alternating signs cannot be a geometric progression.",
                "clarification": "When the common ratio r is negative (e.g. r = -3), terms alternate between positive and negative while maintaining a constant ratio."
            }
        ],
        "ai_system_prompt_context": "Highlight the contrast between AP (repeated addition) and GP (repeated multiplication). Guide students to check consecutive ratios before assuming a sequence is an AP or GP.",
        "visual_lesson_plan": {
            "title": "Geometric Scaling & Exponential Envelopes",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel visual showing doubling square patterns on the left and continuous exponential curves with alternating points on the right.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
