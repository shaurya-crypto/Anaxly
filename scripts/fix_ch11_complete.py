import json

with open('scripts/maths_pt2_modules/ch11_algorithms.json', 'r', encoding='utf-8') as f:
    modules = json.load(f)

# Module 1: Add FORMULA USED to WE 1, and add WE 2 for Exercise Set 11.1 Q2
m1_we1_sol = modules[0]['worked_examples'][0]['solution']
if "FORMULA / ALGORITHM USED" not in m1_we1_sol:
    m1_we1_sol = m1_we1_sol.replace("STEP-BY-STEP", "FORMULA / ALGORITHM PRINCIPLE USED:\nPositional Base-10 Addition Invariant:\nIn any column k, Sum_k = a_k + b_k + carry_{k-1}.\nDigit_k = Sum_k mod 10, carry_k = ⌊Sum_k / 10⌋ ∈ {0, 1}.\n\nSTEP-BY-STEP")
    modules[0]['worked_examples'][0]['solution'] = m1_we1_sol

we_m1_q2 = {
    "problem": "Chapter 11, Exercise Set 11.1, Question 2 (Ganita Manjari Part 2, Section 11.1, p. 38):\nWhat happens if you add a 5-digit number to a 3-digit number? Do our steps handle this situation correctly? Explain how the algorithm handles numbers of unequal digit lengths.",
    "solution": """GIVEN:
Addition of two positive integers with unequal number of digits:
Number A has 5 digits: a₄a₃a₂a₁a₀ (e.g., 42,758).
Number B has 3 digits: b₂b₁b₀ (e.g., 684).

TO FIND / TO PROVE:
Determine whether the standard columnar addition algorithm handles unequal digit lengths, and demonstrate how the steps proceed correctly without ambiguity.

FORMULA / ALGORITHM PRINCIPLE USED:
Implicit Leading Zeros Alignment:
Any n-digit integer written in base 10 can be extended to m digits (m > n) by prepending (m - n) leading zeros:
b = Σ_{i=0}^{n-1} bᵢ·10ⁱ = Σ_{i=0}^{m-1} bᵢ·10ⁱ, where bᵢ = 0 for all i ≥ n.

STEP-BY-STEP CALCULATION / VERIFICATION:
Step 1: Alignment from Right to Left.
Write Number A and Number B aligning units digits at the extreme right:
Column 0 (Units): a₀ + b₀
Column 1 (Tens): a₁ + b₁
Column 2 (Hundreds): a₂ + b₂
Column 3 (Thousands): a₃ has no matching digit in B.
Column 4 (Ten-Thousands): a₄ has no matching digit in B.

Step 2: Execution with Column Loop.
In Columns 0, 1, and 2, the algorithm adds both digits and the incoming carry.
When moving to Column 3, Number B has no more written digits. In mathematics and computation, the absence of a digit in a positional numeral system is identically equal to 0.
Thus:
- For Column 3: Sum₃ = a₃ + 0 + carry₂.
- For Column 4: Sum₄ = a₄ + 0 + carry₃.

Step 3: Verification of Algorithm Correctness.
If the algorithm is implemented rigorously, Step 1 must explicitly state: "Align the numbers on the right. If one number has fewer digits, pad the missing columns on the left with 0." With this minor specification, the columnar addition algorithm handles numbers of any unequal lengths flawlessly.

[ROUGH_WORK]
Example: 42,758 + 684
  4 2 7 5 8
+ 0 0 6 8 4
-----------
Column 0: 8 + 4 = 12 -> write 2, carry 1
Column 1: 5 + 8 + 1 = 14 -> write 4, carry 1
Column 2: 7 + 6 + 1 = 14 -> write 4, carry 1
Column 3: 2 + 0 + 1 = 3 -> write 3, carry 0
Column 4: 4 + 0 + 0 = 4 -> write 4, carry 0
Result: 43,442. Exact match!

Boxed Answer:
[ The algorithm handles unequal lengths correctly by treating missing higher-order columns of the shorter number as zero digits (leading zero padding), preserving the base-10 place-value invariant. ]"""
}
modules[0]['worked_examples'].append(we_m1_q2)

# Module 2: Add FORMULA USED to WE 1, and add WE 2 for Exercise Set 11.2 (Q1, Q2, Q3)
m2_we1_sol = modules[1]['worked_examples'][0]['solution']
if "FORMULA / ALGORITHM USED" not in m2_we1_sol:
    m2_we1_sol = m2_we1_sol.replace("STEP-BY-STEP", "FORMULA / ALGORITHM PRINCIPLE USED:\nSet-Theoretic GCD Invariant:\nDivisors(m) = {d ∈ ℕ : m mod d = 0}\nCommonDivisors(m, n) = Divisors(m) ∩ Divisors(n)\ngcd(m, n) = max(CommonDivisors(m, n))\n\nSTEP-BY-STEP")
    modules[1]['worked_examples'][0]['solution'] = m2_we1_sol

we_m2_ex_11_2 = {
    "problem": "Chapter 11, Exercise Set 11.2, Questions 1, 2 & 3 (Ganita Manjari Part 2, Section 11.2, pp. 43–44):\n(i) Question 1: Suppose List 1 and List 2 are two lists of numbers in increasing order. (a) Write an algorithm to find elements in List 1 that are not present in List 2; (b) Write an algorithm to find elements in List 2 that are not present in List 1.\n(ii) Question 2: Describe an efficient algorithm to compute the least common multiple (lcm) of two positive integers m and n.\n(iii) Question 3: Divisors occur in pairs (e.g., for 18, pairs are (1, 18), (2, 9), (3, 6)). (a) If we write divisors in pairs, how many numbers do we have to examine between 1 and n to find all divisors of n? (b) Will our gcd algorithm still work with paired divisors?",
    "solution": """GIVEN:
(i) Two sorted lists of integers in strictly increasing order: List 1 = [a₁, a₂, ..., aₚ] and List 2 = [b₁, b₂, ..., b_q].
(ii) Two positive integers m and n for computing lcm(m, n).
(iii) Integer n with factor pairs (d, n/d).

TO FIND / TO PROVE:
(i) Design two-pointer list difference algorithms List1 \\ List2 and List2 \\ List1 running in linear time O(p + q).
(ii) Formulate an algorithm for lcm(m, n).
(iii) Determine the search bound for paired divisors and verify applicability to GCD computation.

FORMULA / ALGORITHM PRINCIPLE USED:
1. Two-Pointer Merge Scanning:
   Compare heads of sorted lists: if aᵢ < bⱼ, aᵢ ∉ List 2 (advance i); if aᵢ > bⱼ, bⱼ ∉ List 1 (advance j); if aᵢ = bⱼ, common element (advance both).
2. Fundamental LCM-GCD Duality:
   lcm(m, n) = (m × n) / gcd(m, n)
3. Divisor Pair Bound Invariant:
   If d divides n, then n/d also divides n. If d ≤ n/d, then d² ≤ n, which implies d ≤ √n.

STEP-BY-STEP ALGORITHM DESIGN & PROOF:
Part (i) List Difference Algorithm (Two-Pointer Linear Scan):
Algorithm ListDifference(List 1, List 2):
1. Initialize pointer i = 1, pointer j = 1, ResultList = [].
2. While i ≤ length(List 1) and j ≤ length(List 2):
   - If List 1[i] < List 2[j]:
     Append List 1[i] to ResultList. Increment i by 1.
   - Else if List 1[i] > List 2[j]:
     Increment j by 1.
   - Else (List 1[i] == List 2[j]):
     Increment both i and j by 1 (skip common elements).
3. While i ≤ length(List 1):
   Append List 1[i] to ResultList. Increment i by 1.
4. Report ResultList as (List 1 \\ List 2).
For part (b), swapping the roles of List 1 and List 2 gives (List 2 \\ List 1). Time complexity is O(p + q), far superior to nested loop search O(p × q).

Part (ii) LCM Algorithm:
Algorithm ComputeLCM(m, n):
1. Compute g = gcd(m, n) using Euclid's division algorithm (m mod n remainder chain).
2. Compute lcm = (m / g) × n. (Dividing first prevents integer overflow.)
3. Return lcm.
Alternative Direct Incremental Algorithm:
1. Set multiple = max(m, n), step = max(m, n).
2. While multiple mod min(m, n) ≠ 0:
   multiple = multiple + step.
3. Return multiple.

Part (iii) Paired Divisors and Search Bound:
(a) For any divisor d of n, the paired divisor is k = n/d.
Both cannot be strictly greater than √n because if d > √n and k > √n, then d × k > √n × √n = n, a contradiction.
Therefore, the smaller divisor in every pair must satisfy 1 ≤ d ≤ ⌊√n⌋.
Hence, we only need to examine integers up to ⌊√n⌋!
For n = 1,000,000, instead of scanning 1,000,000 numbers, we examine only 1,000 numbers (a 1000-fold speedup!).
(b) Yes, the GCD algorithm works with paired divisors: collect pairs (d, n/d) for d ≤ √n, sort the collected divisors, and perform list intersection with divisors of m.

[ROUGH_WORK]
Example for 18: √18 ≈ 4.24.
Check d = 1: 18/1 = 18 -> Pair (1, 18).
Check d = 2: 18/2 = 9 -> Pair (2, 9).
Check d = 3: 18/3 = 6 -> Pair (3, 6).
Check d = 4: does not divide 18.
Scan stops at 4. All 6 divisors [1, 2, 3, 6, 9, 18] found!
Only 4 checks needed instead of 18.

Boxed Answer:
[ (i) Two-pointer scan yields O(p + q) list difference, (ii) lcm(m, n) = (m × n) / gcd(m, n), (iii) Only ⌊√n⌋ numbers need to be examined, achieving quadratic speedup from O(n) to O(√n) ]"""
}
modules[1]['worked_examples'].append(we_m2_ex_11_2)

# Module 3: Add FORMULA USED to WE 1, and add WE 2 for Exercise Set 11.3 (Q1, Q2)
m3_we1_sol = modules[2]['worked_examples'][0]['solution']
if "FORMULA / THEOREM USED" not in m3_we1_sol:
    m3_we1_sol = m3_we1_sol.replace("STEP-BY-STEP", "FORMULA / THEOREM USED:\nEuclidean Subtraction Invariant (Elements VII.1):\nFor any positive integers m > n:\ngcd(m, n) = gcd(m - n, n)\n\nSTEP-BY-STEP")
    modules[2]['worked_examples'][0]['solution'] = m3_we1_sol

we_m3_ex_11_3 = {
    "problem": "Chapter 11, Exercise Set 11.3, Questions 1 & 2 (Ganita Manjari Part 2, Section 11.3, p. 45):\n(i) Question 1: How would our original algorithm change if we computed the divisors of n by examining the numbers from 1 to n in reverse order, from n down to 1?\n(ii) Question 2: In the single-variable scan algorithm for gcd(m, n), what happens when we look at candidate common divisors starting from min(m, n) and work backwards to 1? Compare its termination efficiency with forward scanning.",
    "solution": """GIVEN:
(i) Divisor search over integers {n, n - 1, ..., 2, 1}.
(ii) Single-variable common divisor scanner descending from k = min(m, n) down to 1 for gcd(m, n).

TO FIND / TO PROVE:
(i) Impact of reverse scanning on divisor list generation and order.
(ii) Impact of backwards scanning on GCD identification and proving the early termination invariant.

FORMULA / ALGORITHM PRINCIPLE USED:
1. Greatest Common Divisor Maximality:
   gcd(m, n) = max {k ∈ ℕ : k | m and k | n}
2. Early Termination Principle:
   If candidates k are tested in strictly decreasing order, the very FIRST candidate k that satisfies both conditions (k | m and k | n) is guaranteed to be the GREATEST common divisor.

STEP-BY-STEP ALGORITHMIC ANALYSIS:
Part (i) Reverse Divisor Search:
1. If we scan candidate divisors from n down to 1:
   The divisors are naturally produced in descending order: for n = 12, the generated list is [12, 6, 4, 3, 2, 1].
2. Impact on GCD algorithm:
   In the original forward algorithm, the rightmost element of the common divisor list was the GCD.
   With descending lists, the GCD is now the FIRST (leftmost) element!
   However, constructing the full list still requires examining all n numbers unless stopped early.

Part (ii) Backwards Scanning from min(m, n) down to 1 (Early-Exit GCD Algorithm):
Algorithm BackwardScanGCD(m, n):
1. Set k = min(m, n).
2. While k ≥ 1:
   - If (m mod k == 0) and (n mod k == 0):
     Return k immediately as gcd(m, n)!
   - k = k - 1.

Efficiency Comparison:
- Forward Scan (1 to min(m, n)):
  MUST scan all the way up to min(m, n) to confirm no larger divisor exists. Number of checks is always exactly min(m, n).
- Backward Scan (min(m, n) down to 1):
  Can terminate immediately on finding the first common divisor!
  Best-case: If n divides m (e.g., gcd(100, 25)), k = 25 is checked first, divides both, and terminates in exactly 1 step!
  Worst-case: If m and n are coprime (gcd = 1), it scans down to 1, taking min(m, n) steps.
  Average performance is significantly faster than forward scanning.

[ROUGH_WORK]
Example: gcd(60, 16)
min(60, 16) = 16.
k = 16: 60 mod 16 = 12 ≠ 0.
k = 15: 16 mod 15 = 1 ≠ 0.
k = 14: 16 mod 14 = 2 ≠ 0.
k = 13, 12, 11, 10, 9, 8: 60 mod 8 = 4 ≠ 0.
k = 7, 6, 5: 16 mod 5 ≠ 0.
k = 4: 60 mod 4 = 0 and 16 mod 4 = 0.
MATCH FOUND AT k = 4! Terminate immediately.
Steps taken: 13 steps instead of checking all remaining candidates down to 1.

Boxed Answer:
[ (i) Reverse search produces divisors in descending order with GCD at the head, (ii) Backward scan enables immediate early termination on the first common divisor, improving best-case complexity from O(min(m, n)) to O(1) ]"""
}
modules[2]['worked_examples'].append(we_m3_ex_11_3)

# Module 4: Add FORMULA / ALGORITHM USED to WE 1
m4_we1_sol = modules[3]['worked_examples'][0]['solution']
if "FORMULA / ALGORITHM USED" not in m4_we1_sol:
    m4_we1_sol = m4_we1_sol.replace("STEP-BY-STEP", "FORMULA / ALGORITHM PRINCIPLE USED:\nĀryabhaṭa Division Algorithm (Kuṭṭaka / Euclidean Division):\nFor integers m > n:\nm = q · n + r, where 0 ≤ r < n.\ngcd(m, n) = gcd(n, r).\nWhen r = 0, gcd(m, n) = n.\n\nSTEP-BY-STEP")
    modules[3]['worked_examples'][0]['solution'] = m4_we1_sol

# Module 5: Add FORMULA / ALGORITHM USED to WE 1, 2, 3, 4
m5_wes = modules[4]['worked_examples']
for idx, we in enumerate(m5_wes):
    sol = we['solution']
    if "FORMULA / ALGORITHM USED" not in sol and "FORMULA USED" not in sol:
        if idx == 0:
            f_str = "FORMULA / ALGORITHM USED:\nEuclidean Remainder Invariant: gcd(a, b) = gcd(b, a mod b)."
        elif idx == 1:
            f_str = "FORMULA / ALGORITHM USED:\nDivisibility Remainder Theorem: d | m and d | n ⇔ d | n and d | (m - qn)."
        elif idx == 2:
            f_str = "FORMULA / ALGORITHM USED:\nPrime Definition: p > 1 is prime iff Divisors(p) = {1, p} (exactly 2 divisors)."
        else:
            f_str = "FORMULA / ALGORITHM USED:\nFundamental Theorem of Arithmetic: n = ∏ pᵢ^{aᵢ}\ngcd(m, n) = ∏ pᵢ^{min(aᵢ, bᵢ)}, lcm(m, n) = ∏ pᵢ^{max(aᵢ, bᵢ)}."
        
        sol = sol.replace("STEP-BY-STEP", f"{f_str}\n\nSTEP-BY-STEP")
        we['solution'] = sol

with open('scripts/maths_pt2_modules/ch11_algorithms.json', 'w', encoding='utf-8') as f:
    json.dump(modules, f, indent=2, ensure_ascii=False)

print('Updated ch11_algorithms.json successfully!')
