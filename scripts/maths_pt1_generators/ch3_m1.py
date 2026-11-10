"""
Chapter 3: The World of Numbers - Module 1
Curriculum ID: 09ca99d2-0489-48f2-8d39-8b26ca7885c9
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_number_line_points_svg

def get_m1():
    m1_svg = build_number_line_points_svg(
        points=[
            {"val": -15, "label": "-15 (Drop)", "color": "#9333EA"},
            {"val": -11, "label": "Midnight -11°C", "color": "#2563EB"},
            {"val": 0, "label": "Śhūnya (0)", "color": "#0F172A"},
            {"val": 4, "label": "Noon +4°C", "color": "#DC2626"}
        ],
        domain=(-16, 8),
        title="Brahmagupta's Number Line: Debts, Fortunes & Shunya",
        caption="Representing temperature drop from +4°C by 15°C to -11°C, demonstrating directed integers"
    )

    return {
        "order_index": 1,
        "title": "The Dawn of Mathematics, Brahmagupta's Śhūnya & Integer Arithmetic (Exercises 3.1 & 3.2 Complete)",
        "description": "Exhaustive step-by-step solutions to in-text historical examples and Exercises 3.1 & 3.2. Explore the Ishango bone prime notches, the revolutionary formalization of zero (Śhūnya) by Brahmagupta (628 CE), debts and fortunes, and complete signed integer operations.",
        "subtopics": [
            "Historical origins of counting: Ishango bone and Harappan base-12 finger joint tally",
            "Closure property of natural numbers under addition vs failure under subtraction",
            "Brahmagupta's formalization of Śhūnya (Zero) and rules of arithmetic (Brahmasphutasiddhanta)",
            "Debts (negative integers) and Fortunes (positive integers) in commerce and temperature",
            "Why subtracting a negative number equals adding a positive number: rigorous real-world modeling"
        ],
        "key_concepts": [
            "Natural Numbers (N): Counting collection {1, 2, 3, ...} closed under addition and multiplication, but open under subtraction.",
            "Brahmagupta's Shunya Invariant: 0 + a = a, 0 - a = -a, a - a = 0, a * 0 = 0.",
            "Signed Multiplication Law: Debt of debt is fortune: (-a) * (-b) = +ab; Debt times fortune is debt: (-a) * (+b) = -ab.",
            "Debt Removal Equivalence: Subtracting a debt of D corresponds algebraically to an increase of wealth by +D: W - (-D) = W + D.",
            "Duodecimal Finger Joint Counting: Four fingers with 3 phalanges each allow counting to 12 on one hand using the thumb as pointer."
        ],
        "success_criteria": "Students can explain the historical emergence of zero and integers, perform operations with positive and negative integers using Brahmagupta's rules, and model commercial transactions and temperature drops.",
        "chapter_notes": "Module 1 establishes the bedrock of number systems, moving from prehistoric tally marks to Brahmagupta's formal arithmetic of zero and directed integers.",
        "common_misconceptions": [
            {"misconception": "Believing natural numbers are closed under subtraction", "clarification": "3 - 5 = -2, which is an integer but not a natural number; closure under subtraction requires the set of all integers Z."},
            {"misconception": "Thinking subtracting a negative decreases the value", "clarification": "Subtracting a negative removes a liability or debt, which strictly increases the net balance: 10 - (-5) = 15."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Chapter 3 Module 1. Use the physical analogy of financial debts and fortunes as Brahmagupta did in 628 CE.",
        "visual_lesson_plan": {
            "title": "Visualizing Directed Numbers on Brahmagupta's Line",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Interactive directed number line showing zero as the balance point between debts (negative) and fortunes (positive).",
            "concept_visuals": [
                {
                    "concept_title": "Integer Line: Noon to Midnight Temperature Drop",
                    "diagram_title": "Temperature Vector: +4°C - 15°C = -11°C",
                    "interactive_math_formula": "4 - 15 = -11",
                    "mafs_graph_config": {
                        "domain": [-16, 6],
                        "range": [-2, 2],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Number Axis"}
                        ],
                        "points": [
                            {"x": 4, "y": 0, "label": "Noon (+4°C)"},
                            {"x": 0, "y": 0, "label": "Freezing Point (0°C)"},
                            {"x": -11, "y": 0, "label": "Midnight (-11°C)"}
                        ]
                    },
                    "image_query": "number line temperature drop positive to negative integers",
                    "video_query": "negative integers number line temperature elevation drop",
                    "what_to_explain": "Starting at +4°C, shifting 15 units to the left passes zero and lands at -11°C."
                },
                {
                    "concept_title": "Removing Debt: Visual Proof that 10 - (-5) = 15",
                    "diagram_title": "Net Worth Vector Translation",
                    "interactive_math_formula": "10 - (-5) = 10 + 5 = 15",
                    "mafs_graph_config": {
                        "domain": [0, 20],
                        "range": [-2, 2],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Asset Line"}
                        ],
                        "points": [
                            {"x": 10, "y": 0, "label": "Initial Fortune (10)"},
                            {"x": 15, "y": 0, "label": "Debt Removed (+5 -> 15)"}
                        ]
                    },
                    "image_query": "subtracting a negative number number line vector addition",
                    "video_query": "why minus minus is plus visual proof number line",
                    "what_to_explain": "Removing a debt of 5 units relieves a burden, increasing the net financial standing to 15."
                },
                {
                    "concept_title": "Ishango Bone Prime Sequence Tally",
                    "diagram_title": "Prime Number Spacing: 11, 13, 17, 19, 23, 29, 31",
                    "interactive_math_formula": "P = {11, 13, 17, 19, 23, 29, 31}",
                    "mafs_graph_config": {
                        "domain": [10, 35],
                        "range": [-2, 2],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#94A3B8", "label": "Tally Axis"}
                        ],
                        "points": [
                            {"x": 11, "y": 0, "label": "11"},
                            {"x": 13, "y": 0, "label": "13"},
                            {"x": 17, "y": 0, "label": "17"},
                            {"x": 19, "y": 0, "label": "19"},
                            {"x": 23, "y": 0, "label": "23"},
                            {"x": 29, "y": 0, "label": "29"},
                            {"x": 31, "y": 0, "label": "31"}
                        ]
                    },
                    "image_query": "Ishango bone tally marks prime numbers pattern",
                    "video_query": "ishango bone ancient mathematics prime numbers",
                    "what_to_explain": "The notches carved on the prehistoric Ishango bone record prime numbers, demonstrating humanity's early discovery of non-composite integers."
                },
                {
                    "concept_title": "Brahmagupta's Product Plane: Signs of Quadrants",
                    "diagram_title": "Four Quadrants of Integer Multiplication",
                    "interactive_math_formula": "(-a) * (-b) = +ab",
                    "mafs_graph_config": {
                        "domain": [-5, 5],
                        "range": [-5, 5],
                        "lines": [
                            {"slope": 1, "intercept": 0, "color": "#2563EB", "label": "y = x"},
                            {"slope": -1, "intercept": 0, "color": "#DC2626", "label": "y = -x"}
                        ],
                        "points": [
                            {"x": 2, "y": 3, "label": "(+) * (+) = (+)"},
                            {"x": -2, "y": 3, "label": "(-) * (+) = (-)"},
                            {"x": -2, "y": -3, "label": "(-) * (-) = (+)"},
                            {"x": 2, "y": -3, "label": "(+) * (-) = (-)"}
                        ]
                    },
                    "image_query": "multiplication of signs four quadrants coordinate plane",
                    "video_query": "rules of multiplying positive and negative integers",
                    "what_to_explain": "The product of two debts (negatives) is a fortune (positive), matching the reflection across coordinate axes into Quadrant 1."
                },
                {
                    "concept_title": "Duodecimal Finger Joint Counting System",
                    "diagram_title": "Base 12 Phalanx Matrix: 4 fingers x 3 joints = 12",
                    "interactive_math_formula": "4 \\times 3 = 12",
                    "mafs_graph_config": {
                        "domain": [0, 5],
                        "range": [0, 4],
                        "points": [
                            {"x": 1, "y": 1, "label": "J1"}, {"x": 1, "y": 2, "label": "J2"}, {"x": 1, "y": 3, "label": "J3"},
                            {"x": 2, "y": 1, "label": "J4"}, {"x": 2, "y": 2, "label": "J5"}, {"x": 2, "y": 3, "label": "J6"},
                            {"x": 3, "y": 1, "label": "J7"}, {"x": 3, "y": 2, "label": "J8"}, {"x": 3, "y": 3, "label": "J9"},
                            {"x": 4, "y": 1, "label": "J10"}, {"x": 4, "y": 2, "label": "J11"}, {"x": 4, "y": 3, "label": "J12"}
                        ]
                    },
                    "image_query": "ancient finger joint counting base 12 duodecimal",
                    "video_query": "ancient base 12 counting method finger joints",
                    "what_to_explain": "Using the thumb to point to each phalanx on 4 fingers yields 12 distinct positions per hand, giving rise to base-12 systems."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Brahmagupta's Laws of Signs",
                    "questions": [
                        {
                            "question": "What is the product of two negative integers according to Brahmagupta's Brahmasphutasiddhanta?",
                            "type": "short_answer",
                            "ideal_answer": "The product of two debts (negative numbers) is a fortune (positive number).",
                            "socratic_hint": "Recall the aphorism: the debt of a debt is a fortune."
                        },
                        {
                            "question": "Are natural numbers closed under subtraction? Why or why not?",
                            "type": "short_answer",
                            "ideal_answer": "No, because subtracting a larger natural number from a smaller one (such as 3 - 5 = -2) results in a negative integer, which is not in N.",
                            "socratic_hint": "Try subtracting 5 from 3 and check if the result is in {1, 2, 3, ...}."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Textbook Example 1: A merchant has an initial fortune of Rs 500, incurs a loss of Rs 700, and later receives Rs 400. Express his financial state as an integer sequence.",
                "given": "Initial fortune = +500, Loss = -700, Income = +400.",
                "formula": "Final State = Initial + Transactions.",
                "substitution": "S = 500 - 700 + 400.",
                "calculation": "1. 500 - 700 = -200 (a debt of Rs 200).\n2. -200 + 400 = +200 (a net fortune of Rs 200).",
                "finalAnswer": "+200 (Fortune of Rs 200)",
                "unit": "Rs",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 2: Apply Brahmagupta's laws to compute: (i) 0 + (-8), (ii) 0 - 9, (iii) (-5) * (-6).",
                "given": "(i) 0 + (-8), (ii) 0 - 9, (iii) (-5) * (-6).",
                "formula": "Brahmagupta: 0 + (-a) = -a; 0 - a = -a; (-a) * (-b) = +ab.",
                "substitution": "(i) 0 + (-8) = -8; (ii) 0 - 9 = -9; (iii) (-5) * (-6) = +30.",
                "calculation": "1. Adding a debt of 8 to zero leaves a debt of 8: -8.\n2. Subtracting 9 from zero results in debt -9.\n3. Multiplying two debts: (-5) * (-6) = +30.",
                "finalAnswer": "(i) -8, (ii) -9, (iii) 30",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 3: Demonstrate that 12 / (-3) = -4 using Brahmagupta's division rule.",
                "given": "Dividend = 12, Divisor = -3.",
                "formula": "(+a) / (-b) = -(a / b).",
                "substitution": "12 / (-3) = -(12 / 3).",
                "calculation": "1. 12 / 3 = 4.\n2. Fortune divided by debt gives debt: -4.",
                "finalAnswer": "-4",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.1 Q1: A merchant in Lothal receives 15 copper ingots for every 2 bags of spices. If he brings 12 bags of spices to market, how many copper ingots will he leave with?",
                "given": "Exchange rate: 2 bags of spices = 15 copper ingots. Total spices = 12 bags.",
                "formula": "Total ingots = (Total bags / 2) * 15.",
                "substitution": "Total ingots = (12 / 2) * 15.",
                "calculation": "1. 12 / 2 = 6 exchange sets.\n2. 6 * 15 = 90 copper ingots.",
                "finalAnswer": "90 copper ingots",
                "unit": "ingots",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.1 Q2: Column on Ishango bone has 11, 13, 17, 19. What do these numbers have in common? List the next three numbers that fit this pattern.",
                "given": "Sequence: 11, 13, 17, 19.",
                "formula": "Definition of Prime Numbers: Integers greater than 1 having exactly two factors (1 and itself).",
                "substitution": "All given numbers 11, 13, 17, 19 are prime numbers.",
                "calculation": "1. 11, 13, 17, 19 are consecutive prime numbers between 10 and 20.\n2. The next primes greater than 19 are:\n   - 20: composite (2 * 10)\n   - 21: composite (3 * 7)\n   - 22: composite (2 * 11)\n   - 23: prime\n   - 24 to 28: composite\n   - 29: prime\n   - 30: composite\n   - 31: prime.",
                "finalAnswer": "Common property: They are all prime numbers. Next three numbers: 23, 29, 31.",
                "unit": "prime numbers",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.1 Q3: Natural Numbers are closed under addition. Are they closed under subtraction? Provide examples to justify your answer.",
                "given": "Set of Natural Numbers N = {1, 2, 3, ...}.",
                "formula": "A set S is closed under an operation * if for all a, b in S, a * b is also in S.",
                "substitution": "Let a = 3 and b = 5, both in N. Compute a - b = 3 - 5.",
                "calculation": "1. 3 - 5 = -2.\n2. -2 is a negative integer and is not an element of N.\n3. Another example: 4 - 4 = 0, which is not in N.\n4. Hence, the difference of two natural numbers is not always a natural number.",
                "finalAnswer": "No, natural numbers are not closed under subtraction (e.g. 3 - 5 = -2, which is not a natural number).",
                "unit": "closure property",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.1 Q4: Ancient Indians used finger joints to count: 4 fingers with 3 joints each, counted by the thumb. How many can you count on one hand? How does this relate to base-12?",
                "given": "4 counting fingers (index, middle, ring, little), each having 3 phalangeal joints. Thumb acts as pointing stylus.",
                "formula": "Total Count = Number of fingers * joints per finger.",
                "substitution": "Total Count = 4 * 3 = 12.",
                "calculation": "1. Each finger has 3 distinct joints/phalanges.\n2. 4 fingers * 3 joints = 12 distinct count positions on a single hand.\n3. Using the 5 digits of the other hand to record completed cycles of 12 allows counting up to 12 * 5 = 60 (origin of sexagesimal astronomy and 12-hour day/night cycles).",
                "finalAnswer": "12 counts per hand. This is the physiological origin of base-12 (duodecimal) counting and traditional timekeeping.",
                "unit": "counts",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.2 Q1: The temperature in Ladakh is recorded as 4 °C at noon. By midnight, it drops by 15 °C. What is the midnight temperature?",
                "given": "Initial temperature = 4 °C, Temperature drop = 15 °C.",
                "formula": "Midnight Temperature = Initial - Drop.",
                "substitution": "T = 4 - 15.",
                "calculation": "1. 4 - 15 = 4 + (-15).\n2. Since |-15| > 4, the result is negative: -(15 - 4) = -11 °C.",
                "finalAnswer": "-11 °C",
                "unit": "°C",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.2 Q2: A spice trader takes a loan of Rs 850. Next day, he makes a profit of Rs 1,200. Following week, he incurs a loss of Rs 450. Write this sequence as an equation using integers and calculate his final standing.",
                "given": "Loan (debt) = -850, Profit (fortune) = +1200, Loss (debt) = -450.",
                "formula": "Final Balance = Debt1 + Profit + Loss.",
                "substitution": "B = -850 + 1200 - 450.",
                "calculation": "1. Combine debts: -850 + (-450) = -1300.\n2. Add profit: -1300 + 1200 = -100.\n3. A negative balance represents a net debt.",
                "finalAnswer": "Equation: -850 + 1200 - 450 = -100 (Final standing is a net debt of Rs 100).",
                "unit": "Rs",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.2 Q3 (i): Calculate (-12) * 5 using Brahmagupta's laws.",
                "given": "(-12) * 5.",
                "formula": "Debt times Fortune equals Debt: (-a) * b = -(a * b).",
                "substitution": "-(12 * 5).",
                "calculation": "12 * 5 = 60, with negative sign: -60.",
                "finalAnswer": "-60",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.2 Q3 (ii): Calculate (-8) * (-7) using Brahmagupta's laws.",
                "given": "(-8) * (-7).",
                "formula": "Debt times Debt equals Fortune: (-a) * (-b) = +(a * b).",
                "substitution": "+(8 * 7).",
                "calculation": "8 * 7 = 56, with positive sign: 56.",
                "finalAnswer": "56",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.2 Q3 (iii): Calculate 0 - (-14) using Brahmagupta's laws.",
                "given": "0 - (-14).",
                "formula": "Subtracting a debt is equivalent to adding a fortune: 0 - (-a) = +a.",
                "substitution": "0 - (-14) = +14.",
                "calculation": "0 + 14 = 14.",
                "finalAnswer": "14",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.2 Q3 (iv): Calculate (-20) / 4 using Brahmagupta's laws.",
                "given": "(-20) / 4.",
                "formula": "Debt divided by Fortune equals Debt: (-a) / b = -(a / b).",
                "substitution": "-(20 / 4).",
                "calculation": "20 / 4 = 5, with negative sign: -5.",
                "finalAnswer": "-5",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.2 Q4: Explain, using a real-world example of debt, why subtracting a negative number is the same as adding a positive number (e.g. 10 - (-5) = 15).",
                "given": "Expression 10 - (-5) = 15.",
                "formula": "Net Worth = Assets - Liabilities.",
                "substitution": "Assets = Rs 10, Debt liability = Rs 5 (represented as -5).",
                "calculation": "1. If a person has Rs 10 in cash and a recorded debt note of Rs 5, the lender forgives (cancels/subtracts) the debt of Rs 5.\n2. Subtracting a debt note of Rs 5 removes a claim against future earnings.\n3. The person's effective net financial worth immediately increases by Rs 5, from Rs 10 to Rs 15.\n4. Mathematically: 10 - (-5) = 10 + 5 = 15.",
                "finalAnswer": "Canceling or forgiving a debt of Rs 5 removes a liability, which increases net wealth by Rs 5, proving 10 - (-5) = 10 + 5 = 15.",
                "unit": "algebraic explanation",
                "has_diagram": True
            }
        ]
    }
