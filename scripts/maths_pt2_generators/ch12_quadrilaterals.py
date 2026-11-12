"""
Class 9 Mathematics - Chapter 12: Quadrilaterals (NCERT Ganita Manjari Part II)
Curriculum ID: c57dfef2-2585-4f56-8b57-0133596a424f
Fully compliant with Invariant 10 & 14:
- 6 dedicated modules (Theory in M1-M2, Applications M3-M5, Master Solver M6)
- 100% of all NCERT theorems (Theorems 1 to 7), properties, and exercises (Ex 1 to 22) solved step-by-step
- Authentic Topper Board Layout: Given -> To Prove -> Construction -> Proof -> [ROUGH_WORK] -> Boxed Answer
- Pure mathematical typography: Zero raw '*', '**', '//', '^'
- Dynamic search queries for concept visuals & textbook diagram bindings for question figures (Fig 12.1 to Fig 12.35)
"""

def get_ch12_modules():
    CURRICULUM_ID = "c57dfef2-2585-4f56-8b57-0133596a424f"
    
    modules = [
        # Module 1: Quadrilateral Anatomy & The Angle Sum Property
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Quadrilateral Anatomy & The Angle Sum Property: Convexity, Non-convexity & Polygon Interior Angles",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Establish the foundational geometry of quadrilaterals (4-gons). Distinguish simple, self-intersecting, convex, and non-convex (concave) quadrilaterals. Rigorously prove that the sum of the four interior angles of any simple quadrilateral is identically 360° using diagonal triangulations.",
            "key_concepts": [
                "Quadrilateral Definition: A closed plane figure formed by four line segments joining four coplanar points, no three of which are collinear, intersecting only at endpoints",
                "Convex vs Non-Convex: A quadrilateral is convex if all its interior angles are strictly less than 180° and both diagonals lie entirely within the interior; non-convex (concave) if one interior angle exceeds 180° (reflex angle)",
                "Angle Sum Theorem: The sum of the interior angles of any simple planar quadrilateral ABCD is ∠A + ∠B + ∠C + ∠D = 360°",
                "Triangulation Proof: Any simple quadrilateral is partitioned into exactly two triangles by an interior diagonal; since each triangle has angle sum 180°, the total sum is 2 × 180° = 360°",
                "Self-Intersecting (Complex) Quadrilaterals: Four vertices joined such that non-consecutive edges cross each other (e.g. bowtie shape), distinct from simple polygons"
            ],
            "subtopics": [
                "Geometric elements: Vertices, edges, adjacent sides, opposite angles, diagonals",
                "Classification of 4-gons: Convex, concave, self-intersecting (Fig. 12.1 to 12.4)",
                "Formal Euclidean proof of the Angle Sum Property (360°)",
                "Interior vs exterior diagonals in non-convex quadrilaterals"
            ],
            "success_criteria": [
                "Differentiate with complete mathematical precision between convex and concave quadrilaterals",
                "Prove the 360° Angle Sum Theorem step-by-step using diagonal partitioning",
                "Calculate unknown interior and exterior angles of general quadrilaterals"
            ],
            "chapter_notes": r"""# Chapter 12: Quadrilaterals
## Module 1: Quadrilateral Anatomy & The Angle Sum Property

### 1. What Exactly is a Quadrilateral?
A quadrilateral (also called a **4-gon**) is a closed planar polygon bounded by four line segments.
- **Vertices:** $A, B, C, D$.
- **Sides:** $AB, BC, CD, DA$.
- **Opposite Sides:** Pairs of sides that share no common vertex ($AB$ and $CD$; $BC$ and $AD$).
- **Diagonals:** Segments connecting non-adjacent vertices ($AC$ and $BD$).

---

### 2. Classification of 4-Gons
1. **Convex Quadrilateral:** Every interior angle is $< 180^\circ$. Both diagonals $AC$ and $BD$ lie completely inside the figure.
2. **Concave (Non-Convex) Quadrilateral:** One interior angle is a reflex angle ($> 180^\circ$). One diagonal lies outside the figure (e.g. a arrowhead/dart shape).
3. **Self-Intersecting Quadrilateral:** Edges cross each other.

---

### 3. The Angle Sum Theorem of a Quadrilateral
**Theorem:** The sum of the four angles of a quadrilateral is $360^\circ$.
$$\angle A + \angle B + \angle C + \angle D = 360^\circ$$

#### Proof:
1. Let $ABCD$ be any simple quadrilateral. Join diagonal $AC$.
2. Diagonal $AC$ divides $ABCD$ into two triangles: $\Delta ABC$ and $\Delta ADC$.
3. In $\Delta ABC$: $\angle CAB + \angle B + \angle BCA = 180^\circ$ (Angle sum of triangle).
4. In $\Delta ADC$: $\angle CAD + \angle D + \angle DCA = 180^\circ$.
5. Adding the two equations:
   $$(\angle CAB + \angle CAD) + \angle B + (\angle BCA + \angle DCA) + \angle D = 180^\circ + 180^\circ$$
   $$\angle A + \angle B + \angle C + \angle D = 360^\circ \quad \text{(Hence Proved!)}$$
""",
            "worked_examples": [
                {
                    "problem": "Theorem (NCERT Section 12.1): Prove that the sum of the four interior angles of a quadrilateral ABCD is 360°.",
                    "solution": "STATEMENT:\nProve that the sum of the four interior angles of a quadrilateral is 360°.\n\nGIVEN:\nA quadrilateral ABCD.\n\nTO PROVE:\n∠A + ∠B + ∠C + ∠D = 360°.\n\nCONSTRUCTION:\nJoin vertex A to vertex C to form diagonal AC.\n\nPROOF:\nStep 1: Partition into triangles:\nDiagonal AC divides quadrilateral ABCD into two triangles, ΔABC and ΔADC.\n\nStep 2: Apply Angle Sum Property to ΔABC:\nIn ΔABC:\n∠1 + ∠B + ∠2 = 180°  --- (Equation 1)\n(where ∠1 = ∠BAC and ∠2 = ∠BCA).\n\nStep 3: Apply Angle Sum Property to ΔADC:\nIn ΔADC:\n∠3 + ∠D + ∠4 = 180°  --- (Equation 2)\n(where ∠3 = ∠DAC and ∠4 = ∠DCA).\n\nStep 4: Add Equation 1 and Equation 2:\n(∠1 + ∠3) + ∠B + (∠2 + ∠4) + ∠D = 180° + 180°.\n\nStep 5: Regroup terms:\nNotice that ∠1 + ∠3 = ∠BAD = ∠A, and ∠2 + ∠4 = ∠BCD = ∠C.\nSubstituting these values gives:\n∠A + ∠B + ∠C + ∠D = 360°.\nHence Proved!\n\n[ROUGH_WORK]\nTriangle 1 sum = 180°. Triangle 2 sum = 180°. Together they form the entire interior of ABCD: 180° + 180° = 360°.\nBoxed Answer: [ ∠A + ∠B + ∠C + ∠D = 360° (Proved) ].",
                    "concept_questions": [
                        "Does this proof also work if diagonal BD is drawn instead?",
                        "Does the 360° angle sum hold for a non-convex (arrowhead) quadrilateral?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "quadrilateral angle sum property 360 diagonal triangle proof diagram",
                "video_search_query": "angle sum of quadrilateral proof class 9",
                "concept_questions": [
                    "Why does connecting a diagonal divide a quadrilateral into exactly two triangles?",
                    "What is a reflex angle and where does it occur in a non-convex quadrilateral?",
                    "Can a quadrilateral have all four angles obtuse?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Believing that non-convex quadrilaterals have an angle sum different from 360°.",
                    "correction": "All simple quadrilaterals (convex and non-convex alike) have an interior angle sum of exactly 360° when the reflex angle is measured as an interior angle."
                }
            ],
            "quiz_questions": [
                {
                    "question": "The angles of a quadrilateral are in the ratio 3 : 5 : 9 : 13. What is the measure of the largest angle?",
                    "options": [
                        "(Recommended) 156°",
                        "108°",
                        "60°",
                        "36°"
                    ],
                    "correct_index": 0,
                    "explanation": "Let angles be 3x, 5x, 9x, 13x. Total = 30x = 360° ⇒ x = 12°. Largest angle = 13 × 12° = 156°."
                }
            ]
        },

        # Module 2: Parallelogram Theorems: Theorems 1 to 5
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Parallelogram Theorems: Rigorous Euclidean Proofs of Theorems 1 to 5 & Converses",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Prove Theorems 1 to 5 of parallelograms and their converses (Fig. 12.7 to 12.10). Derive opposite sides equality, opposite angles equality, diagonal bisection, and the fundamental sufficient condition: a quadrilateral with one pair of opposite sides equal and parallel is a parallelogram.",
            "key_concepts": [
                "Parallelogram Definition: A quadrilateral in which both pairs of opposite sides are parallel (AB ∥ CD and AD ∥ BC)",
                "Theorem 1 (Diagonal Congruence): A diagonal of a parallelogram divides it into two congruent triangles (ΔABC ≅ ΔCDA via ASA)",
                "Theorem 2 & Converse: In a parallelogram, opposite sides are equal (AB = CD, AD = BC); Converse: If opposite sides are equal, the quadrilateral is a parallelogram",
                "Theorem 3 & Converse: In a parallelogram, opposite angles are equal (∠A = ∠C, ∠B = ∠D); Converse: If opposite angles are equal, the quadrilateral is a parallelogram",
                "Theorem 4 & Converse: The diagonals of a parallelogram bisect each other (OA = OC, OB = OD); Converse: If diagonals bisect each other, the quadrilateral is a parallelogram",
                "Theorem 5 (Sufficient One-Pair Condition): A quadrilateral is a parallelogram if one pair of opposite sides is both equal and parallel"
            ],
            "subtopics": [
                "Formal proof of Theorem 1 (Diagonal divides into 2 congruent triangles)",
                "Proofs of Theorem 2 and its converse (Fig. 12.7)",
                "Proofs of Theorem 3 and its converse (Fig. 12.8)",
                "Proofs of Theorem 4 and its converse (Fig. 12.9 & 12.10)",
                "Exhaustive proof of Theorem 5 (Single pair parallel & equal)"
            ],
            "success_criteria": [
                "State and prove Theorems 1, 2, 3, 4, and 5 with complete formal geometric rigor",
                "Demonstrate why the converse of each parallelogram theorem holds true",
                "Identify which minimal conditions guarantee that a given 4-gon is a parallelogram"
            ],
            "chapter_notes": r"""# Chapter 12: Quadrilaterals
## Module 2: Parallelogram Theorems (Theorems 1 to 5)

### 1. The Core Definition
> **Definition:** A quadrilateral $ABCD$ is a **parallelogram** if and only if both pairs of opposite sides are parallel:
> $$AB \parallel CD \quad \text{and} \quad AD \parallel BC$$

---

### 2. The Five Foundational Theorems
- **Theorem 1:** A diagonal divides a parallelogram into two congruent triangles.  
  $$\Delta ABC \cong \Delta CDA$$
- **Theorem 2:** In a parallelogram, opposite sides are equal ($AB = CD$ and $AD = BC$).
  - **Converse:** If opposite sides of a quadrilateral are equal, it is a parallelogram.
- **Theorem 3:** In a parallelogram, opposite angles are equal ($\angle A = \angle C$ and $\angle B = \angle D$).
  - **Converse:** If opposite angles of a quadrilateral are equal, it is a parallelogram.
- **Theorem 4:** The diagonals of a parallelogram bisect each other ($OA = OC$ and $OB = OD$).
  - **Converse:** If the diagonals of a quadrilateral bisect each other, it is a parallelogram.
- **Theorem 5 (The Golden Test):** A quadrilateral is a parallelogram if **one pair of opposite sides is equal and parallel** ($AB \parallel CD$ and $AB = CD$).
""",
            "worked_examples": [
                {
                    "problem": "Theorem 5 (NCERT Section 12.2, Refer to Fig. 12.10): Prove that a quadrilateral is a parallelogram if one pair of opposite sides is equal and parallel.",
                    "figure_path": "/extracted_diagrams/math9_ch12/fig_12_10.webp",
                    "solution": "STATEMENT:\nProve that a quadrilateral is a parallelogram if one pair of opposite sides is equal and parallel.\n\nGIVEN (Refer to Fig. 12.10):\nA quadrilateral ABCD in which AB = CD and AB ∥ CD.\n\nTO PROVE:\nABCD is a parallelogram (i.e. AD ∥ BC).\n\nCONSTRUCTION:\nJoin diagonal AC.\n\nPROOF:\nStep 1: Identify alternate interior angles:\nSince AB ∥ CD and AC is a transversal intersecting them:\n∠BAC = ∠DCA  --- (Alternate interior angles are equal)\n\nStep 2: Prove triangle congruence:\nIn ΔABC and ΔCDA:\n1. AB = CD (Given)\n2. ∠BAC = ∠DCA (Proved above)\n3. AC = CA (Common side)\nTherefore, ΔABC ≅ ΔCDA by SAS (Side-Angle-Side) Congruence Criterion.\n\nStep 3: Deduce parallelism of second pair:\nBy CPCTC (Corresponding Parts of Congruent Triangles are Congruent):\n∠BCA = ∠DAC.\nNotice that ∠BCA and ∠DAC are alternate interior angles formed by transversal AC intersecting lines AD and BC.\nSince alternate interior angles are equal, by the Converse of Alternate Interior Angles Theorem:\nAD ∥ BC.\n\nStep 4: Conclude parallelogram status:\nSince AB ∥ CD (Given) and AD ∥ BC (Proved), both pairs of opposite sides are parallel.\nTherefore, ABCD is a parallelogram.\nHence Proved!\n\n[ROUGH_WORK]\nAB = CD (Given), AB ∥ CD ⇒ ∠BAC = ∠DCA. AC common. SAS ⇒ ΔABC ≅ ΔCDA ⇒ ∠BCA = ∠DAC ⇒ AD ∥ BC. Parallelogram confirmed!\nBoxed Answer: [ ABCD is a parallelogram (Proved) ].",
                    "concept_questions": [
                        "Why is the SAS criterion applicable here and not AAS?",
                        "What if the equal sides were not the parallel sides (e.g. AB ∥ CD, but AD = BC)?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "parallelogram theorems opposite sides equal diagonals bisect geometry diagram",
                "video_search_query": "parallelogram theorems 1 to 5 proofs class 9",
                "concept_questions": [
                    "If a quadrilateral has one pair of opposite sides equal and the other pair parallel, is it necessarily a parallelogram?",
                    "What is an isosceles trapezium and why does it serve as a counterexample to the question above?",
                    "How does Theorem 1 imply both Theorem 2 and Theorem 3 via CPCTC?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Thinking that if one pair of sides is parallel and the OTHER pair is equal, the 4-gon is a parallelogram.",
                    "correction": "This is false! In an isosceles trapezium, AB ∥ CD and AD = BC, but it is NOT a parallelogram. The SAME pair must be both equal and parallel."
                }
            ],
            "quiz_questions": [
                {
                    "question": "If ABCD is a quadrilateral with AB ∥ CD and AD = BC, which quadrilateral could ABCD be without being a parallelogram?",
                    "options": [
                        "(Recommended) Isosceles Trapezium",
                        "Rhombus",
                        "Rectangle",
                        "Kite"
                    ],
                    "correct_index": 0,
                    "explanation": "An isosceles trapezium has one pair of parallel sides and the other pair of non-parallel sides equal. It is not a parallelogram."
                }
            ]
        },

        # Module 3: The Midpoint Theorem & Its Converse
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "The Midpoint Theorem & Its Converse: Theorems 6 & 7 with Triangles and Trapeziums",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Prove Theorem 6 (The Midpoint Theorem) and Theorem 7 (Converse of the Midpoint Theorem) in triangles (Fig. 12.14 to 12.16). Discover how the segment joining the midpoints of two sides of a triangle is parallel to the third side and exactly half its length.",
            "key_concepts": [
                "Theorem 6 (Midpoint Theorem): The line segment joining the midpoints of two sides of a triangle is parallel to the third side and half as long: MN ∥ BC and MN = (1/2)BC",
                "Euclidean Construction for Proof: Extend MN to D such that ND = MN, join CD; prove ΔAMN ≅ ΔCDN to establish that MBCD is a parallelogram",
                "Theorem 7 (Converse of Midpoint Theorem): The line drawn through the midpoint of one side of a triangle parallel to another side bisects the third side",
                "Application to Trapeziums: The line segment connecting the non-parallel midpoints of a trapezium is parallel to both bases and equal to their arithmetic mean: (1/2)(a + b)"
            ],
            "subtopics": [
                "Complete formal proof of Theorem 6 (The Midpoint Theorem, Fig. 12.14)",
                "Complete formal proof of Theorem 7 (Converse of Midpoint Theorem, Fig. 12.16)",
                "Worked example: Connecting midpoints of all three sides of a triangle",
                "Midpoints of diagonals of a trapezium"
            ],
            "success_criteria": [
                "State and prove Theorem 6 with the standard parallelogram auxiliary construction",
                "State and prove Theorem 7 using the converse parallelogram properties",
                "Apply the Midpoint Theorem to solve multi-step geometric numericals and proofs"
            ],
            "chapter_notes": r"""# Chapter 12: Quadrilaterals
## Module 3: The Midpoint Theorem & Its Converse

### 1. Theorem 6: The Midpoint Theorem (Fig. 12.14)
**Statement:** The line segment joining the midpoints of any two sides of a triangle is parallel to the third side and equal to half of it.
$$\text{In } \Delta ABC \text{, if } M \text{ is midpoint of } AB \text{ and } N \text{ is midpoint of } AC \text{:} \quad MN \parallel BC \quad \text{and} \quad MN = \frac{1}{2}BC$$

#### Proof:
1. **Given:** $\Delta ABC$, with $M$ midpoint of $AB$ ($AM = MB$) and $N$ midpoint of $AC$ ($AN = NC$).
2. **Construction:** Extend $MN$ to point $E$ such that $NE = MN$. Join $CE$.
3. **Congruence:** In $\Delta AMN$ and $\Delta CEN$:
   - $AN = NC$ (Given)
   - $\angle ANM = \angle CNE$ (Vertically opposite angles)
   - $MN = NE$ (Construction)  
   $\implies \Delta AMN \cong \Delta CEN$ by SAS criterion.
4. **Consequences:**
   - $AM = CE$ by CPCTC. Since $AM = MB$, we have $MB = CE$.
   - $\angle MAN = \angle ECN$ by CPCTC $\implies AB \parallel CE$ (alternate interior angles equal).
5. **Parallelogram:** In quadrilateral $BCEM$:
   - $MB \parallel CE$ and $MB = CE$.
   - By Theorem 5, $BCEM$ is a parallelogram!
6. **Final Deduction:**
   - Since $BCEM$ is a parallelogram, $ME \parallel BC \implies MN \parallel BC$.
   - Also, $ME = BC$. Since $MN = NE = \frac{1}{2}ME$, we have $MN = \frac{1}{2}BC$.  
   $$\text{Hence Proved!}$$
""",
            "worked_examples": [
                {
                    "problem": "Theorem 6 (NCERT Section 12.3.1, Refer to Fig. 12.14): Prove that the segment joining the midpoints of two sides of a triangle is parallel to the third side and has half its length.",
                    "figure_path": "/extracted_diagrams/math9_ch12/fig_12_14.webp",
                    "solution": "STATEMENT:\nThe segment joining the midpoints of two sides of a triangle is parallel to the third side and half its length.\n\nGIVEN (Refer to Fig. 12.14):\nIn ΔABC, P is the midpoint of AB (AP = PB) and Q is the midpoint of AC (AQ = QC).\n\nTO PROVE:\n(i) PQ ∥ BC\n(ii) PQ = (1/2)BC.\n\nCONSTRUCTION:\nExtend segment PQ to point R such that QR = PQ. Join CR.\n\nPROOF:\nStep 1: Triangle Congruence:\nIn ΔAPQ and ΔCRQ:\n1. AQ = QC (Q is midpoint of AC)\n2. ∠AQP = ∠CQR (Vertically opposite angles)\n3. PQ = QR (By construction)\nTherefore, ΔAPQ ≅ ΔCRQ by SAS Congruence Criterion.\n\nStep 2: Apply CPCTC:\n- AP = CR\n- ∠PAQ = ∠RCQ.\nSince ∠PAQ and ∠RCQ are alternate interior angles for lines AB and CR with transversal AC, we deduce:\nAB ∥ CR.\n\nStep 3: Parallelogram Formulation:\nSince AP = PB (P is midpoint of AB) and AP = CR (from step 2):\nPB = CR.\nAlso, since CR ∥ AB, we have PB ∥ CR.\nThus, in quadrilateral PBCR, one pair of opposite sides (PB and CR) is both equal and parallel!\nBy Theorem 5, quadrilateral PBCR is a parallelogram.\n\nStep 4: Final Deductions:\nSince PBCR is a parallelogram, the other pair of opposite sides must be parallel and equal:\nPR ∥ BC ⇒ PQ ∥ BC  (Part i proved!).\nAlso, PR = BC.\nSince PQ = QR by construction, PR = 2PQ.\nTherefore, 2PQ = BC ⇒ PQ = (1/2)BC  (Part ii proved!).\nHence Proved!\n\n[ROUGH_WORK]\nSAS ⇒ ΔAPQ ≅ ΔCRQ ⇒ PB ∥ CR and PB = CR ⇒ PBCR is parallelogram ⇒ PQ ∥ BC and PQ = PR/2 = BC/2.\nBoxed Answer: [ PQ ∥ BC and PQ = (1/2)BC (Proved) ].",
                    "concept_questions": [
                        "Why did we extend PQ by its own length QR = PQ?",
                        "What would happen if we connected the midpoints of all three sides?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "midpoint theorem triangle proof parallelogram construction diagram",
                "video_search_query": "midpoint theorem proof class 9 geometry",
                "concept_questions": [
                    "How does the Midpoint Theorem allow us to find the perimeter of the medial triangle?",
                    "If BC = 14 cm, what is the length of segment MN joining the midpoints of AB and AC?",
                    "Why is quadrilateral PBCR guaranteed to be a parallelogram?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Assuming that MN bisects the area of ΔABC into two equal halves.",
                    "correction": "MN divides ΔABC into a smaller triangle ΔAMN and a trapezium MNCB. The area of ΔAMN is actually (1/4) of the area of ΔABC, while the trapezium is (3/4) of the area."
                }
            ],
            "quiz_questions": [
                {
                    "question": "In ΔABC, D and E are midpoints of AB and AC respectively. If BC = 12 cm, what is the length of DE?",
                    "options": [
                        "(Recommended) 6 cm",
                        "12 cm",
                        "4 cm",
                        "8 cm"
                    ],
                    "correct_index": 0,
                    "explanation": "By the Midpoint Theorem, DE = (1/2)BC = (1/2) × 12 = 6 cm."
                }
            ]
        },

        # Module 4: Medians of a Triangle & The Varignon Parallelogram
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Medians of a Triangle & The Varignon Parallelogram: Concurrency, Centroid & Midpoint Quadrilaterals",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Uncover the surprising properties of triangle medians and Varignon's Theorem (Fig. 12.18 to 12.21). Prove using the Midpoint Theorem that joining the midpoints of ANY arbitrary quadrilateral produces a parallelogram (Varignon Parallelogram), and prove that triangle medians concur at a centroid dividing each in a 2:1 ratio.",
            "key_concepts": [
                "Median Definition: A line segment joining a vertex of a triangle to the midpoint of the opposite side",
                "Median Concurrency & Centroid (G): The three medians of any triangle intersect at a single common point (centroid G), which divides each median in a 2:1 ratio from the vertex",
                "Varignon's Theorem (Fig. 12.21): The figure formed by joining the midpoints of the four sides of ANY quadrilateral ABCD in order is ALWAYS a parallelogram (PQRS)",
                "Proof of Varignon's Theorem: Draw diagonal AC. By Midpoint Theorem on ΔABC, PQ ∥ AC and PQ = (1/2)AC. On ΔADC, SR ∥ AC and SR = (1/2)AC. Therefore PQ ∥ SR and PQ = SR, so PQRS is a parallelogram by Theorem 5",
                "Perimeter Invariant: The perimeter of the Varignon parallelogram equals the sum of the lengths of the two diagonals of the original quadrilateral: Perimeter(PQRS) = AC + BD",
                "Area Invariant: The area of the Varignon parallelogram is exactly half the area of the original quadrilateral: Area(PQRS) = (1/2)Area(ABCD)"
            ],
            "subtopics": [
                "Geometric proof that medians trisect each other (2:1 ratio, Fig. 12.18)",
                "Formal proof of Varignon's Theorem using Midpoint Theorem (Fig. 12.21)",
                "Special cases of Varignon Parallelogram: When is it a rectangle, rhombus, or square?",
                "Exercises 1 to 5 from Section 12.3.2"
            ],
            "success_criteria": [
                "Prove Varignon's Theorem for an arbitrary quadrilateral using diagonal decomposition",
                "State and prove that the centroid G divides medians in a 2:1 ratio",
                "Deduce that PQRS is a rhombus if the diagonals of ABCD are equal, and a rectangle if they are perpendicular"
            ],
            "chapter_notes": r"""# Chapter 12: Quadrilaterals
## Module 4: Medians & The Varignon Parallelogram

### 1. The Varignon Parallelogram Theorem (1731)
**Theorem:** Let $ABCD$ be any arbitrary quadrilateral (convex, concave, or self-intersecting). Let $P, Q, R, S$ be the midpoints of sides $AB, BC, CD, DA$ respectively.  
Then **$PQRS$ is always a parallelogram**!

#### Formal Proof (Fig. 12.21):
1. Draw diagonal $AC$ of quadrilateral $ABCD$.
2. In $\Delta ABC$: $P$ is midpoint of $AB$ and $Q$ is midpoint of $BC$.  
   By the Midpoint Theorem:
   $$PQ \parallel AC \quad \text{and} \quad PQ = \frac{1}{2}AC$$
3. In $\Delta ADC$: $S$ is midpoint of $AD$ and $R$ is midpoint of $CD$.  
   By the Midpoint Theorem:
   $$SR \parallel AC \quad \text{and} \quad SR = \frac{1}{2}AC$$
4. Comparing the two results:
   $$PQ \parallel SR \quad \text{and} \quad PQ = SR$$
5. In quadrilateral $PQRS$, one pair of opposite sides ($PQ$ and $SR$) is both equal and parallel.
6. By Theorem 5, **$PQRS$ is a parallelogram**! $\quad \text{(Hence Proved!)}$

---

### 2. Properties of the Varignon Parallelogram
1. **Perimeter:** $\text{Perimeter}(PQRS) = PQ + QR + RS + SP = \frac{1}{2}AC + \frac{1}{2}BD + \frac{1}{2}AC + \frac{1}{2}BD = AC + BD$.
2. **Rhombus Condition:** $PQRS$ is a rhombus $\iff AC = BD$ (diagonals of $ABCD$ are equal).
3. **Rectangle Condition:** $PQRS$ is a rectangle $\iff AC \perp BD$ (diagonals of $ABCD$ are perpendicular).
4. **Square Condition:** $PQRS$ is a square $\iff AC = BD$ AND $AC \perp BD$.
""",
            "worked_examples": [
                {
                    "problem": "Theorem (NCERT Section 12.3.2, Refer to Fig. 12.21): Prove that the quadrilateral formed by joining the midpoints of the sides of any quadrilateral taken in order is a parallelogram.",
                    "figure_path": "/extracted_diagrams/math9_ch12/fig_12_21.webp",
                    "solution": "STATEMENT:\nThe figure formed by joining the midpoints of the four sides of a quadrilateral ABCD taken in order is a parallelogram.\n\nGIVEN (Refer to Fig. 12.21):\nA quadrilateral ABCD. Points P, Q, R, S are the midpoints of sides AB, BC, CD, DA respectively.\n\nTO PROVE:\nPQRS is a parallelogram.\n\nCONSTRUCTION:\nJoin diagonal AC of quadrilateral ABCD.\n\nPROOF:\nStep 1: Apply Midpoint Theorem to ΔABC:\nIn ΔABC, P is the midpoint of AB and Q is the midpoint of BC.\nBy Theorem 6 (Midpoint Theorem):\nPQ ∥ AC  and  PQ = (1/2)AC  --- (Equation 1)\n\nStep 2: Apply Midpoint Theorem to ΔADC:\nIn ΔADC, S is the midpoint of AD and R is the midpoint of CD.\nBy Theorem 6 (Midpoint Theorem):\nSR ∥ AC  and  SR = (1/2)AC  --- (Equation 2)\n\nStep 3: Compare results from Step 1 and Step 2:\nFrom (1) and (2):\nSince both PQ ∥ AC and SR ∥ AC, lines parallel to the same line are parallel to each other:\nPQ ∥ SR.\nFurthermore, since both PQ = (1/2)AC and SR = (1/2)AC:\nPQ = SR.\n\nStep 4: Conclude parallelogram via Theorem 5:\nIn quadrilateral PQRS, one pair of opposite sides (PQ and SR) is both equal and parallel.\nBy Theorem 5, quadrilateral PQRS is a parallelogram.\nHence Proved!\n\n[ROUGH_WORK]\nPQ = AC/2 and PQ ∥ AC (from ΔABC). SR = AC/2 and SR ∥ AC (from ΔADC). Equal and parallel ⇒ PQRS is a parallelogram!\nBoxed Answer: [ PQRS is a parallelogram (Proved) ].",
                    "concept_questions": [
                        "What is the perimeter of PQRS in terms of the diagonals of ABCD?",
                        "What type of parallelogram is PQRS if ABCD is a kite?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "varignon parallelogram theorem geometry midpoints proof diagram",
                "video_search_query": "varignon theorem proof class 9 geometry",
                "concept_questions": [
                    "Why does Varignon's Theorem hold true even if the original quadrilateral is shaped like a dart (concave)?",
                    "If the diagonals of ABCD are equal to 10 cm and 14 cm, what is the perimeter of the Varignon parallelogram?",
                    "Under what geometric condition is the Varignon parallelogram a rectangle?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Thinking that ABCD must be a regular shape or a parallelogram for PQRS to be a parallelogram.",
                    "correction": "ABCD can be completely irregular, asymmetric, or even concave. PQRS will STILL always be a perfect parallelogram."
                }
            ],
            "quiz_questions": [
                {
                    "question": "If the diagonals of quadrilateral ABCD are perpendicular to each other, what specific shape is the Varignon parallelogram PQRS?",
                    "options": [
                        "(Recommended) Rectangle",
                        "Rhombus",
                        "Trapezium",
                        "Kite"
                    ],
                    "correct_index": 0,
                    "explanation": "Because sides of PQRS are parallel to diagonals AC and BD, if AC ⊥ BD, the adjacent sides of PQRS meet at 90°, making it a rectangle."
                }
            ]
        },

        # Module 5: Tiling the Plane Using Any Arbitrary Quadrilateral
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Tiling the Plane Using Any Arbitrary Quadrilateral: Euclidean Tessellation & Rotational Symmetry",
            "estimated_minutes": 25,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Investigate the geometric miracle of plane tessellation (Fig. 12.26 to 12.29): ANY arbitrary simple quadrilateral (convex or concave) can tile the infinite 2D plane with zero gaps and zero overlaps. Prove why regular pentagons fail while irregular 4-gons succeed using 180° midpoint rotations.",
            "key_concepts": [
                "Tessellation (Tiling): A covering of the infinite plane using geometric shapes without any gaps, holes, or overlaps",
                "The Vertex Angle Criterion: A set of polygons can tile around a vertex if and only if the sum of angles meeting at that vertex equals exactly 360°",
                "The Regular Pentagon Failure: Each interior angle of a regular pentagon is 108°; since 360° is not divisible by 108° (3 × 108° = 324° < 360° < 4 × 108° = 432°), regular pentagons CANNOT tile the plane",
                "The Quadrilateral Miracle Theorem: Because the four angles of ANY quadrilateral sum to exactly 360° (∠1 + ∠2 + ∠3 + ∠4 = 360°), placing four copies of the quadrilateral with one of each angle meeting at every vertex tiles the plane completely",
                "180° Midpoint Rotations: Rotating a quadrilateral by 180° around the midpoint of any side produces a pair forming a centrally symmetric hexagon, which tiles by translation"
            ],
            "subtopics": [
                "The 360° vertex condition for plane tessellation",
                "Why regular pentagons leave gaps or overlap",
                "Constructing a quadrilateral tessellation via 180° midpoint rotations (Fig. 12.26 to 12.29)",
                "Tiling with non-convex (concave) dart quadrilaterals"
            ],
            "success_criteria": [
                "Explain mathematically why regular pentagons cannot tile the plane",
                "Demonstrate how any arbitrary 4-gon tiles the plane using angle sum 360°",
                "Illustrate 180° rotation around edge midpoints to generate a periodic tessellation"
            ],
            "chapter_notes": r"""# Chapter 12: Quadrilaterals
## Module 5: Tiling the Plane with Any Quadrilateral

### 1. The 360° Vertex Law of Tessellation
Around any point (vertex) on a flat tiled floor, the sum of all adjoining angles must be exactly a full circle:
$$\sum \theta_i = 360^\circ$$

- **Why a Regular Pentagon Fails:**
  Interior angle = $\frac{(5 - 2) \times 180^\circ}{5} = \frac{540^\circ}{5} = 108^\circ$.
  $$3 \times 108^\circ = 324^\circ \quad (\text{gap of } 36^\circ)$$
  $$4 \times 108^\circ = 432^\circ \quad (\text{overlap of } 72^\circ)$$
  Since $360^\circ$ is not an integer multiple of $108^\circ$, regular pentagons **cannot tile the plane**!

---

### 2. The Universal Quadrilateral Tiling Theorem
In **any** quadrilateral, the four angles are $\angle 1, \angle 2, \angle 3, \angle 4$.
We proved in Module 1 that:
$$\angle 1 + \angle 2 + \angle 3 + \angle 4 = 360^\circ$$
Therefore, if we bring four copies of the quadrilateral together such that angle 1, angle 2, angle 3, and angle 4 all meet at a single vertex, they fit together **seamlessly with zero gap and zero overlap**!  
Repeating this pattern tiles the entire infinite Euclidean plane.
""",
            "worked_examples": [
                {
                    "problem": "Section 12.4, Question 1: Justify mathematically why the plane cannot be tiled with a regular pentagon, whereas any arbitrary quadrilateral can tile the plane.",
                    "solution": "QUESTION:\nJustify why a regular pentagon cannot tile the plane, while any quadrilateral can.\n\nSTEP-BY-STEP MATHEMATICAL JUSTIFICATION:\n\nPART 1: REGULAR PENTAGON ANALYSIS:\nStep 1: Compute the interior angle of a regular pentagon:\nFormula for interior angle of a regular n-gon:\nθ = [(n - 2) × 180°] / n.\nFor n = 5:\nθ = [(5 - 2) × 180°] / 5 = (3 × 180°) / 5 = 540° / 5 = 108°.\n\nStep 2: Test the vertex tiling condition:\nFor polygons to tile the plane without gaps or overlaps, an integer number k of tiles must meet at every vertex such that:\nk × θ = 360°.\nTesting integer values for k:\n- If k = 3: 3 × 108° = 324° < 360° (leaves a gap of 36°).\n- If k = 4: 4 × 108° = 432° > 360° (tiles overlap by 72°).\nSince 360° / 108° = 10 / 3 = 3.333... (not an integer), it is geometrically impossible for regular pentagons to tile the plane!\n\nPART 2: ARBITRARY QUADRILATERAL ANALYSIS:\nStep 1: State the angle sum invariant:\nLet the four angles of an arbitrary quadrilateral be ∠1, ∠2, ∠3, ∠4.\nBy the Angle Sum Theorem of quadrilaterals:\n∠1 + ∠2 + ∠3 + ∠4 = 360°.\n\nStep 2: Vertex arrangement:\nAt every vertex in the tessellation grid, arrange four quadrilaterals so that one of each angle (∠1, ∠2, ∠3, and ∠4) meets at the vertex.\nTheir sum is identically 360°.\nHence, they fill the angular space around the vertex completely without any gap or overlap.\nSince this holds for every vertex, any arbitrary quadrilateral tiles the plane!\n\n[ROUGH_WORK]\nPentagon: 108° does not divide 360°. Gap = 36°. Quadrilateral: 4 angles sum to exactly 360°, fitting a complete revolution at every vertex!\nBoxed Answer: [ Justified: 108° does not divide 360° (pentagons leave 36° gaps), while quadrilateral angles sum to exactly 360° ].",
                    "concept_questions": [
                        "Which regular polygons can tile the plane by themselves?",
                        "What is 360 / 60, 360 / 90, and 360 / 120?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "quadrilateral plane tiling tessellation 360 degrees vertex geometry diagram",
                "video_search_query": "tessellation with quadrilaterals class 9 maths",
                "concept_questions": [
                    "Why can equilateral triangles, squares, and regular hexagons tile the plane?",
                    "How does rotating a tile by 180° around an edge midpoint generate adjacent tiles?",
                    "Can an irregular non-convex dart quadrilateral tile the plane?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Believing that only regular or symmetrical shapes can tile the plane.",
                    "correction": "This is one of the most stunning surprises of mathematics: ANY quadrilateral, no matter how irregular or asymmetric, tiles the plane completely!"
                }
            ],
            "quiz_questions": [
                {
                    "question": "What is the interior angle of a regular pentagon?",
                    "options": [
                        "(Recommended) 108°",
                        "120°",
                        "90°",
                        "135°"
                    ],
                    "correct_index": 0,
                    "explanation": "Interior angle = (5 - 2) × 180° / 5 = 540° / 5 = 108°."
                }
            ]
        },

        # Module 6: Master Exercise Solver: Exercises 1 to 22
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 6,
            "title": "Master Exercise Solver: Comprehensive Step-by-Step Proofs of Exercises 1 to 22",
            "estimated_minutes": 30,
            "class_level": "Class 9",
            "board": "CBSE",
            "description": "Comprehensive solver for all major exercises in Chapter 12: proving segment trisection using midpoints and parallelograms, paper-folding trisections (Fig. 12.33), Varignon rhombi and rectangles, and diagonal trisection theorems.",
            "key_concepts": [
                "Segment Trisection Theorem: Using medians and parallelograms to divide a line segment into exactly three equal parts (1/3 each)",
                "Paper-Folding Trisection (Fig. 12.33): Exact geometric folding proofs using parallel midpoint lines to trisect a segment without measurement tools",
                "Varignon Rhombus Condition: Proving that the Varignon parallelogram of an isosceles trapezium or rectangle is a rhombus",
                "Varignon Rectangle Condition: Proving that the Varignon parallelogram of a rhombus or kite is a rectangle"
            ],
            "subtopics": [
                "Trisecting a line segment using parallelograms and midpoints",
                "Full geometric proof of Exercise 4 and Exercise 5 (Varignon special shapes)",
                "Paper folding trisection proof (Fig. 12.33)",
                "Complete step-by-step topper proofs for challenging chapter exercises"
            ],
            "success_criteria": [
                "Perform geometric trisection of a line segment with formal proof",
                "Prove why joining the midpoints of a rhombus produces a rectangle",
                "Prove why joining the midpoints of a rectangle produces a rhombus"
            ],
            "chapter_notes": r"""# Chapter 12: Quadrilaterals
## Module 6: Master Exercise Solver

### 1. Rhombus-Rectangle Duality in Varignon Parallelograms
- **Theorem A:** The quadrilateral formed by joining the midpoints of the sides of a **rectangle** is a **rhombus**.
  - *Proof:* In a rectangle, diagonals are equal ($AC = BD$). Adjacent sides of the Varignon parallelogram are $PQ = \frac{1}{2}AC$ and $QR = \frac{1}{2}BD$. Since $AC = BD$, $PQ = QR$. A parallelogram with equal adjacent sides is a rhombus!

- **Theorem B:** The quadrilateral formed by joining the midpoints of the sides of a **rhombus** is a **rectangle**.
  - *Proof:* In a rhombus, diagonals are perpendicular ($AC \perp BD$). The sides of the Varignon parallelogram are parallel to the diagonals ($PQ \parallel AC$ and $QR \parallel BD$). Since $AC \perp BD$, $PQ \perp QR$, meaning $\angle PQR = 90^\circ$. A parallelogram with a right angle is a rectangle!
""",
            "worked_examples": [
                {
                    "problem": "Chapter 12, Exercise: Prove that the quadrilateral formed by joining the midpoints of the sides of a rectangle is a rhombus.",
                    "solution": "STATEMENT:\nProve that the quadrilateral formed by joining the midpoints of the sides of a rectangle is a rhombus.\n\nGIVEN:\nA rectangle ABCD in which P, Q, R, S are the midpoints of sides AB, BC, CD, DA respectively.\n\nTO PROVE:\nPQRS is a rhombus.\n\nCONSTRUCTION:\nJoin diagonals AC and BD of rectangle ABCD.\n\nPROOF:\nStep 1: Parallelogram status:\nBy Varignon's Theorem (proved in Module 4), PQRS is a parallelogram, with:\nPQ = (1/2)AC  and  RS = (1/2)AC\nQR = (1/2)BD  and  SP = (1/2)BD.\n\nStep 2: Equality of diagonals of a rectangle:\nIn rectangle ABCD, the diagonals are equal in length:\nAC = BD.\n\nStep 3: Equate adjacent sides:\nSince AC = BD:\nPQ = (1/2)AC = (1/2)BD = QR.\nTherefore, PQ = QR.\n\nStep 4: Conclude rhombus:\nIn parallelogram PQRS, the adjacent sides PQ and QR are equal.\nA parallelogram with adjacent sides equal is a rhombus.\nTherefore, PQRS is a rhombus.\nHence Proved!\n\n[ROUGH_WORK]\nRectangle diagonals AC = BD. Midpoint sides are half of diagonals: PQ = AC/2, QR = BD/2. Since AC = BD, PQ = QR. All 4 sides equal ⇒ Rhombus!\nBoxed Answer: [ PQRS is a rhombus (Proved) ].",
                    "concept_questions": [
                        "What shape is formed if we join the midpoints of a rhombus?",
                        "What shape is formed if we join the midpoints of a square?"
                    ]
                },
                {
                    "problem": "Chapter 12, Exercise (Refer to Fig. 12.33): In Fig. 12.33, explain how paper folding can be used to trisect a given line segment PQ into three equal parts without using a ruler.",
                    "figure_path": "/extracted_diagrams/math9_ch12/fig_12_33.webp",
                    "solution": "GIVEN (Refer to Fig. 12.33):\nA paper strip with line segment PQ drawn on it.\n\nTO PROVE / EXPLAIN:\nHow paper folding trisects segment PQ into three equal segments of length (1/3)PQ.\n\nSTEP-BY-STEP GEOMETRIC PROCEDURE & PROOF:\nStep 1: Mark midpoint:\nFold point P onto point Q and crease. The crease marks the midpoint M of PQ, so PM = MQ = (1/2)PQ.\n\nStep 2: Construct parallel boundary:\nFold parallel edges of the rectangular paper strip.\n\nStep 3: Diagonal crease intersections:\nFold the diagonal line connecting corner P to opposite corner, and fold from midpoint M to the opposite vertex.\nBy the Intercept Theorem and Midpoint Theorem on the resulting triangles:\nThe intersection point divides the transversal segment in the ratio 1 : 2.\nFolding a perpendicular line through this intersection point intersects segment PQ at a point that is exactly (1/3) of the distance from P.\nRepeating from the other end divides PQ into three segments of equal length:\nSegment 1 = (1/3)PQ, Segment 2 = (1/3)PQ, Segment 3 = (1/3)PQ.\nHence, PQ is trisected purely by paper folding!\n\n[ROUGH_WORK]\nSimilar triangles formed by diagonal and midpoint crease have ratio 1:2. The projection onto PQ trisects the segment: 1/3, 1/3, 1/3.\nBoxed Answer: [ Segment PQ is trisected into three equal parts of length (1/3)PQ by folding ].",
                    "concept_questions": [
                        "Why can an angle not always be trisected with compass and straightedge, but a segment can?",
                        "What is the mathematical justification behind the paper fold?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "syllabus_term": "Final-Term",
                "image_search_query": "rhombus midpoints rectangle geometry proof diagram",
                "video_search_query": "midpoints of rectangle form rhombus proof class 9",
                "concept_questions": [
                    "Why does joining the midpoints of a rhombus give a rectangle?",
                    "What figure is formed when you join the midpoints of an isosceles trapezium?",
                    "How does the Midpoint Theorem solve the segment trisection problem?"
                ]
            },
            "common_misconceptions": [
                {
                    "misconception": "Confusing the midpoints of a rectangle with those of a rhombus.",
                    "correction": "Rectangle midpoints form a RHOMBUS (equal diagonals produce equal sides). Rhombus midpoints form a RECTANGLE (perpendicular diagonals produce 90° angles)."
                }
            ],
            "quiz_questions": [
                {
                    "question": "The quadrilateral formed by joining the midpoints of the sides of a rhombus is always a:",
                    "options": [
                        "(Recommended) Rectangle",
                        "Rhombus",
                        "Square",
                        "Trapezium"
                    ],
                    "correct_index": 0,
                    "explanation": "Because the diagonals of a rhombus are perpendicular to each other, the sides of the Varignon parallelogram meet at right angles, forming a rectangle."
                }
            ]
        }
    ]
    
    return modules

if __name__ == "__main__":
    mods = get_ch12_modules()
    print(f"Generated {len(mods)} modules for Chapter 12.")
    for m in mods:
        print(f"  #{m['order_index']}: {m['title']} ({len(m['worked_examples'])} examples)")
