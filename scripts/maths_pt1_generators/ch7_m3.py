"""
scripts/maths_pt1_generators/ch7_m3.py
Module 3 for Chapter 7: The Mathematics of Maybe: Introduction to Probability
Topic: Statistical Probability, Relative Frequency, Spinner Outcomes & Extreme Events
"""

def get_m3():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Empirical Probability &amp; Octagonal Fair Spinner</text>
  
  <!-- Left Side: Bar Chart for Tyre Lifespan -->
  <g transform="translate(60, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Tyre Replacement Lifespan (n = 1000)</text>
    <line x1="40" y1="280" x2="320" y2="280" stroke="#475569" stroke-width="2"/>
    <line x1="40" y1="40" x2="40" y2="280" stroke="#475569" stroke-width="2"/>
    
    <!-- Bars -->
    <!-- Bar 1: <4000 km (20/1000 = 2%) -->
    <rect x="60" y="268" width="45" height="12" fill="#f43f5e" rx="4"/>
    <text x="82" y="260" font-family="system-ui, sans-serif" font-size="12" fill="#fda4af" text-anchor="middle">2%</text>
    <text x="82" y="300" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">&lt;4k</text>
    
    <!-- Bar 2: 4k-9k km (210/1000 = 21%) -->
    <rect x="125" y="160" width="45" height="120" fill="#fb923c" rx="4"/>
    <text x="147" y="150" font-family="system-ui, sans-serif" font-size="12" fill="#fdba74" text-anchor="middle">21%</text>
    <text x="147" y="300" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">4k-9k</text>
    
    <!-- Bar 3: 9k-14k km (325/1000 = 32.5%) -->
    <rect x="190" y="94" width="45" height="186" fill="#facc15" rx="4"/>
    <text x="212" y="85" font-family="system-ui, sans-serif" font-size="12" fill="#fef08a" text-anchor="middle">32.5%</text>
    <text x="212" y="300" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">9k-14k</text>
    
    <!-- Bar 4: >14k km (445/1000 = 44.5%) -->
    <rect x="255" y="26" width="45" height="254" fill="#4ade80" rx="4"/>
    <text x="277" y="18" font-family="system-ui, sans-serif" font-size="12" fill="#bbf7d0" text-anchor="middle">44.5%</text>
    <text x="277" y="300" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">&gt;14k</text>
  </g>
  
  <!-- Right Side: Octagonal Spinner -->
  <g transform="translate(560, 230)">
    <circle cx="0" cy="0" r="130" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <!-- 8 sectors -->
    <line x1="0" y1="-130" x2="0" y2="130" stroke="#475569" stroke-width="2"/>
    <line x1="-130" y1="0" x2="130" y2="0" stroke="#475569" stroke-width="2"/>
    <line x1="-91.9" y1="-91.9" x2="91.9" y2="91.9" stroke="#475569" stroke-width="2"/>
    <line x1="-91.9" y1="91.9" x2="91.9" y2="-91.9" stroke="#475569" stroke-width="2"/>
    
    <!-- Sector Numbers -->
    <text x="35" y="-85" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">1</text>
    <text x="85" y="-35" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">2</text>
    <text x="85" y="55" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">3</text>
    <text x="35" y="105" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">4</text>
    <text x="-35" y="105" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">5</text>
    <text x="-85" y="55" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">6</text>
    <text x="-85" y="-35" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">7</text>
    <text x="-35" y="-85" font-family="system-ui, sans-serif" font-size="22" fill="#f8fafc" font-weight="bold" text-anchor="middle">8</text>
    
    <!-- Spinner Needle -->
    <polygon points="0,-105 12,20 -12,20" fill="#f43f5e"/>
    <circle cx="0" cy="0" r="14" fill="#38bdf8"/>
    
    <text x="0" y="170" font-family="system-ui, sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Equally Likely Outcomes: S = {1, 2, ..., 8}</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "End-of-Chapter Q7 (i): A tyre manufacturing company kept a record of the distance covered before a tyre needed to be replaced. The table shows results of 1000 cases: Distance < 4000 km: 20; 4001 to 9000 km: 210; 9001 to 14000 km: 325; More than 14000 km: 445. If you buy a tyre of this company, what is the probability that it will need to be replaced before it has covered 4000 km?",
            "given": "Total number of recorded tyre replacement cases N = 1000. Favourable cases where replacement is needed before 4000 km = 20.",
            "formula": "P(E) = (Number of trials in which event E occurred) / (Total number of trials)",
            "substitution": "P(distance < 4000 km) = 20 / 1000",
            "calculation": "P = 20 / 1000 = 2 / 100 = 0.02",
            "finalAnswer": "0.02 (or 2%)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q7 (ii): Using the tyre company data of 1000 cases, find the probability that a randomly chosen tyre will last between 4000 km and 14000 km (i.e. more than 4000 km up to 14000 km).",
            "given": "Total cases N = 1000. Cases for 4001 to 9000 km = 210. Cases for 9001 to 14000 km = 325.",
            "formula": "P(4000 < distance <= 14000) = (Cases in 4001-9000 + Cases in 9001-14000) / Total cases",
            "substitution": "P = (210 + 325) / 1000",
            "calculation": "Sum = 535. P = 535 / 1000 = 0.535",
            "finalAnswer": "0.535 (or 53.5%)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q7 (iii): Using the tyre company data of 1000 cases, find the probability that a tyre will need replacement after it has covered more than 14000 km.",
            "given": "Total cases N = 1000. Cases where distance covered is more than 14000 km = 445.",
            "formula": "P(distance > 14000 km) = (Number of cases > 14000 km) / (Total number of cases)",
            "substitution": "P = 445 / 1000",
            "calculation": "P = 445 / 1000 = 89 / 200 = 0.445",
            "finalAnswer": "0.445 (or 44.5%)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q8 (i): The letters of the word 'PEACE' are placed on five identical cards. Leela draws a card without looking. What is the probability that it is a P, E, or C?",
            "given": "Letters of 'PEACE' are on cards: [P, E, A, C, E]. Total number of cards n(S) = 5. Favourable cards containing P, E, or C: P (1), E (2), C (1).",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "Favourable cards = 1 + 2 + 1 = 4 cards {P, E1, C, E2}. n(S) = 5. P = 4 / 5",
            "calculation": "P = 4 / 5 = 0.8",
            "finalAnswer": "4/5 (or 0.8)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q8 (ii): In the same experiment with the cards [P, E, A, C, E], what is the probability that the drawn card is not an E?",
            "given": "Total cards n(S) = 5. Cards that are 'E' = 2. Cards that are not 'E' = [P, A, C] = 3 cards.",
            "formula": "P(not E) = 1 - P(E) = n(not E) / n(S)",
            "substitution": "P(not E) = 3 / 5",
            "calculation": "P = 3 / 5 = 0.6",
            "finalAnswer": "3/5 (or 0.6)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q9 (i): A game of chance consists of spinning an arrow which comes to rest pointing at one of the numbers 1, 2, 3, 4, 5, 6, 7, 8, and these are equally likely outcomes. What is the probability that it will point at 8?",
            "given": "Sample space S = {1, 2, 3, 4, 5, 6, 7, 8}. Total outcomes n(S) = 8. Event E = {8}, so n(E) = 1.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "P(pointing at 8) = 1 / 8",
            "calculation": "P = 1 / 8 = 0.125",
            "finalAnswer": "1/8",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q9 (ii): For the 8-numbered spinner (1 to 8), what is the probability that the arrow will point at an odd number?",
            "given": "Sample space S = {1, 2, 3, 4, 5, 6, 7, 8}, n(S) = 8. Odd numbers in S = {1, 3, 5, 7}, so n(E) = 4.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "P(odd number) = 4 / 8",
            "calculation": "P = 4 / 8 = 1 / 2 = 0.5",
            "finalAnswer": "1/2",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q9 (iii): For the 8-numbered spinner (1 to 8), what is the probability that the arrow will point at a number greater than 2?",
            "given": "Sample space S = {1, 2, 3, 4, 5, 6, 7, 8}, n(S) = 8. Numbers greater than 2 = {3, 4, 5, 6, 7, 8}, so n(E) = 6.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "P(number > 2) = 6 / 8",
            "calculation": "P = 6 / 8 = 3 / 4 = 0.75",
            "finalAnswer": "3/4",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q9 (iv): For the 8-numbered spinner (1 to 8), what is the probability that the arrow will point at a number less than 9?",
            "given": "Sample space S = {1, 2, 3, 4, 5, 6, 7, 8}, n(S) = 8. Numbers less than 9 in S = {1, 2, 3, 4, 5, 6, 7, 8}, so n(E) = 8.",
            "formula": "P(E) = n(E) / n(S) (Certain Event)",
            "substitution": "P(number < 9) = 8 / 8",
            "calculation": "P = 8 / 8 = 1.0",
            "finalAnswer": "1 (Certain Event)",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q9 (v): For the 8-numbered spinner (1 to 8), what is the probability that the arrow will point at a multiple of 3?",
            "given": "Sample space S = {1, 2, 3, 4, 5, 6, 7, 8}, n(S) = 8. Multiples of 3 in S = {3, 6}, so n(E) = 2.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "P(multiple of 3) = 2 / 8",
            "calculation": "P = 2 / 8 = 1 / 4 = 0.25",
            "finalAnswer": "1/4",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q11: I throw a pair of 6-sided dice. Write down an event that has a probability of 0 (impossible event) and an event that has a probability of 1 (certain event).",
            "given": "Pair of standard 6-sided dice thrown. Sample space S = {(1,1), (1,2), ..., (6,6)}, n(S) = 36. Possible sum ranges from (1+1)=2 to (6+6)=12.",
            "formula": "P(Impossible) = 0, P(Certain) = 1",
            "substitution": "Event A = 'Getting a sum of 13' (or 'getting a number 7 on a die'). No outcome satisfies this, n(A) = 0 => P(A) = 0/36 = 0. Event B = 'Getting a sum between 2 and 12 inclusive'. All 36 outcomes satisfy this, n(B) = 36 => P(B) = 36/36 = 1.",
            "calculation": "P(sum = 13) = 0 / 36 = 0. P(2 <= sum <= 12) = 36 / 36 = 1.",
            "finalAnswer": "Impossible event (P = 0): Sum is 13. Certain event (P = 1): Sum is less than or equal to 12.",
            "unit": "probability demonstration",
            "has_diagram": False
        },
        {
            "problem": "Example 5 (Sampling & Estimation): In a survey of 50 students from one class, 20 prefer mango, 15 prefer apple, 10 prefer banana, and 5 prefer grapes. (i) What is the probability that a randomly chosen student prefers mango? (ii) If the entire school has 1500 students, estimate the number of mangoes needed.",
            "given": "Sample size n = 50. Mango preference count = 20. Total school population N = 1500.",
            "formula": "P(Mango) = (count of mango) / (sample size); Expected school demand = P(Mango) * N",
            "substitution": "P(Mango) = 20 / 50 = 0.4. Expected mangoes = 0.4 * 1500",
            "calculation": "P = 0.4 (40%). Expected count = 0.4 * 1500 = 600",
            "finalAnswer": "P(Mango) = 0.4; Estimated mangoes needed = 600",
            "unit": "probability and student count",
            "has_diagram": False
        },
        {
            "problem": "Example 6 (Gambler's Fallacy in Independent Trials): While playing Snakes and Ladders with a fair 6-sided die, you have rolled three 6s in a row. What is the probability of rolling another 6 on your next roll? Explain why believing a 6 is now impossible is a fallacy.",
            "given": "A fair 6-sided die is rolled. Past outcomes: {6, 6, 6}. Next trial is an independent roll.",
            "formula": "For independent trials, P(A | past history) = P(A) = favourable / total",
            "substitution": "P(rolling a 6) = 1 / 6",
            "calculation": "P = 1 / 6 ≈ 0.1667 (16.67%). The die has no physical memory of previous rolls. Believing previous outcomes influence independent rolls is known as the Gambler's Fallacy.",
            "finalAnswer": "1/6 (approx 16.7%)",
            "unit": "probability value",
            "has_diagram": False
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Relative Frequency Convergence (Law of Large Numbers)",
            "diagram_title": "Empirical vs Theoretical Probability Stabilization",
            "interactive_math_formula": "lim_{N -> \\infty} \\frac{f(E)}{N} = P(E)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 500],
                "y_range": [0, 1],
                "grid": True,
                "curves": [
                    {"fn": "0.5 + 0.3 * exp(-0.02 * x) * sin(0.15 * x)", "color": "#f43f5e", "label": "Relative Frequency of Heads"},
                    {"fn": "0.5", "color": "#38bdf8", "label": "Theoretical Probability P = 0.5"}
                ],
                "points": [{"x": 10, "y": 0.72}, {"x": 50, "y": 0.56}, {"x": 200, "y": 0.51}, {"x": 500, "y": 0.50}]
            },
            "image_query": "relative frequency convergence coin tosses graph",
            "video_query": "law of large numbers simulation coin toss",
            "what_to_explain": "Explain that in a small number of trials, experimental probability fluctuates widely, but as trials increase to hundreds or thousands, the relative frequency steadily converges to the theoretical probability 0.5."
        },
        {
            "concept_title": "Tyre Lifespan Histogram Distribution",
            "diagram_title": "Discrete Probability Distribution of 1000 Replacement Records",
            "interactive_math_formula": "P(X \\in [a, b]) = \\frac{\\sum f_i}{1000}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 20],
                "y_range": [0, 0.55],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0.02, "x2": 4, "y2": 0.02, "color": "#f43f5e", "label": "<4k km: 0.02"},
                    {"x1": 4, "y1": 0.21, "x2": 9, "y2": 0.21, "color": "#fb923c", "label": "4k-9k km: 0.21"},
                    {"x1": 9, "y1": 0.325, "x2": 14, "y2": 0.325, "color": "#facc15", "label": "9k-14k km: 0.325"},
                    {"x1": 14, "y1": 0.445, "x2": 20, "y2": 0.445, "color": "#4ade80", "label": ">14k km: 0.445"}
                ],
                "points": [{"x": 2, "y": 0.02}, {"x": 6.5, "y": 0.21}, {"x": 11.5, "y": 0.325}, {"x": 17, "y": 0.445}]
            },
            "image_query": "step histogram probability distribution tyre wear",
            "video_query": "probability density function step histogram explanation",
            "what_to_explain": "Show how each distance interval forms a discrete probability bar, where the sum of probabilities across all intervals equals exactly 1.0."
        },
        {
            "concept_title": "Octagonal Fair Spinner Geometry",
            "diagram_title": "Uniform Discrete Distribution over 8 Equal Angular Sectors",
            "interactive_math_formula": "P(E_i) = \\frac{\\theta_i}{360^\\circ} = \\frac{45^\\circ}{360^\\circ} = \\frac{1}{8}",
            "mafs_graph_config": {
                "type": "polar",
                "r_max": 4,
                "grid": True,
                "sectors": [
                    {"start_angle": 0, "end_angle": 45, "label": "Sector 1", "color": "#38bdf8"},
                    {"start_angle": 45, "end_angle": 90, "label": "Sector 2", "color": "#94a3b8"},
                    {"start_angle": 90, "end_angle": 135, "label": "Sector 3", "color": "#38bdf8"},
                    {"start_angle": 135, "end_angle": 180, "label": "Sector 4", "color": "#94a3b8"},
                    {"start_angle": 180, "end_angle": 225, "label": "Sector 5", "color": "#38bdf8"},
                    {"start_angle": 225, "end_angle": 270, "label": "Sector 6", "color": "#94a3b8"},
                    {"start_angle": 270, "end_angle": 315, "label": "Sector 7", "color": "#38bdf8"},
                    {"start_angle": 315, "end_angle": 360, "label": "Sector 8", "color": "#94a3b8"}
                ]
            },
            "image_query": "8-sector fair probability spinner wheel",
            "video_query": "circular spinner equal probability angles demonstration",
            "what_to_explain": "Demonstrate that each of the 8 sectors subtends an angle of 45 degrees, giving each sector an identical probability of 1/8. Events like odd numbers encompass 4 alternating sectors (180 degrees total, or P = 1/2)."
        },
        {
            "concept_title": "Sample Size vs Margin of Statistical Error",
            "diagram_title": "Sampling Error Decay Curve (1 / sqrt(N))",
            "interactive_math_formula": "\\text{Standard Error} = \\frac{\\sigma}{\\sqrt{N}} \\propto \\frac{1}{\\sqrt{N}}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 1000],
                "y_range": [0, 0.25],
                "grid": True,
                "curves": [
                    {"fn": "1 / sqrt(x + 16)", "color": "#c084fc", "label": "Sampling Uncertainty sigma / sqrt(N)"}
                ],
                "points": [{"x": 50, "y": 0.12}, {"x": 100, "y": 0.09}, {"x": 500, "y": 0.044}, {"x": 1000, "y": 0.031}]
            },
            "image_query": "sampling error margin of error decay graph",
            "video_query": "sample size effect on estimation accuracy statistics",
            "what_to_explain": "Explain that surveying 50 students provides an estimate with about 14% margin of error, but increasing sample size to 1000 reduces uncertainty down to ~3%, making schoolwide purchasing estimates far more reliable."
        },
        {
            "concept_title": "The Probability Spectrum: Impossible to Certain",
            "diagram_title": "Probability Axis and Event Boundaries [0, 1]",
            "interactive_math_formula": "0 \\le P(E) \\le 1 \\quad (P(\\emptyset) = 0, \\; P(S) = 1)",
            "mafs_graph_config": {
                "type": "number_line",
                "x_range": [0, 1],
                "step": 0.25,
                "points": [
                    {"x": 0.0, "label": "Impossible (P=0: Sum 13 on dice)", "color": "#f43f5e"},
                    {"x": 0.25, "label": "Unlikely (P=0.25: Multiple of 3 on spinner)", "color": "#fb923c"},
                    {"x": 0.5, "label": "Even Chance (P=0.5: Odd number on spinner)", "color": "#facc15"},
                    {"x": 0.75, "label": "Likely (P=0.75: Number > 2 on spinner)", "color": "#38bdf8"},
                    {"x": 1.0, "label": "Certain (P=1: Sum <= 12 on dice)", "color": "#4ade80"}
                ]
            },
            "image_query": "probability scale number line impossible certain 0 to 1",
            "video_query": "probability scale impossible certain even chance video",
            "what_to_explain": "Emphasize that all legitimate mathematical probabilities exist strictly in the closed interval [0, 1]. A probability of 0 signifies an impossible event, while 1 signifies a certain event."
        }
    ]

    concept_questions = [
        {
            "concept": "Empirical vs Theoretical Probability",
            "questions": [
                {
                    "question": "If you toss a coin 10 times and get 8 heads, does this mean the coin is biased?",
                    "type": "conceptual",
                    "ideal_answer": "Not necessarily. In a small sample of 10 tosses, random variation can easily produce 8 heads. Only if the high proportion persists across thousands of tosses can we conclude bias.",
                    "socratic_hint": "What does the Law of Large Numbers tell us about small vs large sample sizes?"
                },
                {
                    "question": "What is the Gambler's Fallacy?",
                    "type": "conceptual",
                    "ideal_answer": "The mistaken belief that past independent events affect future trials, such as believing that rolling three 6s in a row makes a fourth 6 less likely.",
                    "socratic_hint": "Does a physical die have a memory of its previous rolls?"
                }
            ]
        },
        {
            "concept": "Discrete Spinner Probability",
            "questions": [
                {
                    "question": "On an 8-number spinner, why is the probability of pointing at a number less than 9 equal to 1?",
                    "type": "conceptual",
                    "ideal_answer": "Because every number in the sample space {1, 2, 3, 4, 5, 6, 7, 8} is strictly less than 9. Therefore, n(E) = n(S) = 8, making it a certain event with P = 1.",
                    "socratic_hint": "Are there any outcomes on the spinner that are 9 or greater?"
                }
            ]
        }
    ]

    return {
        "order_index": 3,
        "title": "Statistical Probability, Relative Frequency & Discrete Spinner Models",
        "description": "Examine empirical frequency data from real-world records (lifespan tables, preference surveys) and master discrete uniform probability models on symmetric spinners and dice.",
        "subtopics": [
            "Empirical vs Theoretical Probability",
            "Lifespan & Replacement Frequency Tables",
            "Survey Sampling and Population Estimation",
            "The Gambler's Fallacy & Independence of Trials",
            "Uniform Spinners & Event Subsets",
            "Impossible (P=0) and Certain (P=1) Events"
        ],
        "key_concepts": [
            "Relative frequency formula: f / N",
            "Convergence to theoretical probability as N -> infinity",
            "Unbiased sample scaling to total population",
            "Memorylessness of independent random experiments",
            "Event subset counting on uniform 8-sector spinner",
            "Extreme probability bounds: 0 <= P(E) <= 1"
        ],
        "success_criteria": "Students can calculate empirical probabilities from frequency tables, scale sample estimates to populations, dismantle the Gambler's fallacy, and determine subset probabilities on multi-sector spinners.",
        "chapter_notes": "Probability links experience to prediction. Through sample surveys and lifespan tables, students learn how businesses and scientists make informed decisions, while discovering why independent trials remain truly memoryless.",
        "common_misconceptions": [
            {
                "misconception": "If a coin lands on heads 5 times in a row, tails is 'due' on the 6th flip.",
                "clarification": "The coin has no physical memory. Each coin toss is completely independent, with an invariant probability of 0.5."
            },
            {
                "misconception": "A probability can be negative or greater than 100%.",
                "clarification": "Probabilities represent proportions of a universal sample space and must strictly lie in [0, 1] (or 0% to 100%)."
            }
        ],
        "ai_system_prompt_context": "Teach statistical probability through intuitive real-world examples: tyre warranties and fruit orders. Guide students to see how the Gambler's Fallacy arises from our brain seeking patterns in pure randomness.",
        "visual_lesson_plan": {
            "title": "Empirical Frequency & Spinner Geometry Lesson Plan",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel visual showing a tyre replacement frequency histogram on the left and an 8-sector fair spinner on the right.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
