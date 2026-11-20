import json

with open('scripts/maths_pt2_modules/ch13_linear_equations.json', 'r', encoding='utf-8') as f:
    modules = json.load(f)

# Module 1: Add FORMULA USED to existing WE 1, 2 and add WE 3 for Exercise Set 13.1
for we in modules[0]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nStandard Linear Form in Two Variables:\nax + by + c = 0, where a, b, c ∈ ℝ and (a, b) ≠ (0, 0).\n\nSTEP-BY-STEP")
        we['solution'] = sol

we_m1_ex_13_1 = {
    "problem": "Chapter 13, Exercise Set 13.1, Questions 1, 2 & 3 (Ganita Manjari Part 2, Section 13.1, p. 87):\n(i) Question 1: Write a linear equation in two variables in which a = 3, b = 0, and c = -1/5.\n(ii) Question 2: Express each of the following equations in the standard form ax + by + c = 0 and identify the coefficients a, b, and c:\n(a) y - 15 = 2x, (b) 3y - 2x = 0, (c) 5x = 3y, (d) x = 8, (e) 3y = 1.\n(iii) Question 3: The cost of a notebook is twice the cost of a pen. Write a linear equation in two variables to represent this statement.",
    "solution": """GIVEN:
(i) Coefficients: a = 3, b = 0, c = -1/5.
(ii) Equations to convert to standard form ax + by + c = 0.
(iii) Statement: Cost of notebook = 2 × (Cost of pen).

TO FIND / TO PROVE:
(i) Standard equation for given coefficients.
(ii) Standard form and coefficient triples (a, b, c) for each equation.
(iii) Two-variable algebraic equation modeling the cost relationship.

FORMULA USED:
General Form of Linear Equation in Two Variables:
ax + by + c = 0, with coefficients a (coefficient of x), b (coefficient of y), and c (constant term).

STEP-BY-STEP CALCULATION:
Part (i):
Substitute a = 3, b = 0, c = -1/5 into ax + by + c = 0:
3x + 0y + (-1/5) = 0  =>  3x - 1/5 = 0  (or 15x - 1 = 0).

Part (ii) Standard Form Conversions:
(a) y - 15 = 2x:
    Rearrange: 2x - y + 15 = 0.
    Coefficients: a = 2, b = -1, c = 15.
(b) 3y - 2x = 0:
    Rearrange: -2x + 3y + 0 = 0 (or 2x - 3y = 0).
    Coefficients: a = -2, b = 3, c = 0 (or a = 2, b = -3, c = 0).
(c) 5x = 3y:
    Rearrange: 5x - 3y + 0 = 0.
    Coefficients: a = 5, b = -3, c = 0.
(d) x = 8:
    Rearrange: 1x + 0y - 8 = 0.
    Coefficients: a = 1, b = 0, c = -8.
(e) 3y = 1:
    Rearrange: 0x + 3y - 1 = 0.
    Coefficients: a = 0, b = 3, c = -1.

Part (iii) Cost Formulation:
Let the cost of a notebook be ₹x.
Let the cost of a pen be ₹y.
Given: x = 2y.
In standard form ax + by + c = 0:
1x - 2y + 0 = 0  =>  x - 2y = 0.

[ROUGH_WORK]
y - 15 = 2x -> 0 = 2x - y + 15 -> a=2, b=-1, c=15.
5x - 3y = 0 -> a=5, b=-3, c=0.
x - 8 = 0 -> 1x + 0y - 8 = 0.
3y - 1 = 0 -> 0x + 3y - 1 = 0.

Boxed Answer:
[ (i) 3x + 0y - 1/5 = 0, (ii) (a) 2x - y + 15 = 0; (b) -2x + 3y = 0; (c) 5x - 3y = 0; (d) 1x + 0y - 8 = 0; (e) 0x + 3y - 1 = 0, (iii) x - 2y = 0 ]"""
}
modules[0]['worked_examples'].append(we_m1_ex_13_1)

# Module 2: Add FORMULA USED to WE 1, and add WE 2 for Exercise Sets 13.2 & 13.3
sol_m2 = modules[1]['worked_examples'][0]['solution']
if "FORMULA USED" not in sol_m2:
    sol_m2 = sol_m2.replace("STEP-BY-STEP", "FORMULA USED:\nSlope-Intercept Form: y = mx + c\nSlope Formula: m = (y₂ - y₁) / (x₂ - x₁)\n\nSTEP-BY-STEP")
    modules[1]['worked_examples'][0]['solution'] = sol_m2

we_m2_ex_13_2_3 = {
    "problem": "Chapter 13, Exercise Sets 13.2 & 13.3 (Ganita Manjari Part 2, Sections 13.2 & 13.3, pp. 93 & 102):\n(i) Exercise Set 13.2, Q1: Verify whether the ordered pair (4, 3) is a solution of 5x - 6y = 2. Explain your reasoning.\n(ii) Exercise Set 13.2, Q2: Find any two solutions for each: (a) 7x - 3y = 21, (b) 2x + 3y = 5.\n(iii) Exercise Set 13.2, Q3: In the equations 2mx + 3y = 7 and 4x + ny = -10, m and n are constants. If (2, -1) is the simultaneous solution of both equations, find m and n.\n(iv) Exercise Set 13.3, Q2: A loading dock ramp rises 2.5 metres over a horizontal run of 4 metres. Calculate the exact slope of the ramp.",
    "solution": """GIVEN:
(i) Equation: 5x - 6y = 2; Candidate solution point: (x, y) = (4, 3).
(ii) Equations: (a) 7x - 3y = 21; (b) 2x + 3y = 5.
(iii) System: 2mx + 3y = 7 and 4x + ny = -10 with common solution (x, y) = (2, -1).
(iv) Ramp: Rise (vertical height) = 2.5 m; Run (horizontal length) = 4.0 m.

TO FIND / TO PROVE:
(i) Verify if (4, 3) satisfies 5x - 6y = 2.
(ii) Compute pairs of coordinates (x, y) satisfying each linear equation.
(iii) Solve for unknown parameters m and n.
(iv) Compute slope m_ramp.

FORMULA USED:
1. Solution Criterion: (x₀, y₀) is a solution iff substituting into LHS yields RHS.
2. Slope of an Incline: m = Rise / Run = Δy / Δx.

STEP-BY-STEP CALCULATION:
Part (i) Solution Verification:
Substitute x = 4 and y = 3 into LHS:
LHS = 5(4) - 6(3) = 20 - 18 = 2.
RHS = 2.
Since LHS = RHS, (4, 3) is indeed a valid solution of 5x - 6y = 2.

Part (ii) Two Solutions:
(a) For 7x - 3y = 21:
    - Set x = 0: 7(0) - 3y = 21 => -3y = 21 => y = -7. Solution: (0, -7).
    - Set y = 0: 7x - 3(0) = 21 => 7x = 21 => x = 3. Solution: (3, 0).
(b) For 2x + 3y = 5:
    - Set x = 1: 2(1) + 3y = 5 => 3y = 3 => y = 1. Solution: (1, 1).
    - Set x = 4: 2(4) + 3y = 5 => 8 + 3y = 5 => 3y = -3 => y = -1. Solution: (4, -1).

Part (iii) Parameter Determination:
Substitute (x, y) = (2, -1) into both equations:
Equation 1: 2m(2) + 3(-1) = 7
4m - 3 = 7  =>  4m = 10  =>  m = 10/4 = 2.5 (or 5/2).
Equation 2: 4(2) + n(-1) = -10
8 - n = -10  =>  -n = -18  =>  n = 18.

Part (iv) Ramp Slope:
Slope = Rise / Run = 2.5 m / 4.0 m = 25 / 40 = 5 / 8 = 0.625.

[ROUGH_WORK]
5(4) - 6(3) = 20 - 18 = 2 = RHS.
4m - 3 = 7 -> 4m = 10 -> m = 5/2.
8 - n = -10 -> n = 18.
2.5 / 4 = 5/8 = 0.625.

Boxed Answer:
[ (i) Yes, (4, 3) is a valid solution, (ii) (a) (0, -7), (3, 0); (b) (1, 1), (4, -1), (iii) m = 5/2 (2.5) and n = 18, (iv) Slope of Ramp = 5/8 = 0.625 ]"""
}
modules[1]['worked_examples'].append(we_m2_ex_13_2_3)

# Module 3: Add FORMULA USED to WE 1
sol_m3 = modules[2]['worked_examples'][0]['solution']
if "FORMULA USED" not in sol_m3:
    sol_m3 = sol_m3.replace("STEP-BY-STEP", "FORMULA USED:\nConsistency Conditions for Pair of Linear Equations:\na₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0.\n- Unique solution (intersecting): a₁/a₂ ≠ b₁/b₂\n- No solution (parallel): a₁/a₂ = b₁/b₂ ≠ c₁/c₂\n- Infinitely many (coincident): a₁/a₂ = b₁/b₂ = c₁/c₂\n\nSTEP-BY-STEP")
    modules[2]['worked_examples'][0]['solution'] = sol_m3

# Module 4: Add FORMULA USED to WE 1, and add WE 2 for Exercise Set 13.5
sol_m4 = modules[3]['worked_examples'][0]['solution']
if "FORMULA USED" not in sol_m4:
    sol_m4 = sol_m4.replace("STEP-BY-STEP", "FORMULA USED:\nMethods of Solving Linear Systems:\n1. Method of Substitution: Express one variable in terms of the other and substitute.\n2. Method of Elimination: Multiply equations by constants to equate coefficients of one variable and add/subtract.\n\nSTEP-BY-STEP")
    modules[3]['worked_examples'][0]['solution'] = sol_m4

we_m4_ex_13_5 = {
    "problem": "Chapter 13, Exercise Set 13.5 (Ganita Manjari Part 2, Section 13.4, pp. 116–117):\nForm a pair of linear equations and solve each problem:\n(i) Q1(i): The sum of two integers is 5 and their difference is -21. Find the two numbers.\n(ii) Q1(ii): The difference between two numbers is 26 and one number is 3 times the other. Find the numbers.\n(iii) Q1(iv): Taxi charges in a city consist of a fixed charge plus a charge per km. For 10 km, the charge is ₹155; for 15 km, the charge is ₹220. Find the fixed charge, charge per km, and the cost for 25 km.\n(iv) Q1(v): A fraction becomes 9/11 if 2 is added to both numerator and denominator. If 3 is added to both, it becomes 5/6. Find the fraction.",
    "solution": """GIVEN:
(i) Two integers x and y: x + y = 5, x - y = -21.
(ii) Two numbers x and y: x - y = 26, x = 3y.
(iii) Taxi fare: Fixed charge ₹x, rate ₹y per km. Total for 10 km = ₹155; total for 15 km = ₹220.
(iv) Fraction x/y: (x + 2)/(y + 2) = 9/11 and (x + 3)/(y + 3) = 5/6.

TO FIND / TO PROVE:
(i) The two integers.
(ii) The two numbers.
(iii) Fixed charge x, per-km rate y, and fare for 25 km.
(iv) The original fraction x/y.

FORMULA USED:
1. Linear Elimination Method.
2. Cost Function: Total Cost = Fixed Charge + (Distance × Rate per km).
3. Cross-Multiplication for rational fractions.

STEP-BY-STEP CALCULATION:
Part (i) Integers:
Equation 1: x + y = 5
Equation 2: x - y = -21
Add Eq 1 and Eq 2:
(x + y) + (x - y) = 5 + (-21)  =>  2x = -16  =>  x = -8.
Substitute x = -8 into Eq 1:
-8 + y = 5  =>  y = 13.
The numbers are -8 and 13. Check: -8 + 13 = 5, -8 - 13 = -21. Correct!

Part (ii) Difference and Ratio:
Equation 1: x - y = 26
Equation 2: x = 3y
Substitute x = 3y into Eq 1:
3y - y = 26  =>  2y = 26  =>  y = 13.
Then x = 3(13) = 39.
The numbers are 39 and 13. Check: 39 - 13 = 26. Correct!

Part (iii) Taxi Fare System:
Equation 1: x + 10y = 155
Equation 2: x + 15y = 220
Subtract Eq 1 from Eq 2:
(x + 15y) - (x + 10y) = 220 - 155
5y = 65  =>  y = 13.
Per-km charge = ₹13/km.
Substitute y = 13 into Eq 1:
x + 10(13) = 155  =>  x + 130 = 155  =>  x = 25.
Fixed charge = ₹25.
For a distance of 25 km:
Total Fare = x + 25y = 25 + 25(13) = 25 + 325 = ₹350.

Part (iv) Fraction:
Condition 1: (x + 2)/(y + 2) = 9/11
11(x + 2) = 9(y + 2)  =>  11x + 22 = 9y + 18  =>  11x - 9y = -4   --- (1)
Condition 2: (x + 3)/(y + 3) = 5/6
6(x + 3) = 5(y + 3)  =>  6x + 18 = 5y + 15  =>  6x - 5y = -3    --- (2)
Solve by elimination:
Multiply (1) by 5: 55x - 45y = -20
Multiply (2) by 9: 54x - 45y = -27
Subtract: (55x - 54x) = -20 - (-27)  =>  x = 7.
Substitute x = 7 into (2):
6(7) - 5y = -3  =>  42 - 5y = -3  =>  5y = 45  =>  y = 9.
Original fraction = 7/9.
Check: (7+2)/(9+2) = 9/11; (7+3)/(9+3) = 10/12 = 5/6. Correct!

[ROUGH_WORK]
2x = -16 -> x = -8, y = 13.
3y - y = 26 -> 2y = 26 -> y = 13, x = 39.
5y = 65 -> y = 13. x = 155 - 130 = 25.
25 + 25(13) = 25 + 325 = 350.
55x - 54x = 7 -> x = 7, y = 9.

Boxed Answer:
[ (i) Numbers: -8 and 13, (ii) Numbers: 39 and 13, (iii) Fixed Charge = ₹25, Rate = ₹13/km, Fare for 25 km = ₹350, (iv) Required Fraction = 7/9 ]"""
}
modules[3]['worked_examples'].append(we_m4_ex_13_5)

# Module 5: Add FORMULA USED to all WE, and add End-of-Chapter Exercise 4!
for we in modules[4]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nLinear Algebraic System Solvability & Consistency Criteria.\n\nSTEP-BY-STEP")
        we['solution'] = sol

we_m5_ex_4 = {
    "problem": "Chapter 13, End-of-Chapter Exercise 4 (Ganita Manjari Part 2, Section 13.5, p. 120):\nFind the point of intersection of the two straight lines shown on the textbook cover page / opening chapter graph: Line 1: 2x + y = 6, and Line 2: 2x - y = 2. Solve both graphically and algebraically.",
    "solution": """GIVEN:
Pair of linear equations from the opening cover page illustration:
Line 1 (L₁): 2x + y = 6
Line 2 (L₂): 2x - y = 2

TO FIND / TO PROVE:
(i) Solve for the unique point of intersection P(x, y) algebraically.
(ii) Determine coordinates of plotting points and verify the graphical intersection.

FORMULA USED:
1. Condition for Unique Intersection:
   a₁/a₂ ≠ b₁/b₂
   Here a₁/a₂ = 2/2 = 1, b₁/b₂ = 1/(-1) = -1. Since 1 ≠ -1, the lines intersect at exactly one point.
2. Algebraic Method of Elimination.

STEP-BY-STEP CALCULATION:
Part (i) Algebraic Solution:
Equation 1: 2x + y = 6   --- (1)
Equation 2: 2x - y = 2   --- (2)
Add Equation (1) and Equation (2):
(2x + y) + (2x - y) = 6 + 2
4x = 8  =>  x = 2.
Substitute x = 2 into Equation (1):
2(2) + y = 6  =>  4 + y = 6  =>  y = 2.
The lines intersect at the point P(2, 2).

Part (ii) Graphical Coordinates and Intersection:
- For Line 1: y = 6 - 2x
  If x = 0, y = 6 -> Point A(0, 6)
  If x = 2, y = 2 -> Point P(2, 2)
  If x = 3, y = 0 -> Point B(3, 0)
- For Line 2: y = 2x - 2
  If x = 0, y = -2 -> Point C(0, -2)
  If x = 1, y = 0 -> Point D(1, 0)
  If x = 2, y = 2 -> Point P(2, 2)
Both lines pass through the common point (2, 2).
Plotting these points on Cartesian axes reveals Line 1 descending with slope -2 and Line 2 ascending with slope +2, intersecting cleanly at P(2, 2).

[ROUGH_WORK]
2x + y = 6
2x - y = 2
Sum: 4x = 8 -> x = 2.
y = 6 - 2(2) = 2.
Check L2: 2(2) - 2 = 2. Correct!

Boxed Answer:
[ The point of intersection of the lines is P(2, 2) ]"""
}
modules[4]['worked_examples'].append(we_m5_ex_4)

# Module 6: Add FORMULA USED to all WE
for we in modules[5]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nApplied Linear Systems: Uniform Motion (Distance = Speed × Time), Geometric Invariants, Digits Expansion (10t + u).\n\nSTEP-BY-STEP")
        we['solution'] = sol

with open('scripts/maths_pt2_modules/ch13_linear_equations.json', 'w', encoding='utf-8') as f:
    json.dump(modules, f, indent=2, ensure_ascii=False)

print('Updated ch13_linear_equations.json successfully!')
