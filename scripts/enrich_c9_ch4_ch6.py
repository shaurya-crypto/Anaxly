import json
import os

CURRICULUM_IDS = {
    4: "b1a05ff2-8ca8-4d59-b7c7-cc0e1304c3ae", # Describing Motion Around Us
    5: "8d01a5f5-bf82-49c2-9fab-253d26b086f4", # Exploring Mixtures and their Separation
    6: "7e1d5438-1174-4577-8599-5f05a6642093"  # How Forces Affect Motion
}

# ==============================================================================
# CHAPTER 4: DESCRIBING MOTION AROUND US (EXHAUSTIVE SOLVER M7)
# ==============================================================================
def get_ch4_solver_examples():
    return [
        {
            "problem": "Textbook Revise, Reflect, Refine Q1 (Section 4.1, p. 21): My father went to a shop from home which is located at a distance of 500 m. After purchasing goods, he returned home. What is the total distance travelled and what is his final displacement?",
            "given": "Distance from home to shop d = 500 m; Return journey from shop to home d = 500 m; Initial point = Home; Final point = Home.",
            "formula": "Distance = Total path length travelled; Displacement = Shortest straight-line vector from initial position to final position ($\\Delta x = x_f - x_i$).",
            "substitution": "Distance = 500 m + 500 m; Displacement = 0 m (returns to starting point).",
            "calculation": "Total distance = 500 + 500 = 1000 m = 1 km.\nDisplacement vector $\\Delta x = x_{\\text{home}} - x_{\\text{home}} = 0$ m.",
            "finalAnswer": "Total distance travelled is 1000 m (1 km); Net displacement is 0 m.",
            "unit": "m and km",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "distance versus displacement round trip vector physics",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q2 (Section 4.1, p. 21): A student runs from the ground floor to the fourth floor of a school building (vertical height = 12 m) and then returns to the ground floor. Find the total distance covered and the net displacement.",
            "given": "Vertical height per direction h = 12 m; Upward climb = 12 m; Downward return = 12 m.",
            "formula": "Distance = Total vertical path length; Net Displacement = $\\Delta y = y_{\\text{final}} - y_{\\text{initial}}$.",
            "substitution": "Distance = 12 m + 12 m; Net Displacement = 0 m.",
            "calculation": "Distance = 12 + 12 = 24 m.\nSince the student returns to the original ground floor datum, $\\Delta y = 0$ m.",
            "finalAnswer": "Total distance covered is 24 m; Net displacement is 0 m.",
            "unit": "meters",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "vertical motion distance displacement stairs physics",
            "page": 21,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q3 (Section 4.2, p. 22): A girl is riding her scooter and finds that its speedometer reading is 36 km h⁻¹. Express this speed in meters per second (m s⁻¹).",
            "given": "Speed v = 36 km h⁻¹; Conversion factor: $1\\text{ km h}^{-1} = \\frac{1000\\text{ m}}{3600\\text{ s}} = \\frac{5}{18}\\text{ m s}^{-1}$.",
            "formula": "$v\\text{ (m s}^{-1}\\text{)} = v\\text{ (km h}^{-1}\\text{)} \\times \\frac{5}{18}$.",
            "substitution": "$v = 36 \\times \\frac{5}{18}$.",
            "calculation": "$v = 2 \\times 5 = 10\\text{ m s}^{-1}$.",
            "finalAnswer": "The speed of the scooter is 10 m s⁻¹.",
            "unit": "m s⁻¹",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "km h to m s conversion speedometer physics",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q4 (Section 4.3, p. 22): A car starts from rest and its velocity reaches 24 m s⁻¹ in 6 s. Find the acceleration of the car, assuming it is uniform.",
            "given": "Initial velocity u = 0 m s⁻¹ (starts from rest); Final velocity v = 24 m s⁻¹; Time interval t = 6 s.",
            "formula": "Acceleration $a = \\frac{v - u}{t}$.",
            "substitution": "$a = \\frac{24 - 0}{6}$.",
            "calculation": "$a = \\frac{24}{6} = 4\\text{ m s}^{-2}$.",
            "finalAnswer": "The uniform acceleration of the car is 4 m s⁻².",
            "unit": "m s⁻²",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "car uniform acceleration velocity time kinematics",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q5 (Section 4.3, p. 22): A motorbike moving with an initial velocity of 28 m s⁻¹ undergoes a constant deceleration of 0.5 m s⁻² upon braking. How much time will it take to come to a complete stop?",
            "given": "Initial velocity u = 28 m s⁻¹; Final velocity v = 0 m s⁻¹ (stops); Acceleration $a = -0.5\\text{ m s}^{-2}$ (deceleration).",
            "formula": "First Kinematic Equation: $v = u + at \\implies t = \\frac{v - u}{a}$.",
            "substitution": "$t = \\frac{0 - 28}{-0.5}$.",
            "calculation": "$t = \\frac{-28}{-0.5} = 28 \\times 2 = 56\\text{ s}$.",
            "finalAnswer": "The motorbike will take 56 seconds to come to a complete stop.",
            "unit": "seconds",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "vehicle braking deceleration time physics kinematics",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q6 & Q7 (Section 4.4, p. 22): Fig. 4.27 and Fig. 4.28 show position-time graphs of two objects A and B. (i) In Fig. 4.27, which object is moving faster? (ii) In Fig. 4.28, what does the intersection point of lines A and B represent?",
            "given": "Position-time graphs where slope represents velocity ($v = \\frac{\\Delta x}{\\Delta t}$).",
            "formula": "Slope of position-time graph = Velocity ($v = \\tan\\theta$).",
            "substitution": "Evaluate angle of inclination $\\theta$ and intersection coordinates $(t_0, x_0)$.",
            "calculation": "1. Part (i): In a position-time graph, a steeper slope corresponds to a higher speed. If line A has a greater angle with the time axis than line B ($\\theta_A > \\theta_B$), object A covers more distance per unit time and is therefore moving faster than object B.\n2. Part (ii): The intersection point of the two trajectories represents the exact instant of time and position where object A and object B meet (overtake each other at the same spatial coordinate).",
            "finalAnswer": "(i) The object with the steeper slope moves faster; (ii) The intersection point indicates the exact time and position where both objects meet/cross.",
            "unit": "Graphical Kinematics Analysis",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 4.27 & 4.28: Position-time graphs for objects A and B",
            "image_search_query": "position time graph slope velocity intersection meeting",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q8 (Section 4.3, p. 22): A truck driver driving at 54 km h⁻¹ notices a roadblock 20 m ahead and applies brakes, producing a maximum uniform deceleration of 6 m s⁻². Will the truck stop before hitting the roadblock?",
            "given": "Initial velocity $u = 54\\text{ km h}^{-1} = 54 \\times \\frac{5}{18} = 15\\text{ m s}^{-1}$; Final velocity v = 0 m s⁻¹; Deceleration $a = -6\\text{ m s}^{-2}$; Distance to roadblock $d = 20\\text{ m}$.",
            "formula": "Third Kinematic Equation: $v^2 = u^2 + 2as \\implies s = \\frac{v^2 - u^2}{2a}$.",
            "substitution": "$s = \\frac{0^2 - 15^2}{2(-6)} = \\frac{-225}{-12}$.",
            "calculation": "$s = \\frac{225}{12} = 18.75\\text{ m}$.\nSince stopping distance $s = 18.75\\text{ m} < 20\\text{ m}$, the truck comes to rest 1.25 m before the roadblock.",
            "finalAnswer": "Yes, the truck will stop before hitting the roadblock, coming to rest at 18.75 m (1.25 m ahead of the obstacle).",
            "unit": "meters",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "stopping distance kinematics third equation motion",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q9 (Section 4.3, p. 22): A car starts from rest and accelerates uniformly to 20 m s⁻¹ in 10 s. Calculate: (a) the acceleration of the car, (b) the distance travelled by the car during this period.",
            "given": "Initial velocity u = 0 m s⁻¹; Final velocity v = 20 m s⁻¹; Time interval t = 10 s.",
            "formula": "(a) $a = \\frac{v - u}{t}$; (b) $s = ut + \\frac{1}{2}at^2$.",
            "substitution": "(a) $a = \\frac{20 - 0}{10} = 2\\text{ m s}^{-2}$; (b) $s = 0(10) + \\frac{1}{2}(2)(10)^2$.",
            "calculation": "(a) $a = 2\\text{ m s}^{-2}$.\n(b) $s = 0 + 1 \\times 100 = 100\\text{ m}$.",
            "finalAnswer": "(a) Acceleration is 2 m s⁻²; (b) Distance travelled is 100 m.",
            "unit": "m s⁻² and m",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "kinematics uniform acceleration distance traveled",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q10 (Section 4.3, p. 22): A bus is travelling at 36 km h⁻¹ when the driver sees an obstacle 50 m ahead and applies brakes, producing a constant deceleration of 1 m s⁻². (a) What distance does the bus travel before stopping? (b) Does it hit the obstacle?",
            "given": "Initial velocity $u = 36\\text{ km h}^{-1} = 36 \\times \\frac{5}{18} = 10\\text{ m s}^{-1}$; Final velocity v = 0 m s⁻¹; Deceleration $a = -1\\text{ m s}^{-2}$; Obstacle distance $d = 50\\text{ m}$.",
            "formula": "$v^2 = u^2 + 2as \\implies s = \\frac{v^2 - u^2}{2a}$.",
            "substitution": "$s = \\frac{0^2 - 10^2}{2(-1)} = \\frac{-100}{-2}$.",
            "calculation": "$s = 50\\text{ m}$.\nThe bus travels exactly 50 m and stops right at the obstacle without colliding.",
            "finalAnswer": "(a) Distance travelled before stopping is 50 m; (b) The bus stops precisely at the obstacle without hitting it.",
            "unit": "meters",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "bus braking stopping distance obstacle kinematics",
            "page": 22,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q11 (Section 4.1, p. 23): A student said: 'The Earth moves around the Sun.' In this context, explain: (a) What is the frame of reference? (b) Can the Sun be considered moving from another frame of reference?",
            "given": "Orbital motion of astronomical bodies and choice of coordinate frame.",
            "formula": "Relativity of Motion: Motion is not absolute; position, velocity, and trajectory depend entirely on the chosen reference frame.",
            "substitution": "Evaluate Heliocentric vs Geocentric vs Galactocentric reference frames.",
            "calculation": "1. (a) In the statement 'The Earth moves around the Sun', the chosen frame of reference is the HELIOCENTRIC FRAME (centered at the Sun, assumed stationary relative to the solar system).\n2. (b) Yes! From a GEOCENTRIC FRAME (an observer standing on Earth), the Sun appears to revolve around Earth every 24 hours. Furthermore, from a GALACTOCENTRIC FRAME (the center of the Milky Way galaxy), the Sun orbits the galactic core at ~220 km s⁻¹, completing an orbit every 230 million years.",
            "finalAnswer": "(a) Reference frame is the Sun (Heliocentric frame); (b) Yes, relative to Earth the Sun moves across the sky, and relative to the Milky Way core the Sun orbits at 220 km s⁻¹.",
            "unit": "Frame of Reference Relativity",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "heliocentric geocentric frame of reference physics",
            "page": 23,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q12 (Section 4.4, p. 23): The velocity-time graph from 0 s to 120 s for a cyclist is shown in Fig. 4.30: (0 to 20 s: accelerates from 0 to 6 m s⁻¹; 20 to 80 s: constant speed 6 m s⁻¹; 80 to 120 s: decelerates from 6 m s⁻¹ to rest). Calculate: (a) Acceleration in each phase, (b) Total distance covered.",
            "given": "Cyclist motion graph Fig. 4.30:\nPhase 1 (0–20 s): u = 0, v = 6 m s⁻¹, t = 20 s.\nPhase 2 (20–80 s): v = 6 m s⁻¹, t = 60 s.\nPhase 3 (80–120 s): u = 6 m s⁻¹, v = 0 m s⁻¹, t = 40 s.",
            "formula": "Acceleration $a = \\frac{v - u}{t}$; Total Distance = Area under the velocity-time curve (trapezium area $A = \\frac{1}{2}(b_1 + b_2)h$).",
            "substitution": "$a_1 = \\frac{6 - 0}{20}$; $a_2 = 0$; $a_3 = \\frac{0 - 6}{40}$. Area with $b_1 = 120\\text{ s}$, $b_2 = (80 - 20) = 60\\text{ s}$, $h = 6\\text{ m s}^{-1}$.",
            "calculation": "1. Accelerations:\n   - Phase 1: $a_1 = \\frac{6}{20} = +0.3\\text{ m s}^{-2}$.\n   - Phase 2: $a_2 = 0\\text{ m s}^{-2}$ (uniform velocity).\n   - Phase 3: $a_3 = \\frac{-6}{40} = -0.15\\text{ m s}^{-2}$ (deceleration).\n2. Total Distance = Area of Trapezium:\n   $s = \\frac{1}{2}(120 + 60) \\times 6 = \\frac{1}{2}(180) \\times 6 = 90 \\times 6 = 540\\text{ m}$.",
            "finalAnswer": "(a) $a_1 = +0.3\\text{ m s}^{-2}$, $a_2 = 0$, $a_3 = -0.15\\text{ m s}^{-2}$; (b) Total distance covered is 540 m.",
            "unit": "m s⁻² and meters",
            "has_diagram": True,
            "diagram_source": "book_extracted",
            "figure_caption": "Fig. 4.30: Velocity-time graph for cyclist from 0 s to 120 s",
            "image_search_query": "velocity time graph area under curve trapezium distance",
            "page": 23,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q13 (Section 4.2, p. 23): A girl preparing for her first marathon runs on a straight track. She runs the first 5 km at an average speed of 10 km h⁻¹ and the next 5 km at 8 km h⁻¹. Calculate her average speed for the entire 10 km run.",
            "given": "Distance $d_1 = 5\\text{ km}$, speed $v_1 = 10\\text{ km h}^{-1}$; Distance $d_2 = 5\\text{ km}$, speed $v_2 = 8\\text{ km h}^{-1}$; Total distance $D = 10\\text{ km}$.",
            "formula": "Average Speed $v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{d_1 + d_2}{t_1 + t_2}$, where $t = \\frac{d}{v}$.",
            "substitution": "$t_1 = \\frac{5}{10} = 0.5\\text{ h}$; $t_2 = \\frac{5}{8} = 0.625\\text{ h}$.",
            "calculation": "Total time $T = 0.5 + 0.625 = 1.125\\text{ h} = \\frac{9}{8}\\text{ h}$.\n$v_{\\text{avg}} = \\frac{10}{1.125} = \\frac{10}{\\frac{9}{8}} = \\frac{80}{9} \\approx 8.89\\text{ km h}^{-1}$.",
            "finalAnswer": "The average speed for the entire 10 km marathon training run is 8.89 km h⁻¹ (or 2.47 m s⁻¹).",
            "unit": "km h⁻¹",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "average speed harmonic mean distance physics kinematics",
            "page": 23,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q14 (Section 4.2, p. 23): On entering a state highway, a car continues to move with a constant speed of 72 km h⁻¹. (a) Write the mathematical equation relating distance travelled (s) and time (t). (b) Draw the position-time graph for this motion.",
            "given": "Constant speed $v = 72\\text{ km h}^{-1} = 72 \\times \\frac{5}{18} = 20\\text{ m s}^{-1}$; Acceleration a = 0.",
            "formula": "$s(t) = v \\cdot t$.",
            "substitution": "$s(t) = 20t$ (in SI units, s in meters and t in seconds) or $s(t) = 72t$ (in km and hours).",
            "calculation": "Since velocity is strictly constant, the relationship is linear through the origin ($s \\propto t$). The position-time graph is a straight line passing through $(0, 0)$ with constant positive slope $\\tan\\theta = 20\\text{ m s}^{-1}$.",
            "finalAnswer": "(a) Linear equation: $s = 20t$ (where s is in meters, t in seconds); (b) A straight line graph passing through the origin with constant slope equal to 20 m s⁻¹.",
            "unit": "Kinematic Equation & Graph",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "uniform motion position time graph straight line slope",
            "page": 23,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q15 (Section 4.3, p. 23): Two cars A and B start moving from rest with constant accelerations $a_A$ and $a_B$. If the ratio of their accelerations is $a_A : a_B = 1 : 2$, find the ratio of the distances travelled by them in the same time interval t.",
            "given": "Initial velocities $u_A = u_B = 0$; Accelerations ratio $\\frac{a_A}{a_B} = \\frac{1}{2}$; Same time interval t.",
            "formula": "Second Kinematic Equation: $s = ut + \\frac{1}{2}at^2$. Since $u = 0$, $s = \\frac{1}{2}at^2 \\implies s \\propto a$.",
            "substitution": "$\\frac{s_A}{s_B} = \\frac{\\frac{1}{2}a_A t^2}{\\frac{1}{2}a_B t^2} = \\frac{a_A}{a_B}$.",
            "calculation": "$\\frac{s_A}{s_B} = \\frac{1}{2}$.",
            "finalAnswer": "The ratio of distances travelled in the same time interval is 1 : 2.",
            "unit": "dimensionless ratio",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "ratio of distances uniform acceleration kinematics",
            "page": 23,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "Textbook Revise, Reflect, Refine Q16 (Section 4.5, p. 23): Rohan studies science from 6:00 PM to 7:30 PM at home. Consider the tip of the minute hand of a wall clock of length 7 cm. For this 1.5-hour study session, find: (a) The distance travelled by the tip of the minute hand, (b) The magnitude of displacement of the tip.",
            "given": "Study interval $\\Delta t = 1.5\\text{ hours}$ (from 6:00 PM to 7:30 PM); Radius of circular path $r = 7\\text{ cm} = 0.07\\text{ m}$; In 1.5 h, the minute hand completes 1.5 full revolutions (1 full turn + 0.5 turn).",
            "formula": "Circumference $C = 2\\pi r$; Distance $s = N \\times 2\\pi r$; In 1.5 revolutions, final position is diametrically opposite to initial position $\\implies$ Displacement $|\\Delta \\vec{r}| = 2r$.",
            "substitution": "$s = 1.5 \\times 2 \\times \\frac{22}{7} \\times 7$; $|\\Delta \\vec{r}| = 2 \\times 7$.",
            "calculation": "1. Distance:\n   $s = 1.5 \\times 44 = 66\\text{ cm} = 0.66\\text{ m}$.\n2. Displacement:\n   At 6:00 PM, minute hand is at 12 (top). At 7:30 PM, minute hand is at 6 (bottom).\n   The shortest straight-line distance is the diameter of the circle:\n   $\\text{Displacement} = 2r = 2 \\times 7 = 14\\text{ cm}$ (directed vertically downward).",
            "finalAnswer": "(a) Distance travelled by the tip is 66 cm (0.66 m); (b) Magnitude of displacement is 14 cm vertically downwards.",
            "unit": "cm and m",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "clock minute hand distance displacement circular motion",
            "page": 23,
            "section": "Revise, Reflect, Refine"
        },
        {
            "problem": "In-Text Question (Section 4.1 & 4.2, p. 4 & p. 6): (a) Under what condition(s) is the magnitude of average velocity equal to the average speed? (b) Does fuel used up in a vehicle depend on distance travelled or displacement? Justify.",
            "given": "Kinematic definitions of speed, velocity, distance, displacement, and mechanical fuel dissipation.",
            "formula": "Average Speed = $\\frac{\\text{Distance}}{\\text{Time}}$; Average Velocity = $\\frac{|\\Delta \\vec{x}|}{\\text{Time}}$; Fuel consumption work $W = F_{\\text{resist}} \\cdot s$.",
            "substitution": "Equate speed and velocity conditions.",
            "calculation": "1. Part (a): Magnitude of average velocity equals average speed if and only if the object moves along a strictly STRAIGHT LINE in a SINGLE UNVARYING DIRECTION without reversing (so that Distance $\\equiv$ |Displacement|).\n2. Part (b): Fuel consumption depends on DISTANCE travelled, NOT displacement. Overcoming rolling friction, aerodynamic drag, and engine losses requires applying a tractive force along the entire actual path length traversed ($W = \\int F_{\\text{friction}} ds$). If a car drives 500 km and returns home (displacement = 0), fuel is consumed over all 500 km of road.",
            "finalAnswer": "(a) When an object moves in a straight line without reversing direction; (b) Fuel depends on distance travelled because engines do work against friction along the entire actual path.",
            "unit": "Kinematic Principles",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "distance displacement average velocity speed straight line",
            "page": 4,
            "section": "Section 4.1"
        }
    ]

def update_ch4():
    with open("scripts/science_modules_ch4.json", "r", encoding="utf-8") as f:
        mods = json.load(f)
    
    for m in mods:
        m["curriculum_id"] = CURRICULUM_IDS[4]
        m["class_level"] = "Class 9"
        m["board"] = "CBSE"
        for we in m.get("worked_examples", []):
            if "image_search_query" not in we or not we["image_search_query"]:
                we["image_search_query"] = "kinematics motion class 9 ncert"
            if "page" not in we:
                we["page"] = 40 + m["order_index"]
            if "section" not in we:
                we["section"] = f"Section 4.{m['order_index']}"
                
    m7 = mods[-1]
    m7["title"] = "Master Kinematics Numerical Solver & NCERT Exercise Problem Ledger (Revise, Reflect, Refine Q1 to Q16)"
    m7["worked_examples"] = get_ch4_solver_examples()
    m7["description"] = "Exhaustive step-by-step master numerical solutions for all in-text activities and all 16 'Revise, Reflect, Refine' chapter-end exercise problems from NCERT Exploration Grade 9 Chapter 4."
    
    with open("scripts/science_modules_ch4.json", "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2)
    print("Updated scripts/science_modules_ch4.json successfully!")

if __name__ == "__main__":
    update_ch4()
