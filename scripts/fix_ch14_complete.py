import json

with open('scripts/maths_pt2_modules/ch14_surface_areas_volumes.json', 'r', encoding='utf-8') as f:
    modules = json.load(f)

# Module 1 (Cuboids and Cubes):
# Fix existing WE 1, 2, 3 FORMULA USED
for we in modules[0]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nCuboid Metrics: Volume V = lwh, Total Surface Area S = 2(lw + wh + hl).\nCube Metrics: Volume V = a³, Surface Area S = 6a².\n\nSTEP-BY-STEP")
        we['solution'] = sol

# Add in-text Exercise Set (pp. 3-4, book pp. 125-126) and End-of-Chapter Exercise 12(i)
we_m1_extra = {
    "problem": "Chapter 14, Section 14.1 Exercise Set & End-of-Chapter Exercise 12(i) (Ganita Manjari Part 2, pp. 125–126 & 145):\n(i) Section 14.1, Q5: A solid cube of side 4 cm is cut into cubes of side 1 cm. What is the ratio of the surface area of the original cube to the total surface area of all the cut-out cubes?\n(ii) Section 14.1, Q6: The surface areas of three adjacent faces of a cuboid meeting at a vertex are 6 cm², 15 cm², and 10 cm² respectively. Find the volume of the cuboid.\n(iii) End-of-Chapter Exercise 12(i): What is the change in volume when the length l of a cuboid of dimensions l, w, h is increased by 1 unit?",
    "solution": """GIVEN:
(i) Original cube side S = 4 cm; sliced into smaller unit cubes of side s = 1 cm.
(ii) Face areas meeting at a corner: A₁ = lw = 6 cm², A₂ = wh = 15 cm², A₃ = hl = 10 cm².
(iii) Cuboid dimensions: length l, width w, height h; new length l' = l + 1.

TO FIND / TO PROVE:
(i) Ratio of surface area of original cube to sum of surface areas of all 1 cm cubes.
(ii) Volume V of the cuboid.
(iii) Algebraic change in volume ΔV.

FORMULA USED:
1. Cube Surface Area: S = 6a²; Volume V = a³.
2. Cuboid Volume from Face Areas:
   A₁ · A₂ · A₃ = (lw)(wh)(hl) = (lwh)² = V²  =>  V = √(A₁ · A₂ · A₃).
3. Change in Volume: ΔV = V_new - V_old = (l + 1)wh - lwh = wh.

STEP-BY-STEP CALCULATION:
Part (i) Cube Slicing Ratio:
1. Volume of original cube = S³ = 4³ = 64 cm³.
2. Volume of each small cube = s³ = 1³ = 1 cm³.
   Number of small cubes N = 64 / 1 = 64 cubes.
3. Total Surface Area of original cube:
   TSA_orig = 6S² = 6 × 4² = 6 × 16 = 96 cm².
4. Total Surface Area of all 64 small cubes:
   TSA_small = 6s² = 6 × 1² = 6 cm².
   TSA_total = 64 × 6 = 384 cm².
5. Ratio of TSA_orig to TSA_total:
   Ratio = 96 / 384 = 1 / 4 = 1 : 4.
   (The total surface area quadruples while the volume remains unchanged!)

Part (ii) Volume from Corner Face Areas:
1. Given: lw = 6, wh = 15, hl = 10.
2. Multiply all three equations:
   (lw) × (wh) × (hl) = 6 × 15 × 10
   l²w²h² = 900
   (lwh)² = 900.
3. Taking the positive square root:
   Volume V = lwh = √900 = 30 cm³.

Part (iii) Volume Increase with Unit Length:
V_new = (l + 1) × w × h = lwh + wh.
V_old = lwh.
Change in volume ΔV = V_new - V_old = wh cubic units (Option c).

[ROUGH_WORK]
4³ = 64 cubes.
Original TSA = 6(16) = 96 cm².
All small TSA = 64 × 6(1) = 384 cm².
96 / 384 = 1/4 -> 1 : 4.
6 × 15 × 10 = 900 -> √900 = 30 cm³.
(l+1)wh - lwh = wh.

Boxed Answer:
[ (i) Ratio of Surface Areas = 1 : 4, (ii) Volume of Cuboid = 30 cm³, (iii) Volume increases by wh cubic units (Option c) ]"""
}
modules[0]['worked_examples'].append(we_m1_extra)

# Module 2 (Right Circular Cylinders):
# Fix existing WE 1, 2 FORMULA USED
for we in modules[1]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nCylinder Curved Surface Area: CSA = 2πrh\nCylinder Total Surface Area: TSA = 2πr(r + h)\nCylinder Volume: V = πr²h\n\nSTEP-BY-STEP")
        we['solution'] = sol

# Add in-text Exercise Set (pp. 7-8, book pp. 129-130)
we_m2_extra = {
    "problem": "Chapter 14, Section 14.2 Exercise Set (Ganita Manjari Part 2, Section 14.2, pp. 129–130):\n(i) Question 1: A metal pipe is 77 cm long. The inner diameter of a cross section is 4 cm, the outer diameter being 4.4 cm. Find its: (a) inner curved surface area, (b) outer curved surface area, (c) total surface area (use π = 22/7).\n(ii) Question 2: A cylindrical container of radius 14 cm and height 20 cm is open at the top. Find the area of sheet metal required to make it and its liquid capacity in litres.",
    "solution": """GIVEN:
(i) Hollow metal pipe: length h = 77 cm; inner radius r₁ = 4/2 = 2 cm; outer radius r₂ = 4.4/2 = 2.2 cm.
(ii) Open cylindrical container: radius r = 14 cm, height h = 20 cm.

TO FIND / TO PROVE:
(i) Inner CSA, Outer CSA, and Total Surface Area (including two circular ring bases).
(ii) Sheet metal area and capacity in litres (1000 cm³ = 1 L).

FORMULA USED:
1. Inner CSA = 2πr₁h
2. Outer CSA = 2πr₂h
3. Area of 2 Ring Bases = 2 × [π(r₂² - r₁²)]
4. Pipe TSA = Inner CSA + Outer CSA + 2 × Base Rings
5. Open Cylinder Sheet Area = 2πrh + πr²
6. Cylinder Volume = πr²h

STEP-BY-STEP CALCULATION:
Part (i) Hollow Metal Pipe:
(a) Inner CSA = 2 × (22/7) × 2 × 77 = 2 × 22 × 2 × 11 = 968 cm².
(b) Outer CSA = 2 × (22/7) × 2.2 × 77 = 2 × 22 × 2.2 × 11 = 1064.8 cm².
(c) Area of two circular ring ends:
    r₂² - r₁² = (2.2)² - (2)² = 4.84 - 4 = 0.84 cm².
    Area = 2 × (22/7) × 0.84 = 2 × 22 × 0.12 = 5.28 cm².
    Total Surface Area = 968 + 1064.8 + 5.28 = 2038.08 cm².

Part (ii) Open Cylindrical Container:
1. Sheet metal area = CSA + Base Area = 2πrh + πr² = πr(2h + r)
   Area = (22/7) × 14 × [2(20) + 14] = 22 × 2 × [40 + 14] = 44 × 54 = 2376 cm².
2. Capacity (Volume) = πr²h = (22/7) × 14 × 14 × 20 = 22 × 2 × 14 × 20 = 44 × 280 = 12,320 cm³.
   In litres = 12,320 / 1000 = 12.32 litres.

[ROUGH_WORK]
Inner CSA: 44 × 22 = 968 cm².
Outer CSA: 44 × 24.2 = 1064.8 cm².
Ring area: 2 × (22/7) × 0.84 = 5.28 cm².
Sum: 968 + 1064.8 + 5.28 = 2038.08 cm².
44 × 54 = 2376 cm².
12320 / 1000 = 12.32 L.

Boxed Answer:
[ (i) (a) Inner CSA = 968 cm², (b) Outer CSA = 1064.8 cm², (c) TSA = 2038.08 cm², (ii) Sheet Area = 2376 cm², Capacity = 12.32 litres ]"""
}
modules[1]['worked_examples'].append(we_m2_extra)

# Module 3 (Right Circular Cones):
# Fix existing WE 1, 2 FORMULA USED
for we in modules[2]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nCone Slant Height: l = √(r² + h²)\nCone Curved Surface Area: CSA = πrl\nCone Total Surface Area: TSA = πr(l + r)\nCone Volume: V = (1/3)πr²h\n\nSTEP-BY-STEP")
        we['solution'] = sol

# Add in-text Exercise Set (pp. 11-12, book pp. 133-134)
we_m3_extra = {
    "problem": "Chapter 14, Section 14.3 Exercise Set (Ganita Manjari Part 2, Section 14.3, pp. 133–134):\n(i) Question 3: The height of a cone is 16 cm and its base radius is 12 cm. Find its curved surface area and total surface area (use π = 3.14).\n(ii) Question 5: The curved surface area of a cone is 308 cm² and its slant height is 14 cm. Find: (a) the radius of the base, (b) the total surface area of the cone (use π = 22/7).\n(iii) Question 6: A joker's cap is in the form of a right circular cone of base radius 7 cm and height 24 cm. Find the area of the sheet required to make 10 such caps.",
    "solution": """GIVEN:
(i) Cone 1: height h = 16 cm, radius r = 12 cm, π = 3.14.
(ii) Cone 2: CSA = 308 cm², slant height l = 14 cm, π = 22/7.
(iii) Joker's cap: radius r = 7 cm, height h = 24 cm; number of caps = 10.

TO FIND / TO PROVE:
(i) Slant height l, CSA, and TSA for Cone 1.
(ii) Base radius r and TSA for Cone 2.
(iii) Sheet area required for 10 joker caps.

FORMULA USED:
1. Slant height: l = √(r² + h²)
2. Curved Surface Area: CSA = πrl
3. Total Surface Area: TSA = πr(l + r)
4. Total Sheet Area for N caps = N × CSA (open cone base)

STEP-BY-STEP CALCULATION:
Part (i) Cone 1 Metrics:
1. Slant height l = √(12² + 16²) = √(144 + 256) = √400 = 20 cm.
2. CSA = πrl = 3.14 × 12 × 20 = 3.14 × 240 = 753.6 cm².
3. TSA = πr(l + r) = 3.14 × 12 × (20 + 12) = 3.14 × 12 × 32 = 1205.76 cm².

Part (ii) Cone 2 Metrics:
1. CSA = πrl = 308 cm²
   (22/7) × r × 14 = 308
   22 × 2 × r = 308  =>  44r = 308  =>  r = 308 / 44 = 7 cm.
2. TSA = πr(l + r) = (22/7) × 7 × (14 + 7) = 22 × 21 = 462 cm².

Part (iii) 10 Joker's Caps:
1. Slant height l = √(7² + 24²) = √(49 + 576) = √625 = 25 cm.
2. Sheet area for 1 cap (open at base) = CSA = πrl
   CSA = (22/7) × 7 × 25 = 22 × 25 = 550 cm².
3. For 10 caps:
   Total Area = 10 × 550 = 5500 cm².

[ROUGH_WORK]
√(144+256) = √400 = 20.
3.14 × 240 = 753.6 cm².
37.68 × 32 = 1205.76 cm².
308 / 44 = 7.
22 × 21 = 462 cm².
√(49+576) = 25. 22 × 25 = 550. 550 × 10 = 5500 cm².

Boxed Answer:
[ (i) CSA = 753.6 cm², TSA = 1205.76 cm², (ii) Base radius = 7 cm, TSA = 462 cm², (iii) Sheet Area for 10 caps = 5500 cm² ]"""
}
modules[2]['worked_examples'].append(we_m3_extra)

# Module 4 (Pyramidal Geometry):
# Fix existing WE 1, 2 FORMULA USED
for we in modules[3]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nRegular Square Pyramid Metrics:\nSlant Height: l = √(h² + (a/2)²)\nLateral Surface Area: LSA = 4 × [(1/2) · a · l] = 2al\nTotal Surface Area: TSA = a² + 2al\nVolume: V = (1/3)a²h\n\nSTEP-BY-STEP")
        we['solution'] = sol

# Module 5 (Spheres & Hemispheres):
# Fix existing WE 1, 2 FORMULA USED
for we in modules[4]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nSphere Surface Area: S = 4πr²; Volume: V = (4/3)πr³\nHemisphere CSA: 2πr²; TSA: 3πr²; Volume: (2/3)πr³\n\nSTEP-BY-STEP")
        we['solution'] = sol

# Add in-text Exercise Set (pp. 18-19) & End-of-Chapter Exercise 12(iii)
we_m5_extra = {
    "problem": "Chapter 14, Section 14.5 Exercise Set & End-of-Chapter Exercise 12(iii) (Ganita Manjari Part 2, pp. 140–141 & 145):\n(i) Section 14.5, Q7: The radius of a sphere is increased by x%. The volume of the sphere increases by 72.8%. Find the value of x.\n(ii) Section 14.5, Q8: The hemispherical dome of a building needs to be painted (Fig. 14.16). The circumference of the base of the dome is 35.2 m. Find the cost of painting it at ₹10 per 100 cm² (use π = 22/7).\n(iii) End-of-Chapter Exercise 12(iii): What is the change in volume when the radius r of a sphere is decreased by 1 unit?",
    "solution": """GIVEN:
(i) Sphere radius increased by x%: r' = r(1 + x/100); Volume increases by 72.8%: V' = 1.728 V.
(ii) Hemispherical dome: base circumference C = 35.2 m; painting rate = ₹10 per 100 cm² = ₹1000 per m² (since 1 m² = 10,000 cm²).
(iii) Sphere radius r changed to r - 1.

TO FIND / TO PROVE:
(i) Percentage increase x in radius.
(ii) Cost of painting the outer curved surface of the dome.
(iii) Algebraic expression for volume decrease ΔV.

FORMULA USED:
1. Sphere Volume Scaling: V ∝ r³  =>  V'/V = (r'/r)³ = (1 + x/100)³.
2. Circumference of Base: C = 2πr  =>  r = C / (2π).
3. Hemispherical Outer Dome Area: CSA = 2πr².
4. Sphere Volume Decrease: ΔV = V(r) - V(r - 1) = (4/3)π [r³ - (r - 1)³].

STEP-BY-STEP CALCULATION:
Part (i) Radius Expansion Percentage:
1. V' = 1.728 V  =>  (r'/r)³ = 1.728.
2. Taking cube root:
   1.728 = 1728 / 1000 = (12/10)³ = 1.2³.
   Thus r'/r = 1.2.
3. 1 + x/100 = 1.2  =>  x/100 = 0.2  =>  x = 20%.
Therefore, the radius was increased by 20%.

Part (ii) Cost of Painting Hemispherical Dome:
1. Base circumference C = 2πr = 35.2 m
   2 × (22/7) × r = 35.2
   (44/7) × r = 35.2  =>  r = (35.2 × 7) / 44 = 0.8 × 7 = 5.6 m.
2. Curved Surface Area of dome = 2πr²
   CSA = 2 × (22/7) × 5.6 × 5.6 = 2 × 22 × 0.8 × 5.6 = 44 × 4.48 = 197.12 m².
3. Cost of Painting:
   Rate = ₹10 per 100 cm².
   1 m² = 10,000 cm²  =>  Cost per m² = (10,000 / 100) × ₹10 = ₹1000/m².
   Total Cost = 197.12 m² × ₹1000/m² = ₹197,120.

Part (iii) Sphere Volume Decrease:
ΔV = (4/3)π r³ - (4/3)π (r - 1)³
Expand (r - 1)³ = r³ - 3r² + 3r - 1:
ΔV = (4/3)π [r³ - (r³ - 3r² + 3r - 1)]
ΔV = (4/3)π [3r² - 3r + 1] = 4πr² - 4πr + (4/3)π cubic units.

[ROUGH_WORK]
1.2³ = 1.728. (1.2 - 1) × 100 = 20%.
35.2 × 7 / 44 = 5.6 m.
2 × (22/7) × 5.6² = 197.12 m².
197.12 × 1000 = ₹197,120.
(4/3)π [3r² - 3r + 1] = 4πr² - 4πr + (4/3)π.

Boxed Answer:
[ (i) x = 20%, (ii) Painting Cost = ₹197,120, (iii) Volume Decrease = (4/3)π(3r² - 3r + 1) = 4πr² - 4πr + (4/3)π cubic units ]"""
}
modules[4]['worked_examples'].append(we_m5_extra)

# Module 6 (Real-World Solids & Fermi Guesstimates):
# Fix existing WE 1, 2 FORMULA USED
for we in modules[5]['worked_examples']:
    sol = we['solution']
    if "FORMULA USED" not in sol:
        sol = sol.replace("STEP-BY-STEP", "FORMULA USED:\nFermi Estimation & Spatial Modeling Principles:\n1. Conservation of Volume: V_total = Σ V_components.\n2. Volume Density & Thin Layer Shell Approximation: Δr ≈ V_fluid / (4πR²).\n\nSTEP-BY-STEP")
        we['solution'] = sol

# Add End-of-Chapter Exercises 3, 5, 17, 18, 21, 22
we_m6_all_missing = {
    "problem": "Chapter 14, End-of-Chapter Exercises 3, 5, 17, 18, 21 & 22 (Ganita Manjari Part 2, Section 14.7, pp. 144–147):\nComprehensive Fermi Estimation & Geometric Solutions:\n(i) Exercise 3: (a) Could a person drink enough water in a lifetime to fill an entire classroom? (b) Estimate the number of bricks required to build classroom walls.\n(ii) Exercise 5: If all 8 billion people in the world are crowded together in one location, how much surface area would they cover?\n(iii) Exercise 17: (a) A dough ball of radius 6 cm is prepared. Estimate how many chapatis of radius 7.5 cm and thickness 2 mm can be made from it. (b) Find the edible flesh volume of a hemispherical coconut.\n(iv) Exercise 18: Ganita Manjari Part 2 textbook: (a) If all 148 pages are laid side-by-side on the floor, will they cover the classroom floor? (b) How many textbooks fit into a storeroom of dimensions 15 ft × 20 ft × 30 ft?\n(v) Exercise 21: Determine the dimensions of a cuboid whose volume is halved when its surface area is doubled.\n(vi) Exercise 22: Formulate the mathematical volume model of a typical house.",
    "solution": """GIVEN:
(i) Lifetime water consumption (2 litres/day over 75 years); standard classroom dimensions: 8 m × 6 m × 3 m. Standard brick dimensions: 20 cm × 10 cm × 10 cm.
(ii) Global human population: N = 8 × 10⁹ people. Personal space in a tight crowd: a = 0.25 m² per person (4 people/m²).
(iii) Chapati dough sphere radius R = 6 cm. Single rolled chapati: cylinder of radius r = 7.5 cm, thickness t = 2 mm = 0.2 cm.
(iv) Textbook: 148 pages (74 leaves, each 21 cm × 28 cm). Storeroom: 15 ft × 20 ft × 30 ft (1 ft = 0.3048 m).
(v) Cuboid with initial volume V = lwh and surface area S = 2(lw + wh + hl).
(vi) Two-room residential house: footprint 10 m × 8 m, wall height 3.2 m, gable roof.

TO FIND / TO PROVE:
(i) Compare lifetime drinking volume to room volume, and compute brick count.
(ii) Compute total ground area occupied by humanity in km².
(iii) Compute number of chapatis rolled from dough sphere.
(iv) Compare total laid-out page area to classroom floor, and packing capacity of storeroom.
(v) Prove mathematical existence and constraints on dimensions for volume halving under area doubling.
(vi) Derive total house volume.

FORMULA USED:
1. Sphere Volume: V_sphere = (4/3)πR³
2. Cylinder Volume: V_cyl = πr²t
3. Brick Count: N_brick = Wall Volume / Brick Volume
4. Surface Area / Volume Invariant: S(λx) = λ²S(x), V(λx) = λ³V(x)
5. Storeroom Capacity: N = Room Volume / Book Volume

STEP-BY-STEP CALCULATION:
Part (i) Classroom vs Lifetime Water & Brickwork (Exercise 3):
(a) Lifetime water consumption:
    Daily intake = 2 litres = 0.002 m³.
    Total lifetime intake (75 years) = 75 × 365 × 0.002 = 54.75 m³ (54,750 litres).
    Classroom volume = 8 m × 6 m × 3 m = 144 m³.
    Fraction filled = 54.75 / 144 ≈ 0.380 (38.0%).
    Conclusion: A person drinks approximately 38% of the room's volume—enough to fill over one-third of the classroom, but NOT the entire room.
(b) Classroom brick count:
    Perimeter = 2(8 + 6) = 28 m. Wall thickness = 0.2 m, height = 3 m.
    Total wall volume = 28 × 0.2 × 3 = 16.8 m³.
    Deduct 15% for doors, windows, and mortar: Net brick volume = 0.85 × 16.8 ≈ 14.28 m³.
    Single brick volume = 0.2 m × 0.1 m × 0.1 m = 0.002 m³.
    Number of bricks = 14.28 / 0.002 ≈ 7,140 bricks.

Part (ii) Humanity Standing Together (Exercise 5):
Crowded standing area per human = 0.25 m² (4 people per square metre).
Total area = 8 × 10⁹ × 0.25 m² = 2 × 10⁹ m².
Convert to square kilometres: 1 km² = 10⁶ m².
Total area = 2 × 10⁹ / 10⁶ = 2,000 km².
Physical intuition: The entire human species of 8 billion people standing shoulder-to-shoulder would comfortably fit inside an area of 2,000 km²—smaller than the state of Goa (3,702 km²) or roughly the size of Mauritius (2,040 km²)!

Part (iii) Chapati Dough Sphere (Exercise 17):
1. Volume of spherical dough ball (R = 6 cm):
   V_dough = (4/3)π(6)³ = (4/3)π(216) = 288π cm³ ≈ 904.78 cm³.
2. Volume of single chapati (cylinder, r = 7.5 cm, t = 0.2 cm):
   V_chapati = πr²t = π × (7.5)² × 0.2 = π × 56.25 × 0.2 = 11.25π cm³ ≈ 35.34 cm³.
3. Number of chapatis = V_dough / V_chapati = 288π / 11.25π = 288 / 11.25 = 25.6.
   Conclusion: Approximately 25 to 26 chapatis can be made.

Part (iv) Textbook Laid Out vs Storeroom (Exercise 18):
(a) Total page area of Ganita Manjari Part 2:
    The book has 148 pages = 74 printed sheets (leaves).
    If leaves are separated and laid side-by-side: 74 × (0.21 m × 0.28 m) = 74 × 0.0588 = 4.35 m² (or 8.7 m² if all 148 page faces could be displayed).
    Classroom floor area = 8 m × 6 m = 48 m².
    Conclusion: The pages cover only about 9% to 18% of the floor, so they will NOT cover the entire classroom floor.
(b) Storeroom Capacity:
    Room dimensions: 15 ft × 20 ft × 30 ft = 9,000 ft³.
    1 ft = 0.3048 m  =>  1 ft³ ≈ 0.028317 m³.
    Room volume = 9,000 × 0.028317 ≈ 254.85 m³.
    Book dimensions: 21 cm × 28 cm × 1 cm = 0.21 × 0.28 × 0.01 = 0.000588 m³.
    Theoretical max books = 254.85 / 0.000588 ≈ 433,400 books.
    Accounting for 80% practical packing density (aisles and cartons): ~346,000 textbooks.

Part (v) Cuboid Halving Volume while Doubling Surface Area (Exercise 21):
1. If all dimensions of a cuboid are scaled by a factor k, S' = k²S and V' = k³V. Since k² = 2 implies k = √2, V' would be (√2)³ = 2√2 ≈ 2.83 times larger, not halved.
2. Therefore, the cuboid CANNOT be scaled uniformly. Instead, we must flatten it into a very thin, broad sheet!
3. Let initial cuboid be a cube of side a = 2: V₀ = 8, S₀ = 24.
   We require V = 4 and S = 48.
   Let the new cuboid have square base of side x and very thin height h:
   V = x²h = 4  =>  h = 4 / x².
   S = 2x² + 4xh = 2x² + 4x(4/x²) = 2x² + 16/x.
   Set S = 48:
   2x² + 16/x = 48  =>  x³ - 24x + 8 = 0.
   Testing roots: at x = 4.75, 4.75³ - 24(4.75) + 8 ≈ 107.17 - 114 + 8 = 1.17 ≈ 0.
   With x ≈ 4.76 cm, h = 4 / (4.76)² ≈ 0.177 cm.
   Check: V = (4.76)² × 0.177 = 4.00 cm³. S = 2(4.76)² + 4(4.76)(0.177) = 45.3 + 3.37 = 48.67 ≈ 48 cm².
   Dimensions: 4.76 cm × 4.76 cm × 0.177 cm achieves half the volume with double the surface area!

Part (vi) House Volume Project (Exercise 22):
Living area = 10 m × 8 m = 80 m².
Wall height = 3.2 m. Main living volume = 80 × 3.2 = 256 m³.
Gable triangular attic space: base = 8 m, peak height = 1.8 m, length = 10 m.
Attic volume = (1/2) × 8 × 1.8 × 10 = 72 m³.
Total House Volume = 256 + 72 = 328 m³.

[ROUGH_WORK]
75 × 365 × 2 = 54,750 L = 54.75 m³. 54.75 / 144 = 38%.
8 × 10⁹ × 0.25 = 2 × 10⁹ m² = 2000 km².
288 / 11.25 = 25.6 chapatis.
x³ - 24x + 8 = 0 -> root near x = 4.76, h = 0.177.
House: 256 + 72 = 328 m³.

Boxed Answer:
[ (i) Lifetime drinking fills 38% of classroom; Walls require ≈ 7,140 bricks, (ii) Entire human population occupies 2,000 km², (iii) 25 to 26 chapatis from dough ball, (iv) Textbook pages cover 9% to 18% of floor; Storeroom holds ≈ 346,000 books, (v) Flat cuboid (4.76 cm × 4.76 cm × 0.177 cm) doubles surface area while halving volume, (vi) Typical residential volume ≈ 328 m³ ]"""
}
modules[5]['worked_examples'].append(we_m6_all_missing)

with open('scripts/maths_pt2_modules/ch14_surface_areas_volumes.json', 'w', encoding='utf-8') as f:
    json.dump(modules, f, indent=2, ensure_ascii=False)

print('Updated ch14_surface_areas_volumes.json successfully!')
