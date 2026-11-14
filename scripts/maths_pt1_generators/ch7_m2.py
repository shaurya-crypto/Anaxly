"""
Chapter 7: The Mathematics of Maybe: Introduction to Probability - Module 2
Curriculum ID: 257078e3-5cf0-4286-a1e3-661ce480edc3
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m2():
    m2_svg = build_cartesian_svg(
        domain=(0, 7), range_y=(0, 3),
        points=[
            {"x": x, "y": y, "label": f"({x}, {'H' if y==1 else 'T'})", "color": "#2563EB"}
            for x in range(1, 7) for y in [1, 2]
        ],
        title="Compound Sample Space: Die (1-6) x Coin (H, T)",
        caption="12 equally likely sample points formed by the Cartesian product of die faces and coin states"
    )

    return {
        "order_index": 2,
        "title": "Textbook Exercise Solver 1: Sample Spaces, Basic Events & Single-Step Classical Probability (Exercise 7.3 & End-of-Chapter Set 2)",
        "description": "Comprehensive step-by-step solutions to Exercise 7.3 (Q1, Q2, Q3) and End-of-Chapter Questions 4, 5, and 6. Master formal notation for sample spaces S, defining events as subsets E subset S, calculating classical probability P(E) = n(E)/n(S) for cards, single dice, 2 coins, 3 coins, and snack-drink combinations, and constructing outfit tables.",
        "subtopics": [
            "Formal definition of sample space S and elementary outcomes",
            "Event definition as a subset of the sample space: E subset S",
            "The Classical Probability Formula: P(E) = n(E) / n(S)",
            "Coin combinations: 2 coins (4 outcomes) and 3 coins (8 outcomes)",
            "Single-die and numbered card probabilities (primes, evens, numbers > 4)",
            "Cartesian product tables: Snack-drink fair choices and shirt-pants outfits"
        ],
        "key_concepts": [
            "Sample Space Cardinality: For independent trials with n1 and n2 outcomes, total outcomes n(S) = n1 * n2.",
            "Coin Invariant: Tossing n coins produces 2^n outcomes in sample space S.",
            "At Least One Head Invariant: P(At least 1 Head in n tosses) = 1 - P(No Heads) = 1 - (1/2)^n.",
            "Complementary Event Rule: P(Not E) = 1 - P(E). For a bag with 3 red out of 6 balls, P(Not Red) = 1 - 3/6 = 1/2.",
            "Outfit Matrix: 2 shirts and 3 pants create 2 * 3 = 6 distinct compound outfit outcomes."
        ],
        "success_criteria": "Students can write out complete sample spaces in set notation, identify favorable outcomes for compound events, compute single-step classical probabilities, and construct Cartesian combination tables.",
        "chapter_notes": "Module 2 formalizes the transition from intuitive chance to set-theoretic sample spaces and combinatorial counting.",
        "common_misconceptions": [
            {"misconception": "Confusing 'at least one head' with 'exactly one head'", "clarification": "'At least one head' includes 1, 2, or 3 heads; only the all-tails outcome is excluded."},
            {"misconception": "Believing order does not matter in two-coin tosses", "clarification": "The outcomes HT and TH are distinct physical events; treating them as one produces an erroneous probability of 1/3 instead of 1/2."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Exercise 7.3 and sample spaces. List sample spaces explicitly in curly braces { } on the digital chalkboard.",
        "visual_lesson_plan": {
            "title": "Visualizing Sample Spaces and Cartesian Products",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Vector Cartesian grid showing 12 sample points for rolling a die (1 to 6) and tossing a coin (H or T).",
            "concept_visuals": [
                {
                    "concept_title": "Two-Coin Sample Space: {HH, HT, TH, TT}",
                    "diagram_title": "4 Equally Likely Outcomes (P = 1/4 Each)",
                    "interactive_math_formula": "S = \\{HH, HT, TH, TT\\}, \\quad n(S) = 4",
                    "mafs_graph_config": {
                        "domain": [-1, 3],
                        "range": [-1, 3],
                        "points": [
                            {"x": 1, "y": 1, "label": "HH (2 Heads)"},
                            {"x": 1, "y": 0, "label": "HT (1 Head)"},
                            {"x": 0, "y": 1, "label": "TH (1 Head)"},
                            {"x": 0, "y": 0, "label": "TT (0 Heads)"}
                        ]
                    },
                    "image_query": "two coins tossed sample space tree diagram grid",
                    "video_query": "sample space of tossing two coins explained",
                    "what_to_explain": "Each toss has 2 outcomes, producing 2^2 = 4 outcomes. At least one head contains 3 outcomes {HH, HT, TH}, giving probability 3/4."
                },
                {
                    "concept_title": "Three Coins Binomial Distribution",
                    "diagram_title": "8 Outcomes: 0H (1/8), 1H (3/8), 2H (3/8), 3H (1/8)",
                    "interactive_math_formula": "P(2H) = \\frac{3}{8}, \\quad \\{HHT, HTH, THH\\}",
                    "mafs_graph_config": {
                        "domain": [-0.5, 3.5],
                        "range": [0, 0.5],
                        "points": [
                            {"x": 0, "y": 0.125, "label": "0 Heads (1/8)"},
                            {"x": 1, "y": 0.375, "label": "1 Head (3/8)"},
                            {"x": 2, "y": 0.375, "label": "2 Heads (3/8)"},
                            {"x": 3, "y": 0.125, "label": "3 Heads (1/8)"}
                        ]
                    },
                    "image_query": "three coins tossed probability distribution bar chart",
                    "video_query": "three coins tossed sample space and probability of 2 heads",
                    "what_to_explain": "Out of 8 total outcomes, exactly 3 have two heads ({HHT, HTH, THH}), giving probability 3/8 = 0.375."
                },
                {
                    "concept_title": "Die Roll and Coin Toss Product Grid",
                    "diagram_title": "6 Die Faces x 2 Coin States = 12 Points",
                    "interactive_math_formula": "n(S) = 6 \\times 2 = 12",
                    "mafs_graph_config": {
                        "domain": [0, 7],
                        "range": [0, 3],
                        "points": [
                            {"x": 1, "y": 1, "label": "(1, H)"}, {"x": 2, "y": 1, "label": "(2, H)"}, {"x": 3, "y": 1, "label": "(3, H)"},
                            {"x": 4, "y": 1, "label": "(4, H)"}, {"x": 5, "y": 1, "label": "(5, H)"}, {"x": 6, "y": 1, "label": "(6, H)"},
                            {"x": 1, "y": 2, "label": "(1, T)"}, {"x": 2, "y": 2, "label": "(2, T)"}, {"x": 3, "y": 2, "label": "(3, T)"},
                            {"x": 4, "y": 2, "label": "(4, T)"}, {"x": 5, "y": 2, "label": "(5, T)"}, {"x": 6, "y": 2, "label": "(6, T)"}
                        ]
                    },
                    "image_query": "rolling a die and flipping a coin sample space lattice",
                    "video_query": "sample space of a die and a coin together",
                    "what_to_explain": "The combined experiment has 6 * 2 = 12 distinct elementary outcomes, each with probability 1/12."
                },
                {
                    "concept_title": "Cards 1 to 10: Even vs Odd Bipartition",
                    "diagram_title": "5 Even Cards out of 10: P(Even) = 5/10 = 1/2",
                    "interactive_math_formula": "P(\\text{Even}) = \\frac{\\{2, 4, 6, 8, 10\\}}{10} = \\frac{5}{10} = 0.5",
                    "mafs_graph_config": {
                        "domain": [0, 11],
                        "range": [-1, 2],
                        "points": [
                            {"x": 2, "y": 1, "label": "2"}, {"x": 4, "y": 1, "label": "4"}, {"x": 6, "y": 1, "label": "6"},
                            {"x": 8, "y": 1, "label": "8"}, {"x": 10, "y": 1, "label": "10"}
                        ]
                    },
                    "image_query": "numbered cards 1 to 10 even numbers probability",
                    "video_query": "probability of drawing even number from cards 1 to 10",
                    "what_to_explain": "Exactly half of the 10 cards are even, giving probability 5/10 = 1/2."
                },
                {
                    "concept_title": "2x3 Outfit Matrix: Shirts vs Pants",
                    "diagram_title": "2 Shirts x 3 Pants = 6 Unique Ensembles",
                    "interactive_math_formula": "2 \\times 3 = 6",
                    "mafs_graph_config": {
                        "domain": [0, 4],
                        "range": [0, 3],
                        "points": [
                            {"x": 1, "y": 1, "label": "(Red, Jeans)"}, {"x": 2, "y": 1, "label": "(Red, Khakis)"}, {"x": 3, "y": 1, "label": "(Red, Shorts)"},
                            {"x": 1, "y": 2, "label": "(Blue, Jeans)"}, {"x": 2, "y": 2, "label": "(Blue, Khakis)"}, {"x": 3, "y": 2, "label": "(Blue, Shorts)"}
                        ]
                    },
                    "image_query": "tree diagram table outfit combinations shirts and pants",
                    "video_query": "fundamental counting principle outfit combinations table",
                    "what_to_explain": "Multiplying the 2 shirt choices by 3 pant choices gives 6 distinct daily outfit combinations."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Sample Spaces & Classical Probability",
                    "questions": [
                        {
                            "question": "When two fair coins are tossed simultaneously, what is the probability of getting at least one head?",
                            "type": "short_answer",
                            "ideal_answer": "3/4 (or 0.75), because 3 of the 4 outcomes in {HH, HT, TH, TT} contain at least one head.",
                            "socratic_hint": "What is the only outcome that does NOT have at least one head?"
                        },
                        {
                            "question": "How many total outcomes exist in the sample space of rolling a 6-sided die and tossing a coin together?",
                            "type": "short_answer",
                            "ideal_answer": "12 outcomes (6 die outcomes * 2 coin outcomes = 12).",
                            "socratic_hint": "Use the fundamental counting principle: multiply the number of outcomes for each independent trial."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 7.3 Q1: When a single 6-sided die is rolled, what is the total number of possible outcomes in the sample space?",
                "given": "A single standard 6-sided die.",
                "formula": "Sample space S is the set of all face numbers.",
                "substitution": "S = {1, 2, 3, 4, 5, 6}.",
                "calculation": "1. The faces of a standard die are marked with dots from 1 to 6.\n2. S = {1, 2, 3, 4, 5, 6}.\n3. Cardinality n(S) = 6.",
                "finalAnswer": "6 possible outcomes (S = {1, 2, 3, 4, 5, 6}).",
                "unit": "outcomes",
                "has_diagram": False
            },
            {
                "problem": "Exercise 7.3 Q2 (i): Write down the sample space S for rolling a die and tossing a coin together.",
                "given": "Experiment: rolling a 6-sided die and tossing a 2-sided coin simultaneously.",
                "formula": "Cartesian product: S = {1, 2, 3, 4, 5, 6} x {H, T}.",
                "substitution": "Pair each die face with both coin faces.",
                "calculation": "1. Die outcomes: {1, 2, 3, 4, 5, 6}.\n2. Coin outcomes: {H, T}.\n3. S = {(1, H), (1, T), (2, H), (2, T), (3, H), (3, T), (4, H), (4, T), (5, H), (5, T), (6, H), (6, T)}.\n4. Total outcomes n(S) = 6 * 2 = 12.",
                "finalAnswer": "S = {(1,H), (1,T), (2,H), (2,T), (3,H), (3,T), (4,H), (4,T), (5,H), (5,T), (6,H), (6,T)} (12 outcomes)",
                "unit": "sample space",
                "has_diagram": True
            },
            {
                "problem": "Exercise 7.3 Q2 (ii): Write down the sample space S for choosing a random integer between -5 and +5.",
                "given": "Random integer strictly between -5 and +5.",
                "formula": "S = {x in Z : -5 < x < 5}.",
                "substitution": "List all integers strictly between -5 and 5.",
                "calculation": "1. Integers strictly between -5 and +5:\n   -4, -3, -2, -1, 0, 1, 2, 3, 4.\n2. S = {-4, -3, -2, -1, 0, 1, 2, 3, 4}.\n3. Total outcomes n(S) = 9 (or 11 if endpoints are included: {-5, ..., 5}).",
                "finalAnswer": "S = {-4, -3, -2, -1, 0, 1, 2, 3, 4} (9 outcomes strictly between -5 and +5).",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Exercise 7.3 Q2 (iii): Write down the sample space S for a box containing 5 green and 7 red balls when one ball is drawn at random.",
                "given": "5 green balls and 7 red balls. Total = 12 balls.",
                "formula": "S can be written by colour {Green, Red} or by distinct balls {G1, ..., G5, R1, ..., R7}.",
                "substitution": "By distinct items: 12 outcomes.",
                "calculation": "1. If balls are distinguished: S = {G1, G2, G3, G4, G5, R1, R2, R3, R4, R5, R6, R7}, with n(S) = 12 equally likely outcomes.\n2. If classified by colour outcome: S = {Green, Red} with P(Green) = 5/12 and P(Red) = 7/12.",
                "finalAnswer": "S = {G1, G2, G3, G4, G5, R1, R2, R3, R4, R5, R6, R7} (12 distinct ball outcomes).",
                "unit": "sample space",
                "has_diagram": False
            },
            {
                "problem": "Exercise 7.3 Q3: At a fair: 3 snacks (Samosa, Pakora, Bhaji) and 2 drinks (Chai, Lassi). (i) List sample space S. (ii) List event 'Selecting Samosa'.",
                "given": "Snacks: {S, P, B}. Drinks: {C, L}.",
                "formula": "Sample space S = Snacks x Drinks.",
                "substitution": "Pair each snack with each drink.",
                "calculation": "1. Part (i): S = {(Samosa, Chai), (Samosa, Lassi), (Pakora, Chai), (Pakora, Lassi), (Bhaji, Chai), (Bhaji, Lassi)}.\n   Total outcomes n(S) = 3 * 2 = 6.\n2. Part (ii): Event E = 'Selecting Samosa as a snack':\n   E = {(Samosa, Chai), (Samosa, Lassi)}.\n   n(E) = 2. Probability P(E) = 2/6 = 1/3.",
                "finalAnswer": "(i) S = {(Samosa, Chai), (Samosa, Lassi), (Pakora, Chai), (Pakora, Lassi), (Bhaji, Chai), (Bhaji, Lassi)}; (ii) E = {(Samosa, Chai), (Samosa, Lassi)}.",
                "unit": "sample space and event",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q4 (i): Two coins are tossed at the same time. What is the probability of getting at least one head?",
                "given": "Two fair coins tossed simultaneously.",
                "formula": "S = {HH, HT, TH, TT}, n(S) = 4. Event E = at least one head.",
                "substitution": "E = {HH, HT, TH}.",
                "calculation": "1. Favourable outcomes: HH (2 heads), HT (1 head), TH (1 head).\n2. Total favourable outcomes n(E) = 3.\n3. P(E) = n(E) / n(S) = 3 / 4 = 0.75.",
                "finalAnswer": "3/4 (or 0.75)",
                "unit": "probability",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q4 (ii): Ten identical cards numbered 1 to 10 are in a box. One card is drawn at random. What is the probability of drawing an even number?",
                "given": "Cards numbered {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. n(S) = 10.",
                "formula": "E = {even numbers in S}. P(E) = n(E) / n(S).",
                "substitution": "E = {2, 4, 6, 8, 10}.",
                "calculation": "1. Favourable outcomes n(E) = 5.\n2. Total cards n(S) = 10.\n3. P(Even) = 5 / 10 = 1 / 2 = 0.5.",
                "finalAnswer": "1/2 (or 0.5)",
                "unit": "probability",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4 (iii): A die is rolled once. What is the probability of getting a number greater than 4?",
                "given": "Single fair 6-sided die. S = {1, 2, 3, 4, 5, 6}, n(S) = 6.",
                "formula": "E = {numbers strictly greater than 4}.",
                "substitution": "E = {5, 6}.",
                "calculation": "1. Favourable outcomes n(E) = 2.\n2. Total outcomes n(S) = 6.\n3. P(Number > 4) = 2 / 6 = 1 / 3 approx 0.333.",
                "finalAnswer": "1/3",
                "unit": "probability",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4 (iv): A bag contains 3 red balls, 2 blue balls, and 1 green ball. One ball is picked at random. What is the probability that it is NOT red?",
                "given": "Balls: 3 red, 2 blue, 1 green. Total n(S) = 3 + 2 + 1 = 6 balls.",
                "formula": "P(Not Red) = 1 - P(Red) or (Blue + Green) / Total.",
                "substitution": "Not red balls = 2 + 1 = 3.",
                "calculation": "1. Number of balls that are not red = 2 (blue) + 1 (green) = 3.\n2. Total balls = 6.\n3. P(Not Red) = 3 / 6 = 1 / 2 = 0.5.",
                "finalAnswer": "1/2 (or 0.5)",
                "unit": "probability",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4 (v): Three coins are tossed simultaneously. What is the probability of getting exactly two heads?",
                "given": "Three fair coins tossed simultaneously. Total outcomes n(S) = 2^3 = 8.",
                "formula": "S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}. E = exactly two heads.",
                "substitution": "E = {HHT, HTH, THH}.",
                "calculation": "1. Favourable outcomes: HHT, HTH, THH.\n2. Number of favourable outcomes n(E) = 3.\n3. Total outcomes n(S) = 8.\n4. P(Exactly 2 Heads) = 3 / 8 = 0.375.",
                "finalAnswer": "3/8 (or 0.375)",
                "unit": "probability",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q5: A bag has 3 candies: strawberry, lemon, and mint. One is picked at random. What is the probability of picking a strawberry candy?",
                "given": "3 distinct candies: {Strawberry, Lemon, Mint}. n(S) = 3.",
                "formula": "P(Strawberry) = 1 / n(S).",
                "substitution": "1 / 3.",
                "calculation": "1. Since the pick is random, all 3 candies are equally likely to be picked.\n2. Favourable outcome = 1 (strawberry).\n3. P(Strawberry) = 1 / 3.",
                "finalAnswer": "1/3",
                "unit": "probability",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q6: A child has 2 shirts (red, blue) and 3 pants (jeans, khakis, shorts). List all combinations in a table format.",
                "given": "2 shirts: {Red, Blue}. 3 pants: {Jeans, Khakis, Shorts}.",
                "formula": "Cartesian grid: Rows = Shirts, Columns = Pants.",
                "substitution": "2 x 3 = 6 combinations.",
                "calculation": "1. Construct 2x3 table:\n   - Row 1 (Red Shirt): (Red, Jeans), (Red, Khakis), (Red, Shorts)\n   - Row 2 (Blue Shirt): (Blue, Jeans), (Blue, Khakis), (Blue, Shorts)\n2. Total distinct outfit combinations = 6.\n3. Each outfit has probability 1/6 of being chosen at random.",
                "finalAnswer": "Table of 6 outfits: {(Red, Jeans), (Red, Khakis), (Red, Shorts), (Blue, Jeans), (Blue, Khakis), (Blue, Shorts)}.",
                "unit": "table",
                "has_diagram": True
            }
        ]
    }
