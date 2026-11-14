"""
scripts/maths_pt1_generators/ch7_m4.py
Module 4 for Chapter 7: The Mathematics of Maybe: Introduction to Probability
Topic: Multi-Step Experiments, Compound Events & Tree Diagrams
"""

def get_m4():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Multi-Step Experiments &amp; Probability Tree Diagrams</text>
  
  <!-- Left Panel: Tree Diagram for Fruit Baskets A and B -->
  <g transform="translate(60, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Fruit Selection Tree (Basket A &rarr; Basket B)</text>
    
    <!-- Root -->
    <circle cx="20" cy="150" r="8" fill="#38bdf8"/>
    <text x="5" y="155" font-family="system-ui, sans-serif" font-size="12" fill="#f8fafc" text-anchor="end">Start</text>
    
    <!-- Stage 1 Branches (Basket A: Apple, Orange1, Orange2) -->
    <line x1="28" y1="145" x2="120" y2="70" stroke="#94a3b8" stroke-width="2"/>
    <line x1="28" y1="150" x2="120" y2="150" stroke="#94a3b8" stroke-width="2"/>
    <line x1="28" y1="155" x2="120" y2="230" stroke="#94a3b8" stroke-width="2"/>
    
    <text x="70" y="95" font-family="system-ui, sans-serif" font-size="12" fill="#f43f5e" font-weight="bold">Apple</text>
    <text x="70" y="142" font-family="system-ui, sans-serif" font-size="12" fill="#fb923c" font-weight="bold">Orange 1</text>
    <text x="70" y="205" font-family="system-ui, sans-serif" font-size="12" fill="#fb923c" font-weight="bold">Orange 2</text>
    
    <!-- Nodes Stage 1 -->
    <circle cx="120" cy="70" r="6" fill="#f43f5e"/>
    <circle cx="120" cy="150" r="6" fill="#fb923c"/>
    <circle cx="120" cy="230" r="6" fill="#fb923c"/>
    
    <!-- Stage 2 Branches from Apple -->
    <line x1="126" y1="68" x2="220" y2="40" stroke="#475569" stroke-width="2"/>
    <line x1="126" y1="72" x2="220" y2="90" stroke="#475569" stroke-width="2"/>
    <text x="230" y="45" font-family="system-ui, sans-serif" font-size="12" fill="#facc15">Banana &rarr; (A, B)</text>
    <text x="230" y="95" font-family="system-ui, sans-serif" font-size="12" fill="#4ade80">Mango &rarr; (A, M)</text>
    
    <!-- Stage 2 Branches from Orange 1 -->
    <line x1="126" y1="148" x2="220" y2="130" stroke="#475569" stroke-width="2"/>
    <line x1="126" y1="152" x2="220" y2="170" stroke="#475569" stroke-width="2"/>
    <text x="230" y="135" font-family="system-ui, sans-serif" font-size="12" fill="#facc15">Banana &rarr; (O1, B)</text>
    <text x="230" y="175" font-family="system-ui, sans-serif" font-size="12" fill="#4ade80">Mango &rarr; (O1, M)</text>
    
    <!-- Stage 2 Branches from Orange 2 -->
    <line x1="126" y1="228" x2="220" y2="210" stroke="#475569" stroke-width="2"/>
    <line x1="126" y1="232" x2="220" y2="250" stroke="#475569" stroke-width="2"/>
    <text x="230" y="215" font-family="system-ui, sans-serif" font-size="12" fill="#facc15">Banana &rarr; (O2, B)</text>
    <text x="230" y="255" font-family="system-ui, sans-serif" font-size="12" fill="#4ade80">Mango &rarr; (O2, M)</text>
    
    <text x="170" y="300" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" text-anchor="middle">Total Outcomes n(S) = 3 &times; 2 = 6</text>
  </g>
  
  <!-- Right Panel: Sampling Without Replacement (Balls in Basket) -->
  <g transform="translate(480, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Drawing Without Replacement (4 Red, 5 Blue)</text>
    
    <!-- Stage 1 -->
    <circle cx="30" cy="150" r="8" fill="#38bdf8"/>
    <line x1="38" y1="145" x2="130" y2="90" stroke="#f43f5e" stroke-width="2.5"/>
    <line x1="38" y1="155" x2="130" y2="210" stroke="#38bdf8" stroke-width="2.5"/>
    
    <text x="75" y="105" font-family="system-ui, sans-serif" font-size="12" fill="#f43f5e" font-weight="bold">R (4/9)</text>
    <text x="75" y="195" font-family="system-ui, sans-serif" font-size="12" fill="#38bdf8" font-weight="bold">B (5/9)</text>
    
    <!-- Stage 2 from R -->
    <circle cx="130" cy="90" r="6" fill="#f43f5e"/>
    <line x1="136" y1="86" x2="210" y2="60" stroke="#f43f5e" stroke-width="2"/>
    <line x1="136" y1="94" x2="210" y2="120" stroke="#38bdf8" stroke-width="2"/>
    <text x="215" y="65" font-family="system-ui, sans-serif" font-size="12" fill="#f8fafc">R (3/8) &rarr; RR = 12/72</text>
    <text x="215" y="125" font-family="system-ui, sans-serif" font-size="12" fill="#f8fafc">B (5/8) &rarr; RB = 20/72</text>
    
    <!-- Stage 2 from B -->
    <circle cx="130" cy="210" r="6" fill="#38bdf8"/>
    <line x1="136" y1="206" x2="210" y2="180" stroke="#f43f5e" stroke-width="2"/>
    <line x1="136" y1="214" x2="210" y2="240" stroke="#38bdf8" stroke-width="2"/>
    <text x="215" y="185" font-family="system-ui, sans-serif" font-size="12" fill="#f8fafc">R (4/8) &rarr; BR = 20/72</text>
    <text x="215" y="245" font-family="system-ui, sans-serif" font-size="12" fill="#f8fafc">B (4/8) &rarr; BB = 20/72</text>
    
    <text x="140" y="300" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" text-anchor="middle">Denominator changes from 9 to 8!</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "Exercise 7.4 Q1 (i): There are two fruit baskets A and B. Basket A contains 1 apple and 2 oranges. Basket B contains 1 banana and 1 mango. You randomly pick one fruit from each basket. Draw a tree diagram showing all possible pairs of fruits.",
            "given": "Basket A contents: {Apple, Orange 1, Orange 2}. Basket B contents: {Banana, Mango}.",
            "formula": "Multi-stage tree diagram branching from stage 1 choices to stage 2 choices.",
            "substitution": "Stage 1 has 3 branches (A, O1, O2). From each stage 1 node, Stage 2 has 2 branches (B, M).",
            "calculation": "Total terminal branches = 3 * 2 = 6 branches: (Apple, Banana), (Apple, Mango), (Orange 1, Banana), (Orange 1, Mango), (Orange 2, Banana), (Orange 2, Mango).",
            "finalAnswer": "Tree diagram with 3 primary branches branching into 2 sub-branches each, producing 6 terminal outcomes.",
            "unit": "tree diagram model",
            "has_diagram": True
        },
        {
            "problem": "Exercise 7.4 Q1 (ii): List the complete sample space S for picking one fruit from Basket A and one fruit from Basket B.",
            "given": "Basket A = {A, O1, O2}, Basket B = {B, M}.",
            "formula": "S = { (a, b) : a in Basket A, b in Basket B }",
            "substitution": "Pairs formed by Cartesian product Basket A x Basket B",
            "calculation": "S = {(A, B), (A, M), (O1, B), (O1, M), (O2, B), (O2, M)}. n(S) = 3 * 2 = 6.",
            "finalAnswer": "S = {(A, B), (A, M), (O1, B), (O1, M), (O2, B), (O2, M)}; n(S) = 6",
            "unit": "sample space set",
            "has_diagram": False
        },
        {
            "problem": "Exercise 7.4 Q1 (iii): What is the probability of picking one apple and one banana from the two baskets?",
            "given": "Sample space size n(S) = 6. Basket A has 1 apple, Basket B has 1 banana. Favourable outcome = {(A, B)}, so n(E) = 1.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "P(Apple and Banana) = 1 / 6",
            "calculation": "P = 1 / 6 ≈ 0.1667",
            "finalAnswer": "1/6",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "Exercise 7.4 Q2 (i): A box contains 3 red pens, 4 black pens, and 2 green pens (total 9 pens). You pick a pen without looking and put it back (sampling with replacement). Then your friend does the same. Draw a tree diagram showing the possible outcomes of pen colours.",
            "given": "Box contains 3 Red, 4 Black, 2 Green pens (Total = 9). Since the pen is replaced, probabilities for the second draw are identical to the first.",
            "formula": "Tree diagram with 3 branches at Step 1 (R with P=3/9, B with P=4/9, G with P=2/9), each splitting into 3 branches at Step 2 with the same probabilities.",
            "substitution": "Total outcomes = 3 * 3 = 9 color pairs: {RR, RB, RG, BR, BB, BG, GR, GB, GG}.",
            "calculation": "Total paired outcomes = 9 branches, with path probabilities calculated by multiplying branch values along each path.",
            "finalAnswer": "Tree diagram with 9 branches representing all 9 ordered color combinations with invariant probabilities.",
            "unit": "tree diagram model",
            "has_diagram": True
        },
        {
            "problem": "Exercise 7.4 Q2 (ii): Using the tree diagram for the two pen draws with replacement, calculate the probability that both you and your friend pick pens of the same colour.",
            "given": "Total pens = 9. Probabilities: P(R) = 3/9 = 1/3, P(B) = 4/9, P(G) = 2/9. Both draws are independent with replacement.",
            "formula": "P(Same Colour) = P(RR) + P(BB) + P(GG) = P(R)*P(R) + P(B)*P(B) + P(G)*P(G)",
            "substitution": "P = (3/9 * 3/9) + (4/9 * 4/9) + (2/9 * 2/9)",
            "calculation": "P(RR) = 9/81, P(BB) = 16/81, P(GG) = 4/81. Sum = (9 + 16 + 4) / 81 = 29 / 81.",
            "finalAnswer": "29/81 (approx 0.358)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q10 (i): A basket contains 4 red balls and 5 blue balls (total 9 balls). One ball is drawn and laid aside (without replacement), and a second ball is drawn. What is the probability of drawing a red ball and then a blue ball?",
            "given": "Initial count: 4 Red, 5 Blue (Total = 9). First ball drawn is Red. Remaining balls for second draw: 3 Red, 5 Blue (Total = 8).",
            "formula": "P(R then B) = P(R1) * P(B2 | R1)",
            "substitution": "P(R then B) = (4 / 9) * (5 / 8)",
            "calculation": "P = (4 * 5) / (9 * 8) = 20 / 72 = 5 / 18",
            "finalAnswer": "5/18 (approx 0.278)",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q10 (ii): In the same experiment with 4 red and 5 blue balls drawn without replacement, what is the probability of drawing 2 blue balls?",
            "given": "Initial balls: 9 (4 Red, 5 Blue). First draw Blue: 5/9. Remaining balls: 8 (4 Red, 4 Blue). Second draw Blue: 4/8.",
            "formula": "P(BB) = P(B1) * P(B2 | B1)",
            "substitution": "P(BB) = (5 / 9) * (4 / 8)",
            "calculation": "P = (5 * 4) / (9 * 8) = 20 / 72 = 5 / 18",
            "finalAnswer": "5/18 (approx 0.278)",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q13 (i): A box contains 4 balls numbered 1 to 4. A ball is drawn, and the number is recorded. Then the ball is returned, and a second ball is drawn and recorded (with replacement). Record the sample space using a tree diagram and list all outcomes.",
            "given": "Balls = {1, 2, 3, 4}. Sampling with replacement: 4 choices in draw 1, 4 choices in draw 2.",
            "formula": "Sample Space S1 = { (x, y) : x, y in {1, 2, 3, 4} }",
            "substitution": "Each of 4 first-draw branches splits into 4 second-draw branches.",
            "calculation": "Outcomes: (1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4), (3,1), (3,2), (3,3), (3,4), (4,1), (4,2), (4,3), (4,4). Size n(S1) = 4 * 4 = 16.",
            "finalAnswer": "16 pairs: {(1,1), (1,2), ..., (4,4)}; n(S1) = 16",
            "unit": "sample space pairs",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q13 (ii): A ball is drawn and recorded from the box containing 4 numbered balls {1, 2, 3, 4}. Without replacing the first ball, a second ball is drawn and recorded. Record the sample space.",
            "given": "Balls = {1, 2, 3, 4}. Sampling without replacement: 4 choices for draw 1, 3 remaining choices for draw 2.",
            "formula": "Sample Space S2 = { (x, y) : x, y in {1, 2, 3, 4}, x != y }",
            "substitution": "Pairs where identical numbers (1,1), (2,2), (3,3), (4,4) are excluded.",
            "calculation": "Outcomes: (1,2), (1,3), (1,4), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,3). Size n(S2) = 4 * 3 = 12.",
            "finalAnswer": "12 pairs with distinct coordinates; n(S2) = 12",
            "unit": "sample space pairs",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q13 (iii): Compare the sizes of the two sample spaces in parts (i) and (ii) and explain the mathematical reason for the difference.",
            "given": "n(S1) = 16 (with replacement), n(S2) = 12 (without replacement).",
            "formula": "Difference = n(S1) - n(S2) = 4 * 4 - 4 * 3",
            "substitution": "16 - 12 = 4 outcomes",
            "calculation": "In sampling without replacement, a ball cannot be drawn twice in the same experiment. Therefore, the 4 diagonal pairs (1,1), (2,2), (3,3), (4,4) are impossible, reducing sample space size from 16 to 12.",
            "finalAnswer": "n(S1) = 16, n(S2) = 12. Difference of 4 outcomes corresponds to identical pairs (k, k) being removed.",
            "unit": "count comparison",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q14: List the elements of the sample space for the simultaneous tossing of a fair coin and drawing of a card from a set of 6 cards numbered 1 through 6.",
            "given": "Coin outcomes: {H, T}. Card outcomes: {1, 2, 3, 4, 5, 6}.",
            "formula": "S = { (C, D) : C in {H, T}, D in {1, 2, 3, 4, 5, 6} }",
            "substitution": "Cross product of {H, T} and {1, 2, 3, 4, 5, 6}",
            "calculation": "S = {(H, 1), (H, 2), (H, 3), (H, 4), (H, 5), (H, 6), (T, 1), (T, 2), (T, 3), (T, 4), (T, 5), (T, 6)}. Total outcomes n(S) = 2 * 6 = 12.",
            "finalAnswer": "S = {(H,1), (H,2), (H,3), (H,4), (H,5), (H,6), (T,1), (T,2), (T,3), (T,4), (T,5), (T,6)}; n(S) = 12",
            "unit": "sample space set",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q15: Three fair coins are tossed, and the number of heads is recorded. Which of the following lists is a valid sample space for this experiment? Why do the other lists fail? (i) {1, 2, 3} (ii) {0, 1, 2} (iii) {0, 1, 2, 3, 4} (iv) {0, 1, 2, 3}",
            "given": "Experiment: Toss 3 coins, count number of heads. Possible head counts range from 0 heads (TTT) to 3 heads (HHH).",
            "formula": "A valid sample space must be exhaustive (contain every possible outcome) and mutually exclusive (no duplicate or impossible outcomes).",
            "substitution": "Evaluating candidate lists against possible counts {0, 1, 2, 3}.",
            "calculation": "(i) {1, 2, 3} misses 0 heads (TTT), so not exhaustive. (ii) {0, 1, 2} misses 3 heads (HHH), so not exhaustive. (iii) {0, 1, 2, 3, 4} contains 4 heads, which is impossible with 3 coins. (iv) {0, 1, 2, 3} contains all possible outcomes and no impossible ones.",
            "finalAnswer": "(iv) {0, 1, 2, 3} is the only valid sample space. The others either omit possible outcomes or include impossible ones.",
            "unit": "sample space validation",
            "has_diagram": False
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Hierarchical Tree Diagram Model",
            "diagram_title": "Two-Stage Branching for Sequential Random Experiments",
            "interactive_math_formula": "n(S) = n_1 \\times n_2 = 3 \\times 2 = 6",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 4],
                "y_range": [-3, 3],
                "grid": False,
                "lines": [
                    {"x1": 0.5, "y1": 0, "x2": 2.0, "y2": 1.5, "color": "#f43f5e", "label": "Apple"},
                    {"x1": 0.5, "y1": 0, "x2": 2.0, "y2": 0, "color": "#fb923c", "label": "Orange 1"},
                    {"x1": 0.5, "y1": 0, "x2": 2.0, "y2": -1.5, "color": "#fb923c", "label": "Orange 2"},
                    {"x1": 2.0, "y1": 1.5, "x2": 3.5, "y2": 2.0, "color": "#facc15", "label": "Banana"},
                    {"x1": 2.0, "y1": 1.5, "x2": 3.5, "y2": 1.0, "color": "#4ade80", "label": "Mango"},
                    {"x1": 2.0, "y1": 0, "x2": 3.5, "y2": 0.5, "color": "#facc15", "label": "Banana"},
                    {"x1": 2.0, "y1": 0, "x2": 3.5, "y2": -0.5, "color": "#4ade80", "label": "Mango"},
                    {"x1": 2.0, "y1": -1.5, "x2": 3.5, "y2": -1.0, "color": "#facc15", "label": "Banana"},
                    {"x1": 2.0, "y1": -1.5, "x2": 3.5, "y2": -2.0, "color": "#4ade80", "label": "Mango"}
                ],
                "points": [{"x": 0.5, "y": 0}, {"x": 2, "y": 1.5}, {"x": 2, "y": 0}, {"x": 2, "y": -1.5}]
            },
            "image_query": "probability tree diagram multi step experiment branching",
            "video_query": "how to draw tree diagrams probability high school",
            "what_to_explain": "Walk students along each path of the tree from the root node to the leaves. Multiplying stage choices yields the total number of outcomes."
        },
        {
            "concept_title": "Sampling With vs Without Replacement",
            "diagram_title": "Sample Space Size Comparison (With: n^2 vs Without: n(n-1))",
            "interactive_math_formula": "n(S_{\\text{with}}) = n^2 = 16, \\quad n(S_{\\text{without}}) = n(n-1) = 12",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 5],
                "y_range": [0, 20],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 0, "x2": 1, "y2": 16, "color": "#38bdf8", "label": "With Replacement: 16"},
                    {"x1": 3, "y1": 0, "x2": 3, "y2": 12, "color": "#f43f5e", "label": "Without Replacement: 12"}
                ],
                "points": [{"x": 1, "y": 16}, {"x": 3, "y": 12}]
            },
            "image_query": "sampling with replacement without replacement probability comparison",
            "video_query": "sampling with and without replacement probability tree",
            "what_to_explain": "Explain that without replacement, the item drawn first is removed, reducing both the total number of candidates in subsequent draws and preventing identical pairs."
        },
        {
            "concept_title": "Joint Outcome Coordinate Grid",
            "diagram_title": "Product Space Grid: Coin Toss {H, T} x Card Number {1..6}",
            "interactive_math_formula": "S = \\{H, T\\} \\times \\{1, 2, 3, 4, 5, 6\\}, \\quad n(S) = 2 \\times 6 = 12",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 7],
                "y_range": [0, 3],
                "grid": True,
                "points": [
                    {"x": 1, "y": 1, "label": "(T, 1)"}, {"x": 2, "y": 1, "label": "(T, 2)"},
                    {"x": 3, "y": 1, "label": "(T, 3)"}, {"x": 4, "y": 1, "label": "(T, 4)"},
                    {"x": 5, "y": 1, "label": "(T, 5)"}, {"x": 6, "y": 1, "label": "(T, 6)"},
                    {"x": 1, "y": 2, "label": "(H, 1)"}, {"x": 2, "y": 2, "label": "(H, 2)"},
                    {"x": 3, "y": 2, "label": "(H, 3)"}, {"x": 4, "y": 2, "label": "(H, 4)"},
                    {"x": 5, "y": 2, "label": "(H, 5)"}, {"x": 6, "y": 2, "label": "(H, 6)"}
                ]
            },
            "image_query": "cartesian product probability sample space grid",
            "video_query": "sample space grid method independent events probability",
            "what_to_explain": "Illustrate the 12 outcomes of tossing a coin and drawing a card as a 2-by-6 lattice of points on the Cartesian plane."
        },
        {
            "concept_title": "Multiplication Rule of Dependent Probabilities",
            "diagram_title": "Path Probability in Ball Drawing Without Replacement",
            "interactive_math_formula": "P(R_1 \\cap B_2) = P(R_1) \\times P(B_2 | R_1) = \\frac{4}{9} \\times \\frac{5}{8} = \\frac{5}{18}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 1],
                "y_range": [0, 1],
                "grid": True,
                "lines": [
                    {"x1": 0.444, "y1": 0, "x2": 0.444, "y2": 1, "color": "#f43f5e", "label": "P(R1) = 4/9"},
                    {"x1": 0, "y1": 0.625, "x2": 0.444, "y2": 0.625, "color": "#38bdf8", "label": "P(B2|R1) = 5/8"}
                ],
                "points": [{"x": 0.444, "y": 0.625}]
            },
            "image_query": "conditional probability area model tree diagram",
            "video_query": "probability without replacement conditional probability visual",
            "what_to_explain": "Show how conditional probability modifies the branch probabilities at step 2 because the sample size decreases from 9 to 8."
        },
        {
            "concept_title": "Binomial Distribution of Head Counts in 3 Coin Tosses",
            "diagram_title": "Discrete Probability Distribution of Heads Count {0, 1, 2, 3}",
            "interactive_math_formula": "P(X = k) = \\binom{3}{k} \\left(\\frac{1}{2}\\right)^3, \\quad k \\in \\{0, 1, 2, 3\\}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-0.5, 3.5],
                "y_range": [0, 0.45],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": 0, "y2": 0.125, "color": "#38bdf8", "label": "0 heads: 1/8"},
                    {"x1": 1, "y1": 0, "x2": 1, "y2": 0.375, "color": "#4ade80", "label": "1 head: 3/8"},
                    {"x1": 2, "y1": 0, "x2": 2, "y2": 0.375, "color": "#4ade80", "label": "2 heads: 3/8"},
                    {"x1": 3, "y1": 0, "x2": 3, "y2": 0.125, "color": "#38bdf8", "label": "3 heads: 1/8"}
                ],
                "points": [{"x": 0, "y": 0.125}, {"x": 1, "y": 0.375}, {"x": 2, "y": 0.375}, {"x": 3, "y": 0.125}]
            },
            "image_query": "binomial distribution 3 coin tosses probability histogram",
            "video_query": "three coin tosses sample space distribution animation",
            "what_to_explain": "Show students why {0, 1, 2, 3} is the complete sample space for counting heads in three coin tosses, and explain the symmetric probabilities 1/8, 3/8, 3/8, 1/8."
        }
    ]

    concept_questions = [
        {
            "concept": "Tree Diagrams & Path Rule",
            "questions": [
                {
                    "question": "How do you calculate the probability of a compound outcome along a branch of a tree diagram?",
                    "type": "conceptual",
                    "ideal_answer": "You multiply the probabilities assigned to each segment of the branch from the start node to the terminal node.",
                    "socratic_hint": "If step 1 occurs with probability P(A) and step 2 occurs with probability P(B|A), how do you find P(A and B)?"
                },
                {
                    "question": "Why does drawing without replacement change the probability in the second draw?",
                    "type": "conceptual",
                    "ideal_answer": "Because the total number of items available decreases by 1, and the count of the chosen color also decreases by 1, changing both the denominator and potentially the numerator.",
                    "socratic_hint": "How many total items remain in the basket after removing one without putting it back?"
                }
            ]
        }
    ]

    return {
        "order_index": 4,
        "title": "Multi-Step Experiments, Compound Events & Tree Diagrams",
        "description": "Construct multi-stage tree diagrams to trace sequential random experiments, distinguish between sampling with and without replacement, and master the multiplication rule of probabilities.",
        "subtopics": [
            "Sequential Experiments & Multi-Stage Trials",
            "Tree Diagrams: Branches, Nodes & Path Multiplication",
            "Sampling With vs Without Replacement",
            "Joint Outcomes & Product Sample Spaces",
            "Discrete Probability Mass Functions"
        ],
        "key_concepts": [
            "Tree diagram path multiplication rule: P(A and B) = P(A) * P(B|A)",
            "Sample space size of Cartesian product: n(S) = n1 * n2",
            "Impact of replacement on independence and sample space size",
            "Validation of sample space completeness and exclusivity"
        ],
        "success_criteria": "Students can draw and interpret probability tree diagrams, compute joint probabilities with and without replacement, and define accurate sample spaces for multi-step trials.",
        "chapter_notes": "Sequential events require systematic visualization. Tree diagrams prevent missed combinations and clearly illustrate how conditional choices alter probabilities in real-world scenarios like sampling and testing.",
        "common_misconceptions": [
            {
                "misconception": "Drawing without replacement keeps the denominator unchanged.",
                "clarification": "Removing an item decreases the total count of available items by 1 for all subsequent draws (e.g. from 9 to 8)."
            },
            {
                "misconception": "The sample space for counting heads in 3 coin tosses has size 8.",
                "clarification": "The sequence space has 8 outcomes {HHH, HHT, ...}, but if the experiment specifically measures the *number* of heads, the sample space is {0, 1, 2, 3} of size 4."
            }
        ],
        "ai_system_prompt_context": "Walk students through drawing tree diagrams branch by branch. Emphasize that every branch split must have probabilities that sum to 1.",
        "visual_lesson_plan": {
            "title": "Multi-Step Tree Diagrams & Sequential Sampling",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel tree diagram comparing independent multi-basket picking with dependent sampling without replacement.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
