"""
Complete Synthesis of Class 10 Mathematics Chapter 13: Statistics
Curriculum ID: ee79fe72-f746-45c7-a36e-b5a11c82d479
100% NCERT Question & Example Coverage:
- Examples: 1, 2, 3, 4, 5, 6, 7, 8
- Exercise 13.1: Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9
- Exercise 13.2: Q1, Q2, Q3, Q4, Q5, Q6
- Exercise 13.3: Q1, Q2, Q3, Q4, Q5, Q6, Q7
All solved in Authentic Board Topper Layout: Given -> To Find/Prove -> Formula -> Step-by-Step -> [ROUGH_WORK] -> Boxed Answer.
Includes Page References, Section References, concise 2-5 word image_search_queries, and High-Precision Vector SVGs.
"""

import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "maths_class10_generators"))
from svg_builder_class10 import build_statistics_chart_svg

def get_ch13_complete_modules():
    CURRICULUM_ID = "ee79fe72-f746-45c7-a36e-b5a11c82d479"

    svg_ogive = build_statistics_chart_svg(
        chart_type="ogive",
        title="Cumulative Frequency Curves (Ogives) & Median Determination",
        caption="Intersection of Less-than & More-than Ogives gives Median on X-axis (N/2 = 50)"
    )

    svg_histogram = build_statistics_chart_svg(
        chart_type="histogram_mode",
        title="Grouped Frequency Histogram: Modal Class Identification",
        caption="Modal Class with maximum frequency fm, flanked by f1 and f2 for interpolation"
    )

    m1_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 174] Example 1: The marks obtained by 30 students of Class X of a certain school in a Mathematics paper consisting of 100 marks are presented in Table 13.1. Find the mean of the marks obtained by the students using the Direct Method (Grouped data: 10-25: 2; 25-40: 3; 40-55: 7; 55-70: 6; 70-85: 6; 85-100: 6).",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 174,
            "image_search_query": "mean grouped data direct method formula table",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Frequency distribution of marks of 30 students:\nClass 10-25: f1 = 2\nClass 25-40: f2 = 3\nClass 40-55: f3 = 7\nClass 55-70: f4 = 6\nClass 70-85: f5 = 6\nClass 85-100: f6 = 6\nTotal frequency Σfi = 30.",
            "formula": "Direct Method: Mean x̄ = (Σ fi xi) / (Σ fi), where class mark xi = (Upper limit + Lower limit) / 2.",
            "substitution": "Class marks xi:\n10-25: 17.5 ⇒ f1 x1 = 2 × 17.5 = 35.0\n25-40: 32.5 ⇒ f2 x2 = 3 × 32.5 = 97.5\n40-55: 47.5 ⇒ f3 x3 = 7 × 47.5 = 332.5\n55-70: 62.5 ⇒ f4 x4 = 6 × 62.5 = 375.0\n70-85: 77.5 ⇒ f5 x5 = 6 × 77.5 = 465.0\n85-100: 92.5 ⇒ f6 x6 = 6 × 92.5 = 555.0\nΣ fi xi = 35 + 97.5 + 332.5 + 375 + 465 + 555 = 1860.0.",
            "calculation": "Mean x̄ = 1860 / 30 = 62.",
            "finalAnswer": "62",
            "unit": "marks",
            "solution": "GIVEN:\nDistribution of marks obtained by 30 students:\n- 10-25: 2 students\n- 25-40: 3 students\n- 40-55: 7 students\n- 55-70: 6 students\n- 70-85: 6 students\n- 85-100: 6 students\nTotal students, Σfi = 30.\n\nTO FIND:\nMean marks of the students using the Direct Method.\n\nFORMULA USED:\nDirect Method for Mean:\nMean (x̄) = Σ(fi × xi) / Σfi\nwhere xi = (Lower limit + Upper limit) / 2 is the class mark.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class mark (xi) and product (fi × xi) for each interval:\n1. 10 - 25: xi = (10 + 25) / 2 = 17.5; fi = 2; fi × xi = 2 × 17.5 = 35.0\n2. 25 - 40: xi = (25 + 40) / 2 = 32.5; fi = 3; fi × xi = 3 × 32.5 = 97.5\n3. 40 - 55: xi = (40 + 55) / 2 = 47.5; fi = 7; fi × xi = 7 × 47.5 = 332.5\n4. 55 - 70: xi = (55 + 70) / 2 = 62.5; fi = 6; fi × xi = 6 × 62.5 = 375.0\n5. 70 - 85: xi = (70 + 85) / 2 = 77.5; fi = 6; fi × xi = 6 × 77.5 = 465.0\n6. 85 - 100: xi = (85 + 100) / 2 = 92.5; fi = 6; fi × xi = 6 × 92.5 = 555.0\n\nStep 2: Sum the products:\nΣ(fi × xi) = 35.0 + 97.5 + 332.5 + 375.0 + 465.0 + 555.0 = 1860.0\nΣfi = 30.\n\nStep 3: Calculate Mean:\nx̄ = 1860 / 30 = 62.\n\n[ROUGH_WORK]\nSum = 35 + 97.5 + 332.5 + 375 + 465 + 555 = 1860. 1860 / 30 = 62. Exact integer mean.\nBoxed Answer: [ 62 marks ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 178] Example 2: The table below gives the percentage distribution of female teachers in primary schools of rural areas of various states and union territories (UT) of India. Find the mean percentage of female teachers using the Step-Deviation Method (15-25: 6; 25-35: 11; 35-45: 7; 45-55: 4; 55-65: 4; 65-75: 2; 75-85: 1).",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 178,
            "image_search_query": "step deviation method mean formula grouped data",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Percentage of female teachers across 35 States/UTs:\n15-25: 6; 25-35: 11; 35-45: 7; 45-55: 4; 55-65: 4; 65-75: 2; 75-85: 1.\nTotal frequency Σfi = 35.",
            "formula": "Step-Deviation Method: Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)], where a is assumed mean, h is class size, and ui = (xi - a) / h.",
            "substitution": "Class width h = 10. Class marks xi: 20, 30, 40, 50, 60, 70, 80. Choose assumed mean a = 50.\nui = (xi - 50) / 10:\n20: ui = -3 ⇒ fi ui = 6 × (-3) = -18\n30: ui = -2 ⇒ fi ui = 11 × (-2) = -22\n40: ui = -1 ⇒ fi ui = 7 × (-1) = -7\n50: ui = 0 ⇒ fi ui = 4 × 0 = 0\n60: ui = 1 ⇒ fi ui = 4 × 1 = 4\n70: ui = 2 ⇒ fi ui = 2 × 2 = 4\n80: ui = 3 ⇒ fi ui = 1 × 3 = 3\nΣ fi ui = (-18 - 22 - 7) + (0 + 4 + 4 + 3) = -47 + 11 = -36.",
            "calculation": "x̄ = 50 + 10 × (-36 / 35) = 50 - 360 / 35 = 50 - 10.29 = 39.71%.",
            "finalAnswer": "39.71%",
            "unit": "%",
            "solution": "GIVEN:\nDistribution of female teachers across 35 States and Union Territories:\n- 15 - 25: 6\n- 25 - 35: 11\n- 35 - 45: 7\n- 45 - 55: 4\n- 55 - 65: 4\n- 65 - 75: 2\n- 75 - 85: 1\nTotal frequency, Σfi = 35.\n\nTO FIND:\nMean percentage of female teachers using the Step-Deviation Method.\n\nFORMULA USED:\nMean (x̄) = a + h × [ Σ(fi × ui) / Σfi ]\nwhere:\n- a = assumed mean (chosen central class mark = 50)\n- h = class size = 10\n- ui = (xi - a) / h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), step-deviations (ui), and products (fi × ui):\n- 15-25: xi = 20; ui = (20 - 50)/10 = -3; fi = 6; fi × ui = 6 × (-3) = -18\n- 25-35: xi = 30; ui = (30 - 50)/10 = -2; fi = 11; fi × ui = 11 × (-2) = -22\n- 35-45: xi = 40; ui = (40 - 50)/10 = -1; fi = 7; fi × ui = 7 × (-1) = -7\n- 45-55: xi = 50; ui = (50 - 50)/10 = 0; fi = 4; fi × ui = 4 × 0 = 0\n- 55-65: xi = 60; ui = (60 - 50)/10 = 1; fi = 4; fi × ui = 4 × 1 = 4\n- 65-75: xi = 70; ui = (70 - 50)/10 = 2; fi = 2; fi × ui = 2 × 2 = 4\n- 75-85: xi = 80; ui = (80 - 50)/10 = 3; fi = 1; fi × ui = 1 × 3 = 3\n\nStep 2: Sum the values:\nNegative sum = -18 - 22 - 7 = -47\nPositive sum = 4 + 4 + 3 = 11\nΣ(fi × ui) = -47 + 11 = -36\nΣfi = 35.\n\nStep 3: Calculate the mean:\nx̄ = a + h × [ Σ(fi × ui) / Σfi ]\nx̄ = 50 + 10 × [ -36 / 35 ]\nx̄ = 50 - (360 / 35) = 50 - 10.2857... ≈ 39.71%.\n\n[ROUGH_WORK]\n50 - 72/7 = 50 - 10.286 = 39.714%.\nBoxed Answer: [ 39.71% ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 180] Example 3: The distribution below shows the number of wickets taken by bowlers in one-day cricket matches. Find the mean number of wickets. What does the mean signify? (Wickets: 20-60: 7; 60-100: 5; 100-150: 16; 150-250: 12; 250-350: 2; 350-450: 3).",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 180,
            "image_search_query": "mean wickets unequal class intervals assumed mean",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Unequal class intervals of wickets taken by 45 bowlers:\n20-60: 7; 60-100: 5; 100-150: 16; 150-250: 12; 250-350: 2; 350-450: 3.\nTotal frequency Σfi = 45.",
            "formula": "Assumed Mean Method: Mean x̄ = a + (Σ fi di) / (Σ fi), where di = xi - a (since class widths vary, step deviation with uniform h cannot be directly used).",
            "substitution": "Class marks xi:\n20-60: 40 ⇒ di = 40 - 200 = -160; fi di = 7 × (-160) = -1120\n60-100: 80 ⇒ di = 80 - 200 = -120; fi di = 5 × (-120) = -600\n100-150: 125 ⇒ di = 125 - 200 = -75; fi di = 16 × (-75) = -1200\n150-250: 200 ⇒ di = 0; fi di = 0\n250-350: 300 ⇒ di = 300 - 200 = 100; fi di = 2 × 100 = 200\n350-450: 400 ⇒ di = 400 - 200 = 200; fi di = 3 × 200 = 600\nΣ fi di = (-1120 - 600 - 1200) + (200 + 600) = -2920 + 800 = -2120.",
            "calculation": "x̄ = 200 + (-2120 / 45) = 200 - 47.11 = 152.89 wickets.",
            "finalAnswer": "152.89 wickets (Signifies on average a bowler took ~153 wickets)",
            "unit": "wickets",
            "solution": "GIVEN:\nDistribution of wickets taken by 45 bowlers across unequal class intervals:\n- 20 - 60: 7\n- 60 - 100: 5\n- 100 - 150: 16\n- 150 - 250: 12\n- 250 - 350: 2\n- 350 - 450: 3\nTotal bowlers, Σfi = 45.\n\nTO FIND:\n(i) Mean number of wickets taken.\n(ii) Significance of the mean.\n\nFORMULA USED:\nSince the class sizes vary (40, 40, 50, 100, 100, 100), we apply the Assumed Mean Method:\nMean (x̄) = a + [ Σ(fi × di) / Σfi ]\nwhere a = 200 (assumed mean) and di = xi - a.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Calculate class marks (xi), deviations (di = xi - 200), and products (fi × di):\n1. 20 - 60: xi = 40; di = -160; fi = 7; fi × di = -1120\n2. 60 - 100: xi = 80; di = -120; fi = 5; fi × di = -600\n3. 100 - 150: xi = 125; di = -75; fi = 16; fi × di = -1200\n4. 150 - 250: xi = 200; di = 0; fi = 12; fi × di = 0\n5. 250 - 350: xi = 300; di = 100; fi = 2; fi × di = 200\n6. 350 - 450: xi = 400; di = 200; fi = 3; fi × di = 600\n\nStep 2: Sum the deviations:\nΣ(fi × di) = -1120 - 600 - 1200 + 200 + 600 = -2920 + 800 = -2120\nΣfi = 45.\n\nStep 3: Compute the mean:\nx̄ = 200 + [ -2120 / 45 ]\nx̄ = 200 - 47.111... ≈ 152.89 wickets.\n\nStep 4: Significance:\nThe mean of 152.89 signifies that on average, a bowler has taken approximately 153 wickets across the recorded one-day cricket matches.\n\n[ROUGH_WORK]\n200 - 2120/45 = 200 - 424/9 = 200 - 47.11 = 152.89 wickets.\nBoxed Answer: [ 152.89 wickets ].",
            "concept_questions": []
        }
    ]

    m2_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 184] Example 4: The wickets taken by a bowler in 10 cricket matches are as follows: 2, 6, 4, 5, 0, 2, 1, 3, 2, 3. Find the mode of the data.",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 184,
            "image_search_query": "mode ungrouped data frequency count",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Wickets taken in 10 matches: 2, 6, 4, 5, 0, 2, 1, 3, 2, 3.",
            "formula": "Mode = Observation with the maximum frequency.",
            "substitution": "Frequencies:\n0 wickets: 1 match\n1 wicket: 1 match\n2 wickets: 3 matches\n3 wickets: 2 matches\n4 wickets: 1 match\n5 wickets: 1 match\n6 wickets: 1 match\nMaximum frequency is 3, corresponding to 2 wickets.",
            "calculation": "Mode = 2 wickets.",
            "finalAnswer": "2 wickets",
            "unit": "wickets",
            "solution": "GIVEN:\nNumber of wickets taken in 10 matches: 2, 6, 4, 5, 0, 2, 1, 3, 2, 3.\n\nTO FIND:\nMode of the given dataset.\n\nFORMULA USED:\nMode is the value among the observations that occurs most frequently, i.e., the value with the maximum frequency.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Construct the frequency distribution table:\n- 0 wickets: 1 time\n- 1 wicket: 1 time\n- 2 wickets: 3 times\n- 3 wickets: 2 times\n- 4 wickets: 1 time\n- 5 wickets: 1 time\n- 6 wickets: 1 time\n\nStep 2: Identify the maximum frequency:\nThe number 2 occurs 3 times, which is more frequent than any other number of wickets.\n\nConclusion:\nMode = 2 wickets.\n\n[ROUGH_WORK]\nCounts: {0:1, 1:1, 2:3, 3:2, 4:1, 5:1, 6:1}. Highest frequency = 3 for observation 2.\nBoxed Answer: [ 2 wickets ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 185] Example 5: A survey conducted on 20 households in a locality by a group of students resulted in the following frequency table for the number of family members in a household: 1-3: 7; 3-5: 8; 5-7: 2; 7-9: 2; 9-11: 1. Find the mode of this data.",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 185,
            "image_search_query": "mode grouped data formula calculation",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Family size distribution:\n1-3: 7; 3-5: 8; 5-7: 2; 7-9: 2; 9-11: 1.\nMaximum frequency = 8, corresponding to class interval 3-5 (Modal Class).",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nwhere:\n- l = lower limit of modal class = 3\n- h = class size = 2\n- f1 = frequency of modal class = 8\n- f0 = frequency of preceding class = 7\n- f2 = frequency of succeeding class = 2.",
            "substitution": "Mode = 3 + [ (8 - 7) / (2(8) - 7 - 2) ] × 2 = 3 + [ 1 / (16 - 9) ] × 2 = 3 + (2 / 7).",
            "calculation": "Mode = 3 + 0.286 = 3.286.",
            "finalAnswer": "3.286",
            "unit": "members",
            "solution": "GIVEN:\nFrequency table of family sizes in 20 households:\n- 1 - 3: 7\n- 3 - 5: 8\n- 5 - 7: 2\n- 7 - 9: 2\n- 9 - 11: 1\n\nTO FIND:\nMode of the family size distribution.\n\nFORMULA USED:\nMode of grouped data:\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nwhere:\n- Modal Class is the interval with highest frequency\n- l = lower limit of modal class\n- h = class width\n- f1 = frequency of modal class\n- f0 = frequency of preceding class\n- f2 = frequency of succeeding class\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Identify the modal class:\nThe maximum frequency is 8, which corresponds to the class interval 3 - 5.\nTherefore, Modal Class = 3 - 5.\n\nStep 2: Identify the parameters:\n- Lower limit, l = 3\n- Class width, h = 5 - 3 = 2\n- Frequency of modal class, f1 = 8\n- Frequency of preceding class (1 - 3), f0 = 7\n- Frequency of succeeding class (5 - 7), f2 = 2\n\nStep 3: Apply the mode formula:\nMode = 3 + [ (8 - 7) / (2 × 8 - 7 - 2) ] × 2\nMode = 3 + [ 1 / (16 - 9) ] × 2\nMode = 3 + [ 1 / 7 ] × 2\nMode = 3 + (2 / 7) = 3 + 0.2857... ≈ 3.286.\n\n[ROUGH_WORK]\nNumerator = 8 - 7 = 1. Denominator = 16 - 9 = 7. Ratio = 1/7. Times h(2) = 2/7 = 0.286. Mode = 3 + 0.286 = 3.286.\nBoxed Answer: [ 3.286 members ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 186] Example 6: The marks distribution of 30 students in a mathematics examination are given in Table 13.12 (10-25: 2; 25-40: 3; 40-55: 7; 55-70: 6; 70-85: 6; 85-100: 6). Find the mode of this data. Also compare and interpret the mode and the mean (Mean was found to be 62 in Example 1).",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 186,
            "image_search_query": "mode mean comparison interpretation grouped data",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Marks of 30 students:\n10-25: 2; 25-40: 3; 40-55: 7; 55-70: 6; 70-85: 6; 85-100: 6.\nMax frequency = 7 ⇒ Modal Class = 40-55. Mean = 62.",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nwhere l = 40, h = 15, f1 = 7, f0 = 3, f2 = 6.",
            "substitution": "Mode = 40 + [ (7 - 3) / (2(7) - 3 - 6) ] × 15 = 40 + [ 4 / (14 - 9) ] × 15 = 40 + [ 4 / 5 ] × 15.",
            "calculation": "Mode = 40 + 4 × 3 = 40 + 12 = 52 marks.",
            "finalAnswer": "Mode = 52 marks, Mean = 62 marks",
            "unit": "marks",
            "solution": "GIVEN:\nDistribution of marks obtained by 30 students:\n- 10-25: 2\n- 25-40: 3\n- 40-55: 7\n- 55-70: 6\n- 70-85: 6\n- 85-100: 6\nMean marks (from Example 1) = 62 marks.\n\nTO FIND:\n(i) Mode of the marks distribution.\n(ii) Comparison and interpretation of mode and mean.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Identify modal class:\nMaximum frequency is 7, which belongs to interval 40 - 55.\nTherefore, Modal Class = 40 - 55.\n\nStep 2: Identify parameters:\n- Lower limit, l = 40\n- Class size, h = 55 - 40 = 15\n- Frequency of modal class, f1 = 7\n- Frequency of preceding class (25 - 40), f0 = 3\n- Frequency of succeeding class (55 - 70), f2 = 6\n\nStep 3: Calculate Mode:\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nMode = 40 + [ (7 - 3) / (2 × 7 - 3 - 6) ] × 15\nMode = 40 + [ 4 / (14 - 9) ] × 15\nMode = 40 + [ 4 / 5 ] × 15\nMode = 40 + (4 × 3) = 40 + 12 = 52 marks.\n\nStep 4: Comparison and Interpretation:\n- Mode = 52 marks indicates that the maximum number of students obtained around 52 marks.\n- Mean = 62 marks indicates that the average overall performance score of all 30 students combined is 62 marks.\n\n[ROUGH_WORK]\n(7-3)/(14-9) = 4/5. (4/5) × 15 = 12. 40 + 12 = 52 marks.\nBoxed Answer: [ Mode = 52 marks, Mean = 62 marks ].",
            "concept_questions": []
        }
    ]

    m3_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 190] Example 7: A survey regarding the heights (in cm) of 51 girls of Class X of a school was conducted and the following data was obtained: Less than 140: 4; Less than 145: 11; Less than 150: 29; Less than 155: 40; Less than 160: 46; Less than 165: 51. Find the median height.",
            "section": "13.4 Median of Grouped Data",
            "page_number": 190,
            "image_search_query": "median height cumulative frequency less than ogive",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Cumulative frequency distribution of heights of 51 girls:\nLess than 140: 4; Less than 145: 11; Less than 150: 29; Less than 155: 40; Less than 160: 46; Less than 165: 51.\nTotal frequency N = 51.",
            "formula": "Median = l + [ (N/2 - cf) / f ] × h\nwhere:\n- N/2 = 51/2 = 25.5\n- Median Class is the class whose cf is just greater than N/2\n- l = lower limit of median class\n- cf = cumulative frequency of preceding class\n- f = frequency of median class\n- h = class size.",
            "substitution": "Convert to standard class intervals:\n135-140: 4 (cf = 4)\n140-145: 11 - 4 = 7 (cf = 11)\n145-150: 29 - 11 = 18 (cf = 29) ⇒ Median class since cf=29 > 25.5!\n150-155: 40 - 29 = 11 (cf = 40)\n155-160: 46 - 40 = 6 (cf = 46)\n160-165: 51 - 46 = 5 (cf = 51)\nFor Median Class 145-150: l = 145, h = 5, f = 18, cf = 11.",
            "calculation": "Median = 145 + [ (25.5 - 11) / 18 ] × 5 = 145 + [ 14.5 / 18 ] × 5 = 145 + 72.5 / 18 = 145 + 4.03 = 149.03 cm.",
            "finalAnswer": "149.03 cm",
            "unit": "cm",
            "solution": "GIVEN:\nCumulative distribution ('less than' type) of heights of 51 girls:\n- Less than 140: 4\n- Less than 145: 11\n- Less than 150: 29\n- Less than 155: 40\n- Less than 160: 46\n- Less than 165: 51\nTotal frequency, N = 51.\n\nTO FIND:\nMedian height of the girls.\n\nFORMULA USED:\nMedian = l + [ (N/2 - cf) / f ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Convert cumulative data to class intervals and individual frequencies (fi):\n- 135 - 140: frequency fi = 4; cf = 4\n- 140 - 145: frequency fi = 11 - 4 = 7; cf = 11\n- 145 - 150: frequency fi = 29 - 11 = 18; cf = 29\n- 150 - 155: frequency fi = 40 - 29 = 11; cf = 40\n- 155 - 160: frequency fi = 46 - 40 = 6; cf = 46\n- 160 - 165: frequency fi = 51 - 46 = 5; cf = 51\n\nStep 2: Find N/2 and determine Median Class:\nN / 2 = 51 / 2 = 25.5.\nThe cumulative frequency just greater than 25.5 is 29, which corresponds to the interval 145 - 150.\nTherefore, Median Class = 145 - 150.\n\nStep 3: Extract parameters:\n- Lower limit, l = 145\n- Cumulative frequency of preceding class, cf = 11\n- Frequency of median class, f = 18\n- Class width, h = 5\n\nStep 4: Compute Median:\nMedian = 145 + [ (25.5 - 11) / 18 ] × 5\nMedian = 145 + [ 14.5 / 18 ] × 5\nMedian = 145 + (72.5 / 18) = 145 + 4.027... ≈ 149.03 cm.\n\n[ROUGH_WORK]\n25.5 - 11 = 14.5. 14.5 × 5 = 72.5. 72.5 / 18 = 4.028. 145 + 4.03 = 149.03 cm.\nBoxed Answer: [ 149.03 cm ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 193] Example 8: The median of the following data is 525. Find the values of x and y, if the total frequency is 100:\n0-100: 2; 100-200: 5; 200-300: x; 300-400: 12; 400-500: 17; 500-600: 20; 600-700: y; 700-800: 9; 800-900: 7; 900-1000: 4.",
            "section": "13.4 Median of Grouped Data",
            "page_number": 193,
            "image_search_query": "median missing frequencies x y grouped data 100",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Median = 525. Total frequency N = 100. Distribution with missing frequencies x and y in classes 200-300 and 600-700.",
            "formula": "Median = l + [ (N/2 - cf) / f ] × h. Total frequency Σfi = N.",
            "substitution": "Cumulative frequencies cf:\n0-100: 2\n100-200: 7\n200-300: 7 + x\n300-400: 19 + x\n400-500: 36 + x\n500-600: 56 + x\n600-700: 56 + x + y\n700-800: 65 + x + y\n800-900: 72 + x + y\n900-1000: 76 + x + y.\nTotal frequency equation: 76 + x + y = 100 ⇒ x + y = 24 ... (1).\nSince Median = 525, it lies in the interval 500-600 (Median Class):\nl = 500, f = 20, h = 100, cf = 36 + x, N/2 = 50.\n525 = 500 + [ (50 - (36 + x)) / 20 ] × 100.",
            "calculation": "525 - 500 = [ (14 - x) / 20 ] × 100\n25 = (14 - x) × 5 ⇒ 14 - x = 5 ⇒ x = 9.\nFrom (1): 9 + y = 24 ⇒ y = 15.",
            "finalAnswer": "x = 9, y = 15",
            "unit": "frequencies",
            "solution": "GIVEN:\nMedian = 525.\nTotal frequency, N = 100.\nClass intervals of width h = 100 with unknown frequencies x and y.\n\nTO FIND:\nValues of missing frequencies x and y.\n\nFORMULA USED:\n1. Total frequency: Σfi = N = 100\n2. Median formula: Median = l + [ (N/2 - cf) / f ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Form the cumulative frequency table:\n- 0 - 100: fi = 2; cf = 2\n- 100 - 200: fi = 5; cf = 7\n- 200 - 300: fi = x; cf = 7 + x\n- 300 - 400: fi = 12; cf = 19 + x\n- 400 - 500: fi = 17; cf = 36 + x\n- 500 - 600: fi = 20; cf = 56 + x\n- 600 - 700: fi = y; cf = 56 + x + y\n- 700 - 800: fi = 9; cf = 65 + x + y\n- 800 - 900: fi = 7; cf = 72 + x + y\n- 900 - 1000: fi = 4; cf = 76 + x + y\n\nStep 2: Relate total frequency to equation in x and y:\n76 + x + y = 100\nx + y = 100 - 76\nx + y = 24   ... (1)\n\nStep 3: Use the given median value to find x:\nSince Median = 525, it lies in the class interval 500 - 600.\nTherefore, Median Class = 500 - 600.\nParameters:\n- Lower limit, l = 500\n- Class width, h = 100\n- Frequency of median class, f = 20\n- cf of preceding class = 36 + x\n- N / 2 = 100 / 2 = 50\n\nApply the median formula:\n525 = 500 + [ (50 - (36 + x)) / 20 ] × 100\n525 - 500 = [ (14 - x) / 20 ] × 100\n25 = (14 - x) × 5\nDivide both sides by 5:\n5 = 14 - x\nx = 14 - 5 = 9.\n\nStep 4: Find y using equation (1):\nx + y = 24\n9 + y = 24\ny = 24 - 9 = 15.\n\n[ROUGH_WORK]\nx = 9, y = 15. Check: 76 + 9 + 15 = 100. Median = 500 + ((50 - 45)/20) × 100 = 500 + (5/20) × 100 = 500 + 25 = 525. Exactly verified!\nBoxed Answer: [ x = 9, y = 15 ].",
            "concept_questions": []
        }
    ]

    m4_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 182] Exercise 13.1 Q1: A survey was conducted by a group of students as a part of their environment awareness programme, in which they collected the following data regarding the number of plants in 20 houses in a locality. Find the mean number of plants per house (0-2: 1; 2-4: 2; 4-6: 1; 6-8: 5; 8-10: 6; 10-12: 2; 12-14: 3). Which method did you use for finding the mean, and why?",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 182,
            "image_search_query": "mean number of plants direct method small values",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Number of plants in 20 houses: 0-2: 1; 2-4: 2; 4-6: 1; 6-8: 5; 8-10: 6; 10-12: 2; 12-14: 3. Total houses Σfi = 20.",
            "formula": "Direct Method: Mean x̄ = (Σ fi xi) / (Σ fi). Direct method is chosen because numerical values of fi and xi are very small.",
            "substitution": "xi values: 1, 3, 5, 7, 9, 11, 13.\nfi xi products: 1×1=1, 2×3=6, 1×5=5, 5×7=35, 6×9=54, 2×11=22, 3×13=39.\nΣ fi xi = 1 + 6 + 5 + 35 + 54 + 22 + 39 = 162.",
            "calculation": "Mean x̄ = 162 / 20 = 8.1 plants.",
            "finalAnswer": "8.1 plants (Direct Method used as values of fi and xi are small)",
            "unit": "plants",
            "solution": "GIVEN:\nDistribution of plants across 20 houses:\n- 0 - 2: 1; 2 - 4: 2; 4 - 6: 1; 6 - 8: 5; 8 - 10: 6; 10 - 12: 2; 12 - 14: 3.\nTotal houses, Σfi = 20.\n\nTO FIND:\n(i) Mean number of plants per house.\n(ii) Choice of method and justification.\n\nFORMULA USED:\nDirect Method: Mean (x̄) = Σ(fi × xi) / Σfi.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi) and products (fi × xi):\n- 0 - 2: xi = 1; fi = 1; fi × xi = 1\n- 2 - 4: xi = 3; fi = 2; fi × xi = 6\n- 4 - 6: xi = 5; fi = 1; fi × xi = 5\n- 6 - 8: xi = 7; fi = 5; fi × xi = 35\n- 8 - 10: xi = 9; fi = 6; fi × xi = 54\n- 10 - 12: xi = 11; fi = 2; fi × xi = 22\n- 12 - 14: xi = 13; fi = 3; fi × xi = 39\n\nStep 2: Sum the values:\nΣ(fi × xi) = 1 + 6 + 5 + 35 + 54 + 22 + 39 = 162\nΣfi = 20.\n\nStep 3: Calculate Mean:\nx̄ = 162 / 20 = 8.1 plants.\n\nStep 4: Method Justification:\nThe Direct Method was used because the numerical values of both class marks (xi) and frequencies (fi) are small integers, making direct multiplication simple and error-free.\n\n[ROUGH_WORK]\n162 / 20 = 8.1.\nBoxed Answer: [ 8.1 plants ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 182] Exercise 13.1 Q2: Consider the following distribution of daily wages of 50 workers of a factory (500-520: 12; 520-540: 14; 540-560: 8; 560-580: 6; 580-600: 10). Find the mean daily wages of the workers of the factory by using an appropriate method.",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 182,
            "image_search_query": "daily wages workers mean step deviation method",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Daily wages of 50 workers: 500-520: 12; 520-540: 14; 540-560: 8; 560-580: 6; 580-600: 10. Σfi = 50.",
            "formula": "Step-Deviation Method: Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)], where a = 550, h = 20, ui = (xi - 550) / 20.",
            "substitution": "xi values: 510, 530, 550, 570, 590.\nui values: -2, -1, 0, 1, 2.\nfi ui products: 12(-2) = -24; 14(-1) = -14; 8(0) = 0; 6(1) = 6; 10(2) = 20.\nΣ fi ui = (-24 - 14) + (6 + 20) = -38 + 26 = -12.",
            "calculation": "x̄ = 550 + 20 × (-12 / 50) = 550 - 240 / 50 = 550 - 4.8 = ₹ 545.20.",
            "finalAnswer": "₹ 545.20",
            "unit": "rupees",
            "solution": "GIVEN:\nDaily wages of 50 workers:\n- 500 - 520: 12\n- 520 - 540: 14\n- 540 - 560: 8\n- 560 - 580: 6\n- 580 - 600: 10\nTotal workers, Σfi = 50.\n\nTO FIND:\nMean daily wage of the workers.\n\nFORMULA USED:\nStep-Deviation Method:\nMean (x̄) = a + h × [ Σ(fi × ui) / Σfi ]\nwith assumed mean a = 550 and class width h = 20.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), ui = (xi - 550)/20, and fi × ui:\n- 500 - 520: xi = 510; ui = -2; fi = 12; fi × ui = -24\n- 520 - 540: xi = 530; ui = -1; fi = 14; fi × ui = -14\n- 540 - 560: xi = 550; ui = 0; fi = 8; fi × ui = 0\n- 560 - 580: xi = 570; ui = 1; fi = 6; fi × ui = 6\n- 580 - 600: xi = 590; ui = 2; fi = 10; fi × ui = 20\n\nStep 2: Sum the values:\nΣ(fi × ui) = -24 - 14 + 6 + 20 = -38 + 26 = -12\nΣfi = 50.\n\nStep 3: Calculate Mean:\nx̄ = 550 + 20 × [ -12 / 50 ]\nx̄ = 550 - (240 / 50) = 550 - 4.8 = ₹ 545.20.\n\n[ROUGH_WORK]\n550 - 4.80 = 545.20 rupees.\nBoxed Answer: [ ₹ 545.20 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 182] Exercise 13.1 Q3: The following distribution shows the daily pocket allowance of children of a locality. The mean pocket allowance is ₹ 18. Find the missing frequency f (11-13: 7; 13-15: 6; 15-17: 9; 17-19: 13; 19-21: f; 21-23: 5; 23-25: 4).",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 182,
            "image_search_query": "mean missing frequency pocket allowance calculation",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Mean pocket allowance x̄ = ₹ 18. Distribution: 11-13: 7; 13-15: 6; 15-17: 9; 17-19: 13; 19-21: f; 21-23: 5; 23-25: 4.",
            "formula": "Direct / Assumed Mean Method: x̄ = (Σ fi xi) / (Σ fi). Let a = 18 (assumed mean), di = xi - 18. Then x̄ - a = (Σ fi di) / (Σ fi) = 0.",
            "substitution": "xi values: 12, 14, 16, 18, 20, 22, 24.\ndi = xi - 18: -6, -4, -2, 0, 2, 4, 6.\nfi di products:\n7(-6) = -42\n6(-4) = -24\n9(-2) = -18\n13(0) = 0\nf(2) = 2f\n5(4) = 20\n4(6) = 24\nΣ fi di = (-42 - 24 - 18) + (20 + 24) + 2f = -84 + 44 + 2f = 2f - 40.",
            "calculation": "Since x̄ = a = 18, Σ fi di = 0 ⇒ 2f - 40 = 0 ⇒ 2f = 40 ⇒ f = 20.",
            "finalAnswer": "f = 20",
            "unit": "frequency",
            "solution": "GIVEN:\nMean daily pocket allowance, x̄ = ₹ 18.\nDistribution:\n- 11 - 13: 7; 13 - 15: 6; 15 - 17: 9; 17 - 19: 13; 19 - 21: f; 21 - 23: 5; 23 - 25: 4.\n\nTO FIND:\nThe missing frequency f.\n\nFORMULA USED:\nAssumed Mean Method:\nx̄ = a + [ Σ(fi × di) / Σfi ]\nChoose assumed mean a = 18 (which equals the given mean x̄!).\nTherefore, [ Σ(fi × di) / Σfi ] = 0 ⇒ Σ(fi × di) = 0.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), deviations di = xi - 18, and fi × di:\n- 11 - 13: xi = 12; di = -6; fi = 7; fi × di = -42\n- 13 - 15: xi = 14; di = -4; fi = 6; fi × di = -24\n- 15 - 17: xi = 16; di = -2; fi = 9; fi × di = -18\n- 17 - 19: xi = 18; di = 0; fi = 13; fi × di = 0\n- 19 - 21: xi = 20; di = 2; fi = f; fi × di = 2f\n- 21 - 23: xi = 22; di = 4; fi = 5; fi × di = 20\n- 23 - 25: xi = 24; di = 6; fi = 4; fi × di = 24\n\nStep 2: Sum the deviations:\nSum of negative terms = -42 - 24 - 18 = -84\nSum of known positive terms = 20 + 24 = 44\nTotal Σ(fi × di) = -84 + 44 + 2f = 2f - 40.\n\nStep 3: Solve for f:\nSince x̄ = a = 18:\n2f - 40 = 0\n2f = 40\nf = 20.\n\n[ROUGH_WORK]\n2f - 40 = 0 ⇒ f = 20.\nBoxed Answer: [ f = 20 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 183] Exercise 13.1 Q4: Thirty women were examined in a hospital by a doctor and the number of heart beats per minute were recorded and summarised as follows. Find the mean heart beats per minute for these women, choosing a suitable method (65-68: 2; 68-71: 4; 71-74: 3; 74-77: 8; 77-80: 7; 80-83: 4; 83-86: 2).",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 183,
            "image_search_query": "women heart beats mean step deviation method",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Heart beats per minute for 30 women across class intervals of width h = 3:\n65-68: 2; 68-71: 4; 71-74: 3; 74-77: 8; 77-80: 7; 80-83: 4; 83-86: 2. Σfi = 30.",
            "formula": "Step-Deviation Method: Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)], where a = 75.5, h = 3, ui = (xi - 75.5) / 3.",
            "substitution": "xi values: 66.5, 69.5, 72.5, 75.5, 78.5, 81.5, 84.5.\nui values: -3, -2, -1, 0, 1, 2, 3.\nfi ui products: 2(-3) = -6; 4(-2) = -8; 3(-1) = -3; 8(0) = 0; 7(1) = 7; 4(2) = 8; 2(3) = 6.\nΣ fi ui = (-6 - 8 - 3) + (7 + 8 + 6) = -17 + 21 = 4.",
            "calculation": "x̄ = 75.5 + 3 × (4 / 30) = 75.5 + 12 / 30 = 75.5 + 0.4 = 75.9 beats/min.",
            "finalAnswer": "75.9 beats/minute",
            "unit": "beats/min",
            "solution": "GIVEN:\nHeart beats per minute of 30 women:\n- 65-68: 2; 68-71: 4; 71-74: 3; 74-77: 8; 77-80: 7; 80-83: 4; 83-86: 2.\nTotal women, Σfi = 30.\n\nTO FIND:\nMean heart beats per minute.\n\nFORMULA USED:\nStep-Deviation Method: Mean (x̄) = a + h × [ Σ(fi × ui) / Σfi ]\nwith assumed mean a = 75.5 and class size h = 3.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), ui = (xi - 75.5)/3, and fi × ui:\n- 65-68: xi = 66.5; ui = -3; fi = 2; fi × ui = -6\n- 68-71: xi = 69.5; ui = -2; fi = 4; fi × ui = -8\n- 71-74: xi = 72.5; ui = -1; fi = 3; fi × ui = -3\n- 74-77: xi = 75.5; ui = 0; fi = 8; fi × ui = 0\n- 77-80: xi = 78.5; ui = 1; fi = 7; fi × ui = 7\n- 80-83: xi = 81.5; ui = 2; fi = 4; fi × ui = 8\n- 83-86: xi = 84.5; ui = 3; fi = 2; fi × ui = 6\n\nStep 2: Sum the values:\nΣ(fi × ui) = -6 - 8 - 3 + 7 + 8 + 6 = -17 + 21 = 4\nΣfi = 30.\n\nStep 3: Calculate Mean:\nx̄ = 75.5 + 3 × [ 4 / 30 ]\nx̄ = 75.5 + (12 / 30) = 75.5 + 0.4 = 75.9 beats/min.\n\n[ROUGH_WORK]\n75.5 + 0.4 = 75.9.\nBoxed Answer: [ 75.9 beats/minute ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 183] Exercise 13.1 Q5: In a retail market, fruit vendors were selling mangoes kept in packing boxes. These boxes contained varying number of mangoes. The following was the distribution of mangoes according to the number of boxes: 50-52: 15; 53-55: 110; 56-58: 135; 59-61: 115; 62-64: 25. Find the mean number of mangoes kept in a packing box. Which method of finding the mean did you choose?",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 183,
            "image_search_query": "mean mangoes packing boxes continuous class boundaries",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Discontinuous class intervals of mangoes: 50-52: 15; 53-55: 110; 56-58: 135; 59-61: 115; 62-64: 25. Total boxes Σfi = 400.",
            "formula": "Convert to continuous classes: 49.5-52.5, 52.5-55.5, 55.5-58.5, 58.5-61.5, 61.5-64.5 (class size h = 3). Class marks xi = 51, 54, 57, 60, 63. Step-Deviation: x̄ = a + h × [(Σ fi ui) / (Σ fi)] with a = 57.",
            "substitution": "ui = (xi - 57) / 3: -2, -1, 0, 1, 2.\nfi ui products: 15(-2) = -30; 110(-1) = -110; 135(0) = 0; 115(1) = 115; 25(2) = 50.\nΣ fi ui = (-30 - 110) + (115 + 50) = -140 + 165 = 25.",
            "calculation": "x̄ = 57 + 3 × (25 / 400) = 57 + 75 / 400 = 57 + 3 / 16 = 57 + 0.1875 = 57.19 mangoes.",
            "finalAnswer": "57.19 mangoes (Step-Deviation method chosen)",
            "unit": "mangoes",
            "solution": "GIVEN:\nDistribution of mangoes in 400 boxes:\n- 50 - 52: 15\n- 53 - 55: 110\n- 56 - 58: 135\n- 59 - 61: 115\n- 62 - 64: 25\nTotal boxes, Σfi = 400.\n\nTO FIND:\nMean number of mangoes per box and method used.\n\nFORMULA USED:\nStep-Deviation Method:\nMean (x̄) = a + h × [ Σ(fi × ui) / Σfi ]\nConvert discontinuous classes to continuous boundaries:\nSubtract 0.5 from lower limit and add 0.5 to upper limit:\n49.5-52.5, 52.5-55.5, 55.5-58.5, 58.5-61.5, 61.5-64.5 (Class size h = 3).\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), ui = (xi - 57)/3, and fi × ui:\n- 49.5 - 52.5: xi = 51; ui = -2; fi = 15; fi × ui = -30\n- 52.5 - 55.5: xi = 54; ui = -1; fi = 110; fi × ui = -110\n- 55.5 - 58.5: xi = 57; ui = 0; fi = 135; fi × ui = 0\n- 58.5 - 61.5: xi = 60; ui = 1; fi = 115; fi × ui = 115\n- 61.5 - 64.5: xi = 63; ui = 2; fi = 25; fi × ui = 50\n\nStep 2: Sum the values:\nΣ(fi × ui) = -30 - 110 + 0 + 115 + 50 = -140 + 165 = 25\nΣfi = 400.\n\nStep 3: Calculate Mean:\nx̄ = 57 + 3 × [ 25 / 400 ]\nx̄ = 57 + (75 / 400) = 57 + (3 / 16) = 57 + 0.1875 ≈ 57.19 mangoes.\n\n[ROUGH_WORK]\n57 + 3/16 = 57.1875 ≈ 57.19.\nBoxed Answer: [ 57.19 mangoes ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 183] Exercise 13.1 Q6: The table below shows the daily expenditure on food of 25 households in a locality (100-150: 4; 150-200: 5; 200-250: 12; 250-300: 2; 300-350: 2). Find the mean daily expenditure on food by a suitable method.",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 183,
            "image_search_query": "daily food expenditure mean step deviation method",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Daily food expenditure of 25 households: 100-150: 4; 150-200: 5; 200-250: 12; 250-300: 2; 300-350: 2. Σfi = 25.",
            "formula": "Step-Deviation Method: Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)], where a = 225, h = 50, ui = (xi - 225) / 50.",
            "substitution": "xi values: 125, 175, 225, 275, 325.\nui values: -2, -1, 0, 1, 2.\nfi ui products: 4(-2) = -8; 5(-1) = -5; 12(0) = 0; 2(1) = 2; 2(2) = 4.\nΣ fi ui = (-8 - 5) + (2 + 4) = -13 + 6 = -7.",
            "calculation": "x̄ = 225 + 50 × (-7 / 25) = 225 - 2 × 7 = 225 - 14 = ₹ 211.",
            "finalAnswer": "₹ 211",
            "unit": "rupees",
            "solution": "GIVEN:\nDaily food expenditure of 25 households:\n- 100 - 150: 4\n- 150 - 200: 5\n- 200 - 250: 12\n- 250 - 300: 2\n- 300 - 350: 2\nTotal households, Σfi = 25.\n\nTO FIND:\nMean daily food expenditure.\n\nFORMULA USED:\nStep-Deviation Method:\nMean (x̄) = a + h × [ Σ(fi × ui) / Σfi ]\nwith assumed mean a = 225 and class size h = 50.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), ui = (xi - 225)/50, and fi × ui:\n- 100 - 150: xi = 125; ui = -2; fi = 4; fi × ui = -8\n- 150 - 200: xi = 175; ui = -1; fi = 5; fi × ui = -5\n- 200 - 250: xi = 225; ui = 0; fi = 12; fi × ui = 0\n- 250 - 300: xi = 275; ui = 1; fi = 2; fi × ui = 2\n- 300 - 350: xi = 325; ui = 2; fi = 2; fi × ui = 4\n\nStep 2: Sum the values:\nΣ(fi × ui) = -8 - 5 + 0 + 2 + 4 = -13 + 6 = -7\nΣfi = 25.\n\nStep 3: Calculate Mean:\nx̄ = 225 + 50 × [ -7 / 25 ]\nx̄ = 225 - (2 × 7) = 225 - 14 = ₹ 211.\n\n[ROUGH_WORK]\n225 - 14 = 211 rupees.\nBoxed Answer: [ ₹ 211 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 183] Exercise 13.1 Q7: To find out the concentration of SO₂ in the air (in parts per million, i.e., ppm), the data was collected for 30 localities in a certain city and is presented below: 0.00-0.04: 4; 0.04-0.08: 9; 0.08-0.12: 9; 0.12-0.16: 2; 0.16-0.20: 4; 0.20-0.24: 2. Find the mean concentration of SO₂ in the air.",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 183,
            "image_search_query": "so2 concentration mean air pollution parts per million",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "SO₂ concentration in 30 localities: 0.00-0.04: 4; 0.04-0.08: 9; 0.08-0.12: 9; 0.12-0.16: 2; 0.16-0.20: 4; 0.20-0.24: 2. Σfi = 30.",
            "formula": "Step-Deviation / Assumed Mean: Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)], where a = 0.10 (or 0.14), h = 0.04.",
            "substitution": "xi values: 0.02, 0.06, 0.10, 0.14, 0.18, 0.22. Choose a = 0.10, h = 0.04.\nui = (xi - 0.10)/0.04: -2, -1, 0, 1, 2, 3.\nfi ui products: 4(-2) = -8; 9(-1) = -9; 9(0) = 0; 2(1) = 2; 4(2) = 8; 2(3) = 6.\nΣ fi ui = (-8 - 9) + (2 + 8 + 6) = -17 + 16 = -1.",
            "calculation": "x̄ = 0.10 + 0.04 × (-1 / 30) = 0.10 - 0.00133 = 0.09867... ≈ 0.099 ppm.",
            "finalAnswer": "0.099 ppm",
            "unit": "ppm",
            "solution": "GIVEN:\nConcentration of SO₂ in 30 localities (in ppm):\n- 0.00 - 0.04: 4; 0.04 - 0.08: 9; 0.08 - 0.12: 9; 0.12 - 0.16: 2; 0.16 - 0.20: 4; 0.20 - 0.24: 2.\nTotal localities, Σfi = 30.\n\nTO FIND:\nMean concentration of SO₂ in the air.\n\nFORMULA USED:\nStep-Deviation Method:\nMean (x̄) = a + h × [ Σ(fi × ui) / Σfi ]\nwith assumed mean a = 0.10 and class width h = 0.04.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), ui = (xi - 0.10)/0.04, and fi × ui:\n- 0.00 - 0.04: xi = 0.02; ui = -2; fi = 4; fi × ui = -8\n- 0.04 - 0.08: xi = 0.06; ui = -1; fi = 9; fi × ui = -9\n- 0.08 - 0.12: xi = 0.10; ui = 0; fi = 9; fi × ui = 0\n- 0.12 - 0.16: xi = 0.14; ui = 1; fi = 2; fi × ui = 2\n- 0.16 - 0.20: xi = 0.18; ui = 2; fi = 4; fi × ui = 8\n- 0.20 - 0.24: xi = 0.22; ui = 3; fi = 2; fi × ui = 6\n\nStep 2: Sum the values:\nΣ(fi × ui) = -8 - 9 + 0 + 2 + 8 + 6 = -17 + 16 = -1\nΣfi = 30.\n\nStep 3: Calculate Mean:\nx̄ = 0.10 + 0.04 × [ -1 / 30 ]\nx̄ = 0.10 - 0.04 / 30 = 0.10 - 0.00133... ≈ 0.099 ppm.\n\n[ROUGH_WORK]\nDirect check: Σfixi = 0.08 + 0.54 + 0.90 + 0.28 + 0.72 + 0.44 = 2.96. 2.96 / 30 = 0.09867 ≈ 0.099 ppm.\nBoxed Answer: [ 0.099 ppm ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 184] Exercise 13.1 Q8: A class teacher has the following absentee record of 40 students of a class for the whole term. Find the mean number of days a student was absent (0-6: 11; 6-10: 10; 10-14: 7; 14-20: 4; 20-28: 4; 28-38: 3; 38-40: 1).",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 184,
            "image_search_query": "student absentee record unequal class intervals mean",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Absentee record of 40 students across unequal intervals: 0-6: 11; 6-10: 10; 10-14: 7; 14-20: 4; 20-28: 4; 28-38: 3; 38-40: 1. Σfi = 40.",
            "formula": "Direct Method: Mean x̄ = (Σ fi xi) / (Σ fi) (or Assumed Mean with di = xi - 17).",
            "substitution": "xi values:\n0-6: 3 ⇒ 11 × 3 = 33\n6-10: 8 ⇒ 10 × 8 = 80\n10-14: 12 ⇒ 7 × 12 = 84\n14-20: 17 ⇒ 4 × 17 = 68\n20-28: 24 ⇒ 4 × 24 = 96\n28-38: 33 ⇒ 3 × 33 = 99\n38-40: 39 ⇒ 1 × 39 = 39\nΣ fi xi = 33 + 80 + 84 + 68 + 96 + 99 + 39 = 499.",
            "calculation": "x̄ = 499 / 40 = 12.475 ≈ 12.48 days.",
            "finalAnswer": "12.48 days",
            "unit": "days",
            "solution": "GIVEN:\nNumber of days 40 students were absent:\n- 0 - 6: 11; 6 - 10: 10; 10 - 14: 7; 14 - 20: 4; 20 - 28: 4; 28 - 38: 3; 38 - 40: 1.\nTotal students, Σfi = 40.\n\nTO FIND:\nMean number of days a student was absent.\n\nFORMULA USED:\nSince class widths are unequal (6, 4, 4, 6, 8, 10, 2), we use the Direct Method:\nMean (x̄) = Σ(fi × xi) / Σfi.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi) and products (fi × xi):\n- 0 - 6: xi = 3; fi = 11; fi × xi = 33\n- 6 - 10: xi = 8; fi = 10; fi × xi = 80\n- 10 - 14: xi = 12; fi = 7; fi × xi = 84\n- 14 - 20: xi = 17; fi = 4; fi × xi = 68\n- 20 - 28: xi = 24; fi = 4; fi × xi = 96\n- 28 - 38: xi = 33; fi = 3; fi × xi = 99\n- 38 - 40: xi = 39; fi = 1; fi × xi = 39\n\nStep 2: Sum the values:\nΣ(fi × xi) = 33 + 80 + 84 + 68 + 96 + 99 + 39 = 499\nΣfi = 40.\n\nStep 3: Calculate Mean:\nx̄ = 499 / 40 = 12.475 ≈ 12.48 days.\n\n[ROUGH_WORK]\n499 / 40 = 12.475 days.\nBoxed Answer: [ 12.48 days ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.2 | Page 184] Exercise 13.1 Q9: The following table gives the literacy rate (in percentage) of 35 cities. Find the mean literacy rate (45-55: 3; 55-65: 10; 65-75: 11; 75-85: 8; 85-95: 3).",
            "section": "13.2 Mean of Grouped Data",
            "page_number": 184,
            "image_search_query": "literacy rate 35 cities mean step deviation",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Literacy rates of 35 cities: 45-55: 3; 55-65: 10; 65-75: 11; 75-85: 8; 85-95: 3. Σfi = 35.",
            "formula": "Step-Deviation Method: Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)], where a = 70, h = 10, ui = (xi - 70) / 10.",
            "substitution": "xi values: 50, 60, 70, 80, 90.\nui values: -2, -1, 0, 1, 2.\nfi ui products: 3(-2) = -6; 10(-1) = -10; 11(0) = 0; 8(1) = 8; 3(2) = 6.\nΣ fi ui = (-6 - 10) + (8 + 6) = -16 + 14 = -2.",
            "calculation": "x̄ = 70 + 10 × (-2 / 35) = 70 - 20 / 35 = 70 - 4 / 7 = 70 - 0.57 = 69.43%.",
            "finalAnswer": "69.43%",
            "unit": "%",
            "solution": "GIVEN:\nLiteracy rate of 35 cities:\n- 45 - 55: 3\n- 55 - 65: 10\n- 65 - 75: 11\n- 75 - 85: 8\n- 85 - 95: 3\nTotal cities, Σfi = 35.\n\nTO FIND:\nMean literacy rate.\n\nFORMULA USED:\nStep-Deviation Method:\nMean (x̄) = a + h × [ Σ(fi × ui) / Σfi ]\nwith assumed mean a = 70 and class size h = 10.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute class marks (xi), ui = (xi - 70)/10, and fi × ui:\n- 45 - 55: xi = 50; ui = -2; fi = 3; fi × ui = -6\n- 55 - 65: xi = 60; ui = -1; fi = 10; fi × ui = -10\n- 65 - 75: xi = 70; ui = 0; fi = 11; fi × ui = 0\n- 75 - 85: xi = 80; ui = 1; fi = 8; fi × ui = 8\n- 85 - 95: xi = 90; ui = 2; fi = 3; fi × ui = 6\n\nStep 2: Sum the values:\nΣ(fi × ui) = -6 - 10 + 0 + 8 + 6 = -16 + 14 = -2\nΣfi = 35.\n\nStep 3: Calculate Mean:\nx̄ = 70 + 10 × [ -2 / 35 ]\nx̄ = 70 - (20 / 35) = 70 - (4 / 7) = 70 - 0.5714... ≈ 69.43%.\n\n[ROUGH_WORK]\n70 - 0.57 = 69.43%.\nBoxed Answer: [ 69.43% ].",
            "concept_questions": []
        }
    ]

    m5_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 187] Exercise 13.2 Q1: The following table shows the ages of the patients admitted in a hospital during a year: 5-15: 6; 15-25: 11; 25-35: 21; 35-45: 23; 45-55: 14; 55-65: 5. Find the mode and the mean of the data given above. Compare and interpret the two measures of central tendency.",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 187,
            "image_search_query": "mode mean hospital patients age compare",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Ages of 80 patients: 5-15: 6; 15-25: 11; 25-35: 21; 35-45: 23; 45-55: 14; 55-65: 5. Total Σfi = 80. Max frequency = 23 (Modal class 35-45).",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h.\nMean x̄ = a + h × [(Σ fi ui) / (Σ fi)].",
            "substitution": "For Mode: l = 35, h = 10, f1 = 23, f0 = 21, f2 = 14.\nMode = 35 + [ (23 - 21) / (2(23) - 21 - 14) ] × 10 = 35 + [ 2 / (46 - 35) ] × 10 = 35 + 20 / 11 = 35 + 1.82 = 36.82 years.\nFor Mean: a = 30, h = 10, ui: -2, -1, 0, 1, 2, 3.\nΣ fi ui = 6(-2) + 11(-1) + 21(0) + 23(1) + 14(2) + 5(3) = -23 + 66 = 43.\nMean = 30 + 10 × (43 / 80) = 30 + 43 / 8 = 30 + 5.375 = 35.38 years.",
            "calculation": "Mode = 36.82 years.\nMean = 35.38 years.",
            "finalAnswer": "Mode = 36.82 years, Mean = 35.38 years",
            "unit": "years",
            "solution": "GIVEN:\nAges of 80 hospital patients:\n- 5-15: 6; 15-25: 11; 25-35: 21; 35-45: 23; 45-55: 14; 55-65: 5.\nTotal patients, Σfi = 80.\n\nTO FIND:\n(i) Mode of the data.\n(ii) Mean of the data.\n(iii) Comparison and interpretation.\n\nSTEP-BY-STEP CALCULATION:\nPart 1: Calculate Mode:\nModal class with highest frequency (23) is 35 - 45.\n- Lower limit, l = 35\n- Class width, h = 10\n- f1 = 23, f0 = 21, f2 = 14\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nMode = 35 + [ (23 - 21) / (2 × 23 - 21 - 14) ] × 10\nMode = 35 + [ 2 / (46 - 35) ] × 10\nMode = 35 + (20 / 11) = 35 + 1.818... ≈ 36.82 years.\n\nPart 2: Calculate Mean (Step-Deviation):\nClass marks: 10, 20, 30, 40, 50, 60. Assumed mean a = 30, h = 10.\n- 5-15: xi = 10; ui = -2; fi = 6; fi ui = -12\n- 15-25: xi = 20; ui = -1; fi = 11; fi ui = -11\n- 25-35: xi = 30; ui = 0; fi = 21; fi ui = 0\n- 35-45: xi = 40; ui = 1; fi = 23; fi ui = 23\n- 45-55: xi = 50; ui = 2; fi = 14; fi ui = 28\n- 55-65: xi = 60; ui = 3; fi = 5; fi ui = 15\nΣ(fi ui) = -23 + 66 = 43\nx̄ = 30 + 10 × (43 / 80) = 30 + 5.375 = 35.38 years.\n\nPart 3: Interpretation:\n- Mode = 36.82 years indicates that maximum number of admitted patients were around 36.8 years of age.\n- Mean = 35.38 years indicates that the average age of all admitted patients combined is 35.38 years.\n\n[ROUGH_WORK]\nMode = 35 + 20/11 = 36.82. Mean = 30 + 43/8 = 35.38 years.\nBoxed Answer: [ Mode = 36.82 years, Mean = 35.38 years ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 187] Exercise 13.2 Q2: The following data gives the information on the observed lifetimes (in hours) of 225 electrical components: 0-20: 10; 20-40: 35; 40-60: 52; 60-80: 61; 80-100: 38; 100-120: 29. Determine the modal lifetimes of the components.",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 187,
            "image_search_query": "modal lifetime electrical components grouped mode",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Lifetimes of 225 components: 0-20: 10; 20-40: 35; 40-60: 52; 60-80: 61; 80-100: 38; 100-120: 29. Max frequency = 61 (Modal class 60-80).",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nwhere l = 60, h = 20, f1 = 61, f0 = 52, f2 = 38.",
            "substitution": "Mode = 60 + [ (61 - 52) / (2(61) - 52 - 38) ] × 20 = 60 + [ 9 / (122 - 90) ] × 20 = 60 + [ 9 / 32 ] × 20.",
            "calculation": "Mode = 60 + (9 × 5) / 8 = 60 + 45 / 8 = 60 + 5.625 = 65.625 hours.",
            "finalAnswer": "65.625 hours",
            "unit": "hours",
            "solution": "GIVEN:\nLifetimes of 225 electrical components:\n- 0-20: 10; 20-40: 35; 40-60: 52; 60-80: 61; 80-100: 38; 100-120: 29.\n\nTO FIND:\nModal lifetime of the components.\n\nFORMULA USED:\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Identify modal class:\nMaximum frequency is 61, corresponding to interval 60 - 80.\nTherefore, Modal Class = 60 - 80.\n\nStep 2: Extract parameters:\n- Lower limit, l = 60\n- Class width, h = 80 - 60 = 20\n- Frequency of modal class, f1 = 61\n- Frequency of preceding class, f0 = 52\n- Frequency of succeeding class, f2 = 38\n\nStep 3: Calculate Mode:\nMode = 60 + [ (61 - 52) / (2 × 61 - 52 - 38) ] × 20\nMode = 60 + [ 9 / (122 - 90) ] × 20\nMode = 60 + [ 9 / 32 ] × 20\nDivide 20 and 32 by 4:\nMode = 60 + [ 9 × 5 / 8 ] = 60 + (45 / 8)\nMode = 60 + 5.625 = 65.625 hours.\n\n[ROUGH_WORK]\n60 + 45/8 = 65.625 hours.\nBoxed Answer: [ 65.625 hours ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 188] Exercise 13.2 Q3: The following data gives the distribution of total monthly household expenditure of 200 families of a village. Find the modal monthly expenditure of the families. Also, find the mean monthly expenditure (1000-1500: 24; 1500-2000: 40; 2000-2500: 33; 2500-3000: 28; 3000-3500: 30; 3500-4000: 22; 4000-4500: 16; 4500-5000: 7).",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 188,
            "image_search_query": "monthly household expenditure modal mean calculation",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Monthly expenditure of 200 families: 1000-1500: 24; 1500-2000: 40; 2000-2500: 33; 2500-3000: 28; 3000-3500: 30; 3500-4000: 22; 4000-4500: 16; 4500-5000: 7. Σfi = 200. Max frequency = 40 (Modal class 1500-2000).",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h.\nMean x̄ = a + h × [(Σ fi ui) / (Σ fi)].",
            "substitution": "For Mode: l = 1500, h = 500, f1 = 40, f0 = 24, f2 = 33.\nMode = 1500 + [ (40 - 24) / (2(40) - 24 - 33) ] × 500 = 1500 + [ 16 / (80 - 57) ] × 500 = 1500 + 8000 / 23 = 1500 + 347.83 = ₹ 1847.83.\nFor Mean: a = 2750, h = 500, ui: -3, -2, -1, 0, 1, 2, 3, 4.\nΣ fi ui = 24(-3) + 40(-2) + 33(-1) + 28(0) + 30(1) + 22(2) + 16(3) + 7(4) = -185 + 150 = -35.\nMean = 2750 + 500 × (-35 / 200) = 2750 - 175 / 2 = 2750 - 87.5 = ₹ 2662.50.",
            "calculation": "Mode = ₹ 1847.83.\nMean = ₹ 2662.50.",
            "finalAnswer": "Modal expenditure = ₹ 1847.83, Mean expenditure = ₹ 2662.50",
            "unit": "rupees",
            "solution": "GIVEN:\nMonthly household expenditure of 200 families:\n- 1000-1500: 24; 1500-2000: 40; 2000-2500: 33; 2500-3000: 28; 3000-3500: 30; 3500-4000: 22; 4000-4500: 16; 4500-5000: 7.\nTotal families, Σfi = 200.\n\nTO FIND:\n(i) Modal monthly expenditure.\n(ii) Mean monthly expenditure.\n\nSTEP-BY-STEP CALCULATION:\nPart 1: Calculate Mode:\nModal class with highest frequency (40) is 1500 - 2000.\n- l = 1500, h = 500, f1 = 40, f0 = 24, f2 = 33\nMode = 1500 + [ (40 - 24) / (2 × 40 - 24 - 33) ] × 500\nMode = 1500 + [ 16 / (80 - 57) ] × 500\nMode = 1500 + (8000 / 23) = 1500 + 347.826... ≈ ₹ 1847.83.\n\nPart 2: Calculate Mean:\nChoose assumed mean a = 2750 and class width h = 500:\n- 1000-1500: xi = 1250; ui = -3; fi = 24; fi ui = -72\n- 1500-2000: xi = 1750; ui = -2; fi = 40; fi ui = -80\n- 2000-2500: xi = 2250; ui = -1; fi = 33; fi ui = -33\n- 2500-3000: xi = 2750; ui = 0; fi = 28; fi ui = 0\n- 3000-3500: xi = 3250; ui = 1; fi = 30; fi ui = 30\n- 3500-4000: xi = 3750; ui = 2; fi = 22; fi ui = 44\n- 4000-4500: xi = 4250; ui = 3; fi = 16; fi ui = 48\n- 4500-5000: xi = 4750; ui = 4; fi = 7; fi ui = 28\nΣ(fi ui) = -185 + 150 = -35\nx̄ = 2750 + 500 × [ -35 / 200 ]\nx̄ = 2750 - (175 / 2) = 2750 - 87.50 = ₹ 2662.50.\n\n[ROUGH_WORK]\nMode = 1500 + 347.83 = 1847.83. Mean = 2750 - 87.50 = 2662.50 rupees.\nBoxed Answer: [ Mode = ₹ 1847.83, Mean = ₹ 2662.50 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 188] Exercise 13.2 Q4: The following distribution gives the state-wise teacher-student ratio in higher secondary schools of India. Find the mode and mean of this data. Interpret the two measures (15-20: 3; 20-25: 8; 25-30: 9; 30-35: 10; 35-40: 3; 40-45: 0; 45-50: 0; 50-55: 2).",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 188,
            "image_search_query": "teacher student ratio state wise mode mean",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Teacher-student ratio across 35 States/UTs: 15-20: 3; 20-25: 8; 25-30: 9; 30-35: 10; 35-40: 3; 40-45: 0; 45-50: 0; 50-55: 2. Total Σfi = 35. Max frequency = 10 (Modal class 30-35).",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h.\nMean x̄ = a + h × [(Σ fi ui) / (Σ fi)].",
            "substitution": "For Mode: l = 30, h = 5, f1 = 10, f0 = 9, f2 = 3.\nMode = 30 + [ (10 - 9) / (2(10) - 9 - 3) ] × 5 = 30 + [ 1 / (20 - 12) ] × 5 = 30 + 5 / 8 = 30 + 0.625 = 30.63.\nFor Mean: a = 32.5, h = 5, ui: -3, -2, -1, 0, 1, 2, 3, 4.\nΣ fi ui = 3(-3) + 8(-2) + 9(-1) + 10(0) + 3(1) + 0 + 0 + 2(4) = -34 + 11 = -23.\nMean = 32.5 + 5 × (-23 / 35) = 32.5 - 23 / 7 = 32.5 - 3.286 = 29.21.",
            "calculation": "Mode = 30.63 students per teacher.\nMean = 29.21 students per teacher.",
            "finalAnswer": "Mode = 30.63, Mean = 29.21",
            "unit": "students/teacher",
            "solution": "GIVEN:\nState-wise teacher-student ratio across 35 states:\n- 15-20: 3; 20-25: 8; 25-30: 9; 30-35: 10; 35-40: 3; 40-45: 0; 45-50: 0; 50-55: 2.\nTotal states, Σfi = 35.\n\nTO FIND:\n(i) Mode of the data.\n(ii) Mean of the data.\n(iii) Interpretation.\n\nSTEP-BY-STEP CALCULATION:\nPart 1: Calculate Mode:\nModal class with highest frequency (10) is 30 - 35.\n- l = 30, h = 5, f1 = 10, f0 = 9, f2 = 3\nMode = 30 + [ (10 - 9) / (2 × 10 - 9 - 3) ] × 5\nMode = 30 + [ 1 / (20 - 12) ] × 5\nMode = 30 + (5 / 8) = 30 + 0.625 = 30.625 ≈ 30.63.\n\nPart 2: Calculate Mean:\nChoose assumed mean a = 32.5 and class width h = 5:\n- 15-20: xi = 17.5; ui = -3; fi = 3; fi ui = -9\n- 20-25: xi = 22.5; ui = -2; fi = 8; fi ui = -16\n- 25-30: xi = 27.5; ui = -1; fi = 9; fi ui = -9\n- 30-35: xi = 32.5; ui = 0; fi = 10; fi ui = 0\n- 35-40: xi = 37.5; ui = 1; fi = 3; fi ui = 3\n- 40-45: xi = 42.5; ui = 2; fi = 0; fi ui = 0\n- 45-50: xi = 47.5; ui = 3; fi = 0; fi ui = 0\n- 50-55: xi = 52.5; ui = 4; fi = 2; fi ui = 8\nΣ(fi ui) = -34 + 11 = -23\nx̄ = 32.5 + 5 × [ -23 / 35 ] = 32.5 - (23 / 7) = 32.5 - 3.2857... ≈ 29.21.\n\nPart 3: Interpretation:\n- Most states/UTs have a teacher-student ratio of approximately 30.6 students per teacher (Mode).\n- On average across all states, the ratio is 29.2 students per teacher (Mean).\n\n[ROUGH_WORK]\nMode = 30.63. Mean = 29.21.\nBoxed Answer: [ Mode = 30.63, Mean = 29.21 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 188] Exercise 13.2 Q5: The given distribution shows the number of runs scored by some top batsmen of the world in one-day international cricket matches: 3000-4000: 4; 4000-5000: 18; 5000-6000: 9; 6000-7000: 7; 7000-8000: 6; 8000-9000: 3; 9000-10000: 1; 10000-11000: 1. Find the mode of the data.",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 188,
            "image_search_query": "runs scored batsmen modal class mode calculation",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Runs scored by batsmen: 3000-4000: 4; 4000-5000: 18; 5000-6000: 9; 6000-7000: 7; 7000-8000: 6; 8000-9000: 3; 9000-10000: 1; 10000-11000: 1. Max frequency = 18 (Modal class 4000-5000).",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nwhere l = 4000, h = 1000, f1 = 18, f0 = 4, f2 = 9.",
            "substitution": "Mode = 4000 + [ (18 - 4) / (2(18) - 4 - 9) ] × 1000 = 4000 + [ 14 / (36 - 13) ] × 1000 = 4000 + 14000 / 23.",
            "calculation": "14000 / 23 = 608.695... Mode = 4000 + 608.70 = 4608.70 runs.",
            "finalAnswer": "4608.7 runs",
            "unit": "runs",
            "solution": "GIVEN:\nRuns scored by top international batsmen:\n- 3000-4000: 4; 4000-5000: 18; 5000-6000: 9; 6000-7000: 7; 7000-8000: 6; 8000-9000: 3; 9000-10000: 1; 10000-11000: 1.\n\nTO FIND:\nMode of the runs scored.\n\nFORMULA USED:\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Identify modal class:\nMaximum frequency is 18, which belongs to interval 4000 - 5000.\nTherefore, Modal Class = 4000 - 5000.\n\nStep 2: Extract parameters:\n- Lower limit, l = 4000\n- Class width, h = 1000\n- Frequency of modal class, f1 = 18\n- Frequency of preceding class, f0 = 4\n- Frequency of succeeding class, f2 = 9\n\nStep 3: Calculate Mode:\nMode = 4000 + [ (18 - 4) / (2 × 18 - 4 - 9) ] × 1000\nMode = 4000 + [ 14 / (36 - 13) ] × 1000\nMode = 4000 + [ 14 / 23 ] × 1000\nMode = 4000 + (14000 / 23) = 4000 + 608.695... ≈ 4608.7 runs.\n\n[ROUGH_WORK]\n14000 / 23 = 608.695. 4000 + 608.7 = 4608.7 runs.\nBoxed Answer: [ 4608.7 runs ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.3 | Page 188] Exercise 13.2 Q6: A student noted the number of cars passing through a spot on a road for 100 periods each of 3 minutes and summarised it in the table given below. Find the mode of the data (0-10: 7; 10-20: 14; 20-30: 13; 30-40: 12; 40-50: 20; 50-60: 11; 60-70: 15; 70-80: 8).",
            "section": "13.3 Mode of Grouped Data",
            "page_number": 188,
            "image_search_query": "number of cars passing spot modal class mode",
            "has_diagram": True,
            "diagram_svg": svg_histogram,
            "given": "Cars passing spot for 100 periods: 0-10: 7; 10-20: 14; 20-30: 13; 30-40: 12; 40-50: 20; 50-60: 11; 60-70: 15; 70-80: 8. Max frequency = 20 (Modal class 40-50).",
            "formula": "Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\nwhere l = 40, h = 10, f1 = 20, f0 = 12, f2 = 11.",
            "substitution": "Mode = 40 + [ (20 - 12) / (2(20) - 12 - 11) ] × 10 = 40 + [ 8 / (40 - 23) ] × 10 = 40 + 80 / 17.",
            "calculation": "80 / 17 = 4.706... Mode = 40 + 4.71 = 44.71 cars.",
            "finalAnswer": "44.7 cars",
            "unit": "cars",
            "solution": "GIVEN:\nDistribution of cars passing in 100 intervals:\n- 0-10: 7; 10-20: 14; 20-30: 13; 30-40: 12; 40-50: 20; 50-60: 11; 60-70: 15; 70-80: 8.\nTotal periods = 100.\n\nTO FIND:\nMode of the number of cars.\n\nFORMULA USED:\nMode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Identify modal class:\nMaximum frequency is 20, corresponding to interval 40 - 50.\nTherefore, Modal Class = 40 - 50.\n\nStep 2: Extract parameters:\n- Lower limit, l = 40\n- Class width, h = 10\n- Frequency of modal class, f1 = 20\n- Frequency of preceding class, f0 = 12\n- Frequency of succeeding class, f2 = 11\n\nStep 3: Calculate Mode:\nMode = 40 + [ (20 - 12) / (2 × 20 - 12 - 11) ] × 10\nMode = 40 + [ 8 / (40 - 23) ] × 10\nMode = 40 + [ 8 / 17 ] × 10\nMode = 40 + (80 / 17) = 40 + 4.7058... ≈ 44.7 cars.\n\n[ROUGH_WORK]\n80 / 17 = 4.7058 ≈ 4.71. Mode = 44.71 cars.\nBoxed Answer: [ 44.7 cars ].",
            "concept_questions": []
        }
    ]

    m6_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 195] Exercise 13.3 Q1: The following frequency distribution gives the monthly consumption of electricity of 68 consumers of a locality. Find the median, mean and mode of the data and compare them (65-85: 4; 85-105: 5; 105-125: 13; 125-145: 20; 145-165: 14; 165-185: 8; 185-205: 4).",
            "section": "13.4 Median of Grouped Data",
            "page_number": 195,
            "image_search_query": "monthly electricity consumption median mean mode comparison",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Monthly consumption of 68 consumers: 65-85: 4; 85-105: 5; 105-125: 13; 125-145: 20; 145-165: 14; 165-185: 8; 185-205: 4. Total N = 68.",
            "formula": "1. Median = l + [ (N/2 - cf) / f ] × h\n2. Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h\n3. Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)].",
            "substitution": "Cumulative frequencies cf: 4, 9, 22, 42, 56, 64, 68. N/2 = 34 ⇒ Median Class = 125-145 (l=125, cf=22, f=20, h=20).\nMedian = 125 + [ (34 - 22) / 20 ] × 20 = 125 + 12 = 137 units.\nMode: Modal class = 125-145 (f1=20, f0=13, f2=14, l=125, h=20).\nMode = 125 + [ (20 - 13) / (40 - 13 - 14) ] × 20 = 125 + [ 7 / 13 ] × 20 = 125 + 140 / 13 = 125 + 10.77 = 135.77 units.\nMean: a = 135, h = 20, ui: -3, -2, -1, 0, 1, 2, 3.\nΣ fi ui = 4(-3) + 5(-2) + 13(-1) + 20(0) + 14(1) + 8(2) + 4(3) = -35 + 42 = 7.\nMean = 135 + 20 × (7 / 68) = 135 + 140 / 68 = 135 + 2.06 = 137.06 units.",
            "calculation": "Median = 137 units.\nMean = 137.06 units.\nMode = 135.77 units.",
            "finalAnswer": "Median = 137 units, Mean = 137.06 units, Mode = 135.77 units",
            "unit": "units",
            "solution": "GIVEN:\nMonthly electricity consumption of 68 consumers:\n- 65-85: 4; 85-105: 5; 105-125: 13; 125-145: 20; 145-165: 14; 165-185: 8; 185-205: 4.\nTotal consumers, N = 68.\n\nTO FIND:\n(i) Median, (ii) Mean, (iii) Mode, (iv) Comparison.\n\nSTEP-BY-STEP CALCULATION:\nPart 1: Calculate Median:\nCumulative frequencies: 4, 9, 22, 42, 56, 64, 68.\nN / 2 = 68 / 2 = 34.\nThe cf just greater than 34 is 42, corresponding to Median Class = 125 - 145.\n- l = 125, cf = 22, f = 20, h = 20\nMedian = 125 + [ (34 - 22) / 20 ] × 20\nMedian = 125 + 12 = 137 units.\n\nPart 2: Calculate Mode:\nModal class with highest frequency (20) is 125 - 145.\n- l = 125, h = 20, f1 = 20, f0 = 13, f2 = 14\nMode = 125 + [ (20 - 13) / (2 × 20 - 13 - 14) ] × 20\nMode = 125 + [ 7 / (40 - 27) ] × 20\nMode = 125 + (140 / 13) = 125 + 10.769... ≈ 135.77 units.\n\nPart 3: Calculate Mean:\nChoose a = 135, h = 20:\nΣ(fi ui) = 4(-3) + 5(-2) + 13(-1) + 20(0) + 14(1) + 8(2) + 4(3) = -35 + 42 = 7\nMean = 135 + 20 × (7 / 68) = 135 + 140 / 68 = 135 + 2.058... ≈ 137.06 units.\n\nPart 4: Comparison:\nAll three measures of central tendency are approximately equal (Median = 137, Mean = 137.06, Mode = 135.77), indicating an almost symmetric bell-shaped distribution.\n\n[ROUGH_WORK]\nMedian = 137. Mode = 135.77. Mean = 137.06.\nBoxed Answer: [ Median = 137, Mean = 137.06, Mode = 135.77 units ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 196] Exercise 13.3 Q2: If the median of the distribution given below is 28.5, find the values of x and y (Total frequency = 60; 0-10: 5; 10-20: x; 20-30: 20; 30-40: 15; 40-50: y; 50-60: 5).",
            "section": "13.4 Median of Grouped Data",
            "page_number": 196,
            "image_search_query": "median missing frequencies x y distribution 28.5",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Median = 28.5. Total frequency N = 60. Missing frequencies x and y in classes 10-20 and 40-50.",
            "formula": "Median = l + [ (N/2 - cf) / f ] × h. Total frequency Σfi = N = 60.",
            "substitution": "Cumulative frequencies cf: 5, 5+x, 25+x, 40+x, 40+x+y, 45+x+y.\nTotal frequency equation: 45 + x + y = 60 ⇒ x + y = 15 ... (1).\nMedian = 28.5 lies in interval 20-30 (Median Class):\nl = 20, h = 10, f = 20, cf = 5 + x, N/2 = 30.\n28.5 = 20 + [ (30 - (5 + x)) / 20 ] × 10.",
            "calculation": "8.5 = [ (25 - x) / 20 ] × 10 = (25 - x) / 2\n17 = 25 - x ⇒ x = 25 - 17 = 8.\nFrom (1): 8 + y = 15 ⇒ y = 7.",
            "finalAnswer": "x = 8, y = 7",
            "unit": "frequencies",
            "solution": "GIVEN:\nMedian = 28.5.\nTotal frequency, N = 60.\nDistribution with unknown frequencies x and y:\n- 0-10: 5; 10-20: x; 20-30: 20; 30-40: 15; 40-50: y; 50-60: 5.\n\nTO FIND:\nValues of missing frequencies x and y.\n\nFORMULA USED:\n1. Total frequency: Σfi = 60\n2. Median = l + [ (N/2 - cf) / f ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Set up the cumulative frequency table:\n- 0 - 10: fi = 5; cf = 5\n- 10 - 20: fi = x; cf = 5 + x\n- 20 - 30: fi = 20; cf = 25 + x\n- 30 - 40: fi = 15; cf = 40 + x\n- 40 - 50: fi = y; cf = 40 + x + y\n- 50 - 60: fi = 5; cf = 45 + x + y\n\nStep 2: Relate total frequency:\n45 + x + y = 60\nx + y = 60 - 45\nx + y = 15   ... (1)\n\nStep 3: Determine Median Class and solve for x:\nSince Median = 28.5, it lies in the interval 20 - 30.\nTherefore, Median Class = 20 - 30.\nParameters:\n- Lower limit, l = 20\n- Class width, h = 10\n- Frequency of median class, f = 20\n- cf of preceding class = 5 + x\n- N / 2 = 60 / 2 = 30\n\nApply the median formula:\n28.5 = 20 + [ (30 - (5 + x)) / 20 ] × 10\n28.5 - 20 = [ (25 - x) / 2 ]\n8.5 = (25 - x) / 2\nMultiply both sides by 2:\n17 = 25 - x\nx = 25 - 17 = 8.\n\nStep 4: Solve for y using equation (1):\nx + y = 15\n8 + y = 15\ny = 15 - 8 = 7.\n\n[ROUGH_WORK]\nx = 8, y = 7. Sum = 45 + 8 + 7 = 60. Check median: 20 + ((30 - 13)/20) × 10 = 20 + 17/2 = 20 + 8.5 = 28.5. Perfect!\nBoxed Answer: [ x = 8, y = 7 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 196] Exercise 13.3 Q3: A life insurance agent found the following data for distribution of ages of 100 policy holders. Calculate the median age, if policies are given only to persons having age 18 years onwards but less than 60 year: Below 20: 2; Below 25: 6; Below 30: 24; Below 35: 45; Below 40: 78; Below 45: 89; Below 50: 92; Below 55: 98; Below 60: 100.",
            "section": "13.4 Median of Grouped Data",
            "page_number": 196,
            "image_search_query": "life insurance policy holders median age cumulative frequency",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Cumulative data of 100 policy holders: Below 20: 2; Below 25: 6; Below 30: 24; Below 35: 45; Below 40: 78; Below 45: 89; Below 50: 92; Below 55: 98; Below 60: 100. Total N = 100.",
            "formula": "Median = l + [ (N/2 - cf) / f ] × h.",
            "substitution": "Convert to standard class intervals:\n15-20 (or 18-20): fi = 2 (cf = 2)\n20-25: fi = 6 - 2 = 4 (cf = 6)\n25-30: fi = 24 - 6 = 18 (cf = 24)\n30-35: fi = 45 - 24 = 21 (cf = 45)\n35-40: fi = 78 - 45 = 33 (cf = 78) ⇒ Median class since cf=78 > 50!\n40-45: fi = 89 - 78 = 11 (cf = 89)\n45-50: fi = 92 - 89 = 3 (cf = 92)\n50-55: fi = 98 - 92 = 6 (cf = 98)\n55-60: fi = 100 - 98 = 2 (cf = 100)\nFor Median Class 35-40: l = 35, h = 5, f = 33, cf = 45, N/2 = 50.",
            "calculation": "Median = 35 + [ (50 - 45) / 33 ] × 5 = 35 + (5 × 5) / 33 = 35 + 25 / 33 = 35 + 0.758 = 35.76 years.",
            "finalAnswer": "35.76 years",
            "unit": "years",
            "solution": "GIVEN:\nCumulative distribution ('below' type) for ages of 100 policy holders:\n- Below 20: 2; Below 25: 6; Below 30: 24; Below 35: 45; Below 40: 78; Below 45: 89; Below 50: 92; Below 55: 98; Below 60: 100.\nTotal policy holders, N = 100.\n\nTO FIND:\nMedian age of the policy holders.\n\nFORMULA USED:\nMedian = l + [ (N/2 - cf) / f ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Convert cumulative data to class intervals and individual frequencies:\n- 15 - 20: fi = 2; cf = 2\n- 20 - 25: fi = 6 - 2 = 4; cf = 6\n- 25 - 30: fi = 24 - 6 = 18; cf = 24\n- 30 - 35: fi = 45 - 24 = 21; cf = 45\n- 35 - 40: fi = 78 - 45 = 33; cf = 78\n- 40 - 45: fi = 89 - 78 = 11; cf = 89\n- 45 - 50: fi = 92 - 89 = 3; cf = 92\n- 50 - 55: fi = 98 - 92 = 6; cf = 98\n- 55 - 60: fi = 100 - 98 = 2; cf = 100\n\nStep 2: Identify Median Class:\nN / 2 = 100 / 2 = 50.\nThe cf just greater than 50 is 78, corresponding to Median Class = 35 - 40.\n\nStep 3: Extract parameters:\n- Lower limit, l = 35\n- Class width, h = 5\n- Frequency of median class, f = 33\n- Preceding cumulative frequency, cf = 45\n\nStep 4: Compute Median:\nMedian = 35 + [ (50 - 45) / 33 ] × 5\nMedian = 35 + [ 5 / 33 ] × 5\nMedian = 35 + (25 / 33) = 35 + 0.7575... ≈ 35.76 years.\n\n[ROUGH_WORK]\n25 / 33 = 0.7576. 35 + 0.76 = 35.76 years.\nBoxed Answer: [ 35.76 years ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 196] Exercise 13.3 Q4: The lengths of 40 leaves of a plant are measured correct to the nearest millimetre, and the data obtained is represented in the following table: 118-126: 3; 127-135: 5; 136-144: 9; 145-153: 12; 154-162: 5; 163-171: 4; 172-180: 2. Find the median length of the leaves (Hint: The data needs to be converted to continuous classes for finding the median, since the formula assumes continuous classes).",
            "section": "13.4 Median of Grouped Data",
            "page_number": 196,
            "image_search_query": "plant leaves continuous boundary median formula",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Lengths of 40 leaves in discontinuous intervals: 118-126: 3; 127-135: 5; 136-144: 9; 145-153: 12; 154-162: 5; 163-171: 4; 172-180: 2. Total N = 40.",
            "formula": "Convert to continuous classes: 117.5-126.5, 126.5-135.5, 135.5-144.5, 144.5-153.5, 153.5-162.5, 162.5-171.5, 171.5-180.5 (class width h = 9).\nMedian = l + [ (N/2 - cf) / f ] × h.",
            "substitution": "Cumulative frequencies cf: 3, 8, 17, 29, 34, 38, 40.\nN/2 = 40/2 = 20 ⇒ Median Class = 144.5 - 153.5 (cf = 29 > 20).\nParameters: l = 144.5, h = 9, f = 12, cf = 17.\nMedian = 144.5 + [ (20 - 17) / 12 ] × 9 = 144.5 + [ 3 / 12 ] × 9 = 144.5 + (1/4) × 9 = 144.5 + 2.25.",
            "calculation": "Median = 144.5 + 2.25 = 146.75 mm.",
            "finalAnswer": "146.75 mm",
            "unit": "mm",
            "solution": "GIVEN:\nLengths of 40 leaves:\n- 118-126: 3; 127-135: 5; 136-144: 9; 145-153: 12; 154-162: 5; 163-171: 4; 172-180: 2.\nTotal leaves, N = 40.\n\nTO FIND:\nMedian length of the leaves.\n\nFORMULA USED:\nMedian = l + [ (N/2 - cf) / f ] × h\nNote: Convert discontinuous classes to continuous classes by subtracting 0.5 from lower limits and adding 0.5 to upper limits.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Convert to continuous intervals and compute cumulative frequency:\n- 117.5 - 126.5: fi = 3; cf = 3\n- 126.5 - 135.5: fi = 5; cf = 8\n- 135.5 - 144.5: fi = 9; cf = 17\n- 144.5 - 153.5: fi = 12; cf = 29\n- 153.5 - 162.5: fi = 5; cf = 34\n- 162.5 - 171.5: fi = 4; cf = 38\n- 171.5 - 180.5: fi = 2; cf = 40\n\nStep 2: Determine Median Class:\nN / 2 = 40 / 2 = 20.\nThe cumulative frequency just greater than 20 is 29, corresponding to Median Class = 144.5 - 153.5.\n\nStep 3: Extract parameters:\n- Lower limit, l = 144.5\n- Class width, h = 153.5 - 144.5 = 9\n- Frequency of median class, f = 12\n- cf of preceding class = 17\n\nStep 4: Compute Median:\nMedian = 144.5 + [ (20 - 17) / 12 ] × 9\nMedian = 144.5 + [ 3 / 12 ] × 9\nMedian = 144.5 + (1 / 4) × 9\nMedian = 144.5 + 2.25 = 146.75 mm.\n\n[ROUGH_WORK]\n144.5 + 2.25 = 146.75 mm.\nBoxed Answer: [ 146.75 mm ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 197] Exercise 13.3 Q5: The following table gives the distribution of the life time of 400 neon lamps: 1500-2000: 14; 2000-2500: 56; 2500-3000: 60; 3000-3500: 86; 3500-4000: 74; 4000-4500: 62; 4500-5000: 48. Find the median life time of a lamp.",
            "section": "13.4 Median of Grouped Data",
            "page_number": 197,
            "image_search_query": "neon lamps lifetime median grouped data",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Lifetimes of 400 neon lamps: 1500-2000: 14; 2000-2500: 56; 2500-3000: 60; 3000-3500: 86; 3500-4000: 74; 4000-4500: 62; 4500-5000: 48. Total N = 400.",
            "formula": "Median = l + [ (N/2 - cf) / f ] × h.",
            "substitution": "Cumulative frequencies cf: 14, 70, 130, 216, 290, 352, 400.\nN/2 = 400/2 = 200 ⇒ Median Class = 3000 - 3500 (cf = 216 > 200).\nParameters: l = 3000, h = 500, f = 86, cf = 130.\nMedian = 3000 + [ (200 - 130) / 86 ] × 500 = 3000 + [ 70 / 86 ] × 500 = 3000 + 35000 / 86 = 3000 + 17500 / 43.",
            "calculation": "17500 / 43 = 406.9767... Median = 3000 + 406.98 = 3406.98 hours.",
            "finalAnswer": "3406.98 hours",
            "unit": "hours",
            "solution": "GIVEN:\nLifetimes of 400 neon lamps:\n- 1500-2000: 14; 2000-2500: 56; 2500-3000: 60; 3000-3500: 86; 3500-4000: 74; 4000-4500: 62; 4500-5000: 48.\nTotal lamps, N = 400.\n\nTO FIND:\nMedian lifetime of a neon lamp.\n\nFORMULA USED:\nMedian = l + [ (N/2 - cf) / f ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute cumulative frequencies (cf):\n- 1500 - 2000: fi = 14; cf = 14\n- 2000 - 2500: fi = 56; cf = 70\n- 2500 - 3000: fi = 60; cf = 130\n- 3000 - 3500: fi = 86; cf = 216\n- 3500 - 4000: fi = 74; cf = 290\n- 4000 - 4500: fi = 62; cf = 352\n- 4500 - 5000: fi = 48; cf = 400\n\nStep 2: Determine Median Class:\nN / 2 = 400 / 2 = 200.\nThe cumulative frequency just greater than 200 is 216, corresponding to Median Class = 3000 - 3500.\n\nStep 3: Extract parameters:\n- Lower limit, l = 3000\n- Class width, h = 500\n- Frequency of median class, f = 86\n- cf of preceding class = 130\n\nStep 4: Compute Median:\nMedian = 3000 + [ (200 - 130) / 86 ] × 500\nMedian = 3000 + [ 70 / 86 ] × 500\nMedian = 3000 + (35000 / 86) = 3000 + (17500 / 43)\nMedian = 3000 + 406.9767... ≈ 3406.98 hours.\n\n[ROUGH_WORK]\n35000 / 86 = 406.98. 3000 + 406.98 = 3406.98 hours.\nBoxed Answer: [ 3406.98 hours ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 197] Exercise 13.3 Q6: 100 surnames were randomly picked up from a local telephone directory and the frequency distribution of the number of letters in the English alphabets in the surnames was obtained as follows: 1-4: 6; 4-7: 30; 7-10: 40; 10-13: 16; 13-16: 4; 16-19: 4. Determine the median number of letters in the surnames. Find the mean number of letters in the surnames? Also, find the modal size of the surnames.",
            "section": "13.4 Median of Grouped Data",
            "page_number": 197,
            "image_search_query": "surnames letters median mean modal size",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Surnames distribution: 1-4: 6; 4-7: 30; 7-10: 40; 10-13: 16; 13-16: 4; 16-19: 4. Total N = 100.",
            "formula": "1. Median = l + [ (N/2 - cf) / f ] × h\n2. Mean x̄ = a + h × [(Σ fi ui) / (Σ fi)]\n3. Mode = l + [ (f1 - f0) / (2f1 - f0 - f2) ] × h.",
            "substitution": "Cumulative frequencies cf: 6, 36, 76, 92, 96, 100. N/2 = 50 ⇒ Median Class = 7-10 (l=7, h=3, f=40, cf=36).\nMedian = 7 + [ (50 - 36) / 40 ] × 3 = 7 + [ 14 / 40 ] × 3 = 7 + 42 / 40 = 7 + 1.05 = 8.05 letters.\nModal class: highest frequency = 40 ⇒ 7-10 (l=7, h=3, f1=40, f0=30, f2=16).\nMode = 7 + [ (40 - 30) / (2(40) - 30 - 16) ] × 3 = 7 + [ 10 / (80 - 46) ] × 3 = 7 + 30 / 34 = 7 + 0.88 = 7.88 letters.\nMean: a = 8.5, h = 3, ui: -2, -1, 0, 1, 2, 3.\nΣ fi ui = 6(-2) + 30(-1) + 40(0) + 16(1) + 4(2) + 4(3) = -42 + 36 = -6.\nMean = 8.5 + 3 × (-6 / 100) = 8.5 - 0.18 = 8.32 letters.",
            "calculation": "Median = 8.05 letters.\nMean = 8.32 letters.\nMode = 7.88 letters.",
            "finalAnswer": "Median = 8.05 letters, Mean = 8.32 letters, Mode = 7.88 letters",
            "unit": "letters",
            "solution": "GIVEN:\nDistribution of number of letters in 100 surnames:\n- 1-4: 6; 4-7: 30; 7-10: 40; 10-13: 16; 13-16: 4; 16-19: 4.\nTotal surnames, N = 100.\n\nTO FIND:\n(i) Median number of letters, (ii) Mean number of letters, (iii) Modal size.\n\nSTEP-BY-STEP CALCULATION:\nPart 1: Calculate Median:\ncf: 6, 36, 76, 92, 96, 100.\nN / 2 = 100 / 2 = 50.\nThe cf just greater than 50 is 76, corresponding to Median Class = 7 - 10.\n- l = 7, h = 3, f = 40, cf = 36\nMedian = 7 + [ (50 - 36) / 40 ] × 3\nMedian = 7 + [ 14 / 40 ] × 3 = 7 + (42 / 40) = 7 + 1.05 = 8.05 letters.\n\nPart 2: Calculate Mode:\nModal class with highest frequency (40) is 7 - 10.\n- l = 7, h = 3, f1 = 40, f0 = 30, f2 = 16\nMode = 7 + [ (40 - 30) / (2 × 40 - 30 - 16) ] × 3\nMode = 7 + [ 10 / (80 - 46) ] × 3\nMode = 7 + (30 / 34) = 7 + 0.882... ≈ 7.88 letters.\n\nPart 3: Calculate Mean:\nChoose a = 8.5, h = 3:\n- 1-4: xi = 2.5; ui = -2; fi = 6; fi ui = -12\n- 4-7: xi = 5.5; ui = -1; fi = 30; fi ui = -30\n- 7-10: xi = 8.5; ui = 0; fi = 40; fi ui = 0\n- 10-13: xi = 11.5; ui = 1; fi = 16; fi ui = 16\n- 13-16: xi = 14.5; ui = 2; fi = 4; fi ui = 8\n- 16-19: xi = 17.5; ui = 3; fi = 4; fi ui = 12\nΣ(fi ui) = -42 + 36 = -6\nMean = 8.5 + 3 × [ -6 / 100 ] = 8.5 - 0.18 = 8.32 letters.\n\n[ROUGH_WORK]\nMedian = 8.05. Mean = 8.32. Mode = 7.88.\nBoxed Answer: [ Median = 8.05, Mean = 8.32, Mode = 7.88 letters ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 13 | Section 13.4 | Page 197] Exercise 13.3 Q7: The distribution below gives the weights of 30 students of a class. Find the median weight of the students (40-45: 2; 45-50: 3; 50-55: 8; 55-60: 6; 60-65: 6; 65-70: 3; 70-75: 2).",
            "section": "13.4 Median of Grouped Data",
            "page_number": 197,
            "image_search_query": "weights 30 students median grouped data",
            "has_diagram": True,
            "diagram_svg": svg_ogive,
            "given": "Weights of 30 students: 40-45: 2; 45-50: 3; 50-55: 8; 55-60: 6; 60-65: 6; 65-70: 3; 70-75: 2. Total N = 30.",
            "formula": "Median = l + [ (N/2 - cf) / f ] × h.",
            "substitution": "Cumulative frequencies cf: 2, 5, 13, 19, 25, 28, 30.\nN/2 = 30/2 = 15 ⇒ Median Class = 55 - 60 (cf = 19 > 15).\nParameters: l = 55, h = 5, f = 6, cf = 13.\nMedian = 55 + [ (15 - 13) / 6 ] × 5 = 55 + [ 2 / 6 ] × 5 = 55 + 5 / 3 = 55 + 1.67.",
            "calculation": "Median = 55 + 1.67 = 56.67 kg.",
            "finalAnswer": "56.67 kg",
            "unit": "kg",
            "solution": "GIVEN:\nWeights of 30 students:\n- 40-45: 2; 45-50: 3; 50-55: 8; 55-60: 6; 60-65: 6; 65-70: 3; 70-75: 2.\nTotal students, N = 30.\n\nTO FIND:\nMedian weight of the students.\n\nFORMULA USED:\nMedian = l + [ (N/2 - cf) / f ] × h\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute cumulative frequencies (cf):\n- 40 - 45: fi = 2; cf = 2\n- 45 - 50: fi = 3; cf = 5\n- 50 - 55: fi = 8; cf = 13\n- 55 - 60: fi = 6; cf = 19\n- 60 - 65: fi = 6; cf = 25\n- 65 - 70: fi = 3; cf = 28\n- 70 - 75: fi = 2; cf = 30\n\nStep 2: Determine Median Class:\nN / 2 = 30 / 2 = 15.\nThe cf just greater than 15 is 19, corresponding to Median Class = 55 - 60.\n\nStep 3: Extract parameters:\n- Lower limit, l = 55\n- Class width, h = 5\n- Frequency of median class, f = 6\n- cf of preceding class = 13\n\nStep 4: Compute Median:\nMedian = 55 + [ (15 - 13) / 6 ] × 5\nMedian = 55 + [ 2 / 6 ] × 5\nMedian = 55 + (1 / 3) × 5\nMedian = 55 + (5 / 3) = 55 + 1.666... ≈ 56.67 kg.\n\n[ROUGH_WORK]\n55 + 1.67 = 56.67 kg.\nBoxed Answer: [ 56.67 kg ].",
            "concept_questions": []
        }
    ]

    # Load existing module metadata
    with open("scripts/maths_class10_modules/ch13_statistics.json", "r", encoding="utf-8") as f:
        modules = json.load(f)

    modules[0]["worked_examples"] = m1_worked_examples
    modules[1]["worked_examples"] = m2_worked_examples
    modules[2]["worked_examples"] = m3_worked_examples
    modules[3]["worked_examples"] = m4_worked_examples
    modules[4]["worked_examples"] = m5_worked_examples
    modules[5]["worked_examples"] = m6_worked_examples

    return modules

if __name__ == "__main__":
    mods = get_ch13_complete_modules()
    out_file = "scripts/maths_class10_modules/ch13_statistics.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2, ensure_ascii=False)
    
    total_we = sum(len(m["worked_examples"]) for m in mods)
    print(f"Ch 13 complete: {len(mods)} modules, {total_we} worked examples saved to {out_file}.")
