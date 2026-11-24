const { supabase } = require('./db_helper');

// Master Topper Question Solutions for Class 11 Mathematics Part 2 (Chapters 8 to 14)
const CHAPTERS_PT2 = [
  {
    order_index: 8,
    title: 'Chapter 8: Sequences and Series',
    solvers: [
      {
        module_order: 2, // Exercise 8.1 Solver
        worked_examples: [
          {
            problem: "Exercise 8.1 Q1, Q5 & Q11: (a) Write the first five terms of the sequences whose nth terms are: (i) a_n = n(n + 2), (ii) a_n = (-1)^(n-1) * 5^(n+1). (b) Find the first five terms of the sequence: a_1 = 3, a_n = 3 a_(n-1) + 2 for all n > 1.",
            given: "General term formulas a_n and recurrence relation.",
            formula: "Substitute n = 1, 2, 3, 4, 5 into the general term a_n.",
            substitution: "Calculate terms sequentially.",
            calculation: "Part (a1) a_n = n(n + 2):\n  a_1 = 1(3) = 3; a_2 = 2(4) = 8; a_3 = 3(5) = 15; a_4 = 4(6) = 24; a_5 = 5(7) = 35.\nPart (a2) a_n = (-1)^(n-1) * 5^(n+1):\n  a_1 = (-1)^0 * 5^2 = 25;\n  a_2 = (-1)^1 * 5^3 = -125;\n  a_3 = (-1)^2 * 5^4 = 625;\n  a_4 = (-1)^3 * 5^5 = -3125;\n  a_5 = (-1)^4 * 5^6 = 15625.\nPart (b) Recurrence a_1 = 3, a_n = 3 a_(n-1) + 2:\n  a_1 = 3;\n  a_2 = 3(3) + 2 = 11;\n  a_3 = 3(11) + 2 = 35;\n  a_4 = 3(35) + 2 = 107;\n  a_5 = 3(107) + 2 = 323.",
            finalAnswer: "(a1) 3, 8, 15, 24, 35; (a2) 25, -125, 625, -3125, 15625; (b) 3, 11, 35, 107, 323",
            unit: "sequence terms",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 5, // Exercise 8.2 Solver (GP)
        worked_examples: [
          {
            problem: "Exercise 8.2 Q1 & Q7: (a) Find the 20th and nth terms of the G.P. 5/2, 5/4, 5/8, ... (b) Find the sum to 20 terms in the geometric progression: 0.15, 0.015, 0.0015, ...",
            given: "G.P. with initial terms.",
            formula: "General term a_n = a r^(n-1); Sum of n terms S_n = a(1 - r^n)/(1 - r) for r < 1.",
            substitution: "Part (a): a = 5/2, r = (5/4)/(5/2) = 1/2. Part (b): a = 0.15, r = 0.015/0.15 = 0.1.",
            calculation: "Part (a):\n  a_20 = (5/2)(1/2)^(19) = 5 / 2^20.\n  a_n = (5/2)(1/2)^(n-1) = 5 / 2^n.\n\nPart (b):\n  S_20 = 0.15 * [ 1 - (0.1)^20 ] / [ 1 - 0.1 ]\n  = (0.15 / 0.9) * [ 1 - (0.1)^20 ] = (1/6) * [ 1 - (0.1)^20 ].",
            finalAnswer: "(a) a_20 = 5/2^20, a_n = 5/2^n; (b) S_20 = (1/6)[1 - (0.1)^20]",
            unit: "geometric progression",
            has_diagram: false
          },
          {
            problem: "Exercise 8.2 Q18: Find the sum to n terms of the sequence: 8, 88, 888, 8888, ...",
            given: "Series S_n = 8 + 88 + 888 + ... to n terms.",
            formula: "Factor out 8, multiply and divide by 9 to convert terms into (10^k - 1).",
            substitution: "S_n = (8/9) [ 9 + 99 + 999 + ... + (10^n - 1) ].",
            calculation: "Step 1: S_n = (8/9) [ (10 - 1) + (10^2 - 1) + (10^3 - 1) + ... + (10^n - 1) ].\nStep 2: Group GP and constant terms:\n  S_n = (8/9) [ (10 + 10^2 + ... + 10^n) - (1 + 1 + ... + 1) ].\nStep 3: Sum of GP (a = 10, r = 10): 10(10^n - 1) / (10 - 1) = (10/9)(10^n - 1).\nStep 4: Substitute back:\n  S_n = (8/9) [ (10/9)(10^n - 1) - n ] = 80/81 (10^n - 1) - 8n/9.",
            finalAnswer: "S_n = (80/81)(10^n - 1) - (8n/9)",
            unit: "series sum",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 9,
    title: 'Chapter 9: Straight Lines',
    solvers: [
      {
        module_order: 4, // Exercise 9.1 & 9.2 Solver
        worked_examples: [
          {
            problem: "Exercise 9.1 Q1 & Q6: (a) Draw a quadrilateral in the Cartesian plane whose vertices are (-4, 5), (0, 7), (5, -5) and (-4, -2). Also, find its area. (b) Find the slope of a line which passes through the origin and the mid-point of the line segment joining points P(0, -4) and B(8, 0).",
            given: "Vertices of quadrilateral; points P(0, -4) and B(8, 0).",
            formula: "Area = 1/2 |(x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2))|. Slope m = (y2 - y1)/(x2 - x1). Midpoint = ((x1+x2)/2, (y1+y2)/2).",
            substitution: "Divide quadrilateral into two triangles: (-4, 5), (0, 7), (5, -5) and (-4, 5), (5, -5), (-4, -2). Midpoint M of PB = ((0+8)/2, (-4+0)/2) = (4, -2).",
            calculation: "Part (a):\nArea of Triangle 1 [(-4, 5), (0, 7), (5, -5)]:\n  = 1/2 | -4(7 - (-5)) + 0 + 5(5 - 7) | = 1/2 | -48 - 10 | = 58/2 = 29 sq units.\nArea of Triangle 2 [(-4, 5), (5, -5), (-4, -2)]:\n  = 1/2 | -4(-5 - (-2)) + 5(-2 - 5) - 4(5 - (-5)) | = 1/2 | 12 - 35 - 40 | = 1/2 | -63 | = 31.5 sq units.\nTotal Area = 29 + 31.5 = 60.5 sq units.\n\nPart (b):\nMidpoint M = (4, -2). Origin O = (0, 0).\nSlope m = (-2 - 0) / (4 - 0) = -2/4 = -1/2.",
            finalAnswer: "(a) Area = 60.5 sq units; (b) Slope = -1/2",
            unit: "slope and area",
            has_diagram: true
          },
          {
            problem: "Exercise 9.2 Q1 & Q7: (a) Find the equation of the line passing through (-4, 3) with slope 1/2. (b) Find the equation of the line passing through (-1, 1) and (2, -4).",
            given: "Point and slope; two points on the line.",
            formula: "Point-slope form: y - y1 = m(x - x1); Two-point form: y - y1 = [(y2 - y1)/(x2 - x1)] (x - x1).",
            substitution: "Part (a): (x1, y1) = (-4, 3), m = 1/2. Part (b): (x1, y1) = (-1, 1), (x2, y2) = (2, -4).",
            calculation: "Part (a):\ny - 3 = (1/2)(x - (-4)) => 2(y - 3) = x + 4 => 2y - 6 = x + 4 => x - 2y + 10 = 0.\n\nPart (b):\nSlope m = (-4 - 1) / (2 - (-1)) = -5/3.\nEquation: y - 1 = (-5/3)(x - (-1)) => 3(y - 1) = -5(x + 1) => 3y - 3 = -5x - 5 => 5x + 3y + 2 = 0.",
            finalAnswer: "(a) x - 2y + 10 = 0; (b) 5x + 3y + 2 = 0",
            unit: "line equations",
            has_diagram: true
          }
        ]
      },
      {
        module_order: 5, // Exercise 9.3 Solver
        worked_examples: [
          {
            problem: "Exercise 9.3 Q4 & Q6: (a) Find points on the x-axis whose distances from the line x/3 + y/4 = 1 are 4 units. (b) Find the distance between parallel lines: 15x + 8y - 34 = 0 and 15x + 8y + 31 = 0.",
            given: "Line 4x + 3y - 12 = 0, distance d = 4 from point (x0, 0); Parallel lines with A = 15, B = 8.",
            formula: "Perpendicular distance d = |Ax0 + By0 + C| / sqrt(A^2 + B^2). Distance between parallel lines d = |C1 - C2| / sqrt(A^2 + B^2).",
            substitution: "A = 4, B = 3, C = -12; point (x0, 0). For parallel lines: C1 = -34, C2 = 31.",
            calculation: "Part (a):\nLine: 4x + 3y - 12 = 0. Point on x-axis is (x0, 0).\nd = |4(x0) + 3(0) - 12| / sqrt(4^2 + 3^2) = |4x0 - 12| / 5 = 4.\n=> |4x0 - 12| = 20.\nCase 1: 4x0 - 12 = 20 => 4x0 = 32 => x0 = 8. Point = (8, 0).\nCase 2: 4x0 - 12 = -20 => 4x0 = -8 => x0 = -2. Point = (-2, 0).\n\nPart (b):\nd = |-34 - 31| / sqrt(15^2 + 8^2) = |-65| / sqrt(225 + 64) = 65 / sqrt(289) = 65 / 17 units.",
            finalAnswer: "(a) Points on x-axis: (8, 0) and (-2, 0); (b) Distance = 65/17 units",
            unit: "distance formulas",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 10,
    title: 'Chapter 10: Conic Sections',
    solvers: [
      {
        module_order: 3, // Exercise 10.1 Circles
        worked_examples: [
          {
            problem: "Exercise 10.1 Q1 & Q6: (a) Find the equation of the circle with centre (0, 2) and radius 2. (b) Find the centre and radius of the circle (x + 5)^2 + (y - 3)^2 = 36.",
            given: "Centre (h, k) and radius r; and standard circle equation.",
            formula: "Standard equation of a circle: (x - h)^2 + (y - k)^2 = r^2.",
            substitution: "Part (a): h = 0, k = 2, r = 2. Part (b): h = -5, k = 3, r = sqrt(36) = 6.",
            calculation: "Part (a):\n(x - 0)^2 + (y - 2)^2 = 2^2\n=> x^2 + y^2 - 4y + 4 = 4\n=> x^2 + y^2 - 4y = 0.\n\nPart (b):\nComparing with (x - h)^2 + (y - k)^2 = r^2:\nh = -5, k = 3, r^2 = 36 => r = 6.\nCentre = (-5, 3), Radius = 6.",
            finalAnswer: "(a) x^2 + y^2 - 4y = 0; (b) Centre = (-5, 3), Radius = 6 units",
            unit: "circle properties",
            has_diagram: true
          }
        ]
      },
      {
        module_order: 4, // Exercise 10.2 Parabolas
        worked_examples: [
          {
            problem: "Exercise 10.2 Q1 & Q5: Find the coordinates of the focus, axis of the parabola, the equation of the directrix and the length of the latus rectum for: (i) y^2 = 12x, (ii) y^2 = 10x.",
            given: "Parabolas symmetric about positive x-axis of form y^2 = 4ax.",
            formula: "For y^2 = 4ax: Focus = (a, 0); Axis is y = 0 (x-axis); Directrix is x = -a; Latus Rectum = 4a.",
            substitution: "Part (i): 4a = 12 => a = 3. Part (ii): 4a = 10 => a = 5/2.",
            calculation: "Part (i) y^2 = 12x:\n  4a = 12 => a = 3.\n  - Focus = (3, 0)\n  - Axis = x-axis (equation y = 0)\n  - Directrix: x = -3 => x + 3 = 0\n  - Latus rectum length = 4a = 12.\n\nPart (ii) y^2 = 10x:\n  4a = 10 => a = 5/2.\n  - Focus = (5/2, 0)\n  - Axis = x-axis (y = 0)\n  - Directrix: x = -5/2 => 2x + 5 = 0\n  - Latus rectum length = 4a = 10.",
            finalAnswer: "(i) Focus (3, 0), Axis y=0, Directrix x=-3, Latus Rectum = 12; (ii) Focus (5/2, 0), Axis y=0, Directrix x=-5/2, Latus Rectum = 10",
            unit: "parabola parameters",
            has_diagram: true
          }
        ]
      },
      {
        module_order: 5, // Exercise 10.3 Ellipses
        worked_examples: [
          {
            problem: "Exercise 10.3 Q1: Find the coordinates of the foci, the vertices, the length of major axis, the minor axis, the eccentricity and the length of the latus rectum of the ellipse: x^2/36 + y^2/16 = 1.",
            given: "Ellipse equation x^2/36 + y^2/16 = 1. Here a^2 = 36 > b^2 = 16, so major axis is along x-axis.",
            formula: "c = sqrt(a^2 - b^2); Foci = (±c, 0); Vertices = (±a, 0); Major axis = 2a; Minor axis = 2b; e = c/a; Latus Rectum = 2b^2/a.",
            substitution: "a = 6, b = 4; c = sqrt(36 - 16) = sqrt(20) = 2 sqrt(5).",
            calculation: "Step 1: Vertices = (±6, 0).\nStep 2: Foci = (±2 sqrt(5), 0).\nStep 3: Major axis length = 2(6) = 12.\nStep 4: Minor axis length = 2(4) = 8.\nStep 5: Eccentricity e = c/a = (2 sqrt(5))/6 = sqrt(5)/3.\nStep 6: Length of latus rectum = 2b^2 / a = 2(16) / 6 = 32/6 = 16/3.",
            finalAnswer: "Foci: (±2√5, 0), Vertices: (±6, 0), Major axis: 12, Minor axis: 8, Eccentricity: √5/3, Latus Rectum: 16/3",
            unit: "ellipse parameters",
            has_diagram: true
          }
        ]
      },
      {
        module_order: 6, // Exercise 10.4 Hyperbolas
        worked_examples: [
          {
            problem: "Exercise 10.4 Q1: Find the coordinates of the foci and vertices, the eccentricity and the length of the latus rectum of the hyperbola: x^2/16 - y^2/9 = 1.",
            given: "Hyperbola of standard form x^2/a^2 - y^2/b^2 = 1 with a^2 = 16, b^2 = 9.",
            formula: "Transverse axis along x-axis. c = sqrt(a^2 + b^2); Foci = (±c, 0); Vertices = (±a, 0); e = c/a; Latus Rectum = 2b^2/a.",
            substitution: "a = 4, b = 3; c = sqrt(16 + 9) = sqrt(25) = 5.",
            calculation: "Step 1: Vertices = (±4, 0).\nStep 2: Foci = (±5, 0).\nStep 3: Eccentricity e = c/a = 5/4.\nStep 4: Latus rectum length = 2b^2 / a = 2(9) / 4 = 18/4 = 9/2.",
            finalAnswer: "Vertices: (±4, 0), Foci: (±5, 0), Eccentricity: 5/4, Latus Rectum: 9/2",
            unit: "hyperbola parameters",
            has_diagram: true
          }
        ]
      }
    ]
  },
  {
    order_index: 11,
    title: 'Chapter 11: Introduction to Three Dimensional Geometry',
    solvers: [
      {
        module_order: 4, // Exercise 11.1 Octants
        worked_examples: [
          {
            problem: "Exercise 11.1 Q1, Q2 & Q3: (a) A point is on the x-axis. What are its y-coordinate and z-coordinates? (b) A point is in the XZ-plane. What can you say about its y-coordinate? (c) Name the octants in which the following points lie: (1, 2, 3), (4, -2, 3), (4, -2, -5), (-4, 2, -5).",
            given: "Point locations on coordinate axes, planes, and coordinate sign triplets.",
            formula: "Points on x-axis: (x, 0, 0); Points on XZ-plane: (x, 0, z); Octant signs: I(+,+,+), II(-,+,+), III(-,-,+), IV(+,-,+), V(+,+,-), VI(-,+,-), VII(-,-,-), VIII(+,-,-).",
            substitution: "Check signs of (x, y, z).",
            calculation: "Part (a): For any point on the x-axis, both y = 0 and z = 0.\nPart (b): For any point in the XZ-plane, y = 0.\nPart (c) Octant identification:\n  (1, 2, 3): (+, +, +) => Octant I.\n  (4, -2, 3): (+, -, +) => Octant IV.\n  (4, -2, -5): (+, -, -) => Octant VIII.\n  (-4, 2, -5): (-, +, -) => Octant VI.",
            finalAnswer: "(a) y = 0, z = 0; (b) y = 0; (c) (1,2,3) in I, (4,-2,3) in IV, (4,-2,-5) in VIII, (-4,2,-5) in VI",
            unit: "3D octants and axes",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 5, // Exercise 11.2 Distance Formula in 3D
        worked_examples: [
          {
            problem: "Exercise 11.2 Q1 & Q2: (a) Find the distance between the points (2, 3, 5) and (4, 3, 1). (b) Show that the points P(-2, 3, 5), Q(1, 2, 3) and R(7, 0, -1) are collinear.",
            given: "Points in 3D space.",
            formula: "Distance d = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2). Collinearity test: PQ + QR = PR.",
            substitution: "Substitute 3D coordinates into Euclidean metric.",
            calculation: "Part (a):\nd = sqrt((4 - 2)^2 + (3 - 3)^2 + (1 - 5)^2) = sqrt(2^2 + 0^2 + (-4)^2) = sqrt(4 + 16) = sqrt(20) = 2 sqrt(5) units.\n\nPart (b) Test for collinearity:\nPQ = sqrt((1 - (-2))^2 + (2 - 3)^2 + (3 - 5)^2) = sqrt(3^2 + (-1)^2 + (-2)^2) = sqrt(9 + 1 + 4) = sqrt(14).\nQR = sqrt((7 - 1)^2 + (0 - 2)^2 + (-1 - 3)^2) = sqrt(6^2 + (-2)^2 + (-4)^2) = sqrt(36 + 4 + 16) = sqrt(56) = 2 sqrt(14).\nPR = sqrt((7 - (-2))^2 + (0 - 3)^2 + (-1 - 5)^2) = sqrt(9^2 + (-3)^2 + (-6)^2) = sqrt(81 + 9 + 36) = sqrt(126) = 3 sqrt(14).\nSince PQ + QR = sqrt(14) + 2 sqrt(14) = 3 sqrt(14) = PR, the points P, Q, and R are COLLINEAR. Hence Proved!",
            finalAnswer: "(a) Distance = 2√5 units; (b) PQ + QR = PR = 3√14 (Points are Collinear)",
            unit: "3D distance and collinearity",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 12,
    title: 'Chapter 12: Limits and Derivatives',
    solvers: [
      {
        module_order: 3, // Exercise 12.1 Limits
        worked_examples: [
          {
            problem: "Exercise 12.1 Q1, Q10 & Q13: Evaluate the following limits: (i) lim_{x->3} (x + 3), (ii) lim_{z->1} (z^(1/3) - 1) / (z^(1/6) - 1), (iii) lim_{x->0} (sin ax) / (bx).",
            given: "Limit expressions as variables approach specific values.",
            formula: "Algebraic limit substitution; Standard theorem: lim_{x->a} (x^n - a^n)/(x - a) = n a^(n-1); Trigonometric standard limit: lim_{theta->0} (sin theta)/theta = 1.",
            substitution: "Apply limit laws and standard forms.",
            calculation: "Part (i):\nlim_{x->3} (x + 3) = 3 + 3 = 6.\n\nPart (ii):\nNotice z^(1/3) = (z^(1/6))^2. Let u = z^(1/6). As z -> 1, u -> 1.\nExpression = (u^2 - 1) / (u - 1) = (u - 1)(u + 1) / (u - 1) = u + 1.\nTaking limit as u -> 1: 1 + 1 = 2.\n\nPart (iii):\nlim_{x->0} (sin ax) / (bx) = lim_{x->0} [ (sin ax)/(ax) ] * (ax / bx)\n  = [ lim_{ax->0} (sin ax)/(ax) ] * (a / b) = 1 * (a / b) = a / b.",
            finalAnswer: "(i) 6; (ii) 2; (iii) a/b",
            unit: "limit evaluation",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 5, // Exercise 12.2 Derivatives
        worked_examples: [
          {
            problem: "Exercise 12.2 Q1 & Q4: (a) Find the derivative of x^2 - 2 at x = 10. (b) Find the derivative of f(x) = x^3 - 27 from FIRST PRINCIPLE.",
            given: "Functions to differentiate.",
            formula: "First Principle Definition: f'(x) = lim_{h->0} [ f(x + h) - f(x) ] / h. Power Rule: d/dx(x^n) = n x^(n-1).",
            substitution: "Evaluate difference quotient as h -> 0.",
            calculation: "Part (a):\nf(x) = x^2 - 2 => f'(x) = 2x - 0 = 2x.\nAt x = 10: f'(10) = 2(10) = 20.\n\nPart (b) By First Principle:\nf(x) = x^3 - 27.\nf(x + h) = (x + h)^3 - 27 = x^3 + 3x^2 h + 3x h^2 + h^3 - 27.\nf(x + h) - f(x) = [ x^3 + 3x^2 h + 3x h^2 + h^3 - 27 ] - [ x^3 - 27 ]\n  = 3x^2 h + 3x h^2 + h^3 = h(3x^2 + 3xh + h^2).\nf'(x) = lim_{h->0} [ h(3x^2 + 3xh + h^2) ] / h = lim_{h->0} (3x^2 + 3xh + h^2)\n  = 3x^2 + 0 + 0 = 3x^2.",
            finalAnswer: "(a) f'(10) = 20; (b) f'(x) = 3x^2 (derived from First Principle)",
            unit: "derivatives",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 13,
    title: 'Chapter 13: Statistics',
    solvers: [
      {
        module_order: 3, // Exercise 13.1 Mean Deviation
        worked_examples: [
          {
            problem: "Exercise 13.1 Q1: Find the mean deviation about the mean for the data: 4, 7, 8, 9, 10, 12, 13, 17.",
            given: "Data values: x = 4, 7, 8, 9, 10, 12, 13, 17. Number of observations n = 8.",
            formula: "Mean x_bar = (sum x_i) / n; Mean Deviation MD(x_bar) = (sum |x_i - x_bar|) / n.",
            substitution: "Calculate sum and absolute deviations.",
            calculation: "Step 1: Calculate Mean x_bar:\n  sum x_i = 4 + 7 + 8 + 9 + 10 + 12 + 13 + 17 = 80.\n  x_bar = 80 / 8 = 10.\nStep 2: Calculate absolute deviations |x_i - 10|:\n  |4 - 10| = 6\n  |7 - 10| = 3\n  |8 - 10| = 2\n  |9 - 10| = 1\n  |10 - 10| = 0\n  |12 - 10| = 2\n  |13 - 10| = 3\n  |17 - 10| = 7\nStep 3: Sum of absolute deviations:\n  sum |x_i - x_bar| = 6 + 3 + 2 + 1 + 0 + 2 + 3 + 7 = 24.\nStep 4: Mean Deviation:\n  MD(x_bar) = 24 / 8 = 3.",
            finalAnswer: "Mean = 10, Mean Deviation about Mean = 3",
            unit: "mean deviation",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 6, // Exercise 13.2 Variance & Standard Deviation
        worked_examples: [
          {
            problem: "Exercise 13.2 Q1: Find the mean and variance for the numbers: 6, 7, 10, 12, 13, 4, 8, 12.",
            given: "Data: 6, 7, 10, 12, 13, 4, 8, 12. Total observations n = 8.",
            formula: "Mean x_bar = (sum x_i)/n; Variance sigma^2 = [ sum (x_i - x_bar)^2 ] / n.",
            substitution: "Compute sum, deviations, and squared deviations.",
            calculation: "Step 1: Mean:\n  sum x_i = 6 + 7 + 10 + 12 + 13 + 4 + 8 + 12 = 72.\n  x_bar = 72 / 8 = 9.\nStep 2: Squared deviations (x_i - 9)^2:\n  (6 - 9)^2 = (-3)^2 = 9\n  (7 - 9)^2 = (-2)^2 = 4\n  (10 - 9)^2 = 1^2 = 1\n  (12 - 9)^2 = 3^2 = 9\n  (13 - 9)^2 = 4^2 = 16\n  (4 - 9)^2 = (-5)^2 = 25\n  (8 - 9)^2 = (-1)^2 = 1\n  (12 - 9)^2 = 3^2 = 9\nStep 3: Sum of squared deviations:\n  sum = 9 + 4 + 1 + 9 + 16 + 25 + 1 + 9 = 74.\nStep 4: Variance:\n  sigma^2 = 74 / 8 = 9.25.\nStep 5: Standard Deviation sigma = sqrt(9.25) ≈ 3.04.",
            finalAnswer: "Mean = 9, Variance = 9.25, Standard Deviation = 3.04",
            unit: "variance and standard deviation",
            has_diagram: false
          }
        ]
      }
    ]
  },
  {
    order_index: 14,
    title: 'Chapter 14: Probability',
    solvers: [
      {
        module_order: 3, // Exercise 14.1 Sample Space
        worked_examples: [
          {
            problem: "Exercise 14.1 Q1 & Q5: Describe the sample space for: (i) A coin is tossed three times. (ii) A coin is tossed and then a die is rolled only in case a head turns up.",
            given: "Random experiment conditions.",
            formula: "Sample space S is the set of all possible outcomes of a random experiment.",
            substitution: "Enumerate all branches of the outcome tree.",
            calculation: "Part (i) Coin tossed 3 times:\n  Total outcomes = 2^3 = 8.\n  S = { HHH, HHT, HTH, HTT, THH, THT, TTH, TTT }.\n\nPart (ii) Coin tossed; if Head, roll a die (outcomes 1 to 6); if Tail, stop:\n  If Tail: outcome is T.\n  If Head: outcomes are H1, H2, H3, H4, H5, H6.\n  Total outcomes = 7.\n  S = { T, (H, 1), (H, 2), (H, 3), (H, 4), (H, 5), (H, 6) }.",
            finalAnswer: "(i) S = { HHH, HHT, HTH, HTT, THH, THT, TTH, TTT }; (ii) S = { T, (H,1), (H,2), (H,3), (H,4), (H,5), (H,6) }",
            unit: "sample spaces",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 6, // Exercise 14.2 Part 1
        worked_examples: [
          {
            problem: "Exercise 14.2 Q1: A box contains 10 red marbles, 20 blue marbles and 30 green marbles. 5 marbles are drawn from the box. What is the probability that: (i) all will be blue? (ii) at least one will be green?",
            given: "Total marbles = 10 + 20 + 30 = 60 marbles. Number drawn = 5.",
            formula: "Total sample space combinations n(S) = C(60, 5). Probability P(E) = n(E) / n(S). P(at least one green) = 1 - P(no green).",
            substitution: "Evaluate combination counts.",
            calculation: "Total ways to choose 5 marbles from 60 = C(60, 5).\n\nPart (i) All 5 are blue:\n  Blue marbles available = 20.\n  Ways to choose 5 blue marbles = C(20, 5).\n  P(all blue) = C(20, 5) / C(60, 5).\n\nPart (ii) At least one is green:\n  Non-green marbles (red + blue) = 10 + 20 = 30 marbles.\n  Ways to choose 5 non-green marbles = C(30, 5).\n  P(no green) = C(30, 5) / C(60, 5).\n  P(at least one green) = 1 - [ C(30, 5) / C(60, 5) ].",
            finalAnswer: "(i) P(all blue) = C(20, 5) / C(60, 5); (ii) P(at least one green) = 1 - [ C(30, 5) / C(60, 5) ]",
            unit: "combinatorial probability",
            has_diagram: false
          }
        ]
      },
      {
        module_order: 7, // Exercise 14.2 Part 2
        worked_examples: [
          {
            problem: "Exercise 14.2 Q11 & Q12: If A and B are events such that P(A) = 1/4, P(B) = 1/2 and P(A intersect B) = 1/8, find: (i) P(A or B), (ii) P(not A and not B).",
            given: "P(A) = 1/4 = 2/8, P(B) = 1/2 = 4/8, P(A intersect B) = 1/8.",
            formula: "Addition Theorem: P(A U B) = P(A) + P(B) - P(A intersect B); De Morgan's Law: P(not A and not B) = P((A U B)') = 1 - P(A U B).",
            substitution: "Substitute probabilities into formulas.",
            calculation: "Part (i) P(A or B) = P(A U B):\n  P(A U B) = P(A) + P(B) - P(A intersect B)\n  = 1/4 + 1/2 - 1/8 = 2/8 + 4/8 - 1/8 = 5/8.\n\nPart (ii) P(not A and not B) = P(A' intersect B'):\n  By De Morgan's Law: A' intersect B' = (A U B)'.\n  P((A U B)') = 1 - P(A U B) = 1 - 5/8 = 3/8.",
            finalAnswer: "(i) P(A or B) = 5/8; (ii) P(not A and not B) = 3/8",
            unit: "probability algebra",
            has_diagram: false
          }
        ]
      }
    ]
  }
];

async function enrichClass11MathsPart2() {
  console.log("Starting Class 11 Mathematics Part 2 (Ch 8 to 14) Enrichment...");

  for (const chData of CHAPTERS_PT2) {
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

  console.log("\nClass 11 Mathematics Part 2 Enrichment Completed!");
}

enrichClass11MathsPart2();
