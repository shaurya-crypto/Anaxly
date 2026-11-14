#!/usr/bin/env python3
"""
Generator for Class 9 Science:
Chapter 4 (Motion), Chapter 5 (Mixtures), and Chapter 6 (Forces)
"""

import os
import json

CH4_ID = "b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae"  # Describing Motion Around Us
CH5_ID = "8d01a5f5-bf82-49c2-9fab-253d26b086f4"  # Exploring Mixtures and their Separation
CH6_ID = "7e1d5438-1174-4577-8599-5f05a6642093"  # How Forces Affect Motion

# ==============================================================================
# CHAPTER 4: DESCRIBING MOTION AROUND US (7 MODULES)
# ==============================================================================
ch4_modules = [
    {
        "curriculum_id": CH4_ID,
        "order_index": 1,
        "title": "Frame of Reference, Relative Motion & The Vector Divide: Distance vs Displacement Mechanics",
        "description": "Master the relativity of motion, reference points (origin), and the foundational distinction between scalar distance and vector displacement in 1D kinematics.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Reference Points & Origin: Why motion is relative to the observer's frame",
            "Motion in a Straight Line: 1D coordinate axis with positive and negative directions",
            "Distance: Total path length traversed by an object (scalar, always positive)",
            "Displacement: Shortest straight-line vector distance from initial to final position (vector, can be zero or negative)",
            "Displacement vs Distance Invariant: Magnitude of displacement is always <= total distance",
            "Zero Displacement Paradox: Closed loops, circular tracks, and round trips"
        ],
        "key_concepts": [
            "Relativity of Motion: An object may be perceived as moving by one observer and stationary by another depending on the reference frame.",
            "Reference Point (Origin): The fixed landmark or coordinate origin from which all spatial positions are measured.",
            "Distance (Scalar): Total ground path covered by a body, possessing magnitude only and never decreasing with time.",
            "Displacement (Vector): Shortest directed straight-line segment from initial position to final position, possessing both magnitude and direction.",
            "Geometric Bound: Displacement magnitude is always less than or equal to distance traveled (|s| <= d); equality holds only for straight line motion without reversing.",
            "Zero Displacement Scenario: When an object returns to its starting point, displacement is exactly zero even if thousands of meters were traveled."
        ],
        "success_criteria": "Student can specify reference frames, calculate distance vs displacement for linear and circular paths, and prove why displacement can be zero while distance is non-zero.",
        "chapter_notes": """### 4.1 Reference Points and the Relativity of Motion
Motion is a change in the position of an object over time **relative to a reference frame**.
- A passenger seated in a moving train appears stationary to a fellow passenger (same reference frame), but appears moving at high speed to an observer on the platform.
- To specify position, we establish a **reference point** called the **Origin ($O$)**.

### 4.2 Distance vs Displacement
| Diagnostic Property | Distance ($d$) | Displacement ($\vec{s}$) |
| :--- | :--- | :--- |
| **Physical Nature** | **Scalar quantity** (Magnitude only) | **Vector quantity** (Magnitude + Direction) |
| **Definition** | Actual length of the entire path traversed | Shortest straight-line distance from Initial ($A$) to Final ($B$) point |
| **Sign & Value** | Always positive ($d > 0$) for moving body; cannot decrease | Can be **positive, zero, or negative** depending on direction |
| **Zero Value** | Cannot be zero if object has moved | **Can be zero** if initial and final positions coincide |
| **Fundamental Invariant** | $d \ge |\vec{s}|$ | $|\vec{s}| \le d$ (Equal only in straight line motion in one direction) |

### 4.3 Classic Examination Scenarios
1. **Circular Track**: An athlete runs around a circular track of radius $r$.
   - For 1 full round: Distance $= 2\pi r$, Displacement $= 0$.
   - For half round: Distance $= \pi r$, Displacement $= 2r$ (diameter).
2. **Farmer along Square Field**: A farmer moves along boundary of square field of side $10\\text{ m}$ in $40\\text{ s}$.
   - Side $= 10\\text{ m}$, Perimeter $= 40\\text{ m}$. Speed $= 1\\text{ m/s}$.
   - In $2\\text{ min } 20\\text{ s} = 140\\text{ s}$: Rounds $= 140/40 = 3.5$.
   - Final position is diagonally opposite: Displacement $= \\sqrt{10^2 + 10^2} = 10\\sqrt{2} \\approx 14.14\\text{ m}$.""",
        "worked_examples": [
            {
                "problem": "An athlete completes one round of a circular track of diameter 200 m in 40 s. What will be the distance covered and the magnitude of displacement at the end of 2 minutes 20 s?",
                "given": "Diameter D = 200 m -> Radius r = 100 m; Time for 1 round T = 40 s; Total elapsed time t = 2 min 20 s = 140 s.",
                "formula": "Distance = Number of rounds * 2*pi*r; Displacement = Vector distance between initial and final position.",
                "substitution": "Rounds n = 140 / 40 = 3.5 rounds. Distance = 3.5 * (2 * pi * 100).",
                "calculation": "1. Distance = 3.5 * 2 * (22/7) * 100 = 3.5 * 628.57 = 2200 m.\\n2. For 3.5 rounds, the athlete completes 3 full rounds (returning to start A) and exactly half a round, landing at point B diametrically opposite to A.\\n3. Displacement is the straight-line diameter connecting A and B = 200 m.",
                "finalAnswer": "Distance covered = 2200 m; Magnitude of displacement = 200 m.",
                "unit": "Metres (m)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 4.2: Athlete running on circular track and Fig. 4.3: Reference point coordinates"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "Displacement can be greater than distance if the object moves fast.",
                "correction": "Displacement is mathematically the straight line connecting two points, which is the shortest possible path in Euclidean geometry. Displacement can never exceed distance.",
                "why_it_matters": "Universal kinematic law tested on every Class 9 examination."
            }
        ],
        "visual_lesson_plan": {
            "title": "Frame of Reference & Vector Divide Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Relativity of Motion: An object may be perceived as moving by one observer and stationary by another depending on the reference frame.",
                    "diagram_title": "Relative Motion & Reference Frame",
                    "diagram_type": "image",
                    "image_query": "Relative motion reference frame train platform diagram",
                    "video_query": "frames of reference relative motion physics",
                    "image_url": "/extracted_diagrams/ch4/fig_4_1.webp",
                    "what_to_make": "Textbook schematic of objects in straight-line motion relative to roadside and train observers.",
                    "timing_and_cue": "Mount reference frame on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_1.webp | Reference Frames | Motion described relative to chosen observer coordinates\")"
                },
                {
                    "concept_title": "Reference Point (Origin): The fixed landmark or coordinate origin from which all spatial positions are measured.",
                    "diagram_title": "1D Linear Coordinate Axis with Origin",
                    "diagram_type": "image",
                    "image_query": "Position coordinates origin number line physics",
                    "video_query": "position vector coordinate origin physics",
                    "image_url": "/extracted_diagrams/ch4/fig_4_3.webp",
                    "what_to_make": "Position axis showing origin O (0 km), point A (25 km), point B (35 km), and point C (60 km).",
                    "timing_and_cue": "Mount coordinate axis on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_3.webp | Position Axis | Measuring linear coordinates from origin reference point O\")"
                },
                {
                    "concept_title": "Distance (Scalar): Total ground path covered by a body, possessing magnitude only and never decreasing with time.",
                    "diagram_title": "Scalar Distance Path Length",
                    "diagram_type": "image",
                    "image_query": "Distance vs displacement path comparison diagram",
                    "video_query": "distance vs displacement scalar vector physics",
                    "image_url": "/extracted_diagrams/ch4/fig_4_4.webp",
                    "what_to_make": "Curvilinear path tracing total ground path length traversed by an object.",
                    "timing_and_cue": "Mount distance on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_4.webp | Distance Path Length | Total scalar ground trajectory traversed\")"
                },
                {
                    "concept_title": "Displacement (Vector): Shortest directed straight-line segment from initial position to final position, possessing both magnitude and direction.",
                    "diagram_title": "Vector Displacement Arrow",
                    "diagram_type": "image",
                    "image_query": "Vector displacement straight line initial final position",
                    "video_query": "displacement vector physics animation",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Displacement_vector.svg",
                    "what_to_make": "Direct straight-line arrow connecting initial point A to final point B across an arbitrary winding path.",
                    "timing_and_cue": "Mount displacement vector on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/4/4d/Displacement_vector.svg | Displacement Vector | Shortest straight-line arrow from start to finish\")"
                },
                {
                    "concept_title": "Geometric Bound: Displacement magnitude is always less than or equal to distance traveled (|s| <= d); equality holds only for straight line motion without reversing.",
                    "diagram_title": "Triangle Inequality of Displacement",
                    "diagram_type": "image",
                    "image_query": "Triangle inequality displacement distance physics",
                    "video_query": "why displacement is less than distance",
                    "image_url": "/extracted_diagrams/ch4/fig_4_2.webp",
                    "what_to_make": "Athlete running path demonstrating that the straight-line chord is always shorter than or equal to the perimeter arc.",
                    "timing_and_cue": "Mount geometric bound on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_2.webp | Geometric Bound | Magnitude of displacement is always <= total distance\")"
                },
                {
                    "concept_title": "Zero Displacement Scenario: When an object returns to its starting point, displacement is exactly zero even if thousands of meters were traveled.",
                    "diagram_title": "Circular Track Zero Displacement Paradox",
                    "diagram_type": "image",
                    "image_query": "Circular motion zero displacement round trip diagram",
                    "video_query": "zero displacement round trip circular track",
                    "image_url": "/extracted_diagrams/ch4/fig_4_5.webp",
                    "what_to_make": "Ball thrown vertically upwards and returning to thrower's hand showing distance = 2h and displacement = 0.",
                    "timing_and_cue": "Mount zero displacement on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_5.webp | Vertical Round Trip | Upward ascent and downward descent yielding net zero displacement\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (If you walk 5 km around a park and return to your bench, how far did you travel vs what is your net displacement?).
   - Stage 2: Precise scientific definitions, scalar vs vector, SI unit metres (m).
   - Stage 3: Common pitfall (|s| <= d invariant).
   - Stage 4: Chalkboard numerical: athlete on circular track (2200 m distance vs 200 m displacement).
   - Stage 5: Socratic check: "Can the magnitude of displacement ever be greater than the distance traveled? Why or why not?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
    },
    {
        "curriculum_id": CH4_ID,
        "order_index": 2,
        "title": "Rate of Motion: Speed, Velocity & The Geometry of Acceleration",
        "description": "Master uniform vs non-uniform motion, scalar speed vs vector velocity, average velocity formulations, and acceleration as the time rate of change of velocity.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Uniform Motion: Equal distances in equal intervals of time along a straight line",
            "Non-Uniform Motion: Unequal distances in equal intervals of time (accelerated/retarded)",
            "Speed: Rate of distance coverage (v = d/t, SI unit m/s, km/h conversion * 5/18)",
            "Velocity: Speed in a specified direction (v = s/t, vector)",
            "Average Speed vs Average Velocity: Total distance / Total time vs (u + v) / 2 for uniform acceleration",
            "Acceleration: Time rate of change of velocity (a = (v - u) / t, SI unit m/s^2)"
        ],
        "key_concepts": [
            "Uniform Motion: Constant speed in a fixed straight-line direction with zero acceleration.",
            "Speed vs Velocity: Speed is scalar magnitude; velocity includes directional orientation. Velocity changes if speed changes, direction changes, or both change.",
            "Unit Conversion Constant: To convert km/h to m/s, multiply by 5/18; to convert m/s to km/h, multiply by 18/5.",
            "Average Velocity Equation: For uniformly changing velocity, v_avg = (u + v) / 2; generally v_avg = total displacement / total time.",
            "Acceleration Formulation: a = (v - u) / t; positive when velocity increases (acceleration), negative when velocity decreases (retardation/deceleration).",
            "Non-Zero Acceleration at Constant Speed: In circular motion, speed is constant but direction changes continuously, creating acceleration."
        ],
        "success_criteria": "Student can convert units between km/h and m/s, calculate average speed vs average velocity, and compute acceleration/retardation with proper SI units.",
        "chapter_notes": """### 4.4 Uniform vs Non-Uniform Motion
1. **Uniform Motion**: An object covers **equal distances in equal intervals of time**, no matter how small these time intervals are. Velocity is constant; acceleration $a = 0$.
2. **Non-Uniform Motion**: An object covers **unequal distances in equal intervals of time** (e.g., a car accelerating in city traffic).

### 4.5 Speed, Velocity & Acceleration
- **Speed ($v$)**: Distance / Time. Scalar, SI unit: $\\text{m/s}$ or $\\text{m}\\cdot\\text{s}^{-1}$.
- **Velocity ($\\vec{v}$)**: Displacement / Time. Vector, SI unit: $\\text{m/s}$.
  $$\\text{Average Speed} = \\frac{\\text{Total Distance Traversed}}{\\text{Total Time Taken}}$$
  $$\\vec{v}_{\\text{avg}} = \\frac{\\text{Net Displacement}}{\\text{Total Time Taken}} = \\frac{u + v}{2} \\quad \\text{(for uniform acceleration)}$$
- **Unit Conversion Rule**:
  $$1 \\text{ km/h} = \\frac{1000\\text{ m}}{3600\\text{ s}} = \\frac{5}{18}\\text{ m/s}$$

### 4.6 Acceleration ($a$)
The measure of the rate of change of velocity of an object per unit time:
$$a = \\frac{v - u}{t}$$
- Where $u = \\text{initial velocity}$, $v = \\text{final velocity}$, $t = \\text{time interval}$.
- SI unit: **$\\text{m/s}^2$** or **$\\text{m}\\cdot\\text{s}^{-2}$**.
- **Positive Acceleration**: $v > u$ (velocity increases in direction of motion).
- **Negative Acceleration (Retardation / Deceleration)**: $v < u$ (velocity decreases; $a < 0$).""",
        "worked_examples": [
            {
                "problem": "Usha swims in a 90 m long pool. She covers 180 m in one minute by swimming from one end to the other and back along the same straight path. Find the average speed and average velocity of Usha.",
                "given": "Length of pool = 90 m; Total distance = 90 + 90 = 180 m; Time t = 1 min = 60 s; Final position = Initial position (swam back).",
                "formula": "Average Speed = Total Distance / Total Time; Average Velocity = Net Displacement / Total Time.",
                "substitution": "Average Speed = 180 m / 60 s; Average Velocity = 0 m / 60 s.",
                "calculation": "1. Average Speed = 180 / 60 = 3 m/s.\\n2. Since Usha returns to her starting point, her net displacement is exactly 0 m.\\n3. Average Velocity = 0 / 60 = 0 m/s.",
                "finalAnswer": "Average speed = 3 m/s; Average velocity = 0 m/s.",
                "unit": "Metres per second (m/s)",
                "has_diagram": True,
                "diagram_source": "book_extracted",
                "figure_caption": "Fig. 4.7: Odometer reading and swimming pool linear round-trip"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "An object with constant speed can never have acceleration.",
                "correction": "In uniform circular motion, speed is strictly constant, but because the direction of motion continuously changes at every instant, velocity changes and the object experiences continuous inward centripetal acceleration.",
                "why_it_matters": "A classic CBSE board exam conceptual trap."
            }
        ],
        "visual_lesson_plan": {
            "title": "Speed, Velocity & Acceleration Visual Plan",
            "diagram_type": "image",
            "concept_visuals": [
                {
                    "concept_title": "Uniform Motion: Constant speed in a fixed straight-line direction with zero acceleration.",
                    "diagram_title": "Uniform Motion Linear Trajectory",
                    "diagram_type": "image",
                    "image_query": "Uniform motion physics diagram equal distance equal time",
                    "video_query": "uniform motion physics demonstration",
                    "image_url": "/extracted_diagrams/ch4/fig_4_7.webp",
                    "what_to_make": "Vehicle moving along a linear highway covering equal 10 m increments every second.",
                    "timing_and_cue": "Mount uniform motion on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_7.webp | Uniform Motion | Equal distances in equal time intervals with zero acceleration\")"
                },
                {
                    "concept_title": "Speed vs Velocity: Speed is scalar magnitude; velocity includes directional orientation. Velocity changes if speed changes, direction changes, or both change.",
                    "diagram_title": "Speedometer & Odometer Instrument Cluster",
                    "diagram_type": "image",
                    "image_query": "Automobile speedometer odometer instrument cluster",
                    "video_query": "speedometer odometer instantaneous speed",
                    "image_url": "/extracted_diagrams/ch4/fig_4_8.webp",
                    "what_to_make": "Car dashboard showing speedometer measuring instantaneous speed in km/h and odometer measuring total distance.",
                    "timing_and_cue": "Mount speedometer on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_8.webp | Speedometer vs Odometer | Instantaneous scalar speed vs cumulative distance\")"
                },
                {
                    "concept_title": "Unit Conversion Constant: To convert km/h to m/s, multiply by 5/18; to convert m/s to km/h, multiply by 18/5.",
                    "diagram_title": "Speed Unit Conversion Factor 5/18",
                    "diagram_type": "image",
                    "image_query": "Speed conversion km per hour to meters per second diagram",
                    "video_query": "convert km/h to m/s physics",
                    "image_url": "/extracted_diagrams/ch4/fig_4_9.webp",
                    "what_to_make": "Graphic badge showing arithmetic proof: 1000m / 3600s = 5/18.",
                    "timing_and_cue": "Mount unit conversion on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_9.webp | Unit Conversion Rule | Multiply by 5/18 for m/s; multiply by 18/5 for km/h\")"
                },
                {
                    "concept_title": "Average Velocity Equation: For uniformly changing velocity, v_avg = (u + v) / 2; generally v_avg = total displacement / total time.",
                    "diagram_title": "Average Velocity in Swimmer Round Trip",
                    "diagram_type": "image",
                    "image_query": "Average speed vs average velocity round trip swimmer diagram",
                    "video_query": "average speed and average velocity examples",
                    "image_url": "/extracted_diagrams/ch4/fig_4_10.webp",
                    "what_to_make": "Diagram of pool showing 180 m round trip with 3 m/s average speed and 0 m/s average velocity.",
                    "timing_and_cue": "Mount average velocity on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_10.webp | Round Trip Velocity | Demonstrating non-zero average speed with zero average velocity\")"
                },
                {
                    "concept_title": "Acceleration Formulation: a = (v - u) / t; positive when velocity increases (acceleration), negative when velocity decreases (retardation/deceleration).",
                    "diagram_title": "Acceleration Vector & Velocity Change",
                    "diagram_type": "image",
                    "image_query": "Acceleration velocity time rate of change diagram physics",
                    "video_query": "acceleration physics explained",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Acceleration_concept.svg",
                    "what_to_make": "Car accelerating from initial velocity u to final velocity v showing positive acceleration vector.",
                    "timing_and_cue": "Mount acceleration on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/1/1d/Acceleration_concept.svg | Acceleration Dynamics | a = (v - u) / t measured in m/s^2\")"
                },
                {
                    "concept_title": "Non-Zero Acceleration at Constant Speed: In circular motion, speed is constant but direction changes continuously, creating acceleration.",
                    "diagram_title": "Centripetal Directional Acceleration",
                    "diagram_type": "image",
                    "image_query": "Centripetal acceleration constant speed circular motion diagram",
                    "video_query": "acceleration without change in speed circular motion",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/71/Centripetal_force_diagram.svg",
                    "what_to_make": "Circular path showing tangential velocity vectors rotating continuously inward under centripetal acceleration.",
                    "timing_and_cue": "Mount directional acceleration on Step 1: write_chalkboard(action=\"draw_image\", content=\"https://upload.wikimedia.org/wikipedia/commons/7/71/Centripetal_force_diagram.svg | Directional Acceleration | Constant speed with non-zero acceleration due to rotating direction vector\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 VISUAL MOUNTING: Mount verified image from concept_visuals on Step 1 of each concept.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Usha swimming across pool and back).
   - Stage 2: Strict definition of speed, velocity, acceleration and SI units.
   - Stage 3: Common pitfall (Circular motion has constant speed but non-zero acceleration).
   - Stage 4: Chalkboard layout: a = (v - u)/t calculation with unit conversions.
   - Stage 5: Socratic check: "A car turns a sharp curve at a steady 40 km/h. Is the car accelerating? Why?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE numerical question."""
    },
    {
        "curriculum_id": CH4_ID,
        "order_index": 3,
        "title": "The Visual Language of Kinematics: Position-Time (s-t) & Velocity-Time (v-t) Master Graphs",
        "description": "Master graphical representation of motion: interpreting slope of distance-time graphs as speed, slope of velocity-time graphs as acceleration, and the area under velocity-time graphs as displacement.",
        "board": "CBSE",
        "class_level": "Class 9",
        "estimated_minutes": 20,
        "subtopics": [
            "Distance-Time Graphs: Horizontal axis (time), Vertical axis (distance)",
            "Interpreting s-t Slopes: Horizontal flat line = stationary; Straight inclined line = uniform speed; Curved line = accelerating",
            "Mathematical Proof: Slope of s-t graph equals speed (Slope = Delta s / Delta t = v)",
            "Velocity-Time Graphs: Horizontal flat line = constant velocity; Constant upward slope = uniform acceleration; Downward slope = uniform retardation",
            "Mathematical Proof: Slope of v-t graph equals acceleration (Slope = Delta v / Delta t = a)",
            "Area Under v-t Graph: Area under velocity-time curve represents magnitude of displacement (s = v * t)"
        ],
        "key_concepts": [
            "Distance-Time Graph Slope: The gradient (slope = (s2 - s1) / (t2 - t1)) represents the speed of the moving object.",
            "Stationary Object s-t Profile: A horizontal line parallel to the time axis indicates zero speed (object at rest).",
            "Velocity-Time Graph Slope: The gradient (slope = (v2 - v1) / (t2 - t1)) represents the acceleration of the object.",
            "Area Theorem of v-t Graphs: The geometric area bounded by the v-t curve and the time axis equals the exact displacement covered.",
            "Rectangle + Triangle Decomposition: The area under a uniformly accelerating v-t curve decomposes into a lower rectangle (u * t) and an upper triangle (1/2 * a * t^2).",
            "Mafs Interactive Plotting: Interactive real-time coordinate curves allow dynamic visualization of kinematic equations."
        ],
        "success_criteria": "Student can extract speed from s-t slopes, extract acceleration from v-t slopes, and calculate displacement by computing area under v-t curves.",
        "chapter_notes": """### 4.7 Graphical Analysis of Motion
Graphs provide a powerful visual method to describe basic properties of motion.

### 4.8 Distance-Time ($s-t$) Graphs
- **Horizontal line parallel to time axis**: Object is **at rest** (distance does not change as time advances; slope $= 0$).
- **Straight line passing through origin with constant slope**: **Uniform speed**.
  $$\\text{Speed } v = \\text{Slope} = \\frac{s_2 - s_1}{t_2 - t_1} = \\frac{\\Delta s}{\\Delta t}$$
- **Steeper Slope**: Higher speed.
- **Curved line (parabola curving upward)**: **Non-uniform speed** (accelerating motion).

### 4.9 Velocity-Time ($v-t$) Graphs
- **Horizontal line parallel to time axis**: **Constant velocity** (zero acceleration; $a = 0$).
- **Straight line sloping upward**: **Uniform acceleration**.
  $$\\text{Acceleration } a = \\text{Slope} = \\frac{v_2 - v_1}{t_2 - t_1} = \\frac{\\Delta v}{\\Delta t}$$
- **Straight line sloping downward**: **Uniform retardation (deceleration)**.
- **THE AREA THEOREM**: The area enclosed by velocity-time graph and the time axis represents the **displacement** ($s$):
  $$\\text{Displacement } s = \\text{Area under } v-t \\text{ curve}$$
  For uniform velocity: $\\text{Area of Rectangle} = v \\times t$.
  For uniform acceleration: $\\text{Area of Trapezoid} = \\text{Area of Rectangle } (u \\times t) + \\text{Area of Triangle } \\left(\\frac{1}{2} \\times t \\times (v - u)\\right)$.""",
        "worked_examples": [
            {
                "problem": "A car accelerates uniformly from 18 km/h to 36 km/h in 5 s. Using a velocity-time graph, calculate (a) the acceleration, and (b) the distance covered by the car in that time.",
                "given": "Initial velocity u = 18 km/h = 18 * (5/18) = 5 m/s; Final velocity v = 36 km/h = 36 * (5/18) = 10 m/s; Time t = 5 s.",
                "formula": "(a) a = (v - u) / t; (b) Distance s = Area under v-t graph = Area of rectangle (u*t) + Area of triangle (1/2 * (v-u) * t).",
                "substitution": "a = (10 - 5) / 5; Area = (5 * 5) + (1/2 * (10 - 5) * 5).",
                "calculation": "1. Acceleration a = 5 / 5 = 1 m/s^2.\\n2. Area of rectangle = 5 * 5 = 25 m.\\n3. Area of triangle = 0.5 * 5 * 5 = 12.5 m.\\n4. Total distance s = 25 + 12.5 = 37.5 m.",
                "finalAnswer": "(a) Acceleration = 1 m/s^2; (b) Distance covered = 37.5 m.",
                "unit": "Acceleration (m/s^2), Distance (m)",
                "has_diagram": True,
                "diagram_source": "mafs_graph",
                "figure_caption": "Fig. 4.17: Velocity-time graph for a car under uniform acceleration showing rectangular and triangular area components"
            }
        ],
        "common_misconceptions": [
            {
                "misconception": "The slope of a velocity-time graph gives the distance covered.",
                "correction": "The SLOPE of a v-t graph gives ACCELERATION; it is the AREA under the v-t graph that gives DISTANCE.",
                "why_it_matters": "The number one source of lost marks in Class 9 kinematics."
            }
        ],
        "visual_lesson_plan": {
            "title": "Visual Language of Kinematics Graphs Visual Plan",
            "diagram_type": "graph",
            "concept_visuals": [
                {
                    "concept_title": "Distance-Time Graph Slope: The gradient (slope = (s2 - s1) / (t2 - t1)) represents the speed of the moving object.",
                    "diagram_title": "Distance-Time Graph for Uniform Speed",
                    "diagram_type": "graph",
                    "image_query": "Distance time graph uniform speed straight line slope diagram",
                    "video_query": "distance time graph physics tutorial",
                    "image_url": "/extracted_diagrams/ch4/fig_4_11.webp",
                    "what_to_make": "Mafs coordinate plot of linear distance-time curve s = 5t showing slope calculation triangle.",
                    "timing_and_cue": "Mount s-t plot on Step 1: plot_mathematical_graph(title=\"Distance-Time Graph: Uniform Speed\", equation=\"5*x\", xMin=0, xMax=10, yMin=0, yMax=50, xLabel=\"Time t (s)\", yLabel=\"Distance s (m)\")"
                },
                {
                    "concept_title": "Stationary Object s-t Profile: A horizontal line parallel to the time axis indicates zero speed (object at rest).",
                    "diagram_title": "Distance-Time Graph for Stationary Body",
                    "diagram_type": "graph",
                    "image_query": "Distance time graph stationary object horizontal line diagram",
                    "video_query": "stationary object distance time graph",
                    "image_url": "/extracted_diagrams/ch4/fig_4_13.webp",
                    "what_to_make": "Mafs plot of horizontal line s = 20 demonstrating zero slope and zero speed.",
                    "timing_and_cue": "Mount stationary plot on Step 1: plot_mathematical_graph(title=\"Distance-Time Graph: Object at Rest\", equation=\"20\", xMin=0, xMax=10, yMin=0, yMax=40, xLabel=\"Time t (s)\", yLabel=\"Distance s (m)\")"
                },
                {
                    "concept_title": "Velocity-Time Graph Slope: The gradient (slope = (v2 - v1) / (t2 - t1)) represents the acceleration of the object.",
                    "diagram_title": "Velocity-Time Graph for Uniform Acceleration",
                    "diagram_type": "graph",
                    "image_query": "Velocity time graph uniform acceleration straight line slope diagram",
                    "video_query": "velocity time graph acceleration slope",
                    "image_url": "/extracted_diagrams/ch4/fig_4_15.webp",
                    "what_to_make": "Mafs plot of v = 2 + 1.5t showing steady linear acceleration with positive slope.",
                    "timing_and_cue": "Mount v-t plot on Step 1: plot_mathematical_graph(title=\"Velocity-Time Graph: Uniform Acceleration\", equation=\"2 + 1.5*x\", xMin=0, xMax=10, yMin=0, yMax=20, xLabel=\"Time t (s)\", yLabel=\"Velocity v (m/s)\")"
                },
                {
                    "concept_title": "Area Theorem of v-t Graphs: The geometric area bounded by the v-t curve and the time axis equals the exact displacement covered.",
                    "diagram_title": "Displacement as Area Under v-t Curve",
                    "diagram_type": "image",
                    "image_query": "Area under velocity time graph displacement rectangle diagram",
                    "video_query": "area under velocity time graph displacement",
                    "image_url": "/extracted_diagrams/ch4/fig_4_17.webp",
                    "what_to_make": "Textbook diagram showing shaded rectangle representing displacement s = v * t for uniform motion.",
                    "timing_and_cue": "Mount area theorem on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_17.webp | Area Theorem | Displacement equals the geometric area bounded under v-t graph\")"
                },
                {
                    "concept_title": "Rectangle + Triangle Decomposition: The area under a uniformly accelerating v-t curve decomposes into a lower rectangle (u * t) and an upper triangle (1/2 * a * t^2).",
                    "diagram_title": "Trapezoid Decomposition Area Under v-t Graph",
                    "diagram_type": "image",
                    "image_query": "Velocity time graph trapezoid area rectangle triangle derivation",
                    "video_query": "deriving equations of motion graphically velocity time graph",
                    "image_url": "/extracted_diagrams/ch4/fig_4_18.webp",
                    "what_to_make": "Geometric trapezoid partitioned into base rectangle OACD (u*t) and top triangle ABD (1/2 * at^2).",
                    "timing_and_cue": "Mount trapezoid decomposition on Step 1: write_chalkboard(action=\"draw_image\", content=\"/extracted_diagrams/ch4/fig_4_18.webp | Trapezoid Decomposition | Area = Rectangle (u*t) + Triangle (1/2*a*t^2)\")"
                },
                {
                    "concept_title": "Mafs Interactive Plotting: Interactive real-time coordinate curves allow dynamic visualization of kinematic equations.",
                    "diagram_title": "Dynamic Multi-Phase Kinematic Curve",
                    "diagram_type": "graph",
                    "image_query": "Kinematics position velocity acceleration graphs physics",
                    "video_query": "interactive graphing kinematics mafs",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Kinematic_graph_example.svg",
                    "what_to_make": "Interactive coordinate canvas plotting multi-phase acceleration and deceleration profiles.",
                    "timing_and_cue": "Mount dynamic graph on Step 1: plot_mathematical_graph(title=\"Multi-Phase Kinematics\", equation=\"4*x - 0.4*x^2\", xMin=0, xMax=10, yMin=0, yMax=15, xLabel=\"Time t (s)\", yLabel=\"Velocity v (m/s)\")"
                }
            ]
        },
        "ai_system_prompt_context": """MANDATORY LIVE TUTOR INVARIANTS:
1. STEP 1 GRAPH / VISUAL MOUNTING: On Step 1 of graphing concepts, immediately call plot_mathematical_graph(...) with the specified equation, domain, range, and axes labels.
2. 6-STAGE SOCRATIC CADENCE:
   - Stage 1: Intuition hook (Why a flat line on an s-t graph means you are standing still, but a flat line on a v-t graph means you are cruising at 100 km/h).
   - Stage 2: Mathematical definition of slope (Delta y / Delta x) and area.
   - Stage 3: Common pitfall (Slope gives acceleration; Area gives distance).
   - Stage 4: Chalkboard derivation of distance from area of rectangle + triangle.
   - Stage 5: Socratic check: "If the slope of a v-t graph is negative, what does that tell you about the car's motion?" HARD STOP: Wait for student response!
   - Stage 6: Authentic CBSE board numerical."""
    }
]

print(f"Synthesized Chapter 4: {len(ch4_modules)} modules complete.")

output_path_ch4 = "scripts/science_modules_ch4.json"
with open(output_path_ch4, "w", encoding="utf-8") as f:
    json.dump(ch4_modules, f, indent=2, ensure_ascii=False)
print(f"Saved Chapter 4 modules to {output_path_ch4}")
