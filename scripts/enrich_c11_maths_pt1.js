const { supabase } = require('./db_helper');

// Master Topper Question Solutions for Class 11 Mathematics Part 1 (Chapters 1 to 7)
const CHAPTERS_PT1 = [
  {
    order_index: 1,
    title: 'Chapter 1: Sets',
    solvers: [
      {
        module_order: 3, // Exercise 1.1 Solver
        worked_examples: [
          {
            problem: "Exercise 1.1 Q1: Which of the following are sets? Justify: (i) Collection of all months of a year beginning with J. (ii) Collection of ten most talented writers of India. (iii) Team of eleven best-cricket batsmen of the world.",
            given: "Statements describing collections of objects.",
            formula: "A set is a well-defined collection of distinct objects where membership does not vary from person to person.",
            substitution: "Test each collection for objective, well-defined criteria.",
            calculation: "Part (i): Months beginning with 'J' are January, June, July. This is unambiguous and well-defined across all observers. Hence, it is a SET.\nPart (ii): 'Most talented' is subjective and vague; a writer talented to one person may not be to another. Hence, NOT a set.\nPart (iii): 'Best-cricket batsmen' has no mathematical metric (average, strike rate, subjective fame). Criteria varies. Hence, NOT a set.",
            finalAnswer: "(i) Yes, it is a set; (ii) No, not well-defined; (iii) No, subjective criteria.",
            unit: "set classification",
            has_diagram: false
          },
          {
            problem: "Exercise 1.1 Q3: Write the following sets in roster form: (i) A = {x : x is an integer and -3 <= x < 7}, (ii) B = {x : x is a natural number less than 6}, (iii) C = {x : x is a two-digit natural number such that sum of its digits is 8}.",
            given: "Set-builder definitions for sets A, B, and C.",
            formula: "Roster form lists all elements separated by commas within braces { }.",
            substitution: "Enumerate all satisfying integers.",
            calculation: "Part (i): Integers >= -3 and < 7 are -3, -2, -1, 0, 1, 2, 3, 4, 5, 6.\n  => A = {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6}.\nPart (ii): Natural numbers < 6 are 1, 2, 3, 4, 5.\n  => B = {1, 2, 3, 4, 5}.\nPart (iii): Two-digit numbers with digit sum = 8: 17 (1+7), 26, 35, 44, 53, 62, 71, 80.\n  => C = {17, 26, 35, 44, 53, 62, 71, 80}.",
            finalAnswer: "A = {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6}; B = {1, 2, 3, 4, 5}; C = {17, 26, 35, 44, 53, 62, 71, 80}",
            unit: "roster form",
            has_diagram: false
          },
          {
            problem: "Exercise 1.1 Q4: Write the following sets in set-builder form: (i) {3, 6, 9, 12}, (ii) {2, 4, 8, 16, 32}, (iii) {5, 25, 125, 625}.",
            given: "Sets in roster form.",
            formula: "State the characteristic property P(x) possessed by all elements in the set.",
            substitution: "Identify mathematical sequences: (i) Multiples of 3, (ii) Powers of 2, (iii) Powers of 5.",
            calculation: "Part (i): Elements are 3(1), 3(2), 3(3), 3(4). Multiples of 3 where n in N and 1 <= n <= 4.\n  => {x : x = 3n, n in N and 1 <= n <= 4}.\nPart (ii): Elements are 2^1, 2^2, 2^3, 2^4, 2^5.\n  => {x : x = 2^n, n in N and 1 <= n <= 5}.\nPart (iii): Elements are 5^1, 5^2, 5^3, 5^4.\n  => {x : x = 5^n, n in N and 1 <= n <= 4}.",
            finalAnswer: "(i) {x : x = 3n, n in N, 1 <= n <= 4}; (ii) {x : x = 2^n, n in N, 1 <= n <= 5}; (iii) {x : x = 5^n, n in N, 1 <= n <= 4}",
            unit: "set-builder notation",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 4, // Exercise 1.2 Solver
        worked_examples: [
          {
            problem: "Exercise 1.2 Q1 & Q2: (a) Which of the following are empty sets: Set of odd natural numbers divisible by 2? Set of even prime numbers? (b) Are the sets finite or infinite: Set of lines parallel to x-axis? The set of concentric circles?",
            given: "Set definitions.",
            formula: "Empty set contains 0 elements: phi = {}. Finite sets have countable cardinality n(A).",
            substitution: "Check element counts.",
            calculation: "Part (a1): Odd natural numbers leave remainder 1 on division by 2, never 0. Cardinality = 0. Hence, it is an EMPTY SET (phi).\nPart (a2): The number 2 is both even and prime. Set = {2}, cardinality = 1. Not empty (singleton set).\nPart (b1): Infinitely many lines parallel to x-axis exist (y = c for any real number c). Hence, INFINITE SET.\nPart (b2): Infinitely many concentric circles with varying radius r > 0. Hence, INFINITE SET.",
            finalAnswer: "(a1) Empty set; (a2) Singleton set {2}; (b1) Infinite set; (b2) Infinite set",
            unit: "set classification",
            has_diagram: false
          },
          {
            problem: "Exercise 1.2 Q4: State whether A = B: (i) A = {a, b, c, d}, B = {d, c, b, a}; (ii) A = {4, 8, 12, 16}, B = {8, 4, 16, 18}; (iii) A = {2, 4, 6, 8, 10}, B = {x : x is positive even integer and x <= 10}.",
            given: "Pairs of sets A and B.",
            formula: "A = B iff every element of A is in B and every element of B is in A.",
            substitution: "Compare element sets regardless of ordering.",
            calculation: "Part (i): Elements are identical: {a, b, c, d}. Order does not matter in sets. A = B.\nPart (ii): 12 in A but 12 not in B; 18 in B but 18 not in A. A != B.\nPart (iii): Positive even integers <= 10 are {2, 4, 6, 8, 10}. Identical to A. A = B.",
            finalAnswer: "(i) A = B; (ii) A != B; (iii) A = B",
            unit: "set equality",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 6, // Exercise 1.3 & 1.4 Solver
        worked_examples: [
          {
            problem: "Exercise 1.3 Q4 & Q6: (a) Write down all subsets of: (i) {a}, (ii) {a, b}, (iii) {1, 2, 3}, (iv) phi. (b) Write as intervals: (i) {x : x in R, -4 < x <= 6}, (ii) {x : x in R, 0 <= x < 7}, (iii) {x : x in R, 3 <= x <= 4}.",
            given: "Sets for power set computation; set-builder inequalities for intervals.",
            formula: "Number of subsets of a set of n elements is 2^n. Open interval (a, b); closed interval [a, b].",
            substitution: "List power set P(A); apply strict (<) vs non-strict (<=) interval brackets.",
            calculation: "Subsets:\n(i) {a}: phi, {a} (2^1 = 2 subsets).\n(ii) {a, b}: phi, {a}, {b}, {a, b} (2^2 = 4 subsets).\n(iii) {1, 2, 3}: phi, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} (2^3 = 8 subsets).\n(iv) phi: phi (2^0 = 1 subset).\nIntervals:\n(i) -4 < x <= 6 is (-4, 6].\n(ii) 0 <= x < 7 is [0, 7).\n(iii) 3 <= x <= 4 is [3, 4].",
            finalAnswer: "Subsets listed; Intervals: (-4, 6], [0, 7), [3, 4]",
            unit: "subsets and intervals",
            has_diagram: false
          },
          {
            problem: "Exercise 1.4 Q1 & Q4: Let U = {1, 2, 3, 4, 5, 6, 7, 8, 9}, A = {2, 4, 6, 8}, B = {2, 3, 5, 7}, C = {3, 4, 5, 6}. Find: (i) A U B, (ii) A intersect B, (iii) A - B, (iv) B - A.",
            given: "Sets A = {2, 4, 6, 8}, B = {2, 3, 5, 7}.",
            formula: "A U B = {x : x in A or x in B}; A intersect B = {x : x in A and x in B}; A - B = {x : x in A and x not in B}.",
            substitution: "Combine, intersect, and subtract elements.",
            calculation: "Part (i): A U B = {2, 3, 4, 5, 6, 7, 8}.\nPart (ii): Common element = {2}. A intersect B = {2}.\nPart (iii): Elements in A not in B: {4, 6, 8}. A - B = {4, 6, 8}.\nPart (iv): Elements in B not in A: {3, 5, 7}. B - A = {3, 5, 7}.",
            finalAnswer: "(i) A U B = {2, 3, 4, 5, 6, 7, 8}; (ii) A intersect B = {2}; (iii) A - B = {4, 6, 8}; (iv) B - A = {3, 5, 7}",
            unit: "set operations",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 7, // Exercise 1.5 & Miscellaneous
        worked_examples: [
          {
            problem: "Exercise 1.5 Q1 & Q2: Let U = {1, 2, 3, 4, 5, 6, 7, 8, 9}, A = {1, 2, 3, 4}, B = {2, 4, 6, 8}, C = {3, 4, 5, 6}. Find: (i) A', (ii) (A U B)', (iii) Verify De Morgan's Law: (A U B)' = A' intersect B'.",
            given: "Universal set U and subsets A, B.",
            formula: "A' = U - A; De Morgan's Law: (A U B)' = A' intersect B'.",
            substitution: "Compute complements with respect to U.",
            calculation: "Step 1: A' = {5, 6, 7, 8, 9}.\nStep 2: A U B = {1, 2, 3, 4, 6, 8}.\nStep 3: (A U B)' = U - (A U B) = {5, 7, 9}.\nStep 4: B' = U - B = {1, 3, 5, 7, 9}.\nStep 5: A' intersect B' = {5, 6, 7, 8, 9} intersect {1, 3, 5, 7, 9} = {5, 7, 9}.\nStep 6: (A U B)' = A' intersect B' = {5, 7, 9}. Hence Proved!",
            finalAnswer: "(i) A' = {5, 6, 7, 8, 9}; (ii) (A U B)' = {5, 7, 9}; (iii) LHS = RHS = {5, 7, 9} (Verified)",
            unit: "De Morgan's Laws",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 2,
    title: 'Chapter 2: Relations and Functions',
    solvers: [
      {
        module_order: 5, // Exercise 2.1 Solver
        worked_examples: [
          {
            problem: "Exercise 2.1 Q1 & Q2: (a) If (x/3 + 1, y - 2/3) = (5/3, 1/3), find x and y. (b) If set A has 3 elements and set B = {3, 4, 5}, find the number of elements in A x B.",
            given: "Ordered pair equality (x/3 + 1, y - 2/3) = (5/3, 1/3); n(A) = 3, B = {3, 4, 5}.",
            formula: "Ordered pairs (a, b) = (c, d) iff a = c and b = d. Cardinality n(A x B) = n(A) x n(B).",
            substitution: "x/3 + 1 = 5/3 and y - 2/3 = 1/3.",
            calculation: "Step 1: x/3 = 5/3 - 1 = 2/3 => x = 2.\nStep 2: y = 1/3 + 2/3 = 3/3 = 1 => y = 1.\nStep 3: Set B = {3, 4, 5} has n(B) = 3 elements.\nStep 4: n(A x B) = n(A) x n(B) = 3 x 3 = 9 elements.",
            finalAnswer: "x = 2, y = 1; Number of elements in A x B = 9",
            unit: "Cartesian product",
            has_diagram: false
          },
          {
            problem: "Exercise 2.1 Q4 & Q5: If A = {-1, 1}, find A x A x A.",
            given: "A = {-1, 1}.",
            formula: "A x A x A = {(a, b, c) : a, b, c in A}, total 2^3 = 8 ordered triplets.",
            substitution: "First compute A x A = {(-1, -1), (-1, 1), (1, -1), (1, 1)}.",
            calculation: "Pair each element of A x A with each element of A {-1, 1}:\nA x A x A = {\n  (-1, -1, -1), (-1, -1, 1),\n  (-1, 1, -1), (-1, 1, 1),\n  (1, -1, -1), (1, -1, 1),\n  (1, 1, -1), (1, 1, 1)\n}.",
            finalAnswer: "A x A x A contains 8 triplets: {(-1,-1,-1), (-1,-1,1), (-1,1,-1), (-1,1,1), (1,-1,-1), (1,-1,1), (1,1,-1), (1,1,1)}",
            unit: "ordered triplets",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 6, // Exercise 2.2 Solver
        worked_examples: [
          {
            problem: "Exercise 2.2 Q1: Let A = {1, 2, 3, ..., 14}. Define a relation R from A to A by R = {(x, y) : 3x - y = 0, where x, y in A}. Write down its domain, codomain, and range.",
            given: "A = {1, 2, ..., 14}, relation rule: y = 3x with x, y in A.",
            formula: "Domain is the set of first elements of R; Range is the set of second elements of R; Codomain is the entire set A.",
            substitution: "Compute pairs: for x = 1, y = 3; x = 2, y = 6; x = 3, y = 9; x = 4, y = 12. For x >= 5, y >= 15 not in A.",
            calculation: "Step 1: R = {(1, 3), (2, 6), (3, 9), (4, 12)}.\nStep 2: Domain = set of first components = {1, 2, 3, 4}.\nStep 3: Range = set of second components = {3, 6, 9, 12}.\nStep 4: Codomain = Target set A = {1, 2, 3, ..., 14}.",
            finalAnswer: "R = {(1,3), (2,6), (3,9), (4,12)}; Domain = {1, 2, 3, 4}; Range = {3, 6, 9, 12}; Codomain = {1, 2, ..., 14}",
            unit: "relation domain and range",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 7, // Exercise 2.3 & Misc Solver
        worked_examples: [
          {
            problem: "Exercise 2.3 Q2: Find the domain and range of the following real functions: (i) f(x) = -|x|, (ii) f(x) = sqrt(9 - x^2).",
            given: "Functions f(x) = -|x| and f(x) = sqrt(9 - x^2).",
            formula: "Domain: set of real x for which f(x) is real and finite. For sqrt(g(x)), condition is g(x) >= 0.",
            substitution: "Part (i): |x| defined for all x in R. Part (ii): 9 - x^2 >= 0.",
            calculation: "Part (i):\n- Domain: Since |x| is defined for every real number, Domain = R.\n- Range: |x| >= 0 for all x => -|x| <= 0. Range = (-infinity, 0].\nPart (ii):\n- Domain: 9 - x^2 >= 0 => x^2 <= 9 => -3 <= x <= 3. Domain = [-3, 3].\n- Range: Since -3 <= x <= 3, 0 <= x^2 <= 9. Therefore, 0 <= 9 - x^2 <= 9.\n  Taking positive square root: 0 <= sqrt(9 - x^2) <= 3. Range = [0, 3].",
            finalAnswer: "(i) Domain = R, Range = (-infinity, 0]; (ii) Domain = [-3, 3], Range = [0, 3]",
            unit: "domain and range",
            has_diagram: true
          }
        ]
      }
    ]
  },
  {
    order_index: 3,
    title: 'Chapter 3: Trigonometric Functions',
    solvers: [
      {
        module_order: 4, // Exercise 3.3 Solver
        worked_examples: [
          {
            problem: "Exercise 3.3 Q1 & Q5: (a) Prove that sin^2(pi/6) + cos^2(pi/3) - tan^2(pi/4) = -1/2. (b) Find the exact values of: (i) sin 75°, (ii) tan 15°.",
            given: "Expressions to evaluate using standard angles and compound angle identities.",
            formula: "sin(A + B) = sin A cos B + cos A sin B; tan(A - B) = (tan A - tan B) / (1 + tan A tan B).",
            substitution: "Part (a): sin(pi/6) = 1/2, cos(pi/3) = 1/2, tan(pi/4) = 1.\nPart (b1): 75° = 45° + 30°.\nPart (b2): 15° = 45° - 30°.",
            calculation: "Part (a):\nLHS = (1/2)^2 + (1/2)^2 - 1^2 = 1/4 + 1/4 - 1 = 2/4 - 1 = 1/2 - 1 = -1/2 = RHS. Hence Proved!\nPart (b1):\nsin(75°) = sin(45° + 30°) = sin 45° cos 30° + cos 45° sin 30°\n  = (1/sqrt(2))(sqrt(3)/2) + (1/sqrt(2))(1/2) = (sqrt(3) + 1) / (2 sqrt(2)).\nPart (b2):\ntan(15°) = tan(45° - 30°) = (tan 45° - tan 30°) / (1 + tan 45° tan 30°)\n  = (1 - 1/sqrt(3)) / (1 + 1/sqrt(3)) = (sqrt(3) - 1) / (sqrt(3) + 1).\nRationalizing: (sqrt(3) - 1)^2 / (3 - 1) = (3 + 1 - 2 sqrt(3)) / 2 = 2 - sqrt(3).",
            finalAnswer: "(a) Proved -1/2; (b1) sin 75° = (sqrt(3)+1)/(2 sqrt(2)); (b2) tan 15° = 2 - sqrt(3)",
            unit: "compound angle trigonometric values",
            has_diagram: false
          },
          {
            problem: "Exercise 3.3 Q8 & Q10: Prove that: (i) cos(pi + x) cos(-x) / [sin(pi - x) cos(pi/2 + x)] = cot^2 x. (ii) sin(n + 1)x sin(n + 2)x + cos(n + 1)x cos(n + 2)x = cos x.",
            given: "Trigonometric quotient and sum of products.",
            formula: "ASTC Quadrant rules: cos(pi + x) = -cos x, cos(-x) = cos x, sin(pi - x) = sin x, cos(pi/2 + x) = -sin x. Identity: cos A cos B + sin A sin B = cos(A - B).",
            substitution: "Substitute quadrant values into LHS.",
            calculation: "Part (i):\nNumerator = (-cos x)(cos x) = -cos^2 x.\nDenominator = (sin x)(-sin x) = -sin^2 x.\nLHS = (-cos^2 x) / (-sin^2 x) = cos^2 x / sin^2 x = cot^2 x = RHS. Hence Proved!\n\nPart (ii):\nLet A = (n + 2)x and B = (n + 1)x.\nLHS = cos A cos B + sin A sin B = cos(A - B)\n  = cos[(n + 2)x - (n + 1)x] = cos[nx + 2x - nx - x] = cos x = RHS. Hence Proved!",
            finalAnswer: "Both identities proved to equal cot^2 x and cos x respectively.",
            unit: "trigonometric identities",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 4,
    title: 'Chapter 4: Complex Numbers and Quadratic Equations',
    solvers: [
      {
        module_order: 4, // Exercise 4.1 Solver
        worked_examples: [
          {
            problem: "Exercise 4.1 Q1, Q3 & Q8: Express in the form a + ib: (i) (5i)(-3/5 i), (ii) i^(-39), (iii) (1 - i)^4.",
            given: "Complex expressions to evaluate in standard form a + ib.",
            formula: "i^2 = -1, i^3 = -i, i^4 = 1. (1 - i)^4 = [ (1 - i)^2 ]^2.",
            substitution: "Apply algebraic simplification and powers of i.",
            calculation: "Part (i):\n(5i)(-3/5 i) = 5 * (-3/5) * i^2 = -3 * (-1) = 3 = 3 + 0i.\nPart (ii):\ni^(-39) = 1 / i^39. Since 39 = 4(9) + 3, i^39 = (i^4)^9 * i^3 = 1 * (-i) = -i.\n1 / (-i) = i / (-i^2) = i / (-(-1)) = i = 0 + 1i.\nPart (iii):\n(1 - i)^2 = 1 - 2i + i^2 = 1 - 2i - 1 = -2i.\n(1 - i)^4 = (-2i)^2 = 4 i^2 = 4(-1) = -4 = -4 + 0i.",
            finalAnswer: "(i) 3 + 0i; (ii) 0 + 1i; (iii) -4 + 0i",
            unit: "standard form a + ib",
            has_diagram: false
          },
          {
            problem: "Exercise 4.1 Q11 & Q14: (a) Find the multiplicative inverse of 4 - 3i. (b) Express [(3 + i sqrt(5))(3 - i sqrt(5))] / [(sqrt(3) + sqrt(2)i) - (sqrt(3) - i sqrt(2))] in the form a + ib.",
            given: "Complex numbers z1 = 4 - 3i and quotient expression.",
            formula: "Multiplicative inverse z^(-1) = z_bar / |z|^2 = (a - ib)/(a^2 + b^2). (a + b)(a - b) = a^2 - b^2.",
            substitution: "For 4 - 3i, a = 4, b = -3, a^2 + b^2 = 16 + 9 = 25.",
            calculation: "Part (a):\nz_bar = 4 + 3i; |z|^2 = 4^2 + (-3)^2 = 25.\nz^(-1) = (4 + 3i)/25 = 4/25 + 3/25 i.\n\nPart (b):\nNumerator: 3^2 - (i sqrt(5))^2 = 9 - i^2(5) = 9 - (-5) = 14.\nDenominator: sqrt(3) + i sqrt(2) - sqrt(3) + i sqrt(2) = 2i sqrt(2).\nExpression = 14 / (2i sqrt(2)) = 7 / (i sqrt(2)).\nMultiply numerator & denominator by i: 7i / (i^2 sqrt(2)) = 7i / (-sqrt(2)) = -7/(sqrt(2)) i = 0 - (7 sqrt(2) / 2) i.",
            finalAnswer: "(a) 4/25 + 3/25 i; (b) 0 - (7 sqrt(2) / 2) i",
            unit: "complex division and inverse",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 5,
    title: 'Chapter 5: Linear Inequalities',
    solvers: [
      {
        module_order: 4, // Exercise 5.1 Solver
        worked_examples: [
          {
            problem: "Exercise 5.1 Q1 & Q4: Solve 24x < 100 when: (i) x is a natural number, (ii) x is an integer. Also solve 3x + 8 > 2 when: (iii) x is an integer, (iv) x is a real number.",
            given: "Inequalities 24x < 100 and 3x + 8 > 2.",
            formula: "Division by positive number preserves inequality sign. Solutions depend on the replacement set (N, Z, R).",
            substitution: "x < 100/24 = 25/6 = 4.167; 3x > -6 => x > -2.",
            calculation: "For 24x < 100 => x < 4.167:\n(i) If x in N: {1, 2, 3, 4}.\n(ii) If x in Z: {..., -3, -2, -1, 0, 1, 2, 3, 4}.\n\nFor 3x + 8 > 2 => 3x > -6 => x > -2:\n(iii) If x in Z: {-1, 0, 1, 2, 3, ...}.\n(iv) If x in R: Interval (-2, infinity).",
            finalAnswer: "(i) {1, 2, 3, 4}; (ii) {..., 0, 1, 2, 3, 4}; (iii) {-1, 0, 1, 2, ...}; (iv) (-2, infinity)",
            unit: "linear inequality solution set",
            has_diagram: false
          },
          {
            problem: "Exercise 5.1 Q21: Ravi obtained 70 and 75 marks in first two unit tests. Find the minimum marks he should get in the third test to have an average of at least 60 marks.",
            given: "Marks in Test 1 = 70; Marks in Test 2 = 75; Target average >= 60.",
            formula: "Average = (x1 + x2 + x3)/3 >= Target.",
            substitution: "Let x be marks in third test: (70 + 75 + x)/3 >= 60.",
            calculation: "Step 1: (145 + x) / 3 >= 60.\nStep 2: Multiply by 3: 145 + x >= 180.\nStep 3: Subtract 145: x >= 180 - 145 = 35.\nStep 4: Minimum marks required = 35.",
            finalAnswer: "Ravi must score a minimum of 35 marks in the third test.",
            unit: "marks",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 6,
    title: 'Chapter 6: Permutations and Combinations',
    solvers: [
      {
        module_order: 3, // Exercise 6.1 & 6.2 Solver
        worked_examples: [
          {
            problem: "Exercise 6.1 Q1 & Q4: (a) How many 3-digit numbers can be formed from the digits 1, 2, 3, 4, 5 assuming that: (i) repetition of digits is allowed? (ii) repetition is not allowed? (b) How many 5-digit telephone numbers can be constructed using digits 0 to 9 if each number starts with 67 and no digit appears more than once?",
            given: "Digits available and constraints.",
            formula: "Fundamental Principle of Counting (Multiplication Principle).",
            substitution: "Evaluate number of choices for each positional slot.",
            calculation: "Part (a1) Repetition allowed: Hundreds place = 5, Tens place = 5, Units place = 5.\n  Total = 5 x 5 x 5 = 125 numbers.\nPart (a2) Repetition NOT allowed: Hundreds = 5, Tens = 4, Units = 3.\n  Total = 5 x 4 x 3 = 60 numbers.\n\nPart (b) 5-digit number starts with 67:\n  Slot 1 = 6 (1 choice), Slot 2 = 7 (1 choice).\n  Digits 6 and 7 are used. Remaining digits = 10 - 2 = 8 digits.\n  Slot 3 = 8 choices, Slot 4 = 7 choices, Slot 5 = 6 choices.\n  Total = 1 x 1 x 8 x 7 x 6 = 336 telephone numbers.",
            finalAnswer: "(a1) 125 numbers; (a2) 60 numbers; (b) 336 telephone numbers",
            unit: "permutations count",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 4, // Exercise 6.3 & 6.4 Solver
        worked_examples: [
          {
            problem: "Exercise 6.3 Q9 & Exercise 6.4 Q3: (a) Find the number of permutations of the letters of the word 'MONDAY' if: (i) 4 letters are used at a time, (ii) all letters are used at a time, (iii) all letters are used but first letter is a vowel. (b) How many chords can be drawn through 21 points on a circle?",
            given: "Word 'MONDAY' (6 distinct letters: M, O, N, D, A, Y; Vowels: O, A); 21 points on circle.",
            formula: "P(n, r) = n! / (n - r)!; A chord requires choosing 2 points: C(n, 2) = n(n - 1) / 2.",
            substitution: "Calculate factorials and combinations.",
            calculation: "Part (a1) 4 letters: P(6, 4) = 6 x 5 x 4 x 3 = 360 words.\nPart (a2) All 6 letters: P(6, 6) = 6! = 720 words.\nPart (a3) First letter vowel: Vowels are O, A (2 choices). Remaining 5 positions filled by 5 letters in 5! ways.\n  Total = 2 x 5! = 2 x 120 = 240 words.\n\nPart (b) Chords through 21 points:\n  C(21, 2) = (21 x 20) / 2 = 21 x 10 = 210 chords.",
            finalAnswer: "(a1) 360 words; (a2) 720 words; (a3) 240 words; (b) 210 chords",
            unit: "permutations and combinations",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 7,
    title: 'Chapter 7: Binomial Theorem',
    solvers: [
      {
        module_order: 3, // Exercise 7.1 Q1-Q5 Solver
        worked_examples: [
          {
            problem: "Exercise 7.1 Q1 & Q4: Expand using Binomial Theorem: (i) (1 - 2x)^5, (ii) (x/3 + 1/x)^5.",
            given: "Binomial expressions with n = 5.",
            formula: "(a + b)^n = sum_{k=0}^n C(n, k) a^(n-k) b^k. Binomial coefficients for n = 5: 1, 5, 10, 10, 5, 1.",
            substitution: "Part (i): a = 1, b = -2x. Part (ii): a = x/3, b = 1/x.",
            calculation: "Part (i):\n(1 - 2x)^5 = C(5,0)(1)^5 + C(5,1)(1)^4(-2x) + C(5,2)(1)^3(-2x)^2 + C(5,3)(1)^2(-2x)^3 + C(5,4)(1)(-2x)^4 + C(5,5)(-2x)^5\n  = 1(1) + 5(-2x) + 10(4x^2) + 10(-8x^3) + 5(16x^4) + 1(-32x^5)\n  = 1 - 10x + 40x^2 - 80x^3 + 80x^4 - 32x^5.\n\nPart (ii):\n(x/3 + 1/x)^5 = C(5,0)(x/3)^5 + C(5,1)(x/3)^4(1/x) + C(5,2)(x/3)^3(1/x)^2 + C(5,3)(x/3)^2(1/x)^3 + C(5,4)(x/3)(1/x)^4 + C(5,5)(1/x)^5\n  = x^5 / 243 + 5(x^4/81)(1/x) + 10(x^3/27)(1/x^2) + 10(x^2/9)(1/x^3) + 5(x/3)(1/x^4) + 1/x^5\n  = x^5/243 + (5/81)x^3 + (10/27)x + 10/(9x) + 5/(3x^3) + 1/x^5.",
            finalAnswer: "(i) 1 - 10x + 40x^2 - 80x^3 + 80x^4 - 32x^5; (ii) x^5/243 + (5/81)x^3 + (10/27)x + 10/(9x) + 5/(3x^3) + 1/x^5",
            unit: "binomial expansion",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 5, // Exercise 7.1 Q6-Q14 Solver
        worked_examples: [
          {
            problem: "Exercise 7.1 Q7, Q10 & Q11: (a) Evaluate (102)^5 using Binomial Theorem. (b) Find which number is larger: (1.01)^1000000 or 10,000. (c) Find (a + b)^4 - (a - b)^4.",
            given: "Numerical and algebraic expressions to evaluate via Binomial Theorem.",
            formula: "(a + b)^n = sum_{k=0}^n C(n, k) a^(n-k) b^k.",
            substitution: "102 = 100 + 2; 1.01 = 1 + 0.01.",
            calculation: "Part (a):\n(100 + 2)^5 = C(5,0)(100)^5 + C(5,1)(100)^4(2) + C(5,2)(100)^3(4) + C(5,3)(100)^2(8) + C(5,4)(100)(16) + C(5,5)(32)\n  = 10,000,000,000 + 5(100,000,000)(2) + 10(1,000,000)(4) + 10(10,000)(8) + 5(100)(16) + 32\n  = 10,000,000,000 + 1,000,000,000 + 40,000,000 + 800,000 + 8,000 + 32\n  = 11,040,808,032.\n\nPart (b):\n(1 + 0.01)^1000000 = 1 + C(1000000, 1)(0.01) + other positive terms\n  = 1 + 1,000,000 * (1/100) + other positive terms\n  = 1 + 10,000 + other positive terms = 10,001 + other positive terms > 10,000.\nHence, (1.01)^1000000 is larger!\n\nPart (c):\n(a + b)^4 - (a - b)^4 = 2 [ C(4, 1) a^3 b + C(4, 3) a b^3 ] = 2 [ 4 a^3 b + 4 a b^3 ] = 8ab(a^2 + b^2).",
            finalAnswer: "(a) 11,040,808,032; (b) (1.01)^1000000 is larger; (c) 8ab(a^2 + b^2)",
            unit: "binomial application",
            has_diagram: false
          }
        ]
      }
    ]
  }
];

async function enrichClass11MathsPart1() {
  console.log("Starting Class 11 Mathematics Part 1 (Ch 1 to 7) Enrichment...");

  for (const chData of CHAPTERS_PT1) {
    const { data: curriculums, error: curErr } = await supabase
      .from('curriculums')
      .select('id, title, order_index')
      .ilike('class_level', '%11%')
      .ilike('category', '%math%')
      .eq('order_index', chData.order_index);

    if (curErr || !curriculums || curriculums.length === 0) {
      console.error(`Curriculum for Ch ${chData.order_index} not found:`, curErr);
      continue;
    }

    const curId = curriculums[0].id;
    console.log(`\nEnriching ${curriculums[0].title} (ID: ${curId})...`);

    for (const solver of chData.solvers) {
      const { data: moduleData, error: modErr } = await supabase
        .from('syllabus_modules')
        .select('id, title, order_index, worked_examples')
        .eq('curriculum_id', curId)
        .eq('order_index', solver.module_order);

      if (modErr || !moduleData || moduleData.length === 0) {
        console.warn(`Module order ${solver.module_order} not found in Ch ${chData.order_index}`);
        continue;
      }

      const mod = moduleData[0];
      const existingExamples = Array.isArray(mod.worked_examples) ? mod.worked_examples : [];
      // Merge: keep solver examples first, then any existing unique ones
      const combined = [...solver.worked_examples];
      for (const ex of existingExamples) {
        if (!combined.some(c => c.problem === ex.problem)) {
          combined.push(ex);
        }
      }

      const { error: updateErr } = await supabase
        .from('syllabus_modules')
        .update({ worked_examples: combined })
        .eq('id', mod.id);

      if (updateErr) {
        console.error(`Failed to update module ${mod.title}:`, updateErr);
      } else {
        console.log(`  ✓ Updated Mod ${mod.order_index}: "${mod.title}" with ${combined.length} comprehensive worked examples!`);
      }
    }
  }

  console.log("\nClass 11 Mathematics Part 1 Enrichment Completed!");
}

enrichClass11MathsPart1();
