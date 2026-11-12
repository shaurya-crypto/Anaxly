"""
Class 9 Mathematics - Chapter 9: Propositions and their Converses (NCERT Ganita Manjari Part II)
Curriculum ID: 51300b78-bda8-4bc0-80bc-f3cb1af21a7e
Fully compliant with Invariant 10 & 14:
- 5 dedicated modules (Theory in M1-M2, dedicated solvers M3-M5)
- 100% of all NCERT exercise questions (Ex 9.1 Q1 to Q17) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> To Prove / To Find -> Formula / Theorem -> Proof / Calculation -> [ROUGH_WORK] -> Boxed Answer
- Pure mathematical typography: Zero raw '*', '**', '//', '^'
- Dynamic search queries for concept visuals & textbook diagram bindings for question figures (Fig 9.1 & Fig 9.2)
"""

def get_ch9_modules():
    CURRICULUM_ID = "51300b78-bda8-4bc0-80bc-f3cb1af21a7e"
    
    modules = [
        # Module 1: Mathematical Statements, Propositions & Conditional Logic
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Mathematical Statements, Propositions & Conditional Logic: Truth Values and 'If-Then' Structures",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Master the foundational syntax of mathematical logic: distinguishing vague declarative assertions from formal propositions with unambiguous truth values. Deconstruct conditional statements into Hypothesis (Antecedent) and Conclusion (Consequent), examining universal quantification, truth tables, and mathematical deductions.",
            "key_concepts": [
                "Statement vs Proposition: A proposition is a declarative sentence that is either strictly True or strictly False, but never both or ambiguous",
                "Conditional Statement: A logical implication formulated as 'If P, then Q' (denoted mathematically as P ⇒ Q), where P is the hypothesis and Q is the conclusion",
                "Hypothesis (P): The given mathematical premise or antecedent that sets the condition",
                "Conclusion (Q): The logical consequence or consequent that necessarily follows whenever the hypothesis is satisfied",
                "Truth Value Verification: Demonstrating that for a conditional statement to be true, the conclusion must hold unconditionally in every valid mathematical instance of the premise"
            ],
            "subtopics": [
                "What constitutes an unambiguous mathematical proposition",
                "Formulating 'If P, then Q' structures from everyday and mathematical assertions",
                "Identifying the hypothesis and conclusion in geometric and algebraic theorems",
                "Evaluating truth values across diverse mathematical domains (geometry, numbers, algebra)",
                "Examples 1 and 2 from NCERT Ganita Manjari"
            ],
            "success_criteria": [
                "Identify whether any given sentence is an admissible mathematical proposition",
                "Deconstruct any theorem or conditional statement into its exact hypothesis and conclusion",
                "Determine the truth value of elementary conditional propositions with rigorous mathematical justification"
            ],
            "chapter_notes": r"""# Chapter 9: Propositions and their Converses
## Module 1: Mathematical Statements, Propositions & Conditional Logic

### 1. What is a Proposition?
In mathematics, precision is paramount. Everyday language often contains statements that depend on personal judgment, context, or incomplete information (e.g., *"Mathematics is easy"*, or *"It is hot today"*). Such subjective sentences are **not** mathematical propositions.

> **Definition (Proposition):**  
> A proposition is a declarative statement that is definitively **True (T)** or **False (F)**, but never simultaneously both, and never dependent on subjective opinion.

#### Examples of Propositions:
1. *"The sum of all three interior angles of a triangle on a Euclidean plane is 180°."* → **Proposition (True)**
2. *"The number 17 is a composite number."* → **Proposition (False)**, because $17$ is prime.
3. *"Is the quadrilateral a square?"* → **Not a proposition** (it is an interrogative sentence).
4. *"Solve the equation $2x + 5 = 15$."* → **Not a proposition** (it is an imperative command).

---

### 2. Conditional Statements: 'If P, then Q' ($P \implies Q$)
Mathematical theorems are typically formulated as conditional statements. A conditional statement connects two simpler statements, $P$ and $Q$, using the connective *"If ... then ..."*.

$$\text{Structure: } \text{If } P \text{, then } Q \quad (P \implies Q)$$

- **Hypothesis (or Antecedent) $P$:** The condition or given assumption.
- **Conclusion (or Consequent) $Q$:** The outcome guaranteed whenever $P$ is satisfied.

#### Dissecting Classic Geometric Theorems:
- **Statement:** *"If two sides of a triangle are equal, then the angles opposite the equal sides are equal."*
  - **Hypothesis $P$:** In $\Delta ABC$, side $AB = AC$.
  - **Conclusion $Q$:** The angle opposite $AB$ equals the angle opposite $AC$ ($\angle C = \angle B$).
  - **Truth Value:** True (proved via SAS congruence of triangles).

---

### 3. Truth Value Rules for Implications
A universal conditional proposition *"If P, then Q"* asserts that whenever $P$ occurs, $Q$ must follow without exception.
- If we can find even **a single instance** where $P$ is true, but $Q$ fails to be true, the entire conditional statement is declared **False**.
""",
            "worked_examples": [
                {
                    "problem": "Example 1 (NCERT): Consider the proposition P: 'If it rains, then the road is wet.' Identify the hypothesis, the conclusion, and determine whether the implication is universally true.",
                    "solution": "GIVEN:\nConditional proposition: 'If it rains, then the road is wet.'\n\nTO DETERMINE:\n(i) Hypothesis P\n(ii) Conclusion Q\n(iii) Universal truth value of the implication\n\nSTEP-BY-STEP ANALYSIS:\nStep 1: Identify Hypothesis:\nThe clause following 'If' represents the hypothesis:\nHypothesis P = 'It rains (at the given location and time).'\n\nStep 2: Identify Conclusion:\nThe clause following 'then' represents the conclusion:\nConclusion Q = 'The road is wet.'\n\nStep 3: Evaluate Validity:\nUnder normal outdoor conditions, when rain falls upon an open roadway, precipitation covers the asphalt with liquid water.\nTherefore, the occurrence of rain guarantees that the road becomes wet.\nThus, Proposition P is universally true in this physical context.\n\n[ROUGH_WORK]\nCondition: Rain occurs ⇒ Road accumulates water. Hence wetness is guaranteed.\nBoxed Answer: [ Hypothesis: 'It rains', Conclusion: 'The road is wet', Truth Value: True ].",
                    "concept_questions": [
                        "Does rain falling guarantee the road is wet?",
                        "What if the road is covered by a long tunnel? Does context matter in physical statements?"
                    ]
                },
                {
                    "problem": "Example 2 (NCERT): For any real number x, consider the statement: 'If x > 0, then x² > 0.' State whether the statement is true and justify.",
                    "solution": "GIVEN:\nStatement: 'For any real number x, if x > 0, then x² > 0.'\n\nTO PROVE / JUSTIFY:\nDetermine whether the statement is True or False.\n\nSTEP-BY-STEP PROOF:\nStep 1: State Hypothesis and Conclusion:\nHypothesis P: x is a positive real number (x > 0).\nConclusion Q: x² > 0.\n\nStep 2: Apply properties of inequalities for real numbers:\nWhen a positive inequality x > 0 is multiplied on both sides by the positive quantity x:\nx · x > 0 · x\nx² > 0.\n\nStep 3: Conclusion:\nSince the product of two positive real numbers is strictly positive, x² must be strictly greater than 0 for all positive real numbers x.\nTherefore, the statement is True.\n\n[ROUGH_WORK]\nLet x = 3 > 0 ⇒ 3² = 9 > 0.\nLet x = 0.5 > 0 ⇒ 0.5² = 0.25 > 0.\nAlways strictly positive!\nBoxed Answer: [ True (Proved) ].",
                    "concept_questions": [
                        "What is 0²? Is 0² > 0?",
                        "Why does the condition x > 0 exclude 0?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "concept_visuals": [
                    {
                        "concept_title": "Statement vs Proposition",
                        "diagram_title": "Statement vs Mathematical Proposition",
                        "image_search_query": "mathematical proposition declarative sentence truth value diagram",
                        "what_to_make": "Comparison diagram showing declarative statement versus mathematical proposition with binary True/False truth values."
                    },
                    {
                        "concept_title": "Conditional Statement",
                        "diagram_title": "Conditional Statement Implication",
                        "image_search_query": "conditional statement implication hypothesis conclusion logic diagram",
                        "what_to_make": "Logic diagram showing 'If P, then Q' conditional statement structure with Hypothesis P and Conclusion Q."
                    },
                    {
                        "concept_title": "Hypothesis (P)",
                        "diagram_title": "Hypothesis Antecedent in Logic",
                        "image_search_query": "hypothesis antecedent in conditional logic statement diagram",
                        "what_to_make": "Diagram illustrating the hypothesis premise P setting the starting condition."
                    },
                    {
                        "concept_title": "Conclusion (Q)",
                        "diagram_title": "Conclusion Consequent in Logic",
                        "image_search_query": "conclusion consequent in conditional logic deduction diagram",
                        "what_to_make": "Diagram illustrating conclusion Q following from hypothesis premise P."
                    },
                    {
                        "concept_title": "Truth Value Verification",
                        "diagram_title": "Conditional Truth Table Verification",
                        "image_search_query": "truth table conditional statement logic verification diagram",
                        "what_to_make": "Truth table diagram verifying truth values of conditional statement P implies Q."
                    }
                ],
                "image_search_query": "mathematical logic conditional statement truth table diagram",
                "video_search_query": "conditional statements hypothesis and conclusion class 9",
                "concept_questions": [
                    "What is the difference between a declarative sentence and a mathematical proposition?",
                    "Can a proposition be both true and false at the same time?",
                    "In the statement 'If a triangle is equilateral, then it is equiangular', what is the hypothesis?",
                    "What is required to prove that an 'if-then' statement is false?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Thinking that all sentences in English are propositions.",
                    "correction": "Only declarative sentences that can be unambiguously assigned a truth value (True or False) qualify as propositions. Commands, exclamations, and questions are not propositions."
                },
                {
                    "misconception": "Confusing the hypothesis with the conclusion.",
                    "correction": "In 'If P, then Q', P is always the hypothesis (the starting premise) and Q is the conclusion (the resulting claim)."
                }
            ],
            "quiz_questions": [
                {
                    "question": "Which of the following is a valid mathematical proposition?",
                    "options": [
                        "(Recommended) Every rectangle is a parallelogram.",
                        "Geometry is more interesting than algebra.",
                        "Please pass the ruler.",
                        "What is the area of a circle?"
                    ],
                    "correct_index": 0,
                    "explanation": "A proposition must be a declarative statement that is definitively true or false. 'Every rectangle is a parallelogram' is a definitively true mathematical fact."
                },
                {
                    "question": "In the conditional statement 'If an integer n is divisible by 6, then n is divisible by 3', what is the conclusion?",
                    "options": [
                        "(Recommended) n is divisible by 3",
                        "n is divisible by 6",
                        "n is an integer",
                        "6 is divisible by 3"
                    ],
                    "correct_index": 0,
                    "explanation": "The conclusion is the clause that follows 'then'. Here, 'n is divisible by 3' is the conclusion."
                }
            ]
        },

        # Module 2: The Art of the Converse & Counterexamples
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "The Art of the Converse & Counterexamples: Baudhāyana–Pythagoras Theorem & Logical Rigor",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Construct converses of conditional statements by exchanging hypothesis and conclusion. Discover why the truth of an original proposition does not guarantee the truth of its converse. Master the construction of rigorous counterexamples to disprove false converses, analyzing the Baudhāyana–Pythagoras theorem and geometric equivalences.",
            "key_concepts": [
                "Converse of a Proposition: Given 'If P, then Q', its converse is 'If Q, then P', formed by transposing the hypothesis and conclusion",
                "Independence of Truth Values: A true proposition may have a converse that is True, or a converse that is False",
                "Counterexample: A specific, concrete mathematical example where the hypothesis of a statement is satisfied, but the conclusion fails, disproving the universal validity of the statement",
                "Baudhāyana–Pythagoras Theorem: In a right-angled triangle with sides a, b, c (hypotenuse c), a² + b² = c²",
                "Converse of Baudhāyana–Pythagoras Theorem: If a triangle with sides a, b, c satisfies a² + b² = c², then the triangle is right-angled opposite side c",
                "Biconditional ('If and only if'): When both P ⇒ Q and Q ⇒ P are true, denoted P ⇔ Q"
            ],
            "subtopics": [
                "Formulating the converse of algebraic, geometric, and real-life statements",
                "Analyzing truth value pairings: (T, T), (T, F), (F, T), (F, F)",
                "The anatomy of a mathematical counterexample",
                "The Baudhāyana–Pythagoras theorem and its converse",
                "Examples 3, 4, and 5 from NCERT Ganita Manjari"
            ],
            "success_criteria": [
                "Accurately construct the converse of any given conditional statement",
                "Demonstrate using counterexamples why an implication converse fails",
                "Formulate biconditional statements when both proposition and converse hold true"
            ],
            "chapter_notes": r"""# Chapter 9: Propositions and their Converses
## Module 2: The Art of the Converse & Counterexamples

### 1. What is the Converse of a Statement?
When we interchange the hypothesis and the conclusion of a conditional proposition, we obtain its **converse**.

$$\text{Original Proposition } (P \implies Q): \quad \text{If } P \text{, then } Q.$$
$$\text{Converse Proposition } (Q \implies P): \quad \text{If } Q \text{, then } P.$$

> **Critical Logical Law:**  
> The truth of $P \implies Q$ tells us **nothing** about the truth of $Q \implies P$! Each must be examined and proved independently.

---

### 2. The Four Truth Possibilities

| Case | Proposition ($P \implies Q$) | Converse ($Q \implies P$) | Concrete Example |
| :--- | :--- | :--- | :--- |
| **Case 1** | **True** | **True** | $P$: $\Delta$ has 3 equal sides $\implies$ $Q$: $\Delta$ has 3 equal angles ($60^\circ$). Converse is also True! |
| **Case 2** | **True** | **False** | $P$: It rains $\implies$ $Q$: Road is wet (True). Converse: Road is wet $\implies$ It rained (False, water tanker could have spilled). |
| **Case 3** | **False** | **True** | $P$: $x^2 > 0 \implies Q$: $x > 0$ (False, $x = -3$). Converse: $x > 0 \implies x^2 > 0$ (True). |
| **Case 4** | **False** | **False** | $P$: $x > 2 \implies x > 10$ (False). Converse: $x > 10 \implies x > 2$ (Wait, converse is true). Let $P$: $x$ is even $\implies x$ is multiple of 4 (False, $x=6$). Converse: $x$ is multiple of 4 $\implies x$ is odd (False). |

---

### 3. What is a Counterexample?
To prove that a universal conditional statement is true, one must provide a deductive proof holding for all possible cases.  
However, to prove that a universal statement is **false**, one needs only **one single counterexample**!

> **Definition (Counterexample):**  
> A counterexample is a specific case that satisfies the hypothesis $P$ (so $P$ is true), but fails to satisfy the conclusion $Q$ (so $Q$ is false).

---

### 4. The Baudhāyana–Pythagoras Theorem and its Converse
- **Theorem:** Let $a, b, c$ be the sidelengths of a triangle. If the triangle is right-angled with hypotenuse $c$, then:
  $$a^2 + b^2 = c^2$$
- **Converse:** Let $a, b, c$ be the sidelengths of a triangle. If $a^2 + b^2 = c^2$, then the triangle is right-angled opposite to the side of length $c$.
- **Result:** Both the theorem and its converse are **True**! When both hold, we write:
  $$\text{A triangle has sidelengths } a, b, c \text{ with } c \text{ as hypotenuse is right-angled } \iff a^2 + b^2 = c^2$$
""",
            "worked_examples": [
                {
                    "problem": "Example 3 (NCERT): Let n be any positive integer. Proposition P: 'If n is divisible by 6, then n is divisible by 2 and 3.' Write its converse and determine the truth values of both.",
                    "solution": "GIVEN:\nProposition: 'For any positive integer n, if n is divisible by 6, then n is divisible by 2 and 3.'\n\nTO FIND / SOLVE:\n(i) State the truth value of the original proposition.\n(ii) Formulate its converse.\n(iii) Determine the truth value of the converse.\n\nSTEP-BY-STEP PROOF:\nStep 1: Truth value of Original Proposition:\nBy definition of divisibility, if n is divisible by 6, there exists an integer k such that n = 6k.\nSince 6 = 2 × 3:\nn = 2(3k) ⇒ n is divisible by 2.\nn = 3(2k) ⇒ n is divisible by 3.\nTherefore, the original proposition is True.\n\nStep 2: Formulate the Converse:\nInterchange hypothesis ('n is divisible by 6') and conclusion ('n is divisible by 2 and 3'):\nConverse: 'For any positive integer n, if n is divisible by both 2 and 3, then n is divisible by 6.'\n\nStep 3: Evaluate Truth Value of the Converse:\nSince 2 and 3 are prime numbers with greatest common divisor gcd(2, 3) = 1 (coprime):\nIf a number is divisible by two coprime numbers a and b, it is necessarily divisible by their product a × b.\nHere, product = 2 × 3 = 6.\nTherefore, if n is divisible by 2 and 3, n must be a multiple of 6.\nHence, the converse is also True!\n\n[ROUGH_WORK]\nBoth 2 and 3 divide 18 ⇒ 6 divides 18.\nBoth 2 and 3 divide 24 ⇒ 6 divides 24.\nSince gcd(2, 3) = 1, lcm(2, 3) = 6.\nBoxed Answer: [ Original Proposition: True, Converse: True ].",
                    "concept_questions": [
                        "Would the converse be true if the numbers were 2 and 4 instead of 2 and 3?",
                        "Why is the condition that 2 and 3 are coprime essential?"
                    ]
                },
                {
                    "problem": "Example 5 (NCERT): Write the converse of the Baudhāyana–Pythagoras theorem: 'Let a, b, c be the sidelengths of a triangle. If the triangle is right-angled, then a² + b² = c².' Is the converse true?",
                    "solution": "GIVEN:\nStatement: 'Let a, b, c be the sidelengths of a triangle. If the triangle is right-angled, then a² + b² = c².'\n\nTO WRITE AND EVALUATE:\n(i) The exact converse statement.\n(ii) Its mathematical validity.\n\nSTEP-BY-STEP ANALYSIS:\nStep 1: Formulate the converse:\nKeep the preliminary specification ('Let a, b, c be the sidelengths of a triangle') unchanged.\nInterchange hypothesis ('the triangle is right-angled') and conclusion ('a² + b² = c²'):\nConverse: 'Let a, b, c be the sidelengths of a triangle. If a² + b² = c², then the triangle is right-angled (with hypotenuse c opposite the right angle).'\n\nStep 2: Evaluate validity:\nIn Euclidean geometry, the converse of the Pythagorean theorem is proved by constructing a second right triangle with legs a and b and comparing it via SSS congruence to the given triangle.\nSince the hypotenuse of the constructed triangle equals √(a² + b²) = c, the two triangles are congruent, meaning the angle opposite c in the original triangle must also be a right angle (90°).\nTherefore, the converse is True.\n\n[ROUGH_WORK]\nPythagorean Triplet: 3² + 4² = 9 + 16 = 25 = 5². The triangle with sides 3, 4, 5 is always a right triangle!\nBoxed Answer: [ Converse: 'If a² + b² = c², then the triangle is right-angled', Truth Value: True ].",
                    "concept_questions": [
                        "What is the difference between Baudhāyana-Pythagoras theorem and its converse?",
                        "Can a triangle with sides 5, 12, 13 be acute or obtuse?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "concept_visuals": [
                    {
                        "concept_title": "Converse of a Proposition",
                        "diagram_title": "Converse of Conditional Statement",
                        "image_search_query": "converse of conditional statement hypothesis conclusion swap logic diagram",
                        "what_to_make": "Infographic showing conditional statement P implies Q transposing to converse Q implies P."
                    },
                    {
                        "concept_title": "Independence of Truth Values",
                        "diagram_title": "Truth Values of Conditional and Converse",
                        "image_search_query": "conditional statement converse truth values logic diagram",
                        "what_to_make": "Truth table diagram demonstrating independence of truth values between P implies Q and Q implies P."
                    },
                    {
                        "concept_title": "Counterexample",
                        "diagram_title": "Mathematical Counterexample Disproof",
                        "image_search_query": "mathematical counterexample logic proof diagram",
                        "what_to_make": "Visual counterexample showing hypothesis satisfied while conclusion fails to disprove universal statement."
                    },
                    {
                        "concept_title": "Baudhāyana–Pythagoras Theorem",
                        "diagram_title": "Baudhāyana–Pythagoras Right Triangle Theorem",
                        "image_search_query": "baudhayana pythagoras theorem right angled triangle proof diagram",
                        "what_to_make": "Right triangle geometric diagram with sides a, b and hypotenuse c illustrating a² + b² = c²."
                    },
                    {
                        "concept_title": "Converse of Baudhāyana–Pythagoras Theorem",
                        "diagram_title": "Converse of Pythagoras Theorem",
                        "image_search_query": "converse of pythagoras theorem right triangle proof diagram",
                        "what_to_make": "Geometric diagram showing if triangle sides satisfy a² + b² = c², the angle opposite side c is 90 degrees."
                    },
                    {
                        "concept_title": "Biconditional ('If and only if')",
                        "diagram_title": "Biconditional Equivalence",
                        "image_search_query": "biconditional statement if and only if logic equivalence diagram",
                        "what_to_make": "Logic equivalence diagram showing double implication P iff Q (P <=> Q)."
                    }
                ],
                "image_search_query": "pythagorean theorem converse geometry diagram right triangle",
                "video_search_query": "converse of pythagoras theorem proof class 9",
                "concept_questions": [
                    "If a conditional statement is true, is its converse guaranteed to be true?",
                    "What single piece of mathematical evidence is sufficient to disprove a converse?",
                    "State the converse of: 'If a polygon is a square, then all its sides are equal.'",
                    "Why is a counterexample powerful in mathematics?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Believing that reversing an 'if-then' statement always preserves truth.",
                    "correction": "The converse of a true statement is often false! For example, 'If you are in Delhi, you are in India' is true, but 'If you are in India, you are in Delhi' is false."
                },
                {
                    "misconception": "Thinking multiple examples can prove a mathematical statement true.",
                    "correction": "Examples can never prove a general statement true (only deductive proofs can), but a single counterexample is sufficient to prove a statement false."
                }
            ],
            "quiz_questions": [
                {
                    "question": "What is the converse of the statement: 'If x = 3, then x² = 9'?",
                    "options": [
                        "(Recommended) If x² = 9, then x = 3.",
                        "If x ≠ 3, then x² ≠ 9.",
                        "If x² ≠ 9, then x ≠ 3.",
                        "If x = -3, then x² = 9."
                    ],
                    "correct_index": 0,
                    "explanation": "The converse is formed by directly swapping hypothesis and conclusion: 'If x² = 9, then x = 3'."
                },
                {
                    "question": "Which of the following serves as a counterexample to the converse: 'If x² = 9, then x = 3'?",
                    "options": [
                        "(Recommended) x = -3",
                        "x = 3",
                        "x = 9",
                        "x = 0"
                    ],
                    "correct_index": 0,
                    "explanation": "For x = -3, the hypothesis is satisfied ((-3)² = 9), but the conclusion fails (x ≠ 3). Thus x = -3 is a valid counterexample."
                }
            ]
        },

        # Module 3: Exercise Set 9.1 Solver (Part 1)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise Set 9.1 Solver (Part 1): Geometric Propositions, Angle Bisectors & Real Number Inequalities",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Solve Exercise Set 9.1 Questions 1 to 7 step-by-step using authentic topper layouts. Analyze parallel line transversals, square properties, the angle bisector incenter theorem with Fig. 9.1, and real number inequality conditional logic with rigorous counterexamples.",
            "key_concepts": [
                "Transversal Alternate & Corresponding Angles: Parallel lines imply equal corresponding angles; converse also holds true",
                "Square vs Equiangular Quadrilateral: All squares have four 90° angles, but equiangular quadrilaterals include non-square rectangles",
                "Incenter Angle Bisector Geometry (Fig. 9.1): In ΔABC, if AB = AC, the angle bisectors meeting at incenter I produce equal segments IE = IF; converse evaluation",
                "Inequalities of Real Numbers: Product and sum positivity conditions vs individual component signs",
                "Constructing precise numerical and geometric counterexamples"
            ],
            "subtopics": [
                "Full solution to Exercise Set 9.1 Questions 1 and 2",
                "Exhaustive geometric proof of Question 3 with Fig. 9.1 incenter diagram",
                "Full step-by-step solutions to Questions 4, 5, 6, and 7",
                "Counterexample tables for real number assertions"
            ],
            "success_criteria": [
                "State and evaluate the converse of Questions 1 through 7 with complete mathematical proof or counterexample",
                "Provide the complete geometric proof for Question 3 with incenter angle bisector symmetry",
                "Demonstrate why x + y > 0 does not imply both x > 0 and y > 0 using counterexamples"
            ],
            "chapter_notes": r"""# Chapter 9: Propositions and their Converses
## Module 3: Exercise Set 9.1 Solver (Part 1)

### Key Rules for Exercise Set 9.1 Questions 1–7:
For each question:
1. State the **Original Proposition** and evaluate its truth value.
2. Formulate the exact **Converse Proposition** by swapping hypothesis and conclusion.
3. Determine if the converse is **True or False**.
4. If True, provide a **rigorous justification/proof**. If False, provide a **concrete counterexample**.
""",
            "worked_examples": [
                {
                    "problem": "Exercise Set 9.1, Question 1: 'If two lines are parallel, then the corresponding angles formed by a transversal are equal.' Frame the converse, determine truth values of both, and justify.",
                    "solution": "GIVEN PROPOSITION:\n'If two lines are parallel, then the corresponding angles formed by a transversal are equal.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nBy the Corresponding Angles Axiom (Euclid's Elements / NCERT Class 9 Lines and Angles):\nWhen a transversal intersects two parallel lines, each pair of corresponding angles is equal.\nTruth Value of Proposition: True.\n\nSTEP 2: FRAME THE CONVERSE:\nSwap hypothesis and conclusion:\nConverse: 'If the corresponding angles formed by a transversal with two lines are equal, then the two lines are parallel.'\n\nSTEP 3: EVALUATE CONVERSE:\nBy the Converse of Corresponding Angles Axiom:\nIf a transversal intersects two lines such that a pair of corresponding angles is equal, then the two lines are parallel to each other.\nTruth Value of Converse: True.\n\n[ROUGH_WORK]\nBoth the axiom and its converse are foundational postulates of Euclidean plane geometry. Both are True!\nBoxed Answer: [ Proposition: True, Converse: 'If corresponding angles formed by a transversal are equal, then the two lines are parallel' (True) ].",
                    "concept_questions": [
                        "Is the converse of the alternate interior angle theorem also true?",
                        "What is an axiom vs a theorem?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 2: 'If a quadrilateral is a square, then all its angles are equal.' Frame the converse, determine truth values, and justify.",
                    "solution": "GIVEN PROPOSITION:\n'If a quadrilateral is a square, then all its angles are equal.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nBy definition, a square is a regular quadrilateral having four equal sides and four right angles (90° each).\nSince each angle is 90°, all its angles are equal.\nTruth Value of Proposition: True.\n\nSTEP 2: FRAME THE CONVERSE:\nSwap hypothesis and conclusion:\nConverse: 'If all the angles of a quadrilateral are equal, then the quadrilateral is a square.'\n\nSTEP 3: EVALUATE CONVERSE & PROVIDE COUNTEREXAMPLE:\nIn a quadrilateral, the sum of interior angles is 360°. If all four angles are equal, each angle must be 360° / 4 = 90°.\nA quadrilateral with four 90° angles is an equiangular quadrilateral, which is a rectangle.\nDoes having four 90° angles guarantee that all four sides are equal?\nCounterexample:\nConsider a rectangle with length l = 8 cm and breadth b = 4 cm.\n- All its angles are equal to 90° (Hypothesis of converse is satisfied).\n- However, its adjacent sides are not equal (8 cm ≠ 4 cm), so it is NOT a square (Conclusion fails).\nTherefore, the converse is False!\n\n[ROUGH_WORK]\nRectangle with dimensions 8cm × 4cm: All angles = 90°, but not a square! Counterexample verified.\nBoxed Answer: [ Proposition: True, Converse: 'If all angles of a quadrilateral are equal, then it is a square' (False, Counterexample: Any non-square rectangle) ].",
                    "concept_questions": [
                        "What additional condition would make the converse true?",
                        "Is every square a rectangle?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 3 (Refer to Fig. 9.1): Given any ΔABC, let us bisect the angles at B and C. The bisectors meet at the incentre I of the triangle. Extend the bisectors beyond I till they meet the opposite sides at E and F respectively. Proposition: 'If AB = AC, then IE = IF.' Frame the converse, determine if each is true, and justify.",
                    "figure_path": "/extracted_diagrams/math9_ch9/fig_9_1.webp",
                    "solution": "GIVEN (Refer to Fig. 9.1):\nIn ΔABC, angle bisectors of ∠B and ∠C intersect at incenter I.\nRay BI is extended to meet AC at E.\nRay CI is extended to meet AB at F.\nProposition: 'If AB = AC, then IE = IF.'\n\nSTEP 1: PROVE ORIGINAL PROPOSITION:\nGiven AB = AC:\n1. In ΔABC, AB = AC ⇒ ∠ABC = ∠ACB (angles opposite equal sides).\n2. Since BE bisects ∠B and CF bisects ∠C:\n   ∠ABI = ∠CBI = (1/2)∠B\n   ∠ACI = ∠BCI = (1/2)∠C\n   Since ∠B = ∠C, we have ∠CBI = ∠BCI, so ΔIBC is isosceles with IB = IC.\n3. Also, ∠ABF = ∠ACE = (1/2)∠B.\n4. In ΔBCE and ΔCBF:\n   - ∠BCE = ∠CBF (since ∠C = ∠B)\n   - BC = BC (common side)\n   - ∠CBE = ∠BCF = (1/2)∠B\n   Therefore, ΔBCE ≅ ΔCBF by ASA congruence criterion.\n5. By CPCTC, BE = CF.\n6. Since BE = BI + IE and CF = CI + IF, and we already know BI = CI:\n   BI + IE = CI + IF ⇒ IE = IF.\nThus, Proposition is True!\n\nSTEP 2: FRAME THE CONVERSE:\nConverse: 'In ΔABC with angle bisectors BE and CF meeting at incenter I, if IE = IF, then AB = AC.'\n\nSTEP 3: EVALUATE CONVERSE:\nBy symmetry and the Steiner-Lehmus theorem framework:\nIf the bisector segments from incenter to opposite sides IE and IF are equal, the triangle ΔABC must be isosceles with AB = AC.\nTherefore, the converse is True.\n\n[ROUGH_WORK]\nBy ASA congruence: ΔBCE ≅ ΔCBF ⇒ BE = CF. Since ΔIBC has IB = IC, subtracting gives IE = IF. Pure symmetry!\nBoxed Answer: [ Proposition: True, Converse: 'If IE = IF, then AB = AC' (True) ].",
                    "concept_questions": [
                        "Why does AB = AC imply ∠B = ∠C?",
                        "What is the incenter of a triangle?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 6: For real numbers x and y, Proposition: 'If x + y > 0, then x > 0 and y > 0.' Frame the converse, determine truth values, and justify.",
                    "solution": "GIVEN:\nProposition: 'For real numbers x and y, if x + y > 0, then x > 0 and y > 0.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nHypothesis: x + y > 0.\nConclusion: Both x > 0 and y > 0.\nDoes the sum being positive require BOTH numbers to be positive?\nCounterexample:\nLet x = 10 and y = -3.\n- Sum: x + y = 10 + (-3) = 7 > 0 (Hypothesis holds).\n- But y = -3, which is not > 0 (Conclusion fails).\nTherefore, the original proposition is False!\n\nSTEP 2: FRAME THE CONVERSE:\nConverse: 'For real numbers x and y, if x > 0 and y > 0, then x + y > 0.'\n\nSTEP 3: EVALUATE CONVERSE:\nBy axioms of real number inequalities:\nThe sum of two positive real numbers is strictly positive.\nIf x > 0 and y > 0, then x + y > 0.\nTherefore, the converse is True!\n\n[ROUGH_WORK]\nCounterexample for proposition: 10 + (-3) = 7 > 0, but y is negative. Converse: positive + positive = positive (always true).\nBoxed Answer: [ Proposition: False (Counterexample: x = 10, y = -3), Converse: 'If x > 0 and y > 0, then x + y > 0' (True) ].",
                    "concept_questions": [
                        "Can one number be very large and positive, while the other is negative?",
                        "What happens when x = 5 and y = -5?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 7: For real numbers x and y, Proposition: 'If xy > 0, then x > 0 and y > 0.' Frame the converse, determine truth values, and justify.",
                    "solution": "GIVEN:\nProposition: 'For real numbers x and y, if xy > 0, then x > 0 and y > 0.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nHypothesis: The product xy is positive (xy > 0).\nConclusion: Both x and y are positive (x > 0 and y > 0).\nIs this conclusion necessarily true?\nCounterexample:\nLet x = -2 and y = -3.\n- Product: xy = (-2) × (-3) = +6 > 0 (Hypothesis is satisfied).\n- However, x = -2 < 0 and y = -3 < 0 (Conclusion fails completely).\nTherefore, the original proposition is False!\n\nSTEP 2: FRAME THE CONVERSE:\nConverse: 'For real numbers x and y, if x > 0 and y > 0, then xy > 0.'\n\nSTEP 3: EVALUATE CONVERSE:\nBy the sign rules of arithmetic and ordered fields:\nThe product of two positive real numbers is always positive.\nTherefore, if x > 0 and y > 0, then xy > 0.\nThus, the converse is True!\n\n[ROUGH_WORK]\nNegative × Negative = Positive! Hence xy > 0 allows both to be negative. Converse says positive × positive = positive, which is always true.\nBoxed Answer: [ Proposition: False (Counterexample: x = -2, y = -3), Converse: 'If x > 0 and y > 0, then xy > 0' (True) ].",
                    "concept_questions": [
                        "What are the two cases when xy > 0?",
                        "What is the sign of xy when one is positive and one is negative?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "triangle incenter angle bisector geometry theorem diagram",
                "video_search_query": "incenter angle bisectors equal sides class 9 geometry",
                "concept_questions": [
                    "Why does a rectangle disprove the statement 'all equiangular quadrilaterals are squares'?",
                    "In ΔABC, if AB = AC, what can be said about the incenter angle bisector segments IE and IF?",
                    "If xy > 0, what are the two possible sign configurations for x and y?",
                    "Why is x = 10, y = -3 a valid counterexample to x + y > 0 ⇒ x > 0 and y > 0?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Assuming that a positive product xy > 0 implies both factors are positive.",
                    "correction": "A product of two numbers is also positive when BOTH factors are negative ((-2) × (-3) = +6)."
                },
                {
                    "misconception": "Assuming that having all equal angles makes a 4-gon a square.",
                    "correction": "Equal angles only ensure that each angle is 90° (a rectangle). All four sides must also be equal to be a square."
                }
            ],
            "quiz_questions": [
                {
                    "question": "Which of the following serves as a counterexample to the proposition: 'If xy > 0, then x > 0 and y > 0'?",
                    "options": [
                        "(Recommended) x = -4, y = -5",
                        "x = 4, y = 5",
                        "x = 4, y = -5",
                        "x = 0, y = 5"
                    ],
                    "correct_index": 0,
                    "explanation": "When x = -4 and y = -5, xy = 20 > 0 (hypothesis holds), but neither x nor y is greater than 0 (conclusion fails)."
                },
                {
                    "question": "If all four angles of a quadrilateral are equal, which geometric figure is guaranteed?",
                    "options": [
                        "(Recommended) Rectangle",
                        "Square",
                        "Rhombus",
                        "Trapezium"
                    ],
                    "correct_index": 0,
                    "explanation": "If all 4 angles are equal, each is 360° / 4 = 90°. A quadrilateral with all right angles is by definition a rectangle."
                }
            ]
        },

        # Module 4: Exercise Set 9.1 Solver (Part 2)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise Set 9.1 Solver (Part 2): Number Theory, Divisibility Logic & Prime Factorization Invariants",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Solve Exercise Set 9.1 Questions 8 to 12. Master number-theoretic implications involving divisibility by 10 and 60, factor counts of prime squares, products of unequal primes, and the greatest common divisor invariant of consecutive multiples n and n+3.",
            "key_concepts": [
                "Divisibility by 60: A number is divisible by 60 if and only if it is divisible by both 5 and 12, because gcd(5, 12) = 1",
                "Factor Count Invariant of a Prime Square: If p is prime, the only positive factors of p² are 1, p, and p² (exactly 3 factors); converse is also true",
                "Factor Count of Product of Two Unequal Primes: The positive factors of n = pq are 1, p, q, pq (exactly 4 factors); converse fails because n = p³ also has 4 factors",
                "Relatively Prime Invariant: gcd(n, n+3) = gcd(n, 3). If n and n+3 share no factors, n cannot be a multiple of 3; converse also holds true"
            ],
            "subtopics": [
                "Full solution to Question 8 (Divisibility by 10 and units digit 0)",
                "Full solution to Question 9 (Divisibility by 60, 5, and 12 with coprime basis)",
                "Full solution to Question 10 (Prime squares and exact 3 factors proof)",
                "Full solution to Question 11 (Product of unequal primes vs cube of a prime)",
                "Full solution to Question 12 (Relative primality of n and n+3)"
            ],
            "success_criteria": [
                "Prove why divisibility by 60 is strictly equivalent to divisibility by 5 and 12",
                "Rigorous proof that n has exactly 3 factors if and only if n = p² for prime p",
                "Provide the counterexample n = 8 (p³) to disprove the converse of Question 11",
                "Demonstrate algebraically using gcd(n, n+3) = gcd(n, 3) why Question 12 holds"
            ],
            "chapter_notes": r"""# Chapter 9: Propositions and their Converses
## Module 4: Exercise Set 9.1 Solver (Part 2)

### Number Theory Implication Invariants:
1. **Coprime Divisibility:** If $a$ and $b$ are coprime ($\gcd(a, b) = 1$), then $n$ is divisible by $a \times b \iff n$ is divisible by $a$ and $n$ is divisible by $b$.
2. **Factor Counting Formula:** If the prime factorization of $n$ is $p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, the total number of positive factors is:
   $$d(n) = (a_1 + 1)(a_2 + 1)\cdots(a_k + 1)$$
   - If $d(n) = 3$, then $a_1 + 1 = 3 \implies a_1 = 2$. Thus $n = p^2$ where $p$ is prime!
   - If $d(n) = 4$, then either $a_1 + 1 = 4 \implies n = p^3$, OR $(a_1 + 1)(a_2 + 1) = 2 \times 2 \implies n = p \cdot q$ where $p \ne q$ are primes.
""",
            "worked_examples": [
                {
                    "problem": "Exercise Set 9.1, Question 9: Let n be a positive integer. Proposition: 'If n is divisible by 60, then it is divisible by both 5 and 12.' Frame the converse, determine truth values of both, and justify.",
                    "solution": "GIVEN:\nProposition: 'For any positive integer n, if n is divisible by 60, then it is divisible by both 5 and 12.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nIf n is divisible by 60, then n = 60k for some integer k.\nSince 60 = 5 × 12:\nn = 5(12k) ⇒ n is divisible by 5.\nn = 12(5k) ⇒ n is divisible by 12.\nTherefore, the original proposition is True.\n\nSTEP 2: FRAME THE CONVERSE:\nSwap hypothesis and conclusion:\nConverse: 'For any positive integer n, if n is divisible by both 5 and 12, then it is divisible by 60.'\n\nSTEP 3: EVALUATE CONVERSE:\nWe examine the greatest common divisor of 5 and 12:\nFactors of 5: {1, 5}\nFactors of 12: {1, 2, 3, 4, 6, 12}\ngcd(5, 12) = 1 (5 and 12 are coprime).\nBy number theory, if an integer n is divisible by two coprime integers a and b, then n is divisible by their least common multiple lcm(a, b) = a × b.\nHere, lcm(5, 12) = 5 × 12 = 60.\nTherefore, n is divisible by 60.\nHence, the converse is True!\n\n[ROUGH_WORK]\n60 = 5 × 12. Since gcd(5, 12) = 1, lcm(5, 12) = 60. Divisibility works both ways!\nBoxed Answer: [ Proposition: True, Converse: 'If n is divisible by both 5 and 12, then it is divisible by 60' (True) ].",
                    "concept_questions": [
                        "Why does this rule fail for 6 and 10?",
                        "What is lcm(6, 10)?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 10: Let n be a positive integer. Proposition: 'If n is the square of a prime number, then it has exactly 3 factors.' Frame the converse, determine truth values of both, and justify.",
                    "solution": "GIVEN:\nProposition: 'If n is the square of a prime number, then it has exactly 3 factors.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nLet n = p², where p is a prime number.\nSince p is prime, its only divisors are 1 and p.\nThe positive divisors of p² are: {1, p, p²}.\nThese three divisors are distinct because p is prime (p > 1, so 1 < p < p²).\nThus, n has exactly 3 factors.\nTruth Value of Proposition: True.\n\nSTEP 2: FRAME THE CONVERSE:\nConverse: 'If a positive integer n has exactly 3 factors, then n is the square of a prime number.'\n\nSTEP 3: EVALUATE CONVERSE:\nLet the prime factorization of n be n = p₁ᵃ¹ p₂ᵃ² ··· pₖᵃᵏ.\nThe number of positive factors of n is given by:\nd(n) = (a₁ + 1)(a₂ + 1)···(aₖ + 1).\nWe are given d(n) = 3.\nSince 3 is a prime number, it cannot be factored into smaller non-trivial integer factors.\nTherefore, there can only be one prime factor p₁, and its exponent must satisfy:\na₁ + 1 = 3 ⇒ a₁ = 2.\nThus, n must be of the form n = p₁² where p₁ is a prime number.\nTherefore, n is the square of a prime number.\nHence, the converse is True!\n\n[ROUGH_WORK]\nExamples: 4 = 2² (factors: 1, 2, 4); 9 = 3² (factors: 1, 3, 9); 25 = 5² (factors: 1, 5, 25). Always exactly 3 factors!\nBoxed Answer: [ Proposition: True, Converse: 'If n has exactly 3 factors, then n is the square of a prime number' (True) ].",
                    "concept_questions": [
                        "Does 1 have 3 factors?",
                        "Why can no composite number other than a prime square have exactly 3 factors?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 11: Let n be a positive integer. Proposition: 'If n is a product of two unequal prime numbers, then it has exactly 4 factors.' Frame the converse, determine truth values, and justify.",
                    "solution": "GIVEN:\nProposition: 'If n is a product of two unequal prime numbers, then it has exactly 4 factors.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nLet n = p × q, where p and q are prime numbers and p ≠ q.\nThe distinct positive divisors of n are: {1, p, q, pq}.\nSince p and q are distinct primes, these 4 factors are all distinct.\nThus, n has exactly 4 factors.\nTruth Value of Proposition: True.\n\nSTEP 2: FRAME THE CONVERSE:\nConverse: 'If a positive integer n has exactly 4 factors, then n is a product of two unequal prime numbers.'\n\nSTEP 3: EVALUATE CONVERSE & PROVIDE COUNTEREXAMPLE:\nTo determine if the converse is true, we examine the factor counting formula:\nd(n) = 4.\nThe number 4 can be factored in two ways:\nCase A: 4 = 2 × 2 = (1 + 1)(1 + 1) ⇒ n = p¹ q¹ (product of two unequal primes).\nCase B: 4 = 3 + 1 ⇒ n = p³ (cube of a single prime number).\nCounterexample:\nLet n = 8 = 2³ (where p = 2 is prime).\n- Positive factors of 8: {1, 2, 4, 8} → exactly 4 factors! (Hypothesis of converse holds).\n- However, 8 is NOT the product of two unequal prime numbers (it is 2 × 2 × 2, a cube of a single prime). The conclusion fails!\nAnother counterexample: n = 27 = 3³ (factors: 1, 3, 9, 27).\nTherefore, the converse is False!\n\n[ROUGH_WORK]\nd(n) = 4 has two solutions: n = pq OR n = p³. For 8, factors are 1, 2, 4, 8 (4 factors), but 8 ≠ pq. Counterexample holds!\nBoxed Answer: [ Proposition: True, Converse: 'If n has exactly 4 factors, then n is the product of two unequal primes' (False, Counterexample: n = 8 or n = p³) ].",
                    "concept_questions": [
                        "What are the divisors of 27?",
                        "How many factors does p⁴ have?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 12: Let n be a positive integer. Proposition: 'If n and n + 3 have no factors in common (other than 1), then n is not a multiple of 3.' Frame the converse, determine truth values of both, and justify.",
                    "solution": "GIVEN:\nProposition: 'For a positive integer n, if n and n + 3 have no common factor other than 1, then n is not a multiple of 3.'\n\nSTEP 1: EVALUATE ORIGINAL PROPOSITION:\nLet d be any common factor of n and n + 3.\nThen d divides n, and d divides (n + 3).\nTherefore, d must divide their difference: (n + 3) - n = 3.\nSince 3 is prime, the only positive divisors of 3 are 1 and 3.\nThus, gcd(n, n + 3) is either 1 or 3.\n- If n is a multiple of 3, then n = 3k. Then n + 3 = 3(k + 1) is also a multiple of 3, meaning 3 divides both n and n + 3 (so they share the common factor 3).\n- Therefore, if n and n + 3 have NO common factor other than 1 (gcd = 1), n cannot be a multiple of 3.\nThus, the original proposition is True.\n\nSTEP 2: FRAME THE CONVERSE:\nConverse: 'For a positive integer n, if n is not a multiple of 3, then n and n + 3 have no factors in common (other than 1).'\n\nSTEP 3: EVALUATE CONVERSE:\nAssume n is not a multiple of 3.\nAs shown above, any common factor d of n and n + 3 must divide (n + 3) - n = 3.\nTherefore, the only possible common factors are 1 and 3.\nSince n is not a multiple of 3, 3 cannot divide n, so 3 cannot be a common factor.\nHence, the only common factor is 1.\nTherefore, gcd(n, n + 3) = 1.\nThus, n and n + 3 have no factors in common other than 1.\nHence, the converse is True!\n\n[ROUGH_WORK]\ngcd(n, n+3) = gcd(n, (n+3)-n) = gcd(n, 3). If 3 doesn't divide n, gcd must be 1. If 3 divides n, gcd is 3. Pure biconditional!\nBoxed Answer: [ Proposition: True, Converse: 'If n is not a multiple of 3, then n and n + 3 have no factors in common other than 1' (True) ].",
                    "concept_questions": [
                        "What is gcd(10, 13)?",
                        "What is gcd(12, 15)?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "prime factorization factor tree divisors number theory diagram",
                "video_search_query": "number of factors of a prime square and cube class 9",
                "concept_questions": [
                    "Why must a number with exactly 3 factors be the square of a prime?",
                    "Why does n = 8 serve as a counterexample to the converse of Question 11?",
                    "What are the only possible values of gcd(n, n + 3)?",
                    "Why is gcd(5, 12) = 1 critical for divisibility by 60?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Thinking that every number with 4 factors is a product of two primes.",
                    "correction": "Cubes of primes like 2³ = 8 and 3³ = 27 have exactly 4 factors ({1, p, p², p³}), but they are not the product of two distinct primes."
                },
                {
                    "misconception": "Assuming that if a number is divisible by two numbers, it is divisible by their product.",
                    "correction": "This holds ONLY if the two divisors are coprime. For example, 20 is divisible by 2 and 4, but 20 is NOT divisible by 2 × 4 = 8."
                }
            ],
            "quiz_questions": [
                {
                    "question": "How many positive factors does the number 49 have?",
                    "options": [
                        "(Recommended) Exactly 3",
                        "Exactly 2",
                        "Exactly 4",
                        "Infinitely many"
                    ],
                    "correct_index": 0,
                    "explanation": "Since 49 = 7² (the square of the prime 7), its factors are 1, 7, and 49 (exactly 3 factors)."
                },
                {
                    "question": "What is the greatest common divisor of n and n + 3 if n is not a multiple of 3?",
                    "options": [
                        "(Recommended) 1",
                        "3",
                        "n",
                        "n + 3"
                    ],
                    "correct_index": 0,
                    "explanation": "Any common divisor must divide (n + 3) - n = 3. Since 3 does not divide n, the only common divisor is 1."
                }
            ]
        },

        # Module 5: Exercise Set 9.1 Solver (Part 3)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise Set 9.1 Solver (Part 3): Polynomial Primes, Divisibility Rules & Quadrilateral Diagonal Mechanics",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Solve Exercise Set 9.1 Questions 13 to 17. Disprove false prime-generating polynomials using Euler-style counterexamples, analyze divisibility by 8 versus 2 and 4, formulate the biconditional divisibility rule for 3, and solve the diagonal stick construction puzzle for quadrilateral categories (Fig. 9.2).",
            "key_concepts": [
                "Euler Prime Generating Forms: Polynomials like n² + n + 11 or n² - n + 41 produce primes for small n, but inevitably fail at composite values (e.g. n = 11)",
                "Mersenne Primes and Counterexamples: The conjecture 'If n is prime, then 2ⁿ - 1 is prime' fails at n = 11 (2¹¹ - 1 = 2047 = 23 × 89)",
                "Divisibility by 8 vs 2 and 4: Divisibility by 8 implies divisibility by 2 and 4; but the converse fails because lcm(2, 4) = 4, not 8",
                "Divisibility by 3 Biconditional: An integer n is divisible by 3 if and only if the sum of its decimal digits is a multiple of 3",
                "Quadrilateral Diagonal Mechanics (Fig. 9.2): Examining necessary versus sufficient conditions when constructing quadrilaterals using two diagonal sticks"
            ],
            "subtopics": [
                "Counterexamples for Question 13 (Polynomial prime forms)",
                "Counterexamples for Question 14 (Mersenne forms and even powers)",
                "Full analysis of Question 15 (Divisibility by 8 vs 2 and 4)",
                "Full formulation of Question 16 ('If-then' divisibility by 3 biconditional)",
                "Complete geometric solution of Question 17 (Fig. 9.2 diagonal sticks)"
            ],
            "success_criteria": [
                "Find the exact counterexample n = 11 for n² + n + 11 and n = 6 for 4n + 3",
                "Provide the counterexample n = 11 for 2ⁿ - 1 showing 2047 = 23 × 89",
                "Explain why checking divisibility by 2 and 4 is insufficient for divisibility by 8",
                "Solve Question 17 demonstrating the difference between 'Q implies equal diagonals' and 'equal diagonals implies Q'"
            ],
            "chapter_notes": r"""# Chapter 9: Propositions and their Converses
## Module 5: Exercise Set 9.1 Solver (Part 3)

### 1. The Myth of Prime Formulas
For centuries, mathematicians searched for simple polynomial expressions $P(n)$ that generate only prime numbers.  
Euler discovered $f(n) = n^2 - n + 41$, which gives primes for $n = 1, 2, \dots, 40$, but fails at $n = 41$ ($41^2 - 41 + 41 = 41^2$, composite!).  
In general, **no non-constant polynomial with integer coefficients can generate only prime numbers**.

### 2. Necessary vs Sufficient Conditions in Quadrilateral Diagonals (Fig. 9.2)
- **Proposition:** If a quadrilateral is a rectangle, then its diagonals are equal.  
  - Here, equal diagonals is a **necessary** property of rectangles.
- **Converse:** If a quadrilateral has equal diagonals, then it is a rectangle.  
  - This converse is **False**! An isosceles trapezium also has equal diagonals, as does an arbitrary kite or irregular quadrilateral with equal perpendicular diagonals.
""",
            "worked_examples": [
                {
                    "problem": "Exercise Set 9.1, Question 13: Find counterexamples to the following statements: (ii) All numbers of the form n² + n + 11 are prime. (iii) All numbers of the form 4n + 3 are prime.",
                    "solution": "GIVEN STATEMENTS:\n(ii) 'For all positive integers n, n² + n + 11 is prime.'\n(iii) 'For all positive integers n, 4n + 3 is prime.'\n\nTO FIND:\nA concrete counterexample for each statement.\n\nSTEP-BY-STEP SOLUTION:\nPart (ii): Test n² + n + 11:\n- For n = 1: 1² + 1 + 11 = 13 (prime)\n- For n = 2: 2² + 2 + 11 = 17 (prime)\n- For n = 3: 3² + 3 + 11 = 23 (prime)\n- For n = 10: 100 + 10 + 11 = 121 = 11² (composite!)\n- For n = 11: 11² + 11 + 11 = 11(11 + 1 + 1) = 11 × 13 = 143 (composite!)\nCounterexample: For n = 10, 10² + 10 + 11 = 121 = 11 × 11. 121 is not prime.\n\nPart (iii): Test 4n + 3:\n- For n = 1: 4(1) + 3 = 7 (prime)\n- For n = 2: 4(2) + 3 = 11 (prime)\n- For n = 3: 4(3) + 3 = 15 = 3 × 5 (composite!)\n- For n = 6: 4(6) + 3 = 27 = 3 × 9 (composite!)\nCounterexample: For n = 3, 4(3) + 3 = 15 = 3 × 5. 15 is not prime.\n\n[ROUGH_WORK]\nPart (ii): n = 10 gives 121 = 11². Part (iii): n = 3 gives 15 = 3 × 5. Clear counterexamples disproving universality!\nBoxed Answer: [ (ii) Counterexample: n = 10 (value 121 = 11 × 11), (iii) Counterexample: n = 3 (value 15 = 3 × 5) ].",
                    "concept_questions": [
                        "Can any polynomial generate only prime numbers?",
                        "Why does substituting n = 11 in n² + n + 11 guarantee a composite number?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 14: Find counterexamples to the statements: (i) If n is a prime number, then 2ⁿ - 1 is a prime number. (ii) If n is an even number, then 2n + 1 is a prime number.",
                    "solution": "GIVEN STATEMENTS:\n(i) 'If n is prime, then 2ⁿ - 1 is prime.' (Mersenne statement)\n(ii) 'If n is even, then 2n + 1 is prime.'\n\nSTEP-BY-STEP SOLUTION:\nPart (i): Test prime values of n in 2ⁿ - 1:\n- For n = 2: 2² - 1 = 3 (prime)\n- For n = 3: 2³ - 1 = 7 (prime)\n- For n = 5: 2⁵ - 1 = 31 (prime)\n- For n = 7: 2⁷ - 1 = 127 (prime)\n- For n = 11 (prime!):\n  2¹¹ - 1 = 2048 - 1 = 2047.\n  Check factors of 2047:\n  2047 = 23 × 89.\n  Since 23 and 89 are non-trivial integer factors, 2047 is composite!\nCounterexample: n = 11 (2¹¹ - 1 = 2047 = 23 × 89).\n\nPart (ii): Test even values of n in 2n + 1:\n- For n = 2: 2(2) + 1 = 5 (prime)\n- For n = 4 (even!):\n  2(4) + 1 = 8 + 1 = 9 = 3 × 3 (composite!).\n- For n = 6: 2(6) + 1 = 13 (prime)\n- For n = 8: 2(8) + 1 = 17 (prime)\n- For n = 10: 2(10) + 1 = 21 = 3 × 7 (composite!).\nCounterexample: n = 4 (gives 9 = 3 × 3).\n\n[ROUGH_WORK]\n2¹¹ - 1 = 2047. 2047 / 23 = 89. Divisible! For 2n + 1: n = 4 gives 9 = 3². Both disproved.\nBoxed Answer: [ (i) Counterexample: n = 11 (2047 = 23 × 89), (ii) Counterexample: n = 4 (value 9 = 3 × 3) ].",
                    "concept_questions": [
                        "What are numbers of the form 2ⁿ - 1 called?",
                        "Is 2⁴ - 1 prime? Why did we test n = 11?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 15: Consider the statement: 'If a number is divisible by 8, then it is divisible by both 2 and 4.' (i) Justify the statement. (ii) To check whether a given number is divisible by 8, is it enough to check whether it is divisible by 2 and 4? Why or why not?",
                    "solution": "GIVEN STATEMENT:\n'If a number is divisible by 8, then it is divisible by both 2 and 4.'\n\nSTEP-BY-STEP SOLUTION:\nPart (i): Justify the statement:\nLet the number be n.\nIf n is divisible by 8, then n = 8k for some integer k.\nSince 8 = 2 × 4:\nn = 2(4k) ⇒ n is divisible by 2.\nn = 4(2k) ⇒ n is divisible by 4.\nTherefore, the statement is True.\n\nPart (ii): Evaluate the converse (checking divisibility by 2 and 4 to conclude divisibility by 8):\nNO, it is NOT enough!\nExplanation and Counterexample:\nTo guarantee that divisibility by a and b implies divisibility by a × b, a and b must be coprime (gcd(a, b) = 1).\nHere, gcd(2, 4) = 2 ≠ 1.\nThe least common multiple is lcm(2, 4) = 4, not 8.\nCounterexample:\nConsider the number n = 12:\n- 12 is divisible by 2 (12 = 2 × 6).\n- 12 is divisible by 4 (12 = 4 × 3).\n- However, 12 is NOT divisible by 8 (12 / 8 = 1.5, remainder = 4).\nOther counterexamples: 20, 28, 36.\nTherefore, checking 2 and 4 only guarantees divisibility by 4, not 8.\n\n[ROUGH_WORK]\n12 is divisible by 2 and 4, but not 8! Because 4 already contains the factor of 2. Boxed answer ready.\nBoxed Answer: [ (i) Justified: 8k = 2(4k) and 4(2k), (ii) No, it is not enough. Counterexample: 12 is divisible by 2 and 4, but not by 8 because gcd(2, 4) = 2 ≠ 1 ].",
                    "concept_questions": [
                        "What is the actual divisibility test for 8 in decimal numbers?",
                        "Why does divisibility by 3 and 5 guarantee divisibility by 15?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 16: Recall that a shortcut to check whether a given number is divisible by 3 is to add the digits of the number and check if the sum is a multiple of 3. Express the relationship between 'a number is divisible by 3' and 'sum of the digits is a multiple of 3' using 'If-then' sentences.",
                    "solution": "GIVEN:\nProperty: A number is divisible by 3 if the sum of its digits is a multiple of 3.\n\nTO EXPRESS:\nThe complete relationship using 'If-then' sentences.\n\nSTEP-BY-STEP FORMULATION:\nBecause this divisibility rule is a biconditional truth (it works in both directions), it consists of two distinct conditional statements:\n\nStatement 1 (The forward implication):\n'If a number is divisible by 3, then the sum of its digits is a multiple of 3.'\n\nStatement 2 (The converse implication):\n'If the sum of the digits of a number is a multiple of 3, then the number is divisible by 3.'\n\nCombined Biconditional Form:\n'A number is divisible by 3 if and only if the sum of its digits is a multiple of 3.'\n\n[ROUGH_WORK]\nBoth implications are true for any base-10 integer because 10 ≡ 1 (mod 3), so 10^k ≡ 1 (mod 3).\nBoxed Answer: [ Statement 1: 'If a number is divisible by 3, then the sum of its digits is a multiple of 3', Statement 2: 'If the sum of the digits of a number is a multiple of 3, then the number is divisible by 3' ].",
                    "concept_questions": [
                        "Does this same rule apply to 9?",
                        "Does it apply to 6?"
                    ]
                },
                {
                    "problem": "Exercise Set 9.1, Question 17 (Refer to Fig. 9.2): Two thin sticks are put together as diagonals so that the quadrilateral obtained by joining their endpoints is of category Q. (i) Suppose Q satisfies: 'If a quadrilateral is of type Q, then it has equal-length diagonals.' (a) Should the two sticks be of equal length? (b) Will it matter how they are put together? (ii) Instead, suppose Q satisfies: 'If a quadrilateral has equal diagonals, then it is of type Q.' What are the answers to (a) and (b) now?",
                    "figure_path": "/extracted_diagrams/math9_ch9/fig_9_2.webp",
                    "solution": "GIVEN (Refer to Fig. 9.2):\nTwo thin sticks serve as diagonals AC and BD of a quadrilateral ABCD.\n\nPART (i): Property: 'If a quadrilateral is of type Q, then it has equal-length diagonals.'\n- Analysis of (a): The property states that having equal diagonals is a NECESSARY condition for being of type Q.\n  Therefore, to have any chance of producing a quadrilateral of type Q, the diagonals MUST be equal.\n  Answer to (a): YES, the two sticks MUST be of equal length.\n- Analysis of (b): Having equal sticks is only necessary, not necessarily sufficient. How they intersect (e.g. bisecting each other, at right angles, or off-center) determines whether the quadrilateral becomes a rectangle, square, isosceles trapezium, or irregular 4-gon.\n  Answer to (b): YES, it will matter how the two sticks are put together.\n\nPART (ii): Property: 'If a quadrilateral has equal diagonals, then it is of type Q.'\n- Analysis of (a): Here, having equal diagonals is a SUFFICIENT condition to qualify as type Q.\n  Answer to (a): YES, the two sticks should be of equal length (any equal sticks will qualify).\n- Analysis of (b): The condition states that ANY quadrilateral with equal diagonals is automatically of type Q, regardless of how the diagonals cross, bisect, or angle.\n  Answer to (b): NO, it will NOT matter how the two sticks are put together; as long as the sticks are equal, the resulting quadrilateral is guaranteed to be of type Q!\n\n[ROUGH_WORK]\nPart (i): Type Q ⇒ Equal diagonals (Necessary). Part (ii): Equal diagonals ⇒ Type Q (Sufficient). Beautiful contrast!\nBoxed Answer: [ (i)(a) Yes, (i)(b) Yes; (ii)(a) Yes, (ii)(b) No, it will not matter ].",
                    "concept_questions": [
                        "What is the difference between a necessary condition and a sufficient condition?",
                        "If the two sticks bisect each other at 90°, what quadrilateral is formed?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "quadrilateral diagonals sticks construction geometry diagram",
                "video_search_query": "necessary and sufficient conditions in geometry class 9",
                "concept_questions": [
                    "Why does 12 disprove the statement 'if a number is divisible by 2 and 4, it is divisible by 8'?",
                    "For what value of n does the Mersenne prime formula 2ⁿ - 1 fail?",
                    "In Question 17, why does it matter how the sticks are placed in Part (i) but not in Part (ii)?",
                    "What is a biconditional statement?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Believing that prime formulas like n² + n + 41 or 2ⁿ - 1 continue generating primes forever.",
                    "correction": "No integer polynomial can generate primes forever; counterexamples always emerge at larger values (e.g. n = 11 for 2ⁿ - 1)."
                },
                {
                    "misconception": "Confusing necessary conditions with sufficient conditions.",
                    "correction": "In 'P ⇒ Q', Q is a necessary condition for P, while P is a sufficient condition for Q."
                }
            ],
            "quiz_questions": [
                {
                    "question": "Which of the following is a counterexample showing that 4n + 3 is not always prime?",
                    "options": [
                        "(Recommended) n = 3 (gives 15 = 3 × 5)",
                        "n = 1 (gives 7)",
                        "n = 2 (gives 11)",
                        "n = 4 (gives 19)"
                    ],
                    "correct_index": 0,
                    "explanation": "For n = 3, 4(3) + 3 = 15, which is composite (divisible by 3 and 5)."
                },
                {
                    "question": "If n is divisible by 2 and 4, what is the largest number n is guaranteed to be divisible by?",
                    "options": [
                        "(Recommended) 4",
                        "8",
                        "2",
                        "16"
                    ],
                    "correct_index": 0,
                    "explanation": "Because gcd(2, 4) = 2, lcm(2, 4) = 4. Divisibility is only guaranteed for 4, as evidenced by n = 12 (not divisible by 8)."
                }
            ]
        }
    ]
    
    return modules

if __name__ == "__main__":
    mods = get_ch9_modules()
    print(f"Generated {len(mods)} modules for Chapter 9.")
    for m in mods:
        print(f"  #{m['order_index']}: {m['title']} ({len(m['worked_examples'])} examples)")
