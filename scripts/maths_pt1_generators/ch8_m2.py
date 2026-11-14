"""
scripts/maths_pt1_generators/ch8_m2.py
Module 2 for Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Topic: Arithmetic Progressions (AP), Common Difference & General Term a_n = a + (n-1)d
"""

def get_m2():
    svg_diagram = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="800" height="500" fill="#0f172a" rx="16"/>
  <text x="400" y="45" font-family="system-ui, sans-serif" font-size="22" fill="#38bdf8" font-weight="bold" text-anchor="middle">Arithmetic Progression: The Constant Staircase d</text>
  
  <!-- Left Side: AP Staircase 3, 8, 13, 18, 23 (d = +5) -->
  <g transform="translate(60, 90)">
    <text x="140" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Growing AP: a = 3, d = 5</text>
    
    <!-- Step 1: n=1, t1 = 3 -->
    <rect x="20" y="240" width="45" height="30" fill="#38bdf8" rx="4"/>
    <text x="42" y="230" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" text-anchor="middle">3</text>
    <text x="42" y="290" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">n=1</text>
    
    <!-- Step 2: n=2, t2 = 8 -->
    <rect x="75" y="190" width="45" height="80" fill="#38bdf8" rx="4"/>
    <text x="97" y="180" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" text-anchor="middle">8</text>
    <text x="97" y="290" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">n=2</text>
    
    <!-- Step 3: n=3, t3 = 13 -->
    <rect x="130" y="140" width="45" height="130" fill="#38bdf8" rx="4"/>
    <text x="152" y="130" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" text-anchor="middle">13</text>
    <text x="152" y="290" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">n=3</text>
    
    <!-- Step 4: n=4, t4 = 18 -->
    <rect x="185" y="90" width="45" height="180" fill="#38bdf8" rx="4"/>
    <text x="207" y="80" font-family="system-ui, sans-serif" font-size="13" fill="#38bdf8" text-anchor="middle">18</text>
    <text x="207" y="290" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">n=4</text>
    
    <!-- Step 5: n=5, t5 = 23 -->
    <rect x="240" y="40" width="45" height="230" fill="#4ade80" rx="4"/>
    <text x="262" y="30" font-family="system-ui, sans-serif" font-size="13" fill="#4ade80" text-anchor="middle">23</text>
    <text x="262" y="290" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">n=5</text>
    
    <!-- Increment arrows showing +5 -->
    <path d="M42,210 Q65,180 85,185" fill="none" stroke="#facc15" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="65" y="170" font-family="system-ui, sans-serif" font-size="11" fill="#facc15">+5</text>
    
    <text x="150" y="325" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">General Term: t_n = 3 + (n - 1)&times;5 = 5n - 2</text>
  </g>
  
  <!-- Right Side: Decreasing AP 21, 18, 15, ..., 0, ..., -81 -->
  <g transform="translate(460, 90)">
    <text x="150" y="0" font-family="system-ui, sans-serif" font-size="16" fill="#94a3b8" font-weight="bold" text-anchor="middle">Decreasing AP: a = 21, d = -3</text>
    
    <!-- Axes -->
    <line x1="20" y1="160" x2="300" y2="160" stroke="#64748b" stroke-width="2"/>
    <text x="305" y="165" font-family="system-ui, sans-serif" font-size="12" fill="#64748b">Axis (y=0)</text>
    
    <!-- Points on line y = 24 - 3x -->
    <line x1="30" y1="50" x2="270" y2="250" stroke="#f43f5e" stroke-width="3"/>
    
    <circle cx="50" cy="65" r="6" fill="#38bdf8"/>
    <text x="50" y="50" font-family="system-ui, sans-serif" font-size="12" fill="#38bdf8">t_1 = 21</text>
    
    <circle cx="110" cy="115" r="6" fill="#38bdf8"/>
    <text x="110" y="100" font-family="system-ui, sans-serif" font-size="12" fill="#38bdf8">t_4 = 12</text>
    
    <circle cx="165" cy="160" r="7" fill="#4ade80"/>
    <text x="165" y="145" font-family="system-ui, sans-serif" font-size="12" fill="#4ade80" font-weight="bold">t_8 = 0 (Root!)</text>
    
    <circle cx="230" cy="215" r="6" fill="#fb923c"/>
    <text x="245" y="225" font-family="system-ui, sans-serif" font-size="12" fill="#fb923c">t_{35} = -81</text>
    
    <text x="150" y="290" font-family="system-ui, sans-serif" font-size="13" fill="#cbd5e1" text-anchor="middle">Common difference d = -3 is negative</text>
    <text x="150" y="325" font-family="system-ui, sans-serif" font-size="13" fill="#f43f5e" font-weight="bold" text-anchor="middle">Crosses zero at exactly n = 8</text>
  </g>
</svg>'''

    worked_examples = [
        {
            "problem": "Exercise 8.2 Q1: Find the 10th and 26th terms of the AP: 3, 8, 13, 18, ....",
            "given": "AP: 3, 8, 13, 18, ... First term a = 3, common difference d = 8 - 3 = 5.",
            "formula": "a_n = a + (n - 1)d",
            "substitution": "For n = 10: a_10 = 3 + (10 - 1)*5. For n = 26: a_26 = 3 + (26 - 1)*5.",
            "calculation": "a_10 = 3 + 9*5 = 3 + 45 = 48.\na_26 = 3 + 25*5 = 3 + 125 = 128.",
            "finalAnswer": "a_10 = 48, a_26 = 128",
            "unit": "AP terms",
            "has_diagram": True
        },
        {
            "problem": "Exercise 8.2 Q2 (i): Which term of the AP: 21, 18, 15, ... is -81?",
            "given": "AP: 21, 18, 15, ... First term a = 21, common difference d = 18 - 21 = -3. Target term a_n = -81.",
            "formula": "a_n = a + (n - 1)d => -81 = 21 + (n - 1)(-3)",
            "substitution": "-81 - 21 = -3(n - 1) => -102 = -3(n - 1)",
            "calculation": "n - 1 = -102 / -3 = 34 => n = 34 + 1 = 35.",
            "finalAnswer": "-81 is the 35th term of the AP.",
            "unit": "term index",
            "has_diagram": True
        },
        {
            "problem": "Exercise 8.2 Q2 (ii): Is 0 a term of the AP: 21, 18, 15, ...? Give reasons for your answer.",
            "given": "AP: 21, 18, 15, ... with a = 21, d = -3. Candidate value = 0.",
            "formula": "a_n = a + (n - 1)d = 0 => 21 + (n - 1)(-3) = 0",
            "substitution": "-3(n - 1) = -21 => n - 1 = 7",
            "calculation": "n = 7 + 1 = 8. Since n = 8 is a natural number, 0 is indeed a member.",
            "finalAnswer": "Yes, 0 is the 8th term of this AP.",
            "unit": "term verification",
            "has_diagram": True
        },
        {
            "problem": "Exercise 8.2 Q3: Find the nth term of the AP: 11, 8, 5, 2, .... Also write the recursive rule for this AP.",
            "given": "AP: 11, 8, 5, 2, ... First term a = 11, common difference d = 8 - 11 = -3.",
            "formula": "Explicit formula: t_n = a + (n - 1)d. Recursive formula: t_1 = a, t_n = t_{n-1} + d for n >= 2.",
            "substitution": "t_n = 11 + (n - 1)(-3) = 11 - 3n + 3",
            "calculation": "Explicit rule: t_n = 14 - 3n.\nRecursive rule: t_1 = 11, t_n = t_{n-1} - 3 for n >= 2.",
            "finalAnswer": "Explicit: t_n = 14 - 3n; Recursive: t_1 = 11, t_n = t_{n-1} - 3 (n >= 2)",
            "unit": "algebraic formulas",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.2 Q4: An AP consists of 50 terms in which the 3rd term is 12 and the last term is 106. Find the 29th term.",
            "given": "Total terms n = 50. Third term a_3 = 12. Fiftieth term a_50 = 106.",
            "formula": "a_3 = a + 2d = 12 (Equation 1); a_50 = a + 49d = 106 (Equation 2). Subtract Eq 1 from Eq 2.",
            "substitution": "(a + 49d) - (a + 2d) = 106 - 12 => 47d = 94",
            "calculation": "d = 94 / 47 = 2.\nSubstitute d = 2 into Eq 1: a + 2(2) = 12 => a + 4 = 12 => a = 8.\nNow find 29th term: a_29 = a + 28d = 8 + 28(2) = 8 + 56 = 64.",
            "finalAnswer": "a_29 = 64 (with a = 8, d = 2)",
            "unit": "AP term value",
            "has_diagram": False
        },
        {
            "problem": "Exercise 8.2 Q6: Harish started work in 1995 at an annual salary of Rs 5,00,000 and received an annual increment of Rs 20,000 each year. After how many years did his income reach Rs 7,00,000?",
            "given": "First year salary a = 5,00,000. Annual increase d = 20,000. Target salary a_n = 7,00,000.",
            "formula": "a_n = a + (n - 1)d => 7,00,000 = 5,00,000 + (n - 1)*20,000",
            "substitution": "(n - 1)*20,000 = 7,00,000 - 5,00,000 = 2,00,000",
            "calculation": "n - 1 = 2,00,000 / 20,000 = 10 => n = 11.\nHere n = 11 means in the 11th year of service, which occurs after 10 completed years.",
            "finalAnswer": "His income reached Rs 7,00,000 in the 11th year (after 10 years of service).",
            "unit": "years",
            "has_diagram": False
        },
        {
            "problem": "In-Text Example 5: A taxi charges Rs 20 for the first kilometer and Rs 8 for each subsequent kilometer. Formulate the AP for the fare of travel and calculate the total fare for a journey of 15 km.",
            "given": "Fare for 1 km a = 20. Charge per subsequent km d = 8. Journey distance n = 15 km.",
            "formula": "Fare for n km: t_n = a + (n - 1)d = 20 + (n - 1)*8",
            "substitution": "t_15 = 20 + (15 - 1)*8 = 20 + 14*8",
            "calculation": "14 * 8 = 112.\nt_15 = 20 + 112 = 132.",
            "finalAnswer": "Total fare for 15 km is Rs 132 (AP: 20, 28, 36, 44, ...).",
            "unit": "Rupees",
            "has_diagram": False
        },
        {
            "problem": "Square Pattern Recurrence (Textbook Fig. 8.3 & 8.4): In a growing square pattern with counts 1, 5, 9, 13, ..., find the common difference d, the explicit rule, and predict the 20th stage.",
            "given": "Sequence of square counts: 1, 5, 9, 13, ...",
            "formula": "d = t_2 - t_1; t_n = a + (n - 1)d",
            "substitution": "a = 1, d = 5 - 1 = 4. t_20 = 1 + (20 - 1)*4.",
            "calculation": "t_n = 1 + 4n - 4 = 4n - 3.\nt_20 = 4(20) - 3 = 80 - 3 = 77.",
            "finalAnswer": "Common difference d = 4; Rule t_n = 4n - 3; 20th stage has 77 squares.",
            "unit": "squares count",
            "has_diagram": True
        },
        {
            "problem": "General Term Difference Theorem: In any AP with common difference d, prove that for any two term indices p and q, a_p - a_q = (p - q)d. Use this to find d if the 20th term is 65 and the 12th term is 41.",
            "given": "General AP: a_p = a + (p-1)d, a_q = a + (q-1)d. Values: a_20 = 65, a_12 = 41.",
            "formula": "a_p - a_q = [a + (p-1)d] - [a + (q-1)d] = (p - 1 - q + 1)d = (p - q)d",
            "substitution": "a_20 - a_12 = (20 - 12)d => 65 - 41 = 8d",
            "calculation": "24 = 8d => d = 24 / 8 = 3.",
            "finalAnswer": "Theorem proven: a_p - a_q = (p - q)d. For given data, d = 3.",
            "unit": "theorem proof and common difference",
            "has_diagram": False
        }
    ]

    concept_visuals = [
        {
            "concept_title": "Arithmetic Progression as a Linear Ray",
            "diagram_title": "Discrete Arithmetic Points Sampled on y = dx + c",
            "interactive_math_formula": "a_n = dn + (a - d)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 8],
                "y_range": [0, 40],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": -2, "x2": 8, "y2": 38, "color": "#38bdf8", "label": "y = 5x - 2"}
                ],
                "points": [
                    {"x": 1, "y": 3, "label": "a1 = 3"},
                    {"x": 2, "y": 8, "label": "a2 = 8"},
                    {"x": 3, "y": 13, "label": "a3 = 13"},
                    {"x": 4, "y": 18, "label": "a4 = 18"},
                    {"x": 5, "y": 23, "label": "a5 = 23"}
                ]
            },
            "image_query": "arithmetic progression linear graph constant slope d",
            "video_query": "why arithmetic progression is linear function slope common difference",
            "what_to_explain": "Show that the common difference d corresponds exactly to the slope of a linear function. The discrete points of an AP lie perfectly on a line."
        },
        {
            "concept_title": "Decreasing AP & Negative Zero Crossing",
            "diagram_title": "AP with Negative Common Difference d = -3",
            "interactive_math_formula": "a_n = 21 + (n - 1)(-3) = 24 - 3n",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 12],
                "y_range": [-10, 25],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 24, "x2": 10, "y2": -6, "color": "#f43f5e", "label": "y = 24 - 3x"}
                ],
                "points": [
                    {"x": 1, "y": 21, "label": "a1 = 21"},
                    {"x": 4, "y": 12, "label": "a4 = 12"},
                    {"x": 8, "y": 0, "label": "a8 = 0 (Root)"},
                    {"x": 10, "y": -6, "label": "a10 = -6"}
                ]
            },
            "image_query": "decreasing arithmetic sequence graph negative slope crossing zero",
            "video_query": "decreasing AP negative common difference zero crossing",
            "what_to_explain": "Demonstrate that an AP decreases when d < 0, crossing the horizontal axis at n = 8 and producing increasingly negative values thereafter."
        },
        {
            "concept_title": "Simultaneous System for AP Parameters",
            "diagram_title": "Intersection of Linear Constraints a + 2d = 12 and a + 49d = 106",
            "interactive_math_formula": "47d = 94 \\implies d = 2, \\; a = 8",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 5],
                "y_range": [0, 15],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 12, "x2": 5, "y2": 2, "color": "#facc15", "label": "a + 2d = 12"},
                    {"x1": 1.5, "y1": 32.5, "x2": 2.5, "y2": -16.5, "color": "#c084fc", "label": "a + 49d = 106"}
                ],
                "points": [{"x": 2, "y": 8, "label": "Solution: (d=2, a=8)"}]
            },
            "image_query": "system of linear equations in a and d for AP",
            "video_query": "finding first term and common difference from two AP terms",
            "what_to_explain": "Explain how knowing any two arbitrary terms in an AP provides two independent linear equations in two unknowns (a and d)."
        },
        {
            "concept_title": "Real-World AP: Stepped Taxi Meter",
            "diagram_title": "Cost Model: Base Fare + Rate per Kilometer",
            "interactive_math_formula": "\\text{Fare}(n) = 20 + 8(n - 1)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 16],
                "y_range": [0, 150],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 20, "x2": 15, "y2": 132, "color": "#4ade80", "label": "Fare: 20 + 8(x-1)"}
                ],
                "points": [{"x": 1, "y": 20}, {"x": 5, "y": 52}, {"x": 10, "y": 92}, {"x": 15, "y": 132}]
            },
            "image_query": "taxi fare linear arithmetic progression graph",
            "video_query": "real world applications arithmetic progression taxi fare",
            "what_to_explain": "Connect AP to everyday billing structures: an initial flag-down cost plus a constant increment per additional unit of distance."
        },
        {
            "concept_title": "The Invariant Difference Property",
            "diagram_title": "Constant First Difference Delta a_n = d",
            "interactive_math_formula": "\\Delta a_n = a_{n+1} - a_n = d \\quad \\forall n \\ge 1",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 8],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 5, "x2": 6, "y2": 5, "color": "#38bdf8", "label": "d = 5 (Constant Delta)"}
                ],
                "points": [{"x": 1, "y": 5}, {"x": 2, "y": 5}, {"x": 3, "y": 5}, {"x": 4, "y": 5}]
            },
            "image_query": "constant first difference arithmetic progression horizontal line",
            "video_query": "common difference invariance test for arithmetic progression",
            "what_to_explain": "Emphasize that the signature defining feature of an AP is that the plot of first differences is a horizontal line of constant height d."
        }
    ]

    concept_questions = [
        {
            "concept": "AP Definition & Common Difference",
            "questions": [
                {
                    "question": "Can the common difference d of an arithmetic progression be negative, zero, or a fraction?",
                    "type": "conceptual",
                    "ideal_answer": "Yes. If d > 0, the AP is increasing; if d < 0, it is decreasing; if d = 0, all terms are equal (a constant sequence); and d can be any real number including fractions and irrationals.",
                    "socratic_hint": "What happens to the terms when d = -3 or d = 0?"
                },
                {
                    "question": "Why is the formula for the nth term a + (n - 1)d rather than a + nd?",
                    "type": "conceptual",
                    "ideal_answer": "Because the first term 'a' requires zero additions of d. To reach the nth term from the 1st term, exactly (n - 1) steps of size d are taken.",
                    "socratic_hint": "How many steps do you take to go from step 1 to step 1?"
                }
            ]
        }
    ]

    return {
        "order_index": 2,
        "title": "Arithmetic Progressions (AP), Common Difference & General Term a_n = a + (n-1)d",
        "description": "Establish the formal definition of an Arithmetic Progression, compute the common difference d, master the general term formula a_n = a + (n-1)d, and solve linear systems for unknown progression parameters.",
        "subtopics": [
            "Formal Definition: Successive Difference Invariant",
            "Sign of Common Difference: Increasing, Decreasing, Constant APs",
            "The General nth Term: a_n = a + (n - 1)d",
            "Zero and Negative Value Intercepts in APs",
            "Solving Systems of Two Terms: a + (p-1)d and a + (q-1)d",
            "Real-World Modeling: Depreciation, Taxi Meters, and Salary Increments"
        ],
        "key_concepts": [
            "AP defining property: a_{n+1} - a_n = d",
            "nth term formula: a_n = a + (n - 1)d",
            "Difference between two terms: a_p - a_q = (p - q)d",
            "Equivalence of linear functions y = mx + c and explicit AP rules",
            "Recursive AP formulation: t_1 = a, t_n = t_{n-1} + d"
        ],
        "success_criteria": "Students can identify APs, determine their first term and common difference, calculate any specified term, verify whether given numbers belong to the AP, and resolve parameter systems.",
        "chapter_notes": "An AP is the discrete analogue of a linear function with constant slope d. Mastering the relationship a_p - a_q = (p - q)d allows solving multi-term exam problems with rapid algebraic efficiency.",
        "common_misconceptions": [
            {
                "misconception": "The nth term of an AP is a + nd.",
                "clarification": "The first term is a + 0d. Therefore, the nth term is a + (n - 1)d.",
                "misconception": "An AP cannot contain negative terms.",
                "clarification": "An AP with d < 0 will eventually cross zero and produce infinitely many negative terms."
            }
        ],
        "ai_system_prompt_context": "Use the staircase analogy to explain why we multiply d by (n - 1). Show students how setting a_n = 0 finds the exact crossing point.",
        "visual_lesson_plan": {
            "title": "Staircase Model of Arithmetic Progressions",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": svg_diagram,
            "what_to_make": "A dual-panel visual showing an increasing AP staircase on the left and a decreasing AP line crossing zero on the right.",
            "concept_visuals": concept_visuals,
            "concept_questions": concept_questions
        },
        "worked_examples": worked_examples
    }
