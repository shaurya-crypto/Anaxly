const { supabase } = require('./db_helper');

const CH3_ID = 'aaea72f0-0eac-40db-b575-4ddedd316072';

const modules = [
  {
    order_index: 1,
    title: 'Core Foundations & Graphical Method of Solution',
    description: 'Master the algebraic definition of a pair of linear equations in two variables, the three geometric line behaviors, and ratio consistency criteria (Table 3.1).',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Formulating Two-Variable Linear Equations: a₁x + b₁y + c₁ = 0',
      'The Three Geometric Representations: Intersecting, Coincident, and Parallel Lines',
      'Consistency Definitions: Consistent, Inconsistent, and Dependent Systems',
      'Table 3.1 Ratio Comparison Invariants: a₁/a₂, b₁/b₂, c₁/c₂',
      'Graphical Solution Mechanics and Verifying Points of Intersection'
    ],
    key_concepts: [
      'General Form: a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0, where a₁² + b₁² ≠ 0 and a₂² + b₂² ≠ 0.',
      'Unique Solution (Consistent): a₁/a₂ ≠ b₁/b₂ => Lines intersect at exactly one point.',
      'Infinitely Many Solutions (Dependent Consistent): a₁/a₂ = b₁/b₂ = c₁/c₂ => Lines coincide.',
      'No Solution (Inconsistent): a₁/a₂ = b₁/b₂ ≠ c₁/c₂ => Lines are parallel and never meet.'
    ],
    success_criteria: 'Student can classify any pair of linear equations as consistent or inconsistent using ratio comparison without plotting.',
    chapter_notes: `### 3.1 & 3.2 Pair of Linear Equations in Two Variables

#### Algebraic Formulation
A general pair of linear equations in two variables $x$ and $y$ is given by:
$$a_1 x + b_1 y + c_1 = 0$$
$$a_2 x + b_2 y + c_2 = 0$$
where $a_1, b_1, c_1, a_2, b_2, c_2$ are real numbers such that $a_1^2 + b_1^2 \\ne 0$ and $a_2^2 + b_2^2 \\ne 0$.

#### Geometric & Algebraic Consistency (Table 3.1)
1. **Intersecting Lines**:
   $$\\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2}$$
   - **Graphical Representation**: Exactly one point of intersection $(x, y)$.
   - **Algebraic Interpretation**: Unique solution.
   - **System Nature**: **Consistent**.

2. **Coincident Lines**:
   $$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$$
   - **Graphical Representation**: One line lies directly on top of the other.
   - **Algebraic Interpretation**: Infinitely many common solutions.
   - **System Nature**: **Dependent and Consistent**.

3. **Parallel Lines**:
   $$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2}$$
   - **Graphical Representation**: Lines run parallel with constant perpendicular distance; never intersect.
   - **Algebraic Interpretation**: No solution.
   - **System Nature**: **Inconsistent**.`,
    worked_examples: [
      {
        problem: 'Example 1: Check graphically whether the pair of equations x + 3y = 6 and 2x - 3y = 12 is consistent. If so, solve them graphically.',
        given: 'Equation 1: x + 3y = 6; Equation 2: 2x - 3y = 12',
        formula: 'Table 3.1: Compare a_1/a_2 and b_1/b_2',
        substitution: 'a_1 = 1, b_1 = 3, c_1 = -6; a_2 = 2, b_2 = -3, c_2 = -12. a_1/a_2 = 1/2, b_1/b_2 = 3/(-3) = -1.',
        calculation: 'Since a_1/a_2 ≠ b_1/b_2 (1/2 ≠ -1), the lines intersect at a unique point. Points for line 1: (0, 2), (6, 0). Points for line 2: (0, -4), (3, -2), (6, 0). Common intersection point is (6, 0).',
        finalAnswer: 'Consistent with unique solution x = 6, y = 0',
        unit: 'Coordinate point'
      },
      {
        problem: 'Example 2: Graphically find whether 5x - 8y + 1 = 0 and 3x - 24/5 y + 3/5 = 0 has no solution, unique solution, or infinitely many solutions.',
        given: 'Eq 1: 5x - 8y + 1 = 0; Eq 2: 3x - (24/5)y + 3/5 = 0',
        formula: 'Multiply Eq 2 by 5/3',
        substitution: '(5/3) * [3x - (24/5)y + 3/5] = 5x - 8y + 1 = 0',
        calculation: 'Eq 2 reduces to Eq 1. a_1/a_2 = 5/3, b_1/b_2 = -8/(-24/5) = 40/24 = 5/3, c_1/c_2 = 1/(3/5) = 5/3. All three ratios are equal.',
        finalAnswer: 'Infinitely many solutions (Coincident lines)',
        unit: 'Infinite set'
      },
      {
        problem: 'Example 3: Champa bought pants and skirts. Number of skirts is two less than twice pants: y = 2x - 2. Skirts is four less than four times pants: y = 4x - 4. Find number of pants and skirts.',
        given: 'y = 2x - 2 and y = 4x - 4, where x = pants, y = skirts',
        formula: 'Equate y: 2x - 2 = 4x - 4',
        substitution: '4x - 2x = 4 - 2 => 2x = 2 => x = 1',
        calculation: 'y = 2(1) - 2 = 0. Point of intersection is (1, 0).',
        finalAnswer: 'Champa purchased 1 pant and 0 skirts',
        unit: 'Garments count'
      }
    ],
    common_misconceptions: [
      'Assuming coincident lines have no solution: coincident lines have INFINITELY MANY solutions and are called dependent consistent.',
      'Forgetting the negative sign of constants when comparing c_1/c_2. Always write equations in standard form a_i x + b_i y + c_i = 0.'
    ],
    ai_system_prompt_context: 'Teach Table 3.1 with clarity. Draw the three geometric line cases on the chalkboard before doing Example 1.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="110" y="12" width="320" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">THE THREE GEOMETRIC LINE CASES (TABLE 3.1)</text>
  <g transform="translate(25, 55)">
    <rect x="0" y="0" width="155" height="205" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="77" y="24" text-anchor="middle" fill="#1E40AF" font-weight="bold" font-size="12">1. Intersecting</text>
    <line x1="20" y1="120" x2="135" y2="40" stroke="#2563EB" stroke-width="2"/>
    <line x1="20" y1="40" x2="135" y2="120" stroke="#DC2626" stroke-width="2"/>
    <circle cx="77" cy="80" r="5" fill="#16A34A"/>
    <text x="77" y="150" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold">a₁/a₂ ≠ b₁/b₂</text>
    <text x="77" y="170" text-anchor="middle" fill="#16A34A" font-size="11" font-weight="bold">Unique Solution</text>
    <text x="77" y="190" text-anchor="middle" fill="#475569" font-size="10">Consistent</text>
  </g>
  <g transform="translate(192, 55)">
    <rect x="0" y="0" width="155" height="205" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="77" y="24" text-anchor="middle" fill="#166534" font-weight="bold" font-size="12">2. Coincident</text>
    <line x1="20" y1="100" x2="135" y2="60" stroke="#16A34A" stroke-width="4"/>
    <line x1="20" y1="100" x2="135" y2="60" stroke="#22C55E" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="77" y="150" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold">a₁/a₂ = b₁/b₂ = c₁/c₂</text>
    <text x="77" y="170" text-anchor="middle" fill="#166534" font-size="11" font-weight="bold">Infinite Solutions</text>
    <text x="77" y="190" text-anchor="middle" fill="#475569" font-size="10">Dependent</text>
  </g>
  <g transform="translate(360, 55)">
    <rect x="0" y="0" width="155" height="205" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.2"/>
    <text x="77" y="24" text-anchor="middle" fill="#991B1B" font-weight="bold" font-size="12">3. Parallel</text>
    <line x1="20" y1="70" x2="135" y2="70" stroke="#DC2626" stroke-width="2"/>
    <line x1="20" y1="100" x2="135" y2="100" stroke="#DC2626" stroke-width="2"/>
    <text x="77" y="150" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold">a₁/a₂ = b₁/b₂ ≠ c₁/c₂</text>
    <text x="77" y="170" text-anchor="middle" fill="#DC2626" font-size="11" font-weight="bold">No Solution</text>
    <text x="77" y="190" text-anchor="middle" fill="#475569" font-size="10">Inconsistent</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Consistency Conditions',
          questions: [
            {
              q_num: 'Q1',
              type: '1-mark MCQ',
              question: 'If a pair of linear equations has no solution, what is the graphical relationship between their lines? (A) Intersecting (B) Parallel (C) Coincident (D) Perpendicular',
              ideal_answer: '(B) Parallel lines. They have the same slope and never intersect, resulting in no common solution.',
              socratic_hint: 'When do two lines never share a single point?'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 2,
    title: 'Exercise 3.1 Complete Step-by-Step Question Solver (Q1 to Q7)',
    description: 'Comprehensive scratchpad solutions for Exercise 3.1 Questions 1 to 7: graphical problem formulation, ratio condition checks, garden perimeter, and triangle vertices with x-axis.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Formulating and Graphically Solving Quiz and Pencil-Pen Word Problems',
      'Ratio Comparisons to Test Intersecting, Parallel, and Coincident Lines',
      'Determining System Consistency and Inconsistency (Q3 & Q4)',
      'Rectangular Garden Perimeter Word Problem Analysis',
      'Constructing Parallel, Intersecting, and Coincident Counterparts',
      'Finding Coordinates of Triangle Vertices Formed with the X-Axis'
    ],
    key_concepts: [
      'Formulation Rule: Assign x and y to unknown quantities, create two independent equations, and solve.',
      'Triangle Vertices with X-Axis: Find the mutual intersection point of the two lines, and find the x-intercepts of each line by setting y = 0.'
    ],
    success_criteria: 'Student can solve all problems in Exercise 3.1 and find triangle boundary coordinates.',
    chapter_notes: `### Exercise 3.1 Comprehensive Solutions

- **Q1(i)**: 10 students in Class X quiz. Girls ($y$) is 4 more than boys ($x$).
  - Equations: $x + y = 10$ and $y = x + 4$.
  - Points for $x + y = 10$: $(0, 10), (10, 0), (5, 5)$.
  - Points for $y - x = 4$: $(0, 4), (2, 6), (3, 7)$.
  - Point of intersection: **$(3, 7)$**. 3 boys, 7 girls.

- **Q1(ii)**: 5 pencils and 7 pens cost ₹50; 7 pencils and 5 pens cost ₹46.
  - $5x + 7y = 50$ and $7x + 5y = 46$.
  - Multiply Eq 1 by 5: $25x + 35y = 250$.
  - Multiply Eq 2 by 7: $49x + 35y = 322$.
  - $24x = 72 \\implies x = 3$ (Cost of pencil = ₹3).
  - $5(3) + 7y = 50 \\implies 7y = 35 \\implies y = 5$ (Cost of pen = ₹5).

- **Q2**: Ratio Comparisons
  - (i) $5x - 4y + 8 = 0$ and $7x + 6y - 9 = 0 \\implies 5/7 \\ne -4/6 \\implies$ **Intersecting at a point**.
  - (ii) $9x + 3y + 12 = 0$ and $18x + 6y + 24 = 0 \\implies 9/18 = 3/6 = 12/24 = 1/2 \\implies$ **Coincident lines**.
  - (iii) $6x - 3y + 10 = 0$ and $2x - y + 9 = 0 \\implies 6/2 = -3/(-1) \\ne 10/9 \\implies 3 = 3 \\ne 10/9 \\implies$ **Parallel lines**.

- **Q3 & Q4**: Consistency
  - $3x + 2y = 5$ and $2x - 3y = 7 \\implies 3/2 \\ne -2/3 \\implies$ **Consistent**.
  - $2x - 3y = 8$ and $4x - 6y = 9 \\implies 2/4 = -3/(-6) \\ne 8/9 \\implies$ **Inconsistent**.
  - $4x - 2y - 4 = 0$ and $2x + y - 6 = 0 \\implies 2/1 \\ne -1/1 \\implies$ **Consistent**, intersects at $(2, 2)$.

- **Q5**: Rectangular Garden. Length is 4 m more than width ($l = w + 4$). Half perimeter is 36 m ($l + w = 36$).
  - $(w + 4) + w = 36 \\implies 2w = 32 \\implies w = 16$ m.
  - Length $l = 16 + 4 = 20$ m.

- **Q6**: Given $2x + 3y - 8 = 0$:
  - (i) Intersecting: $3x + 2y - 7 = 0$ (since $2/3 \\ne 3/2$)
  - (ii) Parallel: $2x + 3y - 12 = 0$ (since $2/2 = 3/3 \\ne -8/(-12)$)
  - (iii) Coincident: $4x + 6y - 16 = 0$ (since $2/4 = 3/6 = -8/(-16)$)

- **Q7**: Lines $x - y + 1 = 0$ and $3x + 2y - 12 = 0$.
  - Line 1: $y = x + 1$. X-intercept ($y=0$): $x = -1 \\implies (-1, 0)$.
  - Line 2: $3x + 2y = 12$. X-intercept ($y=0$): $3x = 12 \\implies x = 4 \\implies (4, 0)$.
  - Intersection point: $y = x + 1 \\implies 3x + 2(x + 1) = 12 \\implies 5x = 10 \\implies x = 2, y = 3 \\implies (2, 3)$.
  - **Vertices of the triangle**: **$(-1, 0), (4, 0), (2, 3)$**.`,
    worked_examples: [
      {
        problem: 'Exercise 3.1 Q7: Draw the graphs of x - y + 1 = 0 and 3x + 2y - 12 = 0. Determine the coordinates of the vertices of the triangle formed by these lines and the x-axis, and shade the triangular region.',
        given: 'Line 1: x - y + 1 = 0; Line 2: 3x + 2y - 12 = 0; Base on X-axis (y = 0)',
        formula: 'Find intersection of Line 1 and Line 2, and x-intercepts of each line',
        substitution: 'For Line 1: y = x + 1. For Line 2: 3x + 2(x + 1) = 12',
        calculation: '5x + 2 = 12 => 5x = 10 => x = 2, y = 3. Top vertex = (2, 3). Line 1 with x-axis: x - 0 + 1 = 0 => x = -1 => Left vertex = (-1, 0). Line 2 with x-axis: 3x + 0 - 12 = 0 => 3x = 12 => x = 4 => Right vertex = (4, 0).',
        finalAnswer: 'Vertices: (-1, 0), (4, 0), (2, 3)',
        unit: 'Coordinate triplets'
      }
    ],
    common_misconceptions: [
      'In Q7, students often find the y-intercepts instead of the x-intercepts. The problem explicitly says "with the x-axis" (so y = 0).',
      'In Q5, students sometimes use 2(l+w) = 36 instead of half perimeter l+w = 36.'
    ],
    ai_system_prompt_context: 'Plot Q7 on the digital whiteboard step-by-step: plot line 1, plot line 2, identify the 3 vertices, and shade the triangle.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="100" y="10" width="340" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="26" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">EXERCISE 3.1 Q7: TRIANGLE FORMED WITH X-AXIS</text>
  <g transform="translate(60, 50)">
    <line x1="20" y1="160" x2="400" y2="160" stroke="#0F172A" stroke-width="2"/>
    <text x="410" y="165" fill="#0F172A" font-size="12" font-weight="bold">X</text>
    <line x1="120" y1="10" x2="120" y2="190" stroke="#0F172A" stroke-width="1.5"/>
    <text x="120" y="8" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold">Y</text>
    <polygon points="80,160 280,160 200,40" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
    <circle cx="80" cy="160" r="4" fill="#DC2626"/>
    <text x="70" y="180" text-anchor="middle" fill="#DC2626" font-weight="bold" font-size="11">A(-1, 0)</text>
    <circle cx="280" cy="160" r="4" fill="#DC2626"/>
    <text x="290" y="180" text-anchor="middle" fill="#DC2626" font-weight="bold" font-size="11">B(4, 0)</text>
    <circle cx="200" cy="40" r="4" fill="#16A34A"/>
    <text x="200" y="30" text-anchor="middle" fill="#16A34A" font-weight="bold" font-size="11">C(2, 3)</text>
    <text x="200" y="115" text-anchor="middle" fill="#2563EB" font-size="12" font-weight="bold">Shaded Region Area = ½ × 5 × 3 = 7.5 sq units</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Exercise 3.1 Problem Solving',
          questions: [
            {
              q_num: 'Q1',
              type: 'PYQ',
              question: 'The vertices of the triangle formed by x - y + 1 = 0, 3x + 2y - 12 = 0 and the x-axis are: (A) (0,1), (0,6), (2,3) (B) (-1,0), (4,0), (2,3) (C) (1,0), (-4,0), (3,2) (D) (0,-1), (0,4), (3,2)',
              ideal_answer: '(B) (-1, 0), (4, 0), and (2, 3).',
              socratic_hint: 'Find the x-intercepts by setting y = 0, then solve for the intersection.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 3,
    title: 'The Substitution Method: Mechanics & Worked Examples (Examples 4 to 7)',
    description: 'Master the algebraic mechanics of substitution, understand identity cases (18=18 infinitely many) vs false cases (-4=0 no solution), and solve Examples 4 to 7.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      '3-Step Algorithmic Protocol of the Substitution Method',
      'Solving Non-Integral Systems (Fractions and Decimals)',
      'Aftab and Daughter Age Modeling via Substitution',
      'Recognizing Coincident Systems (True Statements with Zero Variables)',
      'Recognizing Inconsistent Systems (False Statements with Zero Variables)'
    ],
    key_concepts: [
      'Substitution Step 1: Express one variable completely in terms of the other from either equation.',
      'Substitution Step 2: Substitute this expression into the OTHER equation (never the same equation).',
      'True Statement (e.g. 18 = 18): Indicates infinitely many solutions (coincident lines).',
      'False Statement (e.g. -4 = 0): Indicates no solution (parallel lines).'
    ],
    success_criteria: 'Student can solve any algebraic linear system using substitution and correctly interpret degenerate statements.',
    chapter_notes: `### 3.3.1 The Substitution Method

#### Step-by-Step Methodical Protocol
1. **Step 1**: Pick the simpler equation and express one variable (say $x$) in terms of the other variable ($y$):
   $$x = g(y)$$
2. **Step 2**: Substitute this expression into the **other** equation. This reduces it to a single linear equation in $y$.
3. **Step 3**: Solve for $y$.
4. **Step 4**: Substitute the numerical value of $y$ back into $x = g(y)$ to find $x$.

#### Handling Degenerate Statements
- If substitution yields a **true statement with no variables** (such as $18 = 18$ or $0 = 0$), the original pair has **infinitely many solutions** (Example 6).
- If substitution yields a **false statement with no variables** (such as $-4 = 0$ or $8 = 12$), the original pair has **no solution** and is inconsistent (Example 7).`,
    worked_examples: [
      {
        problem: 'Example 4: Solve 7x - 15y = 2 and x + 2y = 3 by substitution method.',
        given: 'Eq (1): 7x - 15y = 2; Eq (2): x + 2y = 3',
        formula: 'From Eq (2): x = 3 - 2y. Substitute in Eq (1).',
        substitution: '7(3 - 2y) - 15y = 2',
        calculation: '21 - 14y - 15y = 2 => 21 - 29y = 2 => 29y = 19 => y = 19/29. Then x = 3 - 2(19/29) = 3 - 38/29 = (87 - 38) / 29 = 49/29.',
        finalAnswer: 'x = 49/29, y = 19/29',
        unit: 'Fractional coordinates'
      },
      {
        problem: 'Example 5: Aftab tells his daughter: "7 years ago I was 7 times as old as you were then. 3 years from now I shall be 3 times as old as you will be." Find their present ages.',
        given: 'Let Aftab age = s, Daughter age = t. Condition 1: s - 7 = 7(t - 7); Condition 2: s + 3 = 3(t + 3)',
        formula: 'Substitution method',
        substitution: 'From (2): s = 3t + 6. Substitute in (1): (3t + 6) - 7t + 42 = 0',
        calculation: '-4t + 48 = 0 => 4t = 48 => t = 12. Then s = 3(12) + 6 = 36 + 6 = 42.',
        finalAnswer: 'Aftab is 42 years old, and his daughter is 12 years old',
        unit: 'Years'
      },
      {
        problem: 'Example 7: Two railroad tracks: x + 2y - 4 = 0 and 2x + 4y - 12 = 0. Will the rails cross each other?',
        given: 'Eq (1): x = 4 - 2y; Eq (2): 2x + 4y - 12 = 0',
        formula: 'Substitute x in Eq (2)',
        substitution: '2(4 - 2y) + 4y - 12 = 0',
        calculation: '8 - 4y + 4y - 12 = 0 => 8 - 12 = 0 => -4 = 0 (False statement)',
        finalAnswer: 'The rails will never cross (no common solution, parallel lines)',
        unit: 'Physical conclusion'
      }
    ],
    common_misconceptions: [
      'Substituting x = 3 - 2y back into equation (2) instead of equation (1): this gives 3 = 3 without solving anything!',
      'Thinking a fractional answer like 49/29 is wrong. Board exams frequently test non-integer solutions.'
    ],
    ai_system_prompt_context: 'Walk through Example 4 carefully on the board. Show the student why substituting into the SAME equation leads to a circular identity.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="110" y="12" width="320" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">SUBSTITUTION METHOD: ALGORITHMIC PIPELINE</text>
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="140" height="90" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="70" y="25" text-anchor="middle" fill="#1E40AF" font-weight="bold" font-size="12">Step 1: Isolate</text>
    <text x="70" y="55" text-anchor="middle" fill="#0F172A" font-size="11">From Eq (2):</text>
    <text x="70" y="75" text-anchor="middle" fill="#2563EB" font-weight="bold" font-size="13">x = 3 - 2y</text>
  </g>
  <path d="M 175 100 L 205 100" stroke="#16A34A" stroke-width="2" marker-end="url(#axisArrow)"/>
  <g transform="translate(210, 55)">
    <rect x="0" y="0" width="140" height="90" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="70" y="25" text-anchor="middle" fill="#166534" font-weight="bold" font-size="12">Step 2: Substitute</text>
    <text x="70" y="55" text-anchor="middle" fill="#0F172A" font-size="11">Into Eq (1):</text>
    <text x="70" y="75" text-anchor="middle" fill="#16A34A" font-weight="bold" font-size="12">7(3 - 2y) - 15y = 2</text>
  </g>
  <path d="M 355 100 L 385 100" stroke="#16A34A" stroke-width="2"/>
  <g transform="translate(390, 55)">
    <rect x="0" y="0" width="120" height="90" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="1.2"/>
    <text x="60" y="25" text-anchor="middle" fill="#92400E" font-weight="bold" font-size="12">Step 3: Solve</text>
    <text x="60" y="55" text-anchor="middle" fill="#D97706" font-weight="bold" font-size="13">y = 19/29</text>
    <text x="60" y="75" text-anchor="middle" fill="#2563EB" font-weight="bold" font-size="13">x = 49/29</text>
  </g>
  <rect x="30" y="165" width="480" height="90" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
  <text x="270" y="195" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold">Degenerate Condition Check:</text>
  <text x="270" y="220" text-anchor="middle" fill="#475569" font-size="11">Variables disappear to 18 = 18 (True) ⇒ Infinite Solutions | -4 = 0 (False) ⇒ No Solution</text>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Substitution Mechanics',
          questions: [
            {
              q_num: 'Q1',
              type: '2-mark Definition',
              question: 'When solving a pair of linear equations by substitution, what does obtaining the statement "18 = 18" indicate?',
              ideal_answer: 'It indicates that the two equations are dependent and coincident, meaning there are infinitely many common solutions.',
              socratic_hint: 'Since 18 = 18 is true for all values of y, what does it mean for the lines?'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 4,
    title: 'Exercise 3.2 Step-by-Step Substitution Solver Part 1: Direct Algebraic Systems (Q1 & Q2)',
    description: 'Exhaustive step-by-step scratchpad solutions for Exercise 3.2 Question 1 (all 6 parts) and Question 2 finding m for y = mx + 3.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Solving Direct Integer Systems (Q1(i))',
      'Fractional and LCM Pre-Processing (Q1(ii) and Q1(vi))',
      'Decimal Normalization Techniques (Q1(iv))',
      'Square Root Radical Systems (Q1(v))',
      'Finding the Slope Parameter m in y = mx + 3 (Q2)'
    ],
    key_concepts: [
      'Decimal Trick: Multiply by 10 across both equations to convert decimal coefficients to integers.',
      'Radical Trick: In √2x + √3y = 0 and √3x - √8y = 0, both lines pass through origin (0, 0).'
    ],
    success_criteria: 'Student can solve any fractional, decimal, or radical linear system using substitution.',
    chapter_notes: `### Exercise 3.2 (Q1 & Q2) Solutions

- **Q1(i)**: $x + y = 14$ and $x - y = 4$.
  - From (2): $x = y + 4$.
  - $(y + 4) + y = 14 \\implies 2y = 10 \\implies y = 5, x = 9$.

- **Q1(ii)**: $s - t = 3$ and $s/3 + t/2 = 6$.
  - Multiply Eq 2 by 6: $2s + 3t = 36$.
  - From (1): $s = t + 3 \\implies 2(t + 3) + 3t = 36 \\implies 5t = 30 \\implies t = 6, s = 9$.

- **Q1(iii)**: $3x - y = 3$ and $9x - 3y = 9$.
  - From (1): $y = 3x - 3$.
  - Substitute into (2): $9x - 3(3x - 3) = 9 \\implies 9x - 9x + 9 = 9 \\implies 9 = 9$ (True statement).
  - **Infinitely many solutions** where $y = 3x - 3$.

- **Q1(iv)**: $0.2x + 0.3y = 1.3$ and $0.4x + 0.5y = 2.3$.
  - Multiply both by 10: $2x + 3y = 13$ and $4x + 5y = 23$.
  - $x = (13 - 3y)/2 \\implies 4((13 - 3y)/2) + 5y = 23 \\implies 26 - 6y + 5y = 23 \\implies -y = -3 \\implies y = 3, x = 2$.

- **Q1(v)**: $\\sqrt{2}x + \\sqrt{3}y = 0$ and $\\sqrt{3}x - \\sqrt{8}y = 0$.
  - $x = -\\frac{\\sqrt{3}}{\\sqrt{2}}y \\implies \\sqrt{3}\\left(-\\frac{\\sqrt{3}}{\\sqrt{2}}y\\right) - \\sqrt{8}y = 0$.
  - $-\\frac{3}{\\sqrt{2}}y - \\frac{4}{\\sqrt{2}}y = 0 \\implies -\\frac{7}{\\sqrt{2}}y = 0 \\implies y = 0, x = 0$.

- **Q1(vi)**: $\\frac{3x}{2} - \\frac{5y}{3} = -2$ and $\\frac{x}{3} + \\frac{y}{2} = \\frac{13}{6}$.
  - Multiply both by 6: $9x - 10y = -12$ and $2x + 3y = 13$.
  - $x = (13 - 3y)/2 \\implies 9((13 - 3y)/2) - 10y = -12 \\implies 117 - 27y - 20y = -24 \\implies -47y = -141 \\implies y = 3$.
  - $x = (13 - 9)/2 = 2$. Solution: **$(2, 3)$**.

- **Q2**: $2x + 3y = 11$ and $2x - 4y = -24$. Find $m$ for $y = mx + 3$.
  - From (1): $2x = 11 - 3y$. Substitute into (2): $(11 - 3y) - 4y = -24 \\implies -7y = -35 \\implies y = 5$.
  - $2x = 11 - 15 = -4 \\implies x = -2$.
  - Substitute into $y = mx + 3$: $5 = m(-2) + 3 \\implies -2m = 2 \\implies m = -1$.`,
    worked_examples: [
      {
        problem: 'Exercise 3.2 Q2: Solve 2x + 3y = 11 and 2x - 4y = -24 and hence find the value of "m" for which y = mx + 3.',
        given: 'Eq 1: 2x + 3y = 11; Eq 2: 2x - 4y = -24; Target equation: y = mx + 3',
        formula: 'Solve for x and y by substitution, then plug into y = mx + 3',
        substitution: '2x = 11 - 3y => (11 - 3y) - 4y = -24',
        calculation: '11 - 7y = -24 => -7y = -35 => y = 5. Then 2x = 11 - 15 = -4 => x = -2. Plugging into y = mx + 3: 5 = m(-2) + 3 => 2 = -2m => m = -1.',
        finalAnswer: 'x = -2, y = 5, m = -1',
        unit: 'Scalar m'
      },
      {
        problem: 'Exercise 3.2 Q1(v): Solve √2x + √3y = 0 and √3x - √8y = 0 by substitution method.',
        given: 'Eq 1: √2x + √3y = 0; Eq 2: √3x - √8y = 0',
        formula: 'x = (-√3/√2)y',
        substitution: '√3 * (-√3/√2 y) - 2√2 y = 0',
        calculation: '(-3/√2 - 4/√2) y = 0 => (-7/√2) y = 0 => y = 0. Then x = (-√3/√2)(0) = 0.',
        finalAnswer: 'x = 0, y = 0',
        unit: 'Origin coordinates'
      }
    ],
    common_misconceptions: [
      'In Q1(v), students often get intimidated by square roots. Since constant terms are 0, both lines pass through origin (0, 0).',
      'In Q2, forgetting to solve for m after finding x and y.'
    ],
    ai_system_prompt_context: 'Demonstrate Q1(vi) clearing denominators by multiplying by LCM 6 on the board.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="90" y="12" width="360" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">Q2 MASTER SOLVER: FINDING PARAMETER m</text>
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="480" height="90" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="26" fill="#1E40AF" font-weight="bold" font-size="13">1. Solve Simultaneous Equations:</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">2x + 3y = 11  AND  2x - 4y = -24  ⇒  7y = 35  ⇒  y = 5</text>
    <text x="20" y="72" fill="#2563EB" font-weight="bold" font-size="13">2x = 11 - 15 = -4  ⇒  x = -2 (Solution: (-2, 5))</text>
  </g>
  <g transform="translate(30, 160)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="20" y="26" fill="#166534" font-weight="bold" font-size="13">2. Substitute into y = mx + 3:</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">5 = m(-2) + 3  ⇒  5 - 3 = -2m  ⇒  2 = -2m</text>
    <text x="20" y="75" fill="#16A34A" font-weight="bold" font-size="14">m = -1 (Final Boxed Value)</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Parameter Finding',
          questions: [
            {
              q_num: 'Q1',
              type: 'PYQ',
              question: 'If 2x + 3y = 11 and 2x - 4y = -24, what is the value of m for which y = mx + 3? (A) 1 (B) -1 (C) 2 (D) -2',
              ideal_answer: '(B) m = -1. Since x = -2 and y = 5, 5 = -2m + 3 gives m = -1.',
              socratic_hint: 'Substitute the values of x and y into the equation.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 5,
    title: 'Exercise 3.2 Step-by-Step Substitution Solver Part 2: Real-World Word Problems (Q3 All Parts)',
    description: 'Complete algebraic substitution solutions for Exercise 3.2 Question 3 word problems: supplementary angles, cricket equipment, taxi rates, fractions, and age word problems.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Number Theory and Supplementary Angles (Q3(i) & Q3(ii))',
      'Sports Equipment Purchases (Bats and Balls Q3(iii))',
      'Two-Part City Taxi Fare Modeling: Fixed + per km (Q3(iv))',
      'Fraction Numerator/Denominator Alterations (Q3(v))',
      'Future and Past Age Relationships: Jacob and Son (Q3(vi))'
    ],
    key_concepts: [
      'Taxi Fare Model: Total Cost = Fixed Charge + (Distance * Rate per km).',
      'Age Word Problem Rule: When shifting t years in future/past, BOTH ages change by +t or -t.'
    ],
    success_criteria: 'Student can translate English word problems into two-variable linear equations and solve via substitution.',
    chapter_notes: `### Exercise 3.2 Q3 Word Problem Solutions

- **Q3(i)**: Difference between two numbers is 26, one is 3 times the other.
  - $x - y = 26$ and $x = 3y$.
  - $3y - y = 26 \\implies 2y = 26 \\implies y = 13, x = 39$. Numbers are **39 and 13**.

- **Q3(ii)**: Larger of two supplementary angles exceeds smaller by 18°.
  - $x + y = 180$ and $x - y = 18$.
  - $x = y + 18 \\implies (y + 18) + y = 180 \\implies 2y = 162 \\implies y = 81^\\circ, x = 99^\\circ$.

- **Q3(iii)**: Cricket coach: 7 bats, 6 balls cost ₹3800; 3 bats, 5 balls cost ₹1750.
  - $7x + 6y = 3800$ and $3x + 5y = 1750$.
  - From (2): $x = (1750 - 5y)/3$.
  - $7((1750 - 5y)/3) + 6y = 3800 \\implies 12250 - 35y + 18y = 11400 \\implies -17y = -850 \\implies y = 50$.
  - $x = (1750 - 250)/3 = 500$. **Bat = ₹500, Ball = ₹50**.

- **Q3(iv)**: City Taxi: Fixed charge $x$, charge per km $y$.
  - 10 km costs ₹105: $x + 10y = 105$.
  - 15 km costs ₹155: $x + 15y = 155$.
  - Subtracting: $5y = 50 \\implies y = \\text{₹ } 10$/km.
  - $x + 10(10) = 105 \\implies x = \\text{₹ } 5$ (Fixed charge).
  - For 25 km: Cost $= x + 25y = 5 + 25(10) = \\text{₹ } 255$.

- **Q3(v)**: Fraction becomes $9/11$ if 2 added to numerator and denominator: $\\frac{x+2}{y+2} = \\frac{9}{11} \\implies 11x - 9y = -4$.
  - Becomes $5/6$ if 3 added: $\\frac{x+3}{y+3} = \\frac{5}{6} \\implies 6x - 5y = -3$.
  - Solving gives $x = 7, y = 9$. **Fraction is $7/9$**.

- **Q3(vi)**: Jacob and son. 5 years hence: $j + 5 = 3(s + 5) \\implies j - 3s = 10$.
  - 5 years ago: $j - 5 = 7(s - 5) \\implies j - 7s = -30$.
  - Subtracting: $4s = 40 \\implies s = 10$ years (son), $j = 40$ years (Jacob).`,
    worked_examples: [
      {
        problem: 'Exercise 3.2 Q3(iv): The taxi charges in a city consist of a fixed charge together with the charge for the distance covered. For a distance of 10 km, the charge paid is ₹105 and for a journey of 15 km, the charge paid is ₹155. What are the fixed charges and the charge per km? How much does a person have to pay for travelling a distance of 25 km?',
        given: '10 km => ₹105; 15 km => ₹155. Let fixed charge = x, per km rate = y.',
        formula: 'Total Cost = x + d * y',
        substitution: 'x + 10y = 105 (eq 1); x + 15y = 155 (eq 2)',
        calculation: 'From (1): x = 105 - 10y. Substitute in (2): (105 - 10y) + 15y = 155 => 5y = 50 => y = ₹10/km. Fixed charge x = 105 - 10(10) = ₹5. For 25 km: Cost = 5 + 25(10) = 5 + 250 = ₹255.',
        finalAnswer: 'Fixed charge = ₹5, Rate per km = ₹10, Cost for 25 km = ₹255',
        unit: 'Currency (₹)'
      }
    ],
    common_misconceptions: [
      'In age problems, forgetting to change both ages: Jacob is j+5 and son is s+5 (not s).',
      'In fraction problems, adding 2 to the entire fraction instead of to numerator and denominator separately.'
    ],
    ai_system_prompt_context: 'Structure the whiteboard into two columns: algebraic translation on the left, step-by-step substitution on the right.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="90" y="12" width="360" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">Q3(iv): TAXI FARE LINEAR STRUCTURE</text>
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="480" height="90" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="26" fill="#1E40AF" font-weight="bold" font-size="13">Total Cost Equation: C(d) = x + d × y</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">10 km Journey: x + 10y = 105  (1)</text>
    <text x="20" y="70" fill="#0F172A" font-size="12">15 km Journey: x + 15y = 155  (2)</text>
    <text x="280" y="60" fill="#16A34A" font-weight="bold" font-size="13">5y = 50  ⇒  y = ₹10/km</text>
  </g>
  <g transform="translate(30, 160)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="20" y="26" fill="#166534" font-weight="bold" font-size="13">Result for 25 km Journey:</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Fixed Charge: x = 105 - 10(10) = ₹5</text>
    <text x="20" y="75" fill="#16A34A" font-weight="bold" font-size="14">Total Cost = ₹5 + 25(₹10) = ₹255</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Real-Life Linear Modeling',
          questions: [
            {
              q_num: 'Q1',
              type: 'Competency',
              question: 'In the taxi fare model, what does the constant term x represent physically?',
              ideal_answer: 'It represents the fixed boarding fee charged regardless of distance traveled.',
              socratic_hint: 'What do you have to pay even if you travel 0 km?'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 6,
    title: 'The Elimination Method: Mechanics & Worked Examples (Examples 8 to 10)',
    description: 'Master variable elimination via multiplier coefficients, understand algebraic elimination steps, and solve NCERT Examples 8, 9, and 10.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Multiplication by Non-Zero Constants to Equalize Coefficients',
      'Deciding Between Adding vs Subtracting Equations',
      'Income and Expenditure Ratio Problems (Example 8)',
      'Identifying False Elimination Statements: 0 = 9 (Example 9)',
      'Two-Digit Number and Reversed Digit Analysis (Example 10)'
    ],
    key_concepts: [
      'Elimination Rule: Multiply equations by constants such that the coefficients of one variable become equal or opposite, then add/subtract.',
      'Digit Reversal Invariant: If tens digit is x and units digit is y, original number is 10x + y, and reversed number is 10y + x.'
    ],
    success_criteria: 'Student can solve any two-digit number or ratio word problem using elimination.',
    chapter_notes: `### 3.3.2 The Elimination Method

#### 4-Step Elimination Protocol
1. **Step 1**: Multiply both equations by suitable non-zero constants to make the coefficients of one variable (either $x$ or $y$) numerically equal.
2. **Step 2**: Add or subtract the equations to eliminate that variable:
   - If signs are **opposite**, **ADD**.
   - If signs are **same**, **SUBTRACT**.
3. **Step 3**: Solve the resulting single-variable equation.
4. **Step 4**: Substitute back into either original equation to find the other variable.

#### Two-Digit Number Mechanics (Example 10)
Let tens digit be $x$ and units digit be $y$:
- Original Number: $N = 10x + y$
- Reversed Number: $N' = 10y + x$
- Sum of Number and Reversed:
  $$(10x + y) + (10y + x) = 11(x + y)$$
- Difference of Digits: $|x - y| = 2 \\implies x - y = 2$ OR $y - x = 2$.
- Gives two distinct valid answers: **42** and **24**.`,
    worked_examples: [
      {
        problem: 'Example 8: Ratio of incomes of two persons is 9:7 and expenditures is 4:3. If each saves ₹2000 per month, find monthly incomes.',
        given: 'Incomes = 9x, 7x; Expenditures = 4y, 3y; Each saves ₹2000',
        formula: 'Income - Expenditure = Savings',
        substitution: '9x - 4y = 2000 (1); 7x - 3y = 2000 (2)',
        calculation: 'Multiply (1) by 3: 27x - 12y = 6000 (3). Multiply (2) by 4: 28x - 12y = 8000 (4). Subtract (3) from (4): x = 2000. Incomes: 9(2000) = ₹18,000 and 7(2000) = ₹14,000.',
        finalAnswer: 'Monthly incomes are ₹18,000 and ₹14,000',
        unit: 'Currency (₹)'
      },
      {
        problem: 'Example 10: The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits differ by 2, find the number.',
        given: 'Original = 10x + y, Reversed = 10y + x. (10x+y) + (10y+x) = 66 => 11(x+y) = 66 => x + y = 6.',
        formula: 'Digits differ by 2: Either x - y = 2 OR y - x = 2',
        substitution: 'Case 1: x + y = 6 and x - y = 2; Case 2: x + y = 6 and y - x = 2',
        calculation: 'Case 1: Adding gives 2x = 8 => x = 4, y = 2 => Number is 42. Case 2: Adding gives 2y = 8 => y = 4, x = 2 => Number is 24.',
        finalAnswer: 'Two such numbers: 42 and 24',
        unit: 'Integers'
      }
    ],
    common_misconceptions: [
      'In Example 10, writing only one number (42) and forgetting the second valid number (24) where y - x = 2.',
      'Setting up income and expenditure with only one variable x: income and expenditure have different multipliers!'
    ],
    ai_system_prompt_context: 'Demonstrate Example 10 on the board. Make sure the student understands why there are two answers when digits differ by 2.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="100" y="12" width="340" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">TWO-DIGIT NUMBER DIGIT REVERSAL INVARIANT</text>
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="26" fill="#1E40AF" font-weight="bold" font-size="13">Expanded Notation Structure:</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Original Number = 10x + y  |  Reversed Number = 10y + x</text>
    <text x="20" y="75" fill="#2563EB" font-weight="bold" font-size="13">Sum = (10x + y) + (10y + x) = 11(x + y) = 66  ⇒  x + y = 6</text>
  </g>
  <g transform="translate(30, 165)">
    <rect x="0" y="0" width="230" height="85" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="115" y="25" text-anchor="middle" fill="#166534" font-weight="bold" font-size="12">Case 1: x - y = 2</text>
    <text x="115" y="50" text-anchor="middle" fill="#0F172A" font-size="12">x = 4, y = 2</text>
    <text x="115" y="70" text-anchor="middle" fill="#16A34A" font-weight="bold" font-size="14">Number = 42</text>
  </g>
  <g transform="translate(280, 165)">
    <rect x="0" y="0" width="230" height="85" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="1.2"/>
    <text x="115" y="25" text-anchor="middle" fill="#92400E" font-weight="bold" font-size="12">Case 2: y - x = 2</text>
    <text x="115" y="50" text-anchor="middle" fill="#0F172A" font-size="12">x = 2, y = 4</text>
    <text x="115" y="70" text-anchor="middle" fill="#D97706" font-weight="bold" font-size="14">Number = 24</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Elimination Method',
          questions: [
            {
              q_num: 'Q1',
              type: 'PYQ',
              question: 'If the sum of a two-digit number and its reverse is 66 and digits differ by 2, how many such numbers exist? (A) 1 (B) 2 (C) Infinitely many (D) 0',
              ideal_answer: '(B) 2 numbers: 42 and 24.',
              socratic_hint: 'Remember that the difference of digits can be x - y = 2 or y - x = 2.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 7,
    title: 'Exercise 3.3 Complete Step-by-Step Elimination Solver (Q1 & Q2 All Parts)',
    description: 'Exhaustive step-by-step scratchpad solutions for Exercise 3.3 Question 1 (all 4 parts) and Question 2 (all 5 word problems) by elimination.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Direct Elimination of Variables (Q1(i) to Q1(iv))',
      'Fraction Reconstruction Word Problems (Q2(i))',
      'Age Relationships with Shifting Years: Nuri and Sonu (Q2(ii))',
      'Two-Digit Number with Nine-Times Reversal Relation (Q2(iii))',
      'Bank Cash Denominations: ₹50 and ₹100 Notes (Q2(iv))',
      'Lending Library Fixed and Additional Daily Surcharge (Q2(v))'
    ],
    key_concepts: [
      'Cash Denomination Rule: Total Notes = x + y; Total Value = 50x + 100y.',
      'Library Surcharge Model: 7-day cost = x + 4y (since first 3 days are covered by fixed charge x).'
    ],
    success_criteria: 'Student can solve any word problem from Exercise 3.3 using the elimination method with zero errors.',
    chapter_notes: `### Exercise 3.3 Complete Solutions

#### Question 1: Elimination Solutions
- **(i) $x + y = 5$ and $2x - 3y = 4$**:
  - Multiply Eq 1 by 3: $3x + 3y = 15$. Add to Eq 2: $5x = 19 \\implies x = 19/5$.
  - $y = 5 - 19/5 = 6/5$. Solution: **$(19/5, 6/5)$**.
- **(ii) $3x + 4y = 10$ and $2x - 2y = 2$**:
  - Multiply Eq 2 by 2: $4x - 4y = 4$. Add to Eq 1: $7x = 14 \\implies x = 2$.
  - $2(2) - 2y = 2 \\implies 2y = 2 \\implies y = 1$. Solution: **$(2, 1)$**.
- **(iii) $3x - 5y - 4 = 0$ and $9x = 2y + 7$**:
  - $3x - 5y = 4$ and $9x - 2y = 7$.
  - Multiply Eq 1 by 3: $9x - 15y = 12$. Subtract from Eq 2: $13y = -5 \\implies y = -5/13$.
  - $9x = 2(-5/13) + 7 = 81/13 \\implies x = 9/13$. Solution: **$(9/13, -5/13)$**.
- **(iv) $x/2 + 2y/3 = -1$ and $x - y/3 = 3$**:
  - Multiply Eq 1 by 6: $3x + 4y = -6$. Multiply Eq 2 by 3: $3x - y = 9$.
  - Subtract: $5y = -15 \\implies y = -3$. $3x = 9 + (-3) = 6 \\implies x = 2$. Solution: **$(2, -3)$**.

#### Question 2: Word Problems
- **(i) Fraction**: $\\frac{x+1}{y-1} = 1 \\implies x - y = -2$. $\\frac{x}{y+1} = \\frac{1}{2} \\implies 2x - y = 1$.
  - Subtracting: $x = 3$. $y = 3 + 2 = 5$. **Fraction is $3/5$**.
- **(ii) Nuri and Sonu**: 5 yrs ago $N - 5 = 3(S - 5) \\implies N - 3S = -10$.
  - 10 yrs later: $N + 10 = 2(S + 10) \\implies N - 2S = 10$.
  - Subtracting: $S = 20$ years (Sonu), $N = 50$ years (Nuri).
- **(iii) Two-Digit Number**: Digits sum is 9: $x + y = 9$.
  - 9 times number = 2 times reversed: $9(10x + y) = 2(10y + x) \\implies 90x + 9y = 20y + 2x \\implies 88x - 11y = 0 \\implies y = 8x$.
  - $x + 8x = 9 \\implies 9x = 9 \\implies x = 1, y = 8$. **Number is 18**.
- **(iv) Meena's Bank Withdrawal**: 25 notes of ₹50 ($x$) and ₹100 ($y$) totaling ₹2000.
  - $x + y = 25$ and $50x + 100y = 2000 \\implies x + 2y = 40$.
  - Subtracting: $y = 15$ notes of ₹100, $x = 10$ notes of ₹50.
- **(v) Lending Library**: Fixed charge for 3 days = $x$, daily charge after = $y$.
  - Saritha kept 7 days (3 fixed + 4 extra): $x + 4y = 27$.
  - Susy kept 5 days (3 fixed + 2 extra): $x + 2y = 21$.
  - Subtracting: $2y = 6 \\implies y = \\text{₹ } 3$/day. Fixed charge $x = 21 - 6 = \\text{₹ } 15$.`,
    worked_examples: [
      {
        problem: 'Exercise 3.3 Q2(iii): The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.',
        given: 'Original = 10x + y, Reversed = 10y + x. Conditions: x + y = 9 and 9(10x + y) = 2(10y + x).',
        formula: 'Algebraic expansion',
        substitution: '90x + 9y = 20y + 2x => 88x = 11y => y = 8x',
        calculation: 'Substitute y = 8x into x + y = 9: x + 8x = 9 => 9x = 9 => x = 1. Then y = 8(1) = 8. Original number = 10(1) + 8 = 18.',
        finalAnswer: '18',
        unit: 'Two-digit integer'
      },
      {
        problem: 'Exercise 3.3 Q2(iv): Meena went to a bank to withdraw ₹2000. She asked the cashier to give her ₹50 and ₹100 notes only. Meena got 25 notes in all. Find how many notes of ₹50 and ₹100 she received.',
        given: 'Total notes = 25; Total value = ₹2000. Let ₹50 notes = x, ₹100 notes = y.',
        formula: 'x + y = 25 and 50x + 100y = 2000',
        substitution: 'Divide Eq 2 by 50: x + 2y = 40',
        calculation: '(x + 2y) - (x + y) = 40 - 25 => y = 15 notes. Then x = 25 - 15 = 10 notes.',
        finalAnswer: '10 notes of ₹50 and 15 notes of ₹100',
        unit: 'Currency notes count'
      }
    ],
    common_misconceptions: [
      'In Q2(v), writing x + 7y = 27 instead of x + 4y = 27. The fixed charge covers the FIRST THREE DAYS, so only 4 days are charged at y.',
      'In Q2(iii), assuming the number is xy (product) instead of 10x + y.'
    ],
    ai_system_prompt_context: 'Solve Q2(iii) and Q2(v) on the board with great care. Emphasize why the library equation uses 4y and not 7y.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="90" y="12" width="360" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">Q2(v): LENDING LIBRARY 3-DAY FIXED CHARGE MODEL</text>
  <g transform="translate(30, 55)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="26" fill="#1E40AF" font-weight="bold" font-size="13">Timeline Breakdown (Days 1 to 7):</text>
    <rect x="20" y="40" width="180" height="40" rx="4" fill="#DBEAFE" stroke="#2563EB"/>
    <text x="110" y="65" text-anchor="middle" fill="#1E3A8A" font-weight="bold" font-size="12">Days 1 - 3: Fixed (₹x)</text>
    <rect x="210" y="40" width="250" height="40" rx="4" fill="#FEF3C7" stroke="#D97706"/>
    <text x="335" y="65" text-anchor="middle" fill="#92400E" font-weight="bold" font-size="12">Days 4 - 7 (4 Days): ₹4y</text>
  </g>
  <g transform="translate(30, 165)">
    <rect x="0" y="0" width="480" height="90" rx="8" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.2"/>
    <text x="20" y="28" fill="#166534" font-weight="bold" font-size="13">System Resolution:</text>
    <text x="20" y="52" fill="#0F172A" font-size="12">Saritha (7 days): x + 4y = 27  |  Susy (5 days): x + 2y = 21  ⇒  2y = 6</text>
    <text x="20" y="74" fill="#16A34A" font-weight="bold" font-size="13">Daily Surcharge y = ₹3/day  |  Fixed Charge x = ₹15</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Elimination Word Problems',
          questions: [
            {
              q_num: 'Q1',
              type: 'Competency',
              question: 'In the lending library problem, why is Sarithas equation written as x + 4y = 27 and not x + 7y = 27?',
              ideal_answer: 'Because the fixed fee x already covers the first 3 days of borrowing, leaving only 7 - 3 = 4 additional days charged at ₹y per day.',
              socratic_hint: 'How many days are included in the initial fixed charge?'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 8,
    title: 'Board Exam Mastery: High-Yield Traps, Equations Reducible & Multi-Year PYQs',
    description: 'Master authentic board exam questions for Class 10 CBSE: finding k for unique/infinite/no solution, equations reducible to linear form, and upstream-downstream boats.',
    board: 'CBSE',
    class_level: 'Class 10',
    estimated_minutes: 20,
    subtopics: [
      'Finding Unknown Parameter k for Infinite Solutions (Ratio Consistency)',
      'Equations Reducible to a Pair of Linear Equations (1/x = u, 1/y = v)',
      'Upstream and Downstream Boat Speed Physics Modeling',
      'Geometric Area Constraints in Rectangles',
      '5-Mark Structured Board Presentation Standards'
    ],
    key_concepts: [
      'Parameter k Invariant: When solving for k with infinite solutions, ensure that the chosen k satisfies ALL pairwise equalities simultaneously.',
      'Relative Speed: Speed Upstream = (x - y) km/h; Speed Downstream = (x + y) km/h, where x > y.'
    ],
    success_criteria: 'Student can solve complex 5-mark board exam problems involving speed-distance-stream and unknown parameter k.',
    chapter_notes: `### Board Exam Mastery & PYQs

#### 1. Unknown Parameter $k$ Conditions
For the system $kx + 3y - (k - 3) = 0$ and $12x + ky - k = 0$ to have infinitely many solutions:
$$\\frac{k}{12} = \\frac{3}{k} = \\frac{-(k - 3)}{-k}$$
1. From $\\frac{k}{12} = \\frac{3}{k} \\implies k^2 = 36 \\implies k = \\pm 6$.
2. From $\\frac{3}{k} = \\frac{k - 3}{k} \\implies 3k = k^2 - 3k \\implies k^2 - 6k = 0 \\implies k(k - 6) = 0 \\implies k = 0$ or $k = 6$.
3. The common value satisfying both is **$k = 6$**. ($k = -6$ is strictly rejected).

#### 2. Upstream and Downstream Boat Problems
Let speed of boat in still water be $x$ km/h, and speed of stream be $y$ km/h:
- Speed Downstream $= x + y$ km/h
- Speed Upstream $= x - y$ km/h
- Time $= \\frac{\\text{Distance}}{\\text{Speed}}$
- A boat covers 30 km upstream and 44 km downstream in 10 hours:
  $$\\frac{30}{x - y} + \\frac{44}{x + y} = 10$$
  In 13 hours, it covers 40 km upstream and 55 km downstream:
  $$\\frac{40}{x - y} + \\frac{55}{x + y} = 13$$
- Let $u = \\frac{1}{x - y}$ and $v = \\frac{1}{x + y}$.
  - $30u + 44v = 10$ and $40u + 55v = 13$.
  - Solving gives $u = 1/5$ and $v = 1/11$.
  - $x - y = 5$ and $x + y = 11 \\implies 2x = 16 \\implies x = 8$ km/h, $y = 3$ km/h.`,
    worked_examples: [
      {
        problem: 'Board PYQ: For what value of k will the following pair of linear equations have infinitely many solutions? kx + 3y - (k - 3) = 0 and 12x + ky - k = 0.',
        given: 'a_1 = k, b_1 = 3, c_1 = -(k-3); a_2 = 12, b_2 = k, c_2 = -k',
        formula: 'Infinitely many solutions: a_1/a_2 = b_1/b_2 = c_1/c_2',
        substitution: 'k/12 = 3/k = (k-3)/k',
        calculation: 'k/12 = 3/k => k^2 = 36 => k = ±6. Next test: 3/k = (k-3)/k => 3 = k - 3 => k = 6. For k = -6, 3/(-6) = -1/2, while (-6-3)/(-6) = 9/6 = 3/2 ≠ -1/2. Thus k = -6 is rejected.',
        finalAnswer: 'k = 6',
        unit: 'Scalar parameter'
      },
      {
        problem: 'Board PYQ: A boat goes 30 km upstream and 44 km downstream in 10 hours. In 13 hours, it can go 40 km upstream and 55 km downstream. Determine the speed of the stream and that of the boat in still water.',
        given: 'Case 1: 30 km upstream + 44 km downstream = 10 hrs. Case 2: 40 km upstream + 55 km downstream = 13 hrs.',
        formula: 'Let u = 1/(x - y) and v = 1/(x + y)',
        substitution: '30u + 44v = 10 (1); 40u + 55v = 13 (2)',
        calculation: 'Multiply (1) by 4: 120u + 176v = 40. Multiply (2) by 3: 120u + 165v = 39. Subtract: 11v = 1 => v = 1/11. From (1): 30u + 4 = 10 => 30u = 6 => u = 1/5. Therefore: x - y = 5 and x + y = 11. Adding gives 2x = 16 => x = 8 km/h. Then y = 3 km/h.',
        finalAnswer: 'Speed of boat = 8 km/h, Speed of stream = 3 km/h',
        unit: 'km/h'
      }
    ],
    common_misconceptions: [
      'In parameter k problems, stopping at k^2 = 36 and answering k = ±6 without checking the second ratio equation (k = -6 is invalid!).',
      'In boat problems, writing speed upstream as y - x. Since the boat moves against the stream, x > y, so speed is x - y.'
    ],
    ai_system_prompt_context: 'Demonstrate the boat speed substitution u = 1/(x-y) on the chalkboard. Point out why k = -6 must be rejected.',
    visual_lesson_plan: {
      diagram_type: 'vector_svg_diagram',
      diagram_svg: `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">
  <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="110" y="12" width="320" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="270" y="28" text-anchor="middle" fill="#0F172A" font-size="12" font-weight="bold" font-family="system-ui">BOAT RELATIVE SPEED VECTOR PHYSICS</text>
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.2"/>
    <text x="20" y="26" fill="#1E40AF" font-weight="bold" font-size="13">Downstream (With the Current):</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Boat Vector: x → | Stream Vector: y →</text>
    <text x="20" y="75" fill="#16A34A" font-weight="bold" font-size="14">Net Speed = x + y = 11 km/h  ⇒  44 km in 4 hours</text>
  </g>
  <g transform="translate(30, 160)">
    <rect x="0" y="0" width="480" height="95" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.2"/>
    <text x="20" y="26" fill="#991B1B" font-weight="bold" font-size="13">Upstream (Against the Current):</text>
    <text x="20" y="50" fill="#0F172A" font-size="12">Boat Vector: x → | Stream Resistance: y ←</text>
    <text x="20" y="75" fill="#DC2626" font-weight="bold" font-size="14">Net Speed = x - y = 5 km/h  ⇒  30 km in 6 hours</text>
  </g>
</svg>`,
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Board Exam Mastery',
          questions: [
            {
              q_num: 'Q1',
              type: 'PYQ',
              question: 'Why is k = -6 rejected in the system kx + 3y - (k-3) = 0 and 12x + ky - k = 0 for infinite solutions?',
              ideal_answer: 'Because while k = -6 satisfies k/12 = 3/k, it gives -1/2 for 3/k and +3/2 for (k-3)/k. Since -1/2 ≠ 3/2, it fails the third ratio equality.',
              socratic_hint: 'Plug k = -6 into all three ratios to see if they are equal.'
            }
          ]
        }
      ]
    }
  }
];

async function run() {
  console.log('Seeding Chapter 3: Pair of Linear Equations in Two Variables with 8 exhaustive modules...');

  // 1. Delete old modules
  const { error: delErr } = await supabase.from('syllabus_modules').delete().eq('curriculum_id', CH3_ID);
  if (delErr) {
    console.error('Error deleting old modules for Chapter 3:', delErr);
    process.exit(1);
  }
  console.log('Deleted old modules for Chapter 3.');

  // 2. Insert the 8 exhaustive modules
  for (const mod of modules) {
    const { error: insErr } = await supabase.from('syllabus_modules').insert({
      curriculum_id: CH3_ID,
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
    description: 'Complete NCERT-exhaustive masterclass on Pair of Linear Equations in Two Variables with full step-by-step solutions for all exercises (3.1, 3.2, 3.3), 10 textbook examples, and board PYQs.'
  }).eq('id', CH3_ID);

  console.log('Chapter 3 successfully updated in DB with 8 full modules!');
}

run();
