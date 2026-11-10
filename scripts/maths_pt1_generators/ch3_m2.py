"""
Chapter 3: The World of Numbers - Module 2
Curriculum ID: 09ca99d2-0489-48f2-8d39-8b26ca7885c9
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_number_line_points_svg

def get_m2():
    m2_svg = build_number_line_points_svg(
        points=[
            {"val": 0, "label": "0", "color": "#0F172A"},
            {"val": 0.4, "label": "2/5", "color": "#2563EB"},
            {"val": 0.7, "label": "7/10 (Sum)", "color": "#16A34A"},
            {"val": 1.0, "label": "1", "color": "#0F172A"}
        ],
        domain=(-0.2, 1.2),
        title="Rational Number Addition: 2/5 + 3/10 = 7/10",
        caption="Partitioning the unit interval into tenths to find the common denominator sum"
    )

    return {
        "order_index": 2,
        "title": "Textbook Exercise Solver 1: Rational Numbers, Equivalence & Fundamental Operations (Exercise 3.3 Complete)",
        "description": "Exhaustive step-by-step solutions to every sub-part of Exercise 3.3. Master equivalence proofs using cross-multiplication, common denominator addition and subtraction of signed fractions, and rational multiplication and reciprocal division.",
        "subtopics": [
            "Formal definition of Rational Numbers Q = {p/q : p, q in Z, q != 0}",
            "Equivalence criterion: a/b = c/d if and only if a*d = b*c",
            "Signed fraction addition and subtraction via Least Common Denominator (LCM)",
            "Area interpretation of fraction multiplication: (a/b) * (c/d) = (ac)/(bd)",
            "Fraction division via multiplicative inverse: (a/b) / (c/d) = (a/b) * (d/c)"
        ],
        "key_concepts": [
            "Rational Number Definition: Any number expressible in form p/q with integers p and q (q != 0).",
            "Cross-Product Invariant: Two fractions a/b and c/d represent the exact same point on the number line iff ad - bc = 0.",
            "LCM Addition Rule: To add a/b + c/d, scale each fraction to denominator L = lcm(b, d).",
            "Negative Fraction Placement: -p/q = (-p)/q = p/(-q).",
            "Division by Inversion: Dividing by a fraction is strictly equivalent to multiplying by its reciprocal."
        ],
        "success_criteria": "Students can prove fraction equivalence, compute sums, differences, products, and quotients of positive and negative fractions with step-by-step simplification.",
        "chapter_notes": "Exercise 3.3 contains 15 distinct arithmetic verification and calculation exercises covering the algebraic foundations of rational arithmetic.",
        "common_misconceptions": [
            {"misconception": "Adding denominators together: a/b + c/d = (a+c)/(b+d)", "clarification": "Denominators define the unit partition size; fractions cannot be added until they share a common partition (LCM)."},
            {"misconception": "Inverting the first fraction in division", "clarification": "Only the divisor (the second fraction) is inverted: (a/b) / (c/d) = (a/b) * (d/c)."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through Exercise 3.3. Show every LCM calculation and cross-multiplication step without skipping arithmetic.",
        "visual_lesson_plan": {
            "title": "Visualizing Rational Equivalence and Arithmetic",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Interactive coordinate number line illustrating common-denominator addition: 2/5 + 3/10 = 7/10.",
            "concept_visuals": [
                {
                    "concept_title": "Rational Equivalence: Cross-Multiplication Geometry",
                    "diagram_title": "Equivalent Ratios 2/3 = 4/6",
                    "interactive_math_formula": "2 \\times 6 = 3 \\times 4 = 12",
                    "mafs_graph_config": {
                        "domain": [0, 1.2],
                        "range": [-1, 2],
                        "lines": [
                            {"slope": 0, "intercept": 0, "color": "#64748B", "label": "Number Axis"}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "0"},
                            {"x": 0.667, "y": 0, "label": "2/3 = 4/6"},
                            {"x": 1.0, "y": 0, "label": "1"}
                        ]
                    },
                    "image_query": "equivalent fractions number line partition equal points",
                    "video_query": "why cross multiplication works equivalent fractions",
                    "what_to_explain": "2/3 and 4/6 occupy the exact same coordinate on the number line because 2*6 = 3*4."
                },
                {
                    "concept_title": "Fraction Addition via Tenths Partition: 2/5 + 3/10",
                    "diagram_title": "Common Denominator: 4/10 + 3/10 = 7/10",
                    "interactive_math_formula": "\\frac{2}{5} + \\frac{3}{10} = \\frac{4+3}{10} = \\frac{7}{10}",
                    "mafs_graph_config": {
                        "domain": [0, 1],
                        "range": [-1, 1],
                        "points": [
                            {"x": 0.4, "y": 0, "label": "4/10 (2/5)"},
                            {"x": 0.7, "y": 0, "label": "7/10 (Sum)"},
                            {"x": 1.0, "y": 0, "label": "10/10 (1)"}
                        ]
                    },
                    "image_query": "adding fractions common denominator visual number line",
                    "video_query": "adding fractions with unlike denominators visual model",
                    "what_to_explain": "Converting 2/5 into 4/10 allows direct addition with 3/10 to reach 7/10."
                },
                {
                    "concept_title": "Negative Fraction Subtraction: -7/9 - (-2/3)",
                    "diagram_title": "-7/9 + 6/9 = -1/9",
                    "interactive_math_formula": "-\\frac{7}{9} - \\left(-\\frac{2}{3}\\right) = -\\frac{1}{9}",
                    "mafs_graph_config": {
                        "domain": [-1, 0.2],
                        "range": [-1, 1],
                        "points": [
                            {"x": -0.778, "y": 0, "label": "-7/9"},
                            {"x": -0.111, "y": 0, "label": "-1/9 (Result)"},
                            {"x": 0, "y": 0, "label": "0"}
                        ]
                    },
                    "image_query": "subtracting negative fraction on number line vector jump",
                    "video_query": "subtracting negative rational numbers step by step",
                    "what_to_explain": "Subtracting -2/3 equals adding +6/9, shifting rightward from -7/9 to -1/9."
                },
                {
                    "concept_title": "Fraction Multiplication as Rectangular Area",
                    "diagram_title": "Area of (2/3) by (3/10) Rectangle = 1/5",
                    "interactive_math_formula": "\\frac{2}{3} \\times \\frac{3}{10} = \\frac{6}{30} = \\frac{1}{5}",
                    "mafs_graph_config": {
                        "domain": [0, 1],
                        "range": [0, 1],
                        "points": [
                            {"x": 0, "y": 0, "label": "(0, 0)"},
                            {"x": 0.667, "y": 0, "label": "Width 2/3"},
                            {"x": 0.667, "y": 0.3, "label": "Corner (2/3, 3/10)"},
                            {"x": 0, "y": 0.3, "label": "Height 3/10"}
                        ]
                    },
                    "image_query": "multiplying fractions area model grid rectangle",
                    "video_query": "fraction multiplication visual area model",
                    "what_to_explain": "The product (2/3)*(3/10) represents the area of a rectangle with sides 2/3 and 3/10, yielding 6/30 = 1/5."
                },
                {
                    "concept_title": "Fraction Division: Reciprocal Multiplication",
                    "diagram_title": "(2/3) / (3/10) = 20/9 = 2.222...",
                    "interactive_math_formula": "\\frac{2}{3} \\div \\frac{3}{10} = \\frac{2}{3} \\times \\frac{10}{3} = \\frac{20}{9}",
                    "mafs_graph_config": {
                        "domain": [0, 3],
                        "range": [-1, 1],
                        "points": [
                            {"x": 0.667, "y": 0, "label": "Dividend 2/3"},
                            {"x": 2.222, "y": 0, "label": "Quotient 20/9 (2.22)"}
                        ]
                    },
                    "image_query": "dividing fractions visual reciprocal number line",
                    "video_query": "why invert and multiply works dividing fractions",
                    "what_to_explain": "Determines how many groups of 3/10 fit inside 2/3: exactly 20/9 = 2 and 2/9 times."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Fraction Equivalence & Operations",
                    "questions": [
                        {
                            "question": "How do you check whether two fractions a/b and c/d are equal without finding common denominators?",
                            "type": "short_answer",
                            "ideal_answer": "By cross-multiplication: check whether the cross product a*d is equal to b*c.",
                            "socratic_hint": "Multiply numerator of first by denominator of second and compare with denominator of first times numerator of second."
                        },
                        {
                            "question": "Why must the second fraction be inverted when dividing rational numbers?",
                            "type": "short_answer",
                            "ideal_answer": "Because division is the inverse operation of multiplication, so dividing by x is mathematically equivalent to multiplying by its reciprocal 1/x.",
                            "socratic_hint": "Consider that dividing by 2 is the same as multiplying by 1/2."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "Exercise 3.3 Q1 (i): Prove that 2/3 and 4/6 are equal rational numbers.",
                "given": "Rational numbers 2/3 and 4/6.",
                "formula": "Two rational numbers a/b and c/d are equal if and only if a*d = b*c.",
                "substitution": "Here a = 2, b = 3, c = 4, d = 6. Check 2 * 6 and 3 * 4.",
                "calculation": "1. LHS cross product: 2 * 6 = 12.\n2. RHS cross product: 3 * 4 = 12.\n3. Since 12 = 12, the cross products are equal.\n4. Alternatively, simplify 4/6 by dividing numerator and denominator by 2: 4/6 = (4/2)/(6/2) = 2/3.",
                "finalAnswer": "2/3 = 4/6 (Proved by cross-multiplication: 2*6 = 3*4 = 12).",
                "unit": "rational equivalence",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.3 Q1 (ii): Prove that 5/4 and 10/8 are equal rational numbers.",
                "given": "Rational numbers 5/4 and 10/8.",
                "formula": "a/b = c/d <=> a*d = b*c.",
                "substitution": "5 * 8 and 4 * 10.",
                "calculation": "1. 5 * 8 = 40.\n2. 4 * 10 = 40.\n3. Cross products are equal (40 = 40), so 5/4 = 10/8.",
                "finalAnswer": "5/4 = 10/8 (Proved: 5*8 = 4*10 = 40).",
                "unit": "rational equivalence",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q1 (iii): Prove that -3/5 and -6/10 are equal rational numbers.",
                "given": "-3/5 and -6/10.",
                "formula": "(-a)/b = (-c)/d <=> (-a)*d = b*(-c).",
                "substitution": "(-3) * 10 and 5 * (-6).",
                "calculation": "1. (-3) * 10 = -30.\n2. 5 * (-6) = -30.\n3. Both cross products equal -30, confirming equivalence.",
                "finalAnswer": "-3/5 = -6/10 (Proved: (-3)*10 = 5*(-6) = -30).",
                "unit": "rational equivalence",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q1 (iv): Prove that 9/3 and 3 are equal rational numbers.",
                "given": "Rational numbers 9/3 and 3 (written as 3/1).",
                "formula": "a/b = c/d <=> a*d = b*c.",
                "substitution": "9 * 1 and 3 * 3.",
                "calculation": "1. 9 * 1 = 9.\n2. 3 * 3 = 9.\n3. 9 = 9, so 9/3 = 3.",
                "finalAnswer": "9/3 = 3 (Proved: 9*1 = 3*3 = 9).",
                "unit": "rational equivalence",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q2 (i): Find the sum: 2/5 + 3/10.",
                "given": "Fractions: 2/5 and 3/10.",
                "formula": "a/b + c/d = (a*(L/b) + c*(L/d)) / L, where L = lcm(b, d).",
                "substitution": "LCM(5, 10) = 10. Scale 2/5: (2*2)/(5*2) = 4/10.",
                "calculation": "1. 4/10 + 3/10 = (4 + 3) / 10.\n2. (4 + 3) / 10 = 7/10.",
                "finalAnswer": "7/10",
                "unit": "fraction",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.3 Q2 (ii): Find the sum: 7/12 + 5/8.",
                "given": "7/12 + 5/8.",
                "formula": "Find LCM(12, 8).",
                "substitution": "Multiples of 12: 12, 24; Multiples of 8: 8, 16, 24. LCM = 24.",
                "calculation": "1. 7/12 = (7 * 2) / (12 * 2) = 14/24.\n2. 5/8 = (5 * 3) / (8 * 3) = 15/24.\n3. Sum = (14 + 15) / 24 = 29/24 (or 1 5/24).",
                "finalAnswer": "29/24",
                "unit": "fraction",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q2 (iii): Find the sum: -4/7 + 3/14.",
                "given": "-4/7 + 3/14.",
                "formula": "LCM(7, 14) = 14.",
                "substitution": "Scale -4/7 = (-4 * 2) / 14 = -8/14.",
                "calculation": "1. -8/14 + 3/14 = (-8 + 3) / 14.\n2. -5 / 14.",
                "finalAnswer": "-5/14",
                "unit": "fraction",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q3 (i): Find the difference: 5/6 - 1/4.",
                "given": "5/6 - 1/4.",
                "formula": "LCM(6, 4) = 12.",
                "substitution": "5/6 = 10/12; 1/4 = 3/12.",
                "calculation": "1. 10/12 - 3/12 = (10 - 3) / 12.\n2. 7/12.",
                "finalAnswer": "7/12",
                "unit": "fraction",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q3 (ii): Find the difference: 11/8 - 3/4.",
                "given": "11/8 - 3/4.",
                "formula": "LCM(8, 4) = 8.",
                "substitution": "3/4 = (3 * 2) / 8 = 6/8.",
                "calculation": "1. 11/8 - 6/8 = (11 - 6) / 8.\n2. 5/8.",
                "finalAnswer": "5/8",
                "unit": "fraction",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q3 (iii): Find the difference: -7/9 - (-2/3).",
                "given": "-7/9 - (-2/3).",
                "formula": "Subtracting a negative fraction equals adding the positive fraction: -a/b - (-c/d) = -a/b + c/d.",
                "substitution": "-7/9 + 2/3. LCM(9, 3) = 9. Scale 2/3 = 6/9.",
                "calculation": "1. -7/9 + 6/9 = (-7 + 6) / 9.\n2. -1/9.",
                "finalAnswer": "-1/9",
                "unit": "fraction",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.3 Q4 (i): Find the product: (2/3) * (3/10).",
                "given": "(2/3) * (3/10).",
                "formula": "(a/b) * (c/d) = (a * c) / (b * d).",
                "substitution": "(2 * 3) / (3 * 10).",
                "calculation": "1. Numerator: 2 * 3 = 6.\n2. Denominator: 3 * 10 = 30.\n3. Simplify 6/30 by dividing by 6: 1/5.",
                "finalAnswer": "1/5",
                "unit": "fraction",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.3 Q4 (ii): Find the product: (7/11) * (5/8).",
                "given": "(7/11) * (5/8).",
                "formula": "(a/b) * (c/d) = (a * c) / (b * d).",
                "substitution": "(7 * 5) / (11 * 8).",
                "calculation": "1. 7 * 5 = 35.\n2. 11 * 8 = 88.\n3. 35 and 88 share no common factors.",
                "finalAnswer": "35/88",
                "unit": "fraction",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q4 (iii): Find the product: (-4/7) * (5/14).",
                "given": "(-4/7) * (5/14).",
                "formula": "(-a/b) * (c/d) = -(a * c) / (b * d).",
                "substitution": "-(4 * 5) / (7 * 14).",
                "calculation": "1. 4 * 5 = 20.\n2. 7 * 14 = 98.\n3. Simplify -20/98 by dividing by 2: -10/49.",
                "finalAnswer": "-10/49",
                "unit": "fraction",
                "has_diagram": False
            },
            {
                "problem": "Exercise 3.3 Q5 (i): Find the quotient: (2/3) / (3/10).",
                "given": "(2/3) / (3/10).",
                "formula": "(a/b) / (c/d) = (a/b) * (d/c).",
                "substitution": "(2/3) * (10/3).",
                "calculation": "1. Multiply numerators: 2 * 10 = 20.\n2. Multiply denominators: 3 * 3 = 9.\n3. Quotient = 20/9 (or 2 2/9).",
                "finalAnswer": "20/9",
                "unit": "fraction",
                "has_diagram": True
            },
            {
                "problem": "Exercise 3.3 Q5 (ii): Find the quotient: (7/11) / (5/8).",
                "given": "(7/11) / (5/8).",
                "formula": "(a/b) / (c/d) = (a/b) * (d/c).",
                "substitution": "(7/11) * (8/5).",
                "calculation": "1. Numerator: 7 * 8 = 56.\n2. Denominator: 11 * 5 = 55.\n3. Quotient = 56/55 (or 1 1/55).",
                "finalAnswer": "56/55",
                "unit": "fraction",
                "has_diagram": False
            }
        ]
    }
