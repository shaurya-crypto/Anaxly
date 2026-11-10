"""
Chapter 5: I’m Up and Down, and Round and Round (Circles)
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

import json
from .svg_builder import build_circle_geometry_svg, build_cyclic_quad_svg, get_svg_wrapper

def get_ch5_modules():
    curriculum_id = "de83f257-aada-4e27-b420-f7884165c990"
    
    # -------------------------------------------------------------
    # MODULE 1: Circle Foundations, Circumcentres & Chord Bisectors
    # -------------------------------------------------------------
    m1_svg = build_circle_geometry_svg(
        radius=100, center=(290, 185),
        chords=[{"p1": (195, 215), "p2": (385, 215), "color": "#2563EB", "width": 2.5, "label": "Chord AB"}],
        triangles=[{"p1": (290, 185), "p2": (195, 215), "p3": (385, 215), "color": "#3B82F6"}],
        points=[
            {"x": 290, "y": 185, "label": "O (Centre)", "color": "#DC2626"},
            {"x": 290, "y": 215, "label": "M (Midpoint)", "color": "#16A34A"},
            {"x": 195, "y": 215, "label": "A", "color": "#2563EB"},
            {"x": 385, "y": 215, "label": "B", "color": "#2563EB"}
        ],
        title="Theorem 4 & 5: Chord Bisector Perpendicularity",
        caption="Perpendicular OM from centre O to chord AB bisects the chord into AM = MB"
    )

    m1 = {
        "order_index": 1,
        "title": "Foundations of Circles: Circumcentres, Congruent Triangles & Perpendicular Chord Bisectors",
        "description": "Establish the Euclidean definition of a circle as the locus of equidistant points. Prove Theorem 1 (three non-collinear points define a unique circumcircle), Theorem 2 (chord and radii form an isosceles triangle), and Theorems 4 & 5 (the perpendicular bisector of a chord passes through the centre).",
        "subtopics": [
            "Geometric definition of a circle, centre, radius, chord, secant, and tangent",
            "Theorem 1: There is one and only one circle passing through three given non-collinear points",
            "Circumcentre location: Inside for acute triangles, at the midpoint of hypotenuse for right triangles, outside for obtuse triangles",
            "Theorem 2: The triangle formed by any chord and the centre of the circle is isosceles",
            "Theorem 4: The line drawn through the centre of a circle to bisect a chord is perpendicular to the chord",
            "Theorem 5 (Converse): The perpendicular from the centre of a circle to a chord bisects the chord"
        ],
        "key_concepts": [
            "Circle Locus Definition: The set of all points in a plane that are at a fixed positive distance (radius r) from a fixed point (centre O).",
            "Circumcentre Invariant: The unique point of concurrency of the three perpendicular bisectors of the sides of a triangle. It is the centre of the circumcircle.",
            "Circumcentre Location Invariant: In an acute-angled triangle, the circumcentre lies strictly inside; in an obtuse-angled triangle, it lies strictly outside; in a right-angled triangle, it lies exactly on the hypotenuse.",
            "Isosceles Radii Theorem: In triangle OAB, OA = OB = r (radii of the same circle). Therefore, angle OAB = angle OBA, making triangle OAB always isosceles.",
            "Perpendicular Bisector Equivalence: OM is perpendicular to AB if and only if AM = MB. Proven via RHS or SSS congruence between triangle OMA and triangle OMB."
        ],
        "success_criteria": "State and prove Theorems 1, 2, 4, and 5 with full geometric congruence proofs and determine circumcentre locations for all triangle types.",
        "chapter_notes": "Always draw radii OA and OB to form two right triangles OMA and OMB. Congruence is the backbone of all circle theorem proofs.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 5.1 Q1 & Q2: (Q1) Draw triangle ABC with AB = 5 cm, angle A = 70 deg, and angle B = 60 deg. Draw its circumcircle. Is the centre inside or outside? (Q2) Draw triangle ABC with AB = 5 cm, angle A = 100 deg, AC = 4 cm. Where is its circumcentre?",
                "given": "Q1: Triangle with angles 70 deg, 60 deg, and 50 deg (Acute). Q2: Triangle with angle 100 deg (Obtuse).",
                "formula": "The circumcentre is the intersection of perpendicular bisectors of the sides. Theorem 1 guarantees uniqueness.",
                "substitution": "Q1: Angles are all < 90 deg. Q2: Angle A = 100 deg > 90 deg.",
                "calculation": "Part (Q1):\nStep 1: In triangle ABC, angle C = 180 - (70 + 60) = 50 deg. All three angles (70, 60, 50) are strictly less than 90 deg, so triangle ABC is an acute-angled triangle.\nStep 2: Construct perpendicular bisectors of sides AB and BC. Their intersection point O is the circumcentre.\nStep 3: Since all angles are acute, O lies strictly INSIDE triangle ABC.\n\nPart (Q2):\nStep 1: Triangle ABC has angle A = 100 deg, which is obtuse (> 90 deg).\nStep 2: Construct the perpendicular bisectors of sides AB and AC. The bisectors diverge within the interior and intersect OUTSIDE the triangle opposite the obtuse angle A.\nStep 3: Therefore, the circumcentre O lies strictly OUTSIDE triangle ABC.",
                "finalAnswer": "Q1: Centre lies INSIDE the triangle; Q2: Centre lies OUTSIDE the triangle",
                "unit": "geometric proof and location",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m1_svg
            },
            {
                "problem": "Exercise 5.2 Q1 & Q2: (Q1) Show that the triangle formed by a chord and the centre of the circle is isosceles. (Q2) Show that if two such isosceles triangles have equal base lengths (equal chords), they are congruent and subtend equal angles at the centre.",
                "given": "Circle with centre O. Chords AB and CD with AB = CD.",
                "formula": "SSS Congruence Criterion and Isosceles Triangle Definition.",
                "substitution": "In triangle OAB: OA = OB = r. In triangle OCD: OC = OD = r. AB = CD.",
                "calculation": "Part (Q1):\nStep 1: Let AB be any chord of a circle with centre O. Join OA and OB.\nStep 2: OA = OB = r, because both segments are radii of the same circle.\nStep 3: Since two sides are equal (OA = OB), triangle OAB is by definition an isosceles triangle, with angle OAB = angle OBA.\n\nPart (Q2):\nStep 1: Consider triangle OAB and triangle OCD where chord AB = chord CD.\nStep 2: Compare sides:\n  OA = OC = r (radii)\n  OB = OD = r (radii)\n  AB = CD (given)\nStep 3: By SSS (Side-Side-Side) Congruence Criterion, triangle OAB is congruent to triangle OCD.\nStep 4: By CPCTC (Corresponding Parts of Congruent Triangles are Congruent), angle AOB = angle COD.\nTherefore, equal chords subtend equal angles at the centre (Theorem 3).",
                "finalAnswer": "Q1: Proven (OA = OB = r => triangle OAB is isosceles); Q2: Proven by SSS congruence (angle AOB = angle COD)",
                "unit": "geometric proof",
                "has_diagram": False
            },
            {
                "problem": "Exercise 5.3 Q1: Prove Theorem 5 (Converse to Theorem 4): The perpendicular from the centre of a circle to a chord bisects the chord.",
                "given": "Circle with centre O. Chord AB. OM is perpendicular to AB with M on AB.",
                "formula": "RHS (Right angle - Hypotenuse - Side) Congruence Criterion.",
                "substitution": "In right triangles OMA and OMB: angle OMA = angle OMB = 90 deg, OA = OB = r, OM = OM.",
                "calculation": "Step 1: Draw radii OA and OB to form two right-angled triangles: triangle OMA and triangle OMB.\nStep 2: In triangle OMA and triangle OMB:\n  - angle OMA = angle OMB = 90 deg (given that OM is perpendicular to AB)\n  - Hypotenuse OA = Hypotenuse OB = r (radii of the same circle)\n  - Side OM = Side OM (common side)\nStep 3: Therefore, by the RHS Congruence Criterion, triangle OMA is congruent to triangle OMB.\nStep 4: By CPCTC, AM = MB.\nStep 5: Hence, the perpendicular OM bisects the chord AB into two equal halves.",
                "finalAnswer": "Proven: AM = MB by RHS congruence between triangle OMA and triangle OMB",
                "unit": "geometric proof",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Assuming the circumcentre is always inside the triangle. In an obtuse-angled triangle, the circumcentre lies outside the triangle!",
            "Confusing the chord length with the arc length. A chord is a straight line segment, whereas an arc is a curved portion of the circumference."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Emphasize that radii OA and OB are always equal (r). Any triangle formed by the centre and a chord has two sides equal to r, making it isosceles. Call write_chalkboard(action='draw_svg_diagram', content='Theorem 4 & 5: Chord Bisector').",
        "visual_lesson_plan": {
            "title": "Chord Geometry & Congruence",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m1_svg,
            "what_to_make": "Circle with centre O, chord AB, perpendicular bisector OM, and radii OA, OB.",
            "concept_visuals": [
                {
                    "concept_title": "Chord Bisector Perpendicularity",
                    "diagram_title": "Circle with Chord Bisector",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m1_svg,
                    "interactive_math_formula": "AM = MB <=> OM perp AB",
                    "mafs_graph_config": {"domain": [-5, 5], "range": [-5, 5]},
                    "image_query": "Circle geometry perpendicular bisector of chord passes through centre",
                    "video_query": "Perpendicular from centre to chord bisects the chord proof",
                    "image_url": "/images/curriculum/ch5_chord_bisector.png",
                    "what_to_make": "Circle showing radii and chord with right angle marker at midpoint.",
                    "what_to_explain": "Walk through RHS congruence of triangles OMA and OMB.",
                    "timing_and_cue": "Display at 02:30 during theorem proof."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Circle Foundations & Chords",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "Where does the circumcentre of an obtuse-angled triangle lie?",
                            "ideal_answer": "Strictly outside the triangle.",
                            "socratic_hint": "Recall how the perpendicular bisectors of the two sides adjacent to the obtuse angle diverge."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What is the maximum number of points at which a circle can intersect a straight line?",
                            "ideal_answer": "At most 2 points (as a secant). If it touches at 1 point, it is a tangent; if 0, it does not intersect.",
                            "socratic_hint": "Consider a line passing through a circle: how many times does it cross the perimeter?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "A chord of length 16 cm is drawn in a circle of radius 10 cm. Find the distance of the chord from the centre.",
                            "ideal_answer": "The perpendicular from the centre bisects the chord: half-chord = 16/2 = 8 cm. By Pythagoras: d^2 + 8^2 = 10^2 => d^2 + 64 = 100 => d^2 = 36 => d = 6 cm.",
                            "socratic_hint": "Apply Pythagoras to the right triangle formed by radius, half-chord, and perpendicular distance."
                        },
                        {
                            "q_num": "Q4",
                            "type": "1-mark True/False",
                            "question": "True or False: Any two chords of equal length in a circle are at equal distances from the centre.",
                            "ideal_answer": "True. This is Theorem 6: Equal chords of a circle are equidistant from the centre.",
                            "socratic_hint": "Recall Theorem 6 regarding equal chords."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Prove that the line joining the midpoints of two parallel chords in a circle passes through the centre.",
                            "ideal_answer": "The perpendicular bisector of any chord passes through the centre of the circle (Theorems 4 & 5). For two parallel chords, their perpendicular bisectors are perpendicular to parallel lines and hence coincide into a single line passing through the centre.",
                            "socratic_hint": "Use the fact that the perpendicular bisector of a chord is unique and must pass through O."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 2: Equidistant Chords & Centre Proximity Theorems
    # -------------------------------------------------------------
    m2_svg = build_circle_geometry_svg(
        radius=100, center=(290, 185),
        chords=[
            {"p1": (205, 125), "p2": (375, 125), "color": "#2563EB", "width": 2.5, "label": "Chord AB (16 cm)"},
            {"p1": (205, 245), "p2": (375, 245), "color": "#16A34A", "width": 2.5, "label": "Chord CD (16 cm)"}
        ],
        points=[
            {"x": 290, "y": 185, "label": "O", "color": "#DC2626"},
            {"x": 290, "y": 125, "label": "E (d = 6 cm)", "color": "#2563EB"},
            {"x": 290, "y": 245, "label": "F (d = 6 cm)", "color": "#16A34A"}
        ],
        title="Theorems 6, 7 & 8: Equidistant Chords & Pythagoras",
        caption="Chords AB = CD = 16 cm are equidistant from centre O: OE = OF = 6 cm (Radius r = 10 cm)"
    )

    m2 = {
        "order_index": 2,
        "title": "Chord Geometry: Equidistant Chords, Proximity Invariants & Baudhāyana-Pythagoras Applications",
        "description": "Prove Theorem 6 (equal chords are equidistant from the centre) and Theorem 7 (converse: chords equidistant from centre have equal length). Discover Theorem 8: of two unequal chords, the larger chord is closer to the centre. Master numerical problems using r^2 = d^2 + (c/2)^2.",
        "subtopics": [
            "Theorem 6: Equal chords of a circle are equidistant from the centre",
            "Theorem 7: Chords equidistant from the centre of a circle are equal in length",
            "Theorem 8: If two chords are unequal, the longer chord is closer to the centre (d_1 < d_2)",
            "The Baudhāyana-Pythagoras formula for circles: r^2 = d^2 + (c/2)^2",
            "Parallel chords on the same side and opposite sides of the centre",
            "Calculating distance between parallel chords of known lengths"
        ],
        "key_concepts": [
            "Equidistant Chord Theorem (Theorem 6): Chords AB and CD have equal length if and only if their perpendicular distances from the centre are equal (d_1 = d_2).",
            "Pythagorean Half-Chord Invariant: In right triangle OEA, OA is the hypotenuse (r), OE is the perpendicular distance (d), and EA is the half-chord (c/2). Thus: r^2 = d^2 + (c/2)^2.",
            "Proximity Inverse Relationship (Theorem 8): As a chord gets closer to the centre (d decreases), its length c increases. The maximum chord length occurs when d = 0, which is the diameter c = 2r.",
            "Distance Between Parallel Chords: If parallel chords are on opposite sides of the centre, the distance between them is d_1 + d_2. If on the same side, the distance is |d_1 - d_2|."
        ],
        "success_criteria": "Apply r^2 = d^2 + (c/2)^2 to solve chord problems, prove Theorems 6 and 7, and compute distances between parallel chords.",
        "chapter_notes": "Emphasize drawing the perpendicular segment from centre O to each chord. Always split chord length in half before substituting into Pythagoras.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 5.5 Q1 & End-of-Chapter Q1: (Ex 5.5 Q1) Find the length of a chord whose distance from the centre is 6 cm in a circle of radius 7 cm. (End-of-Ch Q1) A chord is 5 cm away from the centre in a circle of radius 13 cm. What is its length?",
                "given": "Ex 5.5 Q1: r = 7 cm, d = 6 cm. End-of-Ch Q1: r = 13 cm, d = 5 cm.",
                "formula": "r^2 = d^2 + (c/2)^2 => c/2 = sqrt(r^2 - d^2) => Chord length c = 2 * sqrt(r^2 - d^2).",
                "substitution": "Ex 5.5 Q1: c = 2 * sqrt(7^2 - 6^2); End-of-Ch Q1: c = 2 * sqrt(13^2 - 5^2).",
                "calculation": "Part (Ex 5.5 Q1):\nStep 1: Half-chord length = sqrt(r^2 - d^2) = sqrt(7^2 - 6^2) = sqrt(49 - 36) = sqrt(13) cm.\nStep 2: Total chord length c = 2 * sqrt(13) cm approx 2 * 3.606 = 7.21 cm.\n\nPart (End-of-Ch Q1):\nStep 1: Half-chord length = sqrt(r^2 - d^2) = sqrt(13^2 - 5^2) = sqrt(169 - 25) = sqrt(144) = 12 cm.\nStep 2: Total chord length c = 2 * 12 = 24 cm.",
                "finalAnswer": "Ex 5.5 Q1: 2*sqrt(13) cm (approx 7.21 cm); End-of-Ch Q1: 24 cm",
                "unit": "centimetres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m2_svg
            },
            {
                "problem": "Board-Exam Problem: In a circle of radius 5 cm, AB and CD are two parallel chords of lengths 8 cm and 6 cm respectively. Find the distance between the chords if they lie: (i) on opposite sides of the centre, (ii) on the same side of the centre.",
                "given": "Radius r = 5 cm. Chords AB = 8 cm, CD = 6 cm.",
                "formula": "Perpendicular distances: d_1 = sqrt(r^2 - (AB/2)^2) and d_2 = sqrt(r^2 - (CD/2)^2).",
                "substitution": "d_1 = sqrt(5^2 - 4^2) = sqrt(25 - 16) = sqrt(9) = 3 cm.\nd_2 = sqrt(5^2 - 3^2) = sqrt(25 - 9) = sqrt(16) = 4 cm.",
                "calculation": "Step 1: Calculate distance d_1 for chord AB (8 cm):\n  Half-chord = 8/2 = 4 cm.\n  d_1 = sqrt(5^2 - 4^2) = sqrt(9) = 3 cm.\nStep 2: Calculate distance d_2 for chord CD (6 cm):\n  Half-chord = 6/2 = 3 cm.\n  d_2 = sqrt(5^2 - 3^2) = sqrt(16) = 4 cm.\nStep 3: Case (i) - Chords on OPPOSITE sides of centre:\n  Total distance = d_1 + d_2 = 3 cm + 4 cm = 7 cm.\nStep 4: Case (ii) - Chords on SAME side of centre:\n  Total distance = |d_2 - d_1| = 4 cm - 3 cm = 1 cm.",
                "finalAnswer": "Case (i) Opposite sides: 7 cm; Case (ii) Same side: 1 cm",
                "unit": "centimetres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Forgetting to divide the chord length by 2 before applying the Pythagorean theorem.",
            "Adding the distances when chords are on the same side of the centre (they must be subtracted: |d_1 - d_2|)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Draw the circle with the horizontal diameter. Show how moving away from the diameter shrinks the chord, illustrating Theorem 8. Call write_chalkboard(action='draw_svg_diagram', content='Theorems 6, 7 & 8: Equidistant Chords').",
        "visual_lesson_plan": {
            "title": "Chord Distances & Pythagorean Geometry",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m2_svg,
            "what_to_make": "Circle with two parallel chords showing perpendicular distances from centre.",
            "concept_visuals": [
                {
                    "concept_title": "Equidistant Chords",
                    "diagram_title": "Parallel Chords and Distances",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m2_svg,
                    "interactive_math_formula": "r^2 = d^2 + (c/2)^2",
                    "mafs_graph_config": {"domain": [-6, 6], "range": [-6, 6]},
                    "image_query": "Equidistant chords from centre of circle geometry diagram",
                    "video_query": "Equal chords are equidistant from the centre proof",
                    "image_url": "/images/curriculum/ch5_equidistant_chords.png",
                    "what_to_make": "Circle with two chords and distance segments.",
                    "what_to_explain": "Explain why r^2 = d^2 + (c/2)^2 applies to every chord.",
                    "timing_and_cue": "Show during Pythagoras application."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Equidistant Chords & Proximity",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "Between two chords of lengths 10 cm and 14 cm in the same circle, which chord is closer to the centre?",
                            "ideal_answer": "The 14 cm chord, because by Theorem 8, longer chords are closer to the centre.",
                            "socratic_hint": "As a chord gets closer to the centre, does it get longer or shorter?"
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What is the perpendicular distance from the centre to a diameter of the circle?",
                            "ideal_answer": "0 cm, because the diameter passes directly through the centre.",
                            "socratic_hint": "Where does the diameter lie relative to the centre O?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "A circle has radius 17 cm. Find the length of a chord that is 8 cm from the centre.",
                            "ideal_answer": "Half-chord = sqrt(17^2 - 8^2) = sqrt(289 - 64) = sqrt(225) = 15 cm. Total chord length = 2 * 15 = 30 cm.",
                            "socratic_hint": "Use Pythagoras with hypotenuse 17 and leg 8."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Two equal chords of length 24 cm lie in a circle of radius 13 cm. What is the distance of each chord from the centre?",
                            "ideal_answer": "Half-chord = 12 cm. Distance d = sqrt(13^2 - 12^2) = sqrt(169 - 144) = sqrt(25) = 5 cm.",
                            "socratic_hint": "Apply Pythagoras with hypotenuse 13 and leg 12."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Prove that if two intersecting chords make equal angles with the diameter passing through their point of intersection, the chords are equal.",
                            "ideal_answer": "Drop perpendiculars from centre O to both chords. The right triangles formed with the diameter have equal angles (given) and a common hypotenuse, making them congruent by AAS. Thus, the perpendicular distances from O to the chords are equal. By Theorem 7, chords equidistant from the centre are equal in length.",
                            "socratic_hint": "Drop perpendiculars from the centre to both chords and prove their lengths are equal."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 3: Central & Inscribed Angles: The Arc Angle Doubling Theorem
    # -------------------------------------------------------------
    m3_svg = build_circle_geometry_svg(
        radius=100, center=(290, 185),
        chords=[
            {"p1": (210, 245), "p2": (370, 245), "color": "#2563EB", "width": 2, "label": "Arc AB"},
            {"p1": (210, 245), "p2": (290, 85), "color": "#16A34A", "width": 2, "label": "AP"},
            {"p1": (370, 245), "p2": (290, 85), "color": "#16A34A", "width": 2, "label": "BP"}
        ],
        angles=[
            {"center": (290, 185), "p1": (210, 245), "p2": (370, 245), "label": "2θ = 70°", "color": "#DC2626"},
            {"center": (290, 85), "p1": (210, 245), "p2": (370, 245), "label": "θ = 35°", "color": "#16A34A"}
        ],
        points=[
            {"x": 290, "y": 185, "label": "O (Centre)", "color": "#DC2626"},
            {"x": 290, "y": 85, "label": "P (Circumference)", "color": "#16A34A"},
            {"x": 210, "y": 245, "label": "A", "color": "#2563EB"},
            {"x": 370, "y": 245, "label": "B", "color": "#2563EB"}
        ],
        title="Theorem 9: The Arc Angle Doubling Theorem",
        caption="Angle subtended by arc AB at centre O (angle AOB = 2θ) is double the angle at circumference (angle APB = θ)"
    )

    m3 = {
        "order_index": 3,
        "title": "Central & Inscribed Angles: The Arc Angle Doubling Theorem (angle AOB = 2 angle APB)",
        "description": "Prove the foundational Theorem 9: the angle subtended by an arc at the centre is double the angle subtended by it at any point on the remaining part of the circle. Derive Theorem 10: angles in the same segment are equal, and the angle in a semicircle is a right angle.",
        "subtopics": [
            "Definition of minor arc, major arc, and semicircular arc",
            "Central angle vs Inscribed angle subtended by the same arc",
            "Theorem 9: Rigorous proof of angle AOB = 2 * angle APB across all three cases (minor arc, semicircle, major arc)",
            "Theorem 10: Angles subtended by the same arc in the same segment are equal (angle APB = angle AQB)",
            "Angle in a Semicircle Theorem: The angle subtended by a diameter at any point on the circumference is strictly 90 degrees",
            "Equilateral triangle formed when central angle is 60 degrees (radius = chord length)"
        ],
        "key_concepts": [
            "Arc Angle Doubling Theorem (Theorem 9): angle AOB = 2 * angle APB. Proven by drawing line PO through centre O to point Q, creating two isosceles triangles (OPA and OPB) where exterior angles equal the sum of two equal interior angles (2*alpha and 2*beta).",
            "Same Segment Invariant (Theorem 10): Any two inscribed angles subtended by the same chord on the same side of the circle are equal, because each equals exactly half the same central angle.",
            "Thales' Semicircle Theorem: When arc AB is a semicircle, central angle AOB = 180 degrees. Therefore, inscribed angle APB = 180 / 2 = 90 degrees. Any triangle inscribed in a semicircle with the diameter as hypotenuse is a right triangle.",
            "Reflex Angle Case: When arc AB is a major arc, the central angle is reflex (> 180 degrees), and the angle subtended at the remaining minor arc is obtuse (half the reflex angle)."
        ],
        "success_criteria": "State and prove Theorem 9 for all arc cases, deduce that angles in the same segment are equal, and compute inscribed angles accurately.",
        "chapter_notes": "Theorem 9 is the crown jewel of Euclidean circle geometry. Show the exterior angle trick (exterior angle of triangle equals sum of two opposite interior angles) clearly.",
        "worked_examples": [
            {
                "problem": "Textbook Exercise 5.6 Q1: In a circle with centre O, the central angle AOB is 60 deg. If the radius of the circle is 12 cm, what is the length of the chord AB?",
                "given": "Centre O, central angle angle AOB = 60 deg, radius OA = OB = 12 cm.",
                "formula": "In triangle OAB, OA = OB => angle OAB = angle OBA. Sum of angles in triangle = 180 deg.",
                "substitution": "OA = OB = 12 cm. angle AOB = 60 deg.",
                "calculation": "Step 1: In triangle OAB, OA = OB = 12 cm (radii of the same circle).\nStep 2: Since OA = OB, triangle OAB is isosceles, so angle OAB = angle OBA.\nStep 3: The sum of angles in triangle OAB is 180 deg:\n  angle AOB + angle OAB + angle OBA = 180 deg\n  60 deg + 2 * angle OAB = 180 deg\n  2 * angle OAB = 120 deg => angle OAB = 60 deg.\nStep 4: Since all three angles are 60 deg (angle AOB = angle OAB = angle OBA = 60 deg), triangle OAB is an EQUILATERAL triangle.\nStep 5: Therefore, all three sides are equal:\n  AB = OA = OB = 12 cm.",
                "finalAnswer": "Length of chord AB = 12 cm (triangle OAB is equilateral)",
                "unit": "centimetres",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m3_svg
            },
            {
                "problem": "End-of-Chapter Q2 & Semicircle Application: (End-of-Ch Q2) An arc of a circle subtends an angle of 70 deg at the centre. What angle does it subtend at a point on the remaining part of the circle? (Application) If AB is a diameter and C is any point on the circle, find angle ACB.",
                "given": "Part 1: Central angle angle AOB = 70 deg. Part 2: AB is diameter (central angle = 180 deg).",
                "formula": "Theorem 9: Inscribed angle = (1/2) * Central angle.",
                "substitution": "Part 1: angle APB = (1/2) * 70 deg; Part 2: angle ACB = (1/2) * 180 deg.",
                "calculation": "Part 1:\nStep 1: By Theorem 9, the angle subtended by an arc at any point on the remaining part of the circle is half the angle subtended by it at the centre.\nStep 2: Inscribed angle = 70 deg / 2 = 35 deg.\n\nPart 2:\nStep 1: A diameter is a straight line segment passing through centre O, so it subtends a central angle of 180 deg.\nStep 2: Inscribed angle ACB = 180 deg / 2 = 90 deg.\nStep 3: This proves the celebrated theorem: The angle in a semicircle is a right angle.",
                "finalAnswer": "Part 1: 35 degrees; Part 2: angle ACB = 90 degrees",
                "unit": "degrees",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Doubling the angle at the circumference instead of halving the central angle.",
            "Applying Theorem 9 when the point P lies on the same arc as AB (point P must lie on the REMAINING part of the circle)."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Teach Theorem 9 by drawing the arrow-head diagram. Point out that the central angle is 'open wide' at 2*theta, while the angle at the circumference is 'pinched sharp' at theta. Call write_chalkboard(action='draw_svg_diagram', content='Theorem 9: Arc Angle Doubling').",
        "visual_lesson_plan": {
            "title": "Central & Inscribed Angles",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m3_svg,
            "what_to_make": "Circle with central angle 2*theta and inscribed angle theta.",
            "concept_visuals": [
                {
                    "concept_title": "Arc Angle Doubling Theorem",
                    "diagram_title": "Theorem 9 Visual Proof",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m3_svg,
                    "interactive_math_formula": "angle AOB = 2 * angle APB",
                    "mafs_graph_config": {"domain": [-5, 5], "range": [-5, 5]},
                    "image_query": "Angle subtended by arc at centre is double angle at circumference proof",
                    "video_query": "Circle theorem angle at centre is twice angle at circumference animated",
                    "image_url": "/images/curriculum/ch5_arc_angle_doubling.png",
                    "what_to_make": "Circle showing central angle and inscribed angle with angle arcs.",
                    "what_to_explain": "Walk through exterior angle theorem in triangles OPA and OPB.",
                    "timing_and_cue": "Show during Theorem 9 proof."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Central & Inscribed Angles",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "If an arc subtends an angle of 110 deg at the centre of a circle, what angle does it subtend at the circumference?",
                            "ideal_answer": "55 degrees, because 110 / 2 = 55 degrees (Theorem 9).",
                            "socratic_hint": "Divide the central angle by 2."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why is the angle inscribed in a semicircle always exactly 90 degrees?",
                            "ideal_answer": "Because the diameter subtends a straight angle of 180 degrees at the centre, and by Theorem 9, the angle at the circumference is half: 180 / 2 = 90 degrees.",
                            "socratic_hint": "What is the angle of a straight line at the centre O?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "In a circle, chords AB and CD intersect at right angles inside the circle. If arc AC subtends 40 deg at the centre and arc BD subtends 80 deg at the centre, find the angle between the chords.",
                            "ideal_answer": "The interior intersection angle equals (central angle 1 + central angle 2)/2 = (40 + 80)/2 = 60 degrees.",
                            "socratic_hint": "Use the inscribed angles subtended by arcs AC and BD and the exterior angle of the small triangle."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Conceptual",
                            "question": "Can two angles in the same segment of a circle have different degree measures?",
                            "ideal_answer": "No. By Theorem 10, angles in the same segment of a circle are strictly equal.",
                            "socratic_hint": "Recall Theorem 10."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "In a circle with centre O, triangle ABC is inscribed such that AB is a diameter and angle CAB = 30 deg. Find angle ABC.",
                            "ideal_answer": "Since AB is a diameter, angle ACB = 90 deg (angle in a semicircle). In triangle ABC, angle ABC = 180 - (90 + 30) = 180 - 120 = 60 deg.",
                            "socratic_hint": "First determine angle ACB using the semicircle theorem, then use angle sum in triangle."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 4: Cyclic Quadrilaterals & Opposite Angle Sum 180°
    # -------------------------------------------------------------
    m4_svg = build_cyclic_quad_svg(
        radius=100, center=(290, 185),
        vertices=[(220, 130), (360, 120), (370, 240), (210, 230)],
        opposite_labels={"A": "80°", "B": "110°", "C": "100°", "D": "70°"},
        title="Theorems 11 & 12: Cyclic Quadrilateral Opposite Angles",
        caption="Opposite angles sum to 180°: ∠A + ∠C = 80° + 100° = 180°, ∠B + ∠D = 110° + 70° = 180°"
    )

    m4 = {
        "order_index": 4,
        "title": "Cyclic Quadrilaterals: The 180° Supplementary Angle Theorem & Concyclic Points",
        "description": "Formulate cyclic quadrilaterals where all four vertices lie on a circle. Prove Theorem 11 (the sum of either pair of opposite angles is 180°) and Theorem 12 (converse: if opposite angles sum to 180°, the quadrilateral is cyclic). Master exterior angle properties.",
        "subtopics": [
            "Definition of a cyclic quadrilateral and concyclic points",
            "Theorem 11: The sum of either pair of opposite angles of a cyclic quadrilateral is 180 degrees",
            "Proof of Theorem 11 using the Arc Angle Doubling Theorem (central angles sum to 360 degrees)",
            "Theorem 12: Converse theorem establishing necessary and sufficient conditions for concyclic points",
            "Exterior angle property: An exterior angle of a cyclic quadrilateral equals the interior opposite angle",
            "Special cyclic quadrilaterals: Cyclic parallelograms are rectangles, cyclic trapeziums are isosceles"
        ],
        "key_concepts": [
            "Cyclic Quadrilateral Invariant: A 4-sided polygon whose four vertices lie on a single circumference.",
            "Supplementary Opposite Angles Theorem (Theorem 11): angle A + angle C = 180 degrees and angle B + angle D = 180 degrees. Proof: arc BCD subtends central angle 2*angle A, and arc DAB subtends reflex central angle 2*angle C. The sum of central angles is 360 degrees, so 2*angle A + 2*angle C = 360 degrees => angle A + angle C = 180 degrees.",
            "Exterior Angle Equality: Extending side AB to X forms exterior angle CBX. Since angle ABC + angle ADC = 180 deg and angle ABC + angle CBX = 180 deg (linear pair), exterior angle CBX = interior opposite angle ADC.",
            "Cyclic Parallelogram Theorem: A parallelogram inscribed in a circle must be a rectangle (opposite angles are equal and supplementary => 2*angle A = 180 deg => angle A = 90 deg)."
        ],
        "success_criteria": "Prove Theorems 11 and 12, determine whether four points are concyclic, and solve complex multi-step angle chasing problems.",
        "chapter_notes": "Cyclic quadrilateral questions appear every single year in CBSE board exams. Focus on combining the linear pair with the supplementary property.",
        "worked_examples": [
            {
                "problem": "Textbook Section 5.8 Exercise: A cyclic quadrilateral has angles measuring angle A = 80 deg, angle B = 110 deg, angle C = 100 deg, and angle D = 70 deg. Can such a quadrilateral be drawn? Explain why or why not.",
                "given": "Quadrilateral ABCD with angles: A = 80 deg, B = 110 deg, C = 100 deg, D = 70 deg.",
                "formula": "Theorems 11 & 12: A quadrilateral is cyclic if and only if opposite angle pairs sum to 180 deg.",
                "substitution": "Check pair 1: angle A + angle C. Check pair 2: angle B + angle D.",
                "calculation": "Step 1: Check the first pair of opposite angles (A and C):\n  angle A + angle C = 80 deg + 100 deg = 180 deg.\nStep 2: Check the second pair of opposite angles (B and D):\n  angle B + angle D = 110 deg + 70 deg = 180 deg.\nStep 3: Check the total angle sum of the 4-gon:\n  80 deg + 110 deg + 100 deg + 70 deg = 360 deg.\nStep 4: By Theorem 12 (Converse of Cyclic Quadrilateral Theorem), since both pairs of opposite angles add up to 180 deg, the quadrilateral ABCD CAN be inscribed in a circle (it is cyclic).",
                "finalAnswer": "Yes, such a cyclic quadrilateral can be drawn because opposite angles are supplementary (80+100=180 and 110+70=180)",
                "unit": "geometric verification",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m4_svg
            },
            {
                "problem": "Board-Exam Theorem: Prove that a cyclic parallelogram is a rectangle.",
                "given": "ABCD is a parallelogram inscribed in a circle (cyclic).",
                "formula": "In a parallelogram, opposite angles are equal. In a cyclic quadrilateral, opposite angles sum to 180 deg.",
                "substitution": "angle A = angle C (parallelogram) and angle A + angle C = 180 deg (cyclic).",
                "calculation": "Step 1: Since ABCD is a parallelogram, opposite angles are equal:\n  angle A = angle C.\nStep 2: Since ABCD is cyclic, the sum of opposite angles is 180 deg (Theorem 11):\n  angle A + angle C = 180 deg.\nStep 3: Substitute angle C = angle A into the sum:\n  angle A + angle A = 180 deg\n  2 * angle A = 180 deg => angle A = 90 deg.\nStep 4: Since angle A = 90 deg, opposite angle angle C = 90 deg.\nStep 5: Consecutive angles in a parallelogram are supplementary, so angle B = 180 - 90 = 90 deg, and angle D = 90 deg.\nStep 6: A parallelogram with one (and therefore all) right angles is by definition a RECTANGLE.",
                "finalAnswer": "Proven: Every cyclic parallelogram has all angles equal to 90 degrees, hence it is a rectangle",
                "unit": "geometric proof",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Assuming adjacent angles in a cyclic quadrilateral sum to 180 deg. Only OPPOSITE angles sum to 180 deg (unless it is an inscribed rectangle or trapezium)!",
            "Assuming every quadrilateral can have a circumcircle drawn around it. Only quadrilaterals with supplementary opposite angles are cyclic."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Draw a quadrilateral on the chalkboard and deliberately test if opposite angles sum to 180 deg. If they sum to 179 deg, a circle CANNOT pass through all 4 points. Call write_chalkboard(action='draw_svg_diagram', content='Theorems 11 & 12: Cyclic Quadrilateral').",
        "visual_lesson_plan": {
            "title": "Cyclic Quadrilaterals & Proofs",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m4_svg,
            "what_to_make": "Cyclic quadrilateral showing opposite supplementary angles.",
            "concept_visuals": [
                {
                    "concept_title": "Cyclic Quadrilateral Invariant",
                    "diagram_title": "Supplementary Opposite Angles",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m4_svg,
                    "interactive_math_formula": "angle A + angle C = 180 deg",
                    "mafs_graph_config": {"domain": [-5, 5], "range": [-5, 5]},
                    "image_query": "Cyclic quadrilateral opposite angles sum to 180 proof circle geometry",
                    "video_query": "Opposite angles of cyclic quadrilateral are supplementary proof",
                    "image_url": "/images/curriculum/ch5_cyclic_quadrilateral.png",
                    "what_to_make": "Circle with quadrilateral inscribed and angle values highlighted.",
                    "what_to_explain": "Walk through the central angle sum (360 deg) proof.",
                    "timing_and_cue": "Show during Theorem 11 derivation."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Cyclic Quadrilaterals",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "In cyclic quadrilateral ABCD, if angle A = 2 * angle C, what is angle A?",
                            "ideal_answer": "120 degrees, because angle A + angle C = 180 => 2C + C = 180 => 3C = 180 => C = 60 deg, so A = 120 deg.",
                            "socratic_hint": "Use the fact that angle A and angle C add up to 180 degrees."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "What kind of quadrilateral is an inscribed parallelogram?",
                            "ideal_answer": "A rectangle, because opposite angles are both equal and add up to 180 degrees, making each angle 90 degrees.",
                            "socratic_hint": "If opposite angles are both equal and add to 180, what is each angle?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "An exterior angle of a cyclic quadrilateral is 65 deg. What is the measure of the interior opposite angle?",
                            "ideal_answer": "65 degrees, because an exterior angle of a cyclic quadrilateral equals the interior opposite angle.",
                            "socratic_hint": "Use the linear pair property with the supplementary opposite angle."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "Can a cyclic quadrilateral have angles 95 deg, 105 deg, 85 deg, and 75 deg in order? Check opposite pairs.",
                            "ideal_answer": "Check opposite pairs: 95 + 85 = 180 deg, and 105 + 75 = 180 deg. Yes, it is cyclic.",
                            "socratic_hint": "Add the first and third angles, then add the second and fourth angles."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Prove that an isosceles trapezium is always cyclic.",
                            "ideal_answer": "In an isosceles trapezium ABCD with AB parallel to CD and AD = BC, adjacent angles on the same base are equal: angle A = angle B and angle C = angle D. Consecutive interior angles between parallel lines sum to 180 deg: angle A + angle D = 180 deg. Since angle D = angle C, this gives angle A + angle C = 180 deg. Therefore, opposite angles are supplementary, so the trapezium is cyclic.",
                            "socratic_hint": "Use the equality of base angles in an isosceles trapezium and consecutive interior angles."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 5: Textbook Exercise Solver 1: Ex 5.1 to 5.5 & Chords
    # -------------------------------------------------------------
    m5_svg = build_circle_geometry_svg(
        radius=100, center=(290, 185),
        chords=[{"p1": (190, 205), "p2": (390, 205), "color": "#2563EB", "width": 2.5, "label": "Chord (24 cm)"}],
        points=[
            {"x": 290, "y": 185, "label": "O", "color": "#DC2626"},
            {"x": 290, "y": 205, "label": "M (d = 5 cm)", "color": "#16A34A"}
        ],
        title="Exercise Solver 1: Chords, Distances & Constructions",
        caption="Full step-by-step solutions for Exercises 5.1 through 5.5 and End-of-Chapter Q1-Q6"
    )

    m5 = {
        "order_index": 5,
        "title": "Textbook Exercise Solver 1: Exercises 5.1 to 5.5 & Chord Distance Problems (Complete Solutions)",
        "description": "Complete step-by-step solutions for all questions in Exercises 5.1, 5.2, 5.3, 5.4, 5.5 and End-of-Chapter Q1 through Q6 with zero skipped calculations, full geometric justifications, and explicit formulas.",
        "subtopics": [
            "Exercise 5.1 Q1 to Q3: Circumcircle constructions and circumcentre positioning",
            "Exercise 5.2 Q1 & Q2: Congruence proofs for chord-centre triangles",
            "Exercise 5.3 Q1: Perpendicular chord bisector converse proof",
            "Exercise 5.4 Q1 & Q2: Baudhāyana-Pythagoras theorem applied to chord distances",
            "Exercise 5.5 Q1 & Q2: Chord length calculations and distance invariants",
            "End-of-Chapter Q1 to Q6: Numerical chord problems and diameter relationships"
        ],
        "key_concepts": [
            "Geometric Rigor Invariant: Every geometric statement must have an accompanying justification: (Radii of same circle), (RHS congruence), (CPCTC), or (Pythagoras theorem).",
            "Baudhāyana-Pythagoras Metric: r^2 = d^2 + (c/2)^2. When any two of (radius, distance, chord) are known, the third is uniquely determined.",
            "Concentric Circles Application: A line intersecting two concentric circles at A, B, C, D produces AB = CD because the perpendicular from the common centre bisects both chords AD and BC."
        ],
        "success_criteria": "Solve every question in Exercises 5.1 to 5.5 and End-of-Chapter Q1 to Q6 with complete working.",
        "chapter_notes": "Ensure students state the geometric theorem name for every single inference line.",
        "worked_examples": [
            {
                "problem": "End-of-Chapter Q3: A chord of length 30 cm is drawn at a distance of 8 cm from the centre of a circle. Find the radius of the circle.",
                "given": "Chord length c = 30 cm, Perpendicular distance d = 8 cm.",
                "formula": "r^2 = d^2 + (c/2)^2.",
                "substitution": "Half-chord = 30/2 = 15 cm. d = 8 cm. r = sqrt(8^2 + 15^2).",
                "calculation": "Step 1: The perpendicular from the centre bisects the chord (Theorem 5).\n  Half-chord length = 30 / 2 = 15 cm.\nStep 2: Form right-angled triangle with radius as hypotenuse:\n  r^2 = d^2 + (half-chord)^2\n  r^2 = 8^2 + 15^2\n  r^2 = 64 + 225 = 289.\nStep 3: Take square root:\n  r = sqrt(289) = 17 cm.",
                "finalAnswer": "Radius of the circle = 17 cm",
                "unit": "centimetres",
                "has_diagram": False
            },
            {
                "problem": "End-of-Chapter Q4: A line l intersects two concentric circles (circles with the same centre O) at points A, B, C, and D in order. Prove that AB = CD.",
                "given": "Two concentric circles with centre O. Secant line l meets outer circle at A, D and inner circle at B, C.",
                "formula": "Theorem 5: The perpendicular from the centre of a circle to a chord bisects the chord.",
                "substitution": "Drop perpendicular OM from centre O onto secant line l.",
                "calculation": "Step 1: Draw OM perpendicular to line l, with M lying on the line.\nStep 2: For the OUTER circle, AD is a chord and OM is perpendicular to AD.\n  By Theorem 5, OM bisects chord AD:\n  AM = MD ... (Equation 1)\nStep 3: For the INNER circle, BC is a chord and OM is perpendicular to BC.\n  By Theorem 5, OM bisects chord BC:\n  BM = MC ... (Equation 2)\nStep 4: Subtract Equation 2 from Equation 1:\n  AM - BM = MD - MC\nStep 5: From the figure, AM - BM = AB, and MD - MC = CD.\n  Therefore, AB = CD.",
                "finalAnswer": "Proven: AB = CD by subtracting inner bisected half-chord from outer bisected half-chord",
                "unit": "geometric proof",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m5_svg
            },
            {
                "problem": "End-of-Chapter Q5 & Q6: (Q5) If two circles intersect at two points, prove that their centres lie on the perpendicular bisector of the common chord. (Q6) In a circle of radius 10 cm, find the length of the longest chord.",
                "given": "Q5: Two intersecting circles with common chord AB. Q6: Circle with radius r = 10 cm.",
                "formula": "Q5: SSS and SAS congruence. Q6: Longest chord of a circle is its diameter (c_max = 2r).",
                "substitution": "Q5: Let centres be O and O'. Common chord is AB. Q6: Diameter = 2 * 10 cm.",
                "calculation": "Part (Q5):\nStep 1: Join OA, OB, O'A, O'B, and OO'.\nStep 2: In triangle OAO' and triangle OBO':\n  OA = OB (radii of circle O)\n  O'A = O'B (radii of circle O')\n  OO' = OO' (common side)\n  By SSS congruence, triangle OAO' is congruent to triangle OBO'.\nStep 3: Therefore, angle AOO' = angle BOO' (CPCTC).\nStep 4: Let OO' intersect AB at M. In triangle OAM and triangle OBM:\n  OA = OB (radii), angle AOM = angle BOM, OM = OM (common).\n  By SAS congruence, triangle OAM is congruent to triangle OBM.\nStep 5: Thus AM = MB and angle OMA = angle OMB = 180/2 = 90 deg.\nStep 6: Hence OO' is the perpendicular bisector of the common chord AB.\n\nPart (Q6):\nStep 1: The longest chord of any circle passes through the centre, which is the diameter.\nStep 2: Diameter = 2 * r = 2 * 10 = 20 cm.",
                "finalAnswer": "Q5: Proven (OO' is perpendicular bisector of common chord AB); Q6: Longest chord = 20 cm",
                "unit": "proof and centimetres",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Assuming the distance between centres of intersecting circles is simply the sum of their radii (that only applies to externally touching circles).",
            "Writing the longest chord as anything other than the diameter."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Guide students through concentric circles by having them draw the common perpendicular OM first. The subtraction AM - BM = AB makes the proof effortless. Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 1: Chords').",
        "visual_lesson_plan": {
            "title": "Chord Solutions & Concentric Circles",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m5_svg,
            "what_to_make": "Concentric circles with secant line showing AB = CD.",
            "concept_visuals": [
                {
                    "concept_title": "Concentric Circles Secant Theorem",
                    "diagram_title": "Concentric Circles Secant",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m5_svg,
                    "interactive_math_formula": "AM - BM = MD - MC => AB = CD",
                    "mafs_graph_config": {"domain": [-5, 5], "range": [-5, 5]},
                    "image_query": "Concentric circles secant line AB equals CD proof geometry",
                    "video_query": "Line intersecting two concentric circles prove AB equals CD",
                    "image_url": "/images/curriculum/ch5_concentric_circles.png",
                    "what_to_make": "Two concentric circles with line intersecting at 4 points.",
                    "what_to_explain": "Explain the perpendicular chord bisector subtraction.",
                    "timing_and_cue": "Show before working on the concentric circles proof."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Chord Solutions Mastery",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "What is the length of the longest possible chord in a circle of radius 15 cm?",
                            "ideal_answer": "30 cm, because the longest chord is the diameter (2 * 15 cm = 30 cm).",
                            "socratic_hint": "What is the maximum distance between two points on a circle?"
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why does the perpendicular from the centre to a chord bisect the chord in both circles of a concentric pair?",
                            "ideal_answer": "Because both circles share the exact same centre O, so the perpendicular OM is perpendicular to both chords simultaneously.",
                            "socratic_hint": "What does concentric mean regarding the centre?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "A chord is 12 cm from the centre of a circle of radius 13 cm. What is the length of the chord?",
                            "ideal_answer": "Half-chord = sqrt(13^2 - 12^2) = sqrt(25) = 5 cm. Total chord length = 2 * 5 = 10 cm.",
                            "socratic_hint": "Use Pythagoras with hypotenuse 13 and leg 12."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Problem",
                            "question": "If two equal chords intersect inside a circle, are the segments of one chord equal to the corresponding segments of the other?",
                            "ideal_answer": "Yes, by dropping perpendiculars from the centre to both chords and proving congruence of the resulting triangles.",
                            "socratic_hint": "Think about the symmetry of equal chords about the centre."
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Three girls Reshma, Salma, and Mandip are playing a game by standing on a circle of radius 5 m. Reshma throws a ball to Salma, Salma to Mandip, Mandip to Reshma. If the distance between Reshma and Salma and between Salma and Mandip is 6 m each, what is the distance between Reshma and Mandip?",
                            "ideal_answer": "Let R, S, M be their positions on circle with centre O and radius 5 m. RS = SM = 6 m. Drop perpendicular from O to RS: half-chord = 3 m, distance = sqrt(5^2 - 3^2) = 4 m. Area of triangle ORS = 1/2 * 6 * 4 = 12 m^2. Also Area of triangle ORS = 1/2 * OS * RK = 1/2 * 5 * RK => 12 = 2.5 * RK => RK = 4.8 m. Since RM is perpendicular to OS and bisected at K, RM = 2 * RK = 2 * 4.8 = 9.6 m.",
                            "socratic_hint": "Calculate the area of triangle ORS in two different ways (using base RS and base OS) to find the altitude RK."
                        }
                    ]
                }
            ]
        }
    }

    # -------------------------------------------------------------
    # MODULE 6: Textbook Exercise Solver 2: Ex 5.6 & Review
    # -------------------------------------------------------------
    m6_svg = build_circle_geometry_svg(
        radius=100, center=(290, 185),
        chords=[
            {"p1": (210, 235), "p2": (370, 235), "color": "#2563EB", "width": 2, "label": "AB"},
            {"p1": (210, 235), "p2": (290, 85), "color": "#16A34A", "width": 2, "label": "AC"},
            {"p1": (370, 235), "p2": (290, 85), "color": "#16A34A", "width": 2, "label": "BC"}
        ],
        angles=[{"center": (290, 85), "p1": (210, 235), "p2": (370, 235), "label": "90°", "color": "#DC2626"}],
        points=[
            {"x": 290, "y": 185, "label": "O", "color": "#DC2626"},
            {"x": 290, "y": 85, "label": "C", "color": "#16A34A"},
            {"x": 210, "y": 235, "label": "A", "color": "#2563EB"},
            {"x": 370, "y": 235, "label": "B", "color": "#2563EB"}
        ],
        title="Exercise Solver 2: Inscribed Angles & Cyclic Quad Review",
        caption="Complete solutions for Exercise 5.6 and End-of-Chapter Q7 through Q14"
    )

    m6 = {
        "order_index": 6,
        "title": "Textbook Exercise Solver 2: Inscribed Angles, Cyclic Quads & End-of-Chapter Review (Q7 to Q14)",
        "description": "Exhaustive solutions for Exercise 5.6 and End-of-Chapter questions Q7 through Q14. Solve complex angle chases involving cyclic quadrilaterals, intersecting circles, diameters, and angle bisectors with zero skipped steps.",
        "subtopics": [
            "Exercise 5.6 Q1 to Q3: Central angle and chord relations in equilateral and isosceles triangles",
            "End-of-Chapter Q7 to Q10: Cyclic quadrilaterals with angle chasing and diameter chords",
            "End-of-Chapter Q11 & Q12: Circles drawn on sides of a triangle as diameters",
            "End-of-Chapter Q13 & Q14: Angle bisectors and concyclic quadrilaterals",
            "Synthesis: Combining semicircle right angles with cyclic opposite angle sums",
            "Board-exam high-frequency proofs"
        ],
        "key_concepts": [
            "Angle Chasing Protocol: When solving circle angle problems: (1) Identify all diameters and mark 90 deg inscribed angles. (2) Identify all cyclic quadrilaterals and mark opposite supplementary angles. (3) Identify equal angles subtended by the same arc.",
            "Diameter as Side Theorem: If circles are drawn taking two sides of a triangle as diameters, their point of intersection must lie on the third side. Proof: Inscribed angles from both diameters to the intersection point are each 90 deg, forming a linear pair 90 + 90 = 180 deg.",
            "Cyclic Quadrilateral Angle Bisector Theorem: The quadrilateral formed by the angle bisectors of any quadrilateral is always cyclic."
        ],
        "success_criteria": "Solve every problem in Exercise 5.6 and End-of-Chapter Q7 to Q14 with complete geometric justifications.",
        "chapter_notes": "Angle chasing in circles is highly satisfying when done systematically. Make students list the theorems used in every step.",
        "worked_examples": [
            {
                "problem": "End-of-Chapter Q7 & Q8: (Q7) In a cyclic quadrilateral ABCD, diagonals AC and BD intersect at P. If angle DBC = 70 deg and angle BAC = 30 deg, find angle BCD. Furthermore, if AB = BC, find angle ECD. (Q8) If diagonals of a cyclic quadrilateral are diameters of the circle, prove that it is a rectangle.",
                "given": "Q7: Cyclic quad ABCD, angle DBC = 70 deg, angle BAC = 30 deg, AB = BC. Q8: Diagonals AC and BD are diameters.",
                "formula": "Q7: Angles in the same segment are equal (Theorem 10). Q8: Angle in a semicircle is 90 deg.",
                "substitution": "Q7: angle BDC = angle BAC = 30 deg. In triangle BCD, angles sum to 180 deg. Q8: AC diameter => angle B = angle D = 90 deg.",
                "calculation": "Part (Q7):\nStep 1: By Theorem 10, angles in the same segment are equal:\n  angle BDC = angle BAC = 30 deg (subtended by arc BC).\nStep 2: In triangle BCD, the sum of angles is 180 deg:\n  angle DBC + angle BDC + angle BCD = 180 deg\n  70 deg + 30 deg + angle BCD = 180 deg\n  100 deg + angle BCD = 180 deg => angle BCD = 80 deg.\nStep 3: If AB = BC, in triangle ABC, angle BCA = angle BAC = 30 deg (angles opposite equal sides).\nStep 4: angle ECD = angle BCD - angle BCA = 80 deg - 30 deg = 50 deg.\n\nPart (Q8):\nStep 1: Diagonal AC is a diameter. By Thales' theorem, the angle subtended by a diameter is 90 deg:\n  angle ABC = 90 deg and angle ADC = 90 deg.\nStep 2: Diagonal BD is also a diameter. By the same theorem:\n  angle BAD = 90 deg and angle BCD = 90 deg.\nStep 3: A quadrilateral with all four interior angles equal to 90 degrees is by definition a RECTANGLE.",
                "finalAnswer": "Q7: angle BCD = 80 degrees, angle ECD = 50 degrees; Q8: Proven (all 4 angles are 90 degrees, so ABCD is a rectangle)",
                "unit": "degrees and geometric proof",
                "has_diagram": True,
                "diagram_type": "vector_svg_diagram",
                "diagram_svg": m6_svg
            },
            {
                "problem": "End-of-Chapter Q11 & Q12: (Q11) If circles are drawn taking two sides of a triangle as diameters, prove that the point of intersection of these circles lies on the third side. (Q12) ABC and ADC are two right triangles with common hypotenuse AC. Prove that angle CAD = angle CBD.",
                "given": "Q11: Triangle ABC, circles on AB and AC as diameters intersecting at D. Q12: Right triangles ABC and ADC on hypotenuse AC.",
                "formula": "Q11: Angle in a semicircle is 90 deg and linear pair axiom. Q12: Concyclic points and angles in the same segment.",
                "substitution": "Q11: angle ADB = 90 deg, angle ADC = 90 deg. Q12: angle B + angle D = 90 + 90 = 180 deg => ABCD cyclic.",
                "calculation": "Part (Q11):\nStep 1: Let the two circles on AB and AC as diameters intersect at point D (other than A). Join AD.\nStep 2: Since AB is a diameter of the first circle, angle ADB is an angle in a semicircle:\n  angle ADB = 90 deg.\nStep 3: Since AC is a diameter of the second circle, angle ADC is an angle in a semicircle:\n  angle ADC = 90 deg.\nStep 4: Add the two adjacent angles at D:\n  angle ADB + angle ADC = 90 deg + 90 deg = 180 deg.\nStep 5: Since the sum of adjacent angles is 180 deg, B, D, and C form a straight line (Linear Pair Axiom).\nStep 6: Therefore, the intersection point D lies strictly on the third side BC.\n\nPart (Q12):\nStep 1: Triangle ABC has angle B = 90 deg; triangle ADC has angle D = 90 deg (given right triangles on hypotenuse AC).\nStep 2: Sum of opposite angles: angle B + angle D = 90 deg + 90 deg = 180 deg.\nStep 3: By Theorem 12 (Converse of Cyclic Quadrilateral Theorem), quadrilateral ABCD is cyclic (points A, B, C, D are concyclic on the circle with diameter AC).\nStep 4: In this circle, angles CAD and CBD are subtended by the SAME arc CD.\nStep 5: By Theorem 10, angles in the same segment are equal:\n  angle CAD = angle CBD.",
                "finalAnswer": "Q11: Proven (B-D-C is a straight line); Q12: Proven (angle CAD = angle CBD by same segment theorem)",
                "unit": "geometric proofs",
                "has_diagram": False
            }
        ],
        "common_misconceptions": [
            "Failing to recognize that two right triangles on the same hypotenuse immediately form a cyclic quadrilateral with the hypotenuse as diameter.",
            "Assuming point D in Q11 can be anywhere off the side BC: the 90+90=180 linear pair strictly constrains D to lie on BC."
        ],
        "ai_system_prompt_context": "TEACHING CADENCE: Show students that circles on diameters turn triangles into right angle treasure hunts. Whenever they see a diameter, their pen should immediately draw a 90 deg box at the circumference. Call write_chalkboard(action='draw_svg_diagram', content='Exercise Solver 2: Inscribed Angles').",
        "visual_lesson_plan": {
            "title": "Inscribed Angles & Concyclic Synthesis",
            "diagram_type": "vector_svg_diagram",
            "diagram_svg": m6_svg,
            "what_to_make": "Right triangles with common hypotenuse showing concyclic vertices.",
            "concept_visuals": [
                {
                    "concept_title": "Concyclic Right Triangles",
                    "diagram_title": "Common Hypotenuse Concyclicity",
                    "diagram_type": "vector_svg_diagram",
                    "diagram_svg": m6_svg,
                    "interactive_math_formula": "angle CAD = angle CBD",
                    "mafs_graph_config": {"domain": [-5, 5], "range": [-5, 5]},
                    "image_query": "Two right triangles with common hypotenuse concyclic points geometry",
                    "video_query": "Angle CAD equals angle CBD common hypotenuse proof circle",
                    "image_url": "/images/curriculum/ch5_concyclic_triangles.png",
                    "what_to_make": "Circle with diameter AC and points B and D on circumference.",
                    "what_to_explain": "Explain why both right triangles share the circumcircle with diameter AC.",
                    "timing_and_cue": "Display during common hypotenuse proof."
                }
            ],
            "concept_questions": [
                {
                    "concept_index": 0,
                    "concept_title": "Advanced Circle Geometry",
                    "questions": [
                        {
                            "q_num": "Q1",
                            "type": "1-mark MCQ",
                            "question": "If AC is the diameter of a circle and B is on the circle, what is angle ABC?",
                            "ideal_answer": "90 degrees, because the angle in a semicircle is always a right angle.",
                            "socratic_hint": "Recall Thales' semicircle theorem."
                        },
                        {
                            "q_num": "Q2",
                            "type": "2-mark Short Answer",
                            "question": "Why do the perpendicular bisectors of the sides of a cyclic quadrilateral meet at a single point?",
                            "ideal_answer": "Because the quadrilateral is inscribed in a circle, so all four vertices are equidistant from the centre O. The perpendicular bisector of every chord passes through the centre O.",
                            "socratic_hint": "Where do all perpendicular bisectors of chords in a circle meet?"
                        },
                        {
                            "q_num": "Q3",
                            "type": "2-mark Problem",
                            "question": "In cyclic quad ABCD, angle A = 2x + 4 and angle C = 3x - 14. Find x and angle A.",
                            "ideal_answer": "angle A + angle C = 180 => (2x + 4) + (3x - 14) = 180 => 5x - 10 = 180 => 5x = 190 => x = 38. angle A = 2(38) + 4 = 76 + 4 = 80 degrees.",
                            "socratic_hint": "Set the sum of opposite angles to 180 degrees and solve for x."
                        },
                        {
                            "q_num": "Q4",
                            "type": "2-mark Conceptual",
                            "question": "If the diagonals of a cyclic quadrilateral intersect at right angles, does that mean the quadrilateral is a square?",
                            "ideal_answer": "No. A cyclic quadrilateral can have perpendicular diagonals without being a square (e.g., a cyclic kite or general orthodiagonal cyclic quadrilateral).",
                            "socratic_hint": "Can a kite have all four vertices on a circle?"
                        },
                        {
                            "q_num": "Q5",
                            "type": "3-mark Board Question",
                            "question": "Prove that the quadrilateral formed by the internal angle bisectors of any quadrilateral is cyclic.",
                            "ideal_answer": "Let the angle bisectors of quadrilateral ABCD intersect to form quadrilateral PQRS. In triangle APB, angle APB = 180 - 1/2(angle A + angle B). Opposite angle in PQRS is angle SRQ = angle CRD = 180 - 1/2(angle C + angle D). The sum of these opposite angles is: angle APB + angle CRD = 360 - 1/2(angle A + angle B + angle C + angle D) = 360 - 1/2(360) = 360 - 180 = 180 degrees. Since opposite angles sum to 180 degrees, PQRS is cyclic.",
                            "socratic_hint": "Find the angles of the inner quadrilateral using angle sums in triangles with the angle bisectors."
                        }
                    ]
                }
            ]
        }
    }

    return [m1, m2, m3, m4, m5, m6]
