"""
Chapter 5: I’m Up and Down, and Round and Round - Module 6
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .svg_builder import build_cyclic_quad_svg

def get_m6():
    m6_svg = build_cyclic_quad_svg(
        radius=95, center=(290, 195),
        vertices=[(220, 130), (360, 130), (370, 260), (210, 260)],
        opposite_labels={"A": "75°", "C": "105°", "B": "110°", "D": "70°"},
        title="Cyclic Quadrilateral: Opposite Angles Sum to 180°",
        caption="Cyclic quadrilateral ABCD with opposite angles summing to 180°: 75° + 105° = 180° and 110° + 70° = 180°"
    )

    return {
        "order_index": 6,
        "title": "Textbook Exercise Solver 5: Cyclic Quadrilaterals, Brahmagupta's Formula & Advanced Geometric Challenges (End-of-Chapter Complete)",
        "description": "Comprehensive step-by-step solutions to End-of-Chapter Questions 7, 8, 10, 11, 12, 14, 15, 21, 25, and 26. Master cyclic quadrilateral angle supplementarity, solving for algebraic unknowns (2x+10 and 3x-20), Brahmagupta's cyclic area formula for sides 5, 5, 12, 12 (Area = 60), circumcentre location test without drawing circle, equal intersecting chord segments, proving an inscribed parallelogram is always a rectangle, exterior cyclic angles, and Fig 5.31 central angle proof.",
        "subtopics": [
            "Supplementary Invariant: Opposite angles of a cyclic quadrilateral sum to 180° (Theorem 11)",
            "Algebraic angle equations in cyclic quadrilaterals: Solving (2x + 10) + (3x - 20) = 180°",
            "Brahmagupta's Cyclic Area Formula: K = sqrt((s-a)(s-b)(s-c)(s-d)) for cyclic quadrilateral with sides 5, 5, 12, 12",
            "Circumcentre location criterion: When does O lie inside vs outside a cyclic quadrilateral?",
            "Equal intersecting chords theorem: Segment equivalence AP = CP and BP = DP",
            "Rigorous proof that a rectangle is the only parallelogram that can be inscribed in a circle",
            "Exterior angle theorem for cyclic quadrilaterals: angle CDE = angle ABC",
            "Central angle proof using Fig. 5.31: u + v = 360° implies p + q = 180°"
        ],
        "key_concepts": [
            "Cyclic Quadrilateral Theorem: A four-sided polygon is inscribed in a circle if and only if opposite pairs of interior angles sum to 180°.",
            "Brahmagupta's Cyclic Area Theorem: If a cyclic quadrilateral has side lengths a, b, c, d and semiperimeter s = (a+b+c+d)/2, Area = sqrt((s-a)(s-b)(s-c)(s-d)).",
            "Inscribed Parallelogram Invariant: Parallelograms have equal opposite angles (A = C). In a circle, A + C = 180° => 2A = 180° => A = 90°, forcing it to be a rectangle.",
            "Diagonal Intersection Centre Theorem: In any inscribed rectangle, the diagonal is a diameter of the circle, so the intersection of diagonals is the circumcentre O.",
            "Exterior Angle Equality: Since angle D + angle CDE = 180° (linear pair) and angle D + angle B = 180° (cyclic opposite), angle CDE = angle B.",
            "Fig. 5.31 Inscribed-Central Angle Derivation: Arcs subtend central angles u and v summing to 360°. The inscribed angles are p = u/2 and q = v/2, so p + q = (u + v)/2 = 360°/2 = 180°."
        ],
        "success_criteria": "Students can calculate missing angles in cyclic quadrilaterals, apply Brahmagupta's formula to compute cyclic areas, prove parallelogram rectilinearity, and demonstrate geometric circle proofs.",
        "chapter_notes": "Module 6 concludes Chapter 5 by providing exhaustive mathematical proofs for all remaining End-of-Chapter problems from the Ganita Manjari Grade 9 Part 1 textbook.",
        "common_misconceptions": [
            {"misconception": "Applying Brahmagupta's formula to non-cyclic quadrilaterals", "clarification": "Brahmagupta's formula K = sqrt((s-a)(s-b)(s-c)(s-d)) holds ONLY for cyclic quadrilaterals; non-cyclic quadrilaterals require Bretschneider's subtraction term."},
            {"misconception": "Believing any rhombus can be inscribed in a circle", "clarification": "The only rhombus that can be inscribed in a circle is a square (since all angles must be 90°)."}
        ],
        "ai_system_prompt_context": "You are guiding a Class 9 CBSE student through advanced cyclic quadrilateral challenges. Walk through Brahmagupta's formula step by step and show the Fig 5.31 central angle derivation.",
        "visual_lesson_plan": {
            "title": "Visualizing Cyclic Quadrilaterals and Brahmagupta's Geometry",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Interactive circle with an inscribed cyclic quadrilateral showing opposite angles summing to 180°.",
            "concept_visuals": [
                {
                    "concept_title": "Cyclic Quadrilateral Opposite Angles: 75° + 105° = 180°",
                    "diagram_title": "Supplementary Opposite Angles",
                    "interactive_math_formula": "\\angle A + \\angle C = 180^\\circ, \\quad \\angle B + \\angle D = 180^\\circ",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Circumcircle r=8"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": -5.65, "y": 5.65, "label": "A (75°)"},
                            {"x": 5.65, "y": 5.65, "label": "B (110°)"},
                            {"x": 6.93, "y": -4, "label": "C (105°)"},
                            {"x": -6.93, "y": -4, "label": "D (70°)"}
                        ]
                    },
                    "image_query": "cyclic quadrilateral opposite angles sum to 180 degrees",
                    "video_query": "sum of opposite angles of cyclic quadrilateral is 180 proof",
                    "what_to_explain": "Opposite angles A and C subtend complementary arcs that together encircle the entire 360°, ensuring A + C = 180°."
                },
                {
                    "concept_title": "Brahmagupta's Cyclic Area: Sides 5, 5, 12, 12",
                    "diagram_title": "Symmetric Cyclic Kite / Quad: Area = 60",
                    "interactive_math_formula": "K = \\sqrt{(17-5)(17-5)(17-12)(17-12)} = \\sqrt{12 \\times 12 \\times 5 \\times 5} = 60",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(42.25 - x^2)", "color": "#2563EB", "label": "Circumcircle r=6.5"},
                            {"fn": "-sqrt(42.25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 6.5, "label": "A(0, 6.5)"},
                            {"x": 6, "y": 2.5, "label": "B(6, 2.5) [AB=5]"},
                            {"x": 0, "y": -6.5, "label": "C(0, -6.5) [BC=12]"},
                            {"x": -6, "y": 2.5, "label": "D(-6, 2.5) [AD=5, CD=12]"}
                        ]
                    },
                    "image_query": "Brahmagupta formula cyclic quadrilateral area sides 5 5 12 12",
                    "video_query": "Brahmagupta formula for area of cyclic quadrilateral solved example",
                    "what_to_explain": "With semiperimeter s = (5+5+12+12)/2 = 17, Brahmagupta's formula yields sqrt(12 * 12 * 5 * 5) = 60 square units."
                },
                {
                    "concept_title": "Inscribed Parallelogram Must Be a Rectangle",
                    "diagram_title": "Opposite Equal Angles in Circle: 2A = 180° -> A = 90°",
                    "interactive_math_formula": "\\angle A = \\angle C \\text{ and } \\angle A + \\angle C = 180^\\circ \\implies \\angle A = 90^\\circ",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [-8, 8],
                        "curves": [
                            {"fn": "sqrt(25 - x^2)", "color": "#2563EB", "label": "Circumcircle r=5"},
                            {"fn": "-sqrt(25 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": -4, "y": 3, "label": "A (90°)"},
                            {"x": 4, "y": 3, "label": "B (90°)"},
                            {"x": 4, "y": -3, "label": "C (90°)"},
                            {"x": -4, "y": -3, "label": "D (90°)"},
                            {"x": 0, "y": 0, "label": "Centre O (Diagonals Meet)"}
                        ]
                    },
                    "image_query": "prove that a cyclic parallelogram is a rectangle geometry",
                    "video_query": "prove that rectangle is the only parallelogram inscribed in circle",
                    "what_to_explain": "Parallelogram angles are equal, and cyclic angles are supplementary. Therefore, every angle must be 90°, making it a rectangle."
                },
                {
                    "concept_title": "Exterior Angle Theorem for Cyclic Quadrilateral",
                    "diagram_title": "Exterior Angle = Interior Opposite Angle",
                    "interactive_math_formula": "\\angle CDE = \\angle ABC",
                    "mafs_graph_config": {
                        "domain": [-10, 10],
                        "range": [-10, 10],
                        "curves": [
                            {"fn": "sqrt(64 - x^2)", "color": "#2563EB", "label": "Circle"},
                            {"fn": "-sqrt(64 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": -6, "y": 5.29, "label": "A"},
                            {"x": 6, "y": 5.29, "label": "B (Interior Opposite)"},
                            {"x": 7, "y": -3.87, "label": "C"},
                            {"x": -4, "y": -6.93, "label": "D"},
                            {"x": -8, "y": -8.5, "label": "E (Extended)"}
                        ]
                    },
                    "image_query": "exterior angle of cyclic quadrilateral equals interior opposite angle",
                    "video_query": "exterior angle of cyclic quadrilateral proof",
                    "what_to_explain": "Both the exterior angle at D and the interior opposite angle B are supplementary to the adjacent interior angle D, making them equal."
                },
                {
                    "concept_title": "Fig 5.31 Central Angle Proof: u + v = 360°",
                    "diagram_title": "p + q = (u + v)/2 = 360°/2 = 180°",
                    "interactive_math_formula": "p = \\frac{u}{2}, \\quad q = \\frac{v}{2} \\implies p + q = 180^\\circ",
                    "mafs_graph_config": {
                        "domain": [-8, 8],
                        "range": [-8, 8],
                        "curves": [
                            {"fn": "sqrt(36 - x^2)", "color": "#2563EB", "label": "Circle"},
                            {"fn": "-sqrt(36 - x^2)", "color": "#2563EB", "label": ""}
                        ],
                        "points": [
                            {"x": 0, "y": 0, "label": "Centre O (u + v = 360°)"},
                            {"x": 0, "y": 6, "label": "A (p = u/2)"},
                            {"x": 0, "y": -6, "label": "C (q = v/2)"},
                            {"x": -5.6, "y": 2, "label": "D"},
                            {"x": 5.6, "y": -2, "label": "B"}
                        ]
                    },
                    "image_query": "sum of opposite angles cyclic quadrilateral 180 central angle u and v",
                    "video_query": "cyclic quadrilateral opposite angles 180 degrees proof using centre angles",
                    "what_to_explain": "By Inscribed Angle Theorem, p = u/2 and q = v/2. Since central angles complete a full rotation (u + v = 360°), p + q = 180°."
                }
            ],
            "concept_questions": [
                {
                    "concept": "Cyclic Quadrilaterals & Brahmagupta",
                    "questions": [
                        {
                            "question": "If an inscribed quadrilateral is a parallelogram, what type of parallelogram must it be?",
                            "type": "short_answer",
                            "ideal_answer": "It must be a rectangle (because opposite angles are both equal and supplementary, so each angle is 90°).",
                            "socratic_hint": "If A = C and A + C = 180°, what is the measure of A?"
                        },
                        {
                            "question": "What is the area of a cyclic quadrilateral with sides 5, 5, 12, 12 units using Brahmagupta's formula?",
                            "type": "short_answer",
                            "ideal_answer": "60 square units (s = 17; sqrt(12 * 12 * 5 * 5) = 12 * 5 = 60).",
                            "socratic_hint": "Calculate the semiperimeter s, then evaluate sqrt((s-a)(s-b)(s-c)(s-d))."
                        }
                    ]
                }
            ]
        },
        "worked_examples": [
            {
                "problem": "End-of-Chapter Q7: ABCD is a cyclic quadrilateral inscribed in a circle. If angle A measures 75°, what is the measure of angle C? If angle B measures 110°, what is the measure of angle D?",
                "given": "Cyclic quadrilateral ABCD. angle A = 75°, angle B = 110°.",
                "formula": "Theorem 11: The opposite angles of a cyclic quadrilateral are supplementary: angle A + angle C = 180° and angle B + angle D = 180°.",
                "substitution": "75° + angle C = 180°; 110° + angle D = 180°.",
                "calculation": "1. For angle C: angle C = 180° - 75° = 105°.\n2. For angle D: angle D = 180° - 110° = 70°.\n3. Sum of all four interior angles = 75° + 110° + 105° + 70° = 360°, confirming consistency.",
                "finalAnswer": "angle C = 105°, angle D = 70°",
                "unit": "degrees",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q8: Quadrilateral PQRS is inscribed in a circle. If angle P = (2x + 10)° and angle R = (3x - 20)°, find the value of x and the measures of angle P and angle R.",
                "given": "Cyclic quadrilateral PQRS. Opposite angles: angle P = (2x + 10)°, angle R = (3x - 20)°.",
                "formula": "Opposite angles sum to 180°: angle P + angle R = 180°.",
                "substitution": "(2x + 10) + (3x - 20) = 180.",
                "calculation": "1. Combine like terms: (2x + 3x) + (10 - 20) = 180 => 5x - 10 = 180.\n2. Add 10 to both sides: 5x = 190.\n3. Divide by 5: x = 190 / 5 = 38.\n4. Calculate angle P: angle P = 2(38) + 10 = 76 + 10 = 86°.\n5. Calculate angle R: angle R = 3(38) - 20 = 114 - 20 = 94°.\n6. Verification: 86° + 94° = 180°. Correct!",
                "finalAnswer": "x = 38; angle P = 86°, angle R = 94°",
                "unit": "degrees",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q10: A cyclic quadrilateral has sides 5, 5, 12, 12 units. Find its area.",
                "given": "Cyclic quadrilateral with side lengths a = 5, b = 5, c = 12, d = 12.",
                "formula": "Brahmagupta's Formula: Area K = sqrt((s - a)(s - b)(s - c)(s - d)), where semiperimeter s = (a + b + c + d) / 2.",
                "substitution": "s = (5 + 5 + 12 + 12) / 2 = 34 / 2 = 17.",
                "calculation": "1. Compute factors:\n   s - a = 17 - 5 = 12\n   s - b = 17 - 5 = 12\n   s - c = 17 - 12 = 5\n   s - d = 17 - 12 = 5.\n2. Substitute into Brahmagupta's formula:\n   K = sqrt(12 * 12 * 5 * 5).\n3. Simplify the square root:\n   K = sqrt((12^2) * (5^2)) = 12 * 5 = 60.\n4. (Alternative geometric check: A cyclic quadrilateral with adjacent equal sides 5, 5 and 12, 12 is a kite whose opposite angles are 90°, composed of two right triangles of legs 5 and 12: Area = 2 * (1/2 * 5 * 12) = 60 sq units).",
                "finalAnswer": "60 square units",
                "unit": "sq units",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q11: Consider a cyclic quadrilateral. Without drawing its circumcircle, how can we find out whether the centre of the circumcircle lies inside the quadrilateral or outside? What is the best way?",
                "given": "A cyclic quadrilateral ABCD with known vertex angles or side lengths.",
                "formula": "Angle-sum criterion relative to 90°: The centre O lies strictly inside the cyclic quadrilateral if and only if all four vertices are acute or right, or equivalently, no side or diagonal subtends an angle > 90° from the opposite vertices (no opposite angle > 90° across a diagonal diameter).",
                "substitution": "Examine the diagonals and angles.",
                "calculation": "1. Method 1 (Angle Analysis): A diameter of the circumcircle subtends a 90° angle on the circle. If the quadrilateral contains a diagonal that subtends an obtuse angle (> 90°) at a vertex, the centre must lie outside that triangle, on the opposite side of the diagonal.\n2. Specifically, if all four triangles formed by the diagonals (triangle ABC, BCD, CDA, DAB) are acute-angled or right-angled, the circumcentre lies inside (or on the boundary of) the quadrilateral.\n3. If any one of the four vertices has an angle exceeding 90° and the opposite vertex subtends an arc that does not contain the centre, the centre lies outside.\n4. Method 2 (Perpendicular Bisector Test): Choose any three sides, find the equations of their perpendicular bisectors, and find their unique intersection point O. Then check whether O satisfies the linear inequalities defining the interior of the polygon.",
                "finalAnswer": "Check if any diagonal subtends an obtuse angle (> 90°) at a vertex. If all triangles formed by vertices are acute or right-angled, the centre lies inside; if one triangle is obtuse and contains a diameter-spanning arc, the centre lies outside.",
                "unit": "geometric criterion",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q12: When two chords intersect, each is divided into two segments. Show that if the intersecting chords are of equal length, the line segments of one chord are equal to the corresponding line segments of the other chord.",
                "given": "Two chords AB and CD of equal length (AB = CD) intersecting at point X inside a circle with centre O.",
                "formula": "Drop perpendiculars OL perp AB and OM perp CD. Equal chords are equidistant from centre: OL = OM.",
                "substitution": "Join OX. In right triangles OLX and OMX: OL = OM, OX = OX (hypotenuse).",
                "calculation": "1. By Theorem 6, since AB = CD, the chords are equidistant from centre O: OL = OM.\n2. In right triangles OLX and OMX:\n   - angle OLX = angle OMX = 90°\n   - OX = OX (common hypotenuse)\n   - OL = OM (equal chord distances)\n   By RHS criterion, triangle OLX ~= triangle OMX.\n3. By CPCTC: LX = MX.\n4. By Theorem 5, the perpendiculars bisect the chords: AL = LB = AB/2 and CM = MD = CD/2.\n   Since AB = CD, we have AL = LB = CM = MD.\n5. Adding LX to AL and MX to CM:\n   AX = AL + LX = CM + MX = CX.\n6. For the remaining segments, subtract from the equal chord lengths:\n   XB = AB - AX = CD - CX = XD.\n7. Thus, AX = CX and XB = XD.",
                "finalAnswer": "Proved: The segments of one chord are equal to the corresponding segments of the other chord (AX = CX and XB = XD).",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q14: Show that a rectangle is the only parallelogram that can be inscribed in a circle.",
                "given": "Parallelogram ABCD inscribed in a circle.",
                "formula": "In a parallelogram, opposite angles are equal: angle A = angle C and angle B = angle D. In a cyclic quadrilateral, opposite angles are supplementary: angle A + angle C = 180°.",
                "substitution": "Substitute angle C = angle A into the supplementary condition.",
                "calculation": "1. Because ABCD is a parallelogram, opposite interior angles are equal:\n   angle A = angle C.\n2. Because ABCD is inscribed in a circle, it is a cyclic quadrilateral, so opposite angles are supplementary:\n   angle A + angle C = 180°.\n3. Substitute angle C = angle A:\n   angle A + angle A = 180° => 2*angle A = 180° => angle A = 90°.\n4. Since angle C = angle A, angle C = 90°.\n5. Similarly, for the other pair of opposite angles:\n   angle B = angle D and angle B + angle D = 180° => 2*angle B = 180° => angle B = 90°, and angle D = 90°.\n6. A parallelogram whose interior angles are all 90° is, by definition, a rectangle.\n7. Therefore, a rectangle is the only parallelogram that can be inscribed in a circle.",
                "finalAnswer": "Proved: Since opposite angles are both equal (parallelogram property) and supplementary (cyclic property), 2*angle A = 180° => angle A = 90°, so the parallelogram must be a rectangle.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q15: Show that if a rectangle is inscribed in a circle, then the point of intersection of its diagonals must lie at the centre of the circle.",
                "given": "Rectangle ABCD inscribed in a circle with centre O. AC and BD are diagonals.",
                "formula": "Every angle of a rectangle is 90°. By Thales' theorem (converse), a chord that subtends 90° at the circumference must be a diameter of the circle.",
                "substitution": "Angle ABC = 90°, so diagonal AC is a diameter.",
                "calculation": "1. In rectangle ABCD, angle ABC = 90°.\n2. Since angle ABC is inscribed in the circle and equals 90°, by the converse of Thales' theorem, the chord AC subtending it must be a diameter of the circle.\n3. The midpoint of any diameter of a circle is the centre of the circle O. Therefore, the midpoint of diagonal AC is centre O.\n4. Similarly, angle BCD = 90°, so chord BD is also a diameter of the circle, and its midpoint is centre O.\n5. In any rectangle, the diagonals bisect each other, meaning their point of intersection is their common midpoint.\n6. Since the midpoint of each diagonal diameter is the centre O, the point of intersection of the diagonals must be the centre of the circle.",
                "finalAnswer": "Proved: Each diagonal subtends 90° at a vertex and is therefore a diameter of the circle. Their intersection (their common midpoint) is the centre of the circle.",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q21: Let ABCD be a cyclic quadrilateral. Explain why the exterior angle at any vertex is equal to the interior opposite angle (e.g., angle CDE = angle ABC, where E is on extension of CD).",
                "given": "Cyclic quadrilateral ABCD. Side CD is extended to point E, forming exterior angle angle CDE.",
                "formula": "Linear pair: angle ADC + angle CDE = 180°. Cyclic quad opposite angles: angle ADC + angle ABC = 180°.",
                "substitution": "Compare both equations summing to 180°.",
                "calculation": "1. Since CDE is a straight line, angle ADC and angle CDE form a linear pair:\n   angle ADC + angle CDE = 180°.\n2. Because ABCD is a cyclic quadrilateral, its opposite angles are supplementary:\n   angle ADC + angle ABC = 180°.\n3. Both expressions equal 180°, so set them equal to each other:\n   angle ADC + angle CDE = angle ADC + angle ABC.\n4. Subtract angle ADC from both sides:\n   angle CDE = angle ABC.\n5. Therefore, the exterior angle at vertex D is exactly equal to the interior opposite angle at vertex B.",
                "finalAnswer": "Proved: angle CDE = angle ABC (Both angles are supplementary to the same angle ADC).",
                "unit": "geometric proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q25: In a circle, two chords CC' and DD' are drawn perpendicular to a diameter AB. Prove that the segment MM' joining the midpoints of the chords CD and C'D' is perpendicular to AB.",
                "given": "Diameter AB perp to chords CC' and DD'. M is midpoint of CD, M' is midpoint of C'D'.",
                "formula": "Reflection symmetry across diameter AB: A diameter perpendicular to a chord reflects the circle and chord onto itself.",
                "substitution": "Set diameter AB as the x-axis.",
                "calculation": "1. Let diameter AB lie along the horizontal x-axis (y = 0).\n2. Since chords CC' and DD' are perpendicular to diameter AB, they are vertical line segments parallel to the y-axis.\n3. By Theorem 5, diameter AB perpendicularly bisects CC' and DD'.\n4. Therefore, point C' is the reflection of C across the x-axis: if C = (x1, y1), then C' = (x1, -y1).\n5. Similarly, D' is the reflection of D across the x-axis: if D = (x2, y2), then D' = (x2, -y2).\n6. Compute midpoint M of segment CD:\n   M = ((x1 + x2)/2, (y1 + y2)/2).\n7. Compute midpoint M' of segment C'D':\n   M' = ((x1 + x2)/2, (-y1 - y2)/2) = ((x1 + x2)/2, -(y1 + y2)/2).\n8. Notice that M and M' have the EXACT same x-coordinate: x_M = x_M' = (x1 + x2)/2.\n9. Therefore, the segment MM' is a vertical line segment.\n10. Since diameter AB lies on the horizontal axis (y = 0) and MM' is vertical, segment MM' is strictly perpendicular to diameter AB.",
                "finalAnswer": "Proved: By reflection symmetry across diameter AB, M and M' have identical x-coordinates, so line segment MM' is perpendicular to diameter AB.",
                "unit": "coordinate symmetry proof",
                "has_diagram": True
            },
            {
                "problem": "End-of-Chapter Q26: How would you use Fig. 5.31 to justify the statement that the sum of the opposite angles of a cyclic quadrilateral is 180°?",
                "given": "Fig. 5.31: Cyclic quadrilateral ABCD inscribed in circle with centre O. Radii OB and OD divide central angle into u (subtending minor arc BAD) and v (subtending major arc BCD). Inscribed angles are p = angle BAD and q = angle BCD.",
                "formula": "Central angle is double the inscribed angle: u = 2q and v = 2p. Central angles form a complete circle: u + v = 360°.",
                "substitution": "Substitute u = 2q and v = 2p into u + v = 360°.",
                "calculation": "1. Consider arc BCD: It subtends central angle u at centre O and inscribed angle p = angle BAD at vertex A.\n   By the Inscribed Angle Theorem: u = 2 * angle BAD = 2p.\n2. Consider arc BAD: It subtends reflex central angle v at centre O and inscribed angle q = angle BCD at vertex C.\n   By the Inscribed Angle Theorem: v = 2 * angle BCD = 2q.\n3. The two central angles u and v together form a complete 360° rotation around the centre O:\n   u + v = 360°.\n4. Substitute u = 2p and v = 2q:\n   2p + 2q = 360°.\n5. Factor out 2:\n   2(p + q) = 360°.\n6. Divide both sides by 2:\n   p + q = 180°.\n7. Since p = angle BAD and q = angle BCD, this proves:\n   angle BAD + angle BCD = 180°.",
                "finalAnswer": "Proved using Fig. 5.31: u = 2q and v = 2p; since u + v = 360°, 2p + 2q = 360° => p + q = 180°, so opposite angles of the cyclic quadrilateral sum to 180°.",
                "unit": "algebraic proof",
                "has_diagram": True
            }
        ]
    }
