import json

with open('scripts/maths_pt2_modules/ch10_understanding_data.json', 'r', encoding='utf-8') as f:
    modules = json.load(f)

# Module 1: Add Exercise Set 10.1 (Q1 to Q5)
we_ex_10_1 = {
    "problem": "Chapter 10, Exercise Set 10.1 (Ganita Manjari Part 2, Section 10.1, p. 13):\n(i) Question 1: The average score of students on a test in Section A is 72 and that of Section B is 76. Section A has 30 students and Section B has 25 students. Find the combined average.\n(ii) Question 2: A farmer mixes three equal quantities of fertilisers containing 1/10, 9/50, and 3/60 nitrogen respectively. Find the fraction of nitrogen in the mixture.\n(iii) Question 3: (Śrīdharācārya, Pāṭīgaṇita, c. 750 CE) A goldsmith melts together three pieces of gold: 9 units at 12 varṇa, 5 units at 10 varṇa, and 17 units at 11 varṇa. Find the purity in varṇa of the combined gold.\n(iv) Question 4: The average daily rainfall in May (31 days), June (30 days), and July (31 days) are 3.5 mm, 10 mm, and 8.7 mm respectively. Write an expression for the combined average daily rainfall.\n(v) Question 5: Calculate the concentration of spice mix when: (a) 100 mL (5%), 200 mL (10%), 300 mL (15%) are mixed; (b) 300 mL (5%), 200 mL (10%), 100 mL (15%) are mixed.",
    "solution": """GIVEN:
(i) Section A: n₁ = 30 students, x̄₁ = 72; Section B: n₂ = 25 students, x̄₂ = 76.
(ii) Three equal volumes (V₁ = V₂ = V₃ = V) of fertiliser with nitrogen fractions f₁ = 1/10, f₂ = 9/50, f₃ = 3/60 = 1/20.
(iii) Gold pieces: w₁ = 9 units at x₁ = 12 varṇa, w₂ = 5 units at x₂ = 10 varṇa, w₃ = 17 units at x₃ = 11 varṇa.
(iv) Days: d₁ = 31 (May), d₂ = 30 (June), d₃ = 31 (July); Daily rainfall: r₁ = 3.5 mm, r₂ = 10 mm, r₃ = 8.7 mm.
(v) Kadha mixes: Scenario (a) V₁ = 100 mL (5%), V₂ = 200 mL (10%), V₃ = 300 mL (15%); Scenario (b) V₁ = 300 mL (5%), V₂ = 200 mL (10%), V₃ = 100 mL (15%).

TO FIND / TO PROVE:
(i) Combined class average test score.
(ii) Nitrogen fraction in the fertilizer mixture.
(iii) Overall gold purity in varṇa.
(iv) Expression and value for 3-month combined average daily rainfall.
(v) Final spice mix percentage in scenarios (a) and (b).

FORMULA USED:
1. Weighted Arithmetic Mean:
   x̄ = (w₁x₁ + w₂x₂ + ... + wₖxₖ) / (w₁ + w₂ + ... + wₖ)
2. Mixture Concentration:
   C_mix = (V₁C₁ + V₂C₂ + ... + VₖCₖ) / (V₁ + V₂ + ... + Vₖ)

STEP-BY-STEP CALCULATION:
Part (i):
Total score = n₁x̄₁ + n₂x̄₂ = 30 × 72 + 25 × 76 = 2160 + 1900 = 4060.
Total students = 30 + 25 = 55.
Combined Average x̄ = 4060 / 55 = 812 / 11 ≈ 73.82.

Part (ii):
Since equal quantities V are mixed, weights are equal (w₁ = w₂ = w₃ = 1):
f_mix = (1/10 + 9/50 + 3/60) / 3 = (1/10 + 9/50 + 1/20) / 3
LCM of denominators (10, 50, 20) = 100:
1/10 = 10/100, 9/50 = 18/100, 1/20 = 5/100.
Sum = (10 + 18 + 5) / 100 = 33/100.
f_mix = (33/100) / 3 = 11/100 = 0.11 (or 11%).

Part (iii):
Total purity value = w₁x₁ + w₂x₂ + w₃x₃ = 9 × 12 + 5 × 10 + 17 × 11 = 108 + 50 + 187 = 345.
Total weight = 9 + 5 + 17 = 31 units.
Combined purity = 345 / 31 ≈ 11.129 varṇa ≈ 11.13 varṇa.

Part (iv):
Total rainfall = 31 × 3.5 + 30 × 10 + 31 × 8.7 mm.
Total days = 31 + 30 + 31 = 92 days.
Expression = (31 × 3.5 + 30 × 10 + 31 × 8.7) / (31 + 30 + 31)
Calculation = (108.5 + 300 + 269.7) / 92 = 678.2 / 92 ≈ 7.37 mm/day.

Part (v):
Scenario (a):
Total spice = 100 × 0.05 + 200 × 0.10 + 300 × 0.15 = 5 + 20 + 45 = 70 mL.
Total volume = 100 + 200 + 300 = 600 mL.
Concentration C_a = (70 / 600) × 100% = 70/6% ≈ 11.67%.

Scenario (b):
Total spice = 300 × 0.05 + 200 × 0.10 + 100 × 0.15 = 15 + 20 + 15 = 50 mL.
Total volume = 300 + 200 + 100 = 600 mL.
Concentration C_b = (50 / 600) × 100% = 50/6% ≈ 8.33%.

[ROUGH_WORK]
4060 / 55 = 73.8181...
345 / 31: 31 × 11 = 341, remainder 4, 4/31 ≈ 0.129.
678.2 / 92 = 7.3717... mm.
70 / 6 = 11.666...%
50 / 6 = 8.333...%

Boxed Answer:
[ (i) Combined Average = 73.82, (ii) Nitrogen Fraction = 11/100 (11%), (iii) Gold Purity = 11.13 varṇa, (iv) Rainfall = (31 × 3.5 + 30 × 10 + 31 × 8.7)/92 ≈ 7.37 mm/day, (v) Concentration (a) = 11.67%, Concentration (b) = 8.33% ]"""
}
modules[0]['worked_examples'].append(we_ex_10_1)

# Module 2: Add Example 3 and Exercise Sets 10.2 & 10.3
we_m2_extra = {
    "problem": "Chapter 10, Example 3 & Exercise Sets 10.2 & 10.3 (Ganita Manjari Part 2, pp. 11–15):\n(i) Example 3 (NCERT p. 11): Two glasses of equal quantities of lemonade are mixed. One has 10% jaggery, the other has 20% jaggery. Find the concentration of the mixture.\n(ii) Exercise Set 10.2, Q1 (p. 14): Savitri's marks in Kashmiri: 35/50 in internals, 44/60 in project, 80/100 in final exam. Weights are in ratio 3 : 4 : 5. Identify the correct expressions for her annual percentage score.\n(iii) Exercise Set 10.3, Q1 (p. 15): A stationery shop owner made ₹8000 selling books (30% profit) and ₹1000 selling book covers (50% profit). Find the overall percentage profit on total sales.\n(iv) Exercise Set 10.3, Q2 (p. 15): A white stork's average daily migration distance over 20 days was 44.5 km. On the 21st day it flew 55 km. Find the combined average daily distance over all 21 days.",
    "solution": """GIVEN:
(i) Equal volumes V of 10% and 20% jaggery lemonade.
(ii) Internals = 35/50 (70%), Project = 44/60 (73.33%), Final = 80/100 (80%); Weights w₁ = 3, w₂ = 4, w₃ = 5.
(iii) Sales: Book sales = ₹8000 with profit 30%; Cover sales = ₹1000 with profit 50%.
(iv) n₁ = 20 days, x̄₁ = 44.5 km/day; day 21 distance x₂₁ = 55 km.

TO FIND / TO PROVE:
(i) Final jaggery concentration in mixed lemonade.
(ii) Correct mathematical expressions for Savitri's annual percentage score.
(iii) Net percentage profit across total sales of ₹9000.
(iv) 21-day combined average flight distance.

FORMULA USED:
1. Equal Volume Mixture: C_final = (C₁ + C₂) / 2
2. Weighted Percentage Score: Combined % = [Σ wᵢ × (Marksᵢ / MaxMarksᵢ) × 100] / Σ wᵢ
3. Overall Profit % = (Total Profit / Total Sales) × 100%
4. Updated Mean after new observation: x̄_new = (n₁x̄₁ + x_new) / (n₁ + 1)

STEP-BY-STEP CALCULATION:
Part (i):
Since volumes are equal (V₁ = V₂ = V):
C_final = (V × 10% + V × 20%) / (2V) = (10 + 20) / 2 = 15%.

Part (ii):
Percentage marks:
Internals % = (35/50) × 100 = 70%.
Project % = (44/60) × 100 = 73.33%.
Final Exam % = (80/100) × 100 = 80%.
Combined Annual Score = [3 × (35/50 × 100) + 4 × (44/60 × 100) + 5 × (80/100 × 100)] / (3 + 4 + 5)
This precisely matches expression (iv):
[(35/50 × 100 × 3) + (44/60 × 100 × 4) + (80/100 × 100 × 5)] / (3 + 4 + 5) = (210 + 293.33 + 400) / 12 = 903.33 / 12 = 75.28%.
Also matches expression (iii) multiplied by 100: [(35/50 × 3 + 44/60 × 4 + 80/100 × 5)/(3+4+5)] × 100.
Expressions (i) and (ii) are incorrect because they fail to normalize raw marks to percentages first.

Part (iii):
Profit from books = 30% of ₹8000 = 0.30 × 8000 = ₹2400.
Profit from covers = 50% of ₹1000 = 0.50 × 1000 = ₹500.
Total Profit = ₹2400 + ₹500 = ₹2900.
Total Sales = ₹8000 + ₹1000 = ₹9000.
Overall Profit Percentage = (2900 / 9000) × 100% = 290 / 9 % = 32.22%.

Part (iv):
Total distance over first 20 days = 20 × 44.5 = 890 km.
Distance on 21st day = 55 km.
Total distance over 21 days = 890 + 55 = 945 km.
New 21-day average = 945 / 21 = 45 km/day.

[ROUGH_WORK]
2900 / 9000 = 29 / 90 = 0.3222... -> 32.22%
890 + 55 = 945
945 / 21: 21 × 40 = 840, 945 - 840 = 105, 21 × 5 = 105. Exact 45!

Boxed Answer:
[ (i) Mixture Concentration = 15%, (ii) Correct Expressions: (iii) and (iv) yielding Annual Score = 75.28%, (iii) Profit Percentage = 32.22%, (iv) Average Daily Distance = 45 km/day ]"""
}
modules[1]['worked_examples'].append(we_m2_extra)

# Fix missing FORMULA USED in Module 2 WE 2
if "FORMULA USED" not in modules[1]['worked_examples'][1]['solution']:
    modules[1]['worked_examples'][1]['solution'] = modules[1]['worked_examples'][1]['solution'].replace(
        "TO FIND:",
        "TO FIND:\n(Determine final alloy copper concentration.)\n\nFORMULA USED:\nC_mix = (m₁c₁ + m₂c₂) / (m₁ + m₂)"
    )

# Module 3: Add Exercise Sets 10.4 & 10.5
we_m3_extra = {
    "problem": "Chapter 10, Exercise Sets 10.4 & 10.5 (Ganita Manjari Part 2, Sections 10.4 & 10.5, pp. 21–29):\n(i) Exercise Set 10.4, Q1 (p. 21): IUCN Red List stacked column chart (Mammals, Reptiles, Birds, Insects, Amphibians, Molluscs, Fish, Others). Explain: (a) What the number 14,234 at the top of the 2019 column represents; (b) Approximate reptile count in 2016; (c) Classes with relatively small increases from 2007 to 2019.\n(ii) Exercise Set 10.4, Q2 (p. 21): Bowler wickets: Test (Home 62, Overseas 172), ODI (Home 100, Overseas 49), T20 (Home 32, Overseas 71). Construct the stacked bar charts comparing home vs overseas wickets.\n(iii) Exercise Set 10.5, Q1 (p. 29): Table 10.3 tracks daily hours (lying down, sitting, standing/moving) for 5 people: Pavani (Patient: 20, 3, 1), Raghu (Nurse: 7, 4, 13), Zakir (Teacher: 8, 6, 10), Julie (8, 10, 6), Sahana (Student). Complete the 100% stacked bar chart and determine percentage distributions.",
    "solution": """GIVEN:
(i) IUCN Red List data: Total endangered species counts: 7851 (2007), 9618 (2010), 11212 (2013), 12630 (2016), 14234 (2019).
(ii) Bowler wickets:
    - Test: Total = 62 + 172 = 234 (Home = 62, Overseas = 172)
    - ODI: Total = 100 + 49 = 149 (Home = 100, Overseas = 49)
    - T20: Total = 32 + 71 = 103 (Home = 32, Overseas = 71)
(iii) 24-hour daily time-budget data for 5 individuals across 3 states: Lying down, Sitting, Standing/Moving.

TO FIND / TO PROVE:
(i) Interpretations of absolute totals and class-wise trends in stacked column charts.
(ii) Segmented heights for absolute stacked bar chart of cricket bowling records.
(iii) 100% component percentages for each individual's 24-hour daily budget.

FORMULA USED:
1. Component Percentage in 100% Stacked Bar Chart:
   Percentage = (Category Value / Total for Entity) × 100%
2. Absolute Stacked Column Height: Total Height = Σ Component Heights

STEP-BY-STEP CALCULATION:
Part (i) IUCN Chart Interpretation:
(a) The number 14,234 at the top of the 2019 bar represents the grand total number of endangered animal species evaluated and recorded on the IUCN Red List across all surveyed taxonomic classes in the year 2019.
(b) In 2016, reading the height of the reptile band between the boundary lines indicates approximately 1300 to 1400 reptile species.
(c) Birds and mammals show relatively gentle, steady slopes (small percentage increases), whereas insects and amphibians exhibited rapid upward expansion in listings.

Part (ii) Bowling Wickets Stacked Bar Formulation:
- Test Bar: Total height = 234 wickets. Bottom segment (Home) = 62, Top segment (Overseas) = 172. Home fraction = 62/234 ≈ 26.5%, Overseas fraction = 73.5%.
- ODI Bar: Total height = 149 wickets. Bottom segment (Home) = 100, Top segment (Overseas) = 49. Home fraction = 100/149 ≈ 67.1%, Overseas fraction = 32.9%.
- T20 Bar: Total height = 103 wickets. Bottom segment (Home) = 32, Top segment (Overseas) = 71. Home fraction = 32/103 ≈ 31.1%, Overseas fraction = 68.9%.

Part (iii) 100% Stacked Bar Activity Distribution:
Total hours per day = 24 hours.
1. Pavani (Patient):
   Lying = (20/24) × 100% = 83.33%
   Sitting = (3/24) × 100% = 12.50%
   Standing/Moving = (1/24) × 100% = 4.17%
2. Raghu (Nurse):
   Lying = (7/24) × 100% = 29.17%
   Sitting = (4/24) × 100% = 16.67%
   Standing/Moving = (13/24) × 100% = 54.16%
3. Zakir (Teacher):
   Lying = (8/24) × 100% = 33.33%
   Sitting = (6/24) × 100% = 25.00%
   Standing/Moving = (10/24) × 100% = 41.67%
4. Sahana (Student - Estimated: Lying 8h, Sitting 9h, Standing/Moving 7h):
   Lying = (8/24) × 100% = 33.33%
   Sitting = (9/24) × 100% = 37.50%
   Standing/Moving = (7/24) × 100% = 29.17%
5. Julie (Desk Worker / IT Professional):
   Lying = (8/24) × 100% = 33.33%
   Sitting = (10/24) × 100% = 41.67%
   Standing/Moving = (6/24) × 100% = 25.00%

[ROUGH_WORK]
20/24 = 5/6 = 83.33%
13/24 = 0.54166... = 54.17%
10/24 = 5/12 = 41.67%
Total wickets = 234 (Test), 149 (ODI), 103 (T20).

Boxed Answer:
[ (i) 14,234 is 2019 Grand Total; Reptiles ≈ 1350; Birds & Mammals grew slowest, (ii) Total Heights: Test = 234, ODI = 149, T20 = 103, (iii) 100% Distributions: Pavani (83.3% L, 12.5% S, 4.2% M), Raghu (29.2% L, 16.7% S, 54.2% M), Zakir (33.3% L, 25.0% S, 41.7% M), Julie (33.3% L, 41.7% S, 25.0% M) ]"""
}
modules[2]['worked_examples'].append(we_m3_extra)

# Fix missing FORMULA USED in Module 3 WE 1
if "FORMULA USED" not in modules[2]['worked_examples'][0]['solution']:
    modules[2]['worked_examples'][0]['solution'] = modules[2]['worked_examples'][0]['solution'].replace(
        "TO PROVE / TO DERIVE:",
        "TO PROVE / TO DERIVE:\nDemonstrate 100% stacked bar chart properties.\n\nFORMULA USED:\nPercentage Share = (Category Units / Total Units) × 100%"
    )

# Fix Module 5: Add missing FORMULA USED and TO FIND headers across WE 1 to WE 8
m5_wes = modules[4]['worked_examples']
for idx, we in enumerate(m5_wes):
    sol = we['solution']
    # If TO FIND missing
    if "TO FIND" not in sol and "TO PROVE" not in sol and "TO EVALUATE" not in sol and "TO FORMULATE" not in sol:
        sol = sol.replace("GIVEN:", "GIVEN:\n(Given problem parameters as stated in question.)\n\nTO FIND:\nSolve for the required quantities and justify inferences.")
    
    # If FORMULA USED missing
    if "FORMULA USED" not in sol and "THEOREM USED" not in sol and "ALGORITHM" not in sol:
        # Determine appropriate formula
        if "Exercise 7" in we['problem']:
            f_str = "FORMULA USED:\nWeighted Mean x̄ = (Σ wᵢxᵢ) / (Σ wᵢ), with boundary condition w_min > 0."
        elif "Exercise 8" in we['problem']:
            f_str = "FORMULA USED:\nComponent Proportion = (Sub-item / Total) × 100%\nAccumulated Total = Σ Category Counts"
        elif "Exercise 9" in we['problem']:
            f_str = "FORMULA USED:\nProportion Comparison: Percentage of total = (Count / Total) × 100%\nAbsolute Count Comparison: Count_A vs Count_B"
        elif "Exercise 10" in we['problem']:
            f_str = "FORMULA USED:\nTotal Time = Time_swim + Time_cycle + Time_run\nSegment Fraction = (Segment Time / Total Time) × 100%"
        elif "Exercise 11" in we['problem']:
            f_str = "FORMULA USED:\nProportion in Group = (Subgroup Count / Total in Group) × 100%"
        elif "Exercise 12" in we['problem']:
            f_str = "FORMULA USED:\nGrand Average = [Σ (Nₖ × Āₖ)] / [Σ Nₖ]\nCategory Share = (Monthly Expense_i / Total Monthly Expense) × 100%"
        elif "Exercise 15" in we['problem']:
            f_str = "FORMULA USED:\nAlgebraic Shift Invariant: x̄_new = [Σ (wᵢ + c)xᵢ] / [Σ (wᵢ + c)]\nDeviation = x̄_new - x̄ = c·Σ(xᵢ - x̄) / [W(W + nc)]"
        elif "Exercise 16" in we['problem']:
            f_str = "FORMULA USED:\nPopulation Share Pᵢ = Nᵢ / N_total\nCondition for Share Change: ΔPᵢ > 0 iff rate of decrease of Nᵢ is less than overall rate of decrease."
        else:
            f_str = "FORMULA USED:\nWeighted Arithmetic Mean x̄ = (Σ wᵢxᵢ) / (Σ wᵢ)"
        
        # Insert before STEP-BY-STEP
        if "STEP-BY-STEP" in sol:
            sol = sol.replace("STEP-BY-STEP", f"{f_str}\n\nSTEP-BY-STEP")
        else:
            sol = sol + f"\n\n{f_str}"
            
    we['solution'] = sol

with open('scripts/maths_pt2_modules/ch10_understanding_data.json', 'w', encoding='utf-8') as f:
    json.dump(modules, f, indent=2, ensure_ascii=False)

print('Updated ch10_understanding_data.json successfully!')
