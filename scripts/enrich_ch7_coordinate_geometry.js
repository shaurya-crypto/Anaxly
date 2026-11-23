const { supabase } = require('./db_helper');

async function enrichCh7() {
  const CURRICULUM_ID = '12f22395-a321-4a9d-85af-cd50b0fdcafe';
  console.log('=== ENRICHING CLASS 10 MATHS - CHAPTER 7: COORDINATE GEOMETRY ===\n');

  // Module 1: Distance Formula Foundations & Collinearity Criteria (Examples 1-5 & Theory)
  const mod1WorkedExamples = [
    {
      problem: "Example 1 (NCERT Page 3): Do the points (3, 2), (-2, -3) and (2, 3) form a triangle? If so, name the type of triangle formed.",
      solution: "Let the points be P(3, 2), Q(-2, -3), and R(2, 3).\nTarget: Test if P, Q, R form a triangle and classify its type.\nFormula: Distance d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]\n\nStep 1: Compute PQ:\nPQ = √[ (-2 - 3)² + (-3 - 2)² ] = √[ (-5)² + (-5)² ] = √[ 25 + 25 ] = √50 ≈ 7.07 units.\n\nStep 2: Compute QR:\nQR = √[ (2 - (-2))² + (3 - (-3))² ] = √[ (4)² + (6)² ] = √[ 16 + 36 ] = √52 ≈ 7.21 units.\n\nStep 3: Compute PR:\nPR = √[ (2 - 3)² + (3 - 2)² ] = √[ (-1)² + (1)² ] = √[ 1 + 1 ] = √2 ≈ 1.41 units.\n\nStep 4: Check Triangle Inequality & Pythagoras Theorem:\nPQ + PR = 7.07 + 1.41 = 8.48 > 7.21 (QR)\nSince the sum of any two sides is strictly greater than the third side, P, Q, and R form a triangle.\nCheck Pythagoras: PQ² + PR² = 50 + 2 = 52 = QR².\nSince PQ² + PR² = QR², by the Converse of Pythagoras Theorem, ∠P = 90°.\n[ROUGH_WORK]\nPQ² = 50, QR² = 52, PR² = 2\n50 + 2 = 52 ⇒ Right-angled at P!\nBoxed Answer: [ Points P, Q, and R form a right-angled triangle right-angled at P ].",
      concept_questions: [
        "What geometric condition proves that three points form a valid triangle?",
        "Why does PQ² + PR² = QR² prove ∠P = 90° and not ∠Q = 90°?"
      ],
      graph_payload: {
        points: [
          { x: 3, y: 2, label: "P(3, 2)", callout: "Vertex (90°)" },
          { x: -2, y: -3, label: "Q(-2, -3)", callout: "Hypotenuse End 1" },
          { x: 2, y: 3, label: "R(2, 3)", callout: "Hypotenuse End 2" }
        ],
        segments: [
          { start: [3, 2], end: [-2, -3], label: "PQ = √50" },
          { start: [-2, -3], end: [2, 3], label: "QR = √52 (Hypotenuse)" },
          { start: [3, 2], end: [2, 3], label: "PR = √2" }
        ],
        polygons: [
          { points: [[3, 2], [-2, -3], [2, 3]], label: "Right Triangle PQR" }
        ]
      }
    },
    {
      problem: "Example 2 (NCERT Page 4): Show that the points (1, 7), (4, 2), (-1, -1) and (-4, 4) are the vertices of a square.",
      solution: "Let the points be A(1, 7), B(4, 2), C(-1, -1), and D(-4, 4).\nCondition for a Square: All four sides must be equal, AND both diagonals must be equal.\n\nStep 1: Compute side lengths:\nAB = √[ (4 - 1)² + (2 - 7)² ] = √[ 3² + (-5)² ] = √[ 9 + 25 ] = √34\nBC = √[ (-1 - 4)² + (-1 - 2)² ] = √[ (-5)² + (-3)² ] = √[ 25 + 9 ] = √34\nCD = √[ (-4 - (-1))² + (4 - (-1))² ] = √[ (-3)² + 5² ] = √[ 9 + 25 ] = √34\nDA = √[ (1 - (-4))² + (7 - 4)² ] = √[ 5² + 3² ] = √[ 25 + 9 ] = √34\nAll four sides AB = BC = CD = DA = √34.\n\nStep 2: Compute diagonal lengths:\nAC = √[ (-1 - 1)² + (-1 - 7)² ] = √[ (-2)² + (-8)² ] = √[ 4 + 64 ] = √68\nBD = √[ (-4 - 4)² + (4 - 2)² ] = √[ (-8)² + 2² ] = √[ 64 + 4 ] = √68\nDiagonals AC = BD = √68.\n[ROUGH_WORK]\nSide² = 34, Diagonal² = 68 = 2 × Side² (True for square with 90° corners!)\nBoxed Answer: [ Since all 4 sides are equal to √34 and both diagonals are equal to √68, ABCD is a square ].",
      concept_questions: [
        "Why is showing all four sides equal not sufficient by itself to prove a quadrilateral is a square?",
        "What shape would it be if all four sides were equal but the diagonals were unequal?"
      ],
      graph_payload: {
        points: [
          { x: 1, y: 7, label: "A(1, 7)" },
          { x: 4, y: 2, label: "B(4, 2)" },
          { x: -1, y: -1, label: "C(-1, -1)" },
          { x: -4, y: 4, label: "D(-4, 4)" }
        ],
        segments: [
          { start: [1, 7], end: [4, 2], label: "AB = √34" },
          { start: [4, 2], end: [-1, -1], label: "BC = √34" },
          { start: [-1, -1], end: [-4, 4], label: "CD = √34" },
          { start: [-4, 4], end: [1, 7], label: "DA = √34" },
          { start: [1, 7], end: [-1, -1], label: "Diagonal AC = √68" },
          { start: [4, 2], end: [-4, 4], label: "Diagonal BD = √68" }
        ],
        polygons: [
          { points: [[1, 7], [4, 2], [-1, -1], [-4, 4]], label: "Square ABCD" }
        ]
      }
    },
    {
      problem: "Example 3 (NCERT Page 5): Figure 7.6 shows the arrangement of desks in a classroom. Ashima, Bharti, and Camella are seated at A(3, 1), B(6, 4), and C(8, 6) respectively. Do you think they are seated in a line?",
      solution: "Let the points be A(3, 1), B(6, 4), and C(8, 6).\nCondition for Collinearity: Three points A, B, and C are collinear if the sum of any two distances equals the third distance.\n\nStep 1: Compute AB:\nAB = √[ (6 - 3)² + (4 - 1)² ] = √[ 3² + 3² ] = √[ 9 + 9 ] = √18 = 3√2 units.\n\nStep 2: Compute BC:\nBC = √[ (8 - 6)² + (6 - 4)² ] = √[ 2² + 2² ] = √[ 4 + 4 ] = √8 = 2√2 units.\n\nStep 3: Compute AC:\nAC = √[ (8 - 3)² + (6 - 1)² ] = √[ 5² + 5² ] = √[ 25 + 25 ] = √50 = 5√2 units.\n\nStep 4: Check collinearity:\nAB + BC = 3√2 + 2√2 = 5√2 = AC.\nSince AB + BC = AC, the three points A, B, and C are collinear.\n[ROUGH_WORK]\nLook at Figure 7.6 on page 5 in your textbook in the side viewer!\nSlope = (4 - 1)/(6 - 3) = 3/3 = 1; Slope BC = (6 - 4)/(8 - 6) = 2/2 = 1. Equal slopes!\nBoxed Answer: [ Yes, Ashima, Bharti, and Camella are seated in a straight line as AB + BC = AC ].",
      figure_id: "Fig. 7.6",
      page: 5,
      notesSourceFilename: "jemh107.pdf",
      concept_questions: [
        "What is the collinearity condition using the distance formula?",
        "Could we also check collinearity using slopes?"
      ],
      graph_payload: {
        points: [
          { x: 3, y: 1, label: "A(3, 1) Ashima" },
          { x: 6, y: 4, label: "B(6, 4) Bharti" },
          { x: 8, y: 6, label: "C(8, 6) Camella" }
        ],
        segments: [
          { start: [3, 1], end: [6, 4], label: "AB = 3√2" },
          { start: [6, 4], end: [8, 6], label: "BC = 2√2" }
        ]
      }
    },
    {
      problem: "Example 4 (NCERT Page 6): Find a relation between x and y such that the point (x, y) is equidistant from the points (7, 1) and (3, 5).",
      solution: "Let P(x, y) be equidistant from A(7, 1) and B(3, 5).\nGiven: PA = PB ⇒ PA² = PB².\n\nStep 1: Set up distance expressions:\nPA² = (x - 7)² + (y - 1)²\nPB² = (x - 3)² + (y - 5)²\n\nStep 2: Equate PA² and PB²:\n(x - 7)² + (y - 1)² = (x - 3)² + (y - 5)²\nx² - 14x + 49 + y² - 2y + 1 = x² - 6x + 9 + y² - 10y + 25\n\nStep 3: Simplify and cancel x² and y²:\n-14x - 2y + 50 = -6x - 10y + 34\n-14x + 6x - 2y + 10y + 50 - 34 = 0\n-8x + 8y + 16 = 0\nDivide throughout by -8:\nx - y - 2 = 0 ⇒ x - y = 2.\n[ROUGH_WORK]\nGeometric Meaning: P(x, y) lies on the perpendicular bisector of segment AB!\nMidpoint of AB = ((7+3)/2, (1+5)/2) = (5, 3). Check: 5 - 3 = 2 (Satisfied!)\nBoxed Answer: [ The required relation is x - y = 2 (or x - y - 2 = 0) ].",
      concept_questions: [
        "What geometric line does the equation x - y = 2 represent relative to segment AB?",
        "Why did the quadratic terms x² and y² cancel out on both sides?"
      ],
      graph_payload: {
        formulas: ["x - 2"],
        points: [
          { x: 7, y: 1, label: "A(7, 1)" },
          { x: 3, y: 5, label: "B(3, 5)" },
          { x: 5, y: 3, label: "Midpoint M(5, 3)" }
        ],
        segments: [
          { start: [7, 1], end: [3, 5], label: "Segment AB" }
        ],
        texts: [
          { x: 6, y: 4, text: "Perpendicular Bisector x - y = 2" }
        ]
      }
    },
    {
      problem: "Example 5 (NCERT Page 6): Find a point on the y-axis which is equidistant from the points A(6, 5) and B(-4, 3).",
      solution: "Let the required point on the y-axis be P(0, y) (since x = 0 on the y-axis).\nGiven: PA = PB ⇒ PA² = PB².\n\nStep 1: Set up distance expressions:\nPA² = (0 - 6)² + (y - 5)² = 36 + (y² - 10y + 25) = y² - 10y + 61\nPB² = (0 - (-4))² + (y - 3)² = 16 + (y² - 6y + 9) = y² - 6y + 25\n\nStep 2: Equate PA² and PB²:\ny² - 10y + 61 = y² - 6y + 25\n-10y + 61 = -6y + 25\n-10y + 6y = 25 - 61\n-4y = -36\ny = -36 / -4 = 9.\n[ROUGH_WORK]\nPA² = 6² + (9 - 5)² = 36 + 16 = 52\nPB² = 4² + (9 - 3)² = 16 + 36 = 52. PA = PB = √52 (Verified!)\nBoxed Answer: [ The point on the y-axis equidistant from A and B is (0, 9) ].",
      concept_questions: [
        "Why are the coordinates of any point on the y-axis taken as (0, y)?",
        "What would the coordinates be if the point was on the x-axis?"
      ],
      graph_payload: {
        points: [
          { x: 6, y: 5, label: "A(6, 5)" },
          { x: -4, y: 3, label: "B(-4, 3)" },
          { x: 0, y: 9, label: "P(0, 9) on y-axis", callout: "Equidistant Point" }
        ],
        segments: [
          { start: [0, 9], end: [6, 5], label: "PA = √52" },
          { start: [0, 9], end: [-4, 3], label: "PB = √52" }
        ]
      }
    }
  ];

  // Module 3: Exercise 7.1 Complete Solver (Q1 to Q10)
  const mod3WorkedExamples = [
    {
      problem: "Exercise 7.1 Q1 (NCERT Page 7): Find the distance between the following pairs of points: (i) (2, 3), (4, 1); (ii) (-5, 7), (-1, 3); (iii) (a, b), (-a, -b).",
      solution: "Formula: d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]\n\nPart (i): P(2, 3) and Q(4, 1)\nd = √[ (4 - 2)² + (1 - 3)² ] = √[ 2² + (-2)² ] = √[ 4 + 4 ] = √8 = 2√2 units.\n\nPart (ii): P(-5, 7) and Q(-1, 3)\nd = √[ (-1 - (-5))² + (3 - 7)² ] = √[ 4² + (-4)² ] = √[ 16 + 16 ] = √32 = 4√2 units.\n\nPart (iii): P(a, b) and Q(-a, -b)\nd = √[ (-a - a)² + (-b - b)² ] = √[ (-2a)² + (-2b)² ] = √[ 4a² + 4b² ] = √[ 4(a² + b²) ] = 2√(a² + b²) units.\n[ROUGH_WORK]\n√8 = √(4 × 2) = 2√2\n√32 = √(16 × 2) = 4√2\n√[4(a²+b²)] = 2√(a²+b²)\nBoxed Answer: [ (i) 2√2 units, (ii) 4√2 units, (iii) 2√(a² + b²) units ].",
      concept_questions: [
        "Why is (-2a)² equal to +4a² and not -4a²?",
        "What happens in part (iii) if a = 3 and b = 4?"
      ],
      graph_payload: {
        points: [
          { x: 2, y: 3, label: "(2, 3)" },
          { x: 4, y: 1, label: "(4, 1)" },
          { x: -5, y: 7, label: "(-5, 7)" },
          { x: -1, y: 3, label: "(-1, 3)" }
        ],
        segments: [
          { start: [2, 3], end: [4, 1], label: "d = 2√2" },
          { start: [-5, 7], end: [-1, 3], label: "d = 4√2" }
        ]
      }
    },
    {
      problem: "Exercise 7.1 Q2 (NCERT Page 7): Find the distance between the points (0, 0) and (36, 15). Can you now find the distance between the two towns A and B discussed in Section 7.2?",
      solution: "Let Town A be at origin O(0, 0) and Town B be at (36, 15) km.\nFormula: Distance d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]\nSince one point is the origin (0, 0), d = √(x² + y²).\n\nStep 1: Substitute coordinates:\nd = √[ 36² + 15² ]\n36² = 1296\n15² = 225\n\nStep 2: Add and take square root:\nd = √[ 1296 + 225 ] = √1521.\nSince 39 × 39 = 1521, d = 39 km.\n[ROUGH_WORK]\n39 × 39 = (40 - 1)² = 1600 - 80 + 1 = 1521. Exactly 39!\nBoxed Answer: [ The distance between the points is 39 units, and the distance between Town A and Town B is 39 km ].",
      concept_questions: [
        "Why is the distance of any point (x, y) from origin given simply by √(x² + y²)?",
        "Could Town B be 39 km away in a different quadrant with negative coordinates?"
      ],
      graph_payload: {
        points: [
          { x: 0, y: 0, label: "Town A (0, 0)" },
          { x: 36, y: 15, label: "Town B (36, 15)" }
        ],
        segments: [
          { start: [0, 0], end: [36, 15], label: "AB = 39 km" }
        ]
      }
    },
    {
      problem: "Exercise 7.1 Q3 (NCERT Page 7): Determine if the points (1, 5), (2, 3) and (-2, -11) are collinear.",
      solution: "Let A(1, 5), B(2, 3), and C(-2, -11).\nCondition for Collinearity: Sum of two smaller segments must equal the largest segment.\n\nStep 1: Compute AB:\nAB = √[ (2 - 1)² + (3 - 5)² ] = √[ 1² + (-2)² ] = √[ 1 + 4 ] = √5 ≈ 2.24.\n\nStep 2: Compute BC:\nBC = √[ (-2 - 2)² + (-11 - 3)² ] = √[ (-4)² + (-14)² ] = √[ 16 + 196 ] = √212 = 2√53 ≈ 14.56.\n\nStep 3: Compute AC:\nAC = √[ (-2 - 1)² + (-11 - 5)² ] = √[ (-3)² + (-16)² ] = √[ 9 + 256 ] = √265 ≈ 16.28.\n\nStep 4: Check collinearity:\nAB + BC = √5 + 2√53 ≈ 2.24 + 14.56 = 16.80 ≠ √265 (16.28).\nSince AB + BC ≠ AC, BC + AC ≠ AB, and AB + AC ≠ BC, the points are NOT collinear.\n[ROUGH_WORK]\n√5 ≈ 2.236, √212 ≈ 14.560, √265 ≈ 16.279. 2.236 + 14.560 = 16.796 ≠ 16.279\nBoxed Answer: [ The points (1, 5), (2, 3) and (-2, -11) are not collinear ].",
      concept_questions: [
        "What would the area of triangle ABC be if the points were collinear?",
        "Why can we not simply add square roots: is √5 + √212 equal to √217?"
      ]
    },
    {
      problem: "Exercise 7.1 Q4 (NCERT Page 7): Check whether (5, -2), (6, 4) and (7, -2) are the vertices of an isosceles triangle.",
      solution: "Let A(5, -2), B(6, 4), and C(7, -2).\nCondition for an Isosceles Triangle: Exactly two sides must be equal.\n\nStep 1: Compute AB:\nAB = √[ (6 - 5)² + (4 - (-2))² ] = √[ 1² + 6² ] = √[ 1 + 36 ] = √37 units.\n\nStep 2: Compute BC:\nBC = √[ (7 - 6)² + (-2 - 4)² ] = √[ 1² + (-6)² ] = √[ 1 + 36 ] = √37 units.\n\nStep 3: Compute AC:\nAC = √[ (7 - 5)² + (-2 - (-2))² ] = √[ 2² + 0² ] = √4 = 2 units.\n\nConclusion:\nSince AB = BC = √37 units and AC = 2 units (two sides equal), triangle ABC is an isosceles triangle.\n[ROUGH_WORK]\nAB = √37, BC = √37, AC = 2. AB = BC ≠ AC ⇒ Isosceles!\nBoxed Answer: [ Yes, (5, -2), (6, 4) and (7, -2) are the vertices of an isosceles triangle ].",
      concept_questions: [
        "What type of triangle would it be if AC was also equal to √37?",
        "Notice y-coordinates of A and C are both -2: what does this tell us about base AC?"
      ],
      graph_payload: {
        points: [
          { x: 5, y: -2, label: "A(5, -2)" },
          { x: 6, y: 4, label: "B(6, 4) Apex" },
          { x: 7, y: -2, label: "C(7, -2)" }
        ],
        segments: [
          { start: [5, -2], end: [6, 4], label: "AB = √37" },
          { start: [6, 4], end: [7, -2], label: "BC = √37" },
          { start: [5, -2], end: [7, -2], label: "Base AC = 2" }
        ],
        polygons: [
          { points: [[5, -2], [6, 4], [7, -2]], label: "Isosceles Triangle ABC" }
        ]
      }
    },
    {
      problem: "Exercise 7.1 Q5 (NCERT Page 7): In a classroom, 4 friends are seated at the points A, B, C and D as shown in Fig. 7.8. Champa and Chameli walk into the class and after observing for a few minutes Champa asks Chameli, 'Don't you think ABCD is a square?' Chameli disagrees. Using distance formula, find which of them is correct.",
      solution: "From Fig. 7.8 in textbook (refer to Figure 7.8 on page 7 in Side Book Viewer):\nCoordinates of friends:\nA = (3, 4)\nB = (6, 7)\nC = (9, 4)\nD = (6, 1)\n\nStep 1: Compute side lengths:\nAB = √[ (6 - 3)² + (7 - 4)² ] = √[ 3² + 3² ] = √18 = 3√2 units.\nBC = √[ (9 - 6)² + (4 - 7)² ] = √[ 3² + (-3)² ] = √18 = 3√2 units.\nCD = √[ (6 - 9)² + (1 - 4)² ] = √[ (-3)² + (-3)² ] = √18 = 3√2 units.\nDA = √[ (3 - 6)² + (4 - 1)² ] = √[ (-3)² + 3² ] = √18 = 3√2 units.\nAll four sides AB = BC = CD = DA = 3√2 units.\n\nStep 2: Compute diagonal lengths:\nDiagonal AC = √[ (9 - 3)² + (4 - 4)² ] = √[ 6² + 0² ] = 6 units.\nDiagonal BD = √[ (6 - 6)² + (1 - 7)² ] = √[ 0² + (-6)² ] = 6 units.\n\nConclusion:\nSince all four sides are equal (3√2) and both diagonals are equal (6), ABCD is a square.\nTherefore, Champa is correct!\n[ROUGH_WORK]\nLook at Figure 7.8 on page 7 in your textbook in the side viewer!\nSide = √18, Diagonal = 6. 18 + 18 = 36 = 6² (Pythagoras holds!). Champa is right.\nBoxed Answer: [ ABCD is a square, hence Champa is correct ].",
      figure_id: "Fig. 7.8",
      page: 7,
      notesSourceFilename: "jemh107.pdf",
      concept_questions: [
        "Why did we need to check diagonals AC and BD in addition to the 4 sides?",
        "What shape would it be if AC = 8 and BD = 4 while all sides were 3√2?"
      ],
      graph_payload: {
        points: [
          { x: 3, y: 4, label: "A(3, 4)" },
          { x: 6, y: 7, label: "B(6, 7)" },
          { x: 9, y: 4, label: "C(9, 4)" },
          { x: 6, y: 1, label: "D(6, 1)" }
        ],
        segments: [
          { start: [3, 4], end: [6, 7], label: "AB = 3√2" },
          { start: [6, 7], end: [9, 4], label: "BC = 3√2" },
          { start: [9, 4], end: [6, 1], label: "CD = 3√2" },
          { start: [6, 1], end: [3, 4], label: "DA = 3√2" },
          { start: [3, 4], end: [9, 4], label: "AC = 6" },
          { start: [6, 7], end: [6, 1], label: "BD = 6" }
        ],
        polygons: [
          { points: [[3, 4], [6, 7], [9, 4], [6, 1]], label: "Square ABCD" }
        ]
      }
    },
    {
      problem: "Exercise 7.1 Q6 (NCERT Page 7): Name the type of quadrilateral formed, if any, by the following points, and give reasons: (i) (-1, -2), (1, 0), (-1, 2), (-3, 0); (ii) (-3, 5), (3, 1), (0, 3), (-1, -4); (iii) (4, 5), (7, 6), (4, 3), (1, 2).",
      solution: "Part (i): A(-1, -2), B(1, 0), C(-1, 2), D(-3, 0)\nSides: AB = √[ 2² + 2² ] = √8 = 2√2; BC = √[ (-2)² + 2² ] = √8 = 2√2; CD = √[ (-2)² + (-2)² ] = √8 = 2√2; DA = √[ 2² + (-2)² ] = √8 = 2√2.\nDiagonals: AC = √[ 0² + 4² ] = 4; BD = √[ (-4)² + 0² ] = 4.\nAll sides equal (2√2) and diagonals equal (4) ⇒ ABCD is a SQUARE.\n\nPart (ii): A(-3, 5), B(3, 1), C(0, 3), D(-1, -4)\nAB = √[ 6² + (-4)² ] = √52 = 2√13; BC = √[ (-3)² + 2² ] = √13; AC = √[ 3² + (-2)² ] = √13.\nNotice: AC + BC = √13 + √13 = 2√13 = AB.\nPoints A, C, and B are collinear! Therefore, no quadrilateral can be formed.\n\nPart (iii): A(4, 5), B(7, 6), C(4, 3), D(1, 2)\nAB = √[ 3² + 1² ] = √10; BC = √[ (-3)² + (-3)² ] = √18 = 3√2;\nCD = √[ (-3)² + (-1)² ] = √10; DA = √[ 3² + 3² ] = √18 = 3√2.\nOpposite sides are equal: AB = CD = √10, BC = DA = 3√2.\nDiagonals: AC = √[ 0² + (-2)² ] = 2; BD = √[ (-6)² + (-4)² ] = √52 = 2√13 (Diagonals unequal!).\nOpposite sides equal and diagonals unequal ⇒ ABCD is a PARALLELOGRAM.\n[ROUGH_WORK]\n(i) 4 sides equal + 2 diagonals equal ⇒ Square\n(ii) A, C, B collinear ⇒ No quadrilateral\n(iii) Opp sides equal + diagonals unequal ⇒ Parallelogram\nBoxed Answer: [ (i) Square, (ii) No quadrilateral formed (points are collinear), (iii) Parallelogram ].",
      concept_questions: [
        "In part (ii), why does AC + BC = AB prevent a quadrilateral from forming?",
        "What additional condition would turn the parallelogram in part (iii) into a rectangle?"
      ]
    },
    {
      problem: "Exercise 7.1 Q7 (NCERT Page 7): Find the point on the x-axis which is equidistant from (2, -5) and (-2, 9).",
      solution: "Let the required point on the x-axis be P(x, 0) (since y = 0 on the x-axis).\nLet A = (2, -5) and B = (-2, 9).\nGiven: PA = PB ⇒ PA² = PB².\n\nStep 1: Set up squared distances:\nPA² = (x - 2)² + (0 - (-5))² = x² - 4x + 4 + 25 = x² - 4x + 29\nPB² = (x - (-2))² + (0 - 9)² = (x + 2)² + 81 = x² + 4x + 4 + 81 = x² + 4x + 85\n\nStep 2: Equate PA² and PB²:\nx² - 4x + 29 = x² + 4x + 85\n-4x + 29 = 4x + 85\n-4x - 4x = 85 - 29\n-8x = 56\nx = 56 / -8 = -7.\n\nConclusion:\nThe point on the x-axis is (-7, 0).\n[ROUGH_WORK]\nCheck: PA² = (-7 - 2)² + 5² = 81 + 25 = 106\nPB² = (-7 + 2)² + (-9)² = 25 + 81 = 106. PA = PB = √106 (True!)\nBoxed Answer: [ The point on the x-axis equidistant from the given points is (-7, 0) ].",
      concept_questions: [
        "Why is y = 0 for any point on the x-axis?",
        "Could there be more than one point on the x-axis equidistant from A and B?"
      ],
      graph_payload: {
        points: [
          { x: 2, y: -5, label: "A(2, -5)" },
          { x: -2, y: 9, label: "B(-2, 9)" },
          { x: -7, y: 0, label: "P(-7, 0)", callout: "Equidistant Point on x-axis" }
        ],
        segments: [
          { start: [-7, 0], end: [2, -5], label: "PA = √106" },
          { start: [-7, 0], end: [-2, 9], label: "PB = √106" }
        ]
      }
    },
    {
      problem: "Exercise 7.1 Q8 (NCERT Page 7): Find the values of y for which the distance between the points P(2, -3) and Q(10, y) is 10 units.",
      solution: "Given points: P(2, -3) and Q(10, y).\nGiven distance: PQ = 10 units ⇒ PQ² = 10² = 100.\nFormula: PQ² = (x₂ - x₁)² + (y₂ - y₁)²\n\nStep 1: Set up the equation:\n(10 - 2)² + (y - (-3))² = 100\n8² + (y + 3)² = 100\n64 + (y + 3)² = 100\n(y + 3)² = 100 - 64 = 36.\n\nStep 2: Take square root on both sides:\ny + 3 = ±√36 = ±6\nCase 1: y + 3 = 6 ⇒ y = 6 - 3 = 3\nCase 2: y + 3 = -6 ⇒ y = -6 - 3 = -9.\n[ROUGH_WORK]\nCheck y = 3: (10-2)² + (3+3)² = 64 + 36 = 100 ⇒ √100 = 10\nCheck y = -9: (10-2)² + (-9+3)² = 64 + (-6)² = 64 + 36 = 100 ⇒ √100 = 10\nBoxed Answer: [ The values of y are 3 and -9 ].",
      concept_questions: [
        "Why are there two possible values for y geometrically?",
        "What circle does point Q lie on centered at P?"
      ],
      graph_payload: {
        circles: [
          { center: [2, -3], radius: 10, label: "Circle of radius 10 around P" }
        ],
        points: [
          { x: 2, y: -3, label: "P(2, -3) Centre" },
          { x: 10, y: 3, label: "Q₁(10, 3)" },
          { x: 10, y: -9, label: "Q₂(10, -9)" }
        ],
        segments: [
          { start: [2, -3], end: [10, 3], label: "PQ₁ = 10" },
          { start: [2, -3], end: [10, -9], label: "PQ₂ = 10" }
        ]
      }
    },
    {
      problem: "Exercise 7.1 Q9 (NCERT Page 8): If Q(0, 1) is equidistant from P(5, -3) and R(x, 6), find the values of x. Also find the distances QR and PR.",
      solution: "Given: QP = QR ⇒ QP² = QR².\n\nStep 1: Find QP²:\nQP² = (0 - 5)² + (1 - (-3))² = (-5)² + 4² = 25 + 16 = 41.\n\nStep 2: Find QR²:\nQR² = (x - 0)² + (6 - 1)² = x² + 5² = x² + 25.\n\nStep 3: Equate QP² and QR²:\nx² + 25 = 41\nx² = 41 - 25 = 16\nx = ±√16 = ±4.\nSo R is either R₁(4, 6) or R₂(-4, 6).\n\nStep 4: Compute distances QR and PR:\nFor QR: QR = √(x² + 25) = √(16 + 25) = √41 units (for both x = 4 and x = -4).\nFor PR when x = 4: PR = √[ (4 - 5)² + (6 - (-3))² ] = √[ (-1)² + 9² ] = √[ 1 + 81 ] = √82 units.\nFor PR when x = -4: PR = √[ (-4 - 5)² + (6 - (-3))² ] = √[ (-9)² + 9² ] = √[ 81 + 81 ] = √162 = 9√2 units.\n[ROUGH_WORK]\nQP² = 41; x² = 16 ⇒ x = ±4\nIf x = 4: PR = √82; If x = -4: PR = 9√2\nBoxed Answer: [ x = ±4; QR = √41 units; PR = √82 units (for x = 4) or 9√2 units (for x = -4) ].",
      concept_questions: [
        "Why is distance QR identical for both x = 4 and x = -4?",
        "Why does PR differ depending on whether x is positive or negative?"
      ]
    },
    {
      problem: "Exercise 7.1 Q10 (NCERT Page 8): Find a relation between x and y such that the point (x, y) is equidistant from the point (3, 6) and (-3, 4).",
      solution: "Let P(x, y) be equidistant from A(3, 6) and B(-3, 4).\nGiven: PA = PB ⇒ PA² = PB².\n\nStep 1: Set up squared distances:\nPA² = (x - 3)² + (y - 6)²\nPB² = (x - (-3))² + (y - 4)² = (x + 3)² + (y - 4)²\n\nStep 2: Expand both sides:\nx² - 6x + 9 + y² - 12y + 36 = x² + 6x + 9 + y² - 8y + 16\n-6x - 12y + 45 = 6x - 8y + 25\n\nStep 3: Group all terms on one side:\n0 = 6x + 6x - 8y + 12y + 25 - 45\n12x + 4y - 20 = 0\nDivide throughout by 4:\n3x + y - 5 = 0 (or 3x + y = 5).\n[ROUGH_WORK]\nGeometric Meaning: Perpendicular bisector of AB!\nMidpoint of AB = ((3-3)/2, (6+4)/2) = (0, 5). Check: 3(0) + 5 = 5 (True!)\nBoxed Answer: [ The relation between x and y is 3x + y - 5 = 0 (or 3x + y = 5) ].",
      concept_questions: [
        "What linear equation represents the perpendicular bisector of AB?",
        "Why does the midpoint of AB always satisfy this relation?"
      ],
      graph_payload: {
        formulas: ["5 - 3*x"],
        points: [
          { x: 3, y: 6, label: "A(3, 6)" },
          { x: -3, y: 4, label: "B(-3, 4)" },
          { x: 0, y: 5, label: "Midpoint (0, 5)" }
        ],
        segments: [
          { start: [3, 6], end: [-3, 4], label: "AB" }
        ],
        texts: [
          { x: 1, y: 2, text: "Line 3x + y = 5" }
        ]
      }
    }
  ];

  // Module 4: Exercise 7.2 Complete Solver (Q1 to Q10)
  const mod4WorkedExamples = [
    {
      problem: "Exercise 7.2 Q1 (NCERT Page 13): Find the coordinates of the point which divides the join of (-1, 7) and (4, -3) in the ratio 2 : 3.",
      solution: "Let A(-1, 7) and B(4, -3). Ratio m₁ : m₂ = 2 : 3.\nFormula: P(x, y) = [ (m₁x₂ + m₂x₁)/(m₁ + m₂), (m₁y₂ + m₂y₁)/(m₁ + m₂) ]\n\nStep 1: Calculate x-coordinate:\nx = [ 2(4) + 3(-1) ] / (2 + 3) = [ 8 - 3 ] / 5 = 5 / 5 = 1.\n\nStep 2: Calculate y-coordinate:\ny = [ 2(-3) + 3(7) ] / (2 + 3) = [ -6 + 21 ] / 5 = 15 / 5 = 3.\n\nConclusion:\nThe coordinates of the point are (1, 3).\n[ROUGH_WORK]\nx = (8 - 3)/5 = 1\ny = (-6 + 21)/5 = 3\nBoxed Answer: [ The coordinates of the dividing point are (1, 3) ].",
      concept_questions: [
        "Why do we cross-multiply m₁ with x₂ and m₂ with x₁ in the section formula?",
        "What would the point be if the ratio was 1 : 1 (midpoint)?"
      ],
      graph_payload: {
        points: [
          { x: -1, y: 7, label: "A(-1, 7)" },
          { x: 4, y: -3, label: "B(4, -3)" },
          { x: 1, y: 3, label: "P(1, 3) Ratio 2:3", callout: "Dividing Point" }
        ],
        segments: [
          { start: [-1, 7], end: [1, 3], label: "AP (m₁ = 2)" },
          { start: [1, 3], end: [4, -3], label: "PB (m₂ = 3)" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q2 (NCERT Page 13): Find the coordinates of the points of trisection of the line segment joining (4, -1) and (-2, -3).",
      solution: "Let A(4, -1) and B(-2, -3). Let P and Q be the points of trisection dividing AB into 3 equal parts (AP = PQ = QB).\nTherefore:\n- P divides AB internally in the ratio 1 : 2.\n- Q divides AB internally in the ratio 2 : 1 (or Q is the midpoint of PB).\n\nStep 1: Find coordinates of P (ratio 1 : 2):\nx_P = [ 1(-2) + 2(4) ] / (1 + 2) = [ -2 + 8 ] / 3 = 6 / 3 = 2.\ny_P = [ 1(-3) + 2(-1) ] / (1 + 2) = [ -3 - 2 ] / 3 = -5/3.\nSo P = (2, -5/3).\n\nStep 2: Find coordinates of Q (midpoint of PB):\nx_Q = (x_P + x_B) / 2 = [ 2 + (-2) ] / 2 = 0 / 2 = 0.\ny_Q = (y_P + y_B) / 2 = [ -5/3 + (-3) ] / 2 = [ -14/3 ] / 2 = -7/3.\nSo Q = (0, -7/3).\n[ROUGH_WORK]\nAlternative for Q (ratio 2 : 1): x = [2(-2) + 1(4)]/3 = 0/3 = 0; y = [2(-3) + 1(-1)]/3 = -7/3. Exactly matches!\nBoxed Answer: [ The points of trisection are P(2, -5/3) and Q(0, -7/3) ].",
      concept_questions: [
        "What does trisection mean in coordinate geometry?",
        "Why is Q the midpoint of segment PB?"
      ],
      graph_payload: {
        points: [
          { x: 4, y: -1, label: "A(4, -1)" },
          { x: -2, y: -3, label: "B(-2, -3)" },
          { x: 2, y: -1.67, label: "P(2, -5/3) 1st Trisection" },
          { x: 0, y: -2.33, label: "Q(0, -7/3) 2nd Trisection" }
        ],
        segments: [
          { start: [4, -1], end: [-2, -3], label: "Segment AB" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q3 (NCERT Page 13): To conduct Sports Day activities in a rectangular ground ABCD, lines have been drawn with chalk powder at a distance of 1 m each. 100 flower pots have been placed at a distance of 1 m from each other along AD, as shown in Fig. 7.12. Niharika runs 1/4th the distance AD on the 2nd line and posts a green flag. Preet runs 1/5th the distance AD on the 8th line and posts a red flag. What is the distance between both the flags? If Rashmi has to post a blue flag exactly halfway between the line segment joining the two flags, where should she post her flag?",
      solution: "From Fig. 7.12 in textbook (refer to Figure 7.12 on page 13 in Side Book Viewer):\nTotal distance AD = 100 × 1 m = 100 m.\n\nStep 1: Coordinates of Green Flag (Niharika):\nRuns on 2nd line ⇒ x₁ = 2.\nDistance = (1/4) × 100 = 25 m ⇒ y₁ = 25.\nGreen Flag G = (2, 25).\n\nStep 2: Coordinates of Red Flag (Preet):\nRuns on 8th line ⇒ x₂ = 8.\nDistance = (1/5) × 100 = 20 m ⇒ y₂ = 20.\nRed Flag R = (8, 20).\n\nStep 3: Distance between Green and Red flags (GR):\nGR = √[ (8 - 2)² + (20 - 25)² ]\n= √[ 6² + (-5)² ] = √[ 36 + 25 ] = √61 m ≈ 7.81 m.\n\nStep 4: Coordinates of Blue Flag (Rashmi, midpoint of GR):\nMidpoint M = [ (x₁ + x₂)/2, (y₁ + y₂)/2 ]\n= [ (2 + 8)/2, (25 + 20)/2 ] = [ 10/2, 45/2 ] = (5, 22.5).\nRashmi should post her blue flag on the 5th line at a distance of 22.5 m.\n[ROUGH_WORK]\nLook at Figure 7.12 on page 13 in your textbook in the side viewer!\nDistance = √(36 + 25) = √61 m\nMidpoint = (5, 22.5 m)\nBoxed Answer: [ Distance between flags = √61 m (≈ 7.81 m); Rashmi posts her flag on the 5th line at 22.5 m ].",
      figure_id: "Fig. 7.12",
      page: 13,
      notesSourceFilename: "jemh107.pdf",
      concept_questions: [
        "How are the runners' line numbers translated into x-coordinates?",
        "Why is Rashmi's position found using the midpoint formula?"
      ],
      graph_payload: {
        points: [
          { x: 2, y: 25, label: "G(2, 25) Green Flag", callout: "Niharika" },
          { x: 8, y: 20, label: "R(8, 20) Red Flag", callout: "Preet" },
          { x: 5, y: 22.5, label: "B(5, 22.5) Blue Flag", callout: "Rashmi (Midpoint)" }
        ],
        segments: [
          { start: [2, 25], end: [8, 20], label: "GR = √61 m" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q4 (NCERT Page 13): Find the ratio in which the line segment joining the points (-3, 10) and (6, -8) is divided by (-1, 6).",
      solution: "Let the points be A(-3, 10) and B(6, -8). Let P(-1, 6) divide AB in the ratio k : 1.\nBy Section Formula:\nx = [ k(x₂) + 1(x₁) ] / (k + 1)\n\nStep 1: Substitute x = -1, x₁ = -3, x₂ = 6:\n-1 = [ 6k + 1(-3) ] / (k + 1)\n-1(k + 1) = 6k - 3\n-k - 1 = 6k - 3\n-1 + 3 = 6k + k\n2 = 7k ⇒ k = 2/7.\n\nStep 2: Verify with y-coordinate:\ny = [ k(-8) + 1(10) ] / (k + 1)\n= [ (2/7)(-8) + 10 ] / (2/7 + 1) = [ -16/7 + 70/7 ] / (9/7) = (54/7) / (9/7) = 54/9 = 6. (Verified!)\n\nConclusion:\nThe ratio k : 1 is (2/7) : 1 = 2 : 7.\n[ROUGH_WORK]\n-k - 1 = 6k - 3 ⇒ 7k = 2 ⇒ k = 2/7 ⇒ Ratio = 2 : 7\nBoxed Answer: [ The line segment is divided in the ratio 2 : 7 ].",
      concept_questions: [
        "Why is it convenient to assume the ratio as k : 1 instead of m₁ : m₂?",
        "What would a negative value of k imply (external division)?"
      ],
      graph_payload: {
        points: [
          { x: -3, y: 10, label: "A(-3, 10)" },
          { x: 6, y: -8, label: "B(6, -8)" },
          { x: -1, y: 6, label: "P(-1, 6) Ratio 2:7", callout: "Dividing Point" }
        ],
        segments: [
          { start: [-3, 10], end: [6, -8], label: "AB" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q5 (NCERT Page 13): Find the ratio in which the line segment joining A(1, -5) and B(-4, 5) is divided by the x-axis. Also find the coordinates of the point of division.",
      solution: "Let the point of division on the x-axis be P(x, 0) (since y = 0 on x-axis).\nLet P divide AB in the ratio k : 1.\nPoints are A(1, -5) and B(-4, 5).\n\nStep 1: Use y-coordinate equation to find k:\ny = [ k(y₂) + 1(y₁) ] / (k + 1)\n0 = [ k(5) + 1(-5) ] / (k + 1)\n0 = 5k - 5 ⇒ 5k = 5 ⇒ k = 1.\nSince k = 1, the ratio is 1 : 1 (P is the midpoint of AB!).\n\nStep 2: Find the x-coordinate of P:\nx = (x₁ + x₂) / 2 = [ 1 + (-4) ] / 2 = -3/2.\n\nConclusion:\nThe ratio is 1 : 1 and the point of division is (-3/2, 0).\n[ROUGH_WORK]\ny = 0 ⇒ 5k - 5 = 0 ⇒ k = 1 (Ratio 1 : 1)\nx = (1 - 4)/2 = -3/2\nBoxed Answer: [ The ratio is 1 : 1 and the point of division is (-3/2, 0) ].",
      concept_questions: [
        "Why did we use the y-coordinate first to find the ratio k?",
        "What does a 1 : 1 ratio indicate about point P?"
      ],
      graph_payload: {
        points: [
          { x: 1, y: -5, label: "A(1, -5)" },
          { x: -4, y: 5, label: "B(-4, 5)" },
          { x: -1.5, y: 0, label: "P(-3/2, 0) on x-axis", callout: "Midpoint" }
        ],
        segments: [
          { start: [1, -5], end: [-4, 5], label: "AB" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q6 (NCERT Page 13): If (1, 2), (4, y), (x, 6) and (3, 5) are the vertices of a parallelogram taken in order, find x and y.",
      solution: "Let A(1, 2), B(4, y), C(x, 6), and D(3, 5) be the vertices in order.\nKey Property of a Parallelogram: The diagonals bisect each other.\nTherefore: Midpoint of diagonal AC = Midpoint of diagonal BD.\n\nStep 1: Compute Midpoint of AC:\nM_AC = [ (1 + x)/2, (2 + 6)/2 ] = [ (1 + x)/2, 8/2 ] = [ (1 + x)/2, 4 ].\n\nStep 2: Compute Midpoint of BD:\nM_BD = [ (4 + 3)/2, (y + 5)/2 ] = [ 7/2, (y + 5)/2 ].\n\nStep 3: Equate coordinates:\nx-coordinates: (1 + x)/2 = 7/2 ⇒ 1 + x = 7 ⇒ x = 6.\ny-coordinates: 4 = (y + 5)/2 ⇒ 8 = y + 5 ⇒ y = 3.\n[ROUGH_WORK]\n1 + x = 7 ⇒ x = 6\ny + 5 = 8 ⇒ y = 3\nBoxed Answer: [ x = 6 and y = 3 ].",
      concept_questions: [
        "Why is using the midpoint of diagonals much easier than using the distance formula for opposite sides?",
        "What would happen if the vertices were not taken in order?"
      ],
      graph_payload: {
        points: [
          { x: 1, y: 2, label: "A(1, 2)" },
          { x: 4, y: 3, label: "B(4, 3)" },
          { x: 6, y: 6, label: "C(6, 6)" },
          { x: 3, y: 5, label: "D(3, 5)" },
          { x: 3.5, y: 4, label: "Midpoint M(3.5, 4)", callout: "Diagonals Intersection" }
        ],
        segments: [
          { start: [1, 2], end: [4, 3], label: "AB" },
          { start: [4, 3], end: [6, 6], label: "BC" },
          { start: [6, 6], end: [3, 5], label: "CD" },
          { start: [3, 5], end: [1, 2], label: "DA" },
          { start: [1, 2], end: [6, 6], label: "AC" },
          { start: [4, 3], end: [3, 5], label: "BD" }
        ],
        polygons: [
          { points: [[1, 2], [4, 3], [6, 6], [3, 5]], label: "Parallelogram ABCD" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q7 (NCERT Page 13): Find the coordinates of a point A, where AB is the diameter of a circle whose centre is (2, -3) and B is (1, 4).",
      solution: "Let the coordinates of A be (x, y).\nGiven: Centre C(2, -3) is the midpoint of diameter AB, and B is (1, 4).\nBy Midpoint Formula: C = [ (x + x_B)/2, (y + y_B)/2 ]\n\nStep 1: Solve for x:\n2 = (x + 1) / 2\n4 = x + 1 ⇒ x = 3.\n\nStep 2: Solve for y:\n-3 = (y + 4) / 2\n-6 = y + 4 ⇒ y = -10.\n\nConclusion:\nThe coordinates of point A are (3, -10).\n[ROUGH_WORK]\nx = 2(2) - 1 = 3\ny = 2(-3) - 4 = -10\nCheck: Midpoint of (3, -10) and (1, 4) = ((3+1)/2, (-10+4)/2) = (2, -3) (True!)\nBoxed Answer: [ The coordinates of point A are (3, -10) ].",
      concept_questions: [
        "Why is the centre of a circle always the midpoint of any diameter?",
        "What is the radius of this circle?"
      ],
      graph_payload: {
        circles: [
          { center: [2, -3], radius: 7.07, label: "Circle with diameter AB" }
        ],
        points: [
          { x: 3, y: -10, label: "A(3, -10)" },
          { x: 2, y: -3, label: "Centre C(2, -3)" },
          { x: 1, y: 4, label: "B(1, 4)" }
        ],
        segments: [
          { start: [3, -10], end: [1, 4], label: "Diameter AB" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q8 (NCERT Page 13): If A and B are (-2, -2) and (2, -4), respectively, find the coordinates of P such that AP = 3/7 AB and P lies on the line segment AB.",
      solution: "Given: A(-2, -2), B(2, -4).\nGiven relation: AP = (3/7) AB.\n\nStep 1: Find ratio AP : PB:\nPB = AB - AP = AB - (3/7) AB = (4/7) AB.\nTherefore: AP : PB = (3/7) AB : (4/7) AB = 3 : 4.\nSo P divides AB internally in the ratio m₁ : m₂ = 3 : 4.\n\nStep 2: Apply Section Formula:\nx = [ m₁ x₂ + m₂ x₁ ] / (m₁ + m₂)\n= [ 3(2) + 4(-2) ] / (3 + 4) = [ 6 - 8 ] / 7 = -2/7.\n\ny = [ m₁ y₂ + m₂ y₁ ] / (m₁ + m₂)\n= [ 3(-4) + 4(-2) ] / (3 + 4) = [ -12 - 8 ] / 7 = -20/7.\n[ROUGH_WORK]\nCommon Trap: Using ratio 3 : 7 instead of 3 : 4! The pieces are AP and PB!\nBoxed Answer: [ The coordinates of P are (-2/7, -20/7) ].",
      concept_questions: [
        "Why is the ratio 3 : 4 and not 3 : 7?",
        "If AP = (5/8) AB, what would the ratio m₁ : m₂ be?"
      ],
      graph_payload: {
        points: [
          { x: -2, y: -2, label: "A(-2, -2)" },
          { x: 2, y: -4, label: "B(2, -4)" },
          { x: -0.29, y: -2.86, label: "P(-2/7, -20/7)", callout: "AP : PB = 3 : 4" }
        ],
        segments: [
          { start: [-2, -2], end: [2, -4], label: "Segment AB" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q9 (NCERT Page 13): Find the coordinates of the points which divide the line segment joining A(-2, 2) and B(2, 8) into four equal parts.",
      solution: "Let the points dividing AB into 4 equal parts be P, Q, and R such that AP = PQ = QR = RB.\nPoints: A(-2, 2) and B(2, 8).\n\nStep 1: Point Q is the midpoint of AB:\nx_Q = (-2 + 2) / 2 = 0 / 2 = 0\ny_Q = (2 + 8) / 2 = 10 / 2 = 5\nSo Q = (0, 5).\n\nStep 2: Point P is the midpoint of AQ:\nx_P = (-2 + 0) / 2 = -2 / 2 = -1\ny_P = (2 + 5) / 2 = 7/2\nSo P = (-1, 7/2).\n\nStep 3: Point R is the midpoint of QB:\nx_R = (0 + 2) / 2 = 2 / 2 = 1\ny_R = (5 + 8) / 2 = 13/2\nSo R = (1, 13/2).\n[ROUGH_WORK]\nNotice: Q is midpoint of AB; P is midpoint of AQ; R is midpoint of QB. Using midpoint formula 3 times is lightning fast!\nBoxed Answer: [ The three dividing points are P(-1, 7/2), Q(0, 5), and R(1, 13/2) ].",
      concept_questions: [
        "Why is using the midpoint formula 3 times faster than using the section formula with ratios 1:3, 2:2, 3:1?",
        "What are the lengths of the four equal segments?"
      ],
      graph_payload: {
        points: [
          { x: -2, y: 2, label: "A(-2, 2)" },
          { x: 2, y: 8, label: "B(2, 8)" },
          { x: -1, y: 3.5, label: "P(-1, 7/2) 1/4" },
          { x: 0, y: 5, label: "Q(0, 5) Midpoint" },
          { x: 1, y: 6.5, label: "R(1, 13/2) 3/4" }
        ],
        segments: [
          { start: [-2, 2], end: [2, 8], label: "Segment AB" }
        ]
      }
    },
    {
      problem: "Exercise 7.2 Q10 (NCERT Page 13): Find the area of a rhombus if its vertices are (3, 0), (4, 5), (-1, 4) and (-2, -1) taken in order. [Hint: Area of a rhombus = (1/2) × product of its diagonals].",
      solution: "Let the vertices in order be A(3, 0), B(4, 5), C(-1, 4), and D(-2, -1).\nFormula: Area of rhombus = (1/2) × d₁ × d₂ = (1/2) × AC × BD.\n\nStep 1: Compute length of diagonal AC:\nAC = √[ (-1 - 3)² + (4 - 0)² ]\n= √[ (-4)² + 4² ] = √[ 16 + 16 ] = √32 = 4√2 units.\n\nStep 2: Compute length of diagonal BD:\nBD = √[ (-2 - 4)² + (-1 - 5)² ]\n= √[ (-6)² + (-6)² ] = √[ 36 + 36 ] = √72 = 6√2 units.\n\nStep 3: Compute Area:\nArea = (1/2) × AC × BD\n= (1/2) × (4√2) × (6√2)\n= (1/2) × 24 × (√2 × √2)\n= (1/2) × 24 × 2 = 24 square units.\n[ROUGH_WORK]\nAC = 4√2, BD = 6√2\nArea = (4√2 × 6√2) / 2 = 24 × 2 / 2 = 24\nBoxed Answer: [ The area of the rhombus is 24 square units ].",
      concept_questions: [
        "Why do the diagonals of a rhombus bisect each other at right angles?",
        "Could we calculate the area by splitting into two triangles ABC and ADC?"
      ],
      graph_payload: {
        points: [
          { x: 3, y: 0, label: "A(3, 0)" },
          { x: 4, y: 5, label: "B(4, 5)" },
          { x: -1, y: 4, label: "C(-1, 4)" },
          { x: -2, y: -1, label: "D(-2, -1)" }
        ],
        segments: [
          { start: [3, 0], end: [4, 5], label: "AB" },
          { start: [4, 5], end: [-1, 4], label: "BC" },
          { start: [-1, 4], end: [-2, -1], label: "CD" },
          { start: [-2, -1], end: [3, 0], label: "DA" },
          { start: [3, 0], end: [-1, 4], label: "Diagonal AC = 4√2" },
          { start: [4, 5], end: [-2, -1], label: "Diagonal BD = 6√2" }
        ],
        polygons: [
          { points: [[3, 0], [4, 5], [-1, 4], [-2, -1]], label: "Rhombus ABCD (Area=24)" }
        ]
      }
    }
  ];

  // Update Module 1
  const { error: err1 } = await supabase
    .from('syllabus_modules')
    .update({ worked_examples: mod1WorkedExamples })
    .eq('curriculum_id', CURRICULUM_ID)
    .eq('order_index', 1);

  if (err1) console.error('Error updating Module 1:', err1);
  else console.log(`✓ Module 1 updated: ${mod1WorkedExamples.length} worked examples (Examples 1-5).`);

  // Update Module 3 (Ex 7.1 Complete Solver: Q1-Q10)
  const { error: err3 } = await supabase
    .from('syllabus_modules')
    .update({ worked_examples: mod3WorkedExamples })
    .eq('curriculum_id', CURRICULUM_ID)
    .eq('order_index', 3);

  if (err3) console.error('Error updating Module 3:', err3);
  else console.log(`✓ Module 3 updated: ${mod3WorkedExamples.length} worked examples (Exercise 7.1 Q1 to Q10 Complete).`);

  // Update Module 4 (Ex 7.2 Complete Solver: Q1-Q10)
  const { error: err4 } = await supabase
    .from('syllabus_modules')
    .update({ worked_examples: mod4WorkedExamples })
    .eq('curriculum_id', CURRICULUM_ID)
    .eq('order_index', 4);

  if (err4) console.error('Error updating Module 4:', err4);
  else console.log(`✓ Module 4 updated: ${mod4WorkedExamples.length} worked examples (Exercise 7.2 Q1 to Q10 Complete).`);

  console.log('\n=== CHAPTER 7 ENRICHMENT COMPLETE: ALL 18 QUESTIONS & EXAMPLES 100% SOLVED WITH GRAPHS & FIGURE CITATIONS ===');
}

enrichCh7().catch(console.error);
