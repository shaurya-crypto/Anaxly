"""
Chapter 2: Introduction to Linear Polynomials - Module 4
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cartesian_svg

def get_m4():
    m4_svg = build_cartesian_svg(
        domain=(0, 10), range_y=(0, 10),
        points=[
            {"x": 0, "y": 1.75, "label": "Initial (0, 1.75)", "color": "#16A34A", "sub": "(0, 1.75)"},
            {"x": 7, "y": 5.25, "label": "7 Months (7, 5.25)", "color": "#2563EB", "sub": "(7, 5.25)"},
            {"x": 10, "y": 6.75, "label": "10 Months (10, 6.75)", "color": "#D97706", "sub": "(10, 6.75)"},
        ],
        lines=[
            {"p1": (0, 1.75), "p2": (10, 6.75), "color": "#2563EB", "stroke_width": 2.5, "label": "h(t) = 1.75 + 0.5t"}
        ],
        title="Linear Plant Growth: h(t) = 1.75 + 0.5t",
        caption="Constant rate of growth of 0.5 feet per month starting from baseline 1.75 feet"
    )

    return {
        "order_index": 4,
        "title": "Textbook Exercise Solver 2: Real-Life Linear Modeling (Exercises 2.3 & 2.4 Complete)",
        "description": "Complete step-by-step solutions to 100% of questions in Exercises 2.3 and 2.4. Model real-world linear growth and decay: bank savings, rally dropouts, geometric dimensions, book reading rates, plant growth, asset depreciation, village populations, and telecom billing.",
        "subtopics": [
            "Linear accumulation: Savings bank balance S(n) = 500 + 150n",
            "Linear attrition: Rally membership M(h) = 120 - 9h",
            "Geometric area and volume linear functions: A(w) = 13w and V(h) = 28h",
            "Reading progress and completion rate: R(d) = 500 - 20d",
            "Botanical growth modeling: Plant height h(t) = 1.75 + 0.5t with table of values",
            "Financial asset depreciation: Mobile phone value V(t) = 10000 - 800t",
            "Demographic linear growth: Village population P(t) = 750 + 50t",
            "Telecom billing functions: Base fee plus per-minute usage",
            "Exhaustive solutions to Exercise 2.3 Q1 to Q5 and Exercise 2.4 Q1 to Q4"
        ],
        "key_concepts": [
            "Linear Growth Invariant: Any quantity that increases by a constant amount per unit time obeys the linear equation y = mt + c with positive slope m > 0.",
            "Linear Decay Invariant: Any quantity that decreases by a fixed amount per unit time obeys y = -mt + c with negative slope -m < 0.",
            "Table of Values Construction: Generating ordered pairs (t, y) by stepping the independent variable t and computing the dependent response y.",
            "Extrapolation and Forecasting: Using the linear formula to predict future states without iterative addition."
        ],
        "success_criteria": "Student can construct linear models from real-life descriptions, generate tables of values, calculate future values, and interpret slope and y-intercept in context.",
        "chapter_notes": "Emphasize that the defining characteristic of linear relationships is a CONSTANT rate of change across all intervals.",
        "worked_examples": [
            {
                "problem": "Exercise 2.3 Q1: A student has Rs 500 in her savings bank account. She gets Rs 150 every month as pocket money. How much money will she have at the end of every month from the second month onwards? Find a linear expression to represent the amount she will have in the nth month.",
                "given": "Initial deposit = Rs 500. Monthly pocket money = Rs 150. Month number = n.",
                "formula": "Total Amount S(n) = Initial Deposit + (Monthly Addition * n) = 500 + 150n.",
                "substitution": "S(n) = 500 + 150n.",
                "calculation": "Step 1: End of month 1: 500 + 150(1) = Rs 650.\nStep 2: End of month 2: 500 + 150(2) = Rs 800.\nStep 3: End of month 3: 500 + 150(3) = Rs 950.\nStep 4: General formula for the nth month: S(n) = 500 + 150n (or 150n + 500).",
                "finalAnswer": "Linear expression: S(n) = 150n + 500 rupees; Month 2: Rs 800; Month 3: Rs 950",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.3 Q2: A rally starts with 120 members. Each hour, 9 members drop out of the group. Find a linear expression for the number of members remaining after h hours, and calculate the members remaining after 6 hours.",
                "given": "Initial rally members = 120. Dropout rate = 9 members/hour. Time = h hours.",
                "formula": "Members M(h) = Initial Count - (Dropout Rate * h) = 120 - 9h.",
                "substitution": "M(6) = 120 - 9(6).",
                "calculation": "Step 1: Formulate linear decay model: M(h) = 120 - 9h.\nStep 2: Substitute h = 6: M(6) = 120 - 54 = 66 members.\nStep 3: Verify when rally ends: 120 - 9h = 0 => h = 120/9 = 13.33 hours.",
                "finalAnswer": "Linear expression: M(h) = 120 - 9h; Members after 6 hours = 66",
                "unit": "members",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.3 Q3: Suppose the length of a rectangle is 13 cm. Find the area if width is w cm, and explain why this represents a linear expression.",
                "given": "Length = 13 cm. Width = w cm.",
                "formula": "Area A(w) = Length * Width = 13 * w.",
                "substitution": "A(w) = 13w.",
                "calculation": "Step 1: Area = 13 * w = 13w sq. cm.\nStep 2: A(w) is a polynomial in w of degree 1 (highest exponent of w is 1) with zero constant term.\nStep 3: Therefore, it is a linear monomial representing direct proportionality.",
                "finalAnswer": "Area A(w) = 13w sq. cm (a linear monomial of degree 1)",
                "unit": "sq. cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.3 Q4: Suppose the length of a rectangular box is 7 cm and breadth is 4 cm. Find its volume if the height is h cm.",
                "given": "Length = 7 cm, Breadth = 4 cm, Height = h cm.",
                "formula": "Volume V(h) = Length * Breadth * Height = 7 * 4 * h.",
                "substitution": "V(h) = 28h.",
                "calculation": "Step 1: Base area = 7 * 4 = 28 sq. cm.\nStep 2: Multiply by height h: V(h) = 28h cubic cm.\nStep 3: The volume is a linear function of height with slope 28.",
                "finalAnswer": "Volume V(h) = 28h cubic cm",
                "unit": "cubic cm",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.3 Q5: Sarita is reading a book of 500 pages. She reads 20 pages every day. Find a linear expression for the pages remaining after d days, and find how many days she will take to finish the book.",
                "given": "Total pages = 500. Reading rate = 20 pages/day. Days = d.",
                "formula": "Pages remaining R(d) = 500 - 20d. Book finished when R(d) = 0.",
                "substitution": "500 - 20d = 0 => 20d = 500.",
                "calculation": "Step 1: Linear expression: R(d) = 500 - 20d.\nStep 2: Set R(d) = 0 to find completion day: 500 - 20d = 0.\nStep 3: 20d = 500 => d = 500 / 20 = 25 days.",
                "finalAnswer": "R(d) = 500 - 20d; She will finish the book in 25 days",
                "unit": "days",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.4 Q1: Suppose a plant has height 1.75 feet and it grows by 0.5 feet each month. (i) Find the height after 7 months. (ii) Make a table of values for t varying from 0 to 10 months. (iii) Find an expression that relates h and t, and explain why it represents linear growth.",
                "given": "Initial height = 1.75 feet. Growth rate = 0.5 feet/month. Time = t months.",
                "formula": "Height h(t) = Initial Height + Rate * t = 1.75 + 0.5t.",
                "substitution": "h(7) = 1.75 + 0.5(7).",
                "calculation": "Part (i): h(7) = 1.75 + 3.5 = 5.25 feet.\nPart (ii) Table of values:\n  - t=0: 1.75 ft | t=1: 2.25 ft | t=2: 2.75 ft | t=3: 3.25 ft | t=4: 3.75 ft\n  - t=5: 4.25 ft | t=6: 4.75 ft | t=7: 5.25 ft | t=8: 5.75 ft | t=9: 6.25 ft | t=10: 6.75 ft.\nPart (iii) Linear expression: h(t) = 0.5t + 1.75. This represents linear growth because the rate of change dh/dt = 0.5 is constant across every month.",
                "finalAnswer": "(i) 5.25 feet; (ii) Table from 1.75 to 6.75 ft; (iii) h(t) = 0.5t + 1.75 (constant slope 0.5)",
                "unit": "feet",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m4_svg
            },
            {
                "problem": "Exercise 2.4 Q2: A mobile phone is bought for Rs 10,000. Its value decreases by Rs 800 every year. (i) Find the value of the phone after 3 years. (ii) Make a table of values for t varying from 0 to 5 years. (iii) Find an expression relating V and t.",
                "given": "Initial purchase value = Rs 10,000. Annual depreciation = Rs 800. Time = t years.",
                "formula": "Value V(t) = 10,000 - 800t.",
                "substitution": "V(3) = 10,000 - 800(3).",
                "calculation": "Part (i): V(3) = 10,000 - 2,400 = Rs 7,600.\nPart (ii) Table of values:\n  - t=0: Rs 10,000 | t=1: Rs 9,200 | t=2: Rs 8,400\n  - t=3: Rs 7,600  | t=4: Rs 6,800 | t=5: Rs 6,000.\nPart (iii): Expression: V(t) = 10000 - 800t (a linear decay function with slope -800).",
                "finalAnswer": "(i) Rs 7,600; (ii) Table from Rs 10,000 to Rs 6,000; (iii) V(t) = 10000 - 800t",
                "unit": "rupees",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.4 Q3: The initial population of a village is 750. Every year, 50 people move into the village. (i) Find the population after 6 years. (ii) Find a linear expression relating population P and time t in years.",
                "given": "Initial population P_0 = 750. Annual growth = 50 people/year. Time = t years.",
                "formula": "Population P(t) = 750 + 50t.",
                "substitution": "P(6) = 750 + 50(6).",
                "calculation": "Part (i): P(6) = 750 + 300 = 1,050 people.\nPart (ii): Linear expression: P(t) = 50t + 750.\nStep 3: Slope = 50 (constant annual addition); y-intercept = 750 (initial population).",
                "finalAnswer": "(i) 1,050 people; (ii) P(t) = 50t + 750",
                "unit": "people",
                "has_diagram": False
            },
            {
                "problem": "Exercise 2.4 Q4: A telecom company charges Rs 600 for a certain recharge scheme that includes a baseline bundle plus Rs 1.50 per additional calling minute. Find a linear expression for the monthly bill B if m additional minutes are used, and compute the bill for 120 additional minutes.",
                "given": "Fixed plan charge = Rs 600. Per-minute rate = Rs 1.50. Additional minutes = m.",
                "formula": "Bill B(m) = 600 + 1.50m.",
                "substitution": "B(120) = 600 + 1.50 * 120.",
                "calculation": "Step 1: Write linear expression: B(m) = 1.50m + 600.\nStep 2: Additional cost for 120 min: 1.50 * 120 = Rs 180.\nStep 3: Total bill: 600 + 180 = Rs 780.",
                "finalAnswer": "B(m) = 1.50m + 600; Total bill for 120 minutes = Rs 780",
                "unit": "rupees",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Confusing depreciation (subtraction) with growth (addition). Depreciation must have a negative slope -800.",
            "Assuming linear growth can continue indefinitely into negative values: physical models have domain restrictions (e.g. remaining pages >= 0)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Show students that all these diverse scenarios (plants, savings, depreciation, phone bills) are identical mathematical objects: y = mt + c.",
        "visual_lesson_plan": {
            "title": "Real-World Linear Models: Growth & Decay",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Plant growth line h(t) = 1.75 + 0.5t showing monthly milestones.",
            "concept_visuals": [
                {
                    "concept_title": "Plant Growth Trajectory h(t) = 1.75 + 0.5t",
                    "diagram_title": "Monthly Height Progression",
                    "interactive_math_formula": "h(t) = 0.5t + 1.75",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [0, 8],
                        "curves": [
                            {"fn": "0.5*x + 1.75", "color": "#16A34A", "label": "h(t) = 0.5t + 1.75"}
                        ],
                        "points": [
                            {"x": 0, "y": 1.75, "label": "Initial: 1.75 ft"},
                            {"x": 7, "y": 5.25, "label": "Month 7: 5.25 ft"},
                            {"x": 10, "y": 6.75, "label": "Month 10: 6.75 ft"}
                        ]
                    },
                    "image_query": "plant growth linear function graph science mathematics",
                    "video_query": "linear growth rate of change biology word problem",
                    "what_to_explain": "Each month the plant adds exactly half a foot, creating a constant slope of 0.5."
                },
                {
                    "concept_title": "Asset Depreciation Decay Line",
                    "diagram_title": "Phone Value V(t) = 10000 - 800t over 5 Years",
                    "interactive_math_formula": "V(t) = 10000 - 800t",
                    "mafs_graph_config": {
                        "domain": [0, 6],
                        "range": [5000, 11000],
                        "curves": [
                            {"fn": "10000 - 800*x", "color": "#DC2626", "label": "V(t) = 10000 - 800t"}
                        ],
                        "points": [
                            {"x": 0, "y": 10000, "label": "New: Rs 10,000"},
                            {"x": 3, "y": 7600, "label": "Year 3: Rs 7,600"},
                            {"x": 5, "y": 6000, "label": "Year 5: Rs 6,000"}
                        ]
                    },
                    "image_query": "straight line depreciation asset value linear graph",
                    "video_query": "linear depreciation formula accounting algebra",
                    "what_to_explain": "The constant loss of Rs 800 per year produces straight-line depreciation with negative slope."
                },
                {
                    "concept_title": "Book Reading Depletion Ray",
                    "diagram_title": "Pages Remaining R(d) = 500 - 20d",
                    "interactive_math_formula": "R(d) = 500 - 20d",
                    "mafs_graph_config": {
                        "domain": [0, 30],
                        "range": [0, 550],
                        "curves": [
                            {"fn": "500 - 20*x", "color": "#2563EB", "label": "Pages R(d)"}
                        ],
                        "points": [
                            {"x": 0, "y": 500, "label": "Start: 500 pages"},
                            {"x": 25, "y": 0, "label": "Finished: Day 25"}
                        ]
                    },
                    "image_query": "linear reading rate pages remaining algebra graph",
                    "video_query": "rate of change reading word problem algebra",
                    "what_to_explain": "Reading 20 pages daily completes the entire 500-page book on day 25."
                },
                {
                    "concept_title": "Village Demographic Expansion",
                    "diagram_title": "Population P(t) = 50t + 750",
                    "interactive_math_formula": "P(t) = 50t + 750",
                    "mafs_graph_config": {
                        "domain": [0, 10],
                        "range": [700, 1300],
                        "curves": [
                            {"fn": "50*x + 750", "color": "#D97706", "label": "P(t) = 50t + 750"}
                        ],
                        "points": [
                            {"x": 0, "y": 750, "label": "Initial: 750"},
                            {"x": 6, "y": 1050, "label": "Year 6: 1,050"}
                        ]
                    },
                    "image_query": "population growth linear graph constant migration",
                    "video_query": "linear population growth model algebra",
                    "what_to_explain": "Constant influx of 50 residents per year causes linear population growth."
                },
                {
                    "concept_title": "Telecom Two-Part Tariff Structure",
                    "diagram_title": "Bill B(m) = 1.50m + 600",
                    "interactive_math_formula": "B(m) = 1.50m + 600",
                    "mafs_graph_config": {
                        "domain": [0, 200],
                        "range": [500, 1000],
                        "curves": [
                            {"fn": "1.5*x + 600", "color": "#7C3AED", "label": "B(m) = 1.5m + 600"}
                        ],
                        "points": [
                            {"x": 0, "y": 600, "label": "Base Plan: Rs 600"},
                            {"x": 120, "y": 780, "label": "120 min: Rs 780"}
                        ]
                    },
                    "image_query": "utility bill linear tariff fixed charge variable cost graph",
                    "video_query": "linear equation utility telephone bill word problems",
                    "what_to_explain": "The fixed plan fee represents the y-intercept, while the call rate sets the line's slope."
                }
            ],
            "concept_questions": [
                {
                    "theme": "Exercises 2.3 & 2.4 Mastery",
                    "questions": [
                        {
                            "question": "What is the height of the plant after 7 months if h(t) = 1.75 + 0.5t?",
                            "type": "short_answer",
                            "options": ["5.25 feet", "5.0 feet", "4.75 feet", "3.5 feet"],
                            "ideal_answer": "5.25 feet, from 1.75 + 0.5(7) = 1.75 + 3.5 = 5.25.",
                            "socratic_hint": "Multiply 0.5 by 7, then add 1.75."
                        },
                        {
                            "question": "After how many days does Sarita finish reading the 500-page book at 20 pages per day?",
                            "type": "short_answer",
                            "options": ["25 days", "20 days", "30 days", "50 days"],
                            "ideal_answer": "25 days, from 500 / 20 = 25.",
                            "socratic_hint": "Divide 500 by 20."
                        },
                        {
                            "question": "What is the value of the Rs 10,000 phone after 3 years if it depreciates by Rs 800 each year?",
                            "type": "short_answer",
                            "options": ["Rs 7,600", "Rs 8,400", "Rs 6,800", "Rs 9,200"],
                            "ideal_answer": "Rs 7,600, from 10,000 - 3 * 800 = 10,000 - 2,400 = 7,600.",
                            "socratic_hint": "Subtract 3 years of 800 from 10,000."
                        },
                        {
                            "question": "In a linear function y = mt + c, what does the constant c represent physically?",
                            "type": "short_answer",
                            "options": [
                                "The initial value or baseline state at time t = 0",
                                "The rate of change per month",
                                "The time when the value becomes zero",
                                "The maximum possible value"
                            ],
                            "ideal_answer": "The initial value at t = 0 (the starting height, deposit, or fixed base fee).",
                            "socratic_hint": "What is the value of y when t is zero?"
                        },
                        {
                            "question": "If a rally loses 9 members each hour from an initial 120, how many members remain after 6 hours?",
                            "type": "short_answer",
                            "options": ["66", "54", "74", "80"],
                            "ideal_answer": "66, from 120 - 9(6) = 120 - 54 = 66.",
                            "socratic_hint": "Compute 9 * 6, then subtract from 120."
                        }
                    ]
                }
            ]
        }
    }
