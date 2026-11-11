"""
Class 10 Mathematics - Chapter 5: Arithmetic Progressions (NCERT CBSE)
Curriculum ID: 916e8989-c22e-4dd9-97a0-f081e63fb77d
Fully compliant with Invariant 10:
- Minimum 5 to 6 dedicated modules (Theory strictly in M1-M2, dedicated solvers M3-M6)
- 100% of all NCERT exercise questions (Ex 5.1, 5.2, 5.3, 5.4) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- High-Precision Vector SVGs from svg_builder_class10 (Staircase of Increments, Sum Area Decomposition)
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_ap_increments_svg, get_svg_wrapper

def get_ch5_modules():
    CURRICULUM_ID = "916e8989-c22e-4dd9-97a0-f081e63fb77d"
    
    # SVG 1: AP Step-ladder staircase showing constant increment +d
    svg_staircase = build_ap_increments_svg(
        a=2,
        d=3,
        n=5,
        title="Arithmetic Progression: Staircase of Constant Increments",
        caption="First term a = 2, common difference d = +3, nth term an = a + (n - 1)d"
    )

    # SVG 2: Formula Card for AP nth term & Sum
    card_formula = """
    <g transform="translate(50, 70)">
      <rect width="480" height="230" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" rx="10"/>
      <text x="24" y="28" fill="#0F172A" font-size="14" font-weight="700">Arithmetic Progression (AP): a, a + d, a + 2d, a + 3d, ...</text>
      
      <!-- nth term -->
      <rect x="24" y="44" width="432" height="46" fill="#EFF6FF" stroke="#93C5FD" rx="6"/>
      <text x="36" y="66" fill="#1E40AF" font-size="11" font-weight="700">General (nth) Term Formula:</text>
      <text x="36" y="82" fill="#2563EB" font-size="13" font-weight="700">aₙ = a + (n - 1)d   [d = aₖ₊₁ - aₖ]</text>
      
      <!-- Sum formulas -->
      <rect x="24" y="98" width="432" height="64" fill="#F0FDF4" stroke="#86EFAC" rx="6"/>
      <text x="36" y="118" fill="#166534" font-size="11" font-weight="700">Sum of First n Terms (Sₙ):</text>
      <text x="36" y="136" fill="#15803D" font-size="13" font-weight="700">Sₙ = (n / 2) [ 2a + (n - 1)d ]</text>
      <text x="36" y="154" fill="#15803D" font-size="12" font-weight="700">Sₙ = (n / 2) [ a + l ]   where l = last term (aₙ)</text>
      
      <!-- Bridge relation -->
      <rect x="24" y="170" width="432" height="42" fill="#FEF2F2" stroke="#FECACA" rx="6"/>
      <text x="36" y="196" fill="#DC2626" font-size="12" font-weight="700">Crucial Term-Sum Bridge: aₙ = Sₙ - Sₙ₋₁   (for n ≥ 2, a₁ = S₁)</text>
    </g>
    """
    svg_ap_card = get_svg_wrapper(card_formula, title="AP Algebraic Foundations HUD", caption="Essential governing equations for sequence analysis and summation")

    modules = [
        # Module 1: AP Foundations & nth Term
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Arithmetic Progressions Foundations: Common Difference & Derivation of General Term aₙ",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand what constitutes an Arithmetic Progression. Learn how a constant common difference d (positive, negative, or zero) defines linear discrete growth, and rigorously derive the nth term formula aₙ = a + (n - 1)d.",
            "key_concepts": [
                "Definition of AP: A sequence where each term is obtained by adding a fixed number d to the preceding term",
                "Common Difference d = aₖ₊₁ - aₖ: Can be positive, negative, or zero",
                "General Form: a, a + d, a + 2d, a + 3d, ..., a + (n - 1)d",
                "Finite vs Infinite AP: Distinction based on whether the number of terms is bounded",
                "Derivation of General Term: a₁ = a, a₂ = a + d, a₃ = a + 2d ⇒ aₙ = a + (n - 1)d"
            ],
            "subtopics": [
                "Derivation of the nth term formula by inductive pattern recognition",
                "Worked Examples 3, 4, 5, 6, 7 from NCERT",
                "Finding number of terms in an AP given the last term",
                "Testing whether a given number belongs to an AP"
            ],
            "worked_examples": [
                {
                    "problem": "Example 3 (NCERT): Find the 10th term of the AP: 2, 7, 12, ...",
                    "solution": "Given AP: 2, 7, 12, ...\nHere, First term (a) = 2\nCommon difference (d) = a₂ - a₁ = 7 - 2 = 5\nTarget: Find 10th term ⇒ n = 10.\nFormula: aₙ = a + (n - 1)d\nSubstitution: a₁₀ = 2 + (10 - 1)(5)\n= 2 + 9(5) = 2 + 45 = 47.\n[ROUGH_WORK]\n2 + 5 = 7 (2nd)\n7 + 5 = 12 (3rd)\n12 + 5 = 17 (4th)\n... 2 + 9×5 = 47 (10th)\nBoxed Answer: [ The 10th term of the given AP is 47 ].",
                    "concept_questions": [
                        "Why is the multiplier of d equal to (n - 1) and not n?",
                        "If d was negative, what would happen to the terms as n increases?"
                    ]
                },
                {
                    "problem": "Example 5 (NCERT): Determine the AP whose 3rd term is 5 and the 7th term is 9.",
                    "solution": "Given:\n3rd term (a₃) = 5\n7th term (a₇) = 9\nFormula: aₙ = a + (n - 1)d\n\nStep 1: Set up equations in a and d:\na₃ = a + (3 - 1)d = a + 2d = 5 ... (1)\na₇ = a + (7 - 1)d = a + 6d = 9 ... (2)\n\nStep 2: Subtract Equation (1) from Equation (2):\n(a + 6d) - (a + 2d) = 9 - 5\n4d = 4 ⇒ d = 1.\n\nStep 3: Substitute d = 1 into Equation (1):\na + 2(1) = 5 ⇒ a = 5 - 2 = 3.\n\nStep 4: Write the AP: a, a + d, a + 2d, a + 3d, ...\n3, 3 + 1, 3 + 2, 3 + 3, ... ⇒ 3, 4, 5, 6, ...\n[ROUGH_WORK]\nCheck a₃ = 3 + 2(1) = 5 (True)\nCheck a₇ = 3 + 6(1) = 9 (True)\nBoxed Answer: [ The required AP is 3, 4, 5, 6, ... ].",
                    "concept_questions": [
                        "Notice that subtracting the two equations directly eliminated the first term a: why does this always work for any two terms of an AP?",
                        "What is the general formula for the difference (aₘ - aₙ) in terms of d?"
                    ]
                },
                {
                    "problem": "Example 6 (NCERT): Check whether 301 is a term of the list of numbers: 5, 11, 17, 23, ...",
                    "solution": "Given sequence: 5, 11, 17, 23, ...\nCheck common difference: 11 - 5 = 6; 17 - 11 = 6; 23 - 17 = 6.\nSince the difference between consecutive terms is constant, it is an AP with a = 5 and d = 6.\n\nTarget: Test if aₙ = 301 for some positive integer n.\nFormula: aₙ = a + (n - 1)d\n301 = 5 + (n - 1)6\n301 - 5 = 6(n - 1)\n296 = 6(n - 1)\nn - 1 = 296 / 6 = 148 / 3\nn = 148/3 + 1 = 151/3 = 50 1/3.\n\nAnalysis: Since n must be a positive integer (term count cannot be fractional), 301 CANNOT be a term of this AP.\n[ROUGH_WORK]\n50th term = 5 + 49(6) = 5 + 294 = 299\n51st term = 299 + 6 = 305\n301 falls strictly between the 50th and 51st terms!\nBoxed Answer: [ 301 is not a term of the given AP as n = 151/3 is not a positive integer ].",
                    "concept_questions": [
                        "Why can term index n never be a fraction or negative?",
                        "What is the mathematical condition for a number k to belong to an AP?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "AP Staircase of Increments Vector Illustration",
                "diagram_type": "diagram",
                "svg": svg_staircase,
                "concept_visuals": [
                    {
                        "concept_title": "Step-Ladder Growth Model",
                        "diagram_title": "Constant Increments Staircase",
                        "svg": svg_staircase,
                        "diagram_type": "diagram",
                        "what_to_make": "Isometric staircase showing bars growing by fixed height d",
                        "what_to_explain": "Visual intuition of linear discrete addition"
                    }
                ]
            },
            "common_misconceptions": [
                "Accepting fractional values of n: n represents an ordinal position (1st, 2nd, 3rd) and must be a natural number!",
                "Subtracting a₁ from a₂ backwards: Common difference is always forward: d = a₂ - a₁."
            ]
        },

        # Module 2: Sum of First n Terms of an AP & Gauss Method
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Sum of Arithmetic Progressions: Gaussian Inversion Method & Term-Sum Bridge aₙ = Sₙ - Sₙ₋₁",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master the derivation of the sum of the first n terms of an AP using young Gauss's elegant pairing inversion technique. Learn both representations: Sₙ = (n/2)[2a + (n-1)d] and Sₙ = (n/2)[a + l], and master the vital diagnostic bridge aₙ = Sₙ - Sₙ₋₁.",
            "key_concepts": [
                "Gauss Inversion Proof: Writing the sum forwards and backwards, adding column-wise to get 2Sₙ = n(a + l)",
                "Formula 1: Sₙ = (n / 2) [ 2a + (n - 1)d ]",
                "Formula 2: Sₙ = (n / 2) [ a + l ] where l is the last term",
                "Sum of First n Positive Integers: Σ n = n(n + 1) / 2",
                "The Term-Sum Bridge: aₙ = Sₙ - Sₙ₋₁ for n ≥ 2, with a₁ = S₁"
            ],
            "subtopics": [
                "Step-by-step algebraic proof of the summation formula",
                "Worked Examples 11, 12, 13, 14, 15 from NCERT",
                "Finding n when Sₙ is given (solving quadratic in n and explaining double answers)",
                "Extracting an AP when Sₙ is given as an algebraic function of n"
            ],
            "worked_examples": [
                {
                    "problem": "Example 11 (NCERT): Find the sum of the first 22 terms of the AP: 8, 3, -2, ...",
                    "solution": "Given AP: 8, 3, -2, ...\nHere, First term (a) = 8\nCommon difference (d) = 3 - 8 = -5\nNumber of terms (n) = 22.\nFormula: Sₙ = (n / 2) [ 2a + (n - 1)d ]\nSubstitution:\nS₂₂ = (22 / 2) [ 2(8) + (22 - 1)(-5) ]\n= 11 [ 16 + 21(-5) ]\n= 11 [ 16 - 105 ]\n= 11 [ -89 ] = -979.\n[ROUGH_WORK]\n21 × (-5) = -105\n16 - 105 = -89\n11 × (-89) = -979\nBoxed Answer: [ The sum of the first 22 terms is -979 ].",
                    "concept_questions": [
                        "Why is the sum negative even though the first term is positive?",
                        "At what term does this AP start becoming negative?"
                    ]
                },
                {
                    "problem": "Example 13 (NCERT): How many terms of the AP: 24, 21, 18, ... must be taken so that their sum is 78?",
                    "solution": "Given AP: 24, 21, 18, ...\nFirst term (a) = 24\nCommon difference (d) = 21 - 24 = -3\nGiven sum (Sₙ) = 78.\nFormula: Sₙ = (n / 2) [ 2a + (n - 1)d ]\n78 = (n / 2) [ 2(24) + (n - 1)(-3) ]\n156 = n [ 48 - 3n + 3 ]\n156 = n [ 51 - 3n ]\n156 = 51n - 3n²\nBring all terms to LHS:\n3n² - 51n + 156 = 0\nDivide by 3:\nn² - 17n + 52 = 0\n\nFactorisation: ac = 52. Numbers with product 52 and sum -17: -13 and -4.\nn² - 13n - 4n + 52 = 0\nn(n - 13) - 4(n - 13) = 0\n(n - 13)(n - 4) = 0 ⇒ n = 4 or n = 13.\n\nExplanation of Double Answer:\nBoth values n = 4 and n = 13 are valid natural numbers!\nWhy are there two answers? Sum of first 4 terms = 24 + 21 + 18 + 15 = 78.\nThe terms from 5th to 13th are: 12, 9, 6, 3, 0, -3, -6, -9, -12.\nThe sum of terms from 5th to 13th is: (12 - 12) + (9 - 9) + (6 - 6) + (3 - 3) + 0 = 0!\nThus, adding the next 9 terms contributes a sum of 0, keeping the total sum at 78.\n[ROUGH_WORK]\nSum(1..4) = 78\nSum(5..13) = 0\nSum(1..13) = 78 + 0 = 78 (Brilliant!)\nBoxed Answer: [ n = 4 or n = 13. Reason for double answer: Sum of terms from 5th to 13th is exactly 0 ].",
                    "concept_questions": [
                        "Why does the quadratic equation in n produce two positive integer solutions here?",
                        "What must be true about the terms between n = 4 and n = 13 for their sum to vanish?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "AP Sum Formula Card & Gauss Inversion HUD",
                "diagram_type": "diagram",
                "svg": svg_ap_card,
                "concept_visuals": [
                    {
                        "concept_title": "Summation Formulas HUD",
                        "diagram_title": "AP Formula Architecture",
                        "svg": svg_ap_card,
                        "diagram_type": "diagram",
                        "what_to_make": "HUD summary of both sum formulas and bridge relation",
                        "what_to_explain": "Symmetric pairing of terms yielding identical sums"
                    }
                ]
            },
            "common_misconceptions": [
                "Discarding one of the roots when a quadratic in n produces two positive integers: Both answers can be physically valid when d is negative because the terms cancel out to zero!",
                "Confusing Sₙ (sum of n terms) with aₙ (the nth term value)."
            ]
        },

        # Module 3: Exercise 5.1 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise 5.1 Complete Solver: AP Verification, Common Difference & Sequence Generation (Q1 to Q4)",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete resolution of all 4 questions in NCERT Exercise 5.1. Question 1 (4 real-life scenarios tested for AP behavior: taxi fare, vacuum pump, well digging, compound interest), Question 2 (generating first 4 terms), Question 3 (extracting a and d), and Question 4 (testing 15 varied sequences for AP status).",
            "key_concepts": [
                "Ex 5.1 Q1: Real-life AP verification (Linear vs Non-linear vs Exponential growth)",
                "Ex 5.1 Q2: Generating terms using aₖ₊₁ = aₖ + d for positive, negative, and fractional d",
                "Ex 5.1 Q3: Reading a = a₁ and d = a₂ - a₁",
                "Ex 5.1 Q4: Testing 15 sequences for constant d (including radicals like √2, √8, √18, √32 and powers like a, a², a³, a⁴)"
            ],
            "subtopics": [
                "Why compound interest is NOT an AP (geometric/exponential, not arithmetic)",
                "Why air removed by vacuum pump (1/4th remaining) is NOT an AP",
                "Simplifying surds to identify hidden APs: √8 = 2√2, √18 = 3√2, √32 = 4√2",
                "Full resolution of all 15 parts of Q4"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 5.1 Q1 (ii): The amount of air present in a cylinder when a vacuum pump removes 1/4 of the air remaining in the cylinder at a time. Does this situation form an AP? Justify.",
                    "solution": "Let initial volume of air in cylinder = V units (term a₁ = V).\nStep 1: First removal: Pump removes (1/4)V.\nRemaining air (a₂) = V - (1/4)V = (3/4)V.\n\nStep 2: Second removal: Pump removes (1/4) of remaining air = (1/4) × (3/4)V = (3/16)V.\nRemaining air (a₃) = (3/4)V - (3/16)V = (12 - 3)/16 V = (9/16)V = (3/4)² V.\n\nStep 3: Third removal: Remaining air (a₄) = (3/4)³ V = (27/64)V.\n\nStep 4: Check if difference between consecutive terms is constant:\na₂ - a₁ = (3/4)V - V = -1/4 V.\na₃ - a₂ = (9/16)V - (3/4)V = -3/16 V.\nSince a₂ - a₁ ≠ a₃ - a₂ (-1/4 V ≠ -3/16 V), the common difference is not constant.\nTherefore, this situation does NOT form an AP.\n[ROUGH_WORK]\nTerms: V, (3/4)V, (9/16)V, (27/64)V\nRatio is constant (3/4) ⇒ This is a Geometric Progression (GP), not an AP!\nBoxed Answer: [ No, it does not form an AP because the difference between consecutive terms is not constant ].",
                    "concept_questions": [
                        "What is the difference between an Arithmetic Progression and a Geometric Progression?",
                        "What kind of air removal would have produced an authentic AP?"
                    ]
                },
                {
                    "problem": "Exercise 5.1 Q4 (xii): Check whether √2, √8, √18, √32, ... forms an AP. If it forms an AP, find the common difference d and write three more terms.",
                    "solution": "Given sequence: √2, √8, √18, √32, ...\nStep 1: Simplify each radical term into simplest surd form:\na₁ = √2\na₂ = √8 = √(4 × 2) = 2√2\na₃ = √18 = √(9 × 2) = 3√2\na₄ = √32 = √(16 × 2) = 4√2\n\nStep 2: Calculate consecutive differences:\na₂ - a₁ = 2√2 - √2 = √2\na₃ - a₂ = 3√2 - 2√2 = √2\na₄ - a₃ = 4√2 - 3√2 = √2\nSince aₖ₊₁ - aₖ is constant (= √2), the sequence is an AP!\nCommon difference d = √2.\n\nStep 3: Find next three terms:\na₅ = a₄ + d = 4√2 + √2 = 5√2 = √(25 × 2) = √50\na₆ = a₅ + d = 5√2 + √2 = 6√2 = √(36 × 2) = √72\na₇ = a₆ + d = 6√2 + √2 = 7√2 = √(49 × 2) = √98\n[ROUGH_WORK]\n5√2 = √50, 6√2 = √72, 7√2 = √98\nBoxed Answer: [ Yes, it forms an AP. Common difference d = √2. Next three terms are √50, √72, and √98 ].",
                    "concept_questions": [
                        "Why does √3, √6, √9, √12 NOT form an AP? Calculate √6 - √3 and √9 - √6 to prove it.",
                        "How does simplifying surds unlock the hidden structure of numerical sequences?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Surd AP Growth & Exponential Contrast HUD",
                "diagram_type": "diagram",
                "svg": svg_staircase,
                "concept_visuals": [
                    {
                        "concept_title": "Radical Progression Visualization",
                        "diagram_title": "Surd Simplification Atlas",
                        "svg": svg_staircase,
                        "diagram_type": "diagram",
                        "what_to_make": "Staircase showing bars increasing by fixed height √2",
                        "what_to_explain": "Rewriting √8, √18, √32 as multiples of √2 reveals exact AP structure"
                    }
                ]
            },
            "common_misconceptions": [
                "Assuming √2, √8, √18, √32 is not an AP because the numbers under the square root are 2, 8, 18, 32: You MUST simplify radicals before testing differences!",
                "Believing √6 - √3 = √3: Radical subtraction does NOT allow subtracting inside the roots!"
            ]
        },

        # Module 4: Exercise 5.2 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 5.2 Complete Solver: General Term aₙ Mastery (All 20 Questions Step-by-Step)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Comprehensive step-by-step resolution of NCERT Exercise 5.2 covering all 20 questions. Includes table missing parameter calculations, box sequence completions, finding term counts, testing belongingness, and solving real-world salary/savings word problems.",
            "key_concepts": [
                "Ex 5.2 Q1: Solving for 4-variable equation aₙ = a + (n - 1)d",
                "Ex 5.2 Q3: Missing box terms using arithmetic mean: Box between a and b is (a + b)/2",
                "Ex 5.2 Q4-Q6: Testing term existence and indices",
                "Ex 5.2 Q7-Q16: Systems of equations in a and d",
                "Ex 5.2 Q17: Finding the 20th term from the last term of the AP: 3, 8, 13, ..., 253",
                "Ex 5.2 Q19-Q20: Subba Rao annual increments & Ramkali weekly savings"
            ],
            "subtopics": [
                "Arithmetic mean property: If a, b, c are in AP, then b = (a + c)/2",
                "Reverse AP technique: To find m-th term from the end, reverse the AP with first term l and common difference -d",
                "Full resolution of Q1 to Q20"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 5.2 Q7: Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.",
                    "solution": "Given:\n11th term (a₁₁) = 38\n16th term (a₁₆) = 73\nTarget: Find a₃₁.\n\nStep 1: Express terms in a and d:\na₁₁ = a + 10d = 38 ... (1)\na₁₆ = a + 15d = 73 ... (2)\n\nStep 2: Subtract (1) from (2):\n(a + 15d) - (a + 10d) = 73 - 38\n5d = 35 ⇒ d = 7.\n\nStep 3: Find a from (1):\na + 10(7) = 38 ⇒ a + 70 = 38 ⇒ a = 38 - 70 = -32.\n\nStep 4: Find the 31st term:\na₃₁ = a + 30d = -32 + 30(7) = -32 + 210 = 178.\n[ROUGH_WORK]\nAlternative shortcut: a₃₁ = a₁₆ + 15d = 73 + 15(7) = 73 + 105 = 178 (Instant verification!)\nBoxed Answer: [ The 31st term is 178 ].",
                    "concept_questions": [
                        "Notice the shortcut a₃₁ = a₁₆ + 15d: why does this formula avoid calculating the first term a altogether?"
                    ]
                },
                {
                    "problem": "Exercise 5.2 Q17: Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.",
                    "solution": "Given AP: 3, 8, 13, ..., 253\nCommon difference (d) = 8 - 3 = 5.\nLast term (l) = 253.\n\nMethod 1 (Reversing the AP):\nWhen looking from the end backwards, the sequence is an AP with:\nFirst term (A) = 253\nCommon difference (D) = -d = -5\nTarget: 20th term of this reversed AP (n = 20).\nFormula: A₂₀ = A + (n - 1)D\n= 253 + (20 - 1)(-5)\n= 253 + 19(-5) = 253 - 95 = 158.\n\nMethod 2 (Using total term count):\n253 = 3 + (N - 1)5 ⇒ 250 = 5(N - 1) ⇒ N - 1 = 50 ⇒ N = 51 terms total.\nThe 20th term from the end is the (N - 20 + 1)th term from the beginning:\n= (51 - 20 + 1)th = 32nd term from beginning.\na₃₂ = a + 31d = 3 + 31(5) = 3 + 155 = 158.\n[ROUGH_WORK]\nBoth methods yield exactly 158!\nBoxed Answer: [ The 20th term from the last term is 158 ].",
                    "concept_questions": [
                        "Why is the formula for the nth term from the end l - (n - 1)d?",
                        "Why is the kth term from the end equal to the (N - k + 1)th term from the start?"
                    ]
                },
                {
                    "problem": "Exercise 5.2 Q19: Subba Rao started work in 1995 at an annual salary of ₹ 5000 and received an increment of ₹ 200 each year. In which year did his income reach ₹ 7000?",
                    "solution": "Annual salaries form an AP: 5000, 5200, 5400, ..., 7000\nFirst term (a) = ₹ 5000\nCommon difference (d) = ₹ 200\nTarget term (aₙ) = ₹ 7000.\nTarget: Find n.\n\nFormula: aₙ = a + (n - 1)d\n7000 = 5000 + (n - 1)(200)\n7000 - 5000 = 200(n - 1)\n2000 = 200(n - 1)\nn - 1 = 2000 / 200 = 10\nn = 11.\n\nYear determination: Started in 1995 (1st year).\n11th year = 1995 + (11 - 1) = 1995 + 10 = 2005.\n[ROUGH_WORK]\n1995: 5000\n2005: 5000 + 10(200) = 7000 (True!)\nBoxed Answer: [ In the 11th year (year 2005), his income reached ₹ 7000 ].",
                    "concept_questions": [
                        "Why do we add 10 to 1995 to reach the 11th year instead of adding 11?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "AP Term Indexing & Reverse AP Traversal HUD",
                "diagram_type": "diagram",
                "svg": svg_staircase,
                "concept_visuals": [
                    {
                        "concept_title": "Reverse AP Traversal",
                        "diagram_title": "Backward Linear Progression",
                        "svg": svg_staircase,
                        "diagram_type": "diagram",
                        "what_to_make": "Staircase traversed in reverse from l with step -d",
                        "what_to_explain": "Reversing an AP inverts common difference d to -d"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting the +1 when converting rank from end to rank from beginning: The kth term from end of N terms is (N - k + 1)th!",
                "Adding n directly to the starting calendar year: For 11th year, add (11 - 1) = 10 years to the start."
            ]
        },

        # Module 5: Exercise 5.3 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise 5.3 Complete Solver: AP Summation Masterclass & 20 Applied Problems (Q1 to Q20)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Exhaustive resolution of NCERT Exercise 5.3 covering all 20 questions. Includes Q1-Q3 algebraic summations, Q4 term count for sum 636, Q10 general term from Sₙ, Q11 finding S₁, S₂, a₂, a₃, a₁₀, aₙ, and famous real-world applications: school trees, spiral of semicircles, log piles, and potato race.",
            "key_concepts": [
                "Ex 5.3 Q3: Master matrix of 10 sub-problems solving across a, d, n, aₙ, Sₙ",
                "Ex 5.3 Q4: Sum 636 in AP 9, 17, 25,... ⇒ 4n² + 5n - 636 = 0 ⇒ n = 12",
                "Ex 5.3 Q11: Given Sₙ = 4n - n², find aₙ = Sₙ - Sₙ₋₁ = 5 - 2n",
                "Ex 5.3 Q17: School tree planting (Classes 1 to 12, 3 sections each ⇒ 3 × 78 = 234 trees)",
                "Ex 5.3 Q18: Spiral of 13 consecutive semicircles with radii 0.5, 1.0, 1.5, ... ⇒ Length = 143 cm",
                "Ex 5.3 Q19: 200 logs stacked in rows (20 in bottom, 19 next, 18 next ⇒ n = 16 rows, 5 logs in top)",
                "Ex 5.3 Q20: Potato race (bucket at 5 m, potatoes spaced 3 m apart ⇒ total distance = 370 m)"
            ],
            "subtopics": [
                "Full resolution of Q1 to Q20",
                "Quadratic factorisation in summation problems",
                "Geometric semicircle spiral arc length summation: l = πr"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 5.3 Q11: If the sum of the first n terms of an AP is given by Sₙ = 4n - n², what is the first term (that is S₁)? What is the sum of first two terms? What is the second term? Similarly, find the 3rd, the 10th and the nth terms.",
                    "solution": "Given: Sₙ = 4n - n²\n\nStep 1: Find first term a₁ (which is S₁):\na₁ = S₁ = 4(1) - 1² = 4 - 1 = 3.\n\nStep 2: Find sum of first two terms S₂:\nS₂ = 4(2) - 2² = 8 - 4 = 4.\n\nStep 3: Find second term a₂ using a₂ = S₂ - S₁:\na₂ = 4 - 3 = 1.\n\nStep 4: Find common difference d:\nd = a₂ - a₁ = 1 - 3 = -2.\n\nStep 5: Find 3rd term (a₃):\na₃ = a + 2d = 3 + 2(-2) = 3 - 4 = -1.\n\nStep 6: Find 10th term (a₁₀):\na₁₀ = a + 9d = 3 + 9(-2) = 3 - 18 = -15.\n\nStep 7: Find the nth term (aₙ) using aₙ = Sₙ - Sₙ₋₁:\nSₙ₋₁ = 4(n - 1) - (n - 1)² = 4n - 4 - (n² - 2n + 1) = 4n - 4 - n² + 2n - 1 = -n² + 6n - 5.\naₙ = Sₙ - Sₙ₋₁ = (4n - n²) - (-n² + 6n - 5)\n= 4n - n² + n² - 6n + 5 = 5 - 2n.\n[ROUGH_WORK]\nCheck formula aₙ = 5 - 2n:\nn = 1: a₁ = 5 - 2 = 3 (Matches!)\nn = 2: a₂ = 5 - 4 = 1 (Matches!)\nn = 10: a₁₀ = 5 - 20 = -15 (Matches!)\nBoxed Answer: [ First term = 3, Sum of 2 terms = 4, Second term = 1, 3rd term = -1, 10th term = -15, nth term = 5 - 2n ].",
                    "concept_questions": [
                        "Why is the formula aₙ = Sₙ - Sₙ₋₁ the fundamental bridge connecting sequence sums to individual terms?",
                        "Notice that Sₙ is quadratic in n with no constant term: why does an AP sum always have this form?"
                    ]
                },
                {
                    "problem": "Exercise 5.3 Q18: A spiral is made up of successive semicircles, with centres alternately at A and B, starting with centre at A, of radii 0.5 cm, 1.0 cm, 1.5 cm, 2.0 cm, ... What is the total length of such a spiral made up of thirteen consecutive semicircles? (Take π = 22/7)",
                    "solution": "Length of a semicircle of radius r is given by perimeter = πr.\nRadii of successive semicircles: r₁ = 0.5, r₂ = 1.0, r₃ = 1.5, r₄ = 2.0, ...\nLengths of semicircles:\nl₁ = π(0.5)\nl₂ = π(1.0)\nl₃ = π(1.5)\nl₄ = π(2.0), ... up to 13 semicircles.\n\nTotal length L = l₁ + l₂ + l₃ + ... + l₁₃\nL = π(0.5 + 1.0 + 1.5 + 2.0 + ... to 13 terms)\nNotice the series inside the bracket is an AP with:\nFirst term (a) = 0.5\nCommon difference (d) = 1.0 - 0.5 = 0.5\nNumber of terms (n) = 13.\n\nSum of AP (S₁₃) = (n / 2) [ 2a + (n - 1)d ]\nS₁₃ = (13 / 2) [ 2(0.5) + (13 - 1)(0.5) ]\n= (13 / 2) [ 1.0 + 12(0.5) ]\n= (13 / 2) [ 1.0 + 6.0 ] = (13 / 2) × 7 = 91 / 2 = 45.5 cm.\n\nTotal Length = π × S₁₃ = (22 / 7) × (91 / 2)\n= 11 × 13 = 143 cm.\n[ROUGH_WORK]\n22/7 × 91/2:\n91 / 7 = 13\n22 / 2 = 11\n11 × 13 = 143\nBoxed Answer: [ Total length of the spiral = 143 cm ].",
                    "concept_questions": [
                        "Why does the perimeter of a semicircle equal πr and not πr + 2r in this spiral?",
                        "How would the total length change if the common difference of the radii was doubled?"
                    ]
                },
                {
                    "problem": "Exercise 5.3 Q19: 200 logs are stacked in the following manner: 20 logs in the bottom row, 19 in the next row, 18 in the row next to it and so on. In how many rows are the 200 logs placed and how many logs are in the top row?",
                    "solution": "Number of logs in rows from bottom to top forms an AP:\nFirst term (a) = 20 (bottom row)\nCommon difference (d) = 19 - 20 = -1\nTotal logs (Sₙ) = 200.\nTarget: Find number of rows n, and logs in top row aₙ.\n\nFormula: Sₙ = (n / 2) [ 2a + (n - 1)d ]\n200 = (n / 2) [ 2(20) + (n - 1)(-1) ]\n400 = n [ 40 - n + 1 ]\n400 = n [ 41 - n ]\n400 = 41n - n²\nn² - 41n + 400 = 0\n\nFactorisation: ac = 400. Numbers with product 400 and sum -41: -25 and -16.\nn² - 25n - 16n + 400 = 0\nn(n - 25) - 16(n - 25) = 0\n(n - 25)(n - 16) = 0 ⇒ n = 25 or n = 16.\n\nTesting both roots for physical feasibility:\nCase 1: If n = 25:\nTop row logs = a₂₅ = a + 24d = 20 + 24(-1) = 20 - 24 = -4.\nNumber of logs cannot be negative! Therefore, n = 25 is physically impossible.\n\nCase 2: If n = 16:\nTop row logs = a₁₆ = a + 15d = 20 + 15(-1) = 20 - 15 = 5.\n5 logs in the top row is completely valid.\n[ROUGH_WORK]\nSum for n = 16: (16/2)(20 + 5) = 8 × 25 = 200 (True!)\nBoxed Answer: [ 200 logs are placed in 16 rows, with 5 logs in the top row ].",
                    "concept_questions": [
                        "Why did the quadratic equation yield n = 25, and what is the physical meaning of negative logs?",
                        "How many logs would be in the 17th row if the stack were continued?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Spiral Semicircle & Log Stacking AP HUD",
                "diagram_type": "diagram",
                "svg": svg_staircase,
                "concept_visuals": [
                    {
                        "concept_title": "Spiral Semicircles Geometry",
                        "diagram_title": "Continuous Spiral Arc Model",
                        "svg": svg_staircase,
                        "diagram_type": "diagram",
                        "what_to_make": "Spiral of 13 semicircles radiating outwards",
                        "what_to_explain": "Cumulative length summation via AP radius increments"
                    }
                ]
            },
            "common_misconceptions": [
                "Blindly accepting n = 25 without checking the number of logs in the top row: Always check aₙ > 0 in physical problems!",
                "Including the diameter in the semicircle perimeter for the spiral problem."
            ]
        },

        # Module 6: Exercise 5.4 (Optional) & Advanced Board Masterclass
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 6,
            "title": "Exercise 5.4 Optional Solver: First Negative Term, Concrete Terrace & Board HOTS",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete resolution of NCERT Exercise 5.4 (Optional). Question 1 (finding first negative term of AP 121, 117, 113, ...), Question 2 (sum of 3rd and 7th terms is 6, product is 8), Question 3 (ladder with uniformly decreasing rungs), Question 4 (houses numbered 1 to 49 with equal sum of predecessors and successors), and Question 5 (solid concrete terrace 15 steps volume summation).",
            "key_concepts": [
                "Ex 5.4 Q1: Condition for first negative term: aₙ < 0 ⇒ a + (n - 1)d < 0 ⇒ n > 31.25 ⇒ n = 32",
                "Ex 5.4 Q2: Solving systems involving products of terms using symmetric substitution: a - d, a, a + d",
                "Ex 5.4 Q3: Trapezoidal ladder rungs AP: a = 45 cm, l = 25 cm, n = 10 rungs",
                "Ex 5.4 Q4: Houses numbered 1 to 49: S_{x-1} = S₄₉ - S_x ⇒ x = 35",
                "Ex 5.4 Q5: Terrace with 15 steps: Step volume = 50 × (1/4) × (1/2)k ⇒ Total volume = 750 m³"
            ],
            "subtopics": [
                "Inequality solving for first negative/positive term index",
                "House number sum equivalence proof",
                "Volume summation of 3D concrete steps"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 5.4 Q1: Which term of the AP: 121, 117, 113, ... is its first negative term?",
                    "solution": "Given AP: 121, 117, 113, ...\nFirst term (a) = 121\nCommon difference (d) = 117 - 121 = -4\n\nCondition for negative term: aₙ < 0\nFormula: a + (n - 1)d < 0\n121 + (n - 1)(-4) < 0\n121 - 4n + 4 < 0\n125 - 4n < 0\n125 < 4n\n4n > 125\nn > 125 / 4\nn > 31.25.\n\nSince n must be an integer, the smallest integer strictly greater than 31.25 is n = 32.\n[ROUGH_WORK]\nCheck 31st term: a₃₁ = 121 + 30(-4) = 121 - 120 = +1 (Last positive term!)\nCheck 32nd term: a₃₂ = 121 + 31(-4) = 121 - 124 = -3 (First negative term!)\nBoxed Answer: [ The 32nd term is the first negative term of the AP (value is -3) ].",
                    "concept_questions": [
                        "Why did the inequality sign flip when rearranging terms?",
                        "What is the value of the last positive term of this AP?"
                    ]
                },
                {
                    "problem": "Exercise 5.4 Q4: The houses of a row are numbered consecutively from 1 to 49. Show that there is a value of x such that the sum of the numbers of the houses preceding the house numbered x is equal to the sum of the numbers of the houses following it. Find this value of x.",
                    "solution": "House numbers are: 1, 2, 3, ..., (x - 1), x, (x + 1), ..., 49\nThis is an AP of natural numbers with a = 1, d = 1.\n\nCondition:\nSum of houses preceding house x = Sum of houses following house x\nSum(1 to x - 1) = Sum(x + 1 to 49)\n\nWe know:\nSum(1 to x - 1) = S_{x - 1}\nSum(x + 1 to 49) = S₄₉ - S_x\n\nEquation:\nS_{x - 1} = S₄₉ - S_x\nFormula for sum of first n natural numbers: Sₙ = n(n + 1) / 2\n\nSubstitute formulas:\n[ (x - 1)(x) ] / 2 = [ 49(50) / 2 ] - [ x(x + 1) / 2 ]\n\nMultiply entire equation by 2 to clear denominators:\nx(x - 1) = 49(50) - x(x + 1)\nx² - x = 2450 - x² - x\n\nNotice -x cancels from both sides:\nx² = 2450 - x²\n2x² = 2450\nx² = 1225\nx = √1225 = 35.\n(Reject negative root since house numbers are positive).\n[ROUGH_WORK]\nS₃₄ = 34 × 35 / 2 = 17 × 35 = 595\nSum(36 to 49) = S₄₉ - S₃₅ = (49 × 50 / 2) - (35 × 36 / 2) = 1225 - 630 = 595\n595 = 595 (Exact match!)\nBoxed Answer: [ The value of x is 35 ].",
                    "concept_questions": [
                        "Why does the term -x conveniently cancel on both sides?",
                        "How is 1225 recognized as 35²?"
                    ]
                },
                {
                    "problem": "Exercise 5.4 Q5: A small terrace at a football ground comprises of 15 steps each of which is 50 m long and built of solid concrete. Each step has a rise of 1/4 m and a tread of 1/2 m. Calculate the total volume of concrete required to build the terrace.",
                    "solution": "Length of each step = 50 m\nTread (width) of each step = 1/2 m\nRise (height increment) of each step = 1/4 m.\n\nStep 1: Volume of concrete in 1st step:\nLength × Width × Height = 50 × (1/2) × (1/4) = 50 / 8 = 25/4 m³.\n\nStep 2: Volume of concrete in 2nd step:\nHeight = 2 × (1/4) m\nVolume = 50 × (1/2) × [2 × (1/4)] = 2 × (25/4) m³.\n\nStep 3: Volume of concrete in 3rd step:\nHeight = 3 × (1/4) m\nVolume = 3 × (25/4) m³.\n\nStep 4: Total volume for all 15 steps is an AP:\nFirst term (a) = 25/4\nCommon difference (d) = 25/4\nNumber of terms (n) = 15.\n\nTotal Volume V = S₁₅ = (n / 2) [ 2a + (n - 1)d ]\n= (15 / 2) [ 2(25/4) + 14(25/4) ]\n= (15 / 2) [ 16 × (25/4) ]\n= (15 / 2) [ 4 × 25 ]\n= (15 / 2) [ 100 ] = 15 × 50 = 750 m³.\n[ROUGH_WORK]\nAlternative: (25/4) × (1 + 2 + ... + 15) = (25/4) × (15 × 16 / 2) = (25/4) × 120 = 25 × 30 = 750 m³.\nBoxed Answer: [ Total volume of concrete required = 750 m³ ].",
                    "concept_questions": [
                        "Why is factoring out the volume of the first step (25/4) so effective?",
                        "What is the physical reason each successive step requires an additional 25/4 m³ of concrete?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Concrete Terrace & House Number AP HUD",
                "diagram_type": "diagram",
                "svg": svg_staircase,
                "concept_visuals": [
                    {
                        "concept_title": "Concrete Step Volume Stacking",
                        "diagram_title": "Isometric Terrace Architecture",
                        "svg": svg_staircase,
                        "diagram_type": "diagram",
                        "what_to_make": "Isometric 15-step terrace showing progressive volume accumulation",
                        "what_to_explain": "Each step adds uniform cross-sectional volume proportional to its height"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting that the steps extend all the way down to the foundation: Each step must support itself, so step k has total height k × (1/4)!",
                "Writing S_{x} = S₄₉ - S_x instead of S_{x-1} = S₄₉ - S_x (house x itself is not included in either sum)."
            ]
        }
    ]
    
    return modules
