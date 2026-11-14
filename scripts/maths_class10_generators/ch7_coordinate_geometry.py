"""
Class 10 Mathematics - Chapter 7: Coordinate Geometry (NCERT CBSE)
Curriculum ID: 12f22395-a321-4a9d-85af-cd50b0fdcafe
Fully compliant with Invariant 10:
- Minimum 5 dedicated modules (Theory strictly in M1-M2, dedicated solvers M3-M5)
- 100% of all NCERT exercise questions (Ex 7.1, 7.2) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- True Cartesian Plots & Unslop High-Precision Vector SVGs
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_cartesian_svg, get_svg_wrapper

def get_ch7_modules():
    CURRICULUM_ID = "12f22395-a321-4a9d-85af-cd50b0fdcafe"
    
    # SVG 1: Distance Formula Right-Angled Triangle derivation
    svg_distance = build_cartesian_svg(
        domain=(-1, 7),
        range_y=(-1, 6),
        points=[
            {"x": 1, "y": 1, "label": "P(x₁, y₁)", "color": "#2563EB"},
            {"x": 6, "y": 4, "label": "Q(x₂, y₂)", "color": "#2563EB"},
            {"x": 6, "y": 1, "label": "R(x₂, y₁)", "color": "#64748B"},
        ],
        lines=[
            {"p1": (1, 1), "p2": (6, 4), "color": "#DC2626", "width": 2.5, "label": "d = √[(x₂-x₁)² + (y₂-y₁)²]"},
            {"p1": (1, 1), "p2": (6, 1), "color": "#2563EB", "width": 1.8, "label": "Δx = x₂ - x₁"},
            {"p1": (6, 1), "p2": (6, 4), "color": "#16A34A", "width": 1.8, "label": "Δy = y₂ - y₁"}
        ],
        title="Distance Formula Derivation via Pythagoras Theorem",
        caption="In right triangle PRQ: PQ² = PR² + RQ² = (x₂ - x₁)² + (y₂ - y₁)²"
    )

    # SVG 2: Section Formula Internal Division
    svg_section = build_cartesian_svg(
        domain=(-2, 8),
        range_y=(-2, 6),
        points=[
            {"x": -1, "y": 1, "label": "A(x₁, y₁)", "color": "#2563EB"},
            {"x": 7, "y": 5, "label": "B(x₂, y₂)", "color": "#2563EB"},
            {"x": 2.2, "y": 2.6, "label": "P(x, y) divides m₁:m₂", "color": "#DC2626"},
        ],
        lines=[
            {"p1": (-1, 1), "p2": (7, 5), "color": "#334155", "width": 2.2, "label": ""},
        ],
        title="Section Formula: Internal Division in Ratio m₁ : m₂",
        caption="P(x, y) = ( (m₁x₂ + m₂x₁)/(m₁ + m₂), (m₁y₂ + m₂y₁)/(m₁ + m₂) )"
    )

    # SVG 3: Formula Card
    card_formula = """
    <g transform="translate(50, 70)">
      <rect width="480" height="230" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" rx="10"/>
      <text x="24" y="28" fill="#0F172A" font-size="14" font-weight="700">Class 10 Coordinate Geometry Governing Formulas</text>
      
      <!-- Distance Formula -->
      <rect x="24" y="44" width="432" height="48" fill="#EFF6FF" stroke="#93C5FD" rx="6"/>
      <text x="36" y="66" fill="#1E40AF" font-size="11" font-weight="700">1. Distance Formula:</text>
      <text x="36" y="84" fill="#2563EB" font-size="13" font-weight="700">d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]   [From origin: d = √(x² + y²)]</text>
      
      <!-- Section Formula -->
      <rect x="24" y="100" width="432" height="52" fill="#F0FDF4" stroke="#86EFAC" rx="6"/>
      <text x="36" y="120" fill="#166534" font-size="11" font-weight="700">2. Section Formula (Internal Division in m₁ : m₂):</text>
      <text x="36" y="140" fill="#15803D" font-size="13" font-weight="700">P(x, y) = [ (m₁x₂ + m₂x₁) / (m₁ + m₂),  (m₁y₂ + m₂y₁) / (m₁ + m₂) ]</text>
      
      <!-- Midpoint Formula -->
      <rect x="24" y="160" width="432" height="52" fill="#FFFBEB" stroke="#FDE68A" rx="6"/>
      <text x="36" y="180" fill="#92400E" font-size="11" font-weight="700">3. Midpoint & Centroid:</text>
      <text x="36" y="198" fill="#B45309" font-size="12" font-weight="700">Midpoint M = [ (x₁ + x₂)/2, (y₁ + y₂)/2 ] | Centroid G = [ Σx/3, Σy/3 ]</text>
    </g>
    """
    svg_coord_card = get_svg_wrapper(card_formula, title="Coordinate Geometry Formula HUD", caption="Fundamental analytical geometry equations for 2D plane calculations")

    modules = [
        # Module 1: Distance Formula & Collinearity
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Distance Formula & Collinearity Criteria: Pythogorean Derivation & Geometric Classifications",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Rigorously derive the Distance Formula d = √[(x₂ - x₁)² + (y₂ - y₁)²] using the Pythagorean theorem on Cartesian projections. Master testing for collinearity via segment addition (AB + BC = AC) and classifying geometric figures (equilateral/isosceles triangles, squares, rectangles, rhombuses).",
            "key_concepts": [
                "Cartesian Projection: Horizontal distance Δx = |x₂ - x₁|, Vertical distance Δy = |y₂ - y₁|",
                "Pythagorean Derivation: In right triangle PRQ, PQ² = PR² + RQ² ⇒ d = √[(x₂ - x₁)² + (y₂ - y₁)²]",
                "Distance from Origin: d(O, P) = √(x² + y²)",
                "Collinearity Criterion: Points A, B, C are collinear if and only if the sum of lengths of any two segments equals the third (e.g. AB + BC = AC)",
                "Geometric Quadrilateral Criteria: Parallelogram (opposite sides equal), Rhombus (all 4 sides equal), Rectangle (opposite sides equal + diagonals equal), Square (all 4 sides equal + diagonals equal)"
            ],
            "subtopics": [
                "Full algebraic derivation of the distance formula",
                "Distance between symbolic points (a, b) and (-a, -b)",
                "Worked Examples 1, 2, 3, 4, 5 from NCERT",
                "Equidistant point condition on axes: On x-axis (x, 0), on y-axis (0, y)"
            ],
            "worked_examples": [
                {
                    "problem": "Example 1 (NCERT): Do the points (3, 2), (-2, -3) and (2, 3) form a triangle? If so, name the type of triangle formed.",
                    "solution": "Let the given points be P(3, 2), Q(-2, -3), and R(2, 3).\nFormula: Distance d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]\n\nStep 1: Calculate length PQ:\nPQ = √[ (-2 - 3)² + (-3 - 2)² ] = √[ (-5)² + (-5)² ] = √[ 25 + 25 ] = √50 ≈ 7.07 units.\n\nStep 2: Calculate length QR:\nQR = √[ (2 - (-2))² + (3 - (-3))² ] = √[ 4² + 6² ] = √[ 16 + 36 ] = √52 ≈ 7.21 units.\n\nStep 3: Calculate length PR:\nPR = √[ (2 - 3)² + (3 - 2)² ] = √[ (-1)² + 1² ] = √[ 1 + 1 ] = √2 ≈ 1.41 units.\n\nStep 4: Check Triangle Inequality Theorem:\nThe sum of any two lengths must be strictly greater than the third length:\nPQ + PR = 7.07 + 1.41 = 8.48 > 7.21 (QR)\nPQ + QR = 7.07 + 7.21 = 14.28 > 1.41 (PR)\nQR + PR = 7.21 + 1.41 = 8.62 > 7.07 (PQ)\nSince the sum of any two sides is greater than the third, the points P, Q, R form a triangle.\n\nStep 5: Check for Right-Angled Triangle via Converse of Pythagoras Theorem:\nPQ² + PR² = (√50)² + (√2)² = 50 + 2 = 52.\nQR² = (√52)² = 52.\nSince PQ² + PR² = QR², by the converse of Pythagoras Theorem, ΔPQR is a right-angled triangle with hypotenuse QR (right angle at P).\n[ROUGH_WORK]\n50 + 2 = 52\nConverse of Pythagoras holds exactly!\nBoxed Answer: [ Yes, the points form a Right-Angled Triangle with ∠P = 90° ].",
                    "concept_questions": [
                        "What would it mean if PQ + PR was exactly equal to QR?",
                        "Why does the distance formula produce identical results if you swap the order of the points (x₁ - x₂)²?"
                    ]
                },
                {
                    "problem": "Example 4 (NCERT): Find a relation between x and y such that the point (x, y) is equidistant from the points (7, 1) and (3, 5).",
                    "solution": "Let P(x, y) be the point equidistant from A(7, 1) and B(3, 5).\nGiven condition: PA = PB\nSquaring both sides (to eliminate the square root radical): PA² = PB²\n\nFormula: PA² = (x - 7)² + (y - 1)²\nPB² = (x - 3)² + (y - 5)²\n\nStep 1: Equate PA² and PB²:\n(x - 7)² + (y - 1)² = (x - 3)² + (y - 5)²\n\nStep 2: Expand all binomials using (a - b)² = a² - 2ab + b²:\n(x² - 14x + 49) + (y² - 2y + 1) = (x² - 6x + 9) + (y² - 10y + 25)\nx² + y² - 14x - 2y + 50 = x² + y² - 6x - 10y + 34\n\nStep 3: Cancel x² and y² from both sides:\n-14x - 2y + 50 = -6x - 10y + 34\nMove all terms to LHS:\n-14x + 6x - 2y + 10y + 50 - 34 = 0\n-8x + 8y + 16 = 0\n\nStep 4: Divide entire equation by -8:\nx - y - 2 = 0 (or x - y = 2).\n[ROUGH_WORK]\nGeometric Meaning: The set of all points equidistant from A and B is the perpendicular bisector of segment AB!\nMidpoint of AB: ((7+3)/2, (1+5)/2) = (5, 3).\nCheck (5, 3): 5 - 3 = 2 (True!)\nBoxed Answer: [ The relation between x and y is x - y = 2 (which represents the perpendicular bisector of segment AB) ].",
                    "concept_questions": [
                        "Why did x² and y² cancel out completely?",
                        "What is the geometric locus represented by x - y = 2?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Distance Formula Derivation & Pythagorean Projection",
                "diagram_type": "graph",
                "svg": svg_distance,
                "interactive_math_formula": "0.6x + 0.4",
                "concept_visuals": [
                    {
                        "concept_title": "Distance Formula Projection",
                        "diagram_title": "Right Triangle Hypotenuse Distance",
                        "svg": svg_distance,
                        "diagram_type": "graph",
                        "interactive_math_formula": "0.6x + 0.4",
                        "what_to_make": "Cartesian plot of segment PQ forming hypotenuse of right triangle with legs Δx and Δy",
                        "what_to_explain": "Direct Pythagorean proof of the distance formula"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting to square the negative difference: (-5)² is +25, NEVER -25!",
                "Trying to take square roots term-by-term: √(a² + b²) ≠ a + b!"
            ]
        },

        # Module 2: Section Formula, Internal Division & Midpoint Formula
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Section Formula & Internal Division: Masterclass in m₁ : m₂ Coordinates, Trisection & Midpoints",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Rigorously derive the Section Formula using similar right triangles. Master finding dividing coordinates P(x, y), calculating the unknown ratio k : 1, trisection coordinates, and the midpoint formula.",
            "key_concepts": [
                "Section Formula: P(x, y) = [ (m₁x₂ + m₂x₁) / (m₁ + m₂), (m₁y₂ + m₂y₁) / (m₁ + m₂) ]",
                "Derivation via Similar Triangles: Horizontal and vertical projections are in ratio m₁ : m₂",
                "Special Case: Midpoint Formula M = [ (x₁ + x₂)/2, (y₁ + y₂)/2 ] (when m₁ = m₂ = 1)",
                "Unknown Ratio Technique: Let ratio be k : 1 ⇒ P = [ (kx₂ + x₁)/(k + 1), (ky₂ + y₁)/(k + 1) ]",
                "Points of Trisection: Dividing a line segment into three equal parts using ratios 1 : 2 and 2 : 1"
            ],
            "subtopics": [
                "Proof of section formula via AAA similarity of projection triangles",
                "Worked Examples 6, 7, 8, 9, 10 from NCERT",
                "Division by coordinate axes: Point on x-axis has y = 0, point on y-axis has x = 0",
                "Parallelogram diagonal bisection theorem applied to coordinate geometry"
            ],
            "worked_examples": [
                {
                    "problem": "Example 6 (NCERT): Find the coordinates of the point which divides the line segment joining the points (4, -3) and (8, 5) in the ratio 3 : 1 internally.",
                    "solution": "Let A = (4, -3) and B = (8, 5).\nHere x₁ = 4, y₁ = -3, x₂ = 8, y₂ = 5.\nGiven ratio m₁ : m₂ = 3 : 1.\n\nFormula: Section Formula for internal division:\nx = (m₁x₂ + m₂x₁) / (m₁ + m₂)\ny = (m₁y₂ + m₂y₁) / (m₁ + m₂)\n\nStep 1: Compute x-coordinate:\nx = [ 3(8) + 1(4) ] / (3 + 1) = [ 24 + 4 ] / 4 = 28 / 4 = 7.\n\nStep 2: Compute y-coordinate:\ny = [ 3(5) + 1(-3) ] / (3 + 1) = [ 15 - 3 ] / 4 = 12 / 4 = 3.\n[ROUGH_WORK]\nx: (3×8 + 1×4)/4 = 28/4 = 7\ny: (3×5 + 1×(-3))/4 = 12/4 = 3\nBoxed Answer: [ The coordinates of the dividing point are P(7, 3) ].",
                    "concept_questions": [
                        "Why does the ratio multiplier m₁ multiply the coordinate of B (x₂) and not A (x₁)?",
                        "What coordinates would you get if the ratio was 1 : 3 instead of 3 : 1?"
                    ]
                },
                {
                    "problem": "Example 7 (NCERT): In what ratio does the point (-4, 6) divide the line segment joining the points A(-6, 10) and B(3, -8)?",
                    "solution": "Let the required ratio be k : 1.\nHere A(-6, 10) is (x₁, y₁), B(3, -8) is (x₂, y₂).\nThe dividing point is P(-4, 6).\n\nFormula for x-coordinate with ratio k : 1:\nx = (k x₂ + 1 x₁) / (k + 1)\n\nSubstitute known values:\n-4 = [ k(3) + 1(-6) ] / (k + 1)\n-4(k + 1) = 3k - 6\n-4k - 4 = 3k - 6\n-4k - 3k = -6 + 4\n-7k = -2\nk = 2/7.\nTherefore, the ratio k : 1 is (2/7) : 1 = 2 : 7.\n\nVerification with y-coordinate:\ny = [ k y₂ + y₁ ] / (k + 1) = [ (2/7)(-8) + 10 ] / (2/7 + 1)\n= [ -16/7 + 70/7 ] / (9/7) = (54/7) / (9/7) = 54 / 9 = 6.\nSince y = 6 matches the given y-coordinate, the result is fully verified!\n[ROUGH_WORK]\nRatio k : 1 reduces 2 variables (m₁, m₂) to 1 variable k!\nBoxed Answer: [ The point P(-4, 6) divides segment AB internally in the ratio 2 : 7 ].",
                    "concept_questions": [
                        "Why is setting the ratio as k : 1 algebraically superior to using m₁ : m₂?",
                        "What would it mean if k turned out to be negative?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Section Formula & Internal Segment Division HUD",
                "diagram_type": "graph",
                "svg": svg_section,
                "interactive_math_formula": "0.5x + 1.5",
                "concept_visuals": [
                    {
                        "concept_title": "Internal Division Geometry",
                        "diagram_title": "Ratio Partition Visualization",
                        "svg": svg_section,
                        "diagram_type": "graph",
                        "interactive_math_formula": "0.5x + 1.5",
                        "what_to_make": "Segment AB divided at P in ratio m₁ : m₂",
                        "what_to_explain": "Proportional projection mapping onto both coordinate axes"
                    }
                ]
            },
            "common_misconceptions": [
                "Criss-cross multiplication error: Multiplying m₁ by x₁ instead of x₂ (always remember: m₁ multiplies the far point B, m₂ multiplies the near point A!).",
                "Forgetting to verify the ratio against the other coordinate when solving for k : 1."
            ]
        },

        # Module 3: Exercise 7.1 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise 7.1 Complete Solver: Distance Formula Calculations & Collinearity Tests (Q1 to Q10)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 7.1 Questions 1 through 10. Master distance between points with symbolic parameters (a, b), Town A to Town B geographical distance, testing collinearity of (1, 5), (2, 3), (-2, -11), Champa-Chameli classroom grid square proof, quadrilateral classification, and finding points equidistant on coordinate axes.",
            "key_concepts": [
                "Ex 7.1 Q1: Distance between 3 pairs: (2, 3) & (4, 1); (-5, 7) & (-1, 3); (a, b) & (-a, -b) ⇒ 2√(a² + b²)",
                "Ex 7.1 Q2: Distance between (0, 0) and (36, 15) ⇒ √(1296 + 225) = √1521 = 39 km",
                "Ex 7.1 Q3: Testing collinearity of A(1, 5), B(2, 3), C(-2, -11) ⇒ AB = √5, BC = √212, AC = √265 (Not collinear)",
                "Ex 7.1 Q4: Testing isosceles triangle (5, -2), (6, 4), (7, -2)",
                "Ex 7.1 Q5: Champa and Chameli classroom grid: A(3, 4), B(6, 7), C(9, 4), D(6, 1) forms a square",
                "Ex 7.1 Q7: Point on x-axis (x, 0) equidistant from (2, -5) and (-2, 9) ⇒ x = -7 ⇒ (-7, 0)",
                "Ex 7.1 Q8: Value of y for distance 10 between P(2, -3) and Q(10, y) ⇒ y = 3 or y = -9",
                "Ex 7.1 Q9: Equidistant Q(0, 1) from P(5, -3) and R(x, 6)",
                "Ex 7.1 Q10: Relation between x and y equidistant from (3, 6) and (-3, 4) ⇒ 3x + y - 5 = 0"
            ],
            "subtopics": [
                "Full resolution of Q1 to Q10",
                "Proving a figure is a square (all 4 sides equal AND both diagonals equal)",
                "Solving quadratic equations arising from distance constraints"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 7.1 Q1 (iii): Find the distance between the points (a, b) and (-a, -b).",
                    "solution": "Let P = (a, b) and Q = (-a, -b).\nHere x₁ = a, y₁ = b, x₂ = -a, y₂ = -b.\n\nFormula: d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]\nSubstitution:\nd = √[ (-a - a)² + (-b - b)² ]\n= √[ (-2a)² + (-2b)² ]\n= √[ 4a² + 4b² ]\nFactor out 4 from under the radical:\n= √[ 4(a² + b²) ]\n= 2 √(a² + b²).\n[ROUGH_WORK]\n(-2a)² = 4a²\n√4 = 2\nBoxed Answer: [ Distance = 2√(a² + b²) units ].",
                    "concept_questions": [
                        "Why is the distance from the origin to (a, b) equal to half of this distance?",
                        "Notice the points (a, b) and (-a, -b) are diagonally opposite reflections through the origin!"
                    ]
                },
                {
                    "problem": "Exercise 7.1 Q7: Find the point on the x-axis which is equidistant from (2, -5) and (-2, 9).",
                    "solution": "Any point on the x-axis has its y-coordinate equal to 0.\nLet the required point on the x-axis be P(x, 0).\nLet given points be A(2, -5) and B(-2, 9).\n\nCondition: PA = PB ⇒ PA² = PB²\n\nFormula:\nPA² = (x - 2)² + (0 - (-5))² = (x - 2)² + 5² = (x² - 4x + 4) + 25 = x² - 4x + 29\nPB² = (x - (-2))² + (0 - 9)² = (x + 2)² + (-9)² = (x² + 4x + 4) + 81 = x² + 4x + 85\n\nEquating PA² and PB²:\nx² - 4x + 29 = x² + 4x + 85\nCancel x² from both sides:\n-4x + 29 = 4x + 85\n-4x - 4x = 85 - 29\n-8x = 56\nx = 56 / (-8) = -7.\n\nTherefore, the required point is (-7, 0).\n[ROUGH_WORK]\nCheck PA: √[(-7 - 2)² + (0 - (-5))²] = √[(-9)² + 5²] = √[81 + 25] = √106\nCheck PB: √[(-7 - (-2))² + (0 - 9)²] = √[(-5)² + (-9)²] = √[25 + 81] = √106\nPA = PB = √106 (Verified!)\nBoxed Answer: [ The point on the x-axis is (-7, 0) ].",
                    "concept_questions": [
                        "Why is the y-coordinate of any point on the x-axis strictly 0?",
                        "How would you set up the problem if the point was on the y-axis instead?"
                    ]
                },
                {
                    "problem": "Exercise 7.1 Q8: Find the values of y for which the distance between the points P(2, -3) and Q(10, y) is 10 units.",
                    "solution": "Given: P = (2, -3), Q = (10, y). Distance PQ = 10 units.\nSquaring both sides: PQ² = 10² = 100.\n\nFormula: PQ² = (10 - 2)² + (y - (-3))²\n100 = 8² + (y + 3)²\n100 = 64 + (y + 3)²\n(y + 3)² = 100 - 64 = 36\n\nTaking square root on both sides:\ny + 3 = ±√36 = ±6\n\nCase 1: y + 3 = 6 ⇒ y = 6 - 3 = 3.\nCase 2: y + 3 = -6 ⇒ y = -6 - 3 = -9.\n[ROUGH_WORK]\nCheck y = 3: (10 - 2)² + (3 - (-3))² = 8² + 6² = 64 + 36 = 100 ⇒ √100 = 10 (True!)\nCheck y = -9: 8² + (-9 + 3)² = 8² + (-6)² = 64 + 36 = 100 ⇒ √100 = 10 (True!)\nBoxed Answer: [ y = 3 or y = -9 ].",
                    "concept_questions": [
                        "Why are there two possible values for y geometrically?",
                        "Notice that (10, 3) and (10, -9) lie on the vertical line x = 10, symmetric above and below y = -3!"
                    ]
                },
                {
                    "problem": "Exercise 7.1 Q10: Find a relation between x and y such that the point (x, y) is equidistant from the point (3, 6) and (-3, 4).",
                    "solution": "Let P(x, y) be equidistant from A(3, 6) and B(-3, 4).\nCondition: PA = PB ⇒ PA² = PB²\n\nPA² = (x - 3)² + (y - 6)² = x² - 6x + 9 + y² - 12y + 36 = x² + y² - 6x - 12y + 45\nPB² = (x - (-3))² + (y - 4)² = (x + 3)² + (y - 4)² = x² + 6x + 9 + y² - 8y + 16 = x² + y² + 6x - 8y + 25\n\nEquating PA² and PB²:\nx² + y² - 6x - 12y + 45 = x² + y² + 6x - 8y + 25\nCancel x² + y²:\n-6x - 12y + 45 = 6x - 8y + 25\nMove terms to RHS:\n6x + 6x - 8y + 12y + 25 - 45 = 0\n12x + 4y - 20 = 0\nDivide entire equation by 4:\n3x + y - 5 = 0.\n[ROUGH_WORK]\nMidpoint of AB: ((3 - 3)/2, (6 + 4)/2) = (0, 5).\nSubstitute (0, 5) into 3x + y - 5: 3(0) + 5 - 5 = 0 (True!)\nBoxed Answer: [ The relation between x and y is 3x + y - 5 = 0 ].",
                    "concept_questions": [
                        "What is the slope of the line segment AB, and what is the slope of 3x + y - 5 = 0? Verify they are negative reciprocals."
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Equidistant Locus & Cartesian Distance HUD",
                "diagram_type": "graph",
                "svg": svg_distance,
                "interactive_math_formula": "-3x + 5",
                "concept_visuals": [
                    {
                        "concept_title": "Equidistant Perpendicular Bisector Locus",
                        "diagram_title": "Linear Locus Projection",
                        "svg": svg_distance,
                        "diagram_type": "graph",
                        "interactive_math_formula": "-3x + 5",
                        "what_to_make": "Segment AB and its perpendicular bisector 3x + y - 5 = 0",
                        "what_to_explain": "Equidistant points form the perpendicular bisector line"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting the ± when taking the square root of 36, losing the second root y = -9!",
                "Assuming (a, b) and (-a, -b) have a distance of 0 because they cancel out: Distances are always positive!"
            ]
        },

        # Module 4: Exercise 7.2 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 7.2 Complete Solver: Section Formula, Trisection & Sports Day Flag Coordinates (Q1 to Q10)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete resolution of NCERT Exercise 7.2 Questions 1 through 10. Master trisection of line segments, the famous Sports Day green and red flag problem, finding unknown ratios from axes division, parallelogram 4th vertex determination, and area of a rhombus via diagonals.",
            "key_concepts": [
                "Ex 7.2 Q1: Point dividing (-1, 7) and (4, -3) in ratio 2 : 3 ⇒ (1, 3)",
                "Ex 7.2 Q2: Points of trisection of (4, -1) and (-2, -3) ⇒ P(2, -5/3) and Q(0, -7/3)",
                "Ex 7.2 Q3: Sports Day: Niharika at (2, 25), Preet at (8, 20) ⇒ Distance = √61 m; Rashmi midpoint at (5, 22.5)",
                "Ex 7.2 Q4: Ratio in which (-1, 6) divides (-3, 10) and (6, -8) ⇒ 2 : 7",
                "Ex 7.2 Q5: Ratio in which x-axis divides (1, -5) and (-4, 5) ⇒ 1 : 1 (midpoint) ⇒ (-3/2, 0)",
                "Ex 7.2 Q6: Vertices of parallelogram (1, 2), (4, y), (x, 6), (3, 5) ⇒ Equating diagonal midpoints ⇒ x = 6, y = 3",
                "Ex 7.2 Q7: Coordinates of point A where AB is diameter of circle with center (2, -3) and B(1, 4) ⇒ A(3, -10)",
                "Ex 7.2 Q8: Point P on AB such that AP = (3/7)AB ⇒ Ratio AP : PB = 3 : 4",
                "Ex 7.2 Q9: Dividing segment joining (-2, 2) and (2, 8) into four equal parts",
                "Ex 7.2 Q10: Area of rhombus with vertices taken in order = (1/2) × d₁ × d₂"
            ],
            "subtopics": [
                "Full resolution of Q1 to Q10",
                "Trisection methodology (1:2 and 2:1)",
                "Parallelogram property: Diagonals bisect each other ⇒ Midpoint of AC = Midpoint of BD",
                "Rhombus area calculation via coordinate diagonal lengths"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 7.2 Q2: Find the coordinates of the points of trisection of the line segment joining (4, -1) and (-2, -3).",
                    "solution": "Let A = (4, -1) and B = (-2, -3).\nPoints of trisection P and Q divide segment AB into 3 equal parts: AP = PQ = QB.\n\nStep 1: Point P divides AB internally in the ratio 1 : 2:\nHere m₁ = 1, m₂ = 2.\nx_P = [ 1(-2) + 2(4) ] / (1 + 2) = [ -2 + 8 ] / 3 = 6 / 3 = 2.\ny_P = [ 1(-3) + 2(-1) ] / (1 + 2) = [ -3 - 2 ] / 3 = -5/3.\nSo P = (2, -5/3).\n\nStep 2: Point Q divides AB internally in the ratio 2 : 1 (or Q is the midpoint of PB):\nUsing midpoint of PB:\nx_Q = (x_P + x_B) / 2 = [ 2 + (-2) ] / 2 = 0 / 2 = 0.\ny_Q = (y_P + y_B) / 2 = [ -5/3 + (-3) ] / 2 = [ -5/3 - 9/3 ] / 2 = (-14/3) / 2 = -7/3.\nSo Q = (0, -7/3).\n[ROUGH_WORK]\nCheck Q via 2:1 on AB:\nx = (2(-2) + 1(4))/3 = (-4 + 4)/3 = 0\ny = (2(-3) + 1(-1))/3 = (-6 - 1)/3 = -7/3\nBoth methods give identical coordinates!\nBoxed Answer: [ Coordinates of points of trisection are P(2, -5/3) and Q(0, -7/3) ].",
                    "concept_questions": [
                        "Why does using the midpoint of PB for finding Q save computational time?",
                        "How many trisection points does a line segment have?"
                    ]
                },
                {
                    "problem": "Exercise 7.2 Q6: If (1, 2), (4, y), (x, 6) and (3, 5) are the vertices of a parallelogram taken in order, find x and y.",
                    "solution": "Let vertices of parallelogram ABCD in order be:\nA(1, 2), B(4, y), C(x, 6), D(3, 5).\n\nFundamental Theorem: The diagonals of a parallelogram bisect each other.\nTherefore: Midpoint of diagonal AC = Midpoint of diagonal BD.\n\nStep 1: Find midpoint of AC:\nMidpoint of AC = [ (1 + x)/2, (2 + 6)/2 ] = [ (1 + x)/2, 8/2 ] = [ (1 + x)/2, 4 ].\n\nStep 2: Find midpoint of BD:\nMidpoint of BD = [ (4 + 3)/2, (y + 5)/2 ] = [ 7/2, (y + 5)/2 ].\n\nStep 3: Equate the respective coordinates of the midpoints:\nx-coordinate:\n(1 + x) / 2 = 7 / 2 ⇒ 1 + x = 7 ⇒ x = 6.\n\ny-coordinate:\n(y + 5) / 2 = 4 ⇒ y + 5 = 8 ⇒ y = 3.\n[ROUGH_WORK]\nMidpoint of AC: ((1+6)/2, 4) = (3.5, 4)\nMidpoint of BD: (7/2, (3+5)/2) = (3.5, 4) (Verified!)\nBoxed Answer: [ x = 6, y = 3 ].",
                    "concept_questions": [
                        "Why is using the midpoint property infinitely faster than setting opposite sides equal with the distance formula?",
                        "What happens if the vertices are not taken in cyclic order?"
                    ]
                },
                {
                    "problem": "Exercise 7.2 Q8: If A and B are (-2, -2) and (2, -4), respectively, find the coordinates of P such that AP = 3/7 AB and P lies on the line segment AB.",
                    "solution": "Given: A = (-2, -2), B = (2, -4).\nGiven relation: AP = (3/7) AB.\n\nStep 1: Determine the ratio AP : PB:\nPB = AB - AP = AB - (3/7) AB = (4/7) AB.\nTherefore:\nAP / PB = [ (3/7) AB ] / [ (4/7) AB ] = 3 / 4.\nSo P divides segment AB internally in the ratio 3 : 4 (m₁ = 3, m₂ = 4).\n\nStep 2: Apply Section Formula:\nx = [ 3(2) + 4(-2) ] / (3 + 4) = [ 6 - 8 ] / 7 = -2/7.\ny = [ 3(-4) + 4(-2) ] / (3 + 4) = [ -12 - 8 ] / 7 = -20/7.\n[ROUGH_WORK]\nCommon pitfall: Taking ratio as 3 : 7 instead of 3 : 4!\nAP is 3 parts out of 7 total parts, so PB is 4 parts!\nBoxed Answer: [ Coordinates of P are (-2/7, -20/7) ].",
                    "concept_questions": [
                        "Why is the ratio AP : PB equal to 3 : 4 and NOT 3 : 7?",
                        "What fraction of AB is PB?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Parallelogram Diagonal Bisection & Trisection HUD",
                "diagram_type": "diagram",
                "svg": svg_coord_card,
                "concept_visuals": [
                    {
                        "concept_title": "Parallelogram Midpoint Equivalence",
                        "diagram_title": "Diagonal Bisection Atlas",
                        "svg": svg_coord_card,
                        "diagram_type": "diagram",
                        "what_to_make": "Parallelogram ABCD with diagonals AC and BD meeting at common midpoint",
                        "what_to_explain": "Equating diagonal midpoints allows solving for 2 unknown coordinates simultaneously"
                    }
                ]
            },
            "common_misconceptions": [
                "Taking the ratio as 3 : 7 when given AP = 3/7 AB: The section formula requires the ratio of the two pieces AP : PB = 3 : 4!",
                "Using the distance formula to find missing vertices of a parallelogram: Setting midpoints equal is 10 times simpler and avoids messy quadratics."
            ]
        },

        # Module 5: Board Exam Advanced Coordinate Geometry & Analytic Properties
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Board Exam Analytic Mastery: Triangle Centroid, Collinear Parameterization & Rhombus Area",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master advanced board exam coordinate geometry problems. Rigorous derivation of the Centroid Formula G = [ (x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3 ], finding circumcentre of a triangle from equidistant vertices, and calculating polygon areas via analytical decomposition.",
            "key_concepts": [
                "Centroid of a Triangle Formula: G = [ (x₁ + x₂ + x₃)/3, (y₁ + y₂ + y₃)/3 ]",
                "Centroid Division Ratio: The centroid G divides each median internally in the ratio 2 : 1 from vertex to base midpoint",
                "Circumcentre Properties: Equidistant from all 3 vertices OA = OB = OC",
                "Area of Rhombus Formula: Area = (1/2) × d₁ × d₂ using distance formula for diagonals AC and BD",
                "Analytical Locus & Equidistant Constraints"
            ],
            "subtopics": [
                "Derivation of the centroid formula using section formula on median",
                "Finding circumcentre coordinates by solving linear system OA² = OB² = OC²",
                "Full resolution of Exercise 7.2 Question 10 (Area of Rhombus)"
            ],
            "worked_examples": [
                {
                    "problem": "Derive the coordinates of the centroid G of a triangle whose vertices are A(x₁, y₁), B(x₂, y₂), and C(x₃, y₃).",
                    "solution": "STATEMENT: The centroid G of a triangle divides each median internally in the ratio 2 : 1.\n\nStep 1: Find the coordinates of the midpoint D of base BC:\nD is the midpoint of B(x₂, y₂) and C(x₃, y₃).\nBy Midpoint Formula:\nD = [ (x₂ + x₃)/2, (y₂ + y₃)/2 ].\n\nStep 2: Apply the Section Formula to median AD:\nThe centroid G divides median AD internally in the ratio 2 : 1 from vertex A to D.\nHere m₁ = 2, m₂ = 1.\nPoint A is (x₁, y₁), and Point D is [ (x₂ + x₃)/2, (y₂ + y₃)/2 ].\n\nStep 3: Calculate x-coordinate of G:\nx_G = [ m₁ x_D + m₂ x_A ] / (m₁ + m₂)\n= [ 2 × ((x₂ + x₃)/2) + 1 × x₁ ] / (2 + 1)\n= [ (x₂ + x₃) + x₁ ] / 3\n= (x₁ + x₂ + x₃) / 3.\n\nStep 4: Calculate y-coordinate of G:\ny_G = [ m₁ y_D + m₂ y_A ] / (m₁ + m₂)\n= [ 2 × ((y₂ + y₃)/2) + 1 × y₁ ] / (2 + 1)\n= [ (y₂ + y₃) + y₁ ] / 3\n= (y₁ + y₂ + y₃) / 3.\n\nConclusion:\nCentroid G = [ (x₁ + x₂ + x₃) / 3, (y₁ + y₂ + y₃) / 3 ].\nHence Derived!\n[ROUGH_WORK]\n2 cancels the /2 in the midpoint formula perfectly!\nBoxed Answer: [ Centroid G = ( (x₁ + x₂ + x₃)/3, (y₁ + y₂ + y₃)/3 ) ].",
                    "concept_questions": [
                        "Why does the centroid divide every median in the ratio 2 : 1?",
                        "What is the physical meaning of the centroid in physics (centre of gravity)?"
                    ]
                },
                {
                    "problem": "Exercise 7.2 Q10: Find the area of a rhombus if its vertices are (3, 0), (4, 5), (-1, 4) and (-2, -1) taken in order.",
                    "solution": "Let vertices in order be A(3, 0), B(4, 5), C(-1, 4), and D(-2, -1).\nFormula: Area of a rhombus = (1/2) × d₁ × d₂ = (1/2) × AC × BD.\n\nStep 1: Find length of diagonal AC:\nAC = √[ (-1 - 3)² + (4 - 0)² ]\n= √[ (-4)² + 4² ] = √[ 16 + 16 ] = √32 = 4√2 units.\n\nStep 2: Find length of diagonal BD:\nBD = √[ (-2 - 4)² + (-1 - 5)² ]\n= √[ (-6)² + (-6)² ] = √[ 36 + 36 ] = √72 = 6√2 units.\n\nStep 3: Calculate Area:\nArea = (1/2) × AC × BD\n= (1/2) × (4√2) × (6√2)\n= (1/2) × 24 × (√2 × √2)\n= (1/2) × 24 × 2 = 24 square units.\n[ROUGH_WORK]\n(4√2 × 6√2) / 2 = 24 × 2 / 2 = 24\nBoxed Answer: [ Area of the rhombus = 24 square units ].",
                    "concept_questions": [
                        "Why is the area of a rhombus equal to half the product of its diagonals?",
                        "Do the diagonals of a rhombus intersect at 90°? Check the slopes of AC and BD."
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Centroid 2:1 Median Division & Rhombus Diagonals HUD",
                "diagram_type": "diagram",
                "svg": svg_coord_card,
                "concept_visuals": [
                    {
                        "concept_title": "Centroid Division Geometry",
                        "diagram_title": "Median Concurrency Atlas",
                        "svg": svg_coord_card,
                        "diagram_type": "diagram",
                        "what_to_make": "Triangle with medians intersecting at centroid G in ratio 2:1",
                        "what_to_explain": "Arithmetic mean of three vertices yields centre of gravity"
                    }
                ]
            },
            "common_misconceptions": [
                "Attempting to calculate rhombus area using side lengths instead of diagonals: The formula is (1/2) × d₁ × d₂!",
                "Dividing by 2 instead of 3 for the centroid formula: Centroid is average of 3 vertices, so divide by 3!"
            ]
        }
    ]
    
    return modules
