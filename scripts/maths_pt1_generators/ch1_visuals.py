"""
scripts/maths_pt1_generators/ch1_visuals.py
Expanded 5 Concept Visuals per Module with Interactive Mafs Graph Configurations for Chapter 1
"""

def get_m1_visuals():
    return [
        {
            "concept_title": "4-Quadrant Cartesian Plane Anatomy",
            "diagram_title": "Quadrant Division & Signs: (+,+), (-,+), (-,-), (+,-)",
            "interactive_math_formula": "Q_I: (+, +), \\; Q_{II}: (-, +), \\; Q_{III}: (-, -), \\; Q_{IV}: (+, -)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-8, 8],
                "y_range": [-8, 8],
                "grid": True,
                "lines": [
                    {"x1": -8, "y1": 0, "x2": 8, "y2": 0, "color": "#38bdf8", "label": "x-axis"},
                    {"x1": 0, "y1": -8, "x2": 0, "y2": 8, "color": "#38bdf8", "label": "y-axis"}
                ],
                "points": [
                    {"x": 4, "y": 4, "label": "Q I: (4, 4)", "color": "#4ade80"},
                    {"x": -4, "y": 4, "label": "Q II: (-4, 4)", "color": "#fb923c"},
                    {"x": -4, "y": -4, "label": "Q III: (-4, -4)", "color": "#f43f5e"},
                    {"x": 4, "y": -4, "label": "Q IV: (4, -4)", "color": "#c084fc"},
                    {"x": 0, "y": 0, "label": "Origin (0,0)", "color": "#facc15"}
                ]
            },
            "image_query": "cartesian plane four quadrants signs coordinates axes",
            "video_query": "cartesian coordinate system quadrants signs origin lesson",
            "what_to_explain": "Walk students through the four quadrants created by the intersection of the two perpendicular axes at the origin (0, 0), noting the invariant sign patterns of abscissa and ordinate."
        },
        {
            "concept_title": "Points on Coordinate Axes",
            "diagram_title": "Axes Equations: y = 0 (x-axis) and x = 0 (y-axis)",
            "interactive_math_formula": "\\text{x-axis: } \\{(x, 0) : x \\in \\mathbb{R}\\}, \\quad \\text{y-axis: } \\{(0, y) : y \\in \\mathbb{R}\\}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-6, 6],
                "y_range": [-6, 6],
                "grid": True,
                "points": [
                    {"x": 5, "y": 0, "label": "(5, 0) on x-axis", "color": "#38bdf8"},
                    {"x": -3, "y": 0, "label": "(-3, 0) on x-axis", "color": "#38bdf8"},
                    {"x": 0, "y": 4, "label": "(0, 4) on y-axis", "color": "#4ade80"},
                    {"x": 0, "y": -5, "label": "(0, -5) on y-axis", "color": "#4ade80"}
                ]
            },
            "image_query": "points on x axis and y axis coordinates zero",
            "video_query": "points lying on axes abscissa ordinate zero coordinates",
            "what_to_explain": "Clarify that any point lying on the horizontal x-axis has ordinate y = 0, and any point on the vertical y-axis has abscissa x = 0."
        },
        {
            "concept_title": "Sindhu-Sarasvati Ancient Urban Grid",
            "diagram_title": "Orthogonal North-South & East-West Street Lattice (10m Spacing)",
            "interactive_math_formula": "\\Delta x = 10\\text{ m}, \\quad \\Delta y = 10\\text{ m}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 5],
                "y_range": [0, 5],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 0, "x2": 1, "y2": 5, "color": "#94a3b8"},
                    {"x1": 2, "y1": 0, "x2": 2, "y2": 5, "color": "#94a3b8"},
                    {"x1": 3, "y1": 0, "x2": 3, "y2": 5, "color": "#94a3b8"},
                    {"x1": 4, "y1": 0, "x2": 4, "y2": 5, "color": "#94a3b8"},
                    {"x1": 0, "y1": 1, "x2": 5, "y2": 1, "color": "#94a3b8"},
                    {"x1": 0, "y1": 2, "x2": 5, "y2": 2, "color": "#94a3b8"},
                    {"x1": 0, "y1": 3, "x2": 5, "y2": 3, "color": "#94a3b8"},
                    {"x1": 0, "y1": 4, "x2": 5, "y2": 4, "color": "#94a3b8"}
                ],
                "points": [{"x": 3, "y": 2, "label": "Warehouse: (3, 2)", "color": "#facc15"}]
            },
            "image_query": "indus valley mohenjo daro planned urban street grid layout",
            "video_query": "ancient indian mathematics indus valley urban grid city planning",
            "what_to_explain": "Connect modern coordinate grids to historical urban engineering in Harappa and Mohenjo-daro, where merchants navigated by counting orthogonal block units from the city center."
        },
        {
            "concept_title": "Projection Distance to Axes",
            "diagram_title": "Perpendicular Distances: |x| from y-axis, |y| from x-axis",
            "interactive_math_formula": "\\text{Dist to y-axis} = |x|, \\quad \\text{Dist to x-axis} = |y|",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-6, 6],
                "y_range": [-6, 6],
                "grid": True,
                "lines": [
                    {"x1": -4, "y1": 0, "x2": -4, "y2": 3, "color": "#f43f5e", "label": "|y| = 3 from x-axis"},
                    {"x1": 0, "y1": 3, "x2": -4, "y2": 3, "color": "#38bdf8", "label": "|x| = 4 from y-axis"}
                ],
                "points": [{"x": -4, "y": 3, "label": "P(-4, 3)", "color": "#facc15"}]
            },
            "image_query": "perpendicular distance of point to coordinate axes diagram",
            "video_query": "distance of point from x axis and y axis explanation",
            "what_to_explain": "Explain that the distance of point P(x, y) from the y-axis is the absolute horizontal coordinate |x|, while distance from the x-axis is |y|."
        },
        {
            "concept_title": "Coordinate Sign Flips across Origin",
            "diagram_title": "Point Reflection: P(x, y) -> P'(-x, -y)",
            "interactive_math_formula": "R_{\\text{origin}}(x, y) = (-x, -y)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-5, 5],
                "y_range": [-5, 5],
                "grid": True,
                "lines": [
                    {"x1": -3, "y1": -4, "x2": 3, "y2": 4, "color": "#c084fc", "label": "Inversion Line through Origin"}
                ],
                "points": [
                    {"x": 3, "y": 4, "label": "P(3, 4)", "color": "#4ade80"},
                    {"x": -3, "y": -4, "label": "P'(-3, -4)", "color": "#f43f5e"},
                    {"x": 0, "y": 0, "label": "Origin", "color": "#facc15"}
                ]
            },
            "image_query": "point reflection through origin coordinate geometry",
            "video_query": "reflection of a point in origin opposite quadrant",
            "what_to_explain": "Show how reflecting a point across the origin negates both coordinates simultaneously, flipping points between Quadrant I and Quadrant III, or Quadrant II and Quadrant IV."
        }
    ]

def get_m2_visuals():
    return [
        {
            "concept_title": "Distance Formula Right-Angled Triangle",
            "diagram_title": "Pythagorean Stepping: Delta x, Delta y and Hypotenuse d",
            "interactive_math_formula": "d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 8],
                "y_range": [0, 7],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 2, "x2": 7, "y2": 2, "color": "#38bdf8", "label": "\\Delta x = 6"},
                    {"x1": 7, "y1": 2, "x2": 7, "y2": 6, "color": "#4ade80", "label": "\\Delta y = 4"},
                    {"x1": 1, "y1": 2, "x2": 7, "y2": 6, "color": "#f43f5e", "label": "d = \\sqrt{52}"}
                ],
                "points": [
                    {"x": 1, "y": 2, "label": "A(1, 2)"},
                    {"x": 7, "y": 6, "label": "B(7, 6)"},
                    {"x": 7, "y": 2, "label": "C(7, 2)"}
                ]
            },
            "image_query": "distance formula pythagorean theorem right triangle cartesian plane",
            "video_query": "distance formula derivation pythagoras theorem coordinate geometry",
            "what_to_explain": "Show that the distance formula is nothing other than the Baudhāyana-Pythagoras theorem applied to the right triangle formed by horizontal and vertical differences."
        },
        {
            "concept_title": "Radial Distance from the Origin",
            "diagram_title": "Pythagorean Triplet: P(-5, 12) at Distance 13 from Origin",
            "interactive_math_formula": "d = \\sqrt{(-5)^2 + (12)^2} = \\sqrt{25 + 144} = 13",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-8, 4],
                "y_range": [-2, 14],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": -5, "y2": 12, "color": "#facc15", "label": "Hypotenuse = 13"},
                    {"x1": 0, "y1": 0, "x2": -5, "y2": 0, "color": "#38bdf8", "label": "Base = |-5| = 5"},
                    {"x1": -5, "y1": 0, "x2": -5, "y2": 12, "color": "#4ade80", "label": "Altitude = 12"}
                ],
                "points": [
                    {"x": 0, "y": 0, "label": "O(0, 0)"},
                    {"x": -5, "y": 12, "label": "P(-5, 12)"}
                ]
            },
            "image_query": "5 12 13 pythagorean triangle origin distance coordinate geometry",
            "video_query": "distance from origin pythagorean triplet 5 12 13 math",
            "what_to_explain": "Demonstrate that the distance of any point (x, y) from the origin simplifies to \\sqrt{x^2 + y^2}, using the classic (5, 12, 13) integer triplet."
        },
        {
            "concept_title": "Baudhāyana Diagonal Rope Theorem",
            "diagram_title": "Sulba Sutra Rope Geometry: Diagonal Square = Sum of Side Squares",
            "interactive_math_formula": "c^2 = a^2 + b^2",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 6],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 1, "x2": 5, "y2": 1, "color": "#38bdf8", "label": "Base a = 4"},
                    {"x1": 5, "y1": 1, "x2": 5, "y2": 4, "color": "#38bdf8", "label": "Height b = 3"},
                    {"x1": 1, "y1": 1, "x2": 5, "y2": 4, "color": "#f43f5e", "label": "Rope Diagonal c = 5"}
                ],
                "points": [{"x": 1, "y": 1}, {"x": 5, "y": 1}, {"x": 5, "y": 4}]
            },
            "image_query": "baudhayana sulba sutra rope diagonal pythagoras geometry",
            "video_query": "baudhayana theorem sulbasutras rope geometry proof",
            "what_to_explain": "Introduce Baudhāyana's Sulba Sutra sutra: the rope stretched along the length of the diagonal produces an area equal to the sum of the areas produced by vertical and horizontal sides."
        },
        {
            "concept_title": "Equidistant Circular Locus",
            "diagram_title": "Circle as the Locus of Constant Distance: x^2 + y^2 = r^2",
            "interactive_math_formula": "x^2 + y^2 = 25 \\implies r = 5",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-6, 6],
                "y_range": [-6, 6],
                "grid": True,
                "curves": [
                    {"fn": "sqrt(25 - x^2)", "color": "#38bdf8", "label": "Upper Semicircle"},
                    {"fn": "-sqrt(25 - x^2)", "color": "#38bdf8", "label": "Lower Semicircle"}
                ],
                "points": [
                    {"x": 3, "y": 4, "label": "(3, 4)"},
                    {"x": -3, "y": 4, "label": "(-3, 4)"},
                    {"x": 4, "y": -3, "label": "(4, -3)"},
                    {"x": 0, "y": 5, "label": "(0, 5)"}
                ]
            },
            "image_query": "circle locus equidistant points origin pythagoras",
            "video_query": "circle definition as locus of points constant distance origin",
            "what_to_explain": "Show students that a circle is simply the set of all points that have the exact same distance r from a central coordinate point."
        },
        {
            "concept_title": "Translation Invariance of Metric Distance",
            "diagram_title": "Distance is Preserved under Rigid Translation",
            "interactive_math_formula": "d(A + v, B + v) = d(A, B)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 10],
                "y_range": [0, 8],
                "grid": True,
                "lines": [
                    {"x1": 1, "y1": 1, "x2": 4, "y2": 5, "color": "#38bdf8", "label": "Segment AB (d = 5)"},
                    {"x1": 5, "y1": 2, "x2": 8, "y2": 6, "color": "#4ade80", "label": "Translated A'B' (d = 5)"}
                ],
                "points": [{"x": 1, "y": 1}, {"x": 4, "y": 5}, {"x": 5, "y": 2}, {"x": 8, "y": 6}]
            },
            "image_query": "rigid transformation translation distance invariance coordinate geometry",
            "video_query": "distance between two points translation invariant",
            "what_to_explain": "Explain that shifting both endpoints by the same displacement vector preserves the length of the segment unchanged."
        }
    ]

def get_m3_visuals():
    return [
        {
            "concept_title": "Reiaan's Room Floor Grid",
            "diagram_title": "Room Boundaries OABC and Door Span D1 R1",
            "interactive_math_formula": "\\text{Door Width} = 11.5 - 8.5 = 3.0\\text{ ft}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 15],
                "y_range": [0, 15],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": 14, "y2": 0, "color": "#38bdf8", "label": "Wall OA (x-axis)"},
                    {"x1": 14, "y1": 0, "x2": 14, "y2": 12, "color": "#38bdf8", "label": "Wall AB"},
                    {"x1": 14, "y1": 12, "x2": 0, "y2": 12, "color": "#38bdf8", "label": "Wall BC"},
                    {"x1": 0, "y1": 12, "x2": 0, "y2": 0, "color": "#38bdf8", "label": "Wall CO (y-axis)"},
                    {"x1": 8.5, "y1": 0, "x2": 11.5, "y2": 0, "color": "#4ade80", "label": "Door D1-R1 (3 ft)"}
                ],
                "points": [
                    {"x": 8.5, "y": 0, "label": "D1(8.5, 0)"},
                    {"x": 11.5, "y": 0, "label": "R1(11.5, 0)"}
                ]
            },
            "image_query": "architectural floor plan coordinate grid room dimensions",
            "video_query": "reading architectural floor plan coordinates high school math",
            "what_to_explain": "Show how Reiaan's room walls align with the coordinate axes, allowing door widths and wall distances to be read directly as coordinate differences."
        },
        {
            "concept_title": "Bathroom Door Swing Clearance Arc",
            "diagram_title": "Circular Arc Swept by Bathroom Door Hinge B1(0, 1.5)",
            "interactive_math_formula": "r = y(B_2) - y(B_1) = 4.0 - 1.5 = 2.5\\text{ ft}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 6],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 1.5, "x2": 0, "y2": 4.0, "color": "#f43f5e", "label": "Closed Door: B1 B2"}
                ],
                "curves": [
                    {"fn": "1.5 + sqrt(2.5^2 - x^2)", "color": "#facc15", "label": "Door Swing Path (r = 2.5 ft)"}
                ],
                "points": [
                    {"x": 0, "y": 1.5, "label": "Hinge B1(0, 1.5)"},
                    {"x": 0, "y": 4.0, "label": "B2(0, 4)"},
                    {"x": 2.5, "y": 1.5, "label": "Fully Open"}
                ]
            },
            "image_query": "door swing clearance circular arc floor plan",
            "video_query": "door swing radius clearance floor plan coordinate math",
            "what_to_explain": "Demonstrate how the 2.5 ft bathroom door swings along a circular arc into the bedroom, checking that it clears nearby furniture like the wardrobe."
        },
        {
            "concept_title": "Rectangular Study Table Footprint",
            "diagram_title": "Four Corners: (8, 9), (11, 9), (11, 7), (8, 7)",
            "interactive_math_formula": "\\text{Width} = 11 - 8 = 3\\text{ ft}, \\quad \\text{Length} = 9 - 7 = 2\\text{ ft}, \\quad \\text{Area} = 6\\text{ sq ft}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [6, 13],
                "y_range": [5, 11],
                "grid": True,
                "lines": [
                    {"x1": 8, "y1": 9, "x2": 11, "y2": 9, "color": "#38bdf8", "label": "Top = 3 ft"},
                    {"x1": 11, "y1": 9, "x2": 11, "y2": 7, "color": "#38bdf8", "label": "Side = 2 ft"},
                    {"x1": 11, "y1": 7, "x2": 8, "y2": 7, "color": "#38bdf8"},
                    {"x1": 8, "y1": 7, "x2": 8, "y2": 9, "color": "#38bdf8"}
                ],
                "points": [
                    {"x": 8, "y": 9, "label": "(8, 9)"},
                    {"x": 11, "y": 9, "label": "(11, 9)"},
                    {"x": 11, "y": 7, "label": "(11, 7)"},
                    {"x": 8, "y": 7, "label": "4th Foot: (8, 7)", "color": "#4ade80"}
                ]
            },
            "image_query": "rectangle corners missing vertex fourth point coordinate plane",
            "video_query": "finding fourth vertex of a rectangle coordinate geometry",
            "what_to_explain": "Explain that in a coordinate-aligned rectangle, opposite sides must be parallel to the axes, uniquely determining the fourth vertex at (8, 7)."
        },
        {
            "concept_title": "Bathroom Fixture Spatial Layout",
            "diagram_title": "Washbasin (3x2 ft) and Toilet (2x3 ft) Placement",
            "interactive_math_formula": "\\text{Area}_{\\text{basin}} = 6\\text{ sq ft}, \\quad \\text{Area}_{\\text{toilet}} = 6\\text{ sq ft}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-6, 2],
                "y_range": [0, 8],
                "grid": True,
                "lines": [
                    {"x1": -5, "y1": 5, "x2": -2, "y2": 5, "color": "#38bdf8"},
                    {"x1": -2, "y1": 5, "x2": -2, "y2": 7, "color": "#38bdf8"},
                    {"x1": -2, "y1": 7, "x2": -5, "y2": 7, "color": "#38bdf8"},
                    {"x1": -5, "y1": 7, "x2": -5, "y2": 5, "color": "#38bdf8", "label": "Washbasin 3x2"},
                    {"x1": -5, "y1": 1, "x2": -3, "y2": 1, "color": "#facc15"},
                    {"x1": -3, "y1": 1, "x2": -3, "y2": 4, "color": "#facc15"},
                    {"x1": -3, "y1": 4, "x2": -5, "y2": 4, "color": "#facc15"},
                    {"x1": -5, "y1": 4, "x2": -5, "y2": 1, "color": "#facc15", "label": "Toilet 2x3"}
                ],
                "points": [{"x": -3.5, "y": 6, "label": "Basin"}, {"x": -4, "y": 2.5, "label": "Toilet"}]
            },
            "image_query": "bathroom fixtures layout grid dimensions coordinate architecture",
            "video_query": "interior design layout coordinate grid planning",
            "what_to_explain": "Show how negative x-coordinates represent the adjacent bathroom space situated to the left of the main bedroom y-axis wall."
        },
        {
            "concept_title": "Accessibility Wheelchair Clearance Standards",
            "diagram_title": "Universal Design: Comparing Door Clearances to 32-inch ADA Standard",
            "interactive_math_formula": "3.0\\text{ ft} = 36\\text{ inches} > 32\\text{ inches (Accessible)}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 5],
                "y_range": [0, 45],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 32, "x2": 5, "y2": 32, "color": "#f43f5e", "label": "Min Wheelchair Standard: 32 in"},
                    {"x1": 1.5, "y1": 0, "x2": 1.5, "y2": 36, "color": "#4ade80", "label": "Room Door: 36 in (3 ft)"},
                    {"x1": 3.5, "y1": 0, "x2": 3.5, "y2": 30, "color": "#fb923c", "label": "Bathroom Door: 30 in (2.5 ft)"}
                ],
                "points": [
                    {"x": 1.5, "y": 36, "label": "36 in (Passes)"},
                    {"x": 3.5, "y": 30, "label": "30 in (Fails ADA)"}
                ]
            },
            "image_query": "wheelchair accessible door width standard 32 inches bar chart",
            "video_query": "wheelchair accessibility doorway width guidelines math",
            "what_to_explain": "Engage students with practical accessibility standards: Reiaan's 36-inch room door is fully wheelchair accessible, but the 30-inch bathroom door requires widening."
        }
    ]

def get_m4_visuals():
    return [
        {
            "concept_title": "Vertical Line Locus Equation x = -5",
            "diagram_title": "Infinitely Many Points with Abscissa -5",
            "interactive_math_formula": "L = \\{(-5, y) : y \\in \\mathbb{R}\\}, \\quad x = -5",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-8, 2],
                "y_range": [-6, 6],
                "grid": True,
                "lines": [
                    {"x1": -5, "y1": -6, "x2": -5, "y2": 6, "color": "#38bdf8", "label": "x = -5 (Parallel to y-axis)"}
                ],
                "points": [
                    {"x": -5, "y": 4, "label": "H1(-5, 4) in Q II", "color": "#4ade80"},
                    {"x": -5, "y": 0, "label": "W(-5, 0) on x-axis", "color": "#facc15"},
                    {"x": -5, "y": -3, "label": "H2(-5, -3) in Q III", "color": "#f43f5e"}
                ]
            },
            "image_query": "vertical line equation x equals constant parallel to y axis graph",
            "video_query": "lines parallel to axes x equals constant coordinate geometry",
            "what_to_explain": "Show that the equation x = -5 represents a straight line parallel to the y-axis, traversing both Quadrants II and III."
        },
        {
            "concept_title": "Polygon RAMP Vertex Configuration",
            "diagram_title": "Trapezoid RAMP: Perpendicular and Parallel Edge Geometry",
            "interactive_math_formula": "R(3, 0), \\; A(0, -2), \\; M(-5, -2), \\; P(-5, 2)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-7, 5],
                "y_range": [-4, 4],
                "grid": True,
                "lines": [
                    {"x1": 3, "y1": 0, "x2": 0, "y2": -2, "color": "#38bdf8", "label": "RA"},
                    {"x1": 0, "y1": -2, "x2": -5, "y2": -2, "color": "#4ade80", "label": "AM (Parallel to x-axis)"},
                    {"x1": -5, "y1": -2, "x2": -5, "y2": 2, "color": "#facc15", "label": "MP (Perpendicular to AM)"},
                    {"x1": -5, "y1": 2, "x2": 3, "y2": 0, "color": "#38bdf8", "label": "PR"}
                ],
                "points": [
                    {"x": 3, "y": 0, "label": "R(3, 0)"},
                    {"x": 0, "y": -2, "label": "A(0, -2)"},
                    {"x": -5, "y": -2, "label": "M(-5, -2)"},
                    {"x": -5, "y": 2, "label": "P(-5, 2)"}
                ]
            },
            "image_query": "polygon vertices coordinates cartesian plane perpendicular sides",
            "video_query": "identifying perpendicular and parallel sides coordinates geometry",
            "what_to_explain": "Guide students to verify that side AM is horizontal (y = -2) while side MP is vertical (x = -5), proving AM and MP are mutually perpendicular."
        },
        {
            "concept_title": "Mirror Symmetry across the x-axis",
            "diagram_title": "Reflection Invariant: P(-5, 2) and M(-5, -2)",
            "interactive_math_formula": "R_{x-\\text{axis}}(x, y) = (x, -y)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-7, 2],
                "y_range": [-4, 4],
                "grid": True,
                "lines": [
                    {"x1": -5, "y1": -2, "x2": -5, "y2": 2, "color": "#f43f5e", "stroke_dash": [4, 4], "label": "Reflection Line"}
                ],
                "points": [
                    {"x": -5, "y": 2, "label": "P(-5, 2) in Q II", "color": "#38bdf8"},
                    {"x": -5, "y": -2, "label": "M(-5, -2) in Q III", "color": "#4ade80"},
                    {"x": -5, "y": 0, "label": "Mirror Plane", "color": "#facc15"}
                ]
            },
            "image_query": "mirror reflection of a point across x axis coordinates",
            "video_query": "reflection of points across x axis coordinate geometry",
            "what_to_explain": "Show how reflecting a point across the horizontal x-axis preserves the x-coordinate while inverting the sign of the y-coordinate."
        },
        {
            "concept_title": "Right Triangle Construction at Z(5, -6)",
            "diagram_title": "Triangle IZN with Orthogonal Legs and Computed Hypotenuse",
            "interactive_math_formula": "d(I, N) = \\sqrt{3^2 + 4^2} = 5",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 8],
                "y_range": [-8, 0],
                "grid": True,
                "lines": [
                    {"x1": 5, "y1": -6, "x2": 5, "y2": -2, "color": "#38bdf8", "label": "Vertical Leg = 4"},
                    {"x1": 5, "y1": -6, "x2": 8, "y2": -6, "color": "#4ade80", "label": "Horizontal Leg = 3"},
                    {"x1": 5, "y1": -2, "x2": 8, "y2": -6, "color": "#f43f5e", "label": "Hypotenuse = 5"}
                ],
                "points": [
                    {"x": 5, "y": -6, "label": "Z(5, -6) [Right Angle]"},
                    {"x": 5, "y": -2, "label": "I(5, -2)"},
                    {"x": 8, "y": -6, "label": "N(8, -6)"}
                ]
            },
            "image_query": "right triangle construction coordinates pythagorean lengths",
            "video_query": "constructing right angled triangle on cartesian coordinate plane",
            "what_to_explain": "Demonstrate that setting right angle at Z(5, -6) with horizontal step 3 and vertical step 4 produces a classic 3-4-5 right triangle."
        },
        {
            "concept_title": "The Positive-Only Coordinate Space",
            "diagram_title": "Why Negative Numbers are Essential for Complete 2D Plane Coverage",
            "interactive_math_formula": "\\text{Quadrant I Only: } \\{(x, y) : x \\ge 0, y \\ge 0\\} = \\frac{1}{4}\\text{ of Plane}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-4, 6],
                "y_range": [-4, 6],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": 6, "y2": 0, "color": "#4ade80", "label": "Active Positive Plane"},
                    {"x1": 0, "y1": 0, "x2": 0, "y2": 6, "color": "#4ade80"}
                ],
                "points": [
                    {"x": 3, "y": 3, "label": "Reachable: (3, 3)", "color": "#4ade80"},
                    {"x": -2, "y": 3, "label": "Unreachable without Negatives", "color": "#f43f5e"},
                    {"x": -2, "y": -2, "label": "Unreachable", "color": "#f43f5e"}
                ]
            },
            "image_query": "quadrant 1 positive numbers cartesian coordinate plane limitation",
            "video_query": "why do we need negative numbers in coordinate geometry",
            "what_to_explain": "Explain that without negative numbers, a coordinate system can only map Quadrant I (one quarter of 2D space), making it impossible to locate points behind, below, or to the left of the origin."
        }
    ]

def get_m5_visuals():
    return [
        {
            "concept_title": "Collinear Points Slope Test",
            "diagram_title": "Slope Equality: M(-3, -4), A(0, 0), G(6, 8)",
            "interactive_math_formula": "m_{MA} = \\frac{0 - (-4)}{0 - (-3)} = \\frac{4}{3}, \\quad m_{AG} = \\frac{8 - 0}{6 - 0} = \\frac{4}{3}",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-5, 8],
                "y_range": [-6, 10],
                "grid": True,
                "lines": [
                    {"x1": -4.5, "y1": -6, "x2": 7.5, "y2": 10, "color": "#38bdf8", "label": "Line: y = (4/3)x"}
                ],
                "points": [
                    {"x": -3, "y": -4, "label": "M(-3, -4)", "color": "#f43f5e"},
                    {"x": 0, "y": 0, "label": "A(0, 0)", "color": "#facc15"},
                    {"x": 6, "y": 8, "label": "G(6, 8)", "color": "#4ade80"}
                ]
            },
            "image_query": "collinear points slope method straight line graph",
            "video_query": "collinearity of three points using slope formula coordinate geometry",
            "what_to_explain": "Show that because the slope from M to A equals the slope from A to G (both 4/3) and they share the common point A, all three points must lie on a single straight line."
        },
        {
            "concept_title": "Non-Collinear Points Area Test",
            "diagram_title": "Points R(-5, -1), B(-2, -5), C(4, -12): Slope Discrepancy",
            "interactive_math_formula": "m_{RB} = \\frac{-4}{3} \\approx -1.33, \\quad m_{BC} = \\frac{-7}{6} \\approx -1.17",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-7, 6],
                "y_range": [-14, 2],
                "grid": True,
                "lines": [
                    {"x1": -5, "y1": -1, "x2": -2, "y2": -5, "color": "#f43f5e", "label": "Slope = -4/3"},
                    {"x1": -2, "y1": -5, "x2": 4, "y2": -12, "color": "#fb923c", "label": "Slope = -7/6"}
                ],
                "points": [
                    {"x": -5, "y": -1, "label": "R(-5, -1)"},
                    {"x": -2, "y": -5, "label": "B(-2, -5)"},
                    {"x": 4, "y": -12, "label": "C(4, -12)"}
                ]
            },
            "image_query": "non collinear points slopes different triangle formed",
            "video_query": "testing collinearity unequal slopes coordinate geometry",
            "what_to_explain": "Demonstrate that because the slope of RB (-4/3) does not match the slope of BC (-7/6), the segment bends at B, proving R, B, and C are NOT collinear."
        },
        {
            "concept_title": "Midpoint Average Formula Geometry",
            "diagram_title": "Centroid of Two Points: M = ((x1+x2)/2, (y1+y2)/2)",
            "interactive_math_formula": "M = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [1, 7],
                "grid": True,
                "lines": [
                    {"x1": 2, "y1": 3, "x2": 4, "y2": 5, "color": "#38bdf8", "label": "Segment ST"}
                ],
                "points": [
                    {"x": 2, "y": 3, "label": "S(2, 3)"},
                    {"x": 3, "y": 4, "label": "M(3, 4) [Midpoint]", "color": "#4ade80"},
                    {"x": 4, "y": 5, "label": "T(4, 5)"}
                ]
            },
            "image_query": "midpoint of a line segment coordinate average geometry",
            "video_query": "midpoint formula derivation visual coordinate geometry",
            "what_to_explain": "Illustrate how the midpoint coordinates are the arithmetic means of the respective abscissae and ordinates of the segment endpoints."
        },
        {
            "concept_title": "Unknown Endpoint Inversion: B = 2M - A",
            "diagram_title": "Extrapolating Unknown Endpoint: A(3, -4), M(-7, 1) -> B(-17, 6)",
            "interactive_math_formula": "x_B = 2x_M - x_A = 2(-7) - 3 = -17, \\quad y_B = 2y_M - y_A = 2(1) - (-4) = 6",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-20, 5],
                "y_range": [-6, 8],
                "grid": True,
                "lines": [
                    {"x1": -17, "y1": 6, "x2": 3, "y2": -4, "color": "#c084fc", "label": "Segment AB with Midpoint M"}
                ],
                "points": [
                    {"x": 3, "y": -4, "label": "A(3, -4)", "color": "#38bdf8"},
                    {"x": -7, "y": 1, "label": "M(-7, 1)", "color": "#facc15"},
                    {"x": -17, "y": 6, "label": "B(-17, 6)", "color": "#f43f5e"}
                ]
            },
            "image_query": "finding missing endpoint given midpoint coordinate geometry",
            "video_query": "find endpoint coordinates given midpoint and one endpoint",
            "what_to_explain": "Show how inverting the midpoint equation allows immediate calculation of the missing endpoint: double the midpoint and subtract the known endpoint."
        },
        {
            "concept_title": "Isosceles Triangle with Vertices in Q3 and Q4",
            "diagram_title": "Symmetric Isosceles Apex at Origin O(0, 0)",
            "interactive_math_formula": "d(O, V_3) = d(O, V_4) = \\sqrt{3^2 + 4^2} = 5",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-5, 5],
                "y_range": [-6, 2],
                "grid": True,
                "lines": [
                    {"x1": 0, "y1": 0, "x2": -3, "y2": -4, "color": "#4ade80", "label": "Leg 1 = 5"},
                    {"x1": 0, "y1": 0, "x2": 3, "y2": -4, "color": "#4ade80", "label": "Leg 2 = 5"},
                    {"x1": -3, "y1": -4, "x2": 3, "y2": -4, "color": "#facc15", "label": "Base = 6"}
                ],
                "points": [
                    {"x": 0, "y": 0, "label": "O(0, 0) [Apex]"},
                    {"x": -3, "y": -4, "label": "V_3(-3, -4) in Q III"},
                    {"x": 3, "y": -4, "label": "V_4(3, -4) in Q IV"}
                ]
            },
            "image_query": "isosceles triangle origin apex vertices quadrants 3 and 4",
            "video_query": "plotting isosceles triangle in quadrants coordinate geometry",
            "what_to_explain": "Show how pairing symmetric points (-3, -4) in Q III and (3, -4) in Q IV with the origin creates an isosceles triangle with equal leg lengths of 5 units."
        }
    ]

def get_m6_visuals():
    return [
        {
            "concept_title": "Segment Trisection Coordinates",
            "diagram_title": "Internal Section 1:2 and 2:1 on Segment A(4, 7) to B(16, -2)",
            "interactive_math_formula": "P = \\left(4 + \\frac{12}{3}, 7 - \\frac{9}{3}\\right) = (8, 4), \\quad Q = (12, 1)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [2, 18],
                "y_range": [-4, 9],
                "grid": True,
                "lines": [
                    {"x1": 4, "y1": 7, "x2": 16, "y2": -2, "color": "#38bdf8", "label": "Segment AB"}
                ],
                "points": [
                    {"x": 4, "y": 7, "label": "A(4, 7)"},
                    {"x": 8, "y": 4, "label": "P(8, 4) [1/3]", "color": "#4ade80"},
                    {"x": 12, "y": 1, "label": "Q(12, 1) [2/3]", "color": "#facc15"},
                    {"x": 16, "y": -2, "label": "B(16, -2)"}
                ]
            },
            "image_query": "points of trisection line segment coordinate geometry 1 to 2 ratio",
            "video_query": "how to find points of trisection of a line segment coordinate geometry",
            "what_to_explain": "Explain that trisection points divide a line segment into three equal parts. P is the midpoint of AQ, and Q is the midpoint of PB."
        },
        {
            "concept_title": "Concentric Circle Distance Test",
            "diagram_title": "Circle Radius r = sqrt(65) centered at Origin",
            "interactive_math_formula": "d(O, A)^2 = 1^2 + (-8)^2 = 65, \\quad d(O, D)^2 = (-5)^2 + 6^2 = 61 < 65",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-10, 10],
                "y_range": [-10, 10],
                "grid": True,
                "curves": [
                    {"fn": "sqrt(65 - x^2)", "color": "#38bdf8", "label": "Circle K (r = sqrt(65))"},
                    {"fn": "-sqrt(65 - x^2)", "color": "#38bdf8"}
                ],
                "points": [
                    {"x": 1, "y": -8, "label": "A(1, -8) ON circle", "color": "#38bdf8"},
                    {"x": -4, "y": 7, "label": "B(-4, 7) ON circle", "color": "#38bdf8"},
                    {"x": -7, "y": -4, "label": "C(-7, -4) ON circle", "color": "#38bdf8"},
                    {"x": -5, "y": 6, "label": "D(-5, 6) INSIDE (d=sqrt(61))", "color": "#4ade80"},
                    {"x": 0, "y": 9, "label": "E(0, 9) OUTSIDE (d=9)", "color": "#f43f5e"}
                ]
            },
            "image_query": "circle points inside on outside distance comparison origin",
            "video_query": "points inside outside or on circle using distance formula",
            "what_to_explain": "Show how comparing the distance of a point from the circle's center to the radius immediately determines whether it lies on, inside, or outside the circle."
        },
        {
            "concept_title": "Triangle Recovery from Midpoint Triangle",
            "diagram_title": "Reconstructing Vertices ABC from Midpoints D(5,1), E(6,5), F(0,3)",
            "interactive_math_formula": "A = D + F - E = (5+0-6, 1+3-5) = (-1, -1)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-3, 14],
                "y_range": [-3, 9],
                "grid": True,
                "lines": [
                    {"x1": -1, "y1": -1, "x2": 11, "y2": 3, "color": "#38bdf8", "label": "Side AB"},
                    {"x1": 11, "y1": 3, "x2": 1, "y2": 7, "color": "#38bdf8", "label": "Side BC"},
                    {"x1": 1, "y1": 7, "x2": -1, "y2": -1, "color": "#38bdf8", "label": "Side CA"},
                    {"x1": 5, "y1": 1, "x2": 6, "y2": 5, "color": "#facc15", "stroke_dash": [3, 3]},
                    {"x1": 6, "y1": 5, "x2": 0, "y2": 3, "color": "#facc15", "stroke_dash": [3, 3]},
                    {"x1": 0, "y1": 3, "x2": 5, "y2": 1, "color": "#facc15", "stroke_dash": [3, 3]}
                ],
                "points": [
                    {"x": -1, "y": -1, "label": "A(-1, -1)", "color": "#4ade80"},
                    {"x": 11, "y": 3, "label": "B(11, 3)", "color": "#4ade80"},
                    {"x": 1, "y": 7, "label": "C(1, 7)", "color": "#4ade80"},
                    {"x": 5, "y": 1, "label": "D(5, 1)"},
                    {"x": 6, "y": 5, "label": "E(6, 5)"},
                    {"x": 0, "y": 3, "label": "F(0, 3)"}
                ]
            },
            "image_query": "triangle recovery from midpoints of sides coordinate geometry",
            "video_query": "finding vertices of triangle given midpoints of sides coordinate math",
            "what_to_explain": "Explain the vector parallelogram shortcut: vertex A equals D + F - E, creating the outer triangle whose side midpoints form triangle DEF."
        },
        {
            "concept_title": "City Grid Street Intersections Uniqueness",
            "diagram_title": "Ordered Pair Coordinates: Intersection (4, 3) != (3, 4)",
            "interactive_math_formula": "(4, 3) \\ne (3, 4)",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [0, 6],
                "y_range": [0, 6],
                "grid": True,
                "lines": [
                    {"x1": 4, "y1": 0, "x2": 4, "y2": 6, "color": "#38bdf8", "label": "4th N-S Street"},
                    {"x1": 0, "y1": 3, "x2": 6, "y2": 3, "color": "#38bdf8", "label": "3rd E-W Street"},
                    {"x1": 3, "y1": 0, "x2": 3, "y2": 6, "color": "#f43f5e", "label": "3rd N-S Street"},
                    {"x1": 0, "y1": 4, "x2": 6, "y2": 4, "color": "#f43f5e", "label": "4th E-W Street"}
                ],
                "points": [
                    {"x": 4, "y": 3, "label": "(4, 3) Intersection", "color": "#38bdf8"},
                    {"x": 3, "y": 4, "label": "(3, 4) Intersection", "color": "#f43f5e"}
                ]
            },
            "image_query": "city street grid ordered pair uniqueness coordinate geometry",
            "video_query": "why ordered pairs order matters 4 comma 3 vs 3 comma 4",
            "what_to_explain": "Highlight why order matters in coordinate geometry: (4, 3) and (3, 4) represent two completely distinct physical crossroads separated by several hundred meters."
        },
        {
            "concept_title": "Square Proof via Equal Sides & Perpendicular Slopes",
            "diagram_title": "Square ABCD: Vertices (2,1), (-1,2), (-2,-1), (1,-2) with Area = 10",
            "interactive_math_formula": "AB^2 = (-1 - 2)^2 + (2 - 1)^2 = 9 + 1 = 10 \\implies \\text{Area} = 10",
            "mafs_graph_config": {
                "type": "cartesian",
                "x_range": [-4, 4],
                "y_range": [-4, 4],
                "grid": True,
                "lines": [
                    {"x1": 2, "y1": 1, "x2": -1, "y2": 2, "color": "#4ade80", "label": "AB = sqrt(10)"},
                    {"x1": -1, "y1": 2, "x2": -2, "y2": -1, "color": "#4ade80", "label": "BC = sqrt(10)"},
                    {"x1": -2, "y1": -1, "x2": 1, "y2": -2, "color": "#4ade80", "label": "CD = sqrt(10)"},
                    {"x1": 1, "y1": -2, "x2": 2, "y2": 1, "color": "#4ade80", "label": "DA = sqrt(10)"},
                    {"x1": 2, "y1": 1, "x2": -2, "y2": -1, "color": "#facc15", "stroke_dash": [3, 3], "label": "Diagonal AC = sqrt(20)"},
                    {"x1": -1, "y1": 2, "x2": 1, "y2": -2, "color": "#facc15", "stroke_dash": [3, 3], "label": "Diagonal BD = sqrt(20)"}
                ],
                "points": [
                    {"x": 2, "y": 1, "label": "A(2, 1)"},
                    {"x": -1, "y": 2, "label": "B(-1, 2)"},
                    {"x": -2, "y": -1, "label": "C(-2, -1)"},
                    {"x": 1, "y": -2, "label": "D(1, -2)"}
                ]
            },
            "image_query": "square proof coordinate plane equal sides equal diagonals area 10",
            "video_query": "prove four points form a square coordinate geometry",
            "what_to_explain": "Guide students through proving ABCD is a square by checking that all 4 sides equal \\sqrt{10} and both diagonals equal \\sqrt{20}, yielding an area of 10 square units."
        }
    ]
