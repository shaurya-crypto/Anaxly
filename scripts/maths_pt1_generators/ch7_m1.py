"""
Chapter 7: The Mathematics of Maybe: Introduction to Probability - Module 1
Curriculum ID: 257078e3-5cf0-4286-a1e3-661ce480edc3
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_probability_scale_tree_svg

def get_m1():
    m1_svg = build_probability_scale_tree_svg(
        type_prob='scale',
        title="The Continuous Probability Scale [0, 1]",
        caption="From Impossible (0) through Even Chance (0.5) to Certain (1.0). Invariant: 0 <= P(E) <= 1"
    )

    return {
        "order_index": 1,
        "title": "The Continuous [0, 1] Probability Scale, Experimental Estimation & Equally Likely Events (Exercises 7.1, 7.2 & End-of-Chapter Set 1)",
        "description": "Comprehensive step-by-step solutions to in-text examples, Exercise 7.1 (all parts), Exercise 7.2 (Q1 to Q4), and End-of-Chapter Questions 1, 2, and 3. Master the continuous probability scale from Impossible (0) to Certain (1), empirical relative frequency from sample surveys, population estimation, and testing whether experimental outcomes are equally likely.",
        "subtopics": [
            "The Continuous Probability Interval: 0 <= P(E) <= 1",
            "Qualitative ranking: Impossible (0), Less Likely, Even Chance (0.5), More Likely, Certain (1.0)",
            "Empirical probability via relative frequency: P(E) = (Frequency of Event) / (Total Trials)",
            "Sample-to-population scaling: Expected count = P(E) * Population Size",
            "Distinction between equally likely and non-equally likely outcomes (fair coins vs starting cars)"
        ],
        "key_concepts": [
            "Probability Axiom 1: For any event E, 0 <= P(E) <= 1.",
            "Probability Axiom 2: P(Impossible Event) = 0 and P(Certain Event) = 1.",
            "Relative Frequency Invariant: Experimental probability is the ratio of observed favourable outcomes to the total number of experimental trials.",
            "Law of Large Numbers: As the number of trials increases indefinitely, the experimental relative frequency converges to the theoretical probability.",
            "Equally Likely Condition: Outcomes are equally likely if there is no physical reason or bias favouring any one outcome over another."
        ],
        "success_criteria": "Students can position real-world events on the [0, 1] probability scale, calculate experimental probabilities from sample data, scale estimates to large populations, and distinguish equally likely experiments.",
        "chapter_notes": "Module 1 establishes the mathematical language of uncertainty and the empirical foundation of relative frequencies.",
        "common_misconceptions": [
            {"misconception": "Thinking probability can be negative or greater than 1", "clarification": "Probability is strictly bounded between 0 and 1 inclusive (or 0% to 100%)."},
            {"misconception": "Assuming an experiment with 2 outcomes is always equally likely", "clarification": "Whether a car starts or does not start has 2 outcomes, but they are not equally likely because a functional car starts almost every time."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Chapter 7 Module 1. Draw the continuous [0, 1] number line scale on the digital chalkboard.",
        "visual_lesson_plan": {
            "title": "Visualizing the Probability Continuum [0, 1]",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Vector probability scale from 0 to 1 with key qualitative milestones and event pins.",
            "concept_visuals": [
                {
                    "concept_title": "The Continuous Probability Scale [0, 1]",
                    "diagram_title": "Milestones: Impossible (0), Unlikely (0.25), Even (0.5), Likely (0.75), Certain (1)",
                    "interactive_math_formula": "0 \\le P(E) \\le 1",
                    "mafs_graph_config": {
                        "domain": [-0.1, 1.1],
                        "range": [-1, 1],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Probability Scale"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "0 (Impossible)"},
                            {"x": 0.25, "y": 0, "label": "0.25 (Unlikely)"},
                            {"x": 0.5, "y": 0, "label": "0.5 (Even Chance)"},
                            {"x": 0.75, "y": 0, "label": "0.75 (Likely)"},
                            {"x": 1.0, "y": 0, "label": "1.0 (Certain)"}
                        ]
                    },
                    "image_query": "probability scale line 0 to 1 impossible even chance certain",
                    "video_query": "probability scale 0 to 1 explained for middle school",
                    "what_to_explain": "Every probability must lie within [0, 1]. Events with probability 0 cannot happen; events with probability 1 are guaranteed."
                },
                {
                    "concept_title": "Relative Frequency vs Population Scaling",
                    "diagram_title": "Sweets Sample: 7/30 Yellow -> 600 * (7/30) = 140",
                    "interactive_math_formula": "E = N \\times P(E) = 600 \\times \\frac{7}{30} = 140",
                    "mafs_graph_config": {
                        "domain": [0, 600],
                        "range": [0, 150],
                        "curves": [
                            {"fn": "(7/30)*x", "color": "#2563EB", "label": "Yellow Expected"}
                        ],
                        "points": [
                            {"x": 30, "y": 7, "label": "Sample (30, 7)"},
                            {"x": 600, "y": 140, "label": "Bag (600, 140)"}
                        ]
                    },
                    "image_query": "sampling ratio population estimate probability linear graph",
                    "video_query": "using sample probability to estimate population size",
                    "what_to_explain": "The empirical fraction 7/30 acts as a constant scaling multiplier to predict 140 yellow sweets in a bag of 600."
                },
                {
                    "concept_title": "Law of Large Numbers: Coin Toss Relative Frequency",
                    "diagram_title": "Convergence to 0.5 as Tosses Increase",
                    "interactive_math_formula": "\\lim_{n \\to \\infty} \\frac{H(n)}{n} = 0.5",
                    "mafs_graph_config": {
                        "domain": [0, 100],
                        "range": [0, 1],
                        "lines": [
                            {"slope": 0, "intercept": 0.5, "color": "#16A34A", "label": "Theoretical P = 0.5"}
                        ],
                        "points": [
                            {"x": 10, "y": 0.7, "label": "10 tosses (0.70)"},
                            {"x": 20, "y": 0.45, "label": "20 tosses (0.45)"},
                            {"x": 50, "y": 0.52, "label": "50 tosses (0.52)"},
                            {"x": 100, "y": 0.50, "label": "100 tosses (0.50)"}
                        ]
                    },
                    "image_query": "law of large numbers coin flip relative frequency graph",
                    "video_query": "law of large numbers coin toss experimental vs theoretical",
                    "what_to_explain": "Small samples fluctuate, but as the number of tosses grows, the experimental fraction stabilizes at exactly 0.5."
                },
                {
                    "concept_title": "Asymmetric Paper Cup Landing Probabilities",
                    "diagram_title": "Non-Equally Likely Physical Orientations",
                    "interactive_math_formula": "P(\\text{Side}) \\gg P(\\text{Bottom}) > P(\\text{Top})",
                    "mafs_graph_config": {
                        "domain": [0, 4],
                        "range": [0, 1],
                        "points": [
                            {"x": 1, "y": 0.15, "label": "Bottom: 15%"},
                            {"x": 2, "y": 0.05, "label": "Top: 5%"},
                            {"x": 3, "y": 0.80, "label": "Side: 80%"}
                        ]
                    },
                    "image_query": "paper cup toss probability landing on side top bottom",
                    "video_query": "paper cup tossing probability experiment",
                    "what_to_explain": "Due to its conical geometry and mass distribution, a paper cup lands on its side far more frequently than on its base."
                },
                {
                    "concept_title": "Equally Likely vs Biased Sample Spaces",
                    "diagram_title": "Fair Die (1/6 Each) vs Biased Bag (3 Red, 7 Blue)",
                    "interactive_math_formula": "P(\\text{Blue}) = \\frac{7}{10} = 0.7 \\ne P(\\text{Red}) = \\frac{3}{10} = 0.3",
                    "mafs_graph_config": {
                        "domain": [0, 5],
                        "range": [0, 1],
                        "points": [
                            {"x": 1, "y": 0.3, "label": "Red (0.3)"},
                            {"x": 2, "y": 0.7, "label": "Blue (0.7)"}
                        ]
                    },
                    "image_query": "equally likely outcomes vs biased probability comparison bar chart",
                    "video_query": "what does equally likely mean in probability",
                    "what_to_explain": "In a bag with 3 red and 7 blue marbles, drawing a blue marble is over twice as likely as drawing a red marble."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Probability Scale & Empirical Scaling",
                    "questions": [
                        {
                            "question": "What is the probability of an impossible event?",
                            "type": "short_answer",
                            "ideal_answer": "0 (zero).",
                            "socratic_hint": "Where does an impossible event sit on the [0, 1] probability scale?"
                        },
                        {
                            "question": "In a sample of 30 sweets, 7 are yellow. If a large bag contains 600 sweets, how many are expected to be yellow?",
                            "type": "short_answer",
                            "ideal_answer": "140 sweets (Expected count = 600 * (7/30) = 140).",
                            "socratic_hint": "Multiply the total count by the sample fraction."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 7.1 Q1: Rank the following events on a scale from 0 to 1 with labels (Impossible, less likely, even chance, more likely, certain) and reasons: (i) Next Monday will come after Sunday; (ii) It will snow in Mumbai in July; (iii) An elephant will walk through your classroom today; (iv) You will greet at least one friend at school tomorrow.",
                "given": "Four real-world statements.",
                "formula": "Probability scale: 0 = Impossible, 0.5 = Even chance, 1.0 = Certain.",
                "substitution": "Assess physical certainty and frequency.",
                "calculation": "1. Event (i): 'The next Monday will come after Sunday.'\n   - By calendar definition, Monday invariably follows Sunday.\n   - Rank: 1.0 (Certain).\n2. Event (ii): 'It will snow in Mumbai in July.'\n   - Mumbai has a tropical coastal climate with July temperatures around 30°C. Snow is physically impossible.\n   - Rank: 0.0 (Impossible).\n3. Event (iii): 'An elephant will walk through your classroom today.'\n   - While theoretically physically possible in rare circumstances, in an urban school setting it is virtually non-existent.\n   - Rank: 0.0 or extremely close to 0 (Impossible / Extremely unlikely).\n4. Event (iv): 'You will greet at least one friend at school tomorrow.'\n   - A student attends school and regularly interacts with peers; it is highly probable.\n   - Rank: ~0.9 (More likely).",
                "finalAnswer": "(i) Certain (1.0); (ii) Impossible (0.0); (iii) Impossible / extremely unlikely (0.0); (iv) More likely (~0.9).",
                "unit": "qualitative rankings",
                "has_diagram": True
            },
            {
                "problem": "Exercise 7.2 Q1: A sample of 30 sweets has 10 red, 8 green, 7 yellow, 5 blue. (i) Calculate P(Green sweet). (ii) In a bag of 600 sweets, estimate the number of yellow sweets.",
                "given": "Sample size N = 30. Counts: Red = 10, Green = 8, Yellow = 7, Blue = 5. Bag size = 600.",
                "formula": "P(E) = Count(E) / N. Estimated Population = Total * P(E).",
                "substitution": "P(Green) = 8 / 30; Estimated Yellow = 600 * (7 / 30).",
                "calculation": "1. Part (i): P(Green) = 8 / 30 = 4 / 15 approx 0.267 (or 26.67%).\n2. Part (ii): Relative frequency of yellow sweets in sample = 7 / 30.\n3. Estimated yellow sweets in large bag of 600:\n   Expected Yellow = 600 * (7 / 30) = 20 * 7 = 140 sweets.",
                "finalAnswer": "(i) P(Green) = 4/15; (ii) Estimated yellow sweets = 140",
                "unit": "probability and count",
                "has_diagram": True
            },
            {
                "problem": "Exercise 7.2 Q2: A survey of 40 students has: 14 Science, 11 Arts, 9 Sports, 6 Debate. Whole school has 800 students. (i) P(Arts)? (ii) Estimate Sports club preference in whole school.",
                "given": "Sample size n = 40. Science = 14, Arts = 11, Sports = 9, Debate = 6. Population N = 800.",
                "formula": "P(E) = n(E) / n. Expected Count = N * P(E).",
                "substitution": "P(Arts) = 11 / 40; Expected Sports = 800 * (9 / 40).",
                "calculation": "1. Part (i): P(Arts) = 11 / 40 = 0.275 (or 27.5%).\n2. Part (ii): P(Sports) = 9 / 40.\n3. In school of 800 students:\n   Expected Sports = 800 * (9 / 40) = 20 * 9 = 180 students.",
                "finalAnswer": "(i) P(Arts) = 11/40 (0.275); (ii) Estimated Sports students = 180",
                "unit": "probability and count",
                "has_diagram": False
            },
            {
                "problem": "Exercise 7.2 Q3: Toss a coin 20 times. (i) Number of heads? (ii) Number of tails? (iii) Experimental P(Heads)? (iv) On the next toss, what is the probability of getting tails?",
                "given": "A trial of 20 coin tosses (e.g. 11 Heads, 9 Tails).",
                "formula": "Experimental P(H) = Heads / 20. Theoretical P(Tails on next toss) = 1/2.",
                "substitution": "Heads = 11, Tails = 9.",
                "calculation": "1. Suppose in 20 tosses we obtain 11 Heads and 9 Tails.\n2. Experimental probability of heads = 11 / 20 = 0.55.\n3. For the 21st toss, the coin has no memory of past tosses (independent trials).\n4. A fair coin still has two equally likely outcomes (Head and Tail).\n5. Therefore, theoretical P(Tails) = 1/2 = 0.5 (or empirical estimate 9/20 = 0.45).",
                "finalAnswer": "(i) 11; (ii) 9; (iii) Experimental P(Heads) = 11/20 = 0.55; (iv) Theoretical P(Tails) on next toss = 1/2 = 0.5.",
                "unit": "experimental probability",
                "has_diagram": True
            },
            {
                "problem": "Exercise 7.2 Q4: Toss a paper cup 100 times. Assign probabilities to landing on bottom, top, or side.",
                "given": "100 tosses of a conical paper cup. Typical empirical data: 12 on bottom, 4 on top, 84 on side.",
                "formula": "P(Orientation) = Observed Count / 100.",
                "substitution": "Bottom = 12/100, Top = 4/100, Side = 84/100.",
                "calculation": "1. Sum of trials = 12 + 4 + 84 = 100.\n2. P(Bottom) = 12 / 100 = 0.12 (12%).\n3. P(Top) = 4 / 100 = 0.04 (4%).\n4. P(Side) = 84 / 100 = 0.84 (84%).\n5. Sum of all probabilities: 0.12 + 0.04 + 0.84 = 1.00 (100%), satisfying the probability axiom.\n6. Notice that the three outcomes are NOT equally likely due to the cup's centre of gravity and curved side.",
                "finalAnswer": "P(Bottom) = 0.12, P(Top) = 0.04, P(Side) = 0.84 (Sum = 1.00; outcomes are not equally likely).",
                "unit": "empirical probabilities",
                "has_diagram": True
            },
            {
                "problem": "Exercise 7.2 Q5: What is the probability of getting an even number when rolling a fair 6-sided die?",
                "given": "A fair 6-sided die. Sample space S = {1, 2, 3, 4, 5, 6}, total outcomes n(S) = 6. Even numbers E = {2, 4, 6}.",
                "formula": "P(E) = n(E) / n(S)",
                "substitution": "n(E) = 3, n(S) = 6. P(Even) = 3 / 6",
                "calculation": "1. Favourable outcomes = {2, 4, 6}, count = 3.\n2. Total outcomes = 6.\n3. P(Even) = 3 / 6 = 1 / 2 = 0.5.",
                "finalAnswer": "1/2 (or 0.5)",
                "unit": "probability value",
                "has_diagram": False
            },
            {
                "problem": "Exercise 7.2 Q6 (i): Suppose you roll a 6-sided die 12 times and get a '3' three times. What is the experimental probability of rolling a '3'?",
                "given": "Total trials N = 12. Frequency of rolling a '3' = 3.",
                "formula": "Experimental P(3) = (Frequency of 3) / (Total number of rolls)",
                "substitution": "P = 3 / 12",
                "calculation": "P = 3 / 12 = 1 / 4 = 0.25",
                "finalAnswer": "1/4 (or 0.25)",
                "unit": "experimental probability",
                "has_diagram": False
            },
            {
                "problem": "Exercise 7.2 Q6 (ii): What is the theoretical probability of rolling a '3' on a fair 6-sided die?",
                "given": "A standard fair 6-sided die. Sample space S = {1, 2, 3, 4, 5, 6}, n(S) = 6. Favourable event E = {3}, n(E) = 1.",
                "formula": "Theoretical P(E) = n(E) / n(S)",
                "substitution": "P(3) = 1 / 6",
                "calculation": "P = 1 / 6 ≈ 0.1667 (16.67%)",
                "finalAnswer": "1/6 (approx 0.167)",
                "unit": "theoretical probability",
                "has_diagram": False
            },
            {
                "problem": "Exercise 7.2 Q6 (iii): Why might the experimental probability (0.25) and theoretical probability (0.167) of rolling a '3' be different? What would you expect to happen if you roll the die 60, 600, or 6000 times?",
                "given": "Comparison of experimental P = 3/12 = 0.25 with theoretical P = 1/6 ≈ 0.167 across 12 trials.",
                "formula": "Law of Large Numbers: lim_{N -> infinity} (Frequency / N) = P_theoretical",
                "substitution": "In small samples (N=12), random fluctuations cause deviation.",
                "calculation": "1. With only 12 rolls, each roll has a large weight (1/12 ≈ 8.3%), so random variance easily produces 3 threes.\n2. As the number of rolls increases to 60, 600, and 6000, random fluctuations average out.\n3. The experimental probability will steadily converge closer and closer to the theoretical value 1/6 (approx 16.7%).",
                "finalAnswer": "Difference is due to small sample variance. With 60, 600, or 6000 rolls, the experimental probability converges towards 1/6 (approx 16.7%).",
                "unit": "convergence analysis",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q1: Fill in the blanks: (i) The probability of an impossible event is ____; (ii) The set of all possible outcomes of a random experiment is called the ____; (iii) The probability of an event that is certain to happen is ____; (iv) Tossing a fair coin has a probability of ____ for getting heads.",
                "given": "Foundational probability definitions.",
                "formula": "Definitions of axiomatic probability.",
                "substitution": "Evaluate each item.",
                "calculation": "1. An impossible event can never occur: P(Impossible) = 0.\n2. The comprehensive set of all possible outcomes is called the Sample Space (denoted by S).\n3. An event certain to occur has probability 1.\n4. A fair coin has 2 equally likely outcomes, so P(Heads) = 1/2 = 0.5.",
                "finalAnswer": "(i) 0; (ii) Sample space; (iii) 1; (iv) 1/2 (or 0.5)",
                "unit": "definitions",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q2: In a survey of 50 students, 15 students said they liked football. The number of students who like football is 15, and the relative frequency is ______.",
                "given": "Sample size N = 50, frequency f = 15.",
                "formula": "Relative frequency = Frequency / Total Sample Size.",
                "substitution": "15 / 50.",
                "calculation": "1. 15 / 50 = 3 / 10 = 0.3.\n2. In percentage: 30%.",
                "finalAnswer": "Relative frequency is 3/10 (or 0.3, or 30%).",
                "unit": "relative frequency",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q3: Which of the following experiments have equally likely outcomes? Explain: (i) Driver attempts to start a car; (ii) Tossing a fair coin once; (iii) Rolling a fair 6-sided die; (iv) Choosing marble from bag of 3 red, 7 blue; (v) A baby is born (boy or girl).",
                "given": "Five experimental scenarios.",
                "formula": "Outcomes are equally likely if each outcome has the exact same probability of occurrence.",
                "substitution": "Analyze physical symmetry and bias.",
                "calculation": "1. (i) Car starts or does not start: NOT equally likely. A normal car starts with very high probability; failure is rare.\n2. (ii) Tossing a fair coin: EQUALLY LIKELY. Symmetrical coin gives P(H) = P(T) = 0.5.\n3. (iii) Rolling a fair 6-sided die: EQUALLY LIKELY. Cube symmetry gives P(1) = P(2) = ... = P(6) = 1/6.\n4. (iv) 3 red and 7 blue marbles: NOT equally likely. P(Blue) = 7/10 is much greater than P(Red) = 3/10.\n5. (v) Baby born boy or girl: EQUALLY LIKELY. Biological sex at birth has essentially equal probability (approx 0.5).",
                "finalAnswer": "(ii), (iii), and (v) have equally likely outcomes. (i) and (iv) do NOT have equally likely outcomes.",
                "unit": "probability analysis",
                "has_diagram": True
            }
        ]
    }
