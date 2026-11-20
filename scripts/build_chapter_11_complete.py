"""
Complete Synthesis of Class 10 Mathematics Chapter 11: Areas Related to Circles
Curriculum ID: 938ed126-df2f-438f-b6dc-8c7e1273ec24
100% NCERT Question & Example Coverage:
- Example 1, Example 2
- Exercise 11.1: Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14
All solved in Authentic Board Topper Layout: Given -> To Find/Prove -> Formula -> Step-by-Step -> [ROUGH_WORK] -> Boxed Answer.
Includes Page References, Section References, concise 2-5 word image_search_queries, and High-Precision Vector SVGs.
"""

import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "maths_class10_generators"))
from svg_builder_class10 import build_circle_sector_segment_svg

def get_ch11_complete_modules():
    CURRICULUM_ID = "938ed126-df2f-438f-b6dc-8c7e1273ec24"

    svg_sector_60 = build_circle_sector_segment_svg(
        radius=90, theta_deg=60,
        title="Sector and Segment Geometry (θ = 60°)",
        caption="Area of Sector = (θ/360°) × πr² | Area of Segment = Area of Sector - Area of ΔOAB"
    )

    svg_sector_120 = build_circle_sector_segment_svg(
        radius=90, theta_deg=120,
        title="Sector and Segment Geometry (θ = 120°)",
        caption="Decomposition: Area of ΔOAB = (1/2)r² sin(120°) = (√3/4)r²"
    )

    m1_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 156] Example 1: Find the area of the sector of a circle with radius 4 cm and of angle 30°. Also, find the area of the corresponding major sector (Use π = 3.14). (refer to Fig. 11.4)",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 156,
            "image_search_query": "circle sector area minor major",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Radius of circle r = 4 cm. Angle of minor sector θ = 30°. Value of π = 3.14 (Fig. 11.4).",
            "formula": "1. Area of minor sector = (θ / 360°) × πr²\n2. Area of major sector = πr² - Area of minor sector (or ((360° - θ) / 360°) × πr²).",
            "substitution": "Minor sector = (30° / 360°) × 3.14 × 4² = (1/12) × 3.14 × 16 = (4/3) × 3.14 = 12.56 / 3 = 4.19 cm².\nMajor sector = 3.14 × 16 - 4.19 = 50.24 - 4.19 = 46.05 cm².",
            "calculation": "1. Area of minor sector = (30/360) × 3.14 × 4 × 4 = (1/12) × 50.24 = 4.1867... ≈ 4.19 cm².\n2. Area of major sector = ((360 - 30)/360) × πr² = (330/360) × 3.14 × 16 = (11/12) × 50.24 = 46.0533... ≈ 46.05 cm².",
            "finalAnswer": "Minor sector area = 4.19 cm², Major sector area = 46.05 cm²",
            "unit": "cm²",
            "solution": "GIVEN:\nRadius of the circle, r = 4 cm.\nSector angle, θ = 30°.\nUse π = 3.14 (Fig. 11.4).\n\nTO FIND:\n(i) Area of the minor sector.\n(ii) Area of the corresponding major sector.\n\nFORMULA USED:\n- Area of minor sector = (θ / 360°) × πr²\n- Area of major sector = πr² - Area of minor sector, or ((360° - θ) / 360°) × πr².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute Area of Minor Sector:\nArea = (θ / 360°) × πr²\nArea = (30° / 360°) × 3.14 × 4²\nArea = (1 / 12) × 3.14 × 16\nArea = (4 / 3) × 3.14 = 12.56 / 3 ≈ 4.19 cm².\n\nStep 2: Compute Area of Major Sector:\nAngle of major sector = 360° - 30° = 330°.\nArea of major sector = (330° / 360°) × πr²\nArea = (11 / 12) × 3.14 × 16\nArea = (11 × 50.24) / 12 = 552.64 / 12 ≈ 46.05 cm².\n(Alternatively: Area of circle - Area of minor sector = 50.24 - 4.19 = 46.05 cm²).\n\n[ROUGH_WORK]\nTotal circle area = 3.14 × 16 = 50.24 cm². Minor fraction = 30/360 = 1/12. 50.24 / 12 = 4.186 ≈ 4.19. Major = 50.24 - 4.19 = 46.05 cm².\nBoxed Answer: [ Minor Sector = 4.19 cm², Major Sector = 46.05 cm² ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q1: Find the area of a sector of a circle with radius 6 cm if angle of the sector is 60° (Use π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "circle sector area formula",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Radius of circle r = 6 cm. Sector angle θ = 60°. Value of π = 22/7.",
            "formula": "Area of sector = (θ / 360°) × πr².",
            "substitution": "(60° / 360°) × (22 / 7) × 6² = (1 / 6) × (22 / 7) × 36 = 6 × (22 / 7) = 132 / 7 cm².",
            "calculation": "132 / 7 cm² = 18.86 cm².",
            "finalAnswer": "132/7 cm² (or 18.86 cm²)",
            "unit": "cm²",
            "solution": "GIVEN:\nRadius of the circle, r = 6 cm.\nAngle of the sector, θ = 60°.\nUse π = 22/7.\n\nTO FIND:\nArea of the sector.\n\nFORMULA USED:\nArea of a sector = (θ / 360°) × πr².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Substitute the given parameters into the formula:\nArea = (60° / 360°) × (22 / 7) × 6²\n\nStep 2: Simplify the angular fraction:\n60° / 360° = 1 / 6\n\nStep 3: Perform multiplication:\nArea = (1 / 6) × (22 / 7) × 36\nCancel 6 from numerator and denominator:\nArea = 6 × (22 / 7) = 132 / 7 cm².\nIn decimal form: 132 / 7 ≈ 18.86 cm².\n\n[ROUGH_WORK]\n(1/6) × 36 = 6. 6 × 22 = 132. 132 / 7 = 18.857... ≈ 18.86 cm².\nBoxed Answer: [ 132/7 cm² (or 18.86 cm²) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q2: Find the area of a quadrant of a circle whose circumference is 22 cm (Use π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "circle quadrant area circumference",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Circumference of the circle = 22 cm. Shape is a quadrant (θ = 90°).",
            "formula": "Circumference = 2πr ⇒ r = Circumference / (2π). Area of quadrant = (1/4)πr².",
            "substitution": "2 × (22/7) × r = 22 ⇒ r = 7/2 = 3.5 cm. Area = (1/4) × (22/7) × (7/2)².",
            "calculation": "Area = (1/4) × (22/7) × (49/4) = (1/4) × (154/4) = 77 / 8 cm² = 9.625 cm².",
            "finalAnswer": "77/8 cm² (or 9.625 cm²)",
            "unit": "cm²",
            "solution": "GIVEN:\nCircumference of the circle = 22 cm.\nThe sector is a quadrant, meaning its central angle θ = 90° (one-fourth of a full circle).\nUse π = 22/7.\n\nTO FIND:\nArea of the quadrant.\n\nFORMULA USED:\n1. Circumference of circle = 2πr\n2. Area of a quadrant = (1 / 4) × πr²\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Calculate the radius r of the circle:\n2πr = 22\n2 × (22 / 7) × r = 22\n(44 / 7) × r = 22\nr = (22 × 7) / 44 = 7 / 2 cm = 3.5 cm.\n\nStep 2: Calculate the area of the quadrant:\nArea = (1 / 4) × πr²\nArea = (1 / 4) × (22 / 7) × (7 / 2)²\nArea = (1 / 4) × (22 / 7) × (49 / 4)\nSimplify by cancelling 7 into 49 (gives 7) and 2 from 22 (gives 11 and 2):\nArea = (11 × 7) / (4 × 2) = 77 / 8 cm².\nIn decimal representation:\n77 / 8 = 9.625 cm².\n\n[ROUGH_WORK]\n2πr = 22 ⇒ r = 3.5 cm. Area = (1/4) × π × r² = 0.25 × (22/7) × 12.25 = 0.25 × 38.5 = 9.625 cm².\nBoxed Answer: [ 77/8 cm² (or 9.625 cm²) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 160] Exercise 11.1 Q14: Tick the correct answer in the following: Area of a sector of angle p (in degrees) of a circle with radius R is:\n(A) (p / 180) × 2πR\n(B) (p / 180) × πR²\n(C) (p / 360) × 2πR\n(D) (p / 720) × 2πR²",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 160,
            "image_search_query": "sector area algebraic formula mcq",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Angle of sector = p (in degrees). Radius of circle = R.",
            "formula": "Standard Area of Sector = (θ / 360°) × πR².",
            "substitution": "Replace θ by p: Area = (p / 360) × πR² = (p / (360 × 2)) × (2 × πR²) = (p / 720) × 2πR².",
            "calculation": "Option (A) is (p/180) × 2πR = arc length with halved denominator (incorrect).\nOption (B) is (p/180) × πR² (incorrect denominator).\nOption (C) is (p/360) × 2πR = arc length, not area (incorrect).\nOption (D) is (p/720) × 2πR² = (p / 360) × πR² (correct).",
            "finalAnswer": "(p / 720) × 2πR² (Option D)",
            "unit": "formula",
            "solution": "GIVEN:\nA circle with radius R and a sector with angle of measure p degrees.\n\nTO FIND:\nThe correct algebraic expression for the area of the sector among the given options.\n\nFORMULA USED:\nThe area of a sector of angle θ in a circle of radius r is:\nArea = (θ / 360) × πr².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Substitute the given parameters θ = p and r = R:\nArea = (p / 360) × πR²   ... (1)\n\nStep 2: Evaluate the given options against expression (1):\n- Option (A): (p / 180) × 2πR = (p / 90) × πR (Dimension of length, represents twice arc length, incorrect)\n- Option (B): (p / 180) × πR² (Incorrect denominator; would represent a sector of a circle with 180° full turn)\n- Option (C): (p / 360) × 2πR (Dimension of length, represents the arc length of the sector, not area)\n- Option (D): (p / 720) × 2πR²\nMultiply and divide by 2 in equation (1):\nArea = (p / (360 × 2)) × (2 × πR²) = (p / 720) × 2πR².\nThis matches Option (D) identically!\n\nTherefore, option (D) is the correct answer.\n\n[ROUGH_WORK]\n(p / 720) × 2πR² = (2 / 720) × pπR² = (1 / 360) × pπR² = (p / 360) × πR².\nBoxed Answer: [ (p / 720) × 2πR² (Option D) ].",
            "concept_questions": []
        }
    ]

    m2_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 157] Example 2: Find the area of the segment AYB shown in Fig. 11.6, if radius of the circle is 21 cm and ∠AOB = 120° (Use π = 22/7, √3 = 1.732).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 157,
            "image_search_query": "circle segment area obtuse angle 120",
            "has_diagram": True,
            "diagram_svg": svg_sector_120,
            "given": "Radius of circle r = 21 cm. Central angle ∠AOB = 120° (Fig. 11.6). Minor segment is bounded by chord AB and arc AYB.",
            "formula": "Area of segment AYB = Area of sector OAYB - Area of ΔOAB.\nArea of sector OAYB = (θ/360°) × πr².\nArea of ΔOAB with central angle 120° = (1/2) × base × height = (1/2) × r² × sin(120°) = (1/2) × r² × (√3/2) = (√3/4) × r².",
            "substitution": "Sector area = (120/360) × (22/7) × 21² = (1/3) × (22/7) × 441 = 22 × 21 = 462 cm².\nArea of ΔOAB: Draw OM ⊥ AB. In ΔOMA, ∠AOM = 60°, OA = 21 cm ⇒ AM = 21 sin(60°) = 21√3/2 cm, OM = 21 cos(60°) = 21/2 cm. AB = 2 × AM = 21√3 cm. Area(ΔOAB) = (1/2) × 21√3 × (21/2) = (441/4)√3 cm².",
            "calculation": "Area of segment = 462 - (441/4)√3 = (21/4)(88 - 21√3) cm².\nIn decimals: (441/4) × 1.732 = 110.25 × 1.732 = 190.95 cm².\nArea of segment = 462 - 190.95 = 271.05 cm².",
            "finalAnswer": "(21/4)(88 - 21√3) cm² (or 271.05 cm²)",
            "unit": "cm²",
            "solution": "GIVEN:\nRadius of the circle, r = 21 cm.\nCentral angle subtended by chord AB, ∠AOB = 120° (Fig. 11.6).\nUse π = 22/7.\n\nTO FIND:\nArea of the segment AYB.\n\nFORMULA USED:\nArea of segment AYB = Area of sector OAYB - Area of ΔOAB.\n- Area of sector OAYB = (θ / 360°) × πr²\n- Area of ΔOAB = (1/2) × base × height = (1/2) × AB × OM (where OM ⊥ AB).\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Calculate the Area of sector OAYB:\nArea of sector = (120° / 360°) × (22 / 7) × 21²\nArea of sector = (1 / 3) × (22 / 7) × 441\nSince 441 / 21 = 21:\nArea of sector = (1 / 3) × 22 × 63 = 22 × 21 = 462 cm².\n\nStep 2: Calculate the Area of ΔOAB:\nDraw OM ⊥ AB from centre O to chord AB.\nIn isosceles ΔOAB with OA = OB = 21 cm, the altitude OM bisects chord AB and ∠AOB:\n∠AOM = ∠BOM = 120° / 2 = 60°,\nand AM = BM = AB / 2.\nIn right triangle ΔOMA:\n- OM / OA = cos(60°) ⇒ OM = 21 × (1/2) = 21/2 cm.\n- AM / OA = sin(60°) ⇒ AM = 21 × (√3/2) = 21√3 / 2 cm.\nTherefore, chord length AB = 2 × AM = 2 × (21√3 / 2) = 21√3 cm.\nNow, Area(ΔOAB) = (1 / 2) × base × height\nArea(ΔOAB) = (1 / 2) × AB × OM\nArea(ΔOAB) = (1 / 2) × 21√3 × (21 / 2) = (441 / 4)√3 cm².\n\nStep 3: Calculate Area of Segment AYB:\nArea of segment AYB = Area of sector OAYB - Area of ΔOAB\nArea of segment AYB = 462 - (441 / 4)√3 cm²\nFactoring out 21/4:\n= (21 / 4) × [ (4 × 462 / 21) - 21√3 ]\n= (21 / 4) × (88 - 21√3) cm².\nUsing √3 ≈ 1.732:\nArea ≈ 462 - 190.95 = 271.05 cm².\n\n[ROUGH_WORK]\nSector area = 462 cm². ΔOAB area = (1/2)r² sin(120°) = 0.5 × 441 × (√3/2) = 110.25 × 1.732 = 190.953 cm². Segment = 462 - 190.95 = 271.05 cm².\nBoxed Answer: [ (21/4)(88 - 21√3) cm² (or 271.05 cm²) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q4: A chord of a circle of radius 10 cm subtends a right angle at the centre. Find the area of the corresponding:\n(i) minor segment\n(ii) major sector (Use π = 3.14).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "circle chord right angle minor segment major sector",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Radius of circle r = 10 cm. Central angle subtended by chord θ = 90°. Use π = 3.14.",
            "formula": "1. Area of minor sector = (90° / 360°) × πr² = (1/4)πr².\n2. Area of right ΔOAB = (1/2) × base × height = (1/2) × r × r = (1/2)r².\n3. Area of minor segment = Area of minor sector - Area of ΔOAB.\n4. Area of major sector = ((360° - 90°) / 360°) × πr² = (3/4)πr².",
            "substitution": "Minor sector = (1/4) × 3.14 × 10² = 314 / 4 = 78.5 cm².\nΔOAB = (1/2) × 10 × 10 = 50 cm².\nMinor segment = 78.5 - 50 = 28.5 cm².\nMajor sector = (3/4) × 3.14 × 100 = 3 × 78.5 = 235.5 cm².",
            "calculation": "Part (i): Minor segment area = 78.5 - 50 = 28.5 cm².\nPart (ii): Major sector area = (3/4) × 314 = 235.5 cm².",
            "finalAnswer": "(i) Minor segment = 28.5 cm², (ii) Major sector = 235.5 cm²",
            "unit": "cm²",
            "solution": "GIVEN:\nRadius of the circle, r = 10 cm.\nCentral angle subtended by the chord, θ = 90°.\nUse π = 3.14.\n\nTO FIND:\n(i) Area of the corresponding minor segment.\n(ii) Area of the corresponding major sector.\n\nFORMULA USED:\n- Area of minor sector = (θ / 360°) × πr²\n- Area of right-angled ΔOAB = (1 / 2) × OA × OB = (1 / 2) × r²\n- Area of minor segment = Area of minor sector - Area of ΔOAB\n- Area of major sector = ((360° - θ) / 360°) × πr²\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Compute Area of Minor Segment:\n1. Area of minor sector:\n   = (90° / 360°) × 3.14 × 10²\n   = (1 / 4) × 3.14 × 100\n   = 314 / 4 = 78.5 cm².\n2. Area of right ΔOAB:\n   = (1 / 2) × base × height\n   = (1 / 2) × 10 × 10 = 50 cm².\n3. Area of minor segment:\n   = Area of minor sector - Area of ΔOAB\n   = 78.5 - 50 = 28.5 cm².\n\nPart (ii): Compute Area of Major Sector:\nAngle of major sector = 360° - 90° = 270°.\nArea of major sector = (270° / 360°) × πr²\nArea = (3 / 4) × 3.14 × 10²\nArea = (3 / 4) × 314\nArea = 3 × 78.5 = 235.5 cm².\n(Alternatively: Area of circle - Area of minor sector = 314 - 78.5 = 235.5 cm²).\n\n[ROUGH_WORK]\nTotal area = 314 cm². 1/4th circle = 78.5 cm². Triangle = 50 cm². Segment = 78.5 - 50 = 28.5 cm². Major sector = 314 - 78.5 = 235.5 cm².\nBoxed Answer: [ (i) Minor segment = 28.5 cm², (ii) Major sector = 235.5 cm² ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q5: In a circle of radius 21 cm, an arc subtends an angle of 60° at the centre. Find:\n(i) the length of the arc\n(ii) area of the sector formed by the arc\n(iii) area of the segment formed by the corresponding chord (Use π = 22/7, √3 = 1.732).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "circle arc length sector segment equilateral triangle",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Radius of circle r = 21 cm. Central angle θ = 60°. Use π = 22/7.",
            "formula": "1. Length of arc = (θ / 360°) × 2πr\n2. Area of sector = (θ / 360°) × πr²\n3. Since θ = 60° and OA = OB = r, ΔOAB is an equilateral triangle. Area of equilateral triangle = (√3 / 4) × r².\n4. Area of segment = Area of sector - Area of ΔOAB.",
            "substitution": "(i) Arc length = (60/360) × 2 × (22/7) × 21 = (1/6) × 2 × 22 × 3 = 22 cm.\n(ii) Sector area = (60/360) × (22/7) × 21² = (1/6) × (22/7) × 441 = (1/6) × 1386 = 231 cm².\n(iii) ΔOAB area = (√3/4) × 21² = (441√3 / 4) cm².\nSegment area = 231 - (441√3 / 4) cm².",
            "calculation": "(i) Arc length = 22 cm.\n(ii) Sector area = 231 cm².\n(iii) Segment area = 231 - 110.25 × 1.732 = 231 - 190.95 = 40.05 cm².",
            "finalAnswer": "(i) Arc length = 22 cm, (ii) Sector area = 231 cm², (iii) Segment area = (231 - 441√3/4) cm² (or 40.05 cm²)",
            "unit": "cm, cm²",
            "solution": "GIVEN:\nRadius of the circle, r = 21 cm.\nCentral angle, θ = 60°.\nUse π = 22/7.\n\nTO FIND:\n(i) Length of the arc.\n(ii) Area of the sector formed by the arc.\n(iii) Area of the segment formed by the corresponding chord.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Compute Length of the Arc:\nFormula: Arc Length l = (θ / 360°) × 2πr\nl = (60° / 360°) × 2 × (22 / 7) × 21\nl = (1 / 6) × 2 × 22 × 3\nl = (1 / 6) × 132 = 22 cm.\n\nPart (ii): Compute Area of the Sector:\nFormula: Area = (θ / 360°) × πr²\nArea = (60° / 360°) × (22 / 7) × 21²\nArea = (1 / 6) × (22 / 7) × 441\nArea = (1 / 6) × 22 × 63\nArea = (1 / 6) × 1386 = 231 cm².\n\nPart (iii): Compute Area of the Segment:\nIn ΔOAB, OA = OB = 21 cm (radii) and ∠AOB = 60°.\nSince angles opposite to equal sides are equal: ∠OAB = ∠OBA = (180° - 60°) / 2 = 60°.\nTherefore, ΔOAB is an equilateral triangle with side length a = 21 cm.\nArea of equilateral ΔOAB = (√3 / 4) × a²\nArea(ΔOAB) = (√3 / 4) × 21² = (441√3 / 4) cm².\nNow, Area of segment = Area of sector - Area of ΔOAB\nArea of segment = 231 - (441√3 / 4) cm².\nUsing √3 ≈ 1.732:\nArea ≈ 231 - (441 × 1.732 / 4) = 231 - 190.95 = 40.05 cm².\n\n[ROUGH_WORK]\nEquilateral triangle with side 21: Area = (√3/4) × 441 = 110.25 × 1.732 = 190.953 cm². 231 - 190.95 = 40.05 cm².\nBoxed Answer: [ (i) 22 cm, (ii) 231 cm², (iii) (231 - 441√3/4) cm² (or 40.05 cm²) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q6: A chord of a circle of radius 15 cm subtends an angle of 60° at the centre. Find the areas of the corresponding minor and major segments of the circle (Use π = 3.14 and √3 = 1.73).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "circle chord minor major segment area",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Radius of circle r = 15 cm. Central angle θ = 60°. Use π = 3.14 and √3 = 1.73.",
            "formula": "1. Area of sector = (60°/360°) × πr² = (1/6)πr².\n2. In ΔOAB, since θ = 60° and OA = OB, ΔOAB is equilateral. Area(ΔOAB) = (√3/4)r².\n3. Area of minor segment = Area of sector - Area(ΔOAB).\n4. Area of major segment = Area of full circle - Area of minor segment = πr² - Minor segment area.",
            "substitution": "Circle area = 3.14 × 15² = 3.14 × 225 = 706.5 cm².\nSector area = (1/6) × 706.5 = 117.75 cm².\nΔOAB area = (1.73 / 4) × 225 = 389.25 / 4 = 97.3125 cm².\nMinor segment = 117.75 - 97.3125 = 20.4375 cm².\nMajor segment = 706.5 - 20.4375 = 686.0625 cm².",
            "calculation": "Minor segment = 20.4375 cm².\nMajor segment = 686.0625 cm².",
            "finalAnswer": "Minor segment = 20.4375 cm², Major segment = 686.0625 cm²",
            "unit": "cm²",
            "solution": "GIVEN:\nRadius of the circle, r = 15 cm.\nCentral angle, θ = 60°.\nUse π = 3.14 and √3 = 1.73.\n\nTO FIND:\n(i) Area of the minor segment.\n(ii) Area of the major segment.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute total area of the circle:\nArea of circle = πr² = 3.14 × 15² = 3.14 × 225 = 706.5 cm².\n\nStep 2: Compute Area of Minor Sector:\nArea of sector = (θ / 360°) × πr²\nArea of sector = (60° / 360°) × 706.5\nArea of sector = (1 / 6) × 706.5 = 117.75 cm².\n\nStep 3: Compute Area of Equilateral Triangle ΔOAB:\nSince OA = OB = 15 cm and ∠AOB = 60°, ΔOAB is an equilateral triangle:\nArea(ΔOAB) = (√3 / 4) × r²\nArea(ΔOAB) = (1.73 / 4) × 15² = (1.73 / 4) × 225\nArea(ΔOAB) = 389.25 / 4 = 97.3125 cm².\n\nStep 4: Compute Area of Minor Segment:\nArea of minor segment = Area of sector - Area(ΔOAB)\nArea of minor segment = 117.75 - 97.3125 = 20.4375 cm².\n\nStep 5: Compute Area of Major Segment:\nArea of major segment = Area of circle - Area of minor segment\nArea of major segment = 706.5 - 20.4375 = 686.0625 cm².\n\n[ROUGH_WORK]\nSector = 117.75. Triangle = 97.3125. Minor = 20.4375. Major = 706.5 - 20.4375 = 686.0625 cm².\nBoxed Answer: [ Minor segment = 20.44 cm², Major segment = 686.06 cm² ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q7: A chord of a circle of radius 12 cm subtends an angle of 120° at the centre. Find the area of the corresponding segment of the circle (Use π = 3.14 and √3 = 1.73).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "circle segment chord 120 degree calculation",
            "has_diagram": True,
            "diagram_svg": svg_sector_120,
            "given": "Radius of circle r = 12 cm. Central angle θ = 120°. Use π = 3.14 and √3 = 1.73.",
            "formula": "Area of segment = Area of sector - Area of ΔOAB.\nArea of sector = (120°/360°) × πr² = (1/3)πr².\nArea of ΔOAB = (1/2) × base × height = (1/2) × (2 r sin 60°) × (r cos 60°) = (1/2) r² sin 120° = (√3 / 4) r².",
            "substitution": "Sector area = (1/3) × 3.14 × 12² = (1/3) × 3.14 × 144 = 48 × 3.14 = 150.72 cm².\nΔOAB area: Draw OM ⊥ AB. In ΔOMA, AM = 12 sin 60° = 12(√3/2) = 6√3 cm ⇒ AB = 12√3 cm. OM = 12 cos 60° = 6 cm. Area(ΔOAB) = (1/2) × 12√3 × 6 = 36√3 = 36 × 1.73 = 62.28 cm².\nSegment area = 150.72 - 62.28 = 88.44 cm².",
            "calculation": "150.72 - 62.28 = 88.44 cm².",
            "finalAnswer": "88.44 cm²",
            "unit": "cm²",
            "solution": "GIVEN:\nRadius of the circle, r = 12 cm.\nCentral angle, θ = 120°.\nUse π = 3.14 and √3 = 1.73.\n\nTO FIND:\nArea of the corresponding segment of the circle.\n\nFORMULA USED:\nArea of segment = Area of sector OAB - Area of ΔOAB.\n- Area of sector = (θ / 360°) × πr²\n- Area of ΔOAB with central angle 120° = (1 / 2) × r² × sin(120°) = (√3 / 4) × r².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute Area of Sector OAB:\nArea of sector = (120° / 360°) × 3.14 × 12²\nArea of sector = (1 / 3) × 3.14 × 144\nArea of sector = 48 × 3.14 = 150.72 cm².\n\nStep 2: Compute Area of ΔOAB:\nDraw altitude OM ⊥ AB from centre O to chord AB.\nIn right ΔOMA (with ∠AOM = 120°/2 = 60°):\n- OM = OA cos(60°) = 12 × (1/2) = 6 cm.\n- AM = OA sin(60°) = 12 × (√3/2) = 6√3 cm.\nChord AB = 2 × AM = 2 × 6√3 = 12√3 cm.\nArea of ΔOAB = (1 / 2) × base × height\nArea of ΔOAB = (1 / 2) × 12√3 × 6 = 36√3 cm².\nSubstitute √3 = 1.73:\nArea of ΔOAB = 36 × 1.73 = 62.28 cm².\n\nStep 3: Compute Area of Segment:\nArea of segment = Area of sector - Area of ΔOAB\nArea of segment = 150.72 - 62.28 = 88.44 cm².\n\n[ROUGH_WORK]\nSector = 150.72. Triangle = 36 × 1.73 = 62.28. Segment = 150.72 - 62.28 = 88.44 cm².\nBoxed Answer: [ 88.44 cm² ].",
            "concept_questions": []
        }
    ]

    m3_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q3: The length of the minute hand of a clock is 14 cm. Find the area swept by the minute hand in 5 minutes (Use π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "clock minute hand area swept 5 minutes",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Length of the minute hand r = 14 cm. Time elapsed = 5 minutes. Use π = 22/7.",
            "formula": "The minute hand completes a full circle (360°) in 60 minutes. Angle swept in 1 minute = 360° / 60 = 6°. Angle in t minutes = t × 6°. Area swept = (θ / 360°) × πr².",
            "substitution": "Angle swept in 5 minutes θ = 5 × 6° = 30°. Area = (30° / 360°) × (22 / 7) × 14² = (1 / 12) × (22 / 7) × 196.",
            "calculation": "196 / 7 = 28. (1/12) × 22 × 28 = (22 × 7) / 3 = 154 / 3 cm² = 51.33 cm².",
            "finalAnswer": "154/3 cm² (or 51.33 cm²)",
            "unit": "cm²",
            "solution": "GIVEN:\nLength of the minute hand of the clock, r = 14 cm.\nTime duration, t = 5 minutes.\nUse π = 22/7.\n\nTO FIND:\nArea swept by the minute hand in 5 minutes.\n\nFORMULA USED:\n- In 60 minutes, the minute hand makes one full 360° revolution.\n- Angle swept in 1 minute = 360° / 60 = 6°.\n- Angle swept in t minutes: θ = t × 6°.\n- Area swept = Area of sector = (θ / 360°) × πr².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Determine the angle θ swept in 5 minutes:\nθ = 5 × (360° / 60) = 5 × 6° = 30°.\n\nStep 2: Calculate the area of the sector swept:\nArea = (θ / 360°) × πr²\nArea = (30° / 360°) × (22 / 7) × 14²\nArea = (1 / 12) × (22 / 7) × 196\nSince 196 / 7 = 28:\nArea = (1 / 12) × 22 × 28\nDivide 28 and 12 by 4:\nArea = (22 × 7) / 3 = 154 / 3 cm².\nIn decimal representation:\n154 / 3 ≈ 51.33 cm².\n\n[ROUGH_WORK]\nFraction of clock = 5/60 = 1/12. Area = (1/12) × (22/7) × 196 = (1/12) × 616 = 154/3 = 51.33 cm².\nBoxed Answer: [ 154/3 cm² (or 51.33 cm²) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 158] Exercise 11.1 Q8: A horse is tied to a peg at one corner of a square shaped grass field of side 15 m by means of a 5 m long rope (see Fig. 11.8). Find:\n(i) the area of that part of the field in which the horse can graze.\n(ii) the increase in the grazing area if the rope were 10 m long instead of 5 m (Use π = 3.14).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 158,
            "image_search_query": "horse grazing square field corner quadrant",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Square field of side 15 m. Corner angle of square = 90°. Initial rope length r1 = 5 m. Extended rope length r2 = 10 m (Fig. 11.8). Use π = 3.14.",
            "formula": "The grazed region is a quadrant of a circle (sector with θ = 90°). Area of quadrant = (1/4)πr². Increase in area = (1/4)π(r2² - r1²).",
            "substitution": "(i) Area with r1 = 5 m: (1/4) × 3.14 × 5² = (1/4) × 3.14 × 25 = 78.5 / 4 = 19.625 m².\n(ii) Increase with r2 = 10 m: (1/4) × 3.14 × (10² - 5²) = (1/4) × 3.14 × 75 = 235.5 / 4 = 58.875 m².",
            "calculation": "(i) Grazing area = 19.625 m².\n(ii) Increase in grazing area = 58.875 m².",
            "finalAnswer": "(i) 19.625 m², (ii) 58.875 m²",
            "unit": "m²",
            "solution": "GIVEN:\nSide of square grass field = 15 m.\nEach corner angle of the square field is 90°.\nInitial rope length, r1 = 5 m.\nExtended rope length, r2 = 10 m.\nUse π = 3.14 (Fig. 11.8).\n\nTO FIND:\n(i) Area of the field the horse can graze with 5 m rope.\n(ii) Increase in grazing area if rope is lengthened to 10 m.\n\nFORMULA USED:\nSince the horse is pegged at a 90° corner, the grazing region forms a quadrant (one-fourth) of a circle:\nArea of grazing quadrant = (90° / 360°) × πr² = (1 / 4) × πr².\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Grazing area with 5 m rope:\nArea = (1 / 4) × π × r1²\nArea = (1 / 4) × 3.14 × 5²\nArea = (1 / 4) × 3.14 × 25\nArea = 78.5 / 4 = 19.625 m².\n\nPart (ii): Increase in grazing area with 10 m rope:\nGrazing area with 10 m rope:\nArea_new = (1 / 4) × π × r2²\nArea_new = (1 / 4) × 3.14 × 10²\nArea_new = (1 / 4) × 3.14 × 100\nArea_new = 314 / 4 = 78.5 m².\n\nIncrease in grazing area = Area_new - Area_initial\nIncrease = 78.5 - 19.625 = 58.875 m².\n(Alternatively: (1/4) × 3.14 × (100 - 25) = (1/4) × 3.14 × 75 = 235.5 / 4 = 58.875 m²).\n\n[ROUGH_WORK]\n(i) 0.25 × 3.14 × 25 = 19.625 m². (ii) 0.25 × 3.14 × 100 = 78.5 m². Difference = 78.5 - 19.625 = 58.875 m².\nBoxed Answer: [ (i) 19.625 m², (ii) 58.875 m² ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 159] Exercise 11.1 Q9: A brooch is made with silver wire in the form of a circle with diameter 35 mm. The wire is also used in making 5 diameters which divide the circle into 10 equal sectors as shown in Fig. 11.9. Find:\n(i) the total length of the silver wire required.\n(ii) the area of each sector of the brooch (Use π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 159,
            "image_search_query": "brooch silver wire sectors diameter",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Diameter of circular brooch d = 35 mm ⇒ radius r = 35/2 mm. Number of diameters made of wire = 5. Circle divided into 10 equal sectors (Fig. 11.9). Use π = 22/7.",
            "formula": "1. Total length of silver wire = Circumference of circle + (5 × Diameter) = πd + 5d.\n2. Area of each sector = Total Area of circle / 10 = (1/10) × πr².",
            "substitution": "(i) Total wire = (22/7) × 35 + 5 × 35 = 22 × 5 + 175 = 110 + 175 = 285 mm.\n(ii) Area of each sector = (1/10) × (22/7) × (35/2)² = (1/10) × (22/7) × (1225/4).",
            "calculation": "(1/10) × 22 × (175/4) = (11 × 175) / (10 × 2) = (11 × 35) / 4 = 385 / 4 mm² = 96.25 mm².",
            "finalAnswer": "(i) Total wire length = 285 mm, (ii) Area of each sector = 385/4 mm² (or 96.25 mm²)",
            "unit": "mm, mm²",
            "solution": "GIVEN:\nDiameter of the circular brooch, d = 35 mm.\nRadius, r = d / 2 = 35 / 2 mm.\nNumber of diameters formed with wire = 5.\nThe brooch is divided into 10 equal sectors (Fig. 11.9).\nUse π = 22/7.\n\nTO FIND:\n(i) Total length of the silver wire required.\n(ii) Area of each of the 10 sectors of the brooch.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Compute Total Length of Silver Wire:\nThe wire is used to form the outer circular circumference plus 5 full diameters:\nTotal Length = Circumference + 5 × Diameter\nCircumference = 2πr = πd = (22 / 7) × 35 = 22 × 5 = 110 mm.\nLength of 5 diameters = 5 × 35 = 175 mm.\nTotal wire required = 110 + 175 = 285 mm.\n\nPart (ii): Compute Area of Each Sector:\nSince the circle is divided into 10 equal sectors, the central angle of each sector is:\nθ = 360° / 10 = 36°.\nArea of each sector = (θ / 360°) × πr²\nArea = (1 / 10) × πr²\nArea = (1 / 10) × (22 / 7) × (35 / 2) × (35 / 2)\nSimplify by cancelling 7 into 35 (giving 5):\nArea = (1 / 10) × 22 × 5 × (35 / 4)\nSince 22 × 5 = 110 and 110 / 10 = 11:\nArea = 11 × (35 / 4) = 385 / 4 mm².\nIn decimal form:\n385 / 4 = 96.25 mm².\n\n[ROUGH_WORK]\nTotal wire: 110 mm (outer loop) + 5 × 35 mm = 110 + 175 = 285 mm. Total area = (22/7) × (35/2)² = 962.5 mm². Divided by 10 = 96.25 mm² = 385/4 mm².\nBoxed Answer: [ (i) 285 mm, (ii) 385/4 mm² (or 96.25 mm²) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 159] Exercise 11.1 Q10: An umbrella has 8 ribs which are equally spaced (see Fig. 11.10). Assuming umbrella to be a flat circle of radius 45 cm, find the area between the two consecutive ribs of the umbrella (Use π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 159,
            "image_search_query": "umbrella ribs equal sectors area calculation",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Flat circular model with radius r = 45 cm. Number of equally spaced ribs = 8, dividing circle into 8 equal sectors (Fig. 11.10). Use π = 22/7.",
            "formula": "Central angle between two consecutive ribs θ = 360° / 8 = 45°. Area between two ribs = (1/8) × πr².",
            "substitution": "(1 / 8) × (22 / 7) × 45² = (1 / 8) × (22 / 7) × 2025.",
            "calculation": "(11 × 2025) / (4 × 7) = 22275 / 28 cm² = 795.54 cm².",
            "finalAnswer": "22275/28 cm² (or 795.54 cm²)",
            "unit": "cm²",
            "solution": "GIVEN:\nAn umbrella modeled as a flat circle of radius r = 45 cm.\nThere are 8 ribs equally spaced, creating 8 equal sectors (Fig. 11.10).\nUse π = 22/7.\n\nTO FIND:\nArea between two consecutive ribs of the umbrella.\n\nFORMULA USED:\n- Angle between two consecutive ribs, θ = 360° / 8 = 45°.\n- Area between two consecutive ribs = Area of one sector = (1 / 8) × πr².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute the fraction of the circle:\nSince there are 8 equal sectors, each sector has an area equal to (1 / 8) of the total circular area.\n\nStep 2: Apply the sector area formula:\nArea = (1 / 8) × πr²\nArea = (1 / 8) × (22 / 7) × 45²\nArea = (1 / 8) × (22 / 7) × 2025\n\nStep 3: Simplify by cancelling 2 from 22 and 8:\nArea = (11 × 2025) / (4 × 7)\nArea = 22275 / 28 cm².\nIn decimal form:\n22275 / 28 ≈ 795.54 cm².\n\n[ROUGH_WORK]\n45² = 2025. 2025 × 11 = 22275. Denominator = 4 × 7 = 28. 22275 / 28 = 795.5357... ≈ 795.54 cm².\nBoxed Answer: [ 22275/28 cm² (or 795.54 cm²) ].",
            "concept_questions": []
        }
    ]

    m4_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 159] Exercise 11.1 Q11: A car has two wipers which do not overlap. Each wiper has a blade of length 25 cm sweeping through an angle of 115°. Find the total area cleaned at each sweep of the blades (Use π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 159,
            "image_search_query": "car wipers sweeping angle sector area",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Two non-overlapping blades. Length of each blade r = 25 cm. Sweep angle θ = 115°. Use π = 22/7.",
            "formula": "Area swept by 1 blade = (θ / 360°) × πr². Total area swept by 2 blades = 2 × Area of 1 blade.",
            "substitution": "Total Area = 2 × [(115° / 360°) × (22 / 7) × 25²].",
            "calculation": "Total Area = 2 × (23 / 72) × (22 / 7) × 625 = (23 × 11 × 625) / (18 × 7) = 158125 / 126 cm² = 1254.96 cm².",
            "finalAnswer": "158125/126 cm² (or 1254.96 cm²)",
            "unit": "cm²",
            "solution": "GIVEN:\nNumber of wiper blades = 2 (non-overlapping).\nLength of each blade, r = 25 cm.\nAngle of sweep for each blade, θ = 115°.\nUse π = 22/7.\n\nTO FIND:\nTotal area cleaned at each sweep of the blades.\n\nFORMULA USED:\nArea cleaned by one blade = Area of sector = (θ / 360°) × πr².\nTotal area cleaned by two identical non-overlapping blades = 2 × (θ / 360°) × πr².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Write down the expression for the combined area:\nTotal Area = 2 × [ (115° / 360°) × (22 / 7) × 25² ]\n\nStep 2: Simplify fractions:\nCancel 2 with 360:\nTotal Area = (115 / 180) × (22 / 7) × 625\nDivide 115 and 180 by 5:\nTotal Area = (23 / 36) × (22 / 7) × 625\nDivide 22 and 36 by 2:\nTotal Area = (23 / 18) × (11 / 7) × 625\n\nStep 3: Multiply numerators and denominators:\nNumerator = 23 × 11 × 625 = 253 × 625 = 158125.\nDenominator = 18 × 7 = 126.\nTotal Area = 158125 / 126 cm².\nIn decimal representation:\n158125 / 126 ≈ 1254.96 cm².\n\n[ROUGH_WORK]\n253 × 625 = 158125. 18 × 7 = 126. 158125 / 126 = 1254.9603... ≈ 1254.96 cm².\nBoxed Answer: [ 158125/126 cm² (or 1254.96 cm²) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 159] Exercise 11.1 Q12: To warn ships for underwater rocks, a lighthouse spreads a red coloured light over a sector of angle 80° to a distance of 16.5 km. Find the area of the sea over which the ships are warned (Use π = 3.14).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 159,
            "image_search_query": "lighthouse sector warning area angle",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Sector angle θ = 80°. Distance of spread (radius) r = 16.5 km. Use π = 3.14.",
            "formula": "Area of sector = (θ / 360°) × πr².",
            "substitution": "Area = (80° / 360°) × 3.14 × (16.5)² = (2 / 9) × 3.14 × 272.25.",
            "calculation": "272.25 / 9 = 30.25. Area = 2 × 3.14 × 30.25 = 6.28 × 30.25 = 189.97 km².",
            "finalAnswer": "189.97 km²",
            "unit": "km²",
            "solution": "GIVEN:\nSector angle of light spread, θ = 80°.\nDistance over which the light spreads (radius), r = 16.5 km.\nUse π = 3.14.\n\nTO FIND:\nArea of the sea over which the ships are warned.\n\nFORMULA USED:\nArea of the sea warned = Area of sector = (θ / 360°) × πr².\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Substitute the given values into the sector formula:\nArea = (80° / 360°) × 3.14 × (16.5)²\n\nStep 2: Simplify the angular fraction:\n80° / 360° = 8 / 36 = 2 / 9.\n\nStep 3: Compute (16.5)²:\n16.5 × 16.5 = 272.25.\n\nStep 4: Divide 272.25 by 9:\n272.25 / 9 = 30.25.\n\nStep 5: Multiply the remaining factors:\nArea = 2 × 3.14 × 30.25\nArea = 6.28 × 30.25 = 189.97 km².\n\n[ROUGH_WORK]\n(2/9) × 3.14 × 272.25 = 2 × 3.14 × 30.25 = 6.28 × 30.25 = 189.97 km².\nBoxed Answer: [ 189.97 km² ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 159] Exercise 11.1 Q13: A round table cover has six equal designs as shown in Fig. 11.11. If the radius of the cover is 28 cm, find the cost of making the designs at the rate of ₹ 0.35 per cm² (Use √3 = 1.7, π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 159,
            "image_search_query": "round table cover hexagonal design segments cost",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Round table cover of radius r = 28 cm. Six equal designs formed by the minor segments of 6 chords forming a regular hexagon (Fig. 11.11). Rate of making design = ₹ 0.35 per cm². Use √3 = 1.7, π = 22/7.",
            "formula": "Central angle for each of 6 equal designs θ = 360° / 6 = 60°.\nArea of 1 design = Area of minor segment = Area of sector (60°) - Area of equilateral ΔOAB.\nArea of 6 designs = 6 × [ ((60/360) × πr²) - ((√3/4) × r²) ].\nCost = Total Design Area × Rate.",
            "substitution": "Area of sector = (1/6) × (22/7) × 28² = (1/6) × (22/7) × 784 = (22 × 112) / 6 = 2464 / 6 = 410.67 cm².\nArea of equilateral Δ = (1.7 / 4) × 28² = (1.7 / 4) × 784 = 1.7 × 196 = 333.2 cm².\nArea of 1 design = 410.67 - 333.2 = 77.47 cm².\nTotal Area of 6 designs = 6 × (410.67 - 333.2) = 2464 - 6 × 333.2 = 2464 - 1999.2 = 464.8 cm².\nCost = 464.8 × 0.35 = ₹ 162.68.",
            "calculation": "Total Area of 6 designs = 464.8 cm².\nCost = 464.8 × 0.35 = ₹ 162.68.",
            "finalAnswer": "₹ 162.68",
            "unit": "rupees",
            "solution": "GIVEN:\nRadius of the round table cover, r = 28 cm.\nNumber of equal designs = 6 (arranged along the circumference as circular segments, Fig. 11.11).\nCost rate = ₹ 0.35 per cm².\nUse √3 = 1.7 and π = 22/7.\n\nTO FIND:\nTotal cost of making the 6 designs.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Determine the central angle of each design segment:\nSince the cover has 6 equal designs forming a regular hexagonal boundary:\nθ = 360° / 6 = 60°.\n\nStep 2: Area of one sector of 60°:\nArea of 1 sector = (60° / 360°) × πr²\nArea = (1 / 6) × (22 / 7) × 28²\nArea = (1 / 6) × (22 / 7) × 784\nSince 784 / 7 = 112:\nArea = (22 × 112) / 6 = 2464 / 6 cm².\n\nStep 3: Area of one equilateral triangle ΔOAB:\nIn ΔOAB, OA = OB = 28 cm and ∠AOB = 60°, so ΔOAB is equilateral:\nArea(ΔOAB) = (√3 / 4) × r²\nArea(ΔOAB) = (1.7 / 4) × 28²\nArea(ΔOAB) = (1.7 / 4) × 784 = 1.7 × 196 = 333.2 cm².\n\nStep 4: Area of one design (segment):\nArea of 1 design = Area of 1 sector - Area of ΔOAB\nArea of 1 design = (2464 / 6) - 333.2 cm².\n\nStep 5: Total Area of all 6 designs:\nTotal Area = 6 × [ (2464 / 6) - 333.2 ]\nTotal Area = 2464 - (6 × 333.2)\nTotal Area = 2464 - 1999.2 = 464.8 cm².\n\nStep 6: Compute the total cost:\nCost = Total Area × Rate\nCost = 464.8 × ₹ 0.35 = ₹ 162.68.\n\n[ROUGH_WORK]\n6 sectors = full circle area = (22/7) × 784 = 2464 cm². 6 triangles = 6 × 333.2 = 1999.2 cm². Design area = 2464 - 1999.2 = 464.8 cm². Cost = 464.8 × 0.35 = ₹ 162.68.\nBoxed Answer: [ ₹ 162.68 ].",
            "concept_questions": []
        }
    ]

    m5_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 11 | Section 11.1 | Page 160] Synthesis Master Problem: A square ABCD of side 14 cm is inscribed with four equal semicircles drawn on each side as diameter, or four quadrants drawn at each corner. Find the area of the shaded flower-leaf design formed in the interior (Take π = 22/7).",
            "section": "11.1 Areas of Sector and Segment of a Circle",
            "page_number": 160,
            "image_search_query": "square four quadrants shaded flower design area",
            "has_diagram": True,
            "diagram_svg": svg_sector_60,
            "given": "Square ABCD of side a = 14 cm. Semicircles are drawn on each of the four sides of the square as diameters. Diameter d = 14 cm ⇒ radius r = 7 cm. Shaded region consists of 4 petals/leaves formed by intersection of semicircles. Use π = 22/7.",
            "formula": "Area of 4 unshaded corner regions (I + II + III + IV) = 2 × [Area of Square - Area of 2 Semicircles (1 full circle)].\nArea of Shaded Flower Design = Area of Square - Area of 4 unshaded corner regions.",
            "substitution": "Area of Square = 14 × 14 = 196 cm².\nArea of 2 semicircles = Area of 1 full circle = πr² = (22/7) × 7² = 154 cm².\nArea of 2 unshaded regions = 196 - 154 = 42 cm².\nArea of all 4 unshaded regions = 2 × 42 = 84 cm².\nArea of shaded design = 196 - 84 = 112 cm².",
            "calculation": "Area of shaded design = 112 cm².",
            "finalAnswer": "112 cm²",
            "unit": "cm²",
            "solution": "GIVEN:\nA square ABCD of side length a = 14 cm.\nFour semicircles are drawn inside the square taking each of the four sides AB, BC, CD, and DA as diameter.\nDiameter of each semicircle = 14 cm ⇒ radius, r = 7 cm.\nUse π = 22/7.\n\nTO FIND:\nArea of the four shaded petals/leaves formed in the interior of the square.\n\nFORMULA USED:\n- Area of square = a²\n- Area of semicircle = (1/2)πr²\n- Two semicircles combined = One full circle of radius r = πr²\n- Area of shaded design = Area of square - Area of 4 unshaded corner regions.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute Area of Square ABCD:\nArea_square = 14 × 14 = 196 cm².\n\nStep 2: Calculate area of unshaded corner regions:\nLet the four unshaded corner regions be marked I, II, III, and IV.\nConsider the pair of semicircles drawn on opposite sides AB and CD as diameters:\nSum of areas of these two semicircles = 2 × [(1/2)πr²] = πr² = (22 / 7) × 7² = 154 cm².\nThe remaining area in the square when these two semicircles are removed consists of regions I and III:\nArea(I + III) = Area_square - Area of two semicircles\nArea(I + III) = 196 - 154 = 42 cm².\nBy identical symmetry for semicircles on sides AD and BC:\nArea(II + IV) = 196 - 154 = 42 cm².\nTotal area of all 4 unshaded regions = Area(I + III) + Area(II + IV) = 42 + 42 = 84 cm².\n\nStep 3: Compute Area of Shaded Petal Design:\nArea of shaded design = Area_square - Total unshaded area\nArea of shaded design = 196 - 84 = 112 cm².\n\n[ROUGH_WORK]\nSum of 4 semicircles = 2 × 154 = 308 cm². Each shaded petal is counted twice: Area_shaded = 308 - 196 = 112 cm²!\nBoxed Answer: [ 112 cm² ].",
            "concept_questions": []
        }
    ]

    # Load existing module metadata
    with open("scripts/maths_class10_modules/ch11_areas_related_to_circles.json", "r", encoding="utf-8") as f:
        modules = json.load(f)

    modules[0]["worked_examples"] = m1_worked_examples
    modules[1]["worked_examples"] = m2_worked_examples
    modules[2]["worked_examples"] = m3_worked_examples
    modules[3]["worked_examples"] = m4_worked_examples
    modules[4]["worked_examples"] = m5_worked_examples

    return modules

if __name__ == "__main__":
    mods = get_ch11_complete_modules()
    out_file = "scripts/maths_class10_modules/ch11_areas_related_to_circles.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2, ensure_ascii=False)
    
    total_we = sum(len(m["worked_examples"]) for m in mods)
    print(f"Ch 11 complete: {len(mods)} modules, {total_we} worked examples saved to {out_file}.")
