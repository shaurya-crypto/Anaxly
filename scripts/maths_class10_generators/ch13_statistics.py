"""
Class 10 Mathematics - Chapter 13: Statistics (NCERT CBSE)
Curriculum ID: ee79fe72-f746-45c7-a36e-b5a11c82d479
Fully compliant with Invariant 10:
- 6 dedicated modules (Theory in M1-M3, dedicated solvers M4-M6)
- 100% of all NCERT exercise questions (Ex 13.1, Ex 13.2, Ex 13.3) and worked examples solved step-by-step
- Authentic Topper Board Layout: Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer
- High-Precision Vector SVGs from svg_builder_class10 (Dual Cumulative Frequency Ogives and Modal Class Histogram)
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
from svg_builder_class10 import build_statistics_chart_svg, get_svg_wrapper

def get_ch13_modules():
    CURRICULUM_ID = "ee79fe72-f746-45c7-a36e-b5a11c82d479"
    
    # SVG 1: Dual Ogives intersecting at Median
    svg_ogives = build_statistics_chart_svg(
        chart_type="ogive",
        title="Statistics: Less-than & More-than Ogives Intersecting at Median",
        caption="Intersection coordinates (x, y) = (Median, N/2). Empirical formula: 3 Median = Mode + 2 Mean"
    )
    
    # SVG 2: Histogram with Modal Class
    svg_histogram = build_statistics_chart_svg(
        chart_type="histogram_mode",
        title="Statistics: Histogram & Modal Class Peak Identification",
        caption="Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h"
    )

    modules = [
        # Module 1: Mean of Grouped Data (Direct, Assumed Mean & Step-Deviation)
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 1,
            "title": "Mean of Grouped Data: Direct, Assumed Mean & Step-Deviation Methods",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Master all three methods for computing the arithmetic mean of grouped continuous frequency distributions: (1) Direct Method (x̄ = Σfi·xi / Σfi), (2) Assumed Mean Method (x̄ = a + Σfi·di / Σfi), and (3) Step-Deviation Method (x̄ = a + [Σfi·ui / Σfi] × h). Understand class marks xi = (Upper + Lower) / 2 and deviations.",
            "key_concepts": [
                "Class Mark (xi): Midpoint of each class interval: xi = (Upper Class Limit + Lower Class Limit) / 2",
                "Direct Method: x̄ = ( Σ fi · xi ) / ( Σ fi )",
                "Assumed Mean Method: Choose central xi as assumed mean 'a', compute deviations di = xi - a: x̄ = a + ( Σ fi · di ) / ( Σ fi )",
                "Step-Deviation Method: When deviations share common factor 'h' (class width), compute ui = (xi - a) / h: x̄ = a + [ ( Σ fi · ui ) / ( Σ fi ) ] × h",
                "Invariance Principle: All three methods yield the EXACT same numerical answer; step-deviation compresses multi-digit multiplications into single-digit arithmetic!"
            ],
            "subtopics": [
                "Computing class marks for continuous and discrete intervals",
                "Choosing the optimal assumed mean 'a'",
                "Step-deviation transformation ui = (xi - a) / h",
                "Worked Example 1, Example 2, Example 3 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Example 2 (NCERT): The table below gives the percentage distribution of female teachers in the primary schools of rural areas of various states and union territories (UT) of India. Find the mean percentage of female teachers using all three methods.\n\nPercentage: 15-25 (6), 25-35 (11), 35-45 (7), 45-55 (4), 55-65 (4), 65-75 (2), 75-85 (1). Total states = 35.",
                    "solution": "Let class intervals be the percentage ranges, and frequencies 'fi' be the number of states.\nTotal frequency Σ fi = 35.\nClass width h = 25 - 15 = 10.\n\nStep 1: Compute Class Marks (xi) and choose Assumed Mean 'a':\nInterval 15-25: x1 = (15+25)/2 = 20, f1 = 6\nInterval 25-35: x2 = (25+35)/2 = 30, f2 = 11\nInterval 35-45: x3 = (35+45)/2 = 40, f3 = 7\nInterval 45-55: x4 = (45+55)/2 = 50, f4 = 4  <-- Choose a = 50\nInterval 55-65: x5 = (55+65)/2 = 60, f5 = 4\nInterval 65-75: x6 = (65+75)/2 = 70, f6 = 2\nInterval 75-85: x7 = (75+85)/2 = 80, f7 = 1\n\nStep 2: Step-Deviation Table (ui = (xi - 50) / 10):\nx1 = 20: u1 = -3, f1·u1 = 6 × (-3) = -18\nx2 = 30: u2 = -2, f2·u2 = 11 × (-2) = -22\nx3 = 40: u3 = -1, f3·u3 = 7 × (-1) = -7\nx4 = 50: u4 = 0,  f4·u4 = 4 × 0 = 0\nx5 = 60: u5 = 1,  f5·u5 = 4 × 1 = 4\nx6 = 70: u6 = 2,  f6·u6 = 2 × 2 = 4\nx7 = 80: u7 = 3,  f7·u7 = 1 × 3 = 3\n\nStep 3: Calculate Σ fi·ui:\nNegative sum = -18 - 22 - 7 = -47\nPositive sum = 4 + 4 + 3 = +11\nΣ fi·ui = -47 + 11 = -36.\n\nStep 4: Compute Mean using Step-Deviation Formula:\nx̄ = a + [ ( Σ fi·ui ) / ( Σ fi ) ] × h\n= 50 + [ (-36) / 35 ] × 10\n= 50 - 360 / 35\n= 50 - 10.2857 ≈ 39.71%.\n[ROUGH_WORK]\nDirect method check: Σ fi·xi = 120 + 330 + 280 + 200 + 240 + 140 + 80 = 1390.\nx̄ = 1390 / 35 = 39.714% (Exact match!).\nBoxed Answer: [ Mean percentage of female teachers = 39.71% ].",
                    "concept_questions": [
                        "Why does step-deviation make calculation faster than direct multiplication?",
                        "What is the value of Σ fi·di in the assumed mean method? (-36 × 10 = -360)"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Mean Computation Methods HUD",
                "diagram_type": "diagram",
                "svg": svg_histogram,
                "concept_visuals": [
                    {
                        "concept_title": "Step-Deviation Transformation",
                        "diagram_title": "Class Mark Deviation Matrix",
                        "svg": svg_histogram,
                        "diagram_type": "diagram",
                        "what_to_make": "Table layout showing transformation from xi to di to ui",
                        "what_to_explain": "Arithmetic compression: ui = (xi - a)/h"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting to multiply by 'h' in the step-deviation formula: x̄ = a + (Σfi·ui / Σfi) × h, forgetting 'h' yields an answer around 49 instead of 39.71!",
                "Taking class limits instead of class marks in the direct method."
            ]
        },

        # Module 2: Mode of Grouped Data
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 2,
            "title": "Mode of Grouped Data: Modal Class Identification & Interpolation Formula",
            "estimated_minutes": 25,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the concept of Mode as the most frequently occurring value. In grouped data, learn how to identify the Modal Class (class interval having the maximum frequency) and interpolate the exact modal value within that class using the landmark board formula: Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h.",
            "key_concepts": [
                "Modal Class: The class interval having the highest frequency in the distribution",
                "Interpolation Formula: Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h",
                "Variable Definitions: l = lower limit of modal class, h = class size, f1 = frequency of modal class, f0 = frequency of preceding class, f2 = frequency of succeeding class",
                "Denominator Identity: 2f1 - f0 - f2 = (f1 - f0) + (f1 - f2) (Sum of the frequency drop-offs on either side of the peak!)",
                "Boundary Constraint: The calculated mode MUST lie strictly within the modal class interval [l, l + h]!"
            ],
            "subtopics": [
                "Locating the modal class in grouped distributions",
                "Physical meaning of (f1 - f0) and (f1 - f2) as directional pull on the mode",
                "Worked Example 4 and Example 5 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Example 5 (NCERT): A survey conducted on 20 households in a locality by a group of students resulted in the following frequency table for the number of family members in a household:\nFamily size: 1-3 (7), 3-5 (8), 5-7 (2), 7-9 (2), 9-11 (1).\nFind the mode of this data.",
                    "solution": "Given distribution:\nClass intervals: 1-3, 3-5, 5-7, 7-9, 9-11\nFrequencies: 7, 8, 2, 2, 1.\n\nStep 1: Identify the Modal Class:\nThe maximum frequency is 8, which corresponds to the class interval 3-5.\nTherefore, Modal Class = 3 - 5.\n\nStep 2: Extract variables for the mode formula:\nLower limit of modal class l = 3\nClass size h = 5 - 3 = 2\nFrequency of modal class f1 = 8\nFrequency of preceding class f0 = 7 (for class 1-3)\nFrequency of succeeding class f2 = 2 (for class 5-7).\n\nStep 3: Apply Mode Interpolation Formula:\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nSubstitute values:\nMode = 3 + [ (8 - 7) / (2(8) - 7 - 2) ] × 2\n= 3 + [ 1 / (16 - 9) ] × 2\n= 3 + [ 1 / 7 ] × 2\n= 3 + 2 / 7\n= 3 + 0.286 = 3.286.\n\nStep 4: Sanity Check:\n3.286 lies inside the modal class 3-5 (Valid!).\n[ROUGH_WORK]\n2 / 7 = 0.2857...\n3 + 0.286 = 3.286 family members.\nBoxed Answer: [ Mode of the data = 3.286 (or 23/7) ].",
                    "concept_questions": [
                        "Why does the mode shift towards 3 rather than 5? (Because f0 = 7 is much closer to 8 than f2 = 2)",
                        "What is the frequency of the modal class?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Histogram Peak and Modal Class HUD",
                "diagram_type": "diagram",
                "svg": svg_histogram,
                "concept_visuals": [
                    {
                        "concept_title": "Modal Class Peak Geometry",
                        "diagram_title": "Histogram Mode Model",
                        "svg": svg_histogram,
                        "diagram_type": "diagram",
                        "what_to_make": "Histogram with highest bar labeled f1 and neighboring bars f0 and f2",
                        "what_to_explain": "Mode interpolation: Mode = l + [(f1-f0)/(2f1-f0-f2)]h"
                    }
                ]
            },
            "common_misconceptions": [
                "Writing 2f1 as f1²: 2f1 is two TIMES f1 (e.g. 2 × 8 = 16), not 8² = 64!",
                "Selecting the modal class based on class mark instead of highest frequency."
            ]
        },

        # Module 3: Median of Grouped Data & Empirical Relation
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 3,
            "title": "Median of Grouped Data: Cumulative Frequencies, Median Class & Empirical Relation",
            "estimated_minutes": 30,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Understand the Median as the middle-most positional measure of central tendency. Construct cumulative frequency distributions (cf), locate the Median Class (where cf ≥ N/2), and apply the median formula: Median = l + [ (N/2 - cf) / f ] × h. Master the classical empirical relationship: 3 Median = Mode + 2 Mean.",
            "key_concepts": [
                "Cumulative Frequency (cf): The running cumulative sum of frequencies up to the upper limit of each class",
                "Median Class: The class interval whose cumulative frequency is greater than (and nearest to) N/2, where N = Σ fi",
                "Median Formula: Median = l + [ (N/2 - cf) / f ] × h",
                "Variable Definitions: l = lower limit of median class, N = total frequency, cf = cumulative frequency of PRECEDING class, f = simple frequency of median class, h = class width",
                "The Empirical Relationship: 3 Median = Mode + 2 Mean (Allows finding any third measure given the other two!)",
                "Ogive Intersection: The x-coordinate of the intersection point of 'less-than' and 'more-than' ogives gives the exact median"
            ],
            "subtopics": [
                "Constructing cumulative frequency tables",
                "Preceding cf vs simple f distinction",
                "Empirical relationship calculations: Mode = 3 Median - 2 Mean",
                "Worked Example 7 and Example 8 from NCERT"
            ],
            "worked_examples": [
                {
                    "problem": "Example 7 (NCERT): A survey regarding the heights (in cm) of 51 girls of Class X of a school was conducted and the following data was obtained:\nHeight: Less than 140 (4), Less than 145 (11), Less than 150 (29), Less than 155 (40), Less than 160 (46), Less than 165 (51).\nFind the median height.",
                    "solution": "Given: 'Less than' cumulative frequency distribution with total girls N = 51.\n\nStep 1: Convert into Continuous Class Intervals and calculate simple frequencies 'fi':\nInterval 135-140: f1 = 4,   cf = 4\nInterval 140-145: f2 = 11 - 4 = 7,  cf = 11\nInterval 145-150: f3 = 29 - 11 = 18, cf = 29\nInterval 150-155: f4 = 40 - 29 = 11, cf = 40\nInterval 155-160: f5 = 46 - 40 = 6,  cf = 46\nInterval 160-165: f6 = 51 - 46 = 5,  cf = 51.\n\nStep 2: Find N/2 and locate the Median Class:\nN = 51 ⇒ N / 2 = 51 / 2 = 25.5.\nThe cumulative frequency just greater than 25.5 is 29, which corresponds to the class 145 - 150.\nTherefore, Median Class = 145 - 150.\n\nStep 3: Extract parameters for Median Formula:\nLower limit of median class l = 145\nClass size h = 150 - 145 = 5\nCumulative frequency of preceding class cf = 11 (from 140-145)\nSimple frequency of median class f = 18.\n\nStep 4: Apply Median Formula:\nMedian = l + [ (N/2 - cf) / f ] × h\nSubstitute values:\nMedian = 145 + [ (25.5 - 11) / 18 ] × 5\n= 145 + [ 14.5 / 18 ] × 5\n= 145 + 72.5 / 18\n= 145 + 4.028 = 149.03 cm.\n\nStep 5: Sanity Check:\n149.03 cm lies strictly within the median class 145 - 150 (Valid!).\n[ROUGH_WORK]\n72.5 / 18 = 4.0277... ≈ 4.03 cm.\n145 + 4.03 = 149.03 cm.\nBoxed Answer: [ Median height = 149.03 cm ].",
                    "concept_questions": [
                        "Why must cf be taken from the class preceding the median class?",
                        "What is the median class when N/2 = 25.5?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Dual Ogives Median Intersection HUD",
                "diagram_type": "diagram",
                "svg": svg_ogives,
                "concept_visuals": [
                    {
                        "concept_title": "Ogive Intersection at Median",
                        "diagram_title": "Dual Ogive Curves",
                        "svg": svg_ogives,
                        "diagram_type": "diagram",
                        "what_to_make": "Less-than and more-than ogives intersecting at (Median, N/2)",
                        "what_to_explain": "Direct graphical determination of median without interpolation formula"
                    }
                ]
            },
            "common_misconceptions": [
                "Using the cf of the median class itself (29) instead of the preceding class (11): The formula specifically requires cf of the PRECEDING class!",
                "Using cumulative frequencies as simple frequencies in calculations: 'Less than' tables already contain cf; you must subtract adjacent rows to get fi."
            ]
        },

        # Module 4: NCERT Exercise 13.1 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 4,
            "title": "Exercise 13.1 Complete Solver: Grouped Mean Across 9 Practical Scenarios (Q1 to Q9)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 13.1 Questions 1 through 9. Covers plants in 20 houses (Q1), daily wages of 50 workers (Q2), missing pocket-money frequency 'f' with mean ₹18 (Q3), heartbeats of 30 women (Q4), packaging boxes with unequal class intervals (Q5), daily food expenditure of 25 households (Q6), SO2 concentration in 30 localities (Q7), student absenteeism days (Q8), and literacy rates of 35 cities (Q9).",
            "key_concepts": [
                "Ex 13.1 Q1: Houses & plants: Direct method x̄ = 162 / 20 = 8.1 plants",
                "Ex 13.1 Q2: 50 workers wages: Assumed mean a = 550, h = 20 ⇒ x̄ = 550 - 240/50 = ₹545.20",
                "Ex 13.1 Q3: Missing frequency: Given x̄ = 18; Σ fi = 44 + f; Σ fi·xi = 752 + 20f ⇒ 18(44 + f) = 752 + 20f ⇒ 792 + 18f = 752 + 20f ⇒ 2f = 40 ⇒ f = 20!",
                "Ex 13.1 Q4: 30 women heartbeats: x̄ = 75.9 beats/min",
                "Ex 13.1 Q5: Mango boxes (continuous adjustment 49.5-52.5 etc.): x̄ = 57.19 mangoes",
                "Ex 13.1 Q6: Daily food expenditure: a = 225, h = 50 ⇒ x̄ = ₹211",
                "Ex 13.1 Q7: SO2 ppm concentration: x̄ = 0.099 ppm",
                "Ex 13.1 Q8: Absenteeism (unequal intervals 0-6, 6-10, 10-14...): Direct method x̄ = 499 / 40 = 12.48 days",
                "Ex 13.1 Q9: 35 cities literacy rate: a = 70, h = 10 ⇒ x̄ = 69.43%"
            ],
            "subtopics": [
                "Full resolution of Exercise 13.1 Questions 1 to 9",
                "Solving for missing frequency 'f' given mean",
                "Handling non-uniform class widths in Q8"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 13.1 Q3: The following distribution shows the daily pocket allowance of children of a locality. The mean pocket allowance is ₹ 18. Find the missing frequency f.\nDaily allowance (in ₹): 11-13 (7), 13-15 (6), 15-17 (9), 17-19 (13), 19-21 (f), 21-23 (5), 23-25 (4).",
                    "solution": "Given: Mean pocket allowance x̄ = ₹ 18.\nLet us construct the table with Class Marks xi and deviations di = xi - 18:\n\nInterval 11-13: x1 = 12, f1 = 7,  d1 = 12 - 18 = -6, f1·d1 = 7 × (-6) = -42\nInterval 13-15: x2 = 14, f2 = 6,  d2 = 14 - 18 = -4, f2·d2 = 6 × (-4) = -24\nInterval 15-17: x3 = 16, f3 = 9,  d3 = 16 - 18 = -2, f3·d3 = 9 × (-2) = -18\nInterval 17-19: x4 = 18, f4 = 13, d4 = 18 - 18 = 0,  f4·d4 = 13 × 0 = 0\nInterval 19-21: x5 = 20, f5 = f,  d5 = 20 - 18 = +2, f5·d5 = f × (+2) = 2f\nInterval 21-23: x6 = 22, f6 = 5,  d6 = 22 - 18 = +4, f6·d6 = 5 × (+4) = +20\nInterval 23-25: x7 = 24, f7 = 4,  d7 = 24 - 18 = +6, f7·d7 = 4 × (+6) = +24\n\nStep 1: Compute Total Frequency Σ fi:\nΣ fi = 7 + 6 + 9 + 13 + f + 5 + 4 = 44 + f.\n\nStep 2: Compute Total Deviations Σ fi·di:\nSum of negative terms = -42 - 24 - 18 = -84\nSum of positive constant terms = +20 + 24 = +44\nNet sum = -84 + 44 + 2f = 2f - 40.\n\nStep 3: Apply Assumed Mean Formula (with a = 18):\nx̄ = a + ( Σ fi·di ) / ( Σ fi )\nSubstitute x̄ = 18, a = 18:\n18 = 18 + ( 2f - 40 ) / ( 44 + f )\nSubtract 18 from both sides:\n0 = ( 2f - 40 ) / ( 44 + f )\n\nStep 4: Solve for f:\nSince 44 + f ≠ 0:\n2f - 40 = 0\n2f = 40\nf = 40 / 2 = 20!\n[ROUGH_WORK]\nBy choosing the assumed mean 'a' to equal the given mean 18, the deviation sum must be identically zero! 2f - 40 = 0 ⇒ f = 20. Lightning fast!\nBoxed Answer: [ Missing frequency f = 20 ].",
                    "concept_questions": [
                        "Why does setting a = 18 reduce the equation to 2f - 40 = 0 instantly?",
                        "What is the total number of children when f = 20? (44 + 20 = 64)"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Missing Frequency Equation HUD",
                "diagram_type": "diagram",
                "svg": svg_histogram,
                "concept_visuals": [
                    {
                        "concept_title": "Mean Balancing Framework",
                        "diagram_title": "Deviation Equilibrium Model",
                        "svg": svg_histogram,
                        "diagram_type": "diagram",
                        "what_to_make": "Deviation balance beam showing positive and negative sums balancing at x̄ = 18",
                        "what_to_explain": "Equating Σ fi·di = 0 when a = x̄"
                    }
                ]
            },
            "common_misconceptions": [
                "Adding 'f' to the numbers and writing Σ fi = 44f: 'f' is an unknown variable, so the sum is 44 + f, NOT 44f!",
                "Assuming class sizes must always be equal: In Q8, class sizes vary (6, 4, 4, 6, 8, 10, 2), so step-deviation CANNOT be used with a single 'h'; direct method must be used."
            ]
        },

        # Module 5: NCERT Exercise 13.2 Complete Solver
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 5,
            "title": "Exercise 13.2 Complete Solver: Grouped Mode & Comparative Mean Analysis (Q1 to Q6)",
            "estimated_minutes": 35,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 13.2 Questions 1 through 6. Covers hospital patient age mode vs mean (Q1), electrical component lifetimes (Q2), household expenditures (Q3), teacher-student ratios (Q4), runs scored by world batsmen (Q5), and passing car counts (Q6). Interpret why Mode and Mean differ.",
            "key_concepts": [
                "Ex 13.2 Q1: Hospital patient ages: Modal class 35-45 (f1 = 23, f0 = 21, f2 = 14) ⇒ Mode = 36.8 years, Mean = 35.37 years",
                "Ex 13.2 Q2: 225 electrical components: Modal class 60-80 (f1 = 61, f0 = 52, f2 = 38) ⇒ Mode = 60 + [9 / (122 - 90)] × 20 = 65.625 hours",
                "Ex 13.2 Q3: Monthly expenditure: Modal class 1500-2000 (f1 = 40, f0 = 24, f2 = 33) ⇒ Mode = ₹1847.83, Mean = ₹2662.50",
                "Ex 13.2 Q4: State teacher-student ratio: Modal class 30-35 (f1 = 10, f0 = 9, f2 = 3) ⇒ Mode = 30.6, Mean = 29.2",
                "Ex 13.2 Q5: World batsmen runs: Modal class 4000-5000 (f1 = 18, f0 = 4, f2 = 9) ⇒ Mode = 4608.7 runs",
                "Ex 13.2 Q6: Passing cars: Modal class 40-50 (f1 = 20, f0 = 12, f2 = 11) ⇒ Mode = 44.7 cars"
            ],
            "subtopics": [
                "Full resolution of Exercise 13.2 Questions 1 to 6",
                "Comparing central tendencies: Mode (most frequent) vs Mean (average balance)",
                "Precise decimal rounding for modal values"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 13.2 Q2: The following data gives the information on the observed lifetimes (in hours) of 225 electrical components:\nLifetimes (in hours): 0-20 (10), 20-40 (35), 40-60 (52), 60-80 (61), 80-100 (38), 100-120 (29).\nDetermine the modal lifetimes of the components.",
                    "solution": "Given:\nTotal components N = 225.\n\nStep 1: Identify the Modal Class:\nThe maximum frequency in the table is 61, which belongs to the class interval 60 - 80.\nTherefore, Modal Class = 60 - 80.\n\nStep 2: Identify variables for Mode formula:\nLower limit of modal class l = 60\nClass size h = 80 - 60 = 20\nFrequency of modal class f1 = 61\nFrequency of preceding class f0 = 52 (for class 40-60)\nFrequency of succeeding class f2 = 38 (for class 80-100).\n\nStep 3: Apply the Mode Formula:\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nSubstitute values:\nMode = 60 + [ (61 - 52) / (2(61) - 52 - 38) ] × 20\n= 60 + [ 9 / (122 - 90) ] × 20\n= 60 + [ 9 / 32 ] × 20\n= 60 + (180 / 32)\nDivide 180 by 32 (or divide numerator and denominator by 4: 45 / 8):\n45 / 8 = 5.625.\nMode = 60 + 5.625 = 65.625 hours.\n\nStep 4: Sanity Check:\n65.625 hours lies strictly inside the modal class 60-80 (Valid!).\n[ROUGH_WORK]\n2 × 61 = 122.\n52 + 38 = 90.\n122 - 90 = 32.\n9 × 20 = 180.\n180 / 32 = 5.625.\nBoxed Answer: [ Modal lifetime of components = 65.625 hours ].",
                    "concept_questions": [
                        "What does 65.625 hours represent in engineering terms? (The single most common lifetime period for the components)",
                        "Why does the mode lie closer to 60 than 80? (Because f0 = 52 is much larger than f2 = 38)"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Exercise 13.2 Modal Lifetime HUD",
                "diagram_type": "diagram",
                "svg": svg_histogram,
                "concept_visuals": [
                    {
                        "concept_title": "Modal Frequency Interpolation",
                        "diagram_title": "Peak Distribution Model",
                        "svg": svg_histogram,
                        "diagram_type": "diagram",
                        "what_to_make": "Histogram of component lifetimes highlighting 60-80 peak",
                        "what_to_explain": "Interpolation between 52, 61, and 38 yielding 65.625"
                    }
                ]
            },
            "common_misconceptions": [
                "Subtracting f0 and f2 from f1 instead of 2f1: The denominator is 2f1 - f0 - f2!",
                "Forgetting to multiply the bracket by class size h = 20."
            ]
        },

        # Module 6: NCERT Exercise 13.3 Complete Solver & Missing Frequencies
        {
            "curriculum_id": CURRICULUM_ID,
            "order_index": 6,
            "title": "Exercise 13.3 Complete Solver: Dual Missing Frequencies (x, y) & Cumulative Ogives (Q1 to Q7)",
            "estimated_minutes": 40,
            "class_level": "Class 10",
            "board": "CBSE",
            "description": "Complete step-by-step resolution of NCERT Exercise 13.3 Questions 1 through 7. Master the celebrated board exam dual missing frequency problem where Median = 28.5 and N = 60 to find x = 8 and y = 7 (Q2), converting cumulative life insurance policies to continuous intervals (Q3), continuous class limit conversions with 0.5 adjustments (Q4), neon lamp median lifetime (Q5), surname letters mean/median/mode comparison (Q6), and student weights (Q7).",
            "key_concepts": [
                "Ex 13.3 Q1: 68 consumers electricity: Median = 137 units, Mean = 137.05 units, Mode = 135.76 units",
                "Ex 13.3 Q2: Landmark Missing Frequencies x and y: Total N = 60, Median = 28.5 (lies in 20-30). Equation 1: 45 + x + y = 60 ⇒ x + y = 15; Equation 2 from median formula: 28.5 = 20 + [(30 - (5 + x)) / 20] × 10 ⇒ x = 8 ⇒ y = 7!",
                "Ex 13.3 Q3: Life insurance 'Below 20, 25...' conversion to 18-20, 20-25...: Median = 35.76 years",
                "Ex 13.3 Q4: Leaf lengths (discrete 118-126, 127-135 continuous adjustment to 117.5-126.5...): Median = 146.75 mm",
                "Ex 13.3 Q5: 400 neon lamps: Median = 3406.98 hours",
                "Ex 13.3 Q6: 100 surnames: Median = 8.05 letters, Mean = 8.32 letters, Mode = 7.88 letters",
                "Ex 13.3 Q7: 30 students weight: Median = 56.67 kg",
                "Empirical Check: 3 Median = Mode + 2 Mean holds across all distributions"
            ],
            "subtopics": [
                "Full resolution of Exercise 13.3 Questions 1 to 7",
                "The dual missing frequency algebraic system (x + y = 15)",
                "Boundary continuity correction: Subtracting 0.5 from lower and adding 0.5 to upper limit"
            ],
            "worked_examples": [
                {
                    "problem": "Exercise 13.3 Q2: If the median of the distribution given below is 28.5, find the values of x and y.\nClass interval: 0-10 (5), 10-20 (x), 20-30 (20), 30-40 (15), 40-50 (y), 50-60 (5). Total frequency = 60.",
                    "solution": "Given:\nMedian = 28.5\nTotal frequency N = 60.\n\nStep 1: Construct the Cumulative Frequency (cf) Table:\nInterval 0-10:   f = 5,   cf = 5\nInterval 10-20:  f = x,   cf = 5 + x\nInterval 20-30:  f = 20,  cf = 25 + x  <-- Median Class\nInterval 30-40:  f = 15,  cf = 40 + x\nInterval 40-50:  f = y,   cf = 40 + x + y\nInterval 50-60:  f = 5,   cf = 45 + x + y.\n\nStep 2: Form Equation (1) from total frequency:\nTotal frequency = 45 + x + y = 60\nx + y = 60 - 45\nx + y = 15 ... (1)\n\nStep 3: Identify the Median Class:\nSince the median is given as 28.5, it lies strictly in the class interval 20 - 30!\nTherefore, Median Class = 20 - 30.\n\nStep 4: Extract parameters for Median Formula:\nLower limit l = 20\nClass size h = 10\nTotal frequency N = 60 ⇒ N / 2 = 30\nCumulative frequency of preceding class cf = 5 + x (from 10-20)\nSimple frequency of median class f = 20.\n\nStep 5: Apply Median Formula:\nMedian = l + [ (N/2 - cf) / f ] × h\nSubstitute values:\n28.5 = 20 + [ (30 - (5 + x)) / 20 ] × 10\nSubtract 20 from both sides:\n8.5 = [ (30 - 5 - x) / 20 ] × 10\n8.5 = (25 - x) / 2\nMultiply both sides by 2:\n17 = 25 - x\nx = 25 - 17 = 8.\n\nStep 6: Find y from Equation (1):\nx + y = 15\n8 + y = 15 ⇒ y = 15 - 8 = 7.\n[ROUGH_WORK]\nCheck total: 5 + 8 + 20 + 15 + 7 + 5 = 60 (Verified!).\nCheck median: 20 + [(30 - 13)/20] × 10 = 20 + (17/2) = 20 + 8.5 = 28.5 (Verified!).\nBoxed Answer: [ x = 8, y = 7 ].",
                    "concept_questions": [
                        "Why did we use Median = 28.5 to identify the median class instead of N/2 = 30? (Because cf contains unknown x, but 28.5 directly tells us the interval is 20-30!)",
                        "What is the value of x + y?"
                    ]
                }
            ],
            "visual_lesson_plan": {
                "diagram_title": "Missing Frequency and Ogives Master HUD",
                "diagram_type": "diagram",
                "svg": svg_ogives,
                "concept_visuals": [
                    {
                        "concept_title": "Median Class Positional Identification",
                        "diagram_title": "Cumulative Frequency Distribution",
                        "svg": svg_ogives,
                        "diagram_type": "diagram",
                        "what_to_make": "Dual ogive chart with point (28.5, 30) highlighted",
                        "what_to_explain": "Solving simultaneous equations x + y = 15 and median formula for x = 8, y = 7"
                    }
                ]
            },
            "common_misconceptions": [
                "Forgetting the brackets around (5 + x) when writing 30 - cf: Writing 30 - 5 + x gives 25 + x, which produces a negative value for x! It MUST be 30 - (5 + x) = 25 - x!",
                "Looking for N/2 = 30 in cf to find the median class: Since cf has variable x, you cannot locate 30 directly; you must look at the known median value 28.5."
            ]
        }
    ]
    
    return modules
