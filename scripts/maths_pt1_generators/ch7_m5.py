"""
scripts/maths_pt1_generators/ch7_m5.py
Module 5 for Chapter 7: The Mathematics of Maybe: Introduction to Probability
Topic: Advanced Combinatorial Probability, Complement Rule & Geometric Probability
"""

def get_m5():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Geometric Probability &amp; Two-Dice Sum Matrix</text>
  
  <!-- Left Side: Geometric Probability Rectangular Board -->
  <g transform="translate(60, 100)">
    <text x="160" y="-15" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Geometric Probability (Dye Drop Target)</text>
    
    <!-- Outer Rectangle 3m x 2m (scaled to 300px x 200px) -->
    <rect x="10" y="10" width="300" height="200" fill="#1e293b" stroke="#38bdf8" stroke-width="3" rx="8"/>
    
    <!-- Dimension Labels -->
    <text x="160" y="235" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle">Length = 3 m</text>
    <text x="-15" y="115" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" text-anchor="middle" transform="rotate(-90,-15,115)">Breadth = 2 m</text>
    
    <!-- Circular Target: Diameter 1m (scaled radius = 50px) -->
    <circle cx="160" cy="110" r="50" fill="#f43f5e" fill-opacity="0.3" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4,4"/>
    <circle cx="160" cy="110" r="4" fill="#f43f5e"/>
    
    <!-- Radius / Diameter annotation -->
    <line x1="160" y1="110" x2="210" y2="110" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="185" y="102" font-family="system-ui, sans-serif" font-size="11" fill="#f8fafc">r = 0.5 m</text>
    
    <text x="160" y="275" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Area_{rect} = 6 m&sup2; | Area_{circle} = &pi;/4 m&sup2;</text>
    <text x="160" y="295" font-family="system-ui, sans-serif" font-size="14" fill="#4ade80" font-weight="bold" text-anchor="middle">P(landing in circle) = &pi; / 24 &approx; 13.1%</text>
  </g>
  
  <!-- Right Side: Two-Dice Sum Matrix (6x6) highlighting Prime Sums > 5 (7 and 11) -->
  <g transform="translate(480, 100)">
    <text x="140" y="-15" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Two-Dice Matrix: Prime Sums &gt; 5</text>
    
    <!-- Grid -->
    <rect x="20" y="10" width="240" height="240" fill="#1e293b" stroke="#475569" stroke-width="2" rx="4"/>
    
    <!-- Sum 7 Highlight Diagonal: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) -->
    <line x1="20" y1="250" x2="260" y2="10" stroke="#facc15" stroke-width="3" stroke-opacity="0.7"/>
    <text x="140" y="135" font-family="system-ui, sans-serif" font-size="12" fill="#facc15" font-weight="bold" text-anchor="middle">Sum = 7 (6 outcomes)</text>
    
    <!-- Sum 11 Highlight: (5,6), (6,5) -->
    <circle cx="210" cy="50" r="14" fill="#4ade80" fill-opacity="0.4"/>
    <circle cx="170" cy="90" r="14" fill="#4ade80" fill-opacity="0.4"/>
    <text x="205" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#4ade80" font-weight="bold">Sum = 11 (2)</text>
    
    <text x="140" y="280" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Total Favourable = 6 + 2 = 8</text>
    <text x="140" y="300" font-family="system-ui, sans-serif" font-size="14" fill="#38bdf8" font-weight="bold" text-anchor="middle">P(Prime Sum &gt; 5) = 8 / 36 = 2 / 9</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "End-of-Chapter Q12 (i): Two standard 6-sided dice are rolled. Write the sample space and calculate the probability that the sum of the numbers appearing on the two dice is a prime number greater than 5.",
            "given": "Two fair 6-sided dice rolled. Total outcomes n(S) = 6 * 6 = 36. Possible sums range from 2 to 12. Prime numbers greater than 5 in this range are 7 and 11.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "Outcomes with sum 7: {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)} (6 pairs). Outcomes with sum 11: {(5,6), (6,5)} (2 pairs). n(E) = 6 + 2 = 8.",
            "calculation": "P = 8 / 36 = 2 / 9 ≈ 0.222",
            "finalAnswer": "2/9 (approx 22.2%)",
            "unit": "probability value",
            "has_diagram": True
        },
        {
            "problem": "End-of-Chapter Q12 (ii): A bag contains 4 red, 3 green, and 2 blue balls (total 9 balls). Two balls are drawn without replacement. What is the probability that both balls are of different colours?",
            "given": "Balls in bag: 4 Red, 3 Green, 2 Blue (Total N = 9). Two balls drawn without replacement. Total possible pairs = 9 * 8 = 72.",
            "formula": "P(Different Colours) = 1 - P(Same Colour), where P(Same Colour) = P(RR) + P(GG) + P(BB)",
            "substitution": "Pairs with both Red: 4 * 3 = 12. Pairs with both Green: 3 * 2 = 6. Pairs with both Blue: 2 * 1 = 2. Total same colour pairs = 12 + 6 + 2 = 20.",
            "calculation": "P(Same Colour) = 20 / 72. P(Different Colours) = 1 - (20 / 72) = 52 / 72 = 13 / 18 ≈ 0.722",
            "finalAnswer": "13/18 (approx 72.2%)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q12 (iii): Three fair coins are tossed simultaneously. What is the probability that the first coin shows heads and exactly two heads occur in total?",
            "given": "Three coins tossed. Sample space S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}, n(S) = 8. Condition: First coin must be H, and exactly two heads must occur in the three tosses.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "Outcomes with exactly two heads: {HHT, HTH, THH}. Those where the first coin is H: {HHT, HTH}. Favourable count n(E) = 2.",
            "calculation": "P = 2 / 8 = 1 / 4 = 0.25",
            "finalAnswer": "1/4 (or 0.25)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q12 (iv): A four-digit number is formed using the digits 1, 2, 3, and 4 with no repetition. What is the probability that the number formed is an even number?",
            "given": "Digits available: {1, 2, 3, 4}. Total 4-digit permutations without repetition = 4! = 4 * 3 * 2 * 1 = 24. A number is even if and only if its units digit is even (2 or 4).",
            "formula": "P(Even) = n(Even numbers) / Total permutations",
            "substitution": "Choices for units digit: 2 (either 2 or 4). For each choice, the remaining 3 positions can be filled in 3! = 6 ways. Total favourable = 2 * 6 = 12.",
            "calculation": "P = 12 / 24 = 1 / 2 = 0.5",
            "finalAnswer": "1/2 (or 0.5)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q12 (v): A student takes a multiple-choice test with 3 questions, each having 4 options (A, B, C, D), with only one correct answer. What is the probability that the student guesses and gets exactly 2 answers correct?",
            "given": "Number of questions n = 3. For each question, probability of guessing correct p = 1/4, probability of wrong q = 3/4. We seek exactly 2 correct answers (k = 2).",
            "formula": "P(X = 2) = C(3, 2) * p^2 * q^(3-2) = 3 * (1/4)^2 * (3/4)",
            "substitution": "P = 3 * (1/16) * (3/4)",
            "calculation": "P = (3 * 1 * 3) / (16 * 4) = 9 / 64 ≈ 0.1406",
            "finalAnswer": "9/64 (approx 14.06%)",
            "unit": "probability value",
            "has_diagram": False
        },
        {
            "problem": "End-of-Chapter Q16: Suppose you drop a dye at random on a rectangular region of dimensions 3 m by 2 m. What is the probability that it will land inside a circle with a diameter of 1 m placed within the rectangle?",
            "given": "Dimensions of rectangle: length l = 3 m, breadth b = 2 m. Total region Area_total = 3 * 2 = 6 m^2. Diameter of circle d = 1 m => radius r = 0.5 m = 1/2 m.",
            "formula": "P(landing in target) = Area(circle) / Area(total rectangle)",
            "substitution": "Area(circle) = pi * r^2 = pi * (1/2)^2 = pi / 4 m^2. Area(rectangle) = 6 m^2. P = (pi / 4) / 6",
            "calculation": "P = pi / 24 ≈ 3.14159 / 24 ≈ 0.1309 (approx 13.09%)",
            "finalAnswer": "pi/24 (approx 0.1309 or 13.09%)",
            "unit": "geometric probability ratio",
            "has_diagram": True
        },
        {
            "problem": "Example 1 (Large-Scale Empirical Trials): A fair coin is tossed 1000 times. The frequencies observed are: Head: 455, Tail: 545. (i) Compute the experimental probability for each event. (ii) Verify that the sum of probabilities is 1.",
            "given": "Total trials N = 1000. Frequencies: f(H) = 455, f(T) = 545.",
            "formula": "P(E) = f(E) / N; P(H) + P(T) = 1",
            "substitution": "P(H) = 455 / 1000 = 0.455; P(T) = 545 / 1000 = 0.545.",
            "calculation": "P(H) + P(T) = 0.455 + 0.545 = 1.000",
            "finalAnswer": "P(Head) = 0.455; P(Tail) = 0.545; Sum = 1",
            "unit": "empirical probability verification",
            "has_diagram": False
        },
        {
            "problem": "Example 2 (Empirical vs Theoretical Die Probability): Suppose you roll a standard 6-sided die 50 times and it lands on a '4' sixteen times. (i) Calculate the experimental probability of rolling a 4. (ii) Compare this with the theoretical probability.",
            "given": "Number of rolls N = 50. Number of times 4 appeared = 16. Theoretical die has 6 equally likely faces {1, 2, 3, 4, 5, 6}.",
            "formula": "Experimental P(4) = f(4) / N; Theoretical P(4) = 1 / 6",
            "substitution": "Experimental P(4) = 16 / 50 = 0.32. Theoretical P(4) = 1 / 6 ≈ 0.1667.",
            "calculation": "Difference = 0.32 - 0.167 = 0.153 (higher in short run due to random sample variance; with thousands of throws it will converge to 0.167).",
            "finalAnswer": "Experimental P(4) = 16/50 = 0.32; Theoretical P(4) = 1/6 ≈ 0.167",
            "unit": "probability comparison",
            "has_diagram": False
        },
        {
            "problem": "Example 3 (Theoretical Die Probabilities): When rolling a single fair 6-sided die, find: (i) P(even number), (ii) P(number >= 5), (iii) P(number > 6).",
            "given": "Sample space S = {1, 2, 3, 4, 5, 6}, n(S) = 6.",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "(i) Even: {2, 4, 6} => n = 3. (ii) >= 5: {5, 6} => n = 2. (iii) > 6: empty set => n = 0.",
            "calculation": "(i) P = 3 / 6 = 1 / 2. (ii) P = 2 / 6 = 1 / 3. (iii) P = 0 / 6 = 0.",
            "finalAnswer": "(i) 1/2, (ii) 1/3, (iii) 0 (impossible event)",
            "unit": "theoretical probability values",
            "has_diagram": False
        },
        {
            "problem": "Example 4 (Letter Probability in MATHEMATICS): A letter is picked at random from the 11 letters of the word 'MATHEMATICS'. Find the probability that the letter is: (i) 'M', (ii) a vowel, (iii) a consonant.",
            "given": "Word: 'M-A-T-H-E-M-A-T-I-C-S'. Total letters n(S) = 11. Letters count: M: 2, A: 2, T: 2, H: 1, E: 1, I: 1, C: 1, S: 1. Vowels = {A, E, A, I} (4 letters). Consonants = {M, T, H, M, T, C, S} (7 letters).",
            "formula": "P(E) = n(E) / n(S)",
            "substitution": "(i) P(M) = 2 / 11. (ii) P(Vowel) = 4 / 11. (iii) P(Consonant) = 7 / 11.",
            "calculation": "P(Vowel) + P(Consonant) = 4/11 + 7/11 = 11/11 = 1.",
            "finalAnswer": "(i) P(M) = 2/11, (ii) P(Vowel) = 4/11, (iii) P(Consonant) = 7/11",
            "unit": "discrete probability values",
            "has_diagram": False
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Geometric Probability Area Ratio",
            "diagram_title": "Circular Target in Rectangular Field (Area_circle / Area_rect)",
            "interactive_math_formula": "P(\\text{Target}) = \\frac{\\text{Area}(\\text{Circle})}{\\text{Area}(\\text{Rectangle})} = \\frac{\\pi r^2}{l \\times b} = \\frac{\\pi (0.5)^2}{3 \\times 2} = \\frac{\\pi}{24}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 3],
                "y_range": [0, 2],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": 3, "y2": 0, "color": "#38bdf8", "label": "Base = 3m"},
                    {"x1": 3, "y1": 0, "x2": 3, "y2": 2, "color": "#38bdf8", "label": "Height = 2m"},
                    {"x1": 3, "y1": 2, "x2": 0, "y2": 2, "color": "#38bdf8"},
                    {"x1": 0, "y1": 2, "x2": 0, "y2": 0, "color": "#38bdf8"}
                ],
                "points": [{"x": 1.5, "y": 1.0, "label": "Circle Center (r=0.5m)"}]
            },
            "image_query": "geometric probability continuous area ratio dartboard diagram",
            "video_query": "geometric probability rectangle circle dartboard math lesson",
            "what_to_explain": "Explain that when outcomes form a continuous geometric continuum rather than distinct counts, probability is measured as the ratio of target measure (area or length) to total measure."
        },
        {
            "concept_title": "Two-Dice Prime Sum Region",
            "diagram_title": "6x6 Lattice Matrix Highlighting Prime Sums 7 and 11",
            "interactive_math_formula": "P(\\text{Sum} \\in \\{7, 11\\}) = \\frac{6 + 2}{36} = \\frac{8}{36} = \\frac{2}{9}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0.5, 6.5],
                "y_range": [0.5, 6.5],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 6, "x2": 6, "y2": 1, "color": "#facc15", "label": "Sum = 7 Anti-diagonal"}
                ],
                "points": [
                    {"x": 1, "y": 6, "color": "#facc15"}, {"x": 2, "y": 5, "color": "#facc15"},
                    {"x": 3, "y": 4, "color": "#facc15"}, {"x": 4, "y": 3, "color": "#facc15"},
                    {"x": 5, "y": 2, "color": "#facc15"}, {"x": 6, "y": 1, "color": "#facc15"},
                    {"x": 5, "y": 6, "color": "#4ade80", "label": "(5,6) sum=11"},
                    {"x": 6, "y": 5, "color": "#4ade80", "label": "(6,5) sum=11"}
                ]
            },
            "image_query": "two dice sample space 36 grid prime sum highlighted",
            "video_query": "sum of two dice sample space grid visual probability",
            "what_to_explain": "Visualizing the 36 outcomes as a 6x6 lattice makes it simple to trace the diagonal for sum 7 and the pair for sum 11."
        },
        {
            "concept_title": "Complement Rule of Probability",
            "diagram_title": "Decomposition: P(Different Colours) = 1 - P(Same Colour)",
            "interactive_math_formula": "P(E') = 1 - P(E) \\implies P(\\text{Diff}) = 1 - \\frac{20}{72} = \\frac{52}{72} = \\frac{13}{18}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 1],
                "y_range": [0, 1],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0.5, "x2": 0.278, "y2": 0.5, "color": "#f43f5e", "label": "P(Same) = 20/72"},
                    {"x1": 0.278, "y1": 0.5, "x2": 1.0, "y2": 0.5, "color": "#4ade80", "label": "P(Different) = 52/72"}
                ],
                "points": [{"x": 0.278, "y": 0.5, "label": "Boundary: 20/72"}]
            },
            "image_query": "complement rule probability unit interval partitioned",
            "video_query": "complementary events probability 1 minus P of A",
            "what_to_explain": "Highlight the efficiency of using the complement rule: computing 3 cases of same colors is much faster than computing all 6 mixed color cases directly."
        },
        {
            "concept_title": "Binomial Probability of MCQ Guessing",
            "diagram_title": "Discrete PMF for 3 Guessing Trials with p = 0.25",
            "interactive_math_formula": "P(X = k) = \\binom{3}{k} (0.25)^k (0.75)^{3-k}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-0.5, 3.5],
                "y_range": [0, 0.5],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": 0, "y2": 0.422, "color": "#94a3b8", "label": "k=0: 27/64"},
                    {"x1": 1, "y1": 0, "x2": 1, "y2": 0.422, "color": "#94a3b8", "label": "k=1: 27/64"},
                    {"x1": 2, "y1": 0, "x2": 2, "y2": 0.141, "color": "#facc15", "label": "k=2: 9/64"},
                    {"x1": 3, "y1": 0, "x2": 3, "y2": 0.016, "color": "#f43f5e", "label": "k=3: 1/64"}
                ],
                "points": [{"x": 0, "y": 0.422}, {"x": 1, "y": 0.422}, {"x": 2, "y": 0.141}, {"x": 3, "y": 0.016}]
            },
            "image_query": "binomial distribution n=3 p=0.25 probability bar chart",
            "video_query": "binomial probability multiple choice test guessing",
            "what_to_explain": "Show students that guessing on a 4-option MCQ makes getting 2 out of 3 correct relatively unlikely (only 9/64 or 14.1%), while getting 0 or 1 correct dominates (84.4%)."
        },
        {
            "concept_title": "Permutation Even vs Odd Partitions",
            "diagram_title": "Parity Symmetry in 4-Digit Permutations without Repetition",
            "interactive_math_formula": "P(\\text{Even}) = \\frac{2 \\times 3!}{4!} = \\frac{12}{24} = \\frac{1}{2}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 3],
                "y_range": [0, 15],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 0, "x2": 1, "y2": 12, "color": "#38bdf8", "label": "Even Numbers: 12"},
                    {"x1": 2, "y1": 0, "x2": 2, "y2": 12, "color": "#fb923c", "label": "Odd Numbers: 12"}
                ],
                "points": [{"x": 1, "y": 12}, {"x": 2, "y": 12}]
            },
            "image_query": "permutations parity even odd partition bar graph",
            "video_query": "probability of even number permutations combinatorics",
            "what_to_explain": "Explain how the symmetry of digits {1, 2, 3, 4} (two even, two odd) ensures an exact 50-50 split among the 24 possible 4-digit numbers."
        }
    ]

    concept_questions = [
        {
            "concept": "Geometric Probability",
            "questions": [
                {
                    "question": "Why is geometric probability calculated using areas instead of counting outcomes?",
                    "type": "conceptual",
                    "ideal_answer": "Because a continuous geometric region contains infinitely many points. We cannot count points, so we compare continuous measures such as area or length.",
                    "socratic_hint": "Can you count how many individual points exist inside a circle or rectangle?"
                },
                {
                    "question": "What is the advantage of using the complement rule P(A') = 1 - P(A)?",
                    "type": "conceptual",
                    "ideal_answer": "It simplifies calculations when the complement event has far fewer cases to sum than the direct event.",
                    "socratic_hint": "Is it faster to calculate 3 matching color pairs or 6 different color pairs?"
                }
            ]
        }
    ]

    return {
        "order_index": 5,
        "title": "Advanced Combinatorial Probability, Complement Rule & Geometric Probability",
        "description": "Master advanced probability techniques including permutations, binomial MCQ guessing, continuous geometric probability over area regions, and the powerful complement rule.",
        "subtopics": [
            "Prime Sums on Two-Dice Matrices",
            "Combinatorics: Permutations and Parity",
            "The Complement Rule: P(A') = 1 - P(A)",
            "Independent Binomial Trials in Multiple-Choice Tests",
            "Geometric Probability: Continuous Area Ratios",
            "Empirical vs Theoretical Asymptotics in Large Samples"
        ],
        "key_concepts": [
            "Geometric probability formula: Area(Target) / Area(Total)",
            "Complementary events formula: P(A) + P(A') = 1",
            "Permutations without repetition: n! / (n-r)!",
            "Binomial probability formula: C(n, k) * p^k * (1-p)^(n-k)",
            "Two-dice sum distribution symmetry"
        ],
        "success_criteria": "Students can solve complex multi-condition probability problems, apply the complement rule to minimize algebra, compute continuous geometric probabilities, and analyze sample trials.",
        "chapter_notes": "Probability extends into higher-dimensional geometry and combinatorics. Whether dropping objects into continuous targets or counting digit permutations, the core principle remains consistent: measure of favorable outcomes over measure of all possible outcomes.",
        "common_misconceptions": [
            {
                "misconception": "Geometric probability requires counting individual pixels or points.",
                "clarification": "Points are infinitely many; geometric probability is strictly the ratio of geometric measures (length, area, or volume)."
            },
            {
                "misconception": "In an MCQ test, guessing 2 out of 3 questions correct is more likely than guessing 0 correct.",
                "clarification": "With 4 choices per question, P(correct) = 0.25. Getting 0 correct has probability (0.75)^3 = 27/64 ≈ 42.2%, while 2 correct is only 9/64 ≈ 14.1%."
            }
        ],
        "ai_system_prompt_context": "Guide students through geometric probability using spatial intuition. Emphasize how the complement rule saves valuable time in board examinations.",
        "visual_lesson_plan": {
            "title": "Geometric Probability & Combinatorial Sample Spaces",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel graphic showing a 3m x 2m rectangular board with circular target and a 6x6 two-dice sum matrix.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
