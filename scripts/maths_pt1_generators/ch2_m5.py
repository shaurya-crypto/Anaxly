"""
Chapter 2: Introduction to Linear Polynomials - Module 5
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m5():
    m5_svg = build_cartesian_svg(
        domain=(-50, 110), range_y=(-50, 220),
        points=[
            {"x": 0, "y": 32, "label": "Freezing (0, 32)", "color": "#2563EB", "sub": "(0, 32)"},
            {"x": 100, "y": 212, "label": "Boiling (100, 212)", "color": "#DC2626", "sub": "(100, 212)"},
            {"x": -40, "y": -40, "label": "Intersection (-40, -40)", "color": "#7C3AED", "sub": "(-40, -40)"},
        ],
        lines=[
            {"p1": (-50, -58), "p2": (105, 221), "color": "#2563EB", "stroke_width": 2.5, "label": "F = 1.8C + 32"},
            {"p1": (-50, -50), "p2": (110, 110), "color": "#94A3B8", "stroke_width": 1.5, "label": "F = C"}
        ],
        title="Linear Temperature Conversion: F = 1.8C + 32",
        caption="Fahrenheit vs Celsius linear relationship intersecting the identity line at (-40, -40)"
    )

    return {
        "order_index": 5,
        "title": "Textbook Exercise Solver 3: Two-Point Determination & Parameter Identification (Exercise 2.5 Complete)",
        "description": "Exhaustive step-by-step solutions to in-text Examples 9 to 13 and Exercise 2.5. Learn how to determine the linear parameters a and b in y = ax + b from two coordinate pairs, model service platform pricing and sports club rentals, and analyze temperature conversions.",
        "subtopics": [
            "Determining slope a = (y2 - y1) / (x2 - x1) from two observed points",
            "Solving simultaneous linear equations for parameters a and b in y = ax + b",
            "Digital learning platform pricing model: Fixed subscription fee vs module cost",
            "Badminton court rental fee model: Fixed monthly membership vs hourly fee",
            "Temperature conversion formula F = 1.8C + 32 and finding the unique fixed point where F = C",
            "Step-by-step graphing of linear functions from tabular coordinates",
            "Solutions to in-text Examples 9 to 13 and Exercise 2.5 Q1, Q2, and Q3"
        ],
        "key_concepts": [
            "Two-Point Linear Parameter Theorem: Any two distinct points (x1, y1) and (x2, y2) uniquely determine the parameters a and b of the linear polynomial y = ax + b.",
            "Rate of Change Invariant: The parameter a equals the difference quotient Delta y / Delta x = (y2 - y1) / (x2 - x1).",
            "Fixed Point Invariant: A value where input equals output (F = C) is found by solving C = 1.8C + 32, yielding the universal temperature equivalence point -40°.",
            "Two-Part Pricing Invariant: Total Cost = Variable Rate * Usage + Fixed Baseline Fee."
        ],
        "success_criteria": "Student can determine linear equations from two real-world data points, solve for unknown coefficients, and perform multi-scale conversions.",
        "chapter_notes": "Exercise 2.5 illustrates the foundation of linear regression: extracting law-like constants (a and b) from empirical pairs of data.",
        "worked_examples": [
            {
                "problem": "Textbook Example 9: The cost of a taxi journey is given by C(d) = 100 + 60d, where d is the distance in km. Find the cost of a 15 km journey.",
                "given": "Cost function C(d) = 100 + 60d. Distance d = 15 km.",
                "formula": "C(d) = 100 + 60d.",
                "substitution": "C(15) = 100 + 60(15).",
                "calculation": "Step 1: 60 * 15 = 900.\nStep 2: Add base fee: 100 + 900 = Rs 1,000.\nStep 3: State the unit: Rs 1,000.",
                "finalAnswer": "Cost = Rs 1,000",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 10: The height of water in a cylindrical tank is 3 m initially. When a drain is opened, water level drops at a rate of 0.2 m per minute. Find the water height after 8 minutes, and find when the tank is empty.",
                "given": "Initial height = 3 m. Drain rate = 0.2 m/min. Time = t minutes.",
                "formula": "Height H(t) = 3 - 0.2t. Empty when H(t) = 0.",
                "substitution": "H(8) = 3 - 0.2(8); 3 - 0.2t = 0.",
                "calculation": "Part (i): H(8) = 3 - 1.6 = 1.4 metres.\nPart (ii): 3 - 0.2t = 0 => 0.2t = 3 => t = 3 / 0.2 = 15 minutes.",
                "finalAnswer": "Height after 8 min = 1.4 m; Tank empties in 15 minutes",
                "unit": "metres and minutes",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 11: A telecom company charges a fixed monthly fee of Rs 150 plus Rs 1.20 per phone call. Find the linear polynomial for total bill B(c) for c calls, and compute the bill for 200 calls.",
                "given": "Fixed charge = Rs 150. Rate per call = Rs 1.20. Number of calls = c.",
                "formula": "B(c) = 150 + 1.20c.",
                "substitution": "B(200) = 150 + 1.20(200).",
                "calculation": "Step 1: 1.20 * 200 = Rs 240.\nStep 2: Add fixed fee: 150 + 240 = Rs 390.",
                "finalAnswer": "B(c) = 1.20c + 150; Bill for 200 calls = Rs 390",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Textbook Examples 12 & 13: Plot the points (-1, -3), (0, 0), and (1, 3) on the Cartesian plane, and show that they lie on the straight line y = 3x passing through the origin.",
                "given": "Points A(-1, -3), O(0, 0), B(1, 3).",
                "formula": "Linear polynomial y = 3x.",
                "substitution": "y(-1) = 3(-1) = -3; y(0) = 3(0) = 0; y(1) = 3(1) = 3.",
                "calculation": "Step 1: Check point A: for x = -1, y = 3(-1) = -3. Matches (-1, -3).\nStep 2: Check origin O: for x = 0, y = 3(0) = 0. Matches (0, 0).\nStep 3: Check point B: for x = 1, y = 3(1) = 3. Matches (1, 3).\nStep 4: All three points satisfy y = 3x, proving collinearity along a line passing through the origin with slope 3.",
                "finalAnswer": "All three points satisfy y = 3x and lie on a straight line through the origin",
                "unit": "collinear points",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.5 Q1: A learning platform charges a fixed monthly fee and an additional cost per digital learning module accessed. A student observes that when she accessed 10 modules, her bill was Rs 400. When she accessed 14 modules, her bill was Rs 500. If the monthly bill y depends on the modules accessed x according to y = ax + b, find the values of a and b.",
                "given": "Point 1: (x1, y1) = (10, 400). Point 2: (x2, y2) = (14, 500). Relation: y = ax + b.",
                "formula": "Slope a = (y2 - y1) / (x2 - x1); Intercept b = y1 - a * x1.",
                "substitution": "a = (500 - 400) / (14 - 10) = 100 / 4.",
                "calculation": "Step 1: Set up system of linear equations:\n  400 = 10a + b  --- (Equation 1)\n  500 = 14a + b  --- (Equation 2)\nStep 2: Subtract Equation 1 from Equation 2:\n  (14a + b) - (10a + b) = 500 - 400\n  4a = 100 => a = 25.\nStep 3: Substitute a = 25 into Equation 1:\n  10(25) + b = 400\n  250 + b = 400 => b = 400 - 250 = 150.\nStep 4: Physical meaning: Fixed monthly fee b = Rs 150; Cost per module a = Rs 25.",
                "finalAnswer": "a = 25, b = 150 (Linear formula: y = 25x + 150)",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.5 Q2: A gym charges a fixed monthly fee and an additional cost per hour for using the badminton court. A student using the court for 6 hours was billed Rs 280, while a student using the court for 10 hours was billed Rs 400. Find the fixed fee and hourly cost by determining a and b in y = ax + b.",
                "given": "Point 1: (6, 280). Point 2: (10, 400). Relation: y = ax + b.",
                "formula": "400 = 10a + b; 280 = 6a + b.",
                "substitution": "(10a + b) - (6a + b) = 400 - 280.",
                "calculation": "Step 1: Subtract equations: 4a = 120 => a = 30.\nStep 2: Substitute a = 30 into first equation:\n  6(30) + b = 280\n  180 + b = 280 => b = 100.\nStep 3: Physical interpretation: Hourly court rate a = Rs 30; Fixed monthly membership b = Rs 100.",
                "finalAnswer": "Fixed fee b = Rs 100; Hourly cost a = Rs 30 (Formula: y = 30x + 100)",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.5 Q3 (Part 1): The relationship between temperature measured in Fahrenheit (F) and Celsius (C) is given by F = 1.8C + 32. Convert: (i) 25°C to Fahrenheit, (ii) 37°C (normal body temperature) to Fahrenheit, and (iii) 0°C to Fahrenheit.",
                "given": "Conversion formula: F = 1.8C + 32.",
                "formula": "F = 1.8C + 32.",
                "substitution": "(i) F = 1.8(25) + 32; (ii) F = 1.8(37) + 32; (iii) F = 1.8(0) + 32.",
                "calculation": "Part (i): 1.8 * 25 = 45 => F = 45 + 32 = 77°F.\nPart (ii): 1.8 * 37 = 66.6 => F = 66.6 + 32 = 98.6°F.\nPart (iii): 1.8 * 0 = 0 => F = 0 + 32 = 32°F (Freezing point of water).",
                "finalAnswer": "(i) 25°C = 77°F; (ii) 37°C = 98.6°F; (iii) 0°C = 32°F",
                "unit": "degrees Fahrenheit",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m5_svg
            },
            {
                "problem": "Exercise 2.5 Q3 (Part 2): Find the numerical temperature that has the same value in both Celsius and Fahrenheit scales (F = C).",
                "given": "Formula: F = 1.8C + 32. Condition: F = C.",
                "formula": "Set F = C in the conversion equation: C = 1.8C + 32.",
                "substitution": "C - 1.8C = 32.",
                "calculation": "Step 1: Set C = 1.8C + 32.\nStep 2: Collect terms in C: C - 1.8C = 32.\nStep 3: -0.8C = 32.\nStep 4: Divide by -0.8: C = 32 / (-0.8) = -40.\nStep 5: Check: At C = -40, F = 1.8(-40) + 32 = -72 + 32 = -40.\nStep 6: Thus -40° is the exact temperature where both scales are identical.",
                "finalAnswer": "-40° (both -40°C and -40°F represent the same physical temperature)",
                "unit": "degrees",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Failing to divide the difference in cost by the difference in usage when calculating slope a: computing (500 - 400) = 100 without dividing by (14 - 10) = 4.",
            "Thinking Fahrenheit and Celsius scales never intersect: they intersect at -40°."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Emphasize that knowing two data points allows one to unlock the entire future and past of any linear system. Illustrate with platform billing and temperature scales.",
        "visual_lesson_plan": {
            "title": "Two-Point Parameter Determination & Scales",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Graph of F = 1.8C + 32 intersecting the line F = C at (-40, -40).",
            "concept_visuals": [
                {
                    "concept_title": "Fahrenheit vs Celsius Temperature Line",
                    "diagram_title": "Linear Mapping F = 1.8C + 32",
                    "interactive_math_formula": "F = 1.8C + 32",
                    "mafs_graph_config": {
                        "domain": [-50, 110],
                        "range": [-50, 220],
                        "curves": [
                            {"fn": "1.8*x + 32", "color": "#2563EB", "label": "F = 1.8C + 32"},
                            {"fn": "x", "color": "#94A3B8", "label": "Identity F = C"}
                        ],
                        "points": [
                            {"x": 0, "y": 32, "label": "Freezing: (0, 32)"},
                            {"x": 100, "y": 212, "label": "Boiling: (100, 212)"},
                            {"x": -40, "y": -40, "label": "Coincidence: (-40, -40)"}
                        ]
                    },
                    "image_query": "Fahrenheit Celsius linear graph intersection at minus 40",
                    "video_query": "deriving temperature conversion formula linear equation graph",
                    "what_to_explain": "The line F = 1.8C + 32 has slope 1.8 and intercept 32, cutting the identity line F = C at exactly (-40, -40)."
                },
                {
                    "concept_title": "Platform Billing Parameter Identification",
                    "diagram_title": "Line y = 25x + 150 through (10, 400) and (14, 500)",
                    "interactive_math_formula": "y = 25x + 150",
                    "mafs_graph_config": {
                        "domain": [0, 20],
                        "range": [100, 600],
                        "curves": [
                            {"fn": "25*x + 150", "color": "#16A34A", "label": "Bill y = 25x + 150"}
                        ],
                        "points": [
                            {"x": 0, "y": 150, "label": "Base Fee: Rs 150"},
                            {"x": 10, "y": 400, "label": "10 Modules: Rs 400"},
                            {"x": 14, "y": 500, "label": "14 Modules: Rs 500"}
                        ]
                    },
                    "image_query": "two point linear slope determination billing data graph",
                    "video_query": "finding linear equation from two points word problems",
                    "what_to_explain": "The slope of 25 is found directly from (500 - 400)/(14 - 10), and the y-intercept reveals the Rs 150 base fee."
                },
                {
                    "concept_title": "Badminton Court Rental Locus",
                    "diagram_title": "Gym Charge y = 30x + 100 through (6, 280) and (10, 400)",
                    "interactive_math_formula": "y = 30x + 100",
                    "mafs_graph_config": {
                        "domain": [0, 15],
                        "range": [50, 500],
                        "curves": [
                            {"fn": "30*x + 100", "color": "#D97706", "label": "Gym Bill y = 30x + 100"}
                        ],
                        "points": [
                            {"x": 0, "y": 100, "label": "Fixed Membership: Rs 100"},
                            {"x": 6, "y": 280, "label": "6 Hours: Rs 280"},
                            {"x": 10, "y": 400, "label": "10 Hours: Rs 400"}
                        ]
                    },
                    "image_query": "gym membership linear pricing graph slope intercept",
                    "video_query": "gym membership cost word problem linear system",
                    "what_to_explain": "Every additional hour costs Rs 30, starting from a fixed Rs 100 entry membership."
                },
                {
                    "concept_title": "Water Tank Linear Drainage Rate",
                    "diagram_title": "Water Level H(t) = 3 - 0.2t",
                    "interactive_math_formula": "H(t) = 3 - 0.2t",
                    "mafs_graph_config": {
                        "domain": [0, 20],
                        "range": [0, 4],
                        "curves": [
                            {"fn": "3 - 0.2*x", "color": "#7C3AED", "label": "Water Height H(t)"}
                        ],
                        "points": [
                            {"x": 0, "y": 3, "label": "Full: 3 m"},
                            {"x": 8, "y": 1.4, "label": "8 min: 1.4 m"},
                            {"x": 15, "y": 0, "label": "Empty: 15 min"}
                        ]
                    },
                    "image_query": "draining tank water level linear decline rate of change",
                    "video_query": "water tank draining linear differential equation algebra",
                    "what_to_explain": "Water level drops by 0.2 m each minute, reaching empty (0 m) at exactly 15 minutes."
                },
                {
                    "concept_title": "Taxi Fare Constant Rate Divergence",
                    "diagram_title": "Journey Cost C(d) = 60d + 100",
                    "interactive_math_formula": "C(d) = 60d + 100",
                    "mafs_graph_config": {
                        "domain": [0, 20],
                        "range": [0, 1200],
                        "curves": [
                            {"fn": "60*x + 100", "color": "#059669", "label": "Cost C(d)"}
                        ],
                        "points": [
                            {"x": 0, "y": 100, "label": "Base: Rs 100"},
                            {"x": 15, "y": 1000, "label": "15 km: Rs 1,000"}
                        ]
                    },
                    "image_query": "taxi fare distance graph linear function slope intercept",
                    "video_query": "taxi fare word problem linear equation slope",
                    "what_to_explain": "A 15 km journey accumulates Rs 900 in distance charges plus the Rs 100 base boarding fee."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Exercise 2.5 Mastery",
                    "questions": [
                        {
                            "question": "If 10 modules cost Rs 400 and 14 modules cost Rs 500 in y = ax + b, what is the cost per module a?",
                            "type": "short_answer",
                            "options": ["Rs 25", "Rs 30", "Rs 20", "Rs 15"],
                            "ideal_answer": "Rs 25, from (500 - 400)/(14 - 10) = 100/4 = 25.",
                            "socratic_hint": "Divide the change in bill (100) by the change in modules (4)."
                        },
                        {
                            "question": "What is the fixed monthly fee b for the learning platform?",
                            "type": "short_answer",
                            "options": ["Rs 150", "Rs 100", "Rs 200", "Rs 250"],
                            "ideal_answer": "Rs 150, from 400 - 10(25) = 400 - 250 = 150.",
                            "socratic_hint": "Subtract 10 times 25 from 400."
                        },
                        {
                            "question": "At what temperature do the Celsius and Fahrenheit scales have the exact same value?",
                            "type": "short_answer",
                            "options": ["-40°", "0°", "32°", "100°"],
                            "ideal_answer": "-40°, obtained by solving C = 1.8C + 32 => -0.8C = 32 => C = -40.",
                            "socratic_hint": "Set F = C in F = 1.8C + 32."
                        },
                        {
                            "question": "What is 37°C (normal body temperature) converted to Fahrenheit?",
                            "type": "short_answer",
                            "options": ["98.6°F", "98.4°F", "99.0°F", "100.2°F"],
                            "ideal_answer": "98.6°F, from 1.8(37) + 32 = 66.6 + 32 = 98.6.",
                            "socratic_hint": "Multiply 37 by 1.8, then add 32."
                        },
                        {
                            "question": "If a gym charges Rs 100 fixed fee plus Rs 30 per hour, what is the bill for 8 hours?",
                            "type": "short_answer",
                            "options": ["Rs 340", "Rs 240", "Rs 300", "Rs 400"],
                            "ideal_answer": "Rs 340, from 100 + 30(8) = 100 + 240 = 340.",
                            "socratic_hint": "Multiply 8 by 30 and add 100."
                        }
                    ]
                }
            ]
        }
    }
