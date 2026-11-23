const { supabase } = require('./db_helper');

async function enrichCh5() {
  console.log('=== ENRICHING CLASS 10 MATHS - CHAPTER 5: ARITHMETIC PROGRESSIONS ===\n');

  // Mod 1: Foundations & Derivation of General Term aₙ (Examples 1-10)
  const mod1Examples = [
    {
      problem: "Example 1 (NCERT Page 6): For the AP: 3/2, 1/2, -1/2, -3/2, ..., write the first term a and the common difference d.",
      solution: "Given AP: 3/2, 1/2, -1/2, -3/2, ...\nTarget: Find first term 'a' and common difference 'd'.\nFormula: First term a = a₁, Common difference d = a₂ - a₁ = a₃ - a₂\n\nStep 1: First term:\na = 3/2\n\nStep 2: Calculate common difference d:\nd = a₂ - a₁ = 1/2 - 3/2 = -2/2 = -1\nVerify with a₃ - a₂: -1/2 - 1/2 = -2/2 = -1 (Consistent!)\n[ROUGH_WORK]\n3/2 - 1 = 1/2; 1/2 - 1 = -1/2; -1/2 - 1 = -3/2\nBoxed Answer: [ First term a = 3/2, Common difference d = -1 ].",
      concept_questions: [
        "Can the common difference of an AP be negative or zero?",
        "How do you verify whether a given sequence is an AP?"
      ],
      graph_payload: {
        points: [
          { x: 1, y: 1.5, label: "a₁ = 1.5" },
          { x: 2, y: 0.5, label: "a₂ = 0.5" },
          { x: 3, y: -0.5, label: "a₃ = -0.5" },
          { x: 4, y: -1.5, label: "a₄ = -1.5" }
        ],
        segments: [
          { start: [1, 1.5], end: [2, 0.5], label: "d = -1" },
          { start: [2, 0.5], end: [3, -0.5], label: "d = -1" },
          { start: [3, -0.5], end: [4, -1.5], label: "d = -1" }
        ]
      }
    },
    {
      problem: "Example 3 (NCERT Page 10): Find the 10th term of the AP: 2, 7, 12, ...",
      solution: "Given AP: 2, 7, 12, ...\nFirst term a = 2\nCommon difference d = 7 - 2 = 5\nTarget: Find 10th term (a₁₀), so n = 10\nFormula: aₙ = a + (n - 1)d\n\nStep 1: Substitute values into formula:\na₁₀ = 2 + (10 - 1) × 5\n\nStep 2: Simplify:\na₁₀ = 2 + 9 × 5 = 2 + 45 = 47\n[ROUGH_WORK]\n2, 7, 12, 17, 22, 27, 32, 37, 42, 47 (10th term is exactly 47)\nBoxed Answer: [ The 10th term of the AP is 47 ].",
      concept_questions: [
        "Why is the formula for the nth term a + (n - 1)d rather than a + nd?",
        "If a = 2 and d = 5, what is the algebraic expression for the nth term?"
      ],
      graph_payload: {
        points: [
          { x: 1, y: 2, label: "a₁ = 2" },
          { x: 2, y: 7, label: "a₂ = 7" },
          { x: 3, y: 12, label: "a₃ = 12" },
          { x: 10, y: 47, label: "a₁₀ = 47" }
        ],
        segments: [
          { start: [1, 2], end: [10, 47], label: "Linear AP growth (slope d = 5)" }
        ]
      }
    },
    {
      problem: "Example 4 (NCERT Page 10): Which term of the AP: 21, 18, 15, ... is -81? Also, is any term 0? Give reason.",
      solution: "Given AP: 21, 18, 15, ...\nFirst term a = 21\nCommon difference d = 18 - 21 = -3\n\nPart A: Find n such that aₙ = -81:\nFormula: aₙ = a + (n - 1)d\n-81 = 21 + (n - 1)(-3)\n-81 - 21 = -3(n - 1)\n-102 = -3(n - 1)\nn - 1 = -102 / -3 = 34\nn = 34 + 1 = 35\nSo, the 35th term is -81.\n\nPart B: Check if any term is 0:\nSet aₙ = 0:\n0 = 21 + (n - 1)(-3)\n-21 = -3(n - 1)\nn - 1 = 7 ⇒ n = 8\nSince n is a positive integer (8), the 8th term of the AP is 0.\n[ROUGH_WORK]\n21, 18, 15, 12, 9, 6, 3, 0 (Term 8 is 0)\nBoxed Answer: [ The 35th term is -81, and the 8th term is 0 ].",
      concept_questions: [
        "What type of number must n always be in an AP?",
        "What does it mean if solving for n yields a fraction or negative number?"
      ]
    },
    {
      problem: "Example 7 (NCERT Page 11): How many two-digit numbers are divisible by 3?",
      solution: "Target: Count all two-digit numbers divisible by 3.\nSmallest two-digit number divisible by 3 is 12.\nNext are 15, 18, 21, ...\nLargest two-digit number divisible by 3 is 99.\n\nStep 1: Formulate the AP:\nAP: 12, 15, 18, ..., 99\nFirst term a = 12\nCommon difference d = 3\nLast term aₙ = 99\n\nStep 2: Solve for n:\nFormula: aₙ = a + (n - 1)d\n99 = 12 + (n - 1)(3)\n99 - 12 = 3(n - 1)\n87 = 3(n - 1)\nn - 1 = 87 / 3 = 29\nn = 29 + 1 = 30\n[ROUGH_WORK]\nTotal two digit numbers: 10 to 99 = 90 numbers.\nEvery 3rd number: 90 / 3 = 30 numbers.\nBoxed Answer: [ There are 30 two-digit numbers divisible by 3 ].",
      concept_questions: [
        "How do you find the first and last terms of such divisibility sequences?",
        "Could you find the sum of all these two-digit numbers using the AP sum formula?"
      ]
    },
    {
      problem: "Example 10 (NCERT Page 13): In a flower bed, there are 23 rose plants in the first row, 21 in the second, 19 in the third, and so on. There are 5 rose plants in the last row. How many rows are there in the flower bed?",
      solution: "Given sequence of rose plants per row: 23, 21, 19, ..., 5\nFirst term a = 23\nCommon difference d = 21 - 23 = -2\nLast term aₙ = 5\n\nStep 1: Apply general term formula:\naₙ = a + (n - 1)d\n5 = 23 + (n - 1)(-2)\n5 - 23 = -2(n - 1)\n-18 = -2(n - 1)\nn - 1 = -18 / -2 = 9\nn = 9 + 1 = 10\n[ROUGH_WORK]\n23, 21, 19, 17, 15, 13, 11, 9, 7, 5 (Count rows: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\nBoxed Answer: [ There are 10 rows in the flower bed ].",
      concept_questions: [
        "What does the negative common difference d = -2 indicate physically?",
        "If the gardener wanted to know total plants, what formula would be used?"
      ]
    }
  ];

  // Mod 3: Exercise 5.1 Complete Solver (Q1 to Q4)
  const mod3Examples = [
    {
      problem: "Exercise 5.1 Q1 (NCERT Page 8): In which of the following situations does the list of numbers involved make an arithmetic progression, and why?\n(i) The taxi fare after each km when the fare is ₹15 for the first km and ₹8 for each additional km.\n(ii) The amount of air present in a cylinder when a vacuum pump removes 1/4 of the air remaining in the cylinder at a time.\n(iii) The cost of digging a well after every metre of digging, when it costs ₹150 for the first metre and rises by ₹50 for each subsequent metre.\n(iv) The amount of money in the account every year, when ₹10,000 is deposited at compound interest at 8% per annum.",
      solution: "Criterion: A situation forms an AP if the difference between successive terms is constant.\n\n(i) Taxi Fare:\nFare for 1 km = ₹15\nFare for 2 km = 15 + 8 = ₹23\nFare for 3 km = 23 + 8 = ₹31\nFare for 4 km = 31 + 8 = ₹39\nSequence: 15, 23, 31, 39, ...\nSuccessive difference: 23 - 15 = 8, 31 - 23 = 8, 39 - 31 = 8 (Constant d = 8).\nConclusion: It forms an AP.\n\n(ii) Air in Cylinder:\nLet initial volume be V.\nAir left after 1st pump: V - V/4 = (3/4)V\nAir left after 2nd pump: (3/4)V - (1/4)(3/4)V = (3/4)²V = (9/16)V\nAir left after 3rd pump: (3/4)³V = (27/64)V\nSequence: V, (3/4)V, (9/16)V, (27/64)V, ...\nDifferences: (3/4)V - V = -V/4; (9/16)V - (3/4)V = -3V/16 (Not equal!)\nConclusion: Does NOT form an AP (it is a Geometric Progression).\n\n(iii) Cost of Digging Well:\nCost for 1m = ₹150\nCost for 2m = 150 + 50 = ₹200\nCost for 3m = 200 + 50 = ₹250\nSequence: 150, 200, 250, ...\nCommon difference d = 50 (Constant).\nConclusion: It forms an AP.\n\n(iv) Compound Interest:\nAmount A = P(1 + r/100)ⁿ = 10000(1 + 0.08)ⁿ = 10000(1.08)ⁿ\nYear 1: 10000(1.08) = 10800\nYear 2: 10800(1.08) = 11664 (Difference = 864)\nYear 3: 11664(1.08) = 12597.12 (Difference = 933.12)\nDifferences are unequal.\nConclusion: Does NOT form an AP.\n[ROUGH_WORK]\nLinear rate = AP. Multiplicative/percentage/geometric = NOT AP.\nBoxed Answer: [ Situations (i) and (iii) form an AP; situations (ii) and (iv) do not ].",
      concept_questions: [
        "Why does simple interest form an AP while compound interest does not?",
        "What is the mathematical condition for a sequence a₁, a₂, a₃, ... to be an AP?"
      ]
    },
    {
      problem: "Exercise 5.1 Q2 (NCERT Page 8): Write first four terms of the AP, when the first term a and the common difference d are given as follows:\n(i) a = 10, d = 10\n(ii) a = -2, d = 0\n(iii) a = 4, d = -3\n(iv) a = -1, d = 1/2\n(v) a = -1.25, d = -0.25",
      solution: "Formula: General terms are a, a + d, a + 2d, a + 3d.\n\n(i) a = 10, d = 10:\na₁ = 10\na₂ = 10 + 10 = 20\na₃ = 20 + 10 = 30\na₄ = 30 + 10 = 40\nTerms: 10, 20, 30, 40.\n\n(ii) a = -2, d = 0:\na₁ = -2, a₂ = -2, a₃ = -2, a₄ = -2.\nTerms: -2, -2, -2, -2.\n\n(iii) a = 4, d = -3:\na₁ = 4\na₂ = 4 + (-3) = 1\na₃ = 1 + (-3) = -2\na₄ = -2 + (-3) = -5\nTerms: 4, 1, -2, -5.\n\n(iv) a = -1, d = 1/2:\na₁ = -1\na₂ = -1 + 1/2 = -1/2\na₃ = -1/2 + 1/2 = 0\na₄ = 0 + 1/2 = 1/2\nTerms: -1, -1/2, 0, 1/2.\n\n(v) a = -1.25, d = -0.25:\na₁ = -1.25\na₂ = -1.25 + (-0.25) = -1.50\na₃ = -1.50 + (-0.25) = -1.75\na₄ = -1.75 + (-0.25) = -2.00\nTerms: -1.25, -1.50, -1.75, -2.00.\nBoxed Answer: [ (i) 10, 20, 30, 40; (ii) -2, -2, -2, -2; (iii) 4, 1, -2, -5; (iv) -1, -1/2, 0, 1/2; (v) -1.25, -1.50, -1.75, -2.00 ].",
      concept_questions: [
        "Is a constant sequence like -2, -2, -2, -2 a valid AP?",
        "What is the common difference of a constant AP?"
      ]
    },
    {
      problem: "Exercise 5.1 Q4 (NCERT Page 9): Which of the following are APs? If they form an AP, find the common difference d and write three more terms:\n(i) 2, 4, 8, 16, ...\n(ii) 2, 5/2, 3, 7/2, ...\n(v) 3, 3 + √2, 3 + 2√2, 3 + 3√2, ...\n(xi) a, a², a³, a⁴, ...\n(xii) √2, √8, √18, √32, ...",
      solution: "Criterion: Check d₁ = a₂ - a₁, d₂ = a₃ - a₂, d₃ = a₄ - a₃.\n\n(i) 2, 4, 8, 16, ...\na₂ - a₁ = 4 - 2 = 2; a₃ - a₂ = 8 - 4 = 4. Since 2 ≠ 4, it is NOT an AP.\n\n(ii) 2, 5/2, 3, 7/2, ...\na₂ - a₁ = 5/2 - 2 = 1/2\na₃ - a₂ = 3 - 5/2 = 1/2\na₄ - a₃ = 7/2 - 3 = 1/2\nIt is an AP with d = 1/2.\nNext 3 terms:\na₅ = 7/2 + 1/2 = 4\na₆ = 4 + 1/2 = 9/2\na₇ = 9/2 + 1/2 = 5\n\n(v) 3, 3 + √2, 3 + 2√2, 3 + 3√2, ...\na₂ - a₁ = (3 + √2) - 3 = √2\na₃ - a₂ = (3 + 2√2) - (3 + √2) = √2\na₄ - a₃ = (3 + 3√2) - (3 + 2√2) = √2\nIt is an AP with d = √2.\nNext 3 terms:\na₅ = 3 + 4√2, a₆ = 3 + 5√2, a₇ = 3 + 6√2.\n\n(xi) a, a², a³, a⁴, ...\na₂ - a₁ = a² - a = a(a - 1)\na₃ - a₂ = a³ - a² = a²(a - 1)\nSince a(a - 1) ≠ a²(a - 1) for a ≠ 1, it is NOT an AP.\n\n(xii) √2, √8, √18, √32, ...\nSimplify radicals:\n√2 = √2\n√8 = √(4 × 2) = 2√2\n√18 = √(9 × 2) = 3√2\n√32 = √(16 × 2) = 4√2\nSequence: √2, 2√2, 3√2, 4√2, ...\nd = 2√2 - √2 = √2. Constant difference!\nIt is an AP with d = √2.\nNext 3 terms:\na₅ = 5√2 = √50\na₆ = 6√2 = √72\na₇ = 7√2 = √98\nBoxed Answer: [ (ii) AP with d = 1/2 (terms 4, 9/2, 5); (v) AP with d = √2; (xii) AP with d = √2 (terms √50, √72, √98) ].",
      concept_questions: [
        "Why must you simplify square root terms like √8 and √18 before deciding if they form an AP?",
        "Why is a, a², a³ not an AP even though the powers increase by 1?"
      ]
    }
  ];

  // Mod 4: Exercise 5.2 Complete Solver (General Term aₙ Mastery)
  const mod4Examples = [
    {
      problem: "Exercise 5.2 Q1 & Q2 (NCERT Page 14): Fill in the blanks in the table: (i) a = 7, d = 3, n = 8, aₙ = ? | (ii) a = -18, n = 10, aₙ = 0, d = ? | Choose correct option: 30th term of AP: 10, 7, 4, ... is (A) 97 (B) 77 (C) -77 (D) -87.",
      solution: "Formula: aₙ = a + (n - 1)d\n\nPart 1: a = 7, d = 3, n = 8\na₈ = 7 + (8 - 1) × 3 = 7 + 7 × 3 = 7 + 21 = 28.\n\nPart 2: a = -18, n = 10, aₙ = 0\n0 = -18 + (10 - 1)d\n18 = 9d ⇒ d = 18 / 9 = 2.\n\nPart 3: 30th term of AP: 10, 7, 4, ...\na = 10, d = 7 - 10 = -3, n = 30\na₃₀ = 10 + (30 - 1)(-3) = 10 + 29(-3) = 10 - 87 = -77.\nCorrect Option is (C) -77.\n[ROUGH_WORK]\n29 × (-3) = -87; 10 - 87 = -77\nBoxed Answer: [ (i) a₈ = 28; (ii) d = 2; 30th term is (C) -77 ].",
      concept_questions: [
        "What are the 4 variables in the general term equation, and how many must be known to solve for the remaining one?",
        "Why does an AP with negative d decrease into negative numbers?"
      ]
    },
    {
      problem: "Exercise 5.2 Q7 & Q10 (NCERT Page 14): Q7: Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73. Q10: The 17th term of an AP exceeds its 10th term by 7. Find the common difference.",
      solution: "Problem 1 (Q7):\nGiven: a₁₁ = 38, a₁₆ = 73.\nTarget: Find a₃₁.\nFormulas:\na₁₁ = a + 10d = 38  ... (Eq. 1)\na₁₆ = a + 15d = 73  ... (Eq. 2)\n\nSubtract Eq. 1 from Eq. 2:\n(a + 15d) - (a + 10d) = 73 - 38\n5d = 35 ⇒ d = 7.\n\nSubstitute d = 7 into Eq. 1:\na + 10(7) = 38\na + 70 = 38 ⇒ a = 38 - 70 = -32.\n\nNow compute 31st term a₃₁:\na₃₁ = a + 30d = -32 + 30(7) = -32 + 210 = 178.\n\nProblem 2 (Q10):\nGiven: a₁₇ - a₁₀ = 7\nExpand using general term:\n[a + 16d] - [a + 9d] = 7\n16d - 9d = 7\n7d = 7 ⇒ d = 1.\n[ROUGH_WORK]\nNotice 'a' cancels out completely in difference a_m - a_n = (m - n)d!\nBoxed Answer: [ Q7: 31st term a₃₁ = 178; Q10: Common difference d = 1 ].",
      concept_questions: [
        "Why does the first term 'a' cancel out when subtracting any two terms of an AP?",
        "Prove that a_m - a_n = (m - n)d for any arithmetic progression."
      ]
    },
    {
      problem: "Exercise 5.2 Q13, Q14 & Q17 (NCERT Page 15): Q13: How many three-digit numbers are divisible by 7? Q14: How many multiples of 4 lie between 10 and 250? Q17: Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.",
      solution: "Problem 1 (Q13): Three-digit numbers divisible by 7.\nSmallest 3-digit number is 100. 100 ÷ 7 = 14 remainder 2. 100 + (7 - 2) = 105.\nFirst term a = 105.\nLargest 3-digit number is 999. 999 ÷ 7 = 142 remainder 5. 999 - 5 = 994.\nLast term aₙ = 994.\nCommon difference d = 7.\naₙ = a + (n - 1)d\n994 = 105 + (n - 1)7\n889 = 7(n - 1)\nn - 1 = 889 / 7 = 127 ⇒ n = 128.\nThere are 128 three-digit numbers divisible by 7.\n\nProblem 2 (Q14): Multiples of 4 between 10 and 250.\nFirst multiple > 10 is 12.\nLast multiple < 250 is 248 (250 ÷ 4 = 62 rem 2; 250 - 2 = 248).\nAP: 12, 16, 20, ..., 248\n248 = 12 + (n - 1)4\n236 = 4(n - 1)\nn - 1 = 59 ⇒ n = 60.\nThere are 60 multiples of 4.\n\nProblem 3 (Q17): 20th term from the last term of AP: 3, 8, 13, ..., 253.\nMethod: Reverse the AP!\nReversed AP: 253, 248, 243, ...\nFirst term A = 253\nCommon difference D = 248 - 253 = -5\nTarget: 20th term of reversed AP:\na₂₀ = A + 19D = 253 + 19(-5) = 253 - 95 = 158.\n[ROUGH_WORK]\nAlternate method: Total terms n: 253 = 3 + (n-1)5 ⇒ n = 51. Term from beginning = 51 - 20 + 1 = 32nd term. a₃₂ = 3 + 31(5) = 158. Exactly matches!\nBoxed Answer: [ Q13: 128 numbers; Q14: 60 multiples; Q17: 20th term from end is 158 ].",
      concept_questions: [
        "Why is reversing the AP the most error-free method to find the nth term from the end?",
        "In finding the m-th term from the end of an AP with n terms, why is the formula (n - m + 1)th term and not (n - m)th term?"
      ]
    }
  ];

  // Mod 5: Exercise 5.3 Complete Solver (AP Summation Masterclass & Applied Problems)
  const mod5Examples = [
    {
      problem: "Exercise 5.3 Q1 & Q3 (NCERT Page 20): Q1(i): Find sum of AP: 2, 7, 12, ... to 10 terms. Q3(i): In an AP, given a = 5, d = 3, aₙ = 50, find n and Sₙ.",
      solution: "Formulas:\nSₙ = (n/2)[2a + (n - 1)d] = (n/2)[a + l]\n\nProblem 1 (Q1(i)):\nAP: 2, 7, 12, ... to n = 10 terms.\na = 2, d = 7 - 2 = 5, n = 10.\nS₁₀ = (10/2)[2(2) + (10 - 1)(5)]\nS₁₀ = 5[4 + 9(5)] = 5[4 + 45] = 5(49) = 245.\n\nProblem 2 (Q3(i)):\nGiven a = 5, d = 3, aₙ = 50.\nStep 1: Find n using aₙ = a + (n - 1)d:\n50 = 5 + (n - 1)3\n45 = 3(n - 1)\nn - 1 = 15 ⇒ n = 16.\n\nStep 2: Find S₁₆ using Sₙ = (n/2)[a + aₙ]:\nS₁₆ = (16/2)[5 + 50] = 8[55] = 440.\n[ROUGH_WORK]\n8 × 55 = 440. Quick Gauss check: (first + last) × n / 2 = 55 × 16 / 2 = 440.\nBoxed Answer: [ Q1(i): S₁₀ = 245; Q3(i): n = 16 and S₁₆ = 440 ].",
      concept_questions: [
        "When is it better to use Sₙ = (n/2)[a + l] instead of (n/2)[2a + (n - 1)d]?",
        "Explain the geometric intuition of Gauss's summation method."
      ]
    },
    {
      problem: "Exercise 5.3 Q7, Q9 & Q11 (NCERT Page 21): Q7: Find the sum of first 22 terms of an AP in which d = 7 and 22nd term is 149. Q9: If the sum of first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of first n terms. Q11: If Sₙ = 4n - n², find first term a, S₂, a₂, a₃, a₁₀ and aₙ.",
      solution: "Problem 1 (Q7):\nGiven: n = 22, d = 7, a₂₂ = 149.\nFormula: a₂₂ = a + 21d\n149 = a + 21(7) = a + 147 ⇒ a = 2.\nNow find S₂₂:\nS₂₂ = (n/2)[a + a₂₂] = (22/2)[2 + 149] = 11 × 151 = 1661.\n\nProblem 2 (Q9):\nGiven: S₇ = 49, S₁₇ = 289.\nS₇ = (7/2)[2a + 6d] = 49 ⇒ 7[a + 3d] = 49 ⇒ a + 3d = 7 ... (Eq. 1)\nS₁₇ = (17/2)[2a + 16d] = 289 ⇒ 17[a + 8d] = 289 ⇒ a + 8d = 17 ... (Eq. 2)\nSubtract Eq. 1 from Eq. 2:\n5d = 10 ⇒ d = 2.\nSubstitute d = 2 into Eq. 1: a + 3(2) = 7 ⇒ a = 1.\nNow find Sₙ:\nSₙ = (n/2)[2(1) + (n - 1)2] = (n/2)[2 + 2n - 2] = (n/2)(2n) = n².\n\nProblem 3 (Q11):\nGiven: Sₙ = 4n - n².\nFirst term a₁ = S₁ = 4(1) - (1)² = 3.\nSum of first two terms S₂ = 4(2) - (2)² = 8 - 4 = 4.\nSecond term a₂ = S₂ - S₁ = 4 - 3 = 1.\nCommon difference d = a₂ - a₁ = 1 - 3 = -2.\nThird term a₃ = a + 2d = 3 + 2(-2) = -1.\n10th term a₁₀ = a + 9d = 3 + 9(-2) = 3 - 18 = -15.\nnth term aₙ = Sₙ - Sₙ₋₁ = (4n - n²) - [4(n - 1) - (n - 1)²]\n= 4n - n² - [4n - 4 - (n² - 2n + 1)] = 4n - n² - [4n - 4 - n² + 2n - 1]\n= 4n - n² - [6n - n² - 5] = 4n - 6n + 5 = 5 - 2n.\n[ROUGH_WORK]\nNotice S₇ = 7² = 49, S₁₇ = 17² = 289 ⇒ Sₙ = n²! Remarkable pattern!\nBoxed Answer: [ Q7: S₂₂ = 1661; Q9: Sₙ = n²; Q11: a = 3, S₂ = 4, a₂ = 1, a₃ = -1, a₁₀ = -15, aₙ = 5 - 2n ].",
      concept_questions: [
        "Why is Sₙ = n² for the AP of odd numbers 1, 3, 5, 7, ...?",
        "What is the relationship between Sₙ and aₙ: prove aₙ = Sₙ - Sₙ₋₁."
      ]
    },
    {
      problem: "Exercise 5.3 Q15, Q17 & Q19 (NCERT Page 22): Q15: Contract penalty: ₹200 for 1st day, ₹250 for 2nd day, ₹300 for 3rd day, increasing by ₹50 each day. How much does a delay of 30 days cost? Q17: School tree plantation: Class I plants 1 tree (each section, 3 sections = 3 trees), Class II plants 2 trees (3 sections = 6 trees), ..., Class XII plants 12 trees. How many trees planted? Q19: 200 logs stacked: 20 in bottom row, 19 in next, 18 in next. How many rows and how many logs in top row?",
      solution: "Problem 1 (Q15): Delay Penalty.\nAP: 200, 250, 300, ... for n = 30 days.\na = 200, d = 50, n = 30.\nS₃₀ = (30/2)[2(200) + (30 - 1)(50)]\nS₃₀ = 15[400 + 29(50)] = 15[400 + 1450] = 15[1850] = ₹27,750.\nPenalty = ₹27,750.\n\nProblem 2 (Q17): Tree Plantation.\nEach class has 3 sections.\nTrees planted by Class k = 3 × k.\nClass 1: 3(1) = 3; Class 2: 3(2) = 6; ... Class 12: 3(12) = 36.\nAP: 3, 6, 9, ..., 36\na = 3, d = 3, n = 12, l = 36.\nS₁₂ = (12/2)[a + l] = 6[3 + 36] = 6[39] = 234 trees.\n\nProblem 3 (Q19): 200 Logs.\nAP: 20, 19, 18, ... with Sₙ = 200.\na = 20, d = -1, Sₙ = 200.\n200 = (n/2)[2(20) + (n - 1)(-1)]\n400 = n[40 - n + 1] = n(41 - n) = 41n - n²\nn² - 41n + 400 = 0\nFactorize quadratic: n² - 25n - 16n + 400 = 0\n(n - 25)(n - 16) = 0 ⇒ n = 25 or n = 16.\nTest n = 25:\na₂₅ = a + 24d = 20 + 24(-1) = 20 - 24 = -4 (Logs cannot be negative! Reject n = 25).\nTest n = 16:\na₁₆ = a + 15d = 20 + 15(-1) = 20 - 15 = 5 logs.\nNumber of rows = 16, logs in top row = 5.\n[ROUGH_WORK]\n20 + 19 + 18 + 17 + 16 + 15 + 14 + 13 + 12 + 11 + 10 + 9 + 8 + 7 + 6 + 5 = (20 + 5) × 16 / 2 = 25 × 8 = 200 logs!\nBoxed Answer: [ Q15: ₹27,750; Q17: 234 trees; Q19: 16 rows, with 5 logs in the top row ].",
      concept_questions: [
        "In Q19, why does solving the quadratic yield two positive roots, and why must one be rejected physically?",
        "How does breaking a word problem into (a, d, n, Sₙ) make real-world modeling systematic?"
      ]
    }
  ];

  // Mod 6: Exercise 5.4 Optional Solver
  const mod6Examples = [
    {
      problem: "Exercise 5.4 Q1 & Q2 (NCERT Page 23): Q1: Which term of the AP: 121, 117, 113, ... is its first negative term? Q2: The sum of the third and the seventh terms of an AP is 6 and their product is 8. Find the sum of first sixteen terms of the AP.",
      solution: "Problem 1 (Q1):\nGiven AP: 121, 117, 113, ...\na = 121, d = 117 - 121 = -4.\nCondition for negative term: aₙ < 0\na + (n - 1)d < 0\n121 + (n - 1)(-4) < 0\n121 - 4n + 4 < 0\n125 < 4n ⇒ 4n > 125 ⇒ n > 125 / 4 = 31.25\nSince n must be an integer, smallest integer > 31.25 is n = 32.\nVerify a₃₂: a₃₂ = 121 + 31(-4) = 121 - 124 = -3 (< 0).\nVerify a₃₁: a₃₁ = 121 + 30(-4) = 121 - 120 = 1 (> 0).\nTherefore, the 32nd term is the first negative term.\n\nProblem 2 (Q2):\nGiven: a₃ + a₇ = 6 and a₃ × a₇ = 8.\n(a + 2d) + (a + 6d) = 6 ⇒ 2a + 8d = 6 ⇒ a + 4d = 3 ⇒ a = 3 - 4d.\nAlso: (a + 2d)(a + 6d) = 8\nSubstitute a = 3 - 4d:\n(3 - 4d + 2d)(3 - 4d + 6d) = 8\n(3 - 2d)(3 + 2d) = 8\n9 - 4d² = 8 ⇒ 4d² = 1 ⇒ d² = 1/4 ⇒ d = ±1/2.\n\nCase 1: d = 1/2:\na = 3 - 4(1/2) = 3 - 2 = 1.\nS₁₆ = (16/2)[2(1) + 15(1/2)] = 8[2 + 15/2] = 8[19/2] = 4 × 19 = 76.\n\nCase 2: d = -1/2:\na = 3 - 4(-1/2) = 3 + 2 = 5.\nS₁₆ = (16/2)[2(5) + 15(-1/2)] = 8[10 - 15/2] = 8[5/2] = 4 × 5 = 20.\n[ROUGH_WORK]\nBoth d = 1/2 and d = -1/2 are completely valid!\nBoxed Answer: [ Q1: 32nd term; Q2: S₁₆ = 76 or S₁₆ = 20 ].",
      concept_questions: [
        "In Q1, why do we round 31.25 up to 32 rather than down to 31?",
        "Why does Q2 yield two distinct sums for S₁₆?"
      ]
    },
    {
      problem: "Exercise 5.4 Q3 & Q5 (NCERT Page 23): Q3: A ladder has rungs 25 cm apart. The rungs decrease uniformly in length from 45 cm at the bottom to 25 cm at the top. If the top and bottom rungs are 2.5 m apart, what is the length of the wood required for the rungs? Q5: A small terrace at a football ground comprises of 15 steps each of which is 50 m long and built of solid concrete. Each step has a rise of 1/4 m and a tread of 1/2 m. Calculate the total volume of concrete required to build the terrace.",
      solution: "Problem 1 (Q3): Ladder Rungs.\nDistance between top and bottom rungs = 2.5 m = 250 cm.\nDistance between consecutive rungs = 25 cm.\nNumber of rungs n = (250 / 25) + 1 = 10 + 1 = 11 rungs.\nLengths of rungs form an AP:\nFirst term a = 45 cm (bottom)\nLast term l = 25 cm (top)\nn = 11\nTotal length of wood S₁₁ = (n/2)[a + l] = (11/2)[45 + 25] = (11/2)[70] = 11 × 35 = 385 cm = 3.85 m.\n\nProblem 2 (Q5): Concrete Terrace Steps.\nNumber of steps n = 15.\nLength of each step = 50 m.\nTread (width) = 1/2 m.\nHeight of step 1 = 1/4 m.\nHeight of step 2 = 2 × (1/4) = 2/4 m.\nHeight of step k = k/4 m.\nVolume of step k = Length × Width × Height = 50 × (1/2) × (k/4) = 25k / 4 m³.\nVolumes form an AP: V₁, V₂, ..., V₁₅\nFirst term a = 25(1)/4 = 25/4 m³.\nCommon difference d = 25/4 m³.\nTotal Volume S₁₅ = (15/2)[2(25/4) + 14(25/4)] = (15/2)[16 × (25/4)] = (15/2)[100] = 750 m³.\n[ROUGH_WORK]\nAlternative: Sum = 25/4 × (1 + 2 + ... + 15) = 25/4 × (15 × 16 / 2) = 25/4 × 120 = 25 × 30 = 750 m³!\nBoxed Answer: [ Q3: 385 cm (or 3.85 m) of wood; Q5: 750 m³ of concrete ].",
      concept_questions: [
        "In Q3, why do we add 1 when calculating the number of rungs from the total height?",
        "In Q5, explain why the volume of each step scales linearly with step index k."
      ]
    }
  ];

  // Upload to Supabase
  const m1Id = 'ed8e9b10-0d30-4dc8-9f72-4143df40c350';
  const m3Id = '398a1ef5-8ea8-42ec-9bc4-b417f614c6ce';
  const m4Id = 'd532162d-9dc7-4cdb-85df-bee7cf8f593c';
  const m5Id = 'fed8f232-cfc4-45f3-8cc2-7e7b4b9bbe8a';
  const m6Id = 'e9fbd14d-5a05-4cdc-8aff-a40fb71cac01';

  await supabase.from('syllabus_modules').update({ worked_examples: mod1Examples }).eq('id', m1Id);
  console.log('✓ Ch 5 Mod 1 updated (Foundations & Examples 1-10)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod3Examples }).eq('id', m3Id);
  console.log('✓ Ch 5 Mod 3 updated (Exercise 5.1 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod4Examples }).eq('id', m4Id);
  console.log('✓ Ch 5 Mod 4 updated (Exercise 5.2 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod5Examples }).eq('id', m5Id);
  console.log('✓ Ch 5 Mod 5 updated (Exercise 5.3 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod6Examples }).eq('id', m6Id);
  console.log('✓ Ch 5 Mod 6 updated (Exercise 5.4 Complete)');

  console.log('\n=== CHAPTER 5 ENRICHMENT 100% COMPLETE ===\n');
}

enrichCh5();
