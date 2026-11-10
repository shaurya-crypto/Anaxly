"""
Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Curriculum ID: b45d590f-323e-4263-b899-23d95b2094a7
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

import json
from .svg_builder import (
    build_triangular_numbers_dot_svg,
    build_cartesian_svg,
    build_sierpinski_triangle_svg,
    build_bouncing_ball_decay_svg,
    get_svg_wrapper
)

def get_ch8_modules():
    curriculum_id = "b45d590f-323e-4263-b899-23d95b2094a7"
    
    # -------------------------------------------------------------
    # MODULE 1: Patterns, Triangular Numbers & Explicit vs Recursive Rules
    # -------------------------------------------------------------
    m1_svg = build_triangular_numbers_dot_svg(
        title="Triangular Numbers: T_n = n(n+1)/2",
        caption="T₁=1, T₂=3, T₃=6, T₄=10, T₅=15. Sum of consecutive triangular numbers equals a square number!"
    )

    m1 = {
        "order_index": 1,
        "title": "Sequences, Triangular Patterns & Rules: Explicit Formulas vs Recursive Relations",
        "description": "Formulate mathematical sequences as ordered lists of numbers obeying a deterministic rule. Contrast explicit formulas t_n = f(n) with recursive definitions t_{n+1} = g(t_n). Explore figurate triangular numbers T_n = n(n+1)/2 and their geometric dot patterns.",
        "subtopics": [
            "Definition of a sequence: Ordered terms t_1, t_2, ..., t_n indexed by natural numbers",
            "Figurate numbers: Visualizing triangular numbers T_n = n(n+1)/2 with geometric dot arrays",
            "Pairing consecutive triangular numbers to produce square numbers: T_n + T_{n-1} = n^2",
            "Explicit rules: Direct evaluation of arbitrary terms (e.g. t_n = 3n - 7, finding 1170th term)",
            "Recursive rules: Defining subsequent terms from predecessors (e.g. t_1 = 1, t_{n+1} = t_n + n + 1)",
            "Testing sequence membership: Determining if a given integer belongs to a sequence"
        ],
        "key_concepts": [
            "Sequence Definition: A mapping from the set of natural numbers {1, 2, 3, ...} to real numbers, denoted as {t_n}.",
            "Explicit Formula Invariant: Expresses t_n purely in terms of its position index n. Allows instant calculation of ANY term (such as t_1000) in O(1) time without computing prior terms.",
            "Recursive Formula Invariant: Expresses t_{n+1} using one or more preceding terms (t_n, t_{n-1}) along with an initial base condition t_1.",
            "Triangular Number Formula: T_n = 1 + 2 + 3 + ... + n = n(n + 1) / 2. Geometrically represented by packing an n x (n+1) rectangle with two congruent triangular dot arrays.",
            "Consecutive Triangular Square Theorem: T_n + T_{n-1} = n(n+1)/2 + (n-1)n/2 = n/2 * (n + 1 + n - 1) = n/2 * (2n) = n^2."
        ],
        "success_criteria": "Generate terms from explicit and recursive rules, calculate triangular numbers, and test whether numbers belong to a given sequence.",
        "chapter_notes": "Triangular numbers provide the vital geometric hook for sequences in Ganita Manjari. Point out how two copies of T_n fit together into an n by (n+1) rectangle.",
        "worked_examples": [
            {
                "problem": "Textbook In-Text Exercise: Consider the explicit rule t_n = 3n - 7. (i) Find its 1st, 2nd, 3rd, 12th, 18th, and 50th terms. (ii) Which term of the sequence is 332? (iii) Is 557 a term of this sequence? Explain why or why not.",
                "given": "Explicit rule: t_n = 3n - 7 for n >= 1.",
                "formula": "Substitute n into t_n = 3n - 7. To test membership, solve 3n - 7 = Target for natural number n.",
                "substitution": "(i) n = 1, 2, 3, 12, 18, 50. (ii) 3n - 7 = 332. (iii) 3n - 7 = 557.",
                "calculation": "Part (i):\\n  t_1 = 3(1) - 7 = 3 - 7 = -4\\n  t_2 = 3(2) - 7 = 6 - 7 = -1\\n  t_3 = 3(3) - 7 = 9 - 7 = 2\\n  t_12 = 3(12) - 7 = 36 - 7 = 29\\n  t_18 = 3(18) - 7 = 54 - 7 = 47\\n  t_50 = 3(50) - 7 = 150 - 7 = 143.\\n\\nPart (ii):\\n  Set t_n = 332:\\n  3n - 7 = 332\\n  3n = 332 + 7 = 339\\n  n = 339 / 3 = 113.\\n  Since 113 is a positive integer, 332 IS the 113th term of the sequence.\\n\\nPart (iii):\\n  Set t_n = 557:\\n  3n - 7 = 557\\n  3n = 557 + 7 = 564\\n  n = 564 / 3 = 188.\\n  Since 188 is a positive integer, 557 IS the 188th term of the sequence.",
                "finalAnswer": "(i) t_1=-4, t_2=-1, t_3=2, t_12=29, t_18=47, t_50=143; (ii) 332 is the 113th term; (iii) 557 is the 188th term",
                "unit": "sequence terms and index integers",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m1_svg
            },
            {
                "problem": "Textbook Exercise 8.1 Q1 (iii): Find the first five terms of the sequence whose nth term is given by t_n = n^2 - 2n + 3 for n >= 1.",
                "given": "Quadratic explicit formula: t_n = n^2 - 2n + 3.",
                "formula": "Evaluate for n = 1, 2, 3, 4, 5.",
                "substitution": "Substitute n = 1, 2, 3, 4, 5 into n^2 - 2n + 3.",
                "calculation": "Step 1: n = 1:\\n  t_1 = (1)^2 - 2(1) + 3 = 1 - 2 + 3 = 2.\\nStep 2: n = 2:\\n  t_2 = (2)^2 - 2(2) + 3 = 4 - 4 + 3 = 3.\\nStep 3: n = 3:\\n  t_3 = (3)^2 - 2(3) + 3 = 9 - 6 + 3 = 6.\\nStep 4: n = 4:\\n  t_4 = (4)^2 - 2(4) + 3 = 16 - 8 + 3 = 11.\\nStep 5: n = 5:\\n  t_5 = (5)^2 - 2(5) + 3 = 25 - 10 + 3 = 18.\\nSequence of terms: 2, 3, 6, 11, 18, ...",
                "finalAnswer": "First five terms: 2, 3, 6, 11, 18",
                "unit": "sequence terms",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Conflating the term index n (position 1, 2, 3...) with the term value t_n. The index n must ALWAYS be a positive integer {1, 2, 3...}.",
            "Thinking that any number can be a term in an AP. If solving t_n = K yields a fraction (like n = 7.4), then K is NOT a term of that sequence!"
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Start with the triangular bowling pin formation (1, 3, 6, 10). Show how adding a new row of n dots creates T_n = T_{n-1} + n. Contrast this with the instant formula n(n+1)/2. Call write_chalkboard(action='draw_svg_diagram', content='Triangular Numbers').",
        "visual_lesson_plan": {
            "title": "Triangular Numbers & Rules",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Dot patterns for triangular numbers T1 through T5.",
            "concept_visuals": [
                {
                    "concept_title": "Figurate Dot Patterns",
                    "diagram_title": "Triangular Numbers T_n",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m1_svg,
                    "interactive_math_formula": "T_n = n(n+1)/2",
                    "mafs_graph_config": {"domain": [-1, 10], "range": [-1, 16]},
                    "image_query": "Triangular numbers visual dot pattern geometric sequence proof",
                    "video_query": "Triangular numbers formula visual proof explained",
                    "image_url": "/images/curriculum/ch8_triangular_numbers.png",
                    "what_to_make": "Arrays of dots forming equilateral triangles.",
                    "what_to_explain": "Walk through T_n + T_{n-1} = n^2.",
                    "timing_and_cue": "Show during figurate number discussion."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Sequences & Triangular Numbers",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the 10th triangular number T_10?",
                            "ideal_answer": "55, because T_10 = 10 * 11 / 2 = 110 / 2 = 55.",
                            "socratic_hint": "Use T_n = n(n+1)/2 with n = 10."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What shape is formed when two consecutive triangular numbers T_n and T_{n-1} are joined together?",
                            "ideal_answer": "A perfect square of side n, because T_n + T_{n-1} = n^2.",
                            "socratic_hint": "Add the algebraic expressions for T_n and T_{n-1}."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "If a sequence has explicit rule t_n = 4n - 1, find its 25th term.",
                            "ideal_answer": "t_25 = 4(25) - 1 = 100 - 1 = 99.",
                            "socratic_hint": "Substitute n = 25 into the formula."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Is 100 a term of the sequence t_n = 7n + 2?",
                            "ideal_answer": "Set 7n + 2 = 100 => 7n = 98 => n = 14. Since 14 is a positive integer, yes, 100 is the 14th term.",
                            "socratic_hint": "Solve 7n + 2 = 100 for n: is n an integer?"
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "A sequence is defined recursively by t_1 = 3 and t_{n+1} = 2t_n - 1 for n >= 1. Find the first four terms and deduce an explicit formula for t_n.",
                            "ideal_answer": "t_1 = 3. t_2 = 2(3) - 1 = 5. t_3 = 2(5) - 1 = 9. t_4 = 2(9) - 1 = 17. The terms are 3, 5, 9, 17... Notice they can be written as 2^1 + 1, 2^2 + 1, 2^3 + 1, 2^4 + 1. Explicit formula: t_n = 2^n + 1.",
                            "socratic_hint": "Examine the powers of 2 in relation to the sequence terms."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 2: Arithmetic Progressions (AP) & General Term
    # -------------------------------------------------------------
    m2_svg = build_cartesian_svg(
        domain=(0, 6), range_y=(0, 20),
        points=[
            {"x": 1, "y": 3, "label": "t₁ = 3", "color": "#2563EB", "sub": "(1, 3)"},
            {"x": 2, "y": 6, "label": "t₂ = 6", "color": "#2563EB", "sub": "(2, 6)"},
            {"x": 3, "y": 9, "label": "t₃ = 9", "color": "#2563EB", "sub": "(3, 9)"},
            {"x": 4, "y": 12, "label": "t₄ = 12", "color": "#2563EB", "sub": "(4, 12)"},
            {"x": 5, "y": 15, "label": "t₅ = 15", "color": "#2563EB", "sub": "(5, 15)"}
        ],
        lines=[
            {"p1": (0, 0), "p2": (6, 18), "color": "#2563EB", "stroke_width": 2, "label": "t_n = 3 + (n-1)*3 = 3n"}
        ],
        title="Arithmetic Progression as a Linear Graph: t_n = a + (n-1)d",
        caption="Points (n, t_n) form a straight line with constant slope d (Common Difference)"
    )

    m2 = {
        "order_index": 2,
        "title": "Arithmetic Progressions (AP): Common Difference, General Term t_n = a + (n-1)d & Linear Plots",
        "description": "Establish Arithmetic Progressions where each term differs from the previous by a constant difference d. Derive the general nth term formula t_n = a + (n-1)d. Prove that plotting (n, t_n) on Cartesian axes produces collinear points on a line of slope d.",
        "subtopics": [
            "Formal definition of an AP: t_{n+1} - t_n = d (constant for all n >= 1)",
            "Common difference d: Positive (increasing AP), Negative (decreasing AP), Zero (constant AP)",
            "Derivation of the general term: t_n = a + (n - 1)d",
            "Linear correspondence: t_n = dn + (a - d) is a linear function with slope d",
            "Textbook Taxi Fare Model (Example 5): Fixed fee Rs 200 + Rs 40/km",
            "Determining whether a given sequence is an AP by checking consecutive differences"
        ],
        "key_concepts": [
            "Common Difference Invariant: An AP is uniquely determined by two parameters: first term a and common difference d = t_{k+1} - t_k.",
            "General Term Formula: t_n = a + (n - 1)d. The factor is (n - 1), because the first term already accounts for 1 step, requiring (n - 1) further jumps of d.",
            "Linear Graph Equivalence: When plotted on a Cartesian plane with horizontal axis n and vertical axis t_n, the points (n, t_n) lie strictly on a straight line whose slope is identically equal to the common difference d.",
            "Recursive AP Rule: t_1 = a, t_{n+1} = t_n + d."
        ],
        "success_criteria": "Verify if sequences are APs, compute general terms, find specific distant terms, and explain the slope-difference equivalence.",
        "chapter_notes": "Connect Chapter 8 directly back to Chapter 1 & 2! The slope of the line in Chapter 2 is exactly the common difference d of the AP in Chapter 8.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 8.2 Q1 & Q2: (Q1) Find the 10th and 26th terms of the AP: 3, 8, 13, 18, ... (Q2) Which term of the AP: 21, 18, 15, ... is -81? Also, is 0 a term of this AP?",
                "given": "Q1: AP 3, 8, 13, 18... (a = 3, d = 5). Q2: AP 21, 18, 15... (a = 21, d = -3).",
                "formula": "t_n = a + (n - 1)d.",
                "substitution": "Q1: t_10 = 3 + 9(5); t_26 = 3 + 25(5). Q2: 21 + (n-1)(-3) = -81; 21 + (n-1)(-3) = 0.",
                "calculation": "Part (Q1):\\nStep 1: First term a = 3, common difference d = 8 - 3 = 5.\\nStep 2: 10th term: t_10 = a + 9d = 3 + 9(5) = 3 + 45 = 48.\\nStep 3: 26th term: t_26 = a + 25d = 3 + 25(5) = 3 + 125 = 128.\\n\\nPart (Q2):\\nStep 1: a = 21, d = 18 - 21 = -3.\\nStep 2: Find n such that t_n = -81:\\n  21 + (n - 1)(-3) = -81\\n  (n - 1)(-3) = -81 - 21 = -102\\n  n - 1 = -102 / -3 = 34\\n  n = 34 + 1 = 35.\\n  Therefore, -81 is the 35th term.\\nStep 3: Test if 0 is a term:\\n  21 + (n - 1)(-3) = 0\\n  (n - 1)(-3) = -21\\n  n - 1 = 7 => n = 8.\\n  Since n is a positive integer, 0 IS the 8th term of the AP.",
                "finalAnswer": "Q1: t_10 = 48, t_26 = 128; Q2: -81 is the 35th term, and 0 is the 8th term",
                "unit": "AP terms and index integers",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m2_svg
            },
            {
                "problem": "Textbook Example 5 (Taxi Fare Model): A taxi company charges a fixed booking fee of Rs 200 plus Rs 40 per kilometre travelled. Write the sequence representing the total fare after 1 km, 2 km, 3 km, and find the fare for travelling 25 km.",
                "given": "Fixed fee = Rs 200, Rate per km = Rs 40/km.",
                "formula": "Fare sequence: F_n = 200 + 40n. This is an AP with first term a = 240 and d = 40.",
                "substitution": "F_1 = 200 + 40(1) = 240. F_2 = 280. F_3 = 320. Find F_25 = 200 + 40(25).",
                "calculation": "Step 1: Write terms for initial kilometres:\\n  After 1 km: 200 + 40 = Rs 240.\\n  After 2 km: 200 + 40(2) = Rs 280.\\n  After 3 km: 200 + 40(3) = Rs 320.\\n  Sequence: 240, 280, 320, 360, ...\\nStep 2: Check common difference:\\n  280 - 240 = 40; 320 - 280 = 40. Constant d = 40, so it is an AP.\\nStep 3: Calculate fare for 25 km:\\n  F_25 = 200 + 40 * 25 = 200 + 1000 = Rs 1,200.",
                "finalAnswer": "Sequence: 240, 280, 320, ... (AP with a=240, d=40); Fare for 25 km = Rs 1,200",
                "unit": "Indian Rupees",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Writing t_n = a + nd instead of a + (n - 1)d, which mistakenly adds one extra step of d.",
            "Getting the sign of d wrong in decreasing sequences (e.g. 21, 18, 15... has d = -3, not +3)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Plot the points (n, t_n) on the chalkboard grid. Draw the straight line connecting them and compute its slope delta y / delta x = d / 1 = d. Call write_chalkboard(action='draw_svg_diagram', content='Arithmetic Progression Graph').",
        "visual_lesson_plan": {
            "title": "AP General Term & Line Graphs",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Cartesian plot of AP points showing constant slope d.",
            "concept_visuals": [
                {
                    "concept_title": "AP Collinear Graph",
                    "diagram_title": "AP Points on Line",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m2_svg,
                    "interactive_math_formula": "t_n = a + (n-1)d",
                    "mafs_graph_config": {"domain": [0, 8], "range": [0, 25], "lines": [{"formula": "3*x"}]},
                    "image_query": "Arithmetic progression linear function graph cartesian plane slope d",
                    "video_query": "Arithmetic progression general term formula visual line slope",
                    "image_url": "/images/curriculum/ch8_ap_graph.png",
                    "what_to_make": "Cartesian coordinate graph with AP points and line.",
                    "what_to_explain": "Explain why constant difference d corresponds to constant linear slope.",
                    "timing_and_cue": "Show during linear slope explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Arithmetic Progressions",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the common difference d of the AP: -5, -1, 3, 7, ...?",
                            "ideal_answer": "4, because (-1) - (-5) = 4.",
                            "socratic_hint": "Subtract the first term from the second term."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why is the coefficient of (n - 1) in t_n = a + (n - 1)d equal to (n - 1) instead of n?",
                            "ideal_answer": "Because the first term t_1 = a requires 0 steps of d. Each subsequent term advances by one step of d, so the nth term requires exactly (n - 1) steps.",
                            "socratic_hint": "How many steps of d do you add to get from the 1st term to the nth term?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Find the 20th term of the AP whose first term is 7 and common difference is -4.",
                            "ideal_answer": "t_20 = 7 + (20 - 1)(-4) = 7 + 19(-4) = 7 - 76 = -69.",
                            "socratic_hint": "Use t_20 = a + 19d."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "If the 7th term of an AP is 34 and the 13th term is 64, find the common difference d.",
                            "ideal_answer": "t_13 - t_7 = (a + 12d) - (a + 6d) = 6d. 64 - 34 = 30 => 6d = 30 => d = 5.",
                            "socratic_hint": "Subtract t_7 from t_13 to eliminate a."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "How many two-digit numbers are divisible by 3?",
                            "ideal_answer": "First two-digit number divisible by 3 is 12; last is 99. The sequence is 12, 15, 18, ..., 99 (an AP with a = 12, d = 3). Formula: t_n = a + (n - 1)d => 99 = 12 + (n - 1)(3) => 87 = 3(n - 1) => n - 1 = 29 => n = 30 two-digit numbers.",
                            "socratic_hint": "Find the smallest two-digit multiple of 3 and largest, then solve for n."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 3: Arithmetic Series & Gauss Summation
    # -------------------------------------------------------------
    m3_svg = get_svg_wrapper(
        '''
        <rect x="140" y="80" width="300" height="180" fill="rgba(37,99,235,0.06)" stroke="#2563EB" stroke-width="2"/>
        <line x1="140" y1="260" x2="440" y2="80" stroke="#DC2626" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="290" y="115" fill="#2563EB" font-size="14" font-weight="700" text-anchor="middle">Gauss Pairing: S_n = n/2 × [2a + (n-1)d]</text>
        <text x="290" y="150" fill="#0F172A" font-size="12" text-anchor="middle">1 + 2 + 3 + ... + 100 = (100 × 101) / 2 = 5,050</text>
        <text x="290" y="185" fill="#16A34A" font-size="12" text-anchor="middle">Sum of First n Odd Numbers: 1 + 3 + 5 + ... = n²</text>
        <text x="290" y="220" fill="#64748B" font-size="11" text-anchor="middle">Rectangle area n × (a + l) divided by 2</text>
        ''',
        title="Arithmetic Series: Gauss Pairing & Summation Formula",
        caption="Reversing and adding the series pairs each term into a constant sum (a + l)"
    )

    m3 = {
        "order_index": 3,
        "title": "Arithmetic Series: Gauss Summation Formula S_n = n/2 [2a + (n-1)d] & Practical Sums",
        "description": "Formulate the sum of an arithmetic series by reversing and pairing terms (Gauss's discovery). Derive both forms S_n = n/2 [2a + (n-1)d] and S_n = n/2 [a + l]. Deduce the sum of the first n natural numbers and first n odd integers.",
        "subtopics": [
            "Young Carl Friedrich Gauss's famous classroom insight: Sum of 1 to 100 = 5050",
            "Derivation of the general AP sum formula by writing S_n forward and backward",
            "Pairwise summation: 2*S_n = n * (a + l) where l is the last term",
            "First form: S_n = (n/2) * [2a + (n - 1)d]",
            "Second form: S_n = (n/2) * [first term + last term]",
            "Sum of first n natural numbers: Σ n = n(n+1)/2; Sum of first n odd numbers: Σ (2k-1) = n^2"
        ],
        "key_concepts": [
            "Gauss Pairing Invariant: In any AP, the sum of terms equidistant from the beginning and end is constant: t_1 + t_n = t_2 + t_{n-1} = ... = a + l = 2a + (n - 1)d.",
            "Series Sum Invariants: S_n = n/2 * (a + l) = n/2 * [2a + (n - 1)d].",
            "Sum of Natural Numbers: 1 + 2 + 3 + ... + n = n(n + 1) / 2. Direct algebraic equivalent of triangular numbers T_n.",
            "Odd Numbers Square Theorem: 1 + 3 + 5 + ... + (2n - 1) = n/2 * [1 + (2n - 1)] = n/2 * (2n) = n^2. Geometrically corresponds to nested L-shaped gnomons forming concentric squares."
        ],
        "success_criteria": "Derive the Gauss summation formula, compute sums of APs using both formulas, and solve practical series problems.",
        "chapter_notes": "Gauss's proof is one of the most beautiful in school mathematics. Have students write S_n forwards and backwards on their chalkboards to see the identical pairs emerge.",
        "worked_examples": [
            {
                "problem": "Textbook Derivation & Gauss Problem: (i) Find the sum of the first 100 positive integers: 1 + 2 + 3 + ... + 100. (ii) Find the sum of the first 22 terms of the AP: 8, 3, -2, ...",
                "given": "(i) Natural numbers 1 to 100 (a = 1, l = 100, n = 100). (ii) AP: a = 8, d = -5, n = 22.",
                "formula": "S_n = (n / 2) * (a + l) and S_n = (n / 2) * [2a + (n - 1)d].",
                "substitution": "(i) S_100 = (100 / 2) * (1 + 100). (ii) S_22 = (22 / 2) * [2(8) + (22 - 1)(-5)].",
                "calculation": "Part (i):\\nStep 1: Write S forward and backward:\\n  S = 1 + 2 + ... + 99 + 100\\n  S = 100 + 99 + ... + 2 + 1\\nStep 2: Add vertically: 2*S = (1+100) + (2+99) + ... + (100+1) = 100 * 101 = 10,100.\\nStep 3: Divide by 2: S = 10,100 / 2 = 5,050.\\n\\nPart (ii):\\nStep 1: First term a = 8, common difference d = 3 - 8 = -5, number of terms n = 22.\\nStep 2: Substitute into formula:\\n  S_22 = (22 / 2) * [2 * 8 + (22 - 1) * (-5)]\\n  S_22 = 11 * [16 + 21 * (-5)]\\n  S_22 = 11 * [16 - 105]\\n  S_22 = 11 * [-89]\\n  S_22 = -979.",
                "finalAnswer": "(i) Sum of first 100 integers = 5,050; (ii) Sum of first 22 terms = -979",
                "unit": "integers",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m3_svg
            },
            {
                "problem": "Board-Exam Problem: If the sum of the first 14 terms of an AP is 1050 and its first term is 10, find the 20th term.",
                "given": "S_14 = 1050, a = 10, n = 14. Target: t_20.",
                "formula": "S_n = (n / 2) * [2a + (n - 1)d] and t_n = a + (n - 1)d.",
                "substitution": "1050 = (14 / 2) * [2(10) + 13d] => 1050 = 7 * (20 + 13d).",
                "calculation": "Step 1: Solve for d using the sum formula:\\n  1050 = 7 * (20 + 13d)\\n  1050 / 7 = 20 + 13d\\n  150 = 20 + 13d\\n  13d = 150 - 20 = 130\\n  d = 130 / 13 = 10.\\nStep 2: Now compute the 20th term t_20:\\n  t_20 = a + (20 - 1)d\\n  t_20 = 10 + 19 * 10\\n  t_20 = 10 + 190 = 200.",
                "finalAnswer": "Common difference d = 10; 20th term = 200",
                "unit": "integers",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Confusing S_n (the sum of the first n terms) with t_n (the nth term alone).",
            "Dropping the negative sign when multiplying by negative common differences like 21 * (-5)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Tell the story of 10-year-old Carl Friedrich Gauss startling his teacher by calculating 1+2+...+100 in seconds. Write the 100 pairs of 101 on the chalkboard. Call write_chalkboard(action='draw_svg_diagram', content='Gauss Summation Formula').",
        "visual_lesson_plan": {
            "title": "Gauss Summation & Series",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Gauss rectangle pairing diagram.",
            "concept_visuals": [
                {
                    "concept_title": "Gauss Pairing Method",
                    "diagram_title": "Gauss Summation Diagram",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m3_svg,
                    "interactive_math_formula": "S_n = (n/2)*(a + l)",
                    "mafs_graph_config": {"domain": [0, 10], "range": [0, 10]},
                    "image_query": "Carl Friedrich Gauss 1 to 100 sum visual pairing proof",
                    "video_query": "Gauss formula for sum of arithmetic series visual proof",
                    "image_url": "/images/curriculum/ch8_gauss_sum.png",
                    "what_to_make": "Diagram showing forward and reversed series pairing.",
                    "what_to_explain": "Walk through 2*S_n = n * (a + l).",
                    "timing_and_cue": "Show during Gauss derivation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Arithmetic Series",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the sum of the first 10 odd positive integers?",
                            "ideal_answer": "100, because 1 + 3 + 5 + ... + 19 = 10^2 = 100.",
                            "socratic_hint": "Recall the formula for the sum of the first n odd numbers: n^2."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "How can you find the nth term t_n if the sum formula S_n is known?",
                            "ideal_answer": "t_n = S_n - S_{n-1} (for n >= 2), with t_1 = S_1.",
                            "socratic_hint": "Subtract the sum of the first (n-1) terms from the sum of the first n terms."
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Find the sum of all natural numbers from 1 to 50.",
                            "ideal_answer": "S_50 = 50 * 51 / 2 = 25 * 51 = 1,275.",
                            "socratic_hint": "Use n(n+1)/2 with n = 50."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "An AP has first term 5, last term 45, and sum 400. Find the number of terms n.",
                            "ideal_answer": "S_n = (n/2)*(a + l) => 400 = (n/2)*(5 + 45) => 400 = 25n => n = 16.",
                            "socratic_hint": "Use S_n = (n/2)(a + l) with a = 5 and l = 45."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Find the sum of all multiples of 7 lying strictly between 100 and 300.",
                            "ideal_answer": "First multiple above 100 is 105 (7*15); last below 300 is 294 (7*42). The AP is 105, 112, ..., 294 (a = 105, d = 7, l = 294). Find n: 294 = 105 + (n-1)(7) => 189 = 7(n-1) => n-1 = 27 => n = 28. S_28 = (28/2)*(105 + 294) = 14 * 399 = 5,586.",
                            "socratic_hint": "Find the first and last multiples of 7, determine n, and apply S_n = (n/2)(a + l)."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 4: Geometric Progressions (GP) & Fractals
    # -------------------------------------------------------------
    m4_svg = build_sierpinski_triangle_svg(
        title="Sierpiński Triangle Fractal: Geometric Progression",
        caption="Stage 0: 1 triangle (Area A₀). Stage n: 3ⁿ triangles, Total Black Area = (3/4)ⁿ A₀ → 0"
    )

    m4 = {
        "order_index": 4,
        "title": "Geometric Progressions (GP): Common Ratio, Exponential Growth & The Sierpiński Fractal",
        "description": "Explore geometric progressions where each term is multiplied by a constant ratio r. Formulate the general term t_n = a * r^{n-1}. Model bouncing ball damping curves and the self-similar Sierpiński triangle fractal.",
        "subtopics": [
            "Formal definition of a GP: t_{n+1} / t_n = r (constant common ratio)",
            "Exponential vs linear growth: Comparing AP common difference with GP ratio",
            "General term formula: t_n = a * r^{n-1}",
            "Fractional and negative common ratios: Oscillating and decaying sequences",
            "Bouncing ball damping model: Successive heights h_n = h_0 * r^n",
            "Fun with Fractals (Section 8.6.1): The Sierpiński Triangle Area GP"
        ],
        "key_concepts": [
            "Common Ratio Invariant: In a GP, the quotient of any term by its predecessor is constant: r = t_{k+1} / t_k.",
            "GP General Term Formula: t_n = a * r^{n-1}. Growth is exponential because the variable n appears in the exponent.",
            "Bouncing Ball Exponential Decay: A ball dropped from height h_0 that rebounds to a fraction r of its previous height reaches height h_n = h_0 * r^n on the nth bounce.",
            "Sierpiński Triangle Fractal Invariants: At stage n, the number of solid triangles is 3^n (a GP with ratio 3), the area of each triangle is (1/4)^n A_0 (a GP with ratio 1/4), and the total shaded area is (3/4)^n A_0 (a decaying GP with ratio 3/4 approaching 0 as n -> infty)."
        ],
        "success_criteria": "Verify if sequences are GPs, compute general terms with fractional/negative ratios, and calculate fractal properties.",
        "chapter_notes": "Fractals in Section 8.6.1 demonstrate the beauty of math. Show how removing the central upside-down triangle creates 3 smaller copies, leading directly to the (3/4)^n area progression.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 8.3 Q1 & Q2: (Q1) Find the 12th term of a GP with common ratio 2 whose 8th term is 192. (Q2) Find the 10th and nth terms of the GP: 5, 25, 125, ...",
                "given": "Q1: r = 2, t_8 = 192. Target: t_12. Q2: GP 5, 25, 125... (a = 5, r = 5).",
                "formula": "t_n = a * r^{n-1}. Notice: t_12 = t_8 * r^(12 - 8) = t_8 * r^4.",
                "substitution": "Q1: t_12 = 192 * 2^4. Q2: a = 5, r = 5 => t_n = 5 * 5^{n-1} = 5^n.",
                "calculation": "Part (Q1):\\nStep 1: Relate t_12 directly to t_8 using the common ratio:\\n  t_8 = a * r^7 = 192\\n  t_12 = a * r^11 = (a * r^7) * r^4 = t_8 * r^4.\\nStep 2: Substitute values:\\n  t_12 = 192 * 2^4 = 192 * 16.\\nStep 3: Perform multiplication:\\n  192 * 16 = 192 * (10 + 6) = 1920 + 1152 = 3,072.\\n\\nPart (Q2):\\nStep 1: First term a = 5, common ratio r = 25 / 5 = 5.\\nStep 2: General term:\\n  t_n = a * r^{n-1} = 5 * 5^{n-1} = 5^{1 + n - 1} = 5^n.\\nStep 3: 10th term:\\n  t_10 = 5^10 = (5^2)^5 = 25^5 = 9,765,625.",
                "finalAnswer": "Q1: 12th term = 3,072; Q2: t_n = 5^n and t_10 = 9,765,625",
                "unit": "integers and exponential powers",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m4_svg
            },
            {
                "problem": "Textbook Section 8.6.1 Fractal Problem: In the Sierpiński triangle, stage 0 is an equilateral triangle of area 64 cm^2. At each stage, the central inverted triangle is removed. Find: (i) the total remaining shaded area at Stage 1, Stage 2, and Stage 3, (ii) the formula for the shaded area at Stage n.",
                "given": "Stage 0 Area A_0 = 64 cm^2. At each stage, 1/4 of each triangle is removed, leaving 3/4 of the area.",
                "formula": "Shaded Area at Stage n: A_n = A_0 * (3/4)^n.",
                "substitution": "A_0 = 64. A_1 = 64*(3/4); A_2 = 64*(3/4)^2; A_3 = 64*(3/4)^3.",
                "calculation": "Step 1: Stage 1 (n = 1):\\n  A_1 = 64 * (3/4) = 16 * 3 = 48 cm^2.\\nStep 2: Stage 2 (n = 2):\\n  A_2 = 64 * (9/16) = 4 * 9 = 36 cm^2.\\nStep 3: Stage 3 (n = 3):\\n  A_3 = 64 * (27/64) = 27 cm^2.\\nStep 4: Stage n general formula:\\n  A_n = 64 * (3/4)^n cm^2.\\n  As n approaches infinity, (3/4)^n approaches 0, meaning the Sierpiński triangle has ZERO area but INFINITE perimeter!",
                "finalAnswer": "Stage 1 = 48 cm^2; Stage 2 = 36 cm^2; Stage 3 = 27 cm^2; Formula A_n = 64 * (3/4)^n cm^2",
                "unit": "square centimetres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Writing the GP general term as a * r^n instead of a * r^{n-1}.",
            "Assuming fractal area increases because the number of triangles grows from 1 to 3 to 9 to 27 (the total area DECREASES because each triangle shrinks faster than the count grows)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Draw the Sierpiński triangle on the chalkboard. Point out that while the count of triangles multiplies by 3, the area multiplies by 3/4. Call write_chalkboard(action='draw_svg_diagram', content='Sierpinski Triangle Fractal').",
        "visual_lesson_plan": {
            "title": "Geometric Progressions & Fractals",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Sierpiński triangle fractal with 3-level recursive nesting.",
            "concept_visuals": [
                {
                    "concept_title": "Fractal Self-Similarity",
                    "diagram_title": "Sierpiński Triangle",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m4_svg,
                    "interactive_math_formula": "A_n = A_0 * (3/4)^n",
                    "mafs_graph_config": {"domain": [-1, 10], "range": [-1, 10]},
                    "image_query": "Sierpinski triangle fractal geometric progression visual math",
                    "video_query": "Sierpinski triangle fractal and geometric progression explained",
                    "image_url": "/images/curriculum/ch8_sierpinski.png",
                    "what_to_make": "Fractal triangle showing stages 0, 1, 2, 3.",
                    "what_to_explain": "Walk through triangle count (3^n) vs area ((3/4)^n).",
                    "timing_and_cue": "Show during fractal discussion."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Geometric Progressions & Fractals",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the common ratio r of the GP: 4, 8/3, 16/9, 32/27, ...?",
                            "ideal_answer": "2/3, because (8/3) / 4 = 8/12 = 2/3.",
                            "socratic_hint": "Divide the second term by the first term."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What happens to the total shaded area of a Sierpiński triangle as the stage number n approaches infinity?",
                            "ideal_answer": "It approaches 0, because the common ratio of the area GP is 3/4 < 1, and (3/4)^n -> 0.",
                            "socratic_hint": "What is the limit of (3/4)^n as n becomes arbitrarily large?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "A ball is dropped from a height of 10 metres. On each bounce, it rebounds to 80% of its previous height. What height does it reach on the 3rd bounce?",
                            "ideal_answer": "h_3 = 10 * (0.8)^3 = 10 * 0.512 = 5.12 metres.",
                            "socratic_hint": "Calculate 10 * (0.8)^3."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Find the 6th term of the GP: 2, -6, 18, -54, ...",
                            "ideal_answer": "a = 2, r = -3. t_6 = 2 * (-3)^5 = 2 * (-243) = -486.",
                            "socratic_hint": "Use t_6 = a * r^5 with r = -3."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "If the 4th, 10th, and 16th terms of a GP are x, y, and z respectively, prove that x, y, z are in GP (i.e. y^2 = xz).",
                            "ideal_answer": "Let the GP have first term a and common ratio r. Then x = t_4 = a*r^3, y = t_10 = a*r^9, z = t_16 = a*r^15. Compute y^2: y^2 = (a*r^9)^2 = a^2 * r^18. Compute x*z: x*z = (a*r^3) * (a*r^15) = a^2 * r^18. Since y^2 = x*z, x, y, z are in GP.",
                            "socratic_hint": "Express x, y, z in terms of a and r and verify that y^2 equals xz."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 5: Textbook Exercise Solver 1: Ex 8.1 & 8.2
    # -------------------------------------------------------------
    m5_svg = build_cartesian_svg(
        domain=(0, 6), range_y=(0, 25),
        points=[
            {"x": 1, "y": 2, "label": "t₁ = 2", "color": "#16A34A"},
            {"x": 2, "y": 7, "label": "t₂ = 7", "color": "#16A34A"},
            {"x": 3, "y": 12, "label": "t₃ = 12", "color": "#16A34A"},
            {"x": 4, "y": 17, "label": "t₄ = 17", "color": "#16A34A"},
            {"x": 5, "y": 22, "label": "t₅ = 22", "color": "#16A34A"}
        ],
        lines=[
            {"p1": (0, -3), "p2": (6, 27), "color": "#16A34A", "stroke_width": 2, "label": "t_n = 5n - 3"}
        ],
        title="Exercise Solver 1: AP Calculations & Linear Plots",
        caption="Full step-by-step solutions for Exercises 8.1 and 8.2 with zero skipped steps"
    )

    m5 = {
        "order_index": 5,
        "title": "Textbook Exercise Solver 1: Exercises 8.1 & 8.2 (AP nth Terms & Linear Plots)",
        "description": "Complete solutions for every problem in Exercise 8.1 (generating sequences, explicit vs recursive rules) and Exercise 8.2 (AP verification, common differences, finding distant terms, and zero testing) with zero skipped steps.",
        "subtopics": [
            "Exercise 8.1 Q1: Generating terms for linear and quadratic sequence formulas",
            "Exercise 8.1 Q2: Computing t_10 and t_15 for t_n = 5n - 3",
            "Exercise 8.1 Q3: Finding recursive rules for given numerical sequences",
            "Exercise 8.2 Q1: Calculating 10th and 26th terms of AP 3, 8, 13, 18...",
            "Exercise 8.2 Q2: Negative term and zero membership testing in AP 21, 18, 15...",
            "Exercise 8.2 Q3: Fractional APs and recursive rule formulations"
        ],
        "key_concepts": [
            "Sequential Verification Protocol: To prove a sequence is an AP, compute t_{k+1} - t_k for at least three consecutive pairs. If and only if the difference is identical, it is an AP.",
            "Index Integer Condition: A number M is a term of the AP t_n = a + (n - 1)d if and only if n = (M - a)/d + 1 is a positive natural number {1, 2, 3...}.",
            "Recursive Rule Mapping: For any AP with first term a and common difference d, the recursive rule is always: t_1 = a, t_{n+1} = t_n + d."
        ],
        "success_criteria": "Solve every question in Exercises 8.1 and 8.2 with 100% precision and complete working.",
        "chapter_notes": "Make students verify the common difference across at least 3 consecutive terms before declaring a sequence is an AP.",
        "worked_examples": [
            {
                "problem": "Exercise 8.1 Q2: Find the 10th and 15th terms of the sequence whose nth term is given by t_n = 5n - 3 for n >= 1. Also write the recursive rule for this sequence.",
                "given": "Explicit rule: t_n = 5n - 3.",
                "formula": "t_n = 5n - 3. First term a = t_1. Recursive rule: t_{n+1} = t_n + d.",
                "substitution": "t_10 = 5(10) - 3; t_15 = 5(15) - 3.",
                "calculation": "Step 1: Compute 10th term:\\n  t_10 = 5 * 10 - 3 = 50 - 3 = 47.\\nStep 2: Compute 15th term:\\n  t_15 = 5 * 15 - 3 = 75 - 3 = 72.\\nStep 3: Determine the first term and common difference:\\n  t_1 = 5(1) - 3 = 2\\n  t_2 = 5(2) - 3 = 7\\n  Common difference d = 7 - 2 = 5.\\nStep 4: Formulate recursive rule:\\n  Base case: t_1 = 2\\n  Inductive step: t_{n+1} = t_n + 5 for n >= 1.",
                "finalAnswer": "t_10 = 47, t_15 = 72; Recursive rule: t_1 = 2, t_{n+1} = t_n + 5",
                "unit": "integers and recursive rule",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m5_svg
            },
            {
                "problem": "Exercise 8.2 Q3: Find the nth term of the AP: 11, 8, 5, 2, ... and write down its recursive rule.",
                "given": "Sequence: 11, 8, 5, 2, ...",
                "formula": "First term a = 11, d = t_2 - t_1. General term t_n = a + (n - 1)d.",
                "substitution": "a = 11, d = 8 - 11 = -3. t_n = 11 + (n - 1)(-3).",
                "calculation": "Step 1: Find common difference:\\n  d = 8 - 11 = -3.\\n  Verify: 5 - 8 = -3; 2 - 5 = -3. (Constant difference -3 confirmed!)\\nStep 2: Apply general term formula:\\n  t_n = a + (n - 1)d\\n  t_n = 11 + (n - 1)(-3)\\n  t_n = 11 - 3n + 3\\n  t_n = 14 - 3n.\\nStep 3: Write recursive rule:\\n  Initial condition: t_1 = 11\\n  Recursive step: t_{n+1} = t_n - 3 for n >= 1.",
                "finalAnswer": "General term: t_n = 14 - 3n; Recursive rule: t_1 = 11, t_{n+1} = t_n - 3",
                "unit": "algebraic rule",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Expanding 11 + (n - 1)(-3) as 11 - 3n - 3 instead of + 3 (negative times negative is positive: -1 * -3 = +3).",
            "Leaving out the base condition t_1 = 11 when specifying a recursive rule."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Remind students that a recursive rule is completely useless without its starting term t_1. You cannot climb a ladder without stepping on the first rung! Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 1: AP Rules').",
        "visual_lesson_plan": {
            "title": "Exercise Solver 1 Solutions",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Line plot for t_n = 5n - 3 showing points (1, 2) to (5, 22).",
            "concept_visuals": [
                {
                    "concept_title": "Linear Discrete Plots",
                    "diagram_title": "t_n = 5n - 3 Graph",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m5_svg,
                    "interactive_math_formula": "t_n = 5n - 3",
                    "mafs_graph_config": {"domain": [0, 8], "range": [0, 25], "lines": [{"formula": "5*x - 3"}]},
                    "image_query": "Arithmetic progression points line plot cartesian plane math",
                    "video_query": "How to graph an arithmetic progression on coordinate axes",
                    "image_url": "/images/curriculum/ch8_solver1_graph.png",
                    "what_to_make": "Coordinate graph showing discrete points on a line.",
                    "what_to_explain": "Explain that an AP only exists at integer points n = 1, 2, 3...",
                    "timing_and_cue": "Show during graphing explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Exercise Solver 1 Mastery",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the 50th term of the AP with general term t_n = 4n + 1?",
                            "ideal_answer": "201, because 4(50) + 1 = 200 + 1 = 201.",
                            "socratic_hint": "Substitute n = 50 into the formula."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why is a base condition like t_1 = 2 strictly required in a recursive rule?",
                            "ideal_answer": "Without a base condition, the recurrence relation cannot be initialized to compute any actual numerical values.",
                            "socratic_hint": "Where do you start if you only know t_{n+1} = t_n + 5?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "Find the general term t_n of the AP: 1/2, 5/2, 9/2, 13/2, ...",
                            "ideal_answer": "a = 1/2, d = 5/2 - 1/2 = 4/2 = 2. t_n = 1/2 + (n - 1)*2 = 2n - 3/2 (or (4n - 3)/2).",
                            "socratic_hint": "Find the difference between consecutive fractions."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Which term of the AP 5, 8, 11, 14, ... is 320?",
                            "ideal_answer": "a = 5, d = 3. 5 + (n-1)*3 = 320 => 3(n-1) = 315 => n-1 = 105 => n = 106.",
                            "socratic_hint": "Set t_n = 320 and solve for n."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Find the 11th term from the last term (towards the first term) of the AP: 10, 7, 4, ..., -62.",
                            "ideal_answer": "Reversing the AP from the end: first term a = -62, common difference d = +3 (since forward d = -3, backward d = +3). The 11th term from the end is: t'_11 = a + 10d = -62 + 10(3) = -62 + 30 = -32.",
                            "socratic_hint": "Reverse the AP so that -62 becomes the first term and d changes sign."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 6: Textbook Exercise Solver 2: Ex 8.3 & Review
    # -------------------------------------------------------------
    m6_svg = build_bouncing_ball_decay_svg(
        title="Exercise Solver 2: GP Decays & End-of-Chapter Review",
        caption="Full step-by-step solutions for Exercise 8.3 and End-of-Chapter Q1 through Q10"
    )

    m6 = {
        "order_index": 6,
        "title": "Textbook Exercise Solver 2: Exercise 8.3 & End-of-Chapter Review (Complete Solutions)",
        "description": "Comprehensive step-by-step solutions for Exercise 8.3 (geometric progressions, recursive nonlinear rules) and End-of-Chapter synthesis questions Q1 through Q10 (linear system AP determinations, bouncing balls, and series) with zero skipped steps.",
        "subtopics": [
            "Exercise 8.3 Q3: Recursive nonlinear sequence t_1 = 2, t_{n+1} = 3t_n - 2",
            "End-of-Chapter Q1: Finding 31st term of AP with given 11th and 16th terms",
            "End-of-Chapter Q2: Determining AP when t_3 = 16 and t_7 exceeds t_5 by 12",
            "End-of-Chapter Q3 & Q4: Sum of first n terms in applications",
            "End-of-Chapter Q5 to Q8: Geometric damping and exponential decay problems",
            "End-of-Chapter Q9 & Q10: Comprehensive review of sequence convergence and series"
        ],
        "key_concepts": [
            "Linear System Method for AP: Given two terms t_p and t_q, form two linear equations in a and d: a + (p-1)d = t_p and a + (q-1)d = t_q. Subtract to eliminate a and find d = (t_q - t_p) / (q - p).",
            "Term Exceeding Invariant: The statement 'the 7th term exceeds the 5th term by 12' translates directly to: t_7 - t_5 = 12 => [a + 6d] - [a + 4d] = 12 => 2d = 12 => d = 6.",
            "Nonlinear Recurrence Trajectory: The rule t_{n+1} = 3t_n - 2 with t_1 = 2 yields: t_2 = 3(2) - 2 = 4, t_3 = 3(4) - 2 = 10, t_4 = 3(10) - 2 = 28. Notice differences are powers of 3: 2, 6, 18..."
        ],
        "success_criteria": "Solve simultaneous linear equations for AP parameters, evaluate nonlinear recurrences, and complete all end-of-chapter synthesis problems.",
        "chapter_notes": "End-of-Chapter Q1 and Q2 are the absolute classic CBSE board exam questions. Make sure students master the elimination of a by subtracting equations.",
        "worked_examples": [
            {
                "problem": "End-of-Chapter Q1: Find the 31st term of an AP whose 11th term is 38 and 16th term is 73.",
                "given": "11th term: t_11 = 38. 16th term: t_16 = 73.",
                "formula": "t_n = a + (n - 1)d. Set up two simultaneous linear equations.",
                "substitution": "t_11 = a + 10d = 38 ... (Eq 1). t_16 = a + 15d = 73 ... (Eq 2).",
                "calculation": "Step 1: Write the two equations:\\n  a + 10d = 38 ... (Equation 1)\\n  a + 15d = 73 ... (Equation 2)\\nStep 2: Subtract Equation 1 from Equation 2:\\n  (a + 15d) - (a + 10d) = 73 - 38\\n  5d = 35\\n  d = 35 / 5 = 7.\\nStep 3: Substitute d = 7 into Equation 1 to find a:\\n  a + 10(7) = 38\\n  a + 70 = 38\\n  a = 38 - 70 = -32.\\nStep 4: Compute the 31st term t_31:\\n  t_31 = a + (31 - 1)d\\n  t_31 = -32 + 30 * (7)\\n  t_31 = -32 + 210 = 178.",
                "finalAnswer": "First term a = -32, Common difference d = 7; 31st term = 178",
                "unit": "integers",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m6_svg
            },
            {
                "problem": "End-of-Chapter Q2: Determine the AP whose third term is 16 and whose 7th term exceeds the 5th term by 12.",
                "given": "t_3 = 16. Difference condition: t_7 - t_5 = 12.",
                "formula": "t_n = a + (n - 1)d.",
                "substitution": "t_3 = a + 2d = 16. t_7 - t_5 = (a + 6d) - (a + 4d) = 2d = 12.",
                "calculation": "Step 1: Analyze the difference condition:\\n  t_7 - t_5 = 12\\n  [a + 6d] - [a + 4d] = 12\\n  2d = 12\\n  d = 12 / 2 = 6.\\nStep 2: Use the third term equation to find a:\\n  a + 2d = 16\\n  a + 2(6) = 16\\n  a + 12 = 16\\n  a = 16 - 12 = 4.\\nStep 3: Construct the AP sequence:\\n  t_1 = a = 4\\n  t_2 = a + d = 4 + 6 = 10\\n  t_3 = a + 2d = 4 + 12 = 16\\n  t_4 = a + 3d = 4 + 18 = 22\\n  AP: 4, 10, 16, 22, 28, ...",
                "finalAnswer": "The AP is: 4, 10, 16, 22, 28, ... (with a = 4 and d = 6)",
                "unit": "arithmetic progression sequence",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting to subtract 70 from 38 properly in End-of-Chapter Q1, writing a = +32 instead of a = -32.",
            "Translating 't_7 exceeds t_5 by 12' as t_7 + t_5 = 12 instead of subtraction t_7 - t_5 = 12."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Teach elimination of 'a' as standard procedure for AP problems. When you subtract two term formulas, 'a' cancels out every single time, leaving only d. Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 2: GP & Review').",
        "visual_lesson_plan": {
            "title": "Exercise Solver 2 Solutions",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Bouncing ball exponential decay curve.",
            "concept_visuals": [
                {
                    "concept_title": "Exponential Damping",
                    "diagram_title": "Bouncing Ball Damping Curve",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m6_svg,
                    "interactive_math_formula": "h_n = h_0 * r^n",
                    "mafs_graph_config": {"domain": [0, 8], "range": [0, 12]},
                    "image_query": "Bouncing ball damping height exponential decay geometric progression",
                    "video_query": "Bouncing ball physics geometric sequence exponential decay",
                    "image_url": "/images/curriculum/ch8_bouncing_ball.png",
                    "what_to_make": "Decaying parabola curves representing ball bounces.",
                    "what_to_explain": "Walk through successive height ratios: h_n = h_0 * (0.8)^n.",
                    "timing_and_cue": "Show during damping explanation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Exercise Solver 2 Mastery",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "In an AP, if t_10 - t_6 = 16, what is the common difference d?",
                            "ideal_answer": "4, because (a + 9d) - (a + 5d) = 4d = 16 => d = 4.",
                            "socratic_hint": "Express t_10 - t_6 in terms of d."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why does subtracting any two AP term equations always eliminate the first term a?",
                            "ideal_answer": "Because every term formula t_k = a + (k-1)d contains the exact same leading term '+a' with coefficient 1, which cancels out upon subtraction.",
                            "socratic_hint": "What is the coefficient of a in all AP terms?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "An AP has first term 2 and 5th term 14. Find the sum of its first 5 terms.",
                            "ideal_answer": "S_5 = (5 / 2) * (t_1 + t_5) = (5 / 2) * (2 + 14) = (5 / 2) * 16 = 40.",
                            "socratic_hint": "Use S_n = (n/2)(first + last)."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "If 7 times the 7th term of an AP is equal to 11 times its 11th term, show that its 18th term is zero.",
                            "ideal_answer": "7*(a + 6d) = 11*(a + 10d) => 7a + 42d = 11a + 110d => 4a + 68d = 0 => 4*(a + 17d) = 0 => a + 17d = 0 => t_18 = 0.",
                            "socratic_hint": "Expand 7(a+6d) = 11(a+10d) and factor out 4."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Determine whether the sequence given by t_1 = 2, t_{n+1} = 3t_n - 2 is an AP, a GP, or neither.",
                            "ideal_answer": "Compute terms: t_1 = 2. t_2 = 3(2) - 2 = 4. t_3 = 3(4) - 2 = 10. t_4 = 3(10) - 2 = 28. Check AP: 4 - 2 = 2, but 10 - 4 = 6 (not constant, not an AP). Check GP: 4/2 = 2, but 10/4 = 2.5 (not constant, not a GP). Therefore, it is NEITHER an AP nor a GP (it is an arithmetic-geometric recurrence).",
                            "socratic_hint": "Check if consecutive differences are constant (AP) or consecutive ratios are constant (GP)."
                        }
                    ]
                }
            ]
        }
    }

    return [m1, m2, m3, m4, m5, m6]
