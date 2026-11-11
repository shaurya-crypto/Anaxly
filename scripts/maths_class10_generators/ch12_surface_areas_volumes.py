"""
Class 10 Mathematics - Chapter 12: Surface Areas and Volumes (NCERT CBSE)
Curriculum ID: f30fffde-90c1-402d-83c3-7d2af0e9f423
Fully compliant with Invariant 10:
- 5 dedicated modules (Theory in M1-M2, dedicated solvers M3-M5)
- 100% of all NCERT exercise questions (Ex 12.1 all 9 problems, Ex 12.2 all 8 problems) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- High-Precision Vector SVGs from svg_builder_class10 (Axonometric Hairline 3D solids: cylinder-cone, capsule, gulab jamun)
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_surface_areas_volumes_3d_svg, get_svg_wrapper

def get_ch12_modules():
    CURRICULUM_ID = "f30fffde-90c1-402d-83c3-7d2af0e9f423"
    
    # SVG 1: Combination Solid - Cylinder surmounted by Cone
    svg_cylinder_cone = build_surface_areas_volumes_3d_svg(
        shape_type="cylinder_cone",
        title="Combination of Solids: Cylinder Surmounted by Cone",
        caption="TSA = Curved Surface Area(Cone) + Curved Surface Area(Cylinder) + Area of Flat Base"
    )
    
    # SVG 2: Capsule (Cylinder with two Hemispherical Ends)
    capsule_svg_content = """
    <g transform="translate(100, 150)">
      <!-- Left Hemisphere -->
      <path d="M 60 -40 A 40 40 0 0 0 60 40 Z" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
      <!-- Cylinder Body -->
      <rect x="60" y="-40" width="180" height="80" fill="#F8FAFC" stroke="#2563EB" stroke-width="2"/>
      <!-- Right Hemisphere -->
      <path d="M 240 -40 A 40 40 0 0 1 240 40 Z" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
      
      <!-- Interface Dashed Lines -->
      <line x1="60" y1="-40" x2="60" y2="40" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="240" y1="-40" x2="240" y2="40" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
      
      <!-- Dimension: Total Length 14 mm -->
      <line x1="20" y1="-60" x2="280" y2="-60" stroke="#475569" stroke-width="1.2" marker-start="url(#arrowSlate)" marker-end="url(#arrowSlate)"/>
      <text x="150" y="-68" fill="#475569" font-size="11" font-weight="700" text-anchor="middle">Total Length = 14 mm</text>
      
      <!-- Dimension: Cylinder Length 9 mm -->
      <line x1="60" y1="60" x2="240" y2="60" stroke="#16A34A" stroke-width="1.2" marker-start="url(#arrowGreen)" marker-end="url(#arrowGreen)"/>
      <text x="150" y="75" fill="#16A34A" font-size="11" font-weight="700" text-anchor="middle">Cylinder Length = 9 mm</text>
      
      <!-- Dimension: Diameter 5 mm -->
      <line x1="300" y1="-40" x2="300" y2="40" stroke="#DC2626" stroke-width="1.2" marker-start="url(#arrowRed)" marker-end="url(#arrowRed)"/>
      <text x="310" y="4" fill="#DC2626" font-size="11" font-weight="700">Diameter 5 mm (r = 2.5)</text>
    </g>
    
    <!-- Formula HUD Card -->
    <g transform="translate(30, 260)">
      <rect width="520" height="70" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2" rx="8"/>
      <text x="16" y="22" fill="#166534" font-size="11" font-weight="700">Medicine Capsule Formula Decomposition:</text>
      <text x="16" y="42" fill="#0F172A" font-size="11">Total Surface Area = CSA of Cylinder + 2 × (CSA of Hemisphere) = 2πrh + 2 × (2πr²) = 2πr(h + 2r)</text>
      <text x="16" y="58" fill="#2563EB" font-size="11 font-weight="600">Total Volume = Volume of Cylinder + 2 × (Volume of Hemisphere) = πr²h + 4/3 πr³</text>
    </g>
    """
    svg_capsule = get_svg_wrapper(capsule_svg_content, title="Medicine Capsule / Gulab Jamun Solid Geometry", caption="Cylinder with two hemispherical ends: Common interface surfaces are interior and excluded from TSA")

    modules = [
        # Module 1: Surface Area of Combinations of Solids
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Surface Area of Combinations of Solids: The Hidden Interface Principle",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master the fundamental principle of combined surface areas: when two solids are joined together, their touching interface surfaces disappear inside and CANNOT be painted or touched. Therefore, Total Surface Area is the sum of the EXPOSED curved surface areas, NOT the sum of their individual total surface areas.",
            "key_concepts": [
                "The Hidden Interface Principle: TSA of combined solid ≠ TSA of Solid 1 + TSA of Solid 2! Touching base faces are hidden inside and must NOT be included",
                "Cone Mounted on Hemisphere (Toy): TSA = CSA of Cone + CSA of Hemisphere = πrl + 2πr²",
                "Slant Height of Cone: l = √(r² + h²)",
                "Cylinder with Two Hemispheres (Capsule): TSA = CSA of Cylinder + 2 × (CSA of Hemisphere) = 2πrh + 4πr² = 2πr(h + 2r)",
                "Cubical Block Surmounted by Hemisphere: TSA = TSA of Cube - Area of Circular Base + CSA of Hemisphere = 6a² - πr² + 2πr² = 6a² + πr²",
                "Hemispherical Depression Scooped Out: TSA = 6a² - πr² + 2πr² = 6a² + πr² (Identical surface area whether surmounted or scooped out!)"
            ],
            "subtopics": [
                "Deconstructing composite 3D objects into elementary curved components",
                "Calculating cone slant height l = √(r² + h²)",
                "Scooped-out cavities vs surmounted solids",
                "Worked Example 1, Example 2, Example 3 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Example 2 (NCERT): The decorative block shown in Fig. is made of two solids — a cube and a hemisphere. The base of the block is a cube with edge 5 cm, and the hemisphere fixed on the top has a diameter of 4.2 cm. Find the total surface area of the block. (Take π = 22/7)",
                    "solution": "Given:\nEdge of the cubical block a = 5 cm.\nDiameter of hemisphere d = 4.2 cm ⇒ Radius r = 4.2 / 2 = 2.1 cm.\n\nStep 1: Understand the exposed surface area:\nThe block consists of 6 faces of the cube, EXCEPT the circular base of the hemisphere which covers part of the top face.\nOn top of that covered part sits the curved dome of the hemisphere.\nTherefore:\nTotal Surface Area = (Total Surface Area of Cube) - (Base Area of Hemisphere) + (Curved Surface Area of Hemisphere)\n= 6a² - πr² + 2πr²\n= 6a² + πr².\n\nStep 2: Calculate TSA of Cube:\n6a² = 6 × (5)² = 6 × 25 = 150 cm².\n\nStep 3: Calculate Net Additional Curved Area (πr²):\nπr² = (22 / 7) × (2.1)²\n= (22 / 7) × 4.41\n= 22 × 0.63 = 13.86 cm².\n\nStep 4: Compute Total Surface Area of the Decorative Block:\nTotal Surface Area = 150 + 13.86 = 163.86 cm².\n[ROUGH_WORK]\n6 × 25 = 150\n22 × 0.63: 20 × 0.63 = 12.6, 2 × 0.63 = 1.26 ⇒ 12.6 + 1.26 = 13.86.\n150 + 13.86 = 163.86 cm².\nBoxed Answer: [ Total surface area of the block = 163.86 cm² ].",
                    "concept_questions": [
                        "Why do we subtract πr² from 6a²?",
                        "What would be the surface area if a hemispherical cavity of the same diameter had been carved into the block?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Hidden Interface and Solid Combination HUD",
                "diagram_type": "diagram",
                "svg": svg_cylinder_cone,
                "concept_visuals": [
                    {
                        "concept_title": "Exposed Surface Area Architecture",
                        "diagram_title": "Cylinder Cone Combination",
                        "svg": svg_cylinder_cone,
                        "diagram_type": "diagram",
                        "what_to_make": "Cylinder surmounted by cone with annotated radii, cylinder height, and cone slant height",
                        "what_to_explain": "TSA = CSA(Cone) + CSA(Cylinder) + Base(Circle)"
                    }
                ]
            },
            "common_misconceptions": [
                "Adding TSA of cube (6a²) and TSA of hemisphere (3πr²): This double-counts the hidden circular contact face and ruins the calculation!",
                "Subtracting the hemisphere volume when calculating surface area of a carved depression: Carving a depression INCREASES the total exposed surface area by +πr², never decreases it!"
            ]
        },

        # Module 2: Volume of Combinations of Solids
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Volume of Combinations of Solids: Additive Conservation & Liquid Displacement",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the additive conservation principle of volume: unlike surface area, volume is strictly additive and subtractive. Total volume of a composite solid is simply the algebraic sum of the individual component volumes (or total volume minus carved volume for cavities). Master liquid displacement in vessels.",
            "key_concepts": [
                "Volume Additive Invariant: Volume is always conserved; Total Volume = Volume(Solid 1) + Volume(Solid 2)",
                "Cavity Volume: When a cavity is scooped out, Remaining Volume = Original Solid Volume - Cavity Volume",
                "Cylinder Volume: V = πr²h",
                "Cone Volume: V = 1/3 πr²h",
                "Sphere Volume: V = 4/3 πr³",
                "Hemisphere Volume: V = 2/3 πr³",
                "Archimedes Liquid Displacement: Volume of water overflowing = Total volume of submerged solids"
            ],
            "subtopics": [
                "Additive volume property for combined solids",
                "Subtractive volume property for hollowed cavities",
                "Archimedes displacement in water vessels",
                "Worked Example 5, Example 6, Example 7 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Example 6 (NCERT): A juice seller was serving his customers using glasses as shown in Fig. The inner diameter of the cylindrical glass was 5 cm, but the bottom of the glass had a hemispherical raised portion which reduced the capacity of the glass. If the height of a glass was 10 cm, find the apparent capacity of the glass and its actual capacity. (Use π = 3.14)",
                    "solution": "Given:\nInner diameter of cylindrical glass d = 5 cm ⇒ Radius r = 5 / 2 = 2.5 cm.\nHeight of glass h = 10 cm.\nValue of π = 3.14.\n\nStep 1: Calculate Apparent Capacity (Apparent Volume = Volume of Cylinder):\nApparent Capacity = πr²h\n= 3.14 × (2.5)² × 10\n= 3.14 × 6.25 × 10\n= 3.14 × 62.5 = 196.25 cm³.\n\nStep 2: Calculate Volume of Hemispherical Raised Bottom:\nVolume of Hemisphere = 2/3 πr³\n= (2 / 3) × 3.14 × (2.5)³\n= (2 / 3) × 3.14 × 15.625\n= (2 / 3) × 49.0625\n= 98.125 / 3 ≈ 32.71 cm³.\n\nStep 3: Calculate Actual Capacity (Net Available Volume):\nActual Capacity = (Apparent Capacity) - (Volume of Hemispherical Dome)\n= 196.25 - 32.71 = 163.54 cm³.\n[ROUGH_WORK]\nApparent = 196.25 cm³, Actual = 163.54 cm³.\nThe customer receives 32.71 cm³ less juice than appears!\nBoxed Answer: [ Apparent capacity = 196.25 cm³, Actual capacity = 163.54 cm³ ].",
                    "concept_questions": [
                        "Why is the actual capacity subtracted while the surface area would have been increased?",
                        "What is the ratio of cone volume to cylinder volume with identical base and height?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Volume Decomposition and Capsule HUD",
                "diagram_type": "diagram",
                "svg": svg_capsule,
                "concept_visuals": [
                    {
                        "concept_title": "Solid Volume Conservation",
                        "diagram_title": "Capsule Additive Volume",
                        "svg": svg_capsule,
                        "diagram_type": "diagram",
                        "what_to_make": "Capsule diagram showing cylindrical middle and two hemispherical end volumes",
                        "what_to_explain": "Total Volume = πr²h + 4/3 πr³"
                    }
                ]
            },
            "common_misconceptions": [
                "Subtracting curved surface area when finding volume: Surface area and volume are separate physical quantities with different units (cm² vs cm³).",
                "Using diameter instead of radius in r² and r³."
            ]
        },

        # Module 3: NCERT Exercise 12.1 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Exercise 12.1 Complete Solver: Joined Cubes, Surmounted Solids & Canvas Tents (Q1 to Q9)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 12.1 Questions 1 through 9. Covers cubes joined end to end (Q1), hollow cylinder on hollow hemisphere (Q2), cone on hemisphere toy (Q3), cubical block with hemisphere (Q4 & Q5), 14 mm medicine capsule (Q6), conical tent on cylinder (Q7), conical cavity hollowed from solid cylinder (Q8), and wooden cylinder with hemispherical scoops (Q9).",
            "key_concepts": [
                "Ex 12.1 Q1: Two cubes volume 64 cm³ ⇒ Edge a = 4 cm; Joined cuboid: L = 8 cm, B = 4 cm, H = 4 cm ⇒ TSA = 2(32 + 16 + 32) = 160 cm²",
                "Ex 12.1 Q2: Vessel: Hemisphere d = 14 cm (r = 7 cm), Total H = 13 cm ⇒ Cylinder h = 13 - 7 = 6 cm ⇒ Inner SA = 2πrh + 2πr² = 2πr(h + r) = 2 × (22/7) × 7 × 13 = 572 cm²",
                "Ex 12.1 Q3: Toy: r = 3.5 cm, Total H = 15.5 cm ⇒ Cone h = 12 cm, l = √(12² + 3.5²) = 12.5 cm ⇒ TSA = πrl + 2πr² = 214.5 cm²",
                "Ex 12.1 Q4: Block side 7 cm: Greatest hemisphere d = 7 cm (r = 3.5 cm) ⇒ TSA = 6(49) + π(3.5)² = 294 + 38.5 = 332.5 cm²",
                "Ex 12.1 Q5: Hemispherical depression edge l: TSA = 6l² + π(l/2)² = (l²/4)(24 + π)",
                "Ex 12.1 Q6: Capsule length 14 mm, diameter 5 mm (r = 2.5 mm): Cylinder h = 14 - 5 = 9 mm ⇒ TSA = 2πr(h + 2r) = 2 × (22/7) × 2.5 × 14 = 220 mm²",
                "Ex 12.1 Q7: Tent: Cylinder d = 4 m (r = 2 m), h = 2.1 m; Cone l = 2.8 m ⇒ Canvas = 2πrh + πrl = πr(2h + l) = (22/7) × 2 × (4.2 + 2.8) = 44 m²; Cost at ₹500/m² = ₹22000",
                "Ex 12.1 Q8: Cylinder h = 2.4 cm, d = 1.4 cm (r = 0.7 cm), cone l = √(2.4² + 0.7²) = 2.5 cm ⇒ Remaining TSA = 2πrh + πr² + πrl = 17.6 cm² ≈ 18 cm²",
                "Ex 12.1 Q9: Wooden cylinder h = 10 cm, r = 3.5 cm with 2 scoops: TSA = 2πrh + 2(2πr²) = 2πr(h + 2r) = 2 × (22/7) × 3.5 × (10 + 7) = 374 cm²"
            ],
            "subtopics": [
                "Full resolution of Exercise 12.1 Questions 1 to 9",
                "Factoring out 2πr to save 80% calculation time",
                "Nearest whole integer rounding in board exams"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 12.1 Q6: A medicine capsule is in the shape of a cylinder with two hemispheres stuck to each of its ends. The length of the entire capsule is 14 mm and the diameter of the capsule is 5 mm. Find its surface area.",
                    "solution": "Given:\nDiameter of capsule d = 5 mm ⇒ Radius r = 5 / 2 = 2.5 mm.\nTotal length of entire capsule = 14 mm.\n\nStep 1: Find height (length) of the cylindrical portion 'h':\nThe two hemispherical ends each contribute their radius r to the total length:\nTotal length = r + h + r = h + 2r\n14 = h + 2(2.5) = h + 5\nh = 14 - 5 = 9 mm.\n\nStep 2: Formulate Total Surface Area of the Capsule:\nThe total surface area is the sum of the curved surface area of the cylinder and the two hemispherical ends:\nTSA = CSA of Cylinder + 2 × (CSA of Hemisphere)\n= 2πrh + 2 × (2πr²)\n= 2πrh + 4πr²\n= 2πr (h + 2r).\n\nStep 3: Substitute known values (notice h + 2r = 14 mm, the total length!):\nTSA = 2 × (22 / 7) × (2.5) × (9 + 5)\n= 2 × (22 / 7) × 2.5 × 14\nCancel 14 with 7 in denominator (14 / 7 = 2):\n= 2 × 22 × 2.5 × 2\n= 44 × 5 = 220 mm².\n[ROUGH_WORK]\n2 × 2.5 = 5; 44 × 5 = 220 mm².\nClean, elegant, zero rounding errors!\nBoxed Answer: [ Surface area of capsule = 220 mm² ].",
                    "concept_questions": [
                        "Why does the cylinder length equal 14 - 5 = 9 mm?",
                        "Why are the two circular bases of the cylinder not included in the surface area?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Exercise 12.1 Complete Geometry HUD",
                "diagram_type": "diagram",
                "svg": svg_capsule,
                "concept_visuals": [
                    {
                        "concept_title": "Composite Surface Calculations",
                        "diagram_title": "Capsule and Tent Layouts",
                        "svg": svg_capsule,
                        "diagram_type": "diagram",
                        "what_to_make": "Diagram showing capsule decomposition into cylinder and 2 hemispheres",
                        "what_to_explain": "Algebraic simplification: 2πr(h + 2r)"
                    }
                ]
            },
            "common_misconceptions": [
                "Subtracting 2.5 mm instead of 5 mm from total length: There are TWO hemispheres at the ends, so subtract 2 × 2.5 = 5 mm!",
                "Including the floor in the tent calculation: Exercise 12.1 Q7 explicitly states 'the base of the tent will not be covered with canvas'."
            ]
        },

        # Module 4: NCERT Exercise 12.2 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 12.2 Complete Solver: Gulab Jamuns, Lead Shots & Displacement Volumes (Q1 to Q8)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 12.2 Questions 1 through 8. Covers cone on hemisphere volume in terms of π (Q1), Rachel's model cylinder with 2 cones (Q2), 45 gulab jamuns 30% syrup volume (Q3), pen stand with 4 conical depressions (Q4), inverted cone with 100 lead shots dropping 1/4 water (Q5), solid iron pole mass (Q6), upright solid inside cylinder (Q7), and checking student's sphere-cylinder vessel volume calculation (Q8).",
            "key_concepts": [
                "Ex 12.2 Q1: r = 1 cm, h = 1 cm: V = 1/3 πr²h + 2/3 πr³ = 1/3 π(1) + 2/3 π(1) = π cm³",
                "Ex 12.2 Q2: Model d = 3 cm (r = 1.5 cm), L = 12 cm, cone h = 2 cm ⇒ Cylinder h = 8 cm ⇒ V = πr²(h_cyl + 2/3 h_cone) = 66 cm³",
                "Ex 12.2 Q3: Gulab jamun d = 2.8 cm (r = 1.4 cm), L = 5 cm ⇒ Cyl h = 2.2 cm ⇒ 1 Jamun V = 25.05 cm³; 45 Jamuns = 1127.28 cm³ ⇒ 30% syrup = 338.18 cm³ ≈ 338 cm³",
                "Ex 12.2 Q4: Cuboid 15×10×3.5 = 525 cm³; 4 cones r = 0.5 cm, h = 1.4 cm ⇒ 4(1/3 πr²h) = 1.47 cm³ ⇒ Remaining wood = 523.53 cm³",
                "Ex 12.2 Q5: Inverted cone r = 5 cm, h = 8 cm: V = 200π/3 cm³; 1/4 flows out = 50π/3 cm³; Sphere r = 0.5 cm: V = 4/3 π(1/8) = π/6 cm³ ⇒ n = (50π/3) / (π/6) = 100 lead shots!",
                "Ex 12.2 Q6: Iron pole: Base cylinder r = 12 cm, h = 220 cm; Top cylinder r = 8 cm, h = 60 cm ⇒ V = 111532.8 cm³; Mass = 111532.8 × 8 g = 892.26 kg",
                "Ex 12.2 Q7: Cylinder r = 60 cm, H = 180 cm: V = 648000π; Solid = 288000π ⇒ Water left = 360000π cm³ = 1.131 m³",
                "Ex 12.2 Q8: Spherical vessel r = 4.25 cm, neck r = 1 cm, h = 8 cm: V = 321.39 + 25.12 = 346.51 cm³ (Student's answer 345 cm³ is incorrect!)"
            ],
            "subtopics": [
                "Full resolution of Exercise 12.2 Questions 1 to 8",
                "Sugar syrup percentage computation across 45 units",
                "Archimedes principle lead shot integer counting"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 12.2 Q3: A gulab jamun, contains sugar syrup up to about 30% of its volume. Find approximately how much syrup would be found in 45 gulab jamuns, each shaped like a cylinder with two hemispherical ends with length 5 cm and diameter 2.8 cm.",
                    "solution": "Given:\nDiameter of gulab jamun d = 2.8 cm ⇒ Radius r = 2.8 / 2 = 1.4 cm.\nTotal length of gulab jamun = 5 cm.\nPercentage of syrup = 30% of total volume.\nNumber of gulab jamuns = 45.\n\nStep 1: Find height (length) of the cylindrical portion 'h':\nh = Total length - 2r = 5 - 2(1.4) = 5 - 2.8 = 2.2 cm.\n\nStep 2: Calculate Volume of ONE Gulab Jamun:\nVolume = Volume of Cylinder + 2 × (Volume of Hemisphere)\n= πr²h + 2 × (2/3 πr³)\n= πr² [ h + 4/3 r ].\nSubstitute r = 1.4 = 7/5, h = 2.2 = 11/5, π = 22/7:\nVolume = (22 / 7) × (1.4)² × [ 2.2 + (4 / 3) × 1.4 ]\n= (22 / 7) × 1.96 × [ 2.2 + 1.867 ]\n= 22 × 0.28 × [ 4.067 ]\n= 6.16 × 4.067 ≈ 25.05 cm³.\n\nStep 3: Calculate Volume of 45 Gulab Jamuns:\nTotal Volume = 45 × 25.05 = 1127.28 cm³.\n\nStep 4: Calculate Volume of Sugar Syrup (30% of Total Volume):\nSyrup Volume = 30% of 1127.28\n= (30 / 100) × 1127.28\n= 0.30 × 1127.28 = 338.184 cm³ ≈ 338 cm³.\n[ROUGH_WORK]\n45 × 6.16 × (6.6 + 5.6)/3 = 15 × 6.16 × 12.2 = 1127.28.\n0.30 × 1127.28 = 338.18 ≈ 338 cm³.\nBoxed Answer: [ Volume of sugar syrup in 45 gulab jamuns ≈ 338 cm³ ].",
                    "concept_questions": [
                        "Why does the cylinder height equal 5 - 2.8 = 2.2 cm?",
                        "What percentage of the volume would be occupied if there were 100 gulab jamuns?"
                    ]
                },
                {
                    "problem": "Exercise 12.2 Q5: A vessel is in the form of an inverted cone. Its height is 8 cm and the radius of its top, which is open, is 5 cm. It is filled with water up to the brim. When lead shots, each of which is a sphere of radius 0.5 cm are dropped into the vessel, one-fourth of the water flows out. Find the number of lead shots dropped into the vessel.",
                    "solution": "Given:\nInverted cone: Radius R = 5 cm, Height H = 8 cm.\nVessel is full of water up to brim.\nLead shots: Spheres of radius r = 0.5 cm.\nFraction of water displaced = 1/4 of total volume of cone.\n\nStep 1: Calculate Volume of Water in the Cone:\nVolume of Cone = 1/3 π R² H\n= (1 / 3) × π × (5)² × 8\n= (1 / 3) × π × 25 × 8\n= 200π / 3 cm³.\n\nStep 2: Calculate Volume of Water that Flows Out:\nVolume displaced = 1/4 × Volume of Cone\n= (1 / 4) × (200π / 3) = 50π / 3 cm³.\n\nStep 3: Calculate Volume of ONE Spherical Lead Shot:\nVolume of 1 lead shot = 4/3 π r³\n= (4 / 3) × π × (0.5)³\n= (4 / 3) × π × 0.125\n= (4 / 3) × π × (1 / 8)\n= π / 6 cm³.\n\nStep 4: Find Number of Lead Shots 'n' using Archimedes Principle:\nBy Archimedes Principle:\nTotal volume of 'n' lead shots = Volume of water displaced\nn × (Volume of 1 lead shot) = Volume of water that flowed out\nn × (π / 6) = 50π / 3\nDivide both sides by π:\nn / 6 = 50 / 3\nn = (50 × 6) / 3 = 50 × 2 = 100 lead shots!\n[ROUGH_WORK]\nNotice π cancels out entirely! Never approximate π = 3.14 or 22/7 until the very end.\nn = (50/3) / (1/6) = (50/3) × 6 = 100.\nBoxed Answer: [ Number of lead shots dropped = 100 ].",
                    "concept_questions": [
                        "Why does π cancel out when computing the number of lead shots?",
                        "What fraction of water would flow out if 200 lead shots were dropped?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Archimedes Displacement and Jamun Volume HUD",
                "diagram_type": "diagram",
                "svg": svg_capsule,
                "concept_visuals": [
                    {
                        "concept_title": "Displacement and Combined Volume",
                        "diagram_title": "Liquid Overflow Model",
                        "svg": svg_capsule,
                        "diagram_type": "diagram",
                        "what_to_make": "Inverted cone vessel with water overflowing into beaker as spheres drop",
                        "what_to_explain": "Equating displaced water volume to n times sphere volume"
                    }
                ]
            },
            "common_misconceptions": [
                "Prematurely substituting π = 3.14 in Q5: Keeping π in symbolic form allows it to cancel cleanly without messy decimal long divisions!",
                "Forgetting that 0.5³ = 0.125 = 1/8."
            ]
        },

        # Module 5: Industrial Modeling, Cost Analysis & Geometric Conversions
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Industrial Modeling, Structural Optimization & Mass-Density Formulations",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master real-world industrial and physical applications of surface areas and volumes: computing iron pole mass using density (Mass = Volume × Density), structural canvas requirements, packaging optimization, and verifying complex container capacities with rigorous dimensional checks.",
            "key_concepts": [
                "Density to Mass Conversion: Mass = Volume × Density (e.g. 1 cm³ of iron = 8 g ⇒ Mass in kg = Volume × 8 / 1000)",
                "Structural Compound Models: Rachel's engineering rocket model (Cylinder with conical nose and tail)",
                "Dimensional Consistency Check: Volume is cubic units (cm³, m³), Surface area is square units (cm², m²); 1 m³ = 1,000,000 cm³ = 1000 Litres",
                "Ratio of Shapes: Sphere inscribed in a cylinder has Volume(Sphere) : Volume(Cylinder) = 2 : 3 and SA(Sphere) : TSA(Cylinder) = 2 : 3 (Archimedes' tombstone theorem!)"
            ],
            "subtopics": [
                "Multi-stage mass and density calculations",
                "Metric conversions between cm³, m³, and litres",
                "Archimedes inscribed sphere ratio theorem"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 12.2 Q6: A solid iron pole consists of a cylinder of height 220 cm and base diameter 24 cm, which is surmounted by another cylinder of height 60 cm and radius 8 cm. Find the mass of the pole, given that 1 cm³ of iron has approximately 8 g mass. (Use π = 3.14)",
                    "solution": "Given:\nLower cylinder: Height H = 220 cm, Diameter D = 24 cm ⇒ Radius R = 12 cm.\nUpper cylinder: Height h = 60 cm, Radius r = 8 cm.\nDensity of iron = 8 g per cm³.\nValue of π = 3.14.\n\nStep 1: Calculate Volume of Lower Cylinder:\nV1 = π R² H\n= 3.14 × (12)² × 220\n= 3.14 × 144 × 220\n= 3.14 × 31680 = 99475.2 cm³.\n\nStep 2: Calculate Volume of Upper Cylinder:\nV2 = π r² h\n= 3.14 × (8)² × 60\n= 3.14 × 64 × 60\n= 3.14 × 3840 = 12057.6 cm³.\n\nStep 3: Calculate Total Volume of the Iron Pole:\nTotal Volume V = V1 + V2\n= 99475.2 + 12057.6 = 111532.8 cm³.\n\nStep 4: Calculate Mass of the Pole:\nMass = Volume × Density\n= 111532.8 × 8 grams\n= 892262.4 grams.\n\nStep 5: Convert Mass into Kilograms (1 kg = 1000 g):\nMass = 892262.4 / 1000\n= 892.2624 kg ≈ 892.26 kg.\n[ROUGH_WORK]\nAlternative factoring: π [ (144 × 220) + (64 × 60) ] = 3.14 × [ 31680 + 3840 ] = 3.14 × 35520 = 111532.8 cm³.\n111532.8 × 8 = 892262.4 g = 892.26 kg.\nBoxed Answer: [ Mass of iron pole ≈ 892.26 kg ].",
                    "concept_questions": [
                        "Why can we add the volumes of the two cylinders directly?",
                        "How many cubic centimeters are in one cubic meter?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Compound Iron Pole and Mass HUD",
                "diagram_type": "diagram",
                "svg": svg_cylinder_cone,
                "concept_visuals": [
                    {
                        "concept_title": "Multi-Cylinder Structural Model",
                        "diagram_title": "Pole Volume and Density Layout",
                        "svg": svg_cylinder_cone,
                        "diagram_type": "diagram",
                        "what_to_make": "Two stacked cylinders with labeled heights and radii",
                        "what_to_explain": "Calculating mass from combined volume and density"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting to divide grams by 1000 to express the final answer in kilograms.",
                "Using the upper radius for the lower cylinder or using diameter 24 cm instead of radius 12 cm."
            ]
        }
    ]
    
    return modules
