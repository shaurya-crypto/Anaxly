"""
scripts/maths_pt1_generators/ch8_m5.py
Module 5 for Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Topic: Physical Applications of GP: Bouncing Balls, Bacterial Growth & Sierpiński Carpet Fractal
"""

def get_m5():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Physical Modeling with GP: Fractals &amp; Damped Bounces</text>
  
  <!-- Left Side: Sierpinski Square Carpet Stages 0, 1, 2 -->
  <g transform="translate(60, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Sierpi&nacute;ski Carpet: Area = (8/9)&supn;</text>
    
    <!-- Stage 0: 1 solid square -->
    <rect x="15" y="30" width="60" height="60" fill="#f43f5e" rx="4"/>
    <text x="45" y="110" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1" text-anchor="middle">Stage 0</text>
    <text x="45" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Area = 1</text>
    
    <!-- Stage 1: 3x3 with center hollow -->
    <g transform="translate(100, 30)">
      <rect x="0" y="0" width="75" height="75" fill="#f43f5e" rx="4"/>
      <rect x="25" y="25" width="25" height="25" fill="#0f172a"/>
      <text x="37" y="110" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1" text-anchor="middle">Stage 1</text>
      <text x="37" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">8 squares (8/9)</text>
    </g>
    
    <!-- Stage 2: 8 surrounding sub-carpets -->
    <g transform="translate(200, 30)">
      <rect x="0" y="0" width="90" height="90" fill="#f43f5e" rx="4"/>
      <!-- Main center hole -->
      <rect x="30" y="30" width="30" height="30" fill="#0f172a"/>
      <!-- 8 mini holes -->
      <rect x="10" y="10" width="10" height="10" fill="#0f172a"/>
      <rect x="40" y="10" width="10" height="10" fill="#0f172a"/>
      <rect x="70" y="10" width="10" height="10" fill="#0f172a"/>
      <rect x="10" y="40" width="10" height="10" fill="#0f172a"/>
      <rect x="70" y="40" width="10" height="10" fill="#0f172a"/>
      <rect x="10" y="70" width="10" height="10" fill="#0f172a"/>
      <rect x="40" y="70" width="10" height="10" fill="#0f172a"/>
      <rect x="70" y="70" width="10" height="10" fill="#0f172a"/>
      <text x="45" y="110" font-family="system-ui, sans-serif" font-size="12" fill="#cbd5e1" text-anchor="middle">Stage 2</text>
      <text x="45" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">64 squares (64/81)</text>
    </g>
    
    <text x="150" y="180" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" text-anchor="middle">Square Count: N_n = 8&supn; (Explodes to &infin;)</text>
    <text x="150" y="205" font-family="system-ui, sans-serif" font-size="13" fill="#f43f5e" text-anchor="middle">Carpet Area: A_n = (8/9)&supn; (Decays to 0!)</text>
  </g>
  
  <!-- Right Side: Bouncing Ball Damped Trajectory (80m, r = 0.6) -->
  <g transform="translate(450, 90)">
    <text x="160" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Bouncing Ball Decay: h_k = 80 &times; (0.6)^k</text>
    
    <!-- Ground line -->
    <line x1="10" y1="210" x2="310" y2="210" stroke="#64748b" stroke-width="3"/>
    
    <!-- Bounce 0 (drop from 80m scaled to 160px) -->
    <line x1="30" y1="50" x2="30" y2="210" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
    <circle cx="30" cy="50" r="7" fill="#38bdf8"/>
    <text x="30" y="40" font-family="system-ui, sans-serif" font-size="11" fill="#38bdf8" text-anchor="middle">80m</text>
    
    <!-- Bounce 1 (rebound to 48m scaled to 96px) -->
    <path d="M30,210 Q65,114 100,210" fill="none" stroke="#facc15" stroke-width="2.5"/>
    <circle cx="65" cy="114" r="5" fill="#facc15"/>
    <text x="65" y="105" font-family="system-ui, sans-serif" font-size="11" fill="#facc15" text-anchor="middle">48m</text>
    
    <!-- Bounce 2 (rebound to 28.8m scaled to 57.6px) -->
    <path d="M100,210 Q130,152 160,210" fill="none" stroke="#4ade80" stroke-width="2.5"/>
    <circle cx="130" cy="152" r="5" fill="#4ade80"/>
    <text x="130" y="145" font-family="system-ui, sans-serif" font-size="11" fill="#4ade80" text-anchor="middle">28.8m</text>
    
    <!-- Bounce 3 (rebound to 17.28m) -->
    <path d="M160,210 Q185,175 210,210" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <text x="185" y="170" font-family="system-ui, sans-serif" font-size="10" fill="#38bdf8" text-anchor="middle">17.3m</text>
    
    <!-- Bounce 4 -->
    <path d="M210,210 Q230,189 250,210" fill="none" stroke="#c084fc" stroke-width="2"/>
    <text x="230" y="185" font-family="system-ui, sans-serif" font-size="10" fill="#c084fc" text-anchor="middle">10.4m</text>
    
    <!-- Bounce 5 -->
    <path d="M250,210 Q265,197 280,210" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <text x="265" y="195" font-family="system-ui, sans-serif" font-size="9" fill="#f43f5e" text-anchor="middle">6.2m</text>
    
    <text x="160" y="245" font-family="system-ui, sans-serif" font-size="13" fill="#f8fafc" text-anchor="middle">5th Bounce Peak = 6.22 m</text>
    <text x="160" y="270" font-family="system-ui, sans-serif" font-size="13" fill="#4ade80" font-weight="bold" text-anchor="middle">Total Distance to 6th Impact = 301.34 m</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "Exercise 8.3 Q5 (i): A ball is dropped from a height of 80 metres. After hitting the ground, it bounces back to 60% of the height from which it fell. It continues bouncing in this way — each time rising to 60% of the previous height. What height does the ball reach after the 5th bounce?",
            "given": "Initial drop height h_0 = 80 m. Rebound ratio r = 60% = 0.6.",
            "formula": "Height after kth bounce: h_k = h_0 * r^k",
            "substitution": "h_5 = 80 * (0.6)^5",
            "calculation": "0.6^1 = 0.6\n0.6^2 = 0.36\n0.6^3 = 0.216\n0.6^4 = 0.1296\n0.6^5 = 0.07776\nh_5 = 80 * 0.07776 = 6.2208 m.",
            "finalAnswer": "6.2208 metres (approx 6.22 m)",
            "unit": "metres",
            "has_diagram": True
        },
        {
            "problem": "Exercise 8.3 Q5 (ii): What is the total vertical distance the ball has travelled by the time it hits the ground for the 6th time?",
            "given": "Initial downward drop = 80 m. For bounces 1 through 5, the ball travels upwards and downwards (2 * h_k). The 6th impact concludes the 5th bounce cycle.",
            "formula": "Total Distance D = h_0 + 2 * \\sum_{k=1}^5 h_k = h_0 + 2 * h_0 * r * [ (1 - r^5) / (1 - r) ]",
            "substitution": "D = 80 + 2 * [ 80 * 0.6 * (1 - 0.6^5) / (1 - 0.6) ] = 80 + 2 * [ 48 * (1 - 0.07776) / 0.4 ]",
            "calculation": "1 - 0.07776 = 0.92224.\n48 / 0.4 = 120.\nSum of 5 rebound peaks = 120 * 0.92224 = 110.6688 m.\nTwo-way vertical travel for 5 bounces = 2 * 110.6688 = 221.3376 m.\nTotal distance D = 80 + 221.3376 = 301.3376 m.",
            "finalAnswer": "301.3376 metres",
            "unit": "metres",
            "has_diagram": True
        },
        {
            "problem": "Exercise 8.3 Q6: Which term of the geometric sequence 2, 2*sqrt(2), 4, ... is 128?",
            "given": "Sequence: 2, 2*sqrt(2), 4, ... First term a = 2. Common ratio r = [2*sqrt(2)] / 2 = sqrt(2). Target term = 128.",
            "formula": "t_n = a * r^(n - 1) = 2 * (sqrt(2))^(n - 1)",
            "substitution": "2 * (sqrt(2))^(n - 1) = 128 => (sqrt(2))^(n - 1) = 128 / 2 = 64",
            "calculation": "Express 64 as a power of 2: 64 = 2^6.\nSince sqrt(2) = 2^(1/2), we have: (sqrt(2))^(n - 1) = 2^[(n - 1)/2].\nTherefore, 2^[(n - 1)/2] = 2^6 => (n - 1) / 2 = 6 => n - 1 = 12 => n = 13.",
            "finalAnswer": "128 is the 13th term of the sequence.",
            "unit": "term index",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.3 Q7 (i): In the Sierpiński square carpet fractal (Fig. 8.12), how many red squares are there in Stages 0 to 3?",
            "given": "Stage 0 is 1 single square. At each subsequent stage, each red square is partitioned into 9 smaller squares and the center square is removed, leaving 8 red squares.",
            "formula": "Number of red squares at stage n: N_n = 8^n",
            "substitution": "N_0 = 8^0; N_1 = 8^1; N_2 = 8^2; N_3 = 8^3.",
            "calculation": "N_0 = 1 square.\nN_1 = 8 squares.\nN_2 = 8 * 8 = 64 squares.\nN_3 = 64 * 8 = 512 squares.",
            "finalAnswer": "Stage 0: 1; Stage 1: 8; Stage 2: 64; Stage 3: 512 red squares.",
            "unit": "square count",
            "has_diagram": True
        },
        {
            "problem": "Exercise 8.3 Q7 (ii): Predict the number of red squares in Stages 4 and 5 of the Sierpiński carpet.",
            "given": "Geometric progression N_n = 8^n.",
            "formula": "N_4 = 8^4, N_5 = 8^5",
            "substitution": "N_4 = 512 * 8; N_5 = 4096 * 8.",
            "calculation": "N_4 = 4,096 squares.\nN_5 = 32,768 squares.",
            "finalAnswer": "Stage 4: 4,096 squares; Stage 5: 32,768 squares.",
            "unit": "square count",
            "has_diagram": True
        },
        {
            "problem": "Exercise 8.3 Q7 (iii): Formulate the explicit rule and recursive rule for the number of red squares at the nth stage of the Sierpiński carpet.",
            "given": "Sequence of square counts: 1, 8, 64, 512, 4096, ...",
            "formula": "Explicit: N_n = a * r^n (with a = 1, r = 8). Recursive: N_0 = 1, N_n = r * N_{n - 1}.",
            "substitution": "r = 8, N_0 = 1.",
            "calculation": "Explicit rule: N_n = 8^n (for n >= 0).\nRecursive rule: N_0 = 1, N_n = 8 * N_{n - 1} for n >= 1.",
            "finalAnswer": "Explicit: N_n = 8^n; Recursive: N_0 = 1, N_n = 8 * N_{n-1} (n >= 1).",
            "unit": "fractal formulas",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.3 Q7 (iv): If the area of Stage 0 is 1 square unit, find the area of the red region in Stages 1 to 5. State explicit and recursive rules for area, and describe the asymptotic behavior as n -> infinity.",
            "given": "Initial area A_0 = 1. In each step, the center 1/9th is removed, retaining 8/9th of the area: ratio r = 8/9.",
            "formula": "Explicit: A_n = (8/9)^n. Recursive: A_0 = 1, A_n = (8/9) * A_{n - 1}.",
            "substitution": "A_1 = 8/9 ≈ 0.889; A_2 = 64/81 ≈ 0.790; A_3 = 512/729 ≈ 0.702; A_4 = 4096/6561 ≈ 0.624; A_5 = 32768/59049 ≈ 0.555.",
            "calculation": "As n goes to infinity: since |8/9| < 1, lim_{n -> infinity} (8/9)^n = 0.\nThis reveals a paradoxical fractal property: the perimeter of the boundaries approaches infinity while the total area shrinks to exactly zero!",
            "finalAnswer": "A_1 = 8/9, A_2 = 64/81, A_3 = 512/729, A_4 = 4096/6561, A_5 = 32768/59049. Rule: A_n = (8/9)^n. As n -> infinity, Area -> 0.",
            "unit": "fractal area units",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q7: The number of bacteria in a certain culture doubles every hour. If there were 30 bacteria present in the culture originally, how many bacteria will be present at the end of the 2nd hour, 4th hour, and nth hour?",
            "given": "Initial count at t = 0 is B_0 = 30. Growth factor r = 2 per hour.",
            "formula": "Count at the end of t hours: B(t) = B_0 * 2^t",
            "substitution": "At t = 2: B(2) = 30 * 2^2. At t = 4: B(4) = 30 * 2^4. At t = n: B(n) = 30 * 2^n.",
            "calculation": "B(2) = 30 * 4 = 120 bacteria.\nB(4) = 30 * 16 = 480 bacteria.\nB(n) = 30 * 2^n bacteria.",
            "finalAnswer": "End of 2nd hour: 120; End of 4th hour: 480; End of nth hour: 30 * 2^n bacteria.",
            "unit": "bacteria count",
            "has_diagram": False
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Damped Bouncing Ball Trajectory",
            "diagram_title": "Geometric Peak Attenuation: h_k = 80 * (0.6)^k",
            "interactive_math_formula": "h_k = 80 \\cdot (0.6)^k \\implies \\sum_{k=1}^5 h_k = 110.67 \\text{ m}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 90],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 80, "x2": 0, "y2": 0, "color": "#38bdf8", "label": "Drop: 80m"},
                    {"x1": 1, "y1": 48, "x2": 1, "y2": 0, "color": "#facc15", "label": "Bounce 1: 48m"},
                    {"x1": 2, "y1": 28.8, "x2": 2, "y2": 0, "color": "#4ade80", "label": "Bounce 2: 28.8m"},
                    {"x1": 3, "y1": 17.28, "x2": 3, "y2": 0, "color": "#38bdf8", "label": "Bounce 3: 17.3m"},
                    {"x1": 4, "y1": 10.37, "x2": 4, "y2": 0, "color": "#c084fc", "label": "Bounce 4: 10.4m"},
                    {"x1": 5, "y1": 6.22, "x2": 5, "y2": 0, "color": "#f43f5e", "label": "Bounce 5: 6.22m"}
                ],
                "points": [{"x": 0, "y": 80}, {"x": 1, "y": 48}, {"x": 2, "y": 28.8}, {"x": 3, "y": 17.28}, {"x": 4, "y": 10.37}, {"x": 5, "y": 6.22}]
            },
            "image_query": "bouncing ball geometric progression height decay physics",
            "video_query": "bouncing ball coefficient of restitution geometric series",
            "what_to_explain": "Walk students through the distinction between one-way drop and two-way vertical bounce cycles (up and down)."
        },
        {
            "concept_title": "Sierpiński Carpet Area Vanishing to Zero",
            "diagram_title": "Asymptotic Decay of Retained Area: A_n = (8/9)^n",
            "interactive_math_formula": "\\lim_{n \\to \\infty} \\left(\\frac{8}{9}\\right)^n = 0",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 20],
                "y_range": [0, 1.1],
                "grid": True,
                "curves": [
                    {"fn": "(8/9)^x", "color": "#f43f5e", "label": "Area A_n = (8/9)^n"}
                ],
                "points": [{"x": 0, "y": 1.0}, {"x": 1, "y": 0.889}, {"x": 2, "y": 0.79}, {"x": 5, "y": 0.555}, {"x": 10, "y": 0.308}, {"x": 20, "y": 0.095}]
            },
            "image_query": "sierpinski carpet area decay curve asymptote zero",
            "video_query": "sierpinski carpet fractal dimension area approaching zero",
            "what_to_explain": "Demonstrate the mathematical wonder where infinitely repeated punctures leave an object with zero area yet infinite boundary perimeter."
        },
        {
            "concept_title": "Sierpiński Carpet Square Count Explosion",
            "diagram_title": "Power of 8 Exponential Growth: N_n = 8^n",
            "interactive_math_formula": "N_n = 8^n \\implies N_5 = 32768",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 5.5],
                "y_range": [0, 35000],
                "grid": True,
                "curves": [
                    {"fn": "8^x", "color": "#38bdf8", "label": "Square Count N_n = 8^n"}
                ],
                "points": [{"x": 0, "y": 1}, {"x": 1, "y": 8}, {"x": 2, "y": 64}, {"x": 3, "y": 512}, {"x": 4, "y": 4096}, {"x": 5, "y": 32768}]
            },
            "image_query": "exponential explosion power of 8 graph curve",
            "video_query": "fractal square counting geometric sequence 8 to the power n",
            "what_to_explain": "Contrast the vanishing area with the explosive proliferation of individual constituent squares multiplying eightfold at every stage."
        },
        {
            "concept_title": "Bacterial Doubling Culture Dynamics",
            "diagram_title": "Binary Fission Growth: B(t) = 30 * 2^t",
            "interactive_math_formula": "B(t) = 30 \\cdot 2^t",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 2000],
                "grid": True,
                "curves": [
                    {"fn": "30 * 2^x", "color": "#4ade80", "label": "B(t) = 30 * 2^t"}
                ],
                "points": [{"x": 0, "y": 30}, {"x": 1, "y": 60}, {"x": 2, "y": 120}, {"x": 3, "y": 240}, {"x": 4, "y": 480}, {"x": 5, "y": 960}]
            },
            "image_query": "bacterial growth exponential doubling curve microbiology",
            "video_query": "bacterial culture doubling time geometric progression",
            "what_to_explain": "Explain binary fission: every hour, each bacterium divides into two, leading to exponential population growth."
        },
        {
            "concept_title": "Radical Common Ratio Logarithmic Step",
            "diagram_title": "Base-2 Exponential with Fractional Power: t_n = 2 * (\\sqrt{2})^{n-1}",
            "interactive_math_formula": "t_n = 2 \\cdot 2^{\\frac{n-1}{2}} = 2^{\\frac{n+1}{2}}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 15],
                "y_range": [0, 150],
                "grid": True,
                "curves": [
                    {"fn": "2 * (sqrt(2))^(x - 1)", "color": "#facc15", "label": "t_n = 2 * (sqrt(2))^(n-1)"}
                ],
                "points": [{"x": 1, "y": 2}, {"x": 5, "y": 8}, {"x": 9, "y": 32}, {"x": 13, "y": 128, "label": "t13 = 128"}]
            },
            "image_query": "geometric progression radical common ratio square root 2 graph",
            "video_query": "solving geometric progression with square root common ratio",
            "what_to_explain": "Show how fractional exponents $(\\sqrt{2})^{n-1} = 2^{(n-1)/2}$ convert radical geometric steps into standard linear exponent equations."
        }
    ]

    concept_questions = [
        {
            "concept": "Fractal Geometry & Series Sums",
            "questions": [
                {
                    "question": "In the bouncing ball problem, why do we multiply the bounce heights by 2 when computing total distance?",
                    "type": "conceptual",
                    "ideal_answer": "Because for every bounce after the initial drop, the ball must travel upward to its peak height and then travel downward the exact same distance to hit the ground again.",
                    "socratic_hint": "Does a ball only go up when it bounces, or does it also come back down?"
                },
                {
                    "question": "How can the Sierpiński carpet have zero area when it still has visible structure?",
                    "type": "conceptual",
                    "ideal_answer": "Because the proportion of area retained at each stage is 8/9 < 1. When raised to an infinite power, (8/9)^n converges strictly to 0, leaving behind a fractal dust or boundary of dimension log(8)/log(3) ≈ 1.89.",
                    "socratic_hint": "What happens to (8/9)^n as n becomes 100, 1000, or infinite?"
                }
            ]
        }
    ]

    return {
        "order_index": 5,
        "title": "Physical Applications of GP: Bouncing Balls, Bacterial Growth & Sierpiński Carpet Fractal",
        "description": "Model real-world physical and biological systems using geometric progressions, analyze damping energy loss in bouncing balls, and explore fractal area attenuation in the Sierpiński carpet.",
        "subtopics": [
            "Damped Physical Oscillations: Bouncing Ball Coefficient",
            "Cumulative Distance Traveled with Two-Way Bounce Paths",
            "Radical Common Ratios: Geometric Progression with Irrationals",
            "Self-Similar Fractals: Construction of the Sierpiński Carpet",
            "Exponential Proliferation: Bacterial Fission Dynamics",
            "Asymptotic Limits: Divergent Counts vs Vanishing Area"
        ],
        "key_concepts": [
            "Bounce height recurrence: h_k = h_0 * r^k",
            "Two-way travel sum: Total = h_0 + 2 * \\sum h_k",
            "Radical exponent simplification: (\\sqrt{2})^m = 2^{m/2}",
            "Sierpiński square count: N_n = 8^n",
            "Sierpiński area limit: A_n = (8/9)^n \\to 0 as n \\to \\infty"
        ],
        "success_criteria": "Students can formulate multi-bounce distance equations, solve radical GP equations, calculate fractal area and count progressions, and analyze biological doubling.",
        "chapter_notes": "Mathematics reveals physical reality through geometric progressions. The contrast between an exponentially exploding count and an exponentially decaying area is the foundational hallmark of fractal geometry.",
        "common_misconceptions": [
            {
                "misconception": "The total distance for 5 bounces is just the sum of the drop and peak heights.",
                "clarification": "The initial drop is one-way (downwards), but every rebound travels both upwards and downwards, requiring a factor of 2 for all bounce heights."
            },
            {
                "misconception": "A fractal with infinitely many squares must have infinite area.",
                "clarification": "The squares become microscopic so rapidly that their combined area vanishes to zero, even as their count explodes to infinity."
            }
        ],
        "ai_system_prompt_context": "Draw the bouncing ball arcs clearly on the whiteboard. Emphasize why the first drop is 80m, but the subsequent rebounds are 2 * 48m, 2 * 28.8m, etc.",
        "visual_lesson_plan": {
            "title": "Fractal Geometry & Damped Bounce Physics",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel visual showing the Sierpiński carpet stages on the left and the decaying bounce arcs on the right.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
