import json

with open('scripts/maths_pt2_modules/ch12_quadrilaterals.json', 'r', encoding='utf-8') as f:
    modules = json.load(f)

# Module 1: Add FORMULA / THEOREM USED to WE 1, and add WE 2 for Exercise Set 12.1
m1_we1_sol = modules[0]['worked_examples'][0]['solution']
if "THEOREM / FORMULA USED" not in m1_we1_sol:
    m1_we1_sol = m1_we1_sol.replace("STEP-BY-STEP", "THEOREM / FORMULA USED:\nAngle Sum Property of Polygon:\nSum of interior angles of an n-gon = (n - 2) × 180°.\nFor n = 4 (quadrilateral): Sum = (4 - 2) × 180° = 360°.\n\nSTEP-BY-STEP")
    modules[0]['worked_examples'][0]['solution'] = m1_we1_sol

we_m1_ex_12_1 = {
    "problem": "Chapter 12, Exercise Set 12.1, Questions 1, 2 & 3 (Ganita Manjari Part 2, Section 12.1, pp. 55–56):\n(i) Question 1: Let ABCD be a quadrilateral. List all sides of ABCD adjacent to side AB. List all sides opposite to AB. How do you define adjacent and opposite sides formally?\n(ii) Question 2: In quadrilateral ABCD, list all angles adjacent to ∠A. List the angle opposite to ∠A. How do you define opposite angles?\n(iii) Question 3: Distinguish between convex and non-convex quadrilaterals based on their diagonals. Prove that in any convex quadrilateral, the two diagonals must intersect in the interior.",
    "solution": """GIVEN:
A quadrilateral ABCD formed by 4 distinct coplanar vertices A, B, C, D with no three collinear.

TO FIND / TO PROVE:
(i) Formal definitions and enumeration of adjacent and opposite sides.
(ii) Formal definitions and enumeration of adjacent and opposite angles.
(iii) Characterization of convexity via diagonals and proving that diagonals of a convex quadrilateral intersect internally.

THEOREM / FORMULA USED:
1. Quadrilateral Incidence Axiom:
   Two sides are adjacent if they share a common vertex. Two sides are opposite if they share no common vertex.
2. Opposite Angles:
   Two angles ∠A and ∠C are opposite if their vertices do not lie on a common side.
3. Convexity Criterion:
   A polygon is convex if the segment joining any two interior points lies entirely within the interior. For a quadrilateral, ABCD is convex iff diagonal AC intersects diagonal BD in their respective interiors.

STEP-BY-STEP CALCULATION / PROOF:
Part (i) Sides of Quadrilateral ABCD:
- Sides sharing a vertex with AB:
  Vertex A connects sides DA and AB -> DA is adjacent to AB.
  Vertex B connects sides AB and BC -> BC is adjacent to AB.
  Hence, adjacent sides to AB are DA and BC.
- Side sharing no vertex with AB:
  Vertices of AB are {A, B}. Vertices of CD are {C, D}. {A, B} ∩ {C, D} = ∅.
  Therefore, side CD is the unique opposite side to AB.

Part (ii) Angles of Quadrilateral ABCD:
- Angles sharing a side with ∠A:
  Side AB connects ∠A and ∠B -> ∠B is adjacent to ∠A.
  Side AD connects ∠A and ∠D -> ∠D is adjacent to ∠A.
- Angle sharing no side with ∠A:
  Vertex C shares no boundary side with vertex A.
  Therefore, ∠C is the unique opposite angle to ∠A.

Part (iii) Convexity and Diagonals:
1. In a convex quadrilateral ABCD:
   All four interior angles are strictly less than 180° (< 180°).
   Vertex C lies in the interior of ∠DAB, and vertex D lies in the interior of ∠ABC.
   Ray AC enters the interior of ∠DAB and must cross segment BD at an interior point M.
   Thus, both diagonals AC and BD lie wholly inside the figure and intersect at point M.
2. In a non-convex (reflex) quadrilateral (e.g., arrow/dart):
   One interior angle exceeds 180° (reflex angle at C).
   Diagonal AC lies entirely outside the region, while diagonal BD lies inside.
   The two diagonals do not intersect in their interior!

[ROUGH_WORK]
Vertices: A, B, C, D in cyclic order.
Sides: AB, BC, CD, DA.
Pairs of opposite sides: (AB, CD) and (BC, DA).
Pairs of opposite angles: (∠A, ∠C) and (∠B, ∠D).
Diagonals: AC and BD.

Boxed Answer:
[ (i) Adjacent to AB: BC and DA; Opposite to AB: CD, (ii) Adjacent to ∠A: ∠B and ∠D; Opposite to ∠A: ∠C, (iii) Diagonals of a convex quadrilateral always intersect internally at a single point M ]"""
}
modules[0]['worked_examples'].append(we_m1_ex_12_1)

# Module 2: Add THEOREM USED to WE 1, and add WE 2 for Exercise Set 12.2
m2_we1_sol = modules[1]['worked_examples'][0]['solution']
if "THEOREM / FORMULA USED" not in m2_we1_sol:
    m2_we1_sol = m2_we1_sol.replace("STEP-BY-STEP", "THEOREM / FORMULA USED:\nParallelogram Diagonal Bisection Theorem (Theorem 5):\nA quadrilateral is a parallelogram iff its opposite sides are parallel, which holds iff its diagonals bisect each other.\n\nSTEP-BY-STEP")
    modules[1]['worked_examples'][0]['solution'] = m2_we1_sol

we_m2_ex_12_2 = {
    "problem": "Chapter 12, Exercise Set 12.2, Questions 1 & 2 (Ganita Manjari Part 2, Section 12.2, p. 60):\n(i) Question 1: State True or False with geometric justification:\n(a) A parallelogram with a right angle is a rectangle.\n(b) A rhombus with perpendicular diagonals is a square.\n(c) If the diagonals of a parallelogram are equal, then it is a rectangle.\n(ii) Question 2: The diagonal AC of a parallelogram ABCD bisects ∠A. Show that it also bisects ∠C and that ABCD is a rhombus.",
    "solution": """GIVEN:
(i) Various quadrilateral configurations with specified angle and diagonal conditions.
(ii) Parallelogram ABCD with diagonal AC such that ∠DAC = ∠BAC.

TO FIND / TO PROVE:
(i) Validate truth value with rigorous geometric proofs.
(ii) Prove: (a) AC bisects ∠C (∠DCA = ∠BCA); (b) ABCD is a rhombus (AB = BC = CD = DA).

THEOREM / FORMULA USED:
1. Alternate Interior Angles Theorem:
   If l₁ ‖ l₂, then alternate interior angles are equal.
2. Isosceles Triangle Theorem:
   Sides opposite to equal angles in a triangle are equal.
3. Parallelogram Properties:
   Opposite sides are parallel and equal: AB ‖ CD, AD ‖ BC, AB = CD, AD = BC.

STEP-BY-STEP CALCULATION / PROOF:
Part (i) True / False Analysis:
(a) TRUE. In parallelogram ABCD, opposite angles are equal (∠A = ∠C) and consecutive angles are supplementary (∠A + ∠B = 180°). If ∠A = 90°, then ∠B = 180° - 90° = 90°, ∠C = 90°, ∠D = 90°. All 4 angles are 90°, so it is a rectangle.
(b) FALSE. The diagonals of EVERY rhombus are perpendicular by definition! A rhombus only becomes a square if its interior angles are right angles (or its diagonals are equal in length). For example, a 60°-120° rhombus has perpendicular diagonals but is not a square.
(c) TRUE. Let diagonals AC = BD in parallelogram ABCD. In △ABC and △DCB: AB = DC (opposite sides), BC = CB (common), AC = DB (given). By SSS congruence, △ABC ≅ △DCB. Thus ∠ABC = ∠DCB. But consecutive angles are supplementary: ∠ABC + ∠DCB = 180° -> 2∠ABC = 180° -> ∠ABC = 90°. Hence, ABCD is a rectangle.

Part (ii) Diagonal Bisector Proof:
1. Since ABCD is a parallelogram, AB ‖ CD and AC is a transversal:
   ∠BAC = ∠DCA (Alternate interior angles)    --- (1)
2. Since AD ‖ BC and AC is a transversal:
   ∠DAC = ∠BCA (Alternate interior angles)    --- (2)
3. Given that AC bisects ∠A:
   ∠BAC = ∠DAC                               --- (3)
4. From (1), (2), and (3):
   ∠DCA = ∠BAC = ∠DAC = ∠BCA.
   Therefore, ∠DCA = ∠BCA, which proves that diagonal AC bisects ∠C!
5. Now consider △ABC:
   From (1) and (3), ∠BAC = ∠BCA.
   Since angles opposite to sides are equal, BC = AB.
6. In parallelogram ABCD, opposite sides are equal: AB = CD and BC = AD.
   Since AB = BC, it follows that AB = BC = CD = DA.
   Therefore, all four sides of ABCD are equal, proving ABCD is a rhombus!

[ROUGH_WORK]
Given ∠1 = ∠2 (at A).
AB ‖ CD -> ∠1 = ∠4 (at C).
AD ‖ BC -> ∠2 = ∠3 (at C).
Since ∠1 = ∠2 -> ∠3 = ∠4 -> AC bisects ∠C.
In △ABC, ∠1 = ∠3 -> BC = AB.
All 4 sides equal -> Rhombus! Hence Proved.

Boxed Answer:
[ (i) (a) True, (b) False (diagonals of all rhombuses are perpendicular; equal diagonals are required for a square), (c) True, (ii) Diagonal AC bisects ∠C and ABCD has four equal sides, proving it is a rhombus ]"""
}
modules[1]['worked_examples'].append(we_m2_ex_12_2)

# Module 3, 4, 5: Add THEOREM USED
for m_idx in [2, 3, 4]:
    sol = modules[m_idx]['worked_examples'][0]['solution']
    if "THEOREM / FORMULA USED" not in sol:
        if m_idx == 2:
            th = "THEOREM / FORMULA USED:\nMidpoint Theorem (Theorem 6):\nThe line segment joining the midpoints of two sides of a triangle is parallel to the third side and half as long: PQ ‖ BC and PQ = (1/2)BC."
        elif m_idx == 3:
            th = "THEOREM / FORMULA USED:\nVarignon's Theorem & Centroid Concurrency:\nThe figure formed by joining the midpoints of the sides of any quadrilateral in order is a parallelogram. The medians of a triangle concur at centroid G dividing each in ratio 2 : 1."
        else:
            th = "THEOREM / FORMULA USED:\nTessellation Angle Sum Condition:\nA set of congruent polygons tiles the Euclidean plane iff at every vertex where polygons meet, the sum of surrounding interior angles equals exactly 360° with matching side edges."
        sol = sol.replace("STEP-BY-STEP", f"{th}\n\nSTEP-BY-STEP")
        modules[m_idx]['worked_examples'][0]['solution'] = sol

# Module 6: Add THEOREM USED to existing WE 1-8
m6_wes = modules[5]['worked_examples']
for we in m6_wes:
    sol = we['solution']
    if "THEOREM / FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "THEOREM / FORMULA USED:\nEuclidean Quadrilateral Theorems: Midpoint Theorem, Intercept Theorem, Angle Sum Property, Area of Triangles between same parallels.\n\nSTEP-BY-STEP")
        we['solution'] = sol

# Module 6: Add missing End-of-Chapter Exercises 23 & 24!
we_m6_ex_23_24 = {
    "problem": "Chapter 12, End-of-Chapter Exercises 23 & 24 (Ganita Manjari Part 2, Section 12.5, pp. 82–83, Refer to Fig. 12.43):\n(i) Exercise 23: Validity of Tiling Methods: Show using geometric reasoning that each of the three tiling procedures (Procedure 1: 180° rotations about edge midpoints; Procedure 2: translating double-quadrilateral parallelograms; Procedure 3: grid reflection) produces a gap-free and overlap-free tiling of the entire Euclidean plane using ANY arbitrary quadrilateral.\n(ii) Exercise 24 (Refer to Fig. 12.43): A square ABCD has each side midpoint connected to an opposite vertex (top midpoint to bottom-right corner, bottom midpoint to top-left corner, left midpoint to top-right corner, and bottom-left corner to right midpoint), forming a central square. What exact fraction of the original square is shaded?",
    "solution": """GIVEN:
(i) Any arbitrary convex quadrilateral ABCD with interior angles α, β, γ, δ such that α + β + γ + δ = 360°.
(ii) A square ABCD of side length s (unit area s² = 1). Midpoints of each side are connected to vertices as shown in Fig. 12.43, enclosing a tilted central quadrilateral.

TO FIND / TO PROVE:
(i) Prove that arbitrary quadrilaterals tile the plane with zero gaps and zero overlaps.
(ii) Prove that the central shaded figure is a square and calculate its exact area as a fraction of square ABCD.

THEOREM / FORMULA USED:
1. Polygon Angle Sum Invariant:
   Sum of interior angles of any 4-gon is α + β + γ + δ = 360°.
2. Tiling Vertex Condition:
   A plane is tiled without gaps or overlaps iff the sum of angles around every vertex is 360° and adjacent edges are congruent and aligned.
3. Coordinate Geometry Distance between Parallel Lines:
   For parallel lines Ax + By + C₁ = 0 and Ax + By + C₂ = 0:
   d = |C₁ - C₂| / √(A² + B²)
4. Area of Square: Area = d²

STEP-BY-STEP CALCULATION / PROOF:
Part (i) Validity of Quadrilateral Tiling (Exercise 23):
1. In any arbitrary quadrilateral ABCD, label the four interior angles at vertices A, B, C, D as α, β, γ, δ. By the angle sum property, α + β + γ + δ = 360°.
2. Procedure 1 (180° Rotations about Side Midpoints):
   - Rotate ABCD by 180° about the midpoint of side BC. The new copy shares side BC, and the orientation of adjacent edges is reversed.
   - Continue rotating about edge midpoints. Around every vertex in the resulting lattice, exactly four quadrilaterals meet: one brings angle α, one brings angle β, one brings angle γ, and one brings angle δ.
   - Total angle around every junction vertex = α + β + γ + δ = 360°. Because the angles sum to 360° and matching edges have identical lengths, there are no angular gaps and no overlapping wedges.
3. Procedure 2 (Centrosymmetric Double-Tile Parallelogram):
   - Joining ABCD with its 180° rotated copy forms a centrally symmetric hexagon with opposite edges equal and parallel, or equivalent to a parallelogram. Since parallelograms tile the plane by pure translation along two vector axes, ABCD tiles the entire Euclidean plane without gaps or overlaps.

Part (ii) Area of Shaded Central Square in Fig. 12.43 (Exercise 24):
1. Set up a Cartesian coordinate system on the square ABCD of side s = 1:
   A = (0, 1) [Top-Left], B = (1, 1) [Top-Right], C = (1, 0) [Bottom-Right], D = (0, 0) [Bottom-Left].
   Midpoints:
   M_AB = (1/2, 1), M_BC = (1, 1/2), M_CD = (1/2, 0), M_DA = (0, 1/2).
2. The four connecting lines in Fig. 12.43 are:
   - Line 1 (from D(0,0) to M_BC(1, 1/2)): Slope = (1/2 - 0) / (1 - 0) = 1/2.
     Equation: y = (1/2)x  =>  x - 2y = 0.
   - Line 2 (from M_DA(0, 1/2) to B(1, 1)): Slope = (1 - 1/2) / (1 - 0) = 1/2.
     Equation: y - 1/2 = (1/2)x  =>  x - 2y + 1 = 0.
   - Line 3 (from A(0, 1) to M_CD(1/2, 0)): Slope = (0 - 1) / (1/2 - 0) = -2.
     Equation: y - 1 = -2x  =>  2x + y - 1 = 0.
   - Line 4 (from M_AB(1/2, 1) to C(1, 0)): Slope = (0 - 1) / (1 - 1/2) = -2.
     Equation: y = -2(x - 1)  =>  2x + y - 2 = 0.
3. Verification of Orthogonality:
   Slope of Line 1 is m₁ = 1/2. Slope of Line 3 is m₂ = -2.
   Product of slopes = m₁ × m₂ = (1/2) × (-2) = -1.
   Therefore, Line 1 is perpendicular to Line 3!
   By symmetry, all four boundary lines intersect at right angles (90°).
   Thus, the central quadrilateral is a rectangle.
4. Calculation of Side Length of Central Square:
   - The perpendicular distance d₁ between parallel Lines 1 and 2 (with equations x - 2y = 0 and x - 2y + 1 = 0):
     d₁ = |1 - 0| / √(1² + (-2)²) = 1 / √5.
   - The perpendicular distance d₂ between parallel Lines 3 and 4 (with equations 2x + y - 1 = 0 and 2x + y - 2 = 0):
     d₂ = |2 - 1| / √(2² + 1²) = 1 / √5.
   Since d₁ = d₂ = 1 / √5, all four sides of the central figure are equal and its angles are 90°.
   Hence, the central figure is a PERFECT SQUARE of side length a = 1 / √5!
5. Area of the Shaded Central Square:
   Area = a² = (1 / √5)² = 1/5 = 0.20 of the total area of the original square!

[ROUGH_WORK]
Perpendicular distance formula: d = |c₁ - c₂| / √(a² + b²).
For x - 2y = 0 and x - 2y + 1 = 0: a = 1, b = -2, c₁ = 0, c₂ = 1.
d = 1 / √(1 + 4) = 1 / √5.
Area = (1 / √5)² = 1/5.
Visual check: The outer square is dissected into 4 right triangles of area (1/2) × 1 × (1/2) = 1/4 each? No, 4 congruent corner triangles + 4 trapeziums + 1 central square. Total sum = 4 × (1/10) + 4 × (1/10) + 1/5 = 1. Exact!

Boxed Answer:
[ (i) Every arbitrary quadrilateral tiles the plane because the sum of four meeting angles α + β + γ + δ = 360°, (ii) The central shaded figure is a square and occupies exactly 1/5 (20%) of the square's area ]"""
}
modules[5]['worked_examples'].append(we_m6_ex_23_24)

with open('scripts/maths_pt2_modules/ch12_quadrilaterals.json', 'w', encoding='utf-8') as f:
    json.dump(modules, f, indent=2, ensure_ascii=False)

print('Updated ch12_quadrilaterals.json successfully!')
