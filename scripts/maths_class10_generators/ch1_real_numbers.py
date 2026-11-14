"""
Class 10 Mathematics - Chapter 1: Real Numbers
Curriculum ID: 4f230f16-2470-4304-b7cd-4aeacbc51831
CBSE Class 10 NCERT (Rationalised Syllabus)
Modules 1 to 5:
- M1: The Fundamental Theorem of Arithmetic & Prime Factorization
- M2: Revisiting Irrational Numbers & Rigorous Proofs of Contradiction
- M3: Dedicated Exercise 1.1 Solver (All questions & parts)
- M4: Dedicated Exercise 1.2 Solver (All irrationality proofs)
- M5: Board Exam Numerical Mastery, HCF-LCM Word Problems & High-Order Thinking
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.maths_class10_generators.svg_builder_class10 import (
    build_real_numbers_factor_tree_svg,
    get_svg_wrapper
)

def build_irrational_number_line_svg():
    elements = []
    # Number line showing rational approximations converging to sqrt(2)
    elements.append('<line x1="60" y1="200" x2="520" y2="200" stroke="#334155" stroke-width="2" marker-end="url(#arrowSlate)"/>')
    elements.append('<line x1="60" y1="200" x2="50" y2="200" stroke="#334155" stroke-width="2" marker-end="url(#arrowSlate)"/>')
    
    # Unit intervals
    ticks = [
        (100, "0"), (220, "1"), (340, "2"), (460, "3")
    ]
    for px, label in ticks:
        elements.append(f'<line x1="{px}" y1="192" x2="{px}" y2="208" stroke="#334155" stroke-width="1.8"/>')
        elements.append(f'<text x="{px}" y="228" fill="#0F172A" font-size="12" font-weight="700" text-anchor="middle">{label}</text>')
        
    # sqrt(2) approx 1.414 -> px = 220 + 0.414 * 120 = 269.7
    sqrt2_x = 220 + 0.4142 * 120
    elements.append(f'<circle cx="{sqrt2_x}" cy="200" r="5" fill="#DC2626"/>')
    elements.append(f'<line x1="{sqrt2_x}" y1="200" x2="{sqrt2_x}" y2="130" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3,3"/>')
    elements.append(f'<text x="{sqrt2_x}" y="118" fill="#DC2626" font-size="13" font-weight="700" text-anchor="middle">√2 ≈ 1.41421356...</text>')
    elements.append(f'<text x="{sqrt2_x}" y="98" fill="#64748B" font-size="11" text-anchor="middle">Non-terminating &amp; Non-repeating</text>')

    # Right triangle 1x1 on hypotenuse
    elements.append('<polygon points="220,200 220,120 340,200" fill="none" stroke="#2563EB" stroke-width="1.8"/>')
    elements.append('<text x="205" y="160" fill="#2563EB" font-size="11" font-weight="600">1</text>')
    elements.append('<text x="280" y="218" fill="#2563EB" font-size="11" font-weight="600">1</text>')
    elements.append('<text x="290" y="150" fill="#2563EB" font-size="11" font-weight="700">Hyp = √2</text>')

    # Theorem Box
    box = """
    <g transform="translate(30, 50)">
      <rect width="160" height="74" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.2" rx="6"/>
      <text x="10" y="20" fill="#991B1B" font-size="11" font-weight="700">Theorem 1.2 &amp; 1.3:</text>
      <text x="10" y="38" fill="#0F172A" font-size="10">If p is prime and p | a²,</text>
      <text x="10" y="52" fill="#0F172A" font-size="10">then p divides a.</text>
      <text x="10" y="66" fill="#DC2626" font-size="10" font-weight="700">Hence √p is irrational.</text>
    </g>
    """
    elements.append(box)
    return get_svg_wrapper("\n".join(elements), title="The Irrational Number Line: Exact Geometric Location of √2", caption="Pythagorean right triangle projection proving irrationality cannot be represented as p/q")


def get_ch1_modules():
    tree_svg = build_real_numbers_factor_tree_svg(32760)
    irrational_svg = build_irrational_number_line_svg()

    # Module 1: The Fundamental Theorem of Arithmetic & Prime Factorization
    m1 = {
        "order_index": 1,
        "title": "Fundamental Theorem of Arithmetic: Prime Powers, Unique Factorization & Relation HCF × LCM = a × b",
        "description": "Master the Fundamental Theorem of Arithmetic (FTA), expressing every composite number uniquely as a product of prime powers. Derive and apply the fundamental identity HCF(a, b) × LCM(a, b) = a × b for two positive integers.",
        "subtopics": [
            "Every composite integer greater than 1 as a unique product of primes",
            "Prime Factor Tree Decomposition Method",
            "Calculating Highest Common Factor (HCF) using minimum prime exponents",
            "Calculating Lowest Common Multiple (LCM) using maximum prime exponents",
            "Verification of the product relationship: HCF(a, b) × LCM(a, b) = a × b",
            "Why the relation HCF × LCM = a × b × c does NOT hold for three integers"
        ],
        "key_concepts": [
            "Fundamental Theorem of Arithmetic (Theorem 1.1): Every composite number can be expressed as a product of primes uniquely, apart from the order in which the prime factors occur.",
            "HCF Calculation Rule: Product of the smallest power of each common prime factor involved in the numbers.",
            "LCM Calculation Rule: Product of the greatest power of each prime factor involved in the numbers.",
            "Two-Integer Product Invariant: For any two positive integers a and b, HCF(a, b) × LCM(a, b) = a × b.",
            "Non-Termination Test: The prime factorization of 6^n or 4^n cannot end with digit 0 because it lacks 5 as a prime factor (requires both 2 and 5)."
        ],
        "success_criteria": "Student can factorize any composite number into prime powers, compute HCF and LCM accurately, verify HCF × LCM = a × b, and prove why numbers like 4^n or 6^n cannot end with digit 0.",
        "chapter_notes": "Remember: The formula HCF × LCM = Product of numbers holds strictly for TWO numbers only. For three numbers a, b, c, HCF(a,b,c) × LCM(a,b,c) ≠ a × b × c.",
        "worked_examples": [
            {
                "problem": "Textbook Example 1: Consider the numbers 4^n, where n is a natural number. Check whether there is any value of n for which 4^n ends with the digit zero.",
                "given": "Expression 4^n where n ∈ N (natural numbers).",
                "formula": "A number ends with digit 0 if and only if its prime factorization contains both 2 and 5 as prime factors (i.e. is divisible by 10 = 2 × 5).",
                "substitution": "4^n = (2^2)^n = 2^(2n).",
                "calculation": "Step 1: Write the prime factors of 4: 4 = 2 × 2 = 2^2.\nStep 2: Express 4^n: 4^n = (2^2)^n = 2^(2n).\nStep 3: By the Fundamental Theorem of Arithmetic, the prime factorization of 4^n contains only the prime 2.\nStep 4: The prime 5 does not occur in the factorization of 4^n for any natural number n.\nStep 5: Since 5 is not a prime factor, 4^n cannot be divisible by 10 for any n.",
                "finalAnswer": "There is no natural number n for which 4^n ends with the digit zero.",
                "unit": "conclusion",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 2: Find the LCM and HCF of 6 and 20 by the prime factorisation method.",
                "given": "Numbers: a = 6, b = 20.",
                "formula": "HCF = Product of smallest power of each common prime factor. LCM = Product of greatest power of each prime factor. Relationship: HCF × LCM = a × b.",
                "substitution": "6 = 2^1 × 3^1; 20 = 2^2 × 5^1.",
                "calculation": "Step 1: Prime factorise 6: 6 = 2^1 × 3^1.\nStep 2: Prime factorise 20: 20 = 2 × 2 × 5 = 2^2 × 5^1.\nStep 3: Identify common prime factor: 2. Smallest power is 2^1 = 2 => HCF(6, 20) = 2.\nStep 4: Identify all prime factors with greatest powers: 2^2, 3^1, 5^1.\nLCM(6, 20) = 2^2 × 3^1 × 5^1 = 4 × 3 × 5 = 60.\nStep 5: Verify product rule: HCF × LCM = 2 × 60 = 120. Product of numbers = 6 × 20 = 120. Verified!",
                "finalAnswer": "HCF(6, 20) = 2, LCM(6, 20) = 60",
                "unit": "integers",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 3: Find the HCF of 96 and 404 by prime factorisation method. Hence, find their LCM.",
                "given": "Two integers: a = 96, b = 404.",
                "formula": "LCM(a, b) = (a × b) / HCF(a, b).",
                "substitution": "96 = 2^5 × 3; 404 = 2^2 × 101. HCF = 2^2 = 4.",
                "calculation": "Step 1: 96 = 32 × 3 = 2^5 × 3^1.\nStep 2: 404 = 4 × 101 = 2^2 × 101^1 (101 is prime).\nStep 3: Common factor is 2; smallest power is 2^2 = 4 => HCF(96, 404) = 4.\nStep 4: Use the relation LCM(a, b) = (a × b) / HCF(a, b):\nLCM = (96 × 404) / 4 = 96 × 101.\nStep 5: Scratchpad arithmetic in [ROUGH_WORK]: 96 × 101 = 96 × (100 + 1) = 9600 + 96 = 9696.",
                "finalAnswer": "HCF = 4, LCM = 9696",
                "unit": "integers",
                "has_diagram": False
            }
        ],
        "visual_lesson_plan": {
            "diagram_svg": tree_svg,
            "diagram_type": "svg",
            "what_to_make": "Prime factor tree breakdown showing composite nodes and circular prime factor leaves",
            "concept_visuals": [
                {
                    "concept_name": "Fundamental Theorem of Arithmetic",
                    "visual_type": "diagram",
                    "title": "Prime Factor Tree Decomposition",
                    "caption": "Visualizing composite number 32760 factoring into prime powers 2³ × 3² × 5 × 7 × 13"
                },
                {
                    "concept_name": "HCF and LCM Venn Intersection",
                    "visual_type": "diagram",
                    "title": "Dual-Set Prime Factor Distribution",
                    "caption": "Common factors in the intersection form HCF; union of all prime powers forms LCM"
                }
            ],
            "concept_questions": [
                {
                    "concept_name": "Prime Powers for 0 Ending",
                    "questions": [
                        {
                            "question": "Can the number 6^n end with the digit 0 for any natural number n? Explain why.",
                            "type": "conceptual",
                            "options": [
                                "No, because 6 = 2 × 3, so its prime factors never include 5",
                                "Yes, when n is a multiple of 10",
                                "Yes, for n = 0",
                                "No, because 6 is an even number"
                            ],
                            "ideal_answer": "No. For a number to end in 0, its prime factorization must contain both 2 and 5. Since 6^n = (2 × 3)^n = 2^n × 3^n, 5 is never a prime factor, so it can never end in 0.",
                            "socratic_hint": "What primes multiply to make 10?"
                        }
                    ]
                }
            ],
            "chapter_flowchart": "Composite Integer -> Prime Factorization (Factor Tree) -> HCF (Min Powers) & LCM (Max Powers) -> Verification (HCF × LCM = a × b)"
        }
    }

    # Module 2: Revisiting Irrational Numbers & Proofs by Contradiction
    m2 = {
        "order_index": 2,
        "title": "Irrational Numbers: Theorem p | a² ⇒ p | a, Rigorous Contradiction Proofs for √2, √3, √5",
        "description": "Prove Theorem 1.2 (If prime p divides a², p divides a). Master the classical proof by contradiction demonstrating that √2, √3, and √5 are irrational. Understand properties of irrational operations with rational numbers.",
        "subtopics": [
            "Formal definition of an irrational number (cannot be written as p/q with integers p, q and q != 0)",
            "Theorem 1.2: If p is a prime and p divides a², then p divides a (where a is a positive integer)",
            "Theorem 1.3: Proof that √2 is irrational using co-prime assumption and contradiction",
            "Proving √3 and √5 are irrational using the identical deductive machinery",
            "Linear combinations of rational and irrational numbers: (a + b√p, a - b√p, c√p) are irrational"
        ],
        "key_concepts": [
            "Co-Prime Invariant: Two integers a and b are co-prime if their Highest Common Factor is exactly 1 (HCF(a, b) = 1).",
            "Theorem 1.2 (Prime Divisibility): Let p be a prime number. If p divides a², then p divides a, where a is a positive integer.",
            "Proof by Contradiction Method: Assume the statement's opposite (that √2 is rational, √2 = a/b where a, b are co-prime), deduce an algebraic impossibility (that both a and b share a common factor p), and conclude that the initial assumption was false.",
            "Arithmetic Closure with Irrationals: The sum, difference, product, and quotient of a non-zero rational number and an irrational number is always irrational."
        ],
        "success_criteria": "Student can write the complete, rigorous board-exam proof for the irrationality of √2, √3, √5, and composite expressions like 3 + 2√5 without missing any logical step.",
        "chapter_notes": "Board Exam Marker Caution: Always explicitly state 'where a and b are co-prime integers and b ≠ 0' at the start of your contradiction proof. Omitting 'co-prime' loses 1 full mark in CBSE marking schemes.",
        "worked_examples": [
            {
                "problem": "Textbook Example 4 (Theorem 1.3): Prove that √2 is irrational.",
                "given": "Number √2.",
                "formula": "Proof by contradiction using Theorem 1.2: If prime p | a², then p | a.",
                "substitution": "Assume √2 = a / b, where a and b are co-prime positive integers (HCF(a, b) = 1) and b ≠ 0.",
                "calculation": "Step 1: Rearrange: b√2 = a.\nStep 2: Squaring both sides: 2b² = a²  --- (Equation 1).\nStep 3: This implies that 2 divides a².\nBy Theorem 1.2, since 2 is prime, 2 must divide a.\nStep 4: Therefore, we can write a = 2c for some integer c.\nStep 5: Substitute a = 2c into Equation 1: 2b² = (2c)² = 4c².\nDivide both sides by 2: b² = 2c².\nStep 6: This implies that 2 divides b². By Theorem 1.2, 2 must divide b.\nStep 7: From Steps 3 and 6, both a and b have 2 as a common factor.\nStep 8: But this contradicts our assumption that a and b are co-prime (HCF(a, b) = 1).\nStep 9: This contradiction has arisen because of our incorrect assumption that √2 is rational.",
                "finalAnswer": "Hence, √2 is irrational.",
                "unit": "Q.E.D. (Proved)",
                "has_diagram": True,
                "diagram_svg": irrational_svg
            },
            {
                "problem": "Textbook Example 5: Prove that √3 is irrational.",
                "given": "Number √3.",
                "formula": "Proof by contradiction: If 3 | a², then 3 | a.",
                "substitution": "Let √3 = a/b where a, b are co-prime integers (b ≠ 0).",
                "calculation": "Step 1: b√3 = a. Squaring both sides: 3b² = a²  --- (Eq 1).\nStep 2: 3 divides a², hence 3 divides a. Write a = 3c for some integer c.\nStep 3: Substitute a = 3c into Eq 1: 3b² = (3c)² = 9c² => b² = 3c².\nStep 4: 3 divides b², hence 3 divides b.\nStep 5: Thus 3 is a common factor of both a and b, contradicting the fact that HCF(a, b) = 1.\nStep 6: Hence, √3 is irrational.",
                "finalAnswer": "Hence, √3 is irrational.",
                "unit": "Q.E.D. (Proved)",
                "has_diagram": False
            },
            {
                "problem": "Textbook Example 6: Show that 5 - √3 is irrational.",
                "given": "Expression 5 - √3.",
                "formula": "Difference of rational and irrational numbers.",
                "substitution": "Assume 5 - √3 is rational: 5 - √3 = a/b (a, b are integers, b ≠ 0).",
                "calculation": "Step 1: Rearrange to isolate the radical: √3 = 5 - a/b = (5b - a) / b.\nStep 2: Since a and b are integers, (5b - a) and b are integers with b ≠ 0.\nStep 3: Therefore, (5b - a) / b is rational.\nStep 4: This implies that √3 is rational.\nStep 5: But this contradicts the well-known fact that √3 is irrational.\nStep 6: This contradiction arose from assuming 5 - √3 is rational.",
                "finalAnswer": "Therefore, 5 - √3 is irrational.",
                "unit": "Q.E.D. (Proved)",
                "has_diagram": False
            }
        ],
        "visual_lesson_plan": {
            "diagram_svg": irrational_svg,
            "diagram_type": "svg",
            "what_to_make": "Number line projection of unit right triangle hypotenuse √2 showing non-terminating irrational coordinate",
            "concept_visuals": [
                {
                    "concept_name": "Irrationality Contradiction Mechanism",
                    "visual_type": "diagram",
                    "title": "Logical Proof Contradiction Loop",
                    "caption": "Assume Rational a/b -> Deduce Common Factor p -> Violates Co-Prime Premise -> Q.E.D. Irrational"
                }
            ],
            "concept_questions": [
                {
                    "concept_name": "Divisibility Invariant",
                    "questions": [
                        {
                            "question": "If p is a prime number and p divides a², why does p necessarily divide a?",
                            "type": "conceptual",
                            "options": [
                                "By Fundamental Theorem of Arithmetic, p must be in the unique prime factorization of a",
                                "Because a² is always greater than a",
                                "Because p is an integer",
                                "Only true for p = 2 and p = 3"
                            ],
                            "ideal_answer": "By the Fundamental Theorem of Arithmetic, the prime factorization of a² consists of squares of the prime factors of a. If p divides a², p must be one of these prime factors, which means p was already present in the prime factorization of a.",
                            "socratic_hint": "Think about the prime factorization of a and what squaring it does to the exponents."
                        }
                    ]
                }
            ],
            "chapter_flowchart": "Assume √p = a/b (co-prime) -> Square: p*b² = a² -> p divides a (a=pc) -> p*b² = p²c² -> b² = pc² -> p divides b -> Contradiction! (Common factor p) -> √p is Irrational"
        }
    }

    # Module 3: Exercise 1.1 Complete Solver
    m3 = {
        "order_index": 3,
        "title": "Exercise 1.1 Solver: Prime Factorization, HCF-LCM Pair Computation & Sports Track Word Problem",
        "description": "Complete, zero-omission solutions for all 5 questions of NCERT Exercise 1.1. Express numbers as product of prime factors, compute and verify HCF and LCM for two and three integers, and solve the circular track LCM problem.",
        "subtopics": [
            "Q1: Prime factorization of 140, 156, 3825, 5005, and 7429",
            "Q2: HCF and LCM calculation and product verification for pairs (26, 91), (510, 92), (336, 54)",
            "Q3: HCF and LCM for integer triplets (12, 15, 21), (17, 23, 29), (8, 9, 25)",
            "Q4: Given HCF(306, 657) = 9, find LCM(306, 657) using formula",
            "Q5: Check whether 6^n can end with the digit 0 for any natural number n",
            "Q6: Explain why 7×11×13 + 13 and 7×6×5×4×3×2×1 + 5 are composite numbers",
            "Q7: Sonia and Ravi circular sports track LCM synchronization word problem"
        ],
        "key_concepts": [
            "Systematic Prime Factorization: Divisibility rules for 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.",
            "Composite Number Identification: A number is composite if it has factors other than 1 and itself (i.e. can be written as product of two or more integers > 1).",
            "LCM Synchronization Invariant: The time when two periodic events repeat together on a closed circuit is given by the LCM of their individual cycle times."
        ],
        "success_criteria": "Student solves all parts of Exercise 1.1 with complete arithmetic breakdown, correct SI units, and full justification.",
        "chapter_notes": "Q7 Word Problem Strategy: When two objects move at different speeds on a circular track and start at the same point and same time in the same direction, they will meet again at the starting point after time = LCM(time1, time2).",
        "worked_examples": [
            {
                "problem": "Exercise 1.1 Q1: Express each number as a product of its prime factors: (i) 140, (ii) 156, (iii) 3825, (iv) 5005, (v) 7429.",
                "given": "Numbers: 140, 156, 3825, 5005, 7429.",
                "formula": "Repeated division by prime numbers.",
                "substitution": "Successive prime division.",
                "calculation": "Part (i): 140 / 2 = 70; 70 / 2 = 35; 35 / 5 = 7; 7 / 7 = 1.\n  => 140 = 2² × 5 × 7.\nPart (ii): 156 / 2 = 78; 78 / 2 = 39; 39 / 3 = 13; 13 / 13 = 1.\n  => 156 = 2² × 3 × 13.\nPart (iii): 3825: sum of digits = 18 (divisible by 3). 3825 / 3 = 1275; 1275 / 3 = 425; 425 / 5 = 85; 85 / 5 = 17; 17 / 17 = 1.\n  => 3825 = 3² × 5² × 17.\nPart (iv): 5005: ends in 5. 5005 / 5 = 1001; 1001 / 7 = 143; 143 / 11 = 13; 13 / 13 = 1.\n  => 5005 = 5 × 7 × 11 × 13.\nPart (v): 7429: Test primes. 7429 / 17 = 437; 437 / 19 = 23; 23 / 23 = 1.\n  => 7429 = 17 × 19 × 23.",
                "finalAnswer": "(i) 2² × 5 × 7; (ii) 2² × 3 × 13; (iii) 3² × 5² × 17; (iv) 5 × 7 × 11 × 13; (v) 17 × 19 × 23",
                "unit": "prime factorizations",
                "has_diagram": False
            },
            {
                "problem": "Exercise 1.1 Q4: Given that HCF(306, 657) = 9, find LCM(306, 657).",
                "given": "a = 306, b = 657, HCF(a, b) = 9.",
                "formula": "LCM(a, b) = (a × b) / HCF(a, b).",
                "substitution": "LCM = (306 × 657) / 9.",
                "calculation": "Step 1: Simplify by dividing 306 by 9: 306 / 9 = 34.\nStep 2: Multiply 34 × 657 in [ROUGH_WORK]:\n  657 × 34 = 657 × (30 + 4) = 19710 + 2628 = 22338.",
                "finalAnswer": "LCM(306, 657) = 22338",
                "unit": "integer",
                "has_diagram": False
            },
            {
                "problem": "Exercise 1.1 Q6: Explain why 7 × 11 × 13 + 13 and 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 are composite numbers.",
                "given": "Expressions A = 7 × 11 × 13 + 13 and B = 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5.",
                "formula": "A composite number has at least one factor other than 1 and itself.",
                "substitution": "Factor out common terms.",
                "calculation": "Expression A: 7 × 11 × 13 + 13 = 13 × (7 × 11 + 1) = 13 × (77 + 1) = 13 × 78 = 13 × (2 × 3 × 13) = 2 × 3 × 13².\nSince A has factors 2, 3, and 13 other than 1 and itself, A is a composite number.\n\nExpression B: 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 = 5 × (7 × 6 × 4 × 3 × 2 × 1 + 1)\n  = 5 × (1008 + 1) = 5 × 1009.\nSince B has factors 5 and 1009 other than 1 and itself, B is a composite number.",
                "finalAnswer": "Both numbers are composite because they can each be factored into a product of multiple prime numbers > 1.",
                "unit": "proved",
                "has_diagram": False
            },
            {
                "problem": "Exercise 1.1 Q7: There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?",
                "given": "Time taken by Sonia = 18 minutes; Time taken by Ravi = 12 minutes.",
                "formula": "They meet at starting point after time = LCM(18, 12) minutes.",
                "substitution": "18 = 2 × 3²; 12 = 2² × 3.",
                "calculation": "Step 1: Prime factorisation of 18 = 2^1 × 3^2.\nStep 2: Prime factorisation of 12 = 2^2 × 3^1.\nStep 3: LCM takes the highest power of each prime:\n  LCM(18, 12) = 2^2 × 3^2 = 4 × 9 = 36.\nStep 4: Check: In 36 minutes, Sonia completes 36/18 = 2 rounds. Ravi completes 36/12 = 3 rounds. Both are exactly at the starting point!",
                "finalAnswer": "They will meet again at the starting point after 36 minutes.",
                "unit": "minutes",
                "has_diagram": False
            }
        ],
        "visual_lesson_plan": {
            "diagram_svg": tree_svg,
            "diagram_type": "svg",
            "what_to_make": "Circular track lap diagram showing Sonia and Ravi meeting at starting point at t=36 min",
            "concept_visuals": [
                {
                    "concept_name": "Circular Lap Synchronization",
                    "visual_type": "diagram",
                    "title": "Sports Track LCM Synchronization",
                    "caption": "Sonia (18 min/lap, 2 laps) and Ravi (12 min/lap, 3 laps) synchronize at 36 minutes"
                }
            ],
            "concept_questions": [
                {
                    "concept_name": "LCM Application in Real Life",
                    "questions": [
                        {
                            "question": "Why is the LCM used rather than HCF to find when two runners on a track meet at the start?",
                            "type": "conceptual",
                            "options": [
                                "Because they meet after an integer multiple of both lap times, which requires a common multiple",
                                "Because HCF is always smaller than the times",
                                "Because track distances are always round",
                                "Either HCF or LCM can be used"
                            ],
                            "ideal_answer": "Each runner arrives at the starting point only at multiples of their lap time (18, 36, 54... and 12, 24, 36, 48...). The first time both are simultaneously at the start is the Lowest Common Multiple (LCM).",
                            "socratic_hint": "List out the minutes when Sonia crosses the start line, then when Ravi does."
                        }
                    ]
                }
            ],
            "chapter_flowchart": "Given Word Problem -> Identify: Are we finding a common cycle/multiple or dividing into equal parts? -> Common Cycle = LCM -> Prime Factorization -> Compute LCM -> Boxed Answer with minutes"
        }
    }

    # Module 4: Exercise 1.2 Complete Solver
    m4 = {
        "order_index": 4,
        "title": "Exercise 1.2 Solver: Step-by-Step Proofs of Irrationality for √5, 3 + 2√5, 1/√2, 7√5, 6 + √2",
        "description": "Complete, rigorous step-by-step proofs for all questions in NCERT Exercise 1.2. Master proof by contradiction for square roots of primes and algebraic combinations with rational coefficients.",
        "subtopics": [
            "Exercise 1.2 Q1: Prove that √5 is irrational (full 9-step contradiction proof)",
            "Exercise 1.2 Q2: Prove that 3 + 2√5 is irrational using radical isolation",
            "Exercise 1.2 Q3 (i): Prove that 1/√2 is irrational",
            "Exercise 1.2 Q3 (ii): Prove that 7√5 is irrational",
            "Exercise 1.2 Q3 (iii): Prove that 6 + √2 is irrational",
            "CBSE Board Exam Marking Scheme Standards for Contradiction Proofs"
        ],
        "key_concepts": [
            "Step 1 Contradiction Premise: Always assume a/b with b ≠ 0 and HCF(a, b) = 1 (co-prime).",
            "Theorem 1.2 Application: If prime p divides a², then p divides a.",
            "Linear Combination Isolation: For expressions like a + b√p = r/s, isolate √p = (r - as)/(bs). Since RHS is rational, LHS must be rational, which contradicts the known irrationality of √p."
        ],
        "success_criteria": "Student writes verbatim, topper-level proofs for Exercise 1.2 Q1, Q2, and Q3 with zero logical omissions.",
        "chapter_notes": "Essential clause: When isolating radicals, state: 'Since a and b are integers, the RHS is a rational number. This implies that √5 is rational. But this contradicts the fact that √5 is irrational. Hence our assumption was wrong.'",
        "worked_examples": [
            {
                "problem": "Exercise 1.2 Q1: Prove that √5 is irrational.",
                "given": "Number √5.",
                "formula": "Proof by contradiction: Assume √5 is rational => √5 = a/b where a, b are co-prime positive integers, b ≠ 0.",
                "substitution": "b√5 = a.",
                "calculation": "Step 1: Squaring both sides: 5b² = a²  --- (1).\nStep 2: 5 divides a². Since 5 is prime, by Theorem 1.2, 5 divides a.\nStep 3: Write a = 5c for some integer c.\nStep 4: Substitute into (1): 5b² = (5c)² = 25c² => b² = 5c².\nStep 5: 5 divides b². Since 5 is prime, by Theorem 1.2, 5 divides b.\nStep 6: Therefore, 5 is a common factor of both a and b.\nStep 7: This contradicts our assumption that a and b are co-prime (HCF(a, b) = 1).\nStep 8: Hence, our assumption that √5 is rational is false.",
                "finalAnswer": "Therefore, √5 is irrational.",
                "unit": "Q.E.D. (Proved)",
                "has_diagram": True,
                "diagram_svg": irrational_svg
            },
            {
                "problem": "Exercise 1.2 Q2: Prove that 3 + 2√5 is irrational.",
                "given": "Expression 3 + 2√5.",
                "formula": "Radical isolation method.",
                "substitution": "Assume 3 + 2√5 is rational: 3 + 2√5 = a/b where a, b are co-prime integers, b ≠ 0.",
                "calculation": "Step 1: Subtract 3 from both sides: 2√5 = a/b - 3 = (a - 3b) / b.\nStep 2: Divide by 2 to isolate the radical: √5 = (a - 3b) / (2b).\nStep 3: Since a and b are integers, (a - 3b) and 2b are integers, with 2b ≠ 0.\nStep 4: Therefore, (a - 3b) / (2b) is a rational number.\nStep 5: This implies that √5 is rational.\nStep 6: But this contradicts the fact that √5 is irrational.\nStep 7: This contradiction arises from our incorrect assumption that 3 + 2√5 is rational.",
                "finalAnswer": "Hence, 3 + 2√5 is irrational.",
                "unit": "Q.E.D. (Proved)",
                "has_diagram": False
            },
            {
                "problem": "Exercise 1.2 Q3: Prove that the following are irrationals: (i) 1/√2, (ii) 7√5, (iii) 6 + √2.",
                "given": "Expressions: (i) 1/√2, (ii) 7√5, (iii) 6 + √2.",
                "formula": "Proof by contradiction via algebraic isolation.",
                "substitution": "Set each equal to a/b (a, b integers, b ≠ 0, co-prime).",
                "calculation": "Part (i) 1/√2 = a/b => b/a = √2. Since a, b are integers and a ≠ 0, b/a is rational. This implies √2 is rational, which contradicts the fact that √2 is irrational. Hence 1/√2 is irrational.\n\nPart (ii) 7√5 = a/b => √5 = a / (7b). Since a, b are integers, a/(7b) is rational. This implies √5 is rational, contradicting the fact that √5 is irrational. Hence 7√5 is irrational.\n\nPart (iii) 6 + √2 = a/b => √2 = a/b - 6 = (a - 6b) / b. Since a, b are integers, (a - 6b)/b is rational. This implies √2 is rational, contradicting the fact that √2 is irrational. Hence 6 + √2 is irrational.",
                "finalAnswer": "(i) 1/√2, (ii) 7√5, and (iii) 6 + √2 are all proved to be irrational.",
                "unit": "Q.E.D. (Proved)",
                "has_diagram": False
            }
        ],
        "visual_lesson_plan": {
            "diagram_svg": irrational_svg,
            "diagram_type": "svg",
            "what_to_make": "Contradiction flow diagram showing step-by-step rational isolation and proof structure",
            "concept_visuals": [
                {
                    "concept_name": "Linear Combination Proof Architecture",
                    "visual_type": "diagram",
                    "title": "Radical Isolation Logic Template",
                    "caption": "Isolating √p on LHS leaves integer fraction on RHS -> Contradicts known irrationality"
                }
            ],
            "concept_questions": [
                {
                    "concept_name": "Contradiction Logic",
                    "questions": [
                        {
                            "question": "In proving 3 + 2√5 is irrational, why do we conclude (a - 3b)/(2b) is rational?",
                            "type": "conceptual",
                            "options": [
                                "Because the set of integers is closed under subtraction and multiplication, and the denominator is non-zero",
                                "Because √5 is irrational",
                                "Because 3 and 2 are prime",
                                "It is an empirical approximation"
                            ],
                            "ideal_answer": "Since a and b are integers, a - 3b is an integer and 2b is a non-zero integer. The quotient of two integers with non-zero denominator is by definition a rational number.",
                            "socratic_hint": "What is the formal definition of a rational number?"
                        }
                    ]
                }
            ],
            "chapter_flowchart": "Expression a + b√p -> Let equal to r/s -> Rearrange: √p = (r - as)/(bs) -> RHS is rational -> Implies √p is rational -> Contradiction! -> Q.E.D. Irrational"
        }
    }

    # Module 5: Board Exam Numerical Mastery & HCF-LCM Word Problems
    m5 = {
        "order_index": 5,
        "title": "Board Exam Numerical Mastery: HCF-LCM Multi-Tier Word Problems, Minimum Room Capacity & PYQ Strategies",
        "description": "Master high-order CBSE board exam questions on Real Numbers. Solve book merchant shelf packing, room capacity optimization, bell ringing synchronization, and decimal expansion termination rules.",
        "subtopics": [
            "HCF Word Problems: Finding maximum capacity, largest tile size, maximum stack height",
            "LCM Word Problems: Traffic lights changing together, toll bells tolling at intervals",
            "Determining decimal expansion termination without actual division (q = 2^m × 5^n)",
            "Common board exam pitfalls: mixing up when to apply HCF vs LCM",
            "Top 5 authentic CBSE Board PYQs solved step-by-step with full marking scheme"
        ],
        "key_concepts": [
            "HCF Identification Rule: Used when dividing or partitioning items into the largest possible equal groups with zero remainder (words: 'maximum', 'largest', 'greatest', 'equal capacity').",
            "LCM Identification Rule: Used when finding the minimum time or distance for independent cyclic events to synchronize (words: 'minimum', 'smallest', 'meet together', 'toll together').",
            "Decimal Termination Theorem: A rational number p/q in simplest form (HCF(p,q)=1) has a terminating decimal expansion if and only if the prime factorization of q is of the form 2^n × 5^m, where n, m are non-negative integers."
        ],
        "success_criteria": "Student instantly classifies word problems as HCF or LCM, computes correct values, and analyzes decimal termination using prime power exponents.",
        "chapter_notes": "Board Numerical Rule: Always state the unit in word problems (e.g. '36 minutes', '12 containers', '42 tiles'). An answer without units loses half a mark.",
        "worked_examples": [
            {
                "problem": "CBSE Board PYQ: An army contingent of 616 members is to march behind an army band of 32 members in a parade. The two groups are to march in the same number of columns. What is the maximum number of columns in which they can march?",
                "given": "Contingent members = 616; Band members = 32. Both march in equal number of columns.",
                "formula": "Maximum number of columns = HCF(616, 32).",
                "substitution": "616 = 2³ × 7 × 11; 32 = 2⁵.",
                "calculation": "Step 1: Identify that 'maximum number of columns' dividing both 616 and 32 equally requires HCF.\nStep 2: Prime factorise 32: 32 = 2 × 2 × 2 × 2 × 2 = 2⁵.\nStep 3: Prime factorise 616: 616 / 2 = 308; 308 / 2 = 154; 154 / 2 = 77; 77 / 7 = 11; 11 / 11 = 1.\n  => 616 = 2³ × 7 × 11.\nStep 4: Find common prime factors with smallest powers:\n  HCF(616, 32) = 2³ = 8.\nStep 5: Verify: 616 / 8 = 77 rows per column for contingent; 32 / 8 = 4 rows per column for band. Perfect!",
                "finalAnswer": "The maximum number of columns in which they can march is 8.",
                "unit": "columns",
                "has_diagram": False
            },
            {
                "problem": "CBSE Board PYQ: Three bells toll at intervals of 9, 12, 15 minutes respectively. If they start tolling together, after what time will they next toll together?",
                "given": "Intervals: 9 minutes, 12 minutes, 15 minutes.",
                "formula": "Bells toll together after time = LCM(9, 12, 15) minutes.",
                "substitution": "9 = 3²; 12 = 2² × 3; 15 = 3 × 5.",
                "calculation": "Step 1: 9 = 3².\nStep 2: 12 = 2² × 3¹.\nStep 3: 15 = 3¹ × 5¹.\nStep 4: LCM takes highest powers: 2² × 3² × 5¹ = 4 × 9 × 5 = 180 minutes.\nStep 5: Convert to hours in [ROUGH_WORK]: 180 / 60 = 3 hours.",
                "finalAnswer": "The bells will toll together after 180 minutes (or 3 hours).",
                "unit": "minutes (3 hours)",
                "has_diagram": False
            },
            {
                "problem": "CBSE Board PYQ: A sweet seller has 420 kaju barfis and 130 badam barfis. She wants to stack them in such a way that each stack has the same number, and they take up the least area of the tray. What is the number of barfis that can be placed in each stack for this purpose?",
                "given": "420 kaju barfis, 130 badam barfis.",
                "formula": "Stack size = HCF(420, 130).",
                "substitution": "420 = 2² × 3 × 5 × 7; 130 = 2 × 5 × 13.",
                "calculation": "Step 1: To take least area, each stack must have the maximum possible number of barfis.\nStep 2: Maximum number in each stack = HCF(420, 130).\nStep 3: 420 = 10 × 42 = (2 × 5) × (2 × 3 × 7) = 2² × 3 × 5 × 7.\nStep 4: 130 = 10 × 13 = 2 × 5 × 13.\nStep 5: Common prime factors with smallest powers: 2¹ × 5¹ = 10.\nStep 6: Total stacks: 420/10 = 42 stacks of kaju barfi, 130/10 = 13 stacks of badam barfi. Total 55 stacks.",
                "finalAnswer": "10 barfis can be placed in each stack.",
                "unit": "barfis per stack",
                "has_diagram": False
            }
        ],
        "visual_lesson_plan": {
            "diagram_svg": tree_svg,
            "diagram_type": "svg",
            "what_to_make": "Dual column comparison diagram contrasting HCF partitioning vs LCM synchronization",
            "concept_visuals": [
                {
                    "concept_name": "HCF vs LCM Decision Tree",
                    "visual_type": "diagram",
                    "title": "Word Problem Classification Algorithm",
                    "caption": "Keywords 'Maximum / Divide / Equal Containers' -> HCF. Keywords 'Synchronize / Repeat / Smallest' -> LCM."
                }
            ],
            "concept_questions": [
                {
                    "concept_name": "Word Problem Strategy",
                    "questions": [
                        {
                            "question": "A merchant wants to pack 120 litres of oil A and 180 litres of oil B into equal containers without mixing. Why must the container capacity be HCF(120, 180)?",
                            "type": "conceptual",
                            "options": [
                                "The container capacity must divide both 120 and 180 exactly, and to minimize containers, the capacity must be the largest common factor",
                                "Because oil density requires LCM",
                                "Because 180 is larger than 120",
                                "Because HCF is always equal to 60"
                            ],
                            "ideal_answer": "Each container must completely divide both quantities without remainder. To use the minimum number of containers, each container must hold the maximum possible volume, which is the Highest Common Factor (HCF).",
                            "socratic_hint": "How do you minimize the number of containers while keeping them equal?"
                        }
                    ]
                }
            ],
            "chapter_flowchart": "Read Problem -> Extract Quantities -> Check: Equal Partitioning (HCF) or Cyclic Repetition (LCM) -> Prime Factorization -> Compute Value -> Write Answer with SI Units"
        }
    }

    CURRICULUM_ID = "4f230f16-2470-4304-b7cd-4aeacbc51831"
    for m in [m1, m2, m3, m4, m5]:
        m["curriculum_id"] = CURRICULUM_ID
        m["class_level"] = "Class 10"
        m["board"] = "CBSE"
        m["estimated_minutes"] = 25

    return [m1, m2, m3, m4, m5]

if __name__ == "__main__":
    mods = get_ch1_modules()
    print(f"Generated {len(mods)} modules for Chapter 1: Real Numbers")
    for m in mods:
        print(f"  [Mod {m['order_index']}] {m['title']} ({len(m['worked_examples'])} worked examples)")
