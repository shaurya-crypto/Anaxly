const { supabase } = require('./db_helper');

const CH5_ID = '285f120a-54c7-4259-b641-b6d0a1abcb78';

const modules = [
  {
    order_index: 1,
    title: 'Core Foundations & Definitions of Arithmetic Progressions',
    description: 'Master the foundational definition of an AP, identify first term a and common difference d (positive, negative, or zero), and distinguish finite vs infinite progressions.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Identifying Mathematical Patterns in Nature and Real Life',
      'Formal Definition of Arithmetic Progression: a_{k+1} - a_k = d',
      'The First Term (a) and Common Difference (d)',
      'General Form of an AP: a, a+d, a+2d, a+3d, ...',
      'Finite vs Infinite APs and Minimum Information Required'
    ],
    key_concepts: [
      'Arithmetic Progression (AP): A list of numbers where each term is obtained by adding a fixed number to the preceding term except the first term.',
      'Common Difference (d): The fixed number added to each term; it can be positive, negative, or zero (d = a_{k+1} - a_k).',
      'General Form of an AP: a, a+d, a+2d, a+3d, ...',
      'Finite AP: An AP having a definite last term (e.g. 147, 148, ..., 157).',
      'Infinite AP: An AP that extends indefinitely without a last term (e.g. 1, 2, 3, 4, ...).'
    ],
    success_criteria: 'Student can identify whether a sequence is an AP, compute common difference d, and write the general form.',
    chapter_notes: `### 5.1 Introduction to Patterns
In nature and daily life, many sequences follow a definite arithmetic rule where succeeding terms increase or decrease by a constant value:
- Reena's salary: ₹8000, ₹8500, ₹9000... (increases by ₹500/yr)
- Ladder rungs: 45 cm, 43 cm, 41 cm... (decreases uniformly by 2 cm)
- Shakila's daughter's piggy bank: ₹100, ₹150, ₹200... (increases by ₹50)

### 5.2 Definition of Arithmetic Progression
An **Arithmetic Progression (AP)** is a list of numbers in which each term is obtained by adding a fixed number $d$ to the preceding term, except the first term $a$.
- The fixed number $d$ is called the **common difference**.
- **Important Invariant**: $d$ can be **positive** ($d > 0$), **negative** ($d < 0$), or **zero** ($d = 0$).
- Consecutive difference rule:
  $$d = a_2 - a_1 = a_3 - a_2 = \\dots = a_{k+1} - a_k$$

### General Form of an AP
$$a, a + d, a + 2d, a + 3d, \\dots, a + (n-1)d$$
- **Finite AP**: Contains a finite number of terms and always has a last term $l$.
- **Infinite AP**: Has infinitely many terms and no last term.
- To completely specify an AP, the minimum required information is the first term $a$ and common difference $d$.`,
    worked_examples: [
      {
        problem: 'Example 1: For the AP: 3/2, 1/2, -1/2, -3/2, ..., write the first term a and the common difference d.',
        given: 'Sequence: a_1 = 3/2, a_2 = 1/2, a_3 = -1/2, a_4 = -3/2',
        formula: 'First term = a_1; Common difference d = a_2 - a_1',
        substitution: 'a = 3/2; d = 1/2 - 3/2',
        calculation: 'd = (1 - 3) / 2 = -2 / 2 = -1',
        finalAnswer: 'a = 3/2, d = -1',
        unit: 'Rational numbers'
      },
      {
        problem: 'Example 2(i): Does the list 4, 10, 16, 22, ... form an AP? If so, write the next two terms.',
        given: 'Terms: a_1 = 4, a_2 = 10, a_3 = 16, a_4 = 22',
        formula: 'd_k = a_{k+1} - a_k',
        substitution: 'a_2 - a_1 = 10 - 4 = 6; a_3 - a_2 = 16 - 10 = 6; a_4 - a_3 = 22 - 16 = 6',
        calculation: 'Since a_{k+1} - a_k is constant (6), it forms an AP with d = 6. Next terms: a_5 = 22 + 6 = 28; a_6 = 28 + 6 = 34.',
        finalAnswer: 'Forms an AP with d = 6. Next two terms are 28 and 34.',
        unit: 'Integers'
      },
      {
        problem: 'Example 2(ii): Does the list 1, -1, -3, -5, ... form an AP? If so, write the next two terms.',
        given: 'Terms: a_1 = 1, a_2 = -1, a_3 = -3, a_4 = -5',
        formula: 'd_k = a_{k+1} - a_k',
        substitution: 'a_2 - a_1 = -1 - 1 = -2; a_3 - a_2 = -3 - (-1) = -2; a_4 - a_3 = -5 - (-3) = -2',
        calculation: 'Constant difference d = -2. Next terms: a_5 = -5 + (-2) = -7; a_6 = -7 + (-2) = -9.',
        finalAnswer: 'Forms an AP with d = -2. Next two terms are -7 and -9.',
        unit: 'Integers'
      },
      {
        problem: 'Example 2(iii): Does the list -2, 2, -2, 2, -2, ... form an AP?',
        given: 'Terms: a_1 = -2, a_2 = 2, a_3 = -2, a_4 = 2',
        formula: 'd_k = a_{k+1} - a_k',
        substitution: 'a_2 - a_1 = 2 - (-2) = 4; a_3 - a_2 = -2 - 2 = -4',
        calculation: 'Since a_2 - a_1 ≠ a_3 - a_2 (4 ≠ -4), the difference is not constant.',
        finalAnswer: 'Does not form an AP.',
        unit: 'N/A'
      }
    ],
    common_misconceptions: [
      'Confusing common difference order: d = a_{k+1} - a_k (succeeding minus preceding), NOT a_k - a_{k+1}. When terms decrease, d is negative.',
      'Assuming constant ratio means AP: Sequences like 2, 4, 8, 16 are geometric, not arithmetic (differences are 2, 4, 8).',
      'Thinking d cannot be zero: 3, 3, 3, 3... is a valid AP where d = 0.'
    ],
    ai_system_prompt_context: 'Teach foundational AP concepts Socratically. Draw the number line progression diagram first. Ask the student why d can be negative before showing Example 1.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="120" y="12" width="300" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">ARITHMETIC PROGRESSION: ANATOMY OF TERMS</text>
  <g transform="translate(30, 70)">
    <line x1="20" y1="60" x2="460" y2="60" stroke="#94A3B8" stroke-width="2"/>
    <circle cx="50" cy="60" r="18" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
    <text x="50" y="65" text-anchor="middle" fill="#2563EB" font-weight="bold" font-size="14">a</text>
    <text x="50" y="95" text-anchor="middle" fill="#64748B" font-size="11">Term 1 (a₁)</text>
    <path d="M 68 50 Q 115 20 152 50" fill="none" stroke="#16A34A" stroke-width="2" stroke-dasharray="4,3"/>
    <text x="110" y="30" text-anchor="middle" fill="#16A34A" font-weight="bold" font-size="12">+d</text>
    <circle cx="170" cy="60" r="18" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
    <text x="170" y="65" text-anchor="middle" fill="#2563EB" font-weight="bold" font-size="14">a+d</text>
    <text x="170" y="95" text-anchor="middle" fill="#64748B" font-size="11">Term 2 (a₂)</text>
    <path d="M 188 50 Q 235 20 272 50" fill="none" stroke="#16A34A" stroke-width="2" stroke-dasharray="4,3"/>
    <text x="230" y="30" text-anchor="middle" fill="#16A34A" font-weight="bold" font-size="12">+d</text>
    <circle cx="290" cy="60" r="18" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
    <text x="290" y="65" text-anchor="middle" fill="#2563EB" font-weight="bold" font-size="13">a+2d</text>
    <text x="290" y="95" text-anchor="middle" fill="#64748B" font-size="11">Term 3 (a₃)</text>
    <path d="M 308 50 Q 355 20 392 50" fill="none" stroke="#16A34A" stroke-width="2" stroke-dasharray="4,3"/>
    <text x="350" y="30" text-anchor="middle" fill="#16A34A" font-weight="bold" font-size="12">+d</text>
    <circle cx="410" cy="60" r="18" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
    <text x="410" y="65" text-anchor="middle" fill="#D97706" font-weight="bold" font-size="12">a+(n-1)d</text>
    <text x="410" y="95" text-anchor="middle" fill="#64748B" font-size="11">General (aₙ)</text>
  </g>
  <rect x="50" y="195" width="440" height="60" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
  <text x="270" y="215" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold">Core Relation: d = a_{k+1} - a_k</text>
  <text x="270" y="235" text-anchor="middle" fill="#475569" font-size="11">d &gt; 0: Increasing AP | d &lt; 0: Decreasing AP | d = 0: Constant AP</text>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Definition of AP & Common Difference',
          questions: [
            {
              q_num: 'Q1',
              type: '1-mark MCQ',
              question: 'Which of the following is an AP? (A) 1, 3, 9, 27 (B) 2, 4, 8, 16 (C) -10, -6, -2, 2 (D) 0.2, 0.22, 0.222',
              ideal_answer: '(C) -10, -6, -2, 2. Here, common difference d = -6 - (-10) = 4, and -2 - (-6) = 4, which is constant.',
              socratic_hint: 'Check if the difference between any two consecutive terms remains identical.'
            },
            {
              q_num: 'Q2',
              type: '2-mark Definition',
              question: 'Define the common difference of an AP. Can it be negative? Illustrate with a concrete example.',
              ideal_answer: 'Common difference (d) is the fixed number added to any term to obtain the next term, defined as d = a_{k+1} - a_k. Yes, it can be negative. For example: 10, 7, 4, 1... has d = -3.',
              socratic_hint: 'Subtract the first term from the second term to verify the sign of d.'
            },
            {
              q_num: 'Q3',
              type: 'PYQ',
              question: 'For the AP: 3/2, 1/2, -1/2, -3/2, ..., write the first term a and common difference d.',
              ideal_answer: 'First term a = 3/2. Common difference d = a_2 - a_1 = 1/2 - 3/2 = -2/2 = -1.',
              socratic_hint: 'Compute a_2 - a_1 carefully with common denominator 2.'
            },
            {
              q_num: 'Q4',
              type: 'Competency',
              question: 'A ladder has rungs that decrease uniformly by 2 cm from bottom (45 cm) to top. Does this form an AP? State its first term and common difference.',
              ideal_answer: 'Yes, it forms a finite AP: 45, 43, 41, 39, ... with first term a = 45 cm and common difference d = -2 cm.',
              socratic_hint: 'Notice that each successive rung is 2 cm shorter than the previous one.'
            }
          ]
        }
      ],
      textbook_exercises: [
        {
          exercise_number: 'Exercise 5.1 Intro',
          questions: [
            {
              q_num: 'Intro Concepts',
              question: 'Verifying sequences for arithmetic progression criteria.',
              question_type: 'conceptual',
              solution_method: 'Test consecutive differences a_{k+1} - a_k across all adjacent pairs.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 2,
    title: 'Exercise 5.1: Complete Step-by-Step Question Solver',
    description: 'Exhaustive step-by-step solver for every single question and sub-part in NCERT Exercise 5.1: real-life models, generating terms, finding a and d, and investigating 15 sequences.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Testing Real-Life Situations for Constant Common Difference',
      'Constructing First 4 Terms from Given a and d (Integers, Fractions, Decimals)',
      'Extracting a and d from Given Rational and Decimal Sequences',
      'Investigating 15 Numerical Sequences to Identify Valid APs'
    ],
    key_concepts: [
      'AP Verification Rule: a_{k+1} - a_k must be strictly identical across all pairs.',
      'Terms Construction: a_1 = a, a_2 = a+d, a_3 = a+2d, a_4 = a+3d.',
      'Radical APs: Sequences like √2, √8, √18, √32 simplify to √2, 2√2, 3√2, 4√2 (d = √2).'
    ],
    success_criteria: 'Student can solve any question from Exercise 5.1 with 100% accuracy and complete scratchpad working.',
    chapter_notes: `### Exercise 5.1 Comprehensive Walkthrough

#### Question 1: Real-Life AP Testing
- **(i) Taxi Fare**: First km = ₹15, each additional km = ₹8.
  - Terms: 15, 23, 31, 39...
  - $d = 23 - 15 = 31 - 23 = 8$. **Forms an AP**.
- **(ii) Vacuum Pump**: Removes $1/4$ of remaining air at each stroke.
  - Let initial volume be $V$. Remaining after stroke 1 = $3/4 V$. Stroke 2 = $(3/4)^2 V = 9/16 V$.
  - Difference: $3/4 V - V = -1/4 V$, but $9/16 V - 3/4 V = -3/16 V$. **Not an AP** (geometric sequence).
- **(iii) Well Digging**: First metre = ₹150, rises by ₹50/m.
  - Terms: 150, 200, 250, 300... $d = 50$. **Forms an AP**.
- **(iv) Compound Interest**: ₹10,000 at 8% compound interest per annum.
  - Amount $A_n = P(1 + r/100)^n$. Terms grow exponentially. Difference is not constant. **Not an AP**.

#### Question 2: Write First 4 Terms
- (i) $a=10, d=10 \\implies 10, 20, 30, 40$
- (ii) $a=-2, d=0 \\implies -2, -2, -2, -2$
- (iii) $a=4, d=-3 \\implies 4, 1, -2, -5$
- (iv) $a=-1, d=1/2 \\implies -1, -1/2, 0, 1/2$
- (v) $a=-1.25, d=-0.25 \\implies -1.25, -1.50, -1.75, -2.00$

#### Question 3: Find $a$ and $d$
- (i) $3, 1, -1, -3 \\implies a = 3, d = 1 - 3 = -2$
- (ii) $-5, -1, 3, 7 \\implies a = -5, d = -1 - (-5) = 4$
- (iii) $1/3, 5/3, 9/3, 13/3 \\implies a = 1/3, d = 5/3 - 1/3 = 4/3$
- (iv) $0.6, 1.7, 2.8, 3.9 \\implies a = 0.6, d = 1.7 - 0.6 = 1.1$

#### Question 4: AP Verification & Next 3 Terms
- (i) $2, 4, 8, 16 \\implies 4-2=2 \\ne 8-4=4$ (**Not AP**)
- (ii) $2, 5/2, 3, 7/2 \\implies d = 1/2$. Next: $4, 9/2, 5$ (**AP**)
- (iii) $-1.2, -3.2, -5.2, -7.2 \\implies d = -2$. Next: $-9.2, -11.2, -13.2$ (**AP**)
- (iv) $-10, -6, -2, 2 \\implies d = 4$. Next: $6, 10, 14$ (**AP**)
- (v) $3, 3+\\sqrt{2}, 3+2\\sqrt{2}, 3+3\\sqrt{2} \\implies d = \\sqrt{2}$. Next: $3+4\\sqrt{2}, 3+5\\sqrt{2}, 3+6\\sqrt{2}$ (**AP**)
- (vi) $0.2, 0.22, 0.222 \\implies 0.22-0.2=0.02 \\ne 0.222-0.22=0.002$ (**Not AP**)
- (vii) $0, -4, -8, -12 \\implies d = -4$. Next: $-16, -20, -24$ (**AP**)
- (viii) $-1/2, -1/2, -1/2, -1/2 \\implies d = 0$. Next: $-1/2, -1/2, -1/2$ (**AP**)
- (ix) $1, 3, 9, 27 \\implies 3-1=2 \\ne 9-3=6$ (**Not AP**)
- (x) $a, 2a, 3a, 4a \\implies d = a$. Next: $5a, 6a, 7a$ (**AP**)
- (xi) $a, a^2, a^3, a^4 \\implies a^2 - a \\ne a^3 - a^2$ (**Not AP**)
- (xii) $\\sqrt{2}, \\sqrt{8}, \\sqrt{18}, \\sqrt{32} = \\sqrt{2}, 2\\sqrt{2}, 3\\sqrt{2}, 4\\sqrt{2} \\implies d = \\sqrt{2}$. Next: $5\\sqrt{2}=\\sqrt{50}, 6\\sqrt{2}=\\sqrt{72}, 7\\sqrt{2}=\\sqrt{98}$ (**AP**)
- (xiii) $\\sqrt{3}, \\sqrt{6}, \\sqrt{9}, \\sqrt{12} \\implies \\sqrt{6}-\\sqrt{3} \\ne \\sqrt{9}-\\sqrt{6}$ (**Not AP**)
- (xiv) $1^2, 3^2, 5^2, 7^2 = 1, 9, 25, 49 \\implies 8 \\ne 16$ (**Not AP**)
- (xv) $1^2, 5^2, 7^2, 73 = 1, 25, 49, 73 \\implies d = 24$. Next: $73+24=97, 97+24=121, 121+24=145$ (**AP**)`,
    worked_examples: [
      {
        problem: 'Exercise 5.1 Q1(ii): Amount of air in a cylinder when vacuum pump removes 1/4 of remaining air at a time. Is it an AP?',
        given: 'Initial air = V. Each stroke removes 1/4 of remaining air.',
        formula: 'Check consecutive differences: d_1 = a_2 - a_1, d_2 = a_3 - a_2',
        substitution: 'a_1 = V; a_2 = V - V/4 = 3V/4; a_3 = 3V/4 - 1/4(3V/4) = 9V/16',
        calculation: 'a_2 - a_1 = 3V/4 - V = -V/4. a_3 - a_2 = 9V/16 - 3V/4 = -3V/16. Since -V/4 ≠ -3V/16, the differences are not equal.',
        finalAnswer: 'Does not form an AP.',
        unit: 'Volume fraction'
      },
      {
        problem: 'Exercise 5.1 Q4(xii): Check if √2, √8, √18, √32, ... forms an AP. If so, find d and next three terms.',
        given: 'Terms: √2, √8, √18, √32',
        formula: 'Simplify radicals: √8 = 2√2, √18 = 3√2, √32 = 4√2. d = a_{k+1} - a_k',
        substitution: 'a_2 - a_1 = 2√2 - √2 = √2; a_3 - a_2 = 3√2 - 2√2 = √2; a_4 - a_3 = 4√2 - 3√2 = √2',
        calculation: 'Since difference is constant, d = √2. Next terms: a_5 = 4√2 + √2 = 5√2 = √50; a_6 = 5√2 + √2 = 6√2 = √72; a_7 = 6√2 + √2 = 7√2 = √98.',
        finalAnswer: 'Forms an AP with d = √2. Next three terms are √50, √72, √98.',
        unit: 'Radicals'
      },
      {
        problem: 'Exercise 5.1 Q4(xv): Check if 1², 5², 7², 73, ... forms an AP. If so, find d and next three terms.',
        given: 'Terms: 1² = 1, 5² = 25, 7² = 49, 73',
        formula: 'd_k = a_{k+1} - a_k',
        substitution: 'a_2 - a_1 = 25 - 1 = 24; a_3 - a_2 = 49 - 25 = 24; a_4 - a_3 = 73 - 49 = 24',
        calculation: 'd = 24 (constant). Next terms: a_5 = 73 + 24 = 97; a_6 = 97 + 24 = 121; a_7 = 121 + 24 = 145.',
        finalAnswer: 'Forms an AP with d = 24. Next three terms are 97, 121, 145.',
        unit: 'Integers'
      }
    ],
    common_misconceptions: [
      'Assuming decimal strings like 0.2, 0.22, 0.222 are APs: 0.22 - 0.2 = 0.02, but 0.222 - 0.22 = 0.002. Not an AP.',
      'Misidentifying square terms: 1², 3², 5², 7² is NOT an AP, but 1², 5², 7², 73 IS an AP because 73 = 49 + 24.'
    ],
    ai_system_prompt_context: 'Focus on working out every question step-by-step on the board. Make sure the student learns the radical simplification trick for Q4(xii).',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="100" y="12" width="340" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">EXERCISE 5.1 MASTER SOLVER: RADICAL AP INVESTIGATION</text>
  <g transform="translate(40, 60)">
    <rect x="0" y="0" width="460" height="85" rx="6" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="25" fill="#1E40AF" font-weight="bold" font-size="13">Q4(xii): √2, √8, √18, √32, ...</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Simplified: √2, 2√2, 3√2, 4√2, ...</text>
    <text x="20" y="70" fill="#16A34A" font-weight="bold" font-size="12">Common Difference: d = 2√2 - √2 = √2 (Constant! AP Verified)</text>
    <text x="320" y="50" fill="#2563EB" font-weight="bold" font-size="12">Next: 5√2 = √50</text>
    <text x="320" y="70" fill="#2563EB" font-weight="bold" font-size="12">6√2 = √72, 7√2 = √98</text>
  </g>
  <g transform="translate(40, 160)">
    <rect x="0" y="0" width="460" height="85" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.2"/>
    <text x="20" y="25" fill="#991B1B" font-weight="bold" font-size="13">Q4(vi): 0.2, 0.22, 0.222, 0.2222, ...</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">a₂ - a₁ = 0.22 - 0.20 = 0.02</text>
    <text x="20" y="70" fill="#DC2626" font-weight="bold" font-size="12">a₃ - a₂ = 0.222 - 0.220 = 0.002 ≠ 0.02 (NOT an AP!)</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Exercise 5.1 Mastery',
          questions: [
            {
              q_num: 'Q1',
              type: '1-mark MCQ',
              question: 'In which situation does the sequence form an AP? (A) Compound interest at 8% (B) Taxi fare with ₹15 first km and ₹8 additional (C) Vacuum pump air evacuation (D) Side vs Area of squares',
              ideal_answer: '(B) Taxi fare: 15, 23, 31, 39... has constant difference d = 8.',
              socratic_hint: 'Which scenario adds a fixed amount rather than multiplying or taking powers?'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 3,
    title: 'The nth Term of an AP (a_n = a + (n-1)d) & Textbook Examples',
    description: 'Mathematical deduction of the general term formula a_n = a + (n-1)d, last term l, and complete solutions for NCERT Examples 3 through 10.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Mathematical Deduction of General Term a_n = a + (n-1)d',
      'The Last Term Notation (l = a + (m-1)d)',
      'Finding Unknown Position Index (Integral n Invariant)',
      'Two-Digit Numbers and Divisibility Problems',
      'Finding Terms from the End: Reversed Sequence Technique',
      'Real-Life Linear Growth: Simple Interest & Step Ladders'
    ],
    key_concepts: [
      'General Term Formula: a_n = a + (n - 1)d.',
      'Integer n Rule: The position index n MUST be a positive integer (n ∈ ℕ). If n is fractional or negative, the number is NOT a term of the AP.',
      'Term from the End: The mth term from the end of an AP with last term l and common difference d is: a\'_m = l - (m - 1)d.'
    ],
    success_criteria: 'Student can derive a_n, solve for unknown n, verify if a given number is in an AP, and find terms from the end.',
    chapter_notes: `### 5.3 The nth Term of an Arithmetic Progression

#### Mathematical Deduction
Let $a_1, a_2, a_3, \\dots$ be an AP with first term $a$ and common difference $d$:
- $a_1 = a = a + (1 - 1)d$
- $a_2 = a + d = a + (2 - 1)d$
- $a_3 = a_2 + d = (a + d) + d = a + 2d = a + (3 - 1)d$
- $a_4 = a_3 + d = (a + 2d) + d = a + 3d = a + (4 - 1)d$

Observing the pattern, the **$n^{\\text{th}}$ term (general term)** is:
$$a_n = a + (n - 1)d$$

If there are $m$ terms in the AP, then $a_m$ represents the last term, denoted by $l$:
$$l = a + (m - 1)d$$

#### Crucial Examination Principles
1. **Testing Term Belonging**: Set $a_n = k$ and solve for $n$. If $n$ is a positive natural number ($n \\in \\{1, 2, 3, \\dots\\}$), $k$ belongs to the AP; if $n$ is fractional, $k$ does not belong.
2. **$n^{\\text{th}}$ Term from the End**:
   - *Method A*: Find total terms $n$, then the $m^{\\text{th}}$ term from end is the $(n - m + 1)^{\\text{th}}$ term from beginning.
   - *Method B (Topper Trick)*: Reverse the AP! New first term $A = l$, new common difference $D = -d$. Then $a'_m = l + (m - 1)(-d) = l - (m - 1)d$.`,
    worked_examples: [
      {
        problem: 'Example 3: Find the 10th term of the AP: 2, 7, 12, ...',
        given: 'a = 2, d = 7 - 2 = 5, n = 10',
        formula: 'a_n = a + (n - 1)d',
        substitution: 'a_{10} = 2 + (10 - 1) * 5',
        calculation: 'a_{10} = 2 + 9 * 5 = 2 + 45 = 47',
        finalAnswer: 'a_{10} = 47',
        unit: 'Integer'
      },
      {
        problem: 'Example 4: Which term of the AP: 21, 18, 15, ... is -81? Also, is any term 0?',
        given: 'a = 21, d = 18 - 21 = -3, a_n = -81',
        formula: 'a_n = a + (n - 1)d',
        substitution: '-81 = 21 + (n - 1)(-3)',
        calculation: '-81 - 21 = -3(n - 1) => -102 = -3(n - 1) => n - 1 = 34 => n = 35. For a_n = 0: 0 = 21 + (n - 1)(-3) => 3(n - 1) = 21 => n = 8.',
        finalAnswer: 'The 35th term is -81, and the 8th term is 0.',
        unit: 'Ordinal indices'
      },
      {
        problem: 'Example 6: Check whether 301 is a term of the list of numbers 5, 11, 17, 23, ...',
        given: 'a = 5, d = 11 - 5 = 6, candidate a_n = 301',
        formula: 'a_n = a + (n - 1)d',
        substitution: '301 = 5 + (n - 1) * 6',
        calculation: '301 - 5 = 6(n - 1) => 296 = 6(n - 1) => n - 1 = 296 / 6 = 148 / 3 => n = 151 / 3 = 50.33',
        finalAnswer: 'Since n is not a positive integer, 301 is NOT a term of this AP.',
        unit: 'Fractional index rejected'
      },
      {
        problem: 'Example 8: Find the 11th term from the last term of the AP: 10, 7, 4, ..., -62.',
        given: 'AP: 10, 7, 4, ..., -62. To find 11th term from last.',
        formula: 'Reversed AP: A = -62, D = -(-3) = +3',
        substitution: 'a\'_{11} = -62 + (11 - 1) * 3',
        calculation: 'a\'_{11} = -62 + 10 * 3 = -62 + 30 = -32',
        finalAnswer: '-32',
        unit: 'Integer'
      }
    ],
    common_misconceptions: [
      'Forgetting that n must be a whole positive number. If solving gives n = 25.5, the number is not in the AP.',
      'Miscalculating term from the end by setting index as (n - m) instead of (n - m + 1).'
    ],
    ai_system_prompt_context: 'Lead with the deduction of a_n. Pose Example 6 to test if the student realizes n must be a natural number.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="90" y="12" width="360" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">THE GENERAL TERM: aₙ = a + (n - 1)d</text>
  <g transform="translate(30, 60)">
    <rect x="0" y="0" width="480" height="90" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
    <text x="240" y="32" text-anchor="middle" fill="#1E3A8A" font-size="18" font-weight="bold">aₙ = a + (n - 1)d</text>
    <text x="50" y="65" fill="#2563EB" font-size="12" font-weight="bold">a = First Term</text>
    <text x="180" y="65" fill="#059669" font-size="12" font-weight="bold">n = Term Index (n ∈ ℕ)</text>
    <text x="350" y="65" fill="#D97706" font-size="12" font-weight="bold">d = Common Difference</text>
  </g>
  <g transform="translate(30, 165)">
    <rect x="0" y="0" width="480" height="90" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5"/>
    <text x="20" y="25" fill="#166534" font-weight="bold" font-size="13">REVERSED AP TRICK (Term from the End):</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Original: a, a+d, a+2d, ... l  (diff = +d)</text>
    <text x="20" y="70" fill="#0F172A" font-size="12">Reversed: l, l-d, l-2d, ... a  (First Term = l, Difference = -d)</text>
    <text x="310" y="60" fill="#16A34A" font-weight="bold" font-size="13">a'ₘ = l - (m - 1)d</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'General Term Formula',
          questions: [
            {
              q_num: 'Q1',
              type: '1-mark MCQ',
              question: 'The 10th term of the AP 2, 7, 12, ... is: (A) 45 (B) 47 (C) 52 (D) 50',
              ideal_answer: '(B) 47. a_10 = 2 + 9 * 5 = 47.',
              socratic_hint: 'Identify a and d, then compute a + 9d.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 4,
    title: 'Exercise 5.2 Step-by-Step Solver Part 1: Unknowns, Missing Terms & Basic Numericals (Q1 to Q10)',
    description: 'Complete scratchpad solutions for Exercise 5.2 Questions 1 to 10 covering table fill-ins, box unknowns, two-equation systems, and term tests.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Solving the Table of 4 Variables (a, d, n, a_n)',
      'MCQ Justifications for 30th and 11th Terms',
      'Solving Boxed Missing Terms via Simultaneous Equations',
      'Checking Term Belonging and Multi-Condition APs'
    ],
    key_concepts: [
      'Four-Variable Equation: a_n = a + (n-1)d connects four variables; given any 3, find the 4th.',
      'Arithmetic Mean for Three Terms: If a, b, c are in AP, then b = (a+c)/2.'
    ],
    success_criteria: 'Student can solve any missing term problem or simultaneous AP equation from Q1 to Q10.',
    chapter_notes: `### Exercise 5.2 (Q1 to Q10) Solutions

#### Q1: Fill in the Table
- (i) $a=7, d=3, n=8 \\implies a_8 = 7 + 7(3) = 28$
- (ii) $a=-18, n=10, a_n=0 \\implies 0 = -18 + 9d \\implies 9d = 18 \\implies d = 2$
- (iii) $d=-3, n=18, a_n=-5 \\implies -5 = a + 17(-3) \\implies a = -5 + 51 = 46$
- (iv) $a=-18.9, d=2.5, a_n=3.6 \\implies 3.6 = -18.9 + (n-1)(2.5) \\implies 22.5 = 2.5(n-1) \\implies n-1 = 9 \\implies n = 10$
- (v) $a=3.5, d=0, n=105 \\implies a_{105} = 3.5 + 104(0) = 3.5$

#### Q2: MCQs
- (i) 30th term of $10, 7, 4...$: $a = 10, d = -3 \\implies a_{30} = 10 + 29(-3) = 10 - 87 = -77$ (**Option C**).
- (ii) 11th term of $-3, -1/2, 2...$: $d = -1/2 - (-3) = 5/2 \\implies a_{11} = -3 + 10(5/2) = -3 + 25 = 22$ (**Option B**).

#### Q3: Missing Box Terms
- (i) $2, [\\;], 26 \\implies b = (2 + 26)/2 = 14$
- (ii) $[\\;], 13, [\\;], 3 \\implies a+d=13, a+3d=3 \\implies 2d = -10 \\implies d = -5, a = 18$. Missing: **18, 8**.
- (iii) $5, [\\;], [\\;], 9\\frac{1}{2} \\implies a=5, a+3d=19/2 \\implies 3d = 9/2 \\implies d = 3/2$. Missing: **$6\\frac{1}{2}, 8$**.
- (iv) $-4, [\\;], [\\;], [\\;], [\\;], 6 \\implies a=-4, a+5d=6 \\implies 5d = 10 \\implies d = 2$. Missing: **-2, 0, 2, 4**.
- (v) $[\\;], 38, [\\;], [\\;], [\\;], -22 \\implies a+d=38, a+5d=-22 \\implies 4d = -60 \\implies d = -15, a = 53$. Missing: **53, 23, 8, -7**.

#### Q4 to Q10:
- **Q4**: $3, 8, 13, 18...$ Which term is 78? $78 = 3 + (n-1)5 \\implies 75 = 5(n-1) \\implies n = 16$.
- **Q5(i)**: $7, 13, 19... 205 \\implies 205 = 7 + (n-1)6 \\implies n-1 = 33 \\implies n = 34$.
- **Q5(ii)**: $18, 15.5, 13... -47 \\implies -47 = 18 + (n-1)(-2.5) \\implies -65 = -2.5(n-1) \\implies n = 27$.
- **Q6**: Is $-150$ in $11, 8, 5, 2...$? $-150 = 11 + (n-1)(-3) \\implies -161 = -3(n-1) \\implies n = 164/3$ (not integer). **No**.
- **Q7**: $a_{11} = 38, a_{16} = 73 \\implies 5d = 35 \\implies d = 7, a = -32$. $a_{31} = -32 + 30(7) = 178$.
- **Q8**: 50 terms, $a_3 = 12, a_{50} = 106 \\implies 47d = 94 \\implies d = 2, a = 8$. $a_{29} = 8 + 28(2) = 64$.
- **Q9**: $a_3 = 4, a_9 = -8 \\implies 6d = -12 \\implies d = -2, a = 8$. $a_n = 0 \\implies 8 + (n-1)(-2) = 0 \\implies n = 5$.
- **Q10**: $a_{17} - a_{10} = 7 \\implies (a + 16d) - (a + 9d) = 7 \\implies 7d = 7 \\implies d = 1$.`,
    worked_examples: [
      {
        problem: 'Exercise 5.2 Q7: Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.',
        given: 'a_{11} = 38, a_{16} = 73',
        formula: 'a_n = a + (n - 1)d',
        substitution: 'a + 10d = 38 (eq 1); a + 15d = 73 (eq 2)',
        calculation: 'Subtract (1) from (2): 5d = 35 => d = 7. From (1): a + 70 = 38 => a = -32. Then a_{31} = -32 + (31 - 1)*7 = -32 + 210 = 178.',
        finalAnswer: '178',
        unit: 'Integer'
      },
      {
        problem: 'Exercise 5.2 Q10: The 17th term of an AP exceeds its 10th term by 7. Find the common difference.',
        given: 'a_{17} - a_{10} = 7',
        formula: 'a_n = a + (n - 1)d',
        substitution: '[a + 16d] - [a + 9d] = 7',
        calculation: '7d = 7 => d = 1',
        finalAnswer: 'd = 1',
        unit: 'Integer'
      }
    ],
    common_misconceptions: [
      'In Q3(ii), assuming the first term is 13. 13 is the SECOND term (a+d=13).',
      'Forgetting that Q8 states "an AP consists of 50 terms of which the last term is 106", so a_{50} = 106.'
    ],
    ai_system_prompt_context: 'Demonstrate the 2-equation elimination method for Q7 and Q8 on the chalkboard. Point out that a always cancels out when subtracting.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="100" y="12" width="340" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">EXERCISE 5.2: SIMULTANEOUS AP EQUATIONS</text>
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="480" height="100" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="28" fill="#1E40AF" font-weight="bold" font-size="14">Elimination Technique for Unknown a and d:</text>
    <text x="20" y="52" fill="#0F172A" font-size="13">Equation (1): a + (p - 1)d = Value₁</text>
    <text x="20" y="74" fill="#0F172A" font-size="13">Equation (2): a + (q - 1)d = Value₂</text>
    <text x="260" y="63" fill="#16A34A" font-weight="bold" font-size="14">Subtracting gives: (p - q)d = ΔValue</text>
  </g>
  <g transform="translate(30, 170)">
    <rect x="0" y="0" width="480" height="85" rx="8" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1"/>
    <text x="20" y="26" fill="#0F172A" font-weight="bold" font-size="12">Applied to Q7 (a₁₁ = 38, a₁₆ = 73):</text>
    <text x="20" y="48" fill="#475569" font-size="12">(a + 15d) - (a + 10d) = 73 - 38  ⇒  5d = 35  ⇒  d = 7</text>
    <text x="20" y="70" fill="#2563EB" font-weight="bold" font-size="12">a = 38 - 70 = -32  ⇒  a₃₁ = -32 + 30(7) = 178</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Exercise 5.2 Part 1',
          questions: [
            {
              q_num: 'Q1',
              type: '1-mark MCQ',
              question: 'If a = 7, d = 3, n = 8, then a_n is: (A) 21 (B) 28 (C) 31 (D) 24',
              ideal_answer: '(B) 28. a_8 = 7 + 7 * 3 = 28.',
              socratic_hint: 'Substitute into a + (n-1)d with n=8.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 5,
    title: 'Exercise 5.2 Step-by-Step Solver Part 2: Advanced Word Problems & Systems (Q11 to Q20)',
    description: 'Complete step-by-step scratchpad solutions for Exercise 5.2 Questions 11 to 20, including term comparisons, divisibility sequences, and real-life career savings models.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Term Exceeding Conditions (a_n = a_m + K)',
      'Equal Difference Invariant in Dual APs',
      'Divisibility and Multiple Counting (7-divisible 3-digit numbers)',
      'Equal Term Conditions Across Distinct APs',
      'Finding 20th Term from the End in Reverse',
      'Career Salary and Incremental Savings Applications'
    ],
    key_concepts: [
      'Dual AP Invariant: If two APs have the same common difference, the difference between their corresponding terms is identical for all n.',
      'Counting Multiples: Form the AP of multiples, identify first multiple a and last multiple l, and solve for n.'
    ],
    success_criteria: 'Student can solve complex word problems and divisibility APs from Exercise 5.2 Questions 11 to 20.',
    chapter_notes: `### Exercise 5.2 (Q11 to Q20) Solutions

- **Q11**: $3, 15, 27, 39...$ Which term will be 132 more than its 54th term?
  - $a = 3, d = 12$. $a_{54} = 3 + 53(12) = 639$.
  - Required term $a_n = 639 + 132 = 771$.
  - $771 = 3 + (n-1)12 \\implies 12(n-1) = 768 \\implies n-1 = 64 \\implies n = 65$.
  - *Short trick*: $(n - 54)d = 132 \\implies (n-54)(12) = 132 \\implies n - 54 = 11 \\implies n = 65$.

- **Q12**: Two APs have the same common difference $d$. Difference between 100th terms is 100.
  - Let first AP have first term $a$, second have $b$.
  - $a_{100} - b_{100} = (a + 99d) - (b + 99d) = a - b = 100$.
  - Difference between 1000th terms: $a_{1000} - b_{1000} = (a + 999d) - (b + 999d) = a - b = 100$.

- **Q13**: How many three-digit numbers are divisible by 7?
  - Smallest 3-digit divisible by 7: $105$. Largest: $994$.
  - Sequence: $105, 112, 119, \\dots, 994$. $a = 105, d = 7, a_n = 994$.
  - $994 = 105 + (n-1)7 \\implies 889 = 7(n-1) \\implies n-1 = 127 \\implies n = 128$.

- **Q14**: How many multiples of 4 lie between 10 and 250?
  - First multiple: $12$. Last multiple: $248$.
  - $248 = 12 + (n-1)4 \\implies 236 = 4(n-1) \\implies n-1 = 59 \\implies n = 60$.

- **Q15**: For what value of $n$ are $n^{\\text{th}}$ terms of $63, 65, 67...$ and $3, 10, 17...$ equal?
  - AP 1: $a_n = 63 + (n-1)2 = 2n + 61$.
  - AP 2: $b_n = 3 + (n-1)7 = 7n - 4$.
  - $2n + 61 = 7n - 4 \\implies 5n = 65 \\implies n = 13$.

- **Q16**: Determine AP whose 3rd term is 16 and 7th term exceeds 5th term by 12.
  - $a_7 - a_5 = 12 \\implies 2d = 12 \\implies d = 6$.
  - $a_3 = a + 2(6) = 16 \\implies a = 4$.
  - AP: $4, 10, 16, 22, \\dots$

- **Q17**: 20th term from last of $3, 8, 13, \\dots, 253$.
  - Reverse AP: $a = 253, d = -5$.
  - $a_{20} = 253 + 19(-5) = 253 - 95 = 158$.

- **Q18**: $a_4 + a_8 = 24$ and $a_6 + a_{10} = 44$.
  - $2a + 10d = 24 \\implies a + 5d = 12$.
  - $2a + 14d = 44 \\implies a + 7d = 22$.
  - Subtracting gives $2d = 10 \\implies d = 5, a = -13$. First three terms: $-13, -8, -3$.

- **Q19**: Subba Rao started in 1995 at ₹5000 with ₹200 increment. When does income reach ₹7000?
  - $a = 5000, d = 200, a_n = 7000$.
  - $7000 = 5000 + (n-1)200 \\implies 2000 = 200(n-1) \\implies n = 11$. Year: $1995 + 10 = 2005$.

- **Q20**: Ramkali savings: ₹5 first week, increases by ₹1.75. When does weekly savings reach ₹20.75?
  - $20.75 = 5 + (n-1)1.75 \\implies 15.75 = 1.75(n-1) \\implies n-1 = 9 \\implies n = 10$.`,
    worked_examples: [
      {
        problem: 'Exercise 5.2 Q13: How many three-digit numbers are divisible by 7?',
        given: 'Range: 100 to 999. First number divisible by 7 = 105; Last number = 994.',
        formula: 'a_n = a + (n - 1)d',
        substitution: '994 = 105 + (n - 1) * 7',
        calculation: '994 - 105 = 7(n - 1) => 889 = 7(n - 1) => n - 1 = 127 => n = 128.',
        finalAnswer: '128 three-digit numbers',
        unit: 'Count'
      },
      {
        problem: 'Exercise 5.2 Q17: Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.',
        given: 'AP: 3, 8, 13, ..., 253. Finding 20th from end.',
        formula: 'Reversed AP: First term A = 253, Common difference D = -5',
        substitution: 'a\'_{20} = 253 + (20 - 1) * (-5)',
        calculation: 'a\'_{20} = 253 + 19 * (-5) = 253 - 95 = 158',
        finalAnswer: '158',
        unit: 'Integer'
      },
      {
        problem: 'Exercise 5.2 Q19: Subba Rao started work in 1995 at an annual salary of ₹5000 and received an increment of ₹200 each year. In which year did his income reach ₹7000?',
        given: 'a = 5000, d = 200, a_n = 7000',
        formula: 'a_n = a + (n - 1)d',
        substitution: '7000 = 5000 + (n - 1) * 200',
        calculation: '2000 = 200(n - 1) => n - 1 = 10 => n = 11. Years elapsed = 10. Year = 1995 + 10 = 2005.',
        finalAnswer: 'Year 2005 (in the 11th year of work)',
        unit: 'Calendar Year'
      }
    ],
    common_misconceptions: [
      'In Q19, adding 11 to 1995 instead of 10. In year 1 (1995) salary is ₹5000. In year 11 (1995 + 10 = 2005) salary is ₹7000.',
      'In Q12, thinking the difference between 1000th terms would be 1000. The common differences cancel out completely, so the difference remains 100.'
    ],
    ai_system_prompt_context: 'Demonstrate Q11 and Q17 using smart shortcut techniques on the chalkboard. Point out that reversing the AP is far faster than finding total n.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="110" y="12" width="320" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">DIVISIBILITY AP: 3-DIGIT NUMBERS DIVISIBLE BY 7</text>
  <g transform="translate(40, 55)">
    <rect x="0" y="0" width="460" height="95" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="20" y="26" fill="#166534" font-weight="bold" font-size="13">Boundary Extraction (100 to 999):</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">100 ÷ 7 = 14 with remainder 2  ⇒  First term: a = 100 + (7 - 2) = 105</text>
    <text x="20" y="72" fill="#0F172A" font-size="12">999 ÷ 7 = 142 with remainder 5  ⇒  Last term: l = 999 - 5 = 994</text>
  </g>
  <g transform="translate(40, 165)">
    <rect x="0" y="0" width="460" height="90" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="28" fill="#1E40AF" font-weight="bold" font-size="13">Calculation Scratchpad:</text>
    <text x="20" y="52" fill="#0F172A" font-size="12">994 = 105 + (n - 1) × 7  ⇒  889 = 7(n - 1)</text>
    <text x="20" y="74" fill="#2563EB" font-weight="bold" font-size="13">n - 1 = 127  ⇒  n = 128 Numbers Total</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Exercise 5.2 Part 2',
          questions: [
            {
              q_num: 'Q1',
              type: 'PYQ',
              question: 'How many three-digit numbers are divisible by 7? (A) 125 (B) 128 (C) 130 (D) 120',
              ideal_answer: '(B) 128. a = 105, l = 994, d = 7. 994 = 105 + (n-1)*7 gives n = 128.',
              socratic_hint: 'Find the first and last 3-digit numbers divisible by 7.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 6,
    title: 'Sum of First n Terms (S_n) Formulas, Gauss Derivation & Exercise 5.3 Part 1 (Q1 to Q10)',
    description: 'Deduce Gauss pairing technique, derive S_n = n/2[2a+(n-1)d] and S_n = n/2(a+l), and solve Exercise 5.3 Questions 1 to 10.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Gauss Pairing Trick for 1 to 100 Summation',
      'Derivation of S_n = n/2[2a + (n-1)d]',
      'First and Last Term Formula S_n = n/2(a + l)',
      'The nth Term from Sums Relation: a_n = S_n - S_{n-1}',
      'Solving Exercise 5.3 Q1 to Q10: Dual Answers and Quadratic Factoring'
    ],
    key_concepts: [
      'General Sum Formula: S_n = (n/2)[2a + (n - 1)d].',
      'Last Term Sum Formula: S_n = (n/2)(a + l), where l = a_n.',
      'Sum of First n Natural Numbers: S_n = n(n + 1)/2.',
      'Term Extraction Property: a_n = S_n - S_{n-1}.'
    ],
    success_criteria: 'Student can derive S_n formulas and solve any numerical problem from Exercise 5.3 Q1 to Q10.',
    chapter_notes: `### 5.4 Sum of First n Terms of an AP

#### The Gauss Pairing Insight
When Carl Friedrich Gauss was 10 years old, he computed $1 + 2 + \\dots + 100 = 5050$ by writing the series forward and backward:
$$S = 1 + 2 + 3 + \\dots + 100$$
$$S = 100 + 99 + 98 + \\dots + 1$$
$$2S = 101 + 101 + \\dots + 101 \\text{ (100 times)} = 100 \\times 101 \\implies S = \\frac{100 \\times 101}{2} = 5050$$

#### Formal Algebraic Derivation
$$S_n = a + (a+d) + (a+2d) + \\dots + [a + (n-1)d] \\quad (1)$$
$$S_n = [a+(n-1)d] + [a+(n-2)d] + \\dots + a \\quad (2)$$
Adding (1) and (2) term-wise:
$$2S_n = [2a + (n-1)d] + [2a + (n-1)d] + \\dots + [2a + (n-1)d] \\text{ (n times)}$$
$$2S_n = n[2a + (n-1)d] \\implies S_n = \\frac{n}{2}[2a + (n-1)d]$$

Since $a_n = l = a + (n-1)d$:
$$S_n = \\frac{n}{2}[a + l]$$

#### Essential Relation: $a_n = S_n - S_{n-1}$
The $n^{\\text{th}}$ term is the difference between the sum of first $n$ terms and sum of first $(n-1)$ terms.

#### Exercise 5.3 (Q1 to Q10) Highlights:
- **Q1(i)**: $2, 7, 12...$ to 10 terms: $S_{10} = 5[4 + 9(5)] = 5(49) = 245$.
- **Q2(i)**: $7 + 10.5 + 14 + \\dots + 84$: $a = 7, d = 3.5, l = 84 \\implies n = 23$. $S_{23} = 23/2(7 + 84) = 2093/2 = 1046.5$.
- **Q4**: How many terms of $9, 17, 25...$ give sum 636?
  - $636 = \\frac{n}{2}[18 + (n-1)8] = n(4n + 5) \\implies 4n^2 + 5n - 636 = 0$.
  - Factoring: $(4n + 53)(n - 12) = 0 \\implies n = 12$ ($n = -53/4$ rejected).
- **Q5**: $a = 5, l = 45, S_n = 400 \\implies 400 = n/2(50) \\implies n = 16$. $d = (45 - 5)/15 = 40/15 = 8/3$.
- **Q7**: $d = 7, a_{22} = 149 \\implies a + 21(7) = 149 \\implies a = 2$. $S_{22} = 11(2 + 149) = 1661$.
- **Q9**: $S_7 = 49, S_{17} = 289$. Notice $7^2 = 49, 17^2 = 289 \\implies S_n = n^2$.`,
    worked_examples: [
      {
        problem: 'Exercise 5.3 Q4: How many terms of the AP: 9, 17, 25, ... must be taken to give a sum of 636?',
        given: 'a = 9, d = 17 - 9 = 8, S_n = 636',
        formula: 'S_n = (n/2)[2a + (n - 1)d]',
        substitution: '636 = (n/2)[2(9) + (n - 1)8]',
        calculation: '636 = (n/2)[18 + 8n - 8] = (n/2)[8n + 10] = n(4n + 5) => 4n^2 + 5n - 636 = 0. Using quadratic formula: n = [-5 ± sqrt(25 - 4(4)(-636))] / 8 = [-5 ± sqrt(25 + 10176)] / 8 = [-5 ± 101] / 8. n = 96 / 8 = 12 (positive integer).',
        finalAnswer: 'n = 12 terms',
        unit: 'Terms'
      },
      {
        problem: 'Exercise 5.3 Q9: If the sum of first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of first n terms.',
        given: 'S_7 = 49, S_{17} = 289',
        formula: 'S_n = (n/2)[2a + (n - 1)d]',
        substitution: '49 = (7/2)[2a + 6d] => a + 3d = 7 (eq 1); 289 = (17/2)[2a + 16d] => a + 8d = 17 (eq 2)',
        calculation: 'Subtract (1) from (2): 5d = 10 => d = 2. From (1): a + 6 = 7 => a = 1. Then S_n = (n/2)[2(1) + (n - 1)(2)] = (n/2)[2n] = n^2.',
        finalAnswer: 'S_n = n²',
        unit: 'Algebraic expression'
      }
    ],
    common_misconceptions: [
      'In quadratic equations for n (like in Q4), student might accept the negative fractional root. n must be a positive integer.',
      'In Example 13, having two valid answers (n = 4 and n = 13) confuses students: explain that terms from 5 to 13 sum to 0 because positive and negative terms cancel.'
    ],
    ai_system_prompt_context: 'Derive Gauss trick on the board with arrows. Explain the physical reason why a sum can equal the same value for two different values of n.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="100" y="12" width="340" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">GAUSS SUMMATION PAIRING MECHANISM</text>
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="480" height="90" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.2"/>
    <text x="20" y="28" fill="#1E3A8A" font-weight="bold" font-size="13">Pairing 1 to 100 Forward and Backward:</text>
    <text x="30" y="54" fill="#0F172A" font-family="monospace" font-size="13">S =   1  +   2  +   3  + ... + 100</text>
    <text x="30" y="74" fill="#0F172A" font-family="monospace" font-size="13">S = 100  +  99  +  98  + ... +   1</text>
    <line x1="25" y1="80" x2="450" y2="80" stroke="#94A3B8" stroke-width="1"/>
  </g>
  <g transform="translate(30, 160)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="20" y="28" fill="#166534" font-weight="bold" font-size="13">Result: 100 Identical Pairs of 101:</text>
    <text x="20" y="52" fill="#0F172A" font-size="12">2S = 101 × 100 = 10100  ⇒  S = 5050</text>
    <text x="20" y="75" fill="#2563EB" font-weight="bold" font-size="13">In General: Sₙ = (n/2)[2a + (n-1)d] = (n/2)(a + l)</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Sum of n Terms Formula',
          questions: [
            {
              q_num: 'Q1',
              type: '1-mark MCQ',
              question: 'The sum of the first 1000 positive integers is: (A) 500500 (B) 5050 (C) 100000 (D) 500000',
              ideal_answer: '(A) 500500. S = 1000 * 1001 / 2 = 500500.',
              socratic_hint: 'Use n(n+1)/2 with n=1000.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 7,
    title: 'Exercise 5.3 Part 2: Real-World AP Word Problems & Competency Numericals (Q11 to Q20)',
    description: 'Exhaustive step-by-step solutions for Exercise 5.3 Questions 11 to 20 covering tree planting, semicircle spirals, log stacks, and potato race.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Extracting Terms from Sum Expression S_n = 4n - n^2',
      'Sum of Multiples and Divisible Numbers',
      'Penalty Schedule Problems (Daily Increments)',
      'School Tree Plantation Scheme Modeling',
      'Semicircle Spiral Cumulative Perimeter Analysis',
      'Quadratic Invariant in 200 Logs Stacking',
      'Competency-Based Potato Race Distance Modeling'
    ],
    key_concepts: [
      'Log Stacking Physical Constraint: The number of logs in any row cannot be negative (a_n > 0); this rejects unphysical quadratic roots.',
      'Potato Race Distance Rule: To pick up each potato and return to bucket, distance is DOUBLED: 2 * (initial + potato offset).'
    ],
    success_criteria: 'Student can translate real-world word problems into AP equations and eliminate unphysical solutions.',
    chapter_notes: `### Exercise 5.3 (Q11 to Q20) Detailed Solutions

- **Q11**: $S_n = 4n - n^2$.
  - First term $S_1 = 4(1) - 1^2 = 3$. ($a_1 = 3$)
  - Sum of first two $S_2 = 4(2) - 2^2 = 8 - 4 = 4$.
  - Second term $a_2 = S_2 - S_1 = 4 - 3 = 1$.
  - Common difference $d = a_2 - a_1 = 1 - 3 = -2$.
  - 3rd term $a_3 = 3 + 2(-2) = -1$.
  - 10th term $a_{10} = 3 + 9(-2) = -15$.
  - $n^{\\text{th}}$ term $a_n = S_n - S_{n-1} = (4n - n^2) - [4(n-1) - (n-1)^2] = 5 - 2n$.

- **Q12**: Sum of first 40 positive integers divisible by 6.
  - $6, 12, 18, \\dots, 240$. $n = 40, a = 6, l = 240$.
  - $S_{40} = \\frac{40}{2}(6 + 240) = 20(246) = 4920$.

- **Q13**: Sum of first 15 multiples of 8.
  - $8, 16, 24, \\dots, 120$. $n = 15, a = 8, l = 120$.
  - $S_{15} = \\frac{15}{2}(8 + 120) = \\frac{15}{2}(128) = 15 \\times 64 = 960$.

- **Q14**: Sum of odd numbers between 0 and 50.
  - $1, 3, 5, \\dots, 49$. $n = 25, a = 1, l = 49$.
  - $S_{25} = 25^2 = 625$.

- **Q15**: Construction Delay Penalty: ₹200 for Day 1, ₹250 for Day 2, ₹300 for Day 3... for 30 days.
  - $a = 200, d = 50, n = 30$.
  - $S_{30} = \\frac{30}{2}[2(200) + 29(50)] = 15[400 + 1450] = 15(1850) = \\text{₹ } 27,750$.

- **Q16**: 7 cash prizes from ₹700, each ₹20 less than preceding.
  - $n = 7, S_7 = 700, d = -20$.
  - $700 = \\frac{7}{2}[2a + 6(-20)] \\implies 200 = 2a - 120 \\implies 2a = 320 \\implies a = 160$.
  - Prizes: **₹160, ₹140, ₹120, ₹100, ₹80, ₹60, ₹40**.

- **Q17**: Tree Planting: Classes 1 to 12, each class has 3 sections.
  - Trees by Class $k$: $3 \\times k$.
  - Total trees $= 3 \\times [1 + 2 + \\dots + 12] = 3 \\times \\frac{12 \\times 13}{2} = 3 \\times 78 = 234$ trees.

- **Q18**: Semicircle Spiral of 13 semicircles: radii $0.5, 1.0, 1.5, \\dots, 6.5$ cm.
  - Perimeter of semicircle $l_k = \\pi r_k$.
  - Total Length $= \\pi [r_1 + r_2 + \\dots + r_{13}] = \\frac{22}{7} \\times \\frac{13}{2} [0.5 + 6.5] = \\frac{22}{7} \\times \\frac{13}{2} \\times 7 = 143$ cm.

- **Q19**: 200 logs stacked: 20 in bottom row, 19 in next, 18 in next...
  - $S_n = 200, a = 20, d = -1$.
  - $200 = \\frac{n}{2}[40 + (n-1)(-1)] \\implies 400 = n(41 - n) \\implies n^2 - 41n + 400 = 0$.
  - Factoring: $(n - 16)(n - 25) = 0$.
  - If $n = 25$, $a_{25} = 20 + 24(-1) = -4$ logs (impossible!).
  - Hence $n = 16$ rows, and logs in top row $a_{16} = 20 + 15(-1) = 5$ logs.

- **Q20**: Potato Race: Bucket at 0, first potato at 5 m, next 9 potatoes spaced 3 m apart.
  - Total distance $= 2 \\times [5 + 8 + 11 + \\dots + \\text{10 terms}]$.
  - Sum $= 2 \\times \\left(\\frac{10}{2}[2(5) + 9(3)]\\right) = 2 \\times [5(10 + 27)] = 2 \\times [5 \\times 37] = 2 \\times 185 = 370$ m.`,
    worked_examples: [
      {
        problem: 'Exercise 5.3 Q18: A spiral is made of 13 consecutive semicircles with radii 0.5 cm, 1.0 cm, 1.5 cm, ... What is the total length of the spiral? (Take π = 22/7)',
        given: 'Radii form an AP: r_1 = 0.5, r_2 = 1.0, ..., n = 13. Semicircle perimeter = πr.',
        formula: 'Total Length L = π(r_1 + r_2 + ... + r_{13}) = π * S_{13}',
        substitution: 'L = (22/7) * (13/2) * [2(0.5) + (13 - 1)(0.5)]',
        calculation: 'L = (22/7) * (13/2) * [1.0 + 6.0] = (22/7) * (13/2) * 7 = 11 * 13 = 143 cm.',
        finalAnswer: '143 cm',
        unit: 'Centimetres'
      },
      {
        problem: 'Exercise 5.3 Q19: 200 logs are stacked: 20 in the bottom row, 19 in next, 18 in next... In how many rows are the 200 logs placed, and how many logs are in the top row?',
        given: 'S_n = 200, a = 20, d = -1',
        formula: 'S_n = (n/2)[2a + (n - 1)d] and a_n = a + (n - 1)d',
        substitution: '200 = (n/2)[2(20) + (n - 1)(-1)] => 400 = n[41 - n]',
        calculation: 'n^2 - 41n + 400 = 0 => (n - 16)(n - 25) = 0 => n = 16 or n = 25. For n = 25: a_{25} = 20 + 24(-1) = -4 (impossible). For n = 16: a_{16} = 20 + 15(-1) = 5 logs.',
        finalAnswer: '16 rows, with 5 logs in the top row',
        unit: 'Count'
      },
      {
        problem: 'Exercise 5.3 Q20: Potato race: bucket at 5 m from 1st potato, 3 m apart, 10 potatoes. Find total distance run.',
        given: 'Distance for potato k = 2 * [5 + (k - 1) * 3] meters, n = 10',
        formula: 'Total Distance D = 2 * S_{10}',
        substitution: 'D = 2 * (10/2) * [2(5) + 9(3)]',
        calculation: 'D = 10 * [10 + 27] = 10 * 37 = 370 m.',
        finalAnswer: '370 metres',
        unit: 'Metres'
      }
    ],
    common_misconceptions: [
      'In Q19, accepting n = 25 without checking the number of logs in the 25th row. You cannot have -4 logs in a row!',
      'In Q20, forgetting to double the distances (competitor runs to the potato AND back to the bucket).'
    ],
    ai_system_prompt_context: 'Draw the log stacking diagram and potato race coordinate model on the board. Emphasize why the physical boundary condition rejects n=25.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="100" y="12" width="340" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">Q19: 200 LOGS STACKING REJECTION MODEL</text>
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="26" fill="#1E40AF" font-weight="bold" font-size="13">Quadratic Resolution: n² - 41n + 400 = 0</text>
    <text x="20" y="48" fill="#0F172A" font-size="12">Roots: (n - 16)(n - 25) = 0  ⇒  n = 16  OR  n = 25</text>
    <text x="20" y="75" fill="#DC2626" font-weight="bold" font-size="13">Check n = 25: a₂₅ = 20 + 24(-1) = -4 Logs ❌ REJECTED!</text>
  </g>
  <g transform="translate(30, 160)">
    <rect x="0" y="0" width="480" height="100" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="20" y="26" fill="#166534" font-weight="bold" font-size="13">Physical Verification: n = 16 Rows</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Row 1 (Bottom): 20 logs | Row 2: 19 logs ... Row 16: 5 logs</text>
    <text x="20" y="75" fill="#16A34A" font-weight="bold" font-size="14">Top Row Logs: a₁₆ = 20 + 15(-1) = 5 Logs (Valid!)</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Real-World AP Applications',
          questions: [
            {
              q_num: 'Q1',
              type: 'Competency',
              question: 'Why is the mathematical solution n = 25 rejected in the 200 logs stacking problem?',
              ideal_answer: 'Because for n = 25, the number of logs in the 25th row would be a_25 = 20 + 24(-1) = -4, which is physically impossible.',
              socratic_hint: 'Calculate how many logs would be in the 25th row.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 8,
    title: 'Exercise 5.4 Optional Masterclass & Board HOTS',
    description: 'Rigorous step-by-step solutions for high-order thinking problems in Exercise 5.4: first negative term, ladder rungs, house numbering equality, and football terrace volume.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Solving Linear Inequalities for First Negative Term (a_n < 0)',
      'Dual Solution APs with Sum and Product Constraints',
      'Non-Uniform Ladder Rung Spacing Integration',
      'Symmetric Sum Equalities in House Numbering (S_{x-1} = S_{49} - S_x)',
      '3D Volume Integration via Discrete AP Steps (Football Terrace)'
    ],
    key_concepts: [
      'First Negative Term Condition: a_n < 0 => a + (n-1)d < 0. The smallest integer strictly greater than the resulting bound gives the first negative term.',
      'Symmetric Sum Relation: S_{x-1} = S_{49} - S_x.',
      'Prism Volume as AP: Step k volume = Length * Tread * (k * Rise).'
    ],
    success_criteria: 'Student can solve any 5-mark HOTS board exam problem on Arithmetic Progressions.',
    chapter_notes: `### Exercise 5.4 (Optional / HOTS) Masterclass

- **Q1: First Negative Term of $121, 117, 113, \\dots$**
  - $a = 121, d = -4$.
  - We require $a_n < 0 \\implies 121 + (n-1)(-4) < 0$.
  - $121 - 4n + 4 < 0 \\implies 125 < 4n \\implies n > \\frac{125}{4} = 31.25$.
  - Since $n$ must be an integer, the smallest integer greater than $31.25$ is $n = 32$.
  - Verification: $a_{31} = 121 + 30(-4) = 1$ (last positive); $a_{32} = 121 + 31(-4) = -3$ (first negative).

- **Q2: $a_3 + a_7 = 6$ and $a_3 \\times a_7 = 8$. Find $S_{16}$.**
  - Let terms symmetric about average be $(a+4d) - 2d$ and $(a+4d) + 2d$.
  - $a_3 + a_7 = 2(a + 4d) = 6 \\implies a + 4d = 3$.
  - Product: $(3 - 2d)(3 + 2d) = 8 \\implies 9 - 4d^2 = 8 \\implies 4d^2 = 1 \\implies d = \\pm 1/2$.
  - *Case 1*: If $d = 1/2 \\implies a = 3 - 4(1/2) = 1$.
    $$S_{16} = \\frac{16}{2}[2(1) + 15(1/2)] = 8[2 + 7.5] = 8(9.5) = 76$$
  - *Case 2*: If $d = -1/2 \\implies a = 3 - 4(-1/2) = 5$.
    $$S_{16} = \\frac{16}{2}[2(5) + 15(-1/2)] = 8[10 - 7.5] = 8(2.5) = 20$$.

- **Q3: Ladder Rungs from 45 cm to 25 cm, spaced 25 cm apart over $2\\frac{1}{2}$ m (250 cm).**
  - Number of rungs $n = \\frac{250}{25} + 1 = 10 + 1 = 11$ rungs.
  - Length of wood $= S_{11} = \\frac{11}{2}[45 + 25] = \\frac{11}{2}[70] = 11 \\times 35 = 385$ cm (3.85 m).

- **Q4: Houses numbered 1 to 49. Find $x$ such that $S_{x-1} = S_{49} - S_x$.**
  - Sum of preceding houses $= \\frac{(x-1)x}{2}$.
  - Sum of following houses $= S_{49} - S_x = \\frac{49 \\times 50}{2} - \\frac{x(x+1)}{2}$.
  - $\\frac{x^2 - x}{2} = 1225 - \\frac{x^2 + x}{2} \\implies \\frac{2x^2}{2} = 1225 \\implies x^2 = 1225 \\implies x = 35$.

- **Q5: Football Terrace of 15 steps. Length 50 m, rise 1/4 m, tread 1/2 m.**
  - Volume of step $k = 50 \\times \\frac{1}{2} \\times \\left(k \\times \\frac{1}{4}\\right) = \\frac{25}{4} k$ m³.
  - Total Volume $= \\frac{25}{4} \\sum_{k=1}^{15} k = \\frac{25}{4} \\times \\frac{15 \\times 16}{2} = \\frac{25}{4} \\times 120 = 25 \\times 30 = 750$ m³.`,
    worked_examples: [
      {
        problem: 'Exercise 5.4 Q4: The houses of a row are numbered consecutively from 1 to 49. Show that there is a value of x such that the sum of the numbers of the houses preceding the house numbered x is equal to the sum of the numbers of the houses following it. Find x.',
        given: 'Houses numbered 1 to 49. Condition: S_{x-1} = S_{49} - S_x.',
        formula: 'S_n = n(n + 1)/2',
        substitution: '(x - 1)x / 2 = 49 * 50 / 2 - x(x + 1) / 2',
        calculation: '(x^2 - x)/2 + (x^2 + x)/2 = 1225 => 2x^2 / 2 = 1225 => x^2 = 1225 => x = 35.',
        finalAnswer: 'x = 35',
        unit: 'House number'
      },
      {
        problem: 'Exercise 5.4 Q5: A small terrace at a football ground comprises of 15 steps each of which is 50 m long and built of solid concrete. Each step has a rise of 1/4 m and a tread of 1/2 m. Calculate total volume of concrete.',
        given: 'n = 15 steps, Length = 50 m, Tread = 0.5 m, Step k Height = k * 0.25 m',
        formula: 'Volume of step k = Length * Tread * Height_k = 50 * (1/2) * (k/4) = (25/4)k',
        substitution: 'Total Volume V = (25/4) * [1 + 2 + ... + 15]',
        calculation: 'V = (25/4) * [15 * 16 / 2] = (25/4) * 120 = 25 * 30 = 750 m³.',
        finalAnswer: '750 m³',
        unit: 'Cubic metres'
      }
    ],
    common_misconceptions: [
      'In Q3, forgetting the +1 when calculating number of rungs: (250/25) gives the number of intervals (10), so there are 11 rungs.',
      'In Q4, confusing houses following x: it is S_{49} - S_x (do NOT include house x in the following sum).'
    ],
    ai_system_prompt_context: 'Walk through Q4 and Q5 as classic 5-mark board toppers. Draw the terrace cross-section showing how the heights form an AP.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="90" y="12" width="360" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">Q4: SYMMETRIC HOUSE NUMBERING EQUATION</text>
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="26" fill="#1E40AF" font-weight="bold" font-size="13">Equating Preceding and Succeeding Sums:</text>
    <text x="20" y="50" fill="#0F172A" font-size="13">S_{x-1} = S₄₉ - S_x  ⇒  x(x-1)/2 = (49×50)/2 - x(x+1)/2</text>
    <text x="20" y="75" fill="#2563EB" font-weight="bold" font-size="14">x² = 1225  ⇒  x = 35 (House #35)</text>
  </g>
  <g transform="translate(30, 160)">
    <rect x="0" y="0" width="480" height="100" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="1.2"/>
    <text x="20" y="26" fill="#92400E" font-weight="bold" font-size="13">Q5 Football Terrace Volume AP:</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Step Volume V_k = 50 × (1/2) × (k/4) = (25/4)k m³</text>
    <text x="20" y="75" fill="#D97706" font-weight="bold" font-size="14">Total Concrete = (25/4) × (15×16/2) = 750 m³</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'HOTS AP Mastery',
          questions: [
            {
              q_num: 'Q1',
              type: 'PYQ',
              question: 'Which term of the AP 121, 117, 113, ... is its first negative term? (A) 31st (B) 32nd (C) 33rd (D) 30th',
              ideal_answer: '(B) 32nd term. a_n < 0 gives 121 - 4(n-1) < 0 => 4n > 125 => n > 31.25, so n = 32.',
              socratic_hint: 'Set a_n < 0 and find the first integer n.'
            }
          ]
        }
      ]
    }
  }
];

async function run() {
  console.log('Seeding Chapter 5: Arithmetic Progressions with 8 exhaustive modules...');

  // 1. Delete old modules
  const { error: delErr } = await supabase.from('syllabus_modules').delete().eq('curriculum_id', CH5_ID);
  if (delErr) {
    console.error('Error deleting old modules for Chapter 5:', delErr);
    process.exit(1);
  }
  console.log('Deleted old modules for Chapter 5.');

  // 2. Insert the 8 exhaustive modules
  for (const mod of modules) {
    const { error: insErr } = await supabase.from('syllabus_modules').insert({
      curriculum_id: CH5_ID,
      order_index: mod.order_index,
      title: mod.title,
      description: mod.description,
      board: mod.board,
      class_level: mod.class_level,
      subtopics: mod.subtopics,
      key_concepts: mod.key_concepts,
      success_criteria: mod.success_criteria,
      chapter_notes: mod.chapter_notes,
      worked_examples: mod.worked_examples,
      common_misconceptions: mod.common_misconceptions,
      ai_system_prompt_context: mod.ai_system_prompt_context,
      visual_lesson_plan: mod.visual_lesson_plan,
      estimated_minutes: mod.estimated_minutes
    });
    if (insErr) {
      console.error(`Error inserting Module ${mod.order_index} (${mod.title}):`, insErr);
      process.exit(1);
    }
    console.log(`Inserted Module ${mod.order_index}: ${mod.title}`);
  }

  // 3. Update curriculums estimated_duration_minutes to 160 (8 * 20)
  await supabase.from('curriculums').update({
    estimated_duration_minutes: 160,
    description: 'Complete NCERT-exhaustive masterclass on Arithmetic Progressions with full step-by-step solutions for all 49 exercise questions, 16 textbook examples, and board HOTS.'
  }).eq('id', CH5_ID);

  console.log('Chapter 5 successfully updated in DB with 8 full modules!');
}

run();
