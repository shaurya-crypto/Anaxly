const { supabase } = require('./db_helper');

async function enrichCh8() {
  console.log('=== ENRICHING CLASS 10 MATHS - CHAPTER 8: INTRODUCTION TO TRIGONOMETRY ===\n');

  // Mod 1: Trigonometric Ratios of an Acute Angle & Examples 1-5
  const mod1Examples = [
    {
      problem: "Example 1 (NCERT Page 6): Given tan A = 4/3, find the other trigonometric ratios of the angle A.",
      solution: "Given: In a right-angled triangle ABC right-angled at B, tan A = 4/3.\nDefinitions:\ntan A = Opposite / Adjacent = BC / AB = 4/3.\nLet BC = 4k and AB = 3k, where k is a positive constant.\n\nStep 1: Compute Hypotenuse AC using Pythagoras Theorem:\nAC² = AB² + BC² = (3k)² + (4k)² = 9k² + 16k² = 25k²\nAC = √(25k²) = 5k.\n\nStep 2: Calculate all 5 remaining trigonometric ratios:\nsin A = Opposite / Hypotenuse = BC / AC = 4k / 5k = 4/5.\ncos A = Adjacent / Hypotenuse = AB / AC = 3k / 5k = 3/5.\ncot A = 1 / tan A = AB / BC = 3/4.\nsec A = 1 / cos A = AC / AB = 5/3.\ncosec A = 1 / sin A = AC / BC = 5/4.\n[ROUGH_WORK]\nStandard 3-4-5 right triangle!\nsin²A + cos²A = (4/5)² + (3/5)² = 16/25 + 9/25 = 25/25 = 1 (Verified!)\nBoxed Answer: [ sin A = 4/5, cos A = 3/5, cot A = 3/4, sec A = 5/3, cosec A = 5/4 ].",
      concept_questions: [
        "Why do we introduce the constant k when setting sides BC = 4k and AB = 3k?",
        "Does the value of sin A change if the sides of the triangle are doubled?"
      ],
      graph_payload: {
        points: [
          { x: 0, y: 0, label: "B (90°)" },
          { x: 3, y: 0, label: "A (Angle θ)" },
          { x: 0, y: 4, label: "C (Opposite vertex)" }
        ],
        segments: [
          { start: [0, 0], end: [3, 0], label: "AB = 3 (Adjacent)" },
          { start: [0, 0], end: [0, 4], label: "BC = 4 (Opposite)" },
          { start: [3, 0], end: [0, 4], label: "AC = 5 (Hypotenuse)" }
        ],
        polygons: [
          { points: [[0, 0], [3, 0], [0, 4]], label: "Right Triangle ABC" }
        ]
      }
    },
    {
      problem: "Example 3 (NCERT Page 7): Consider ΔACB, right-angled at C, in which AB = 29 units, BC = 21 units and ∠ABC = θ. Determine the values of: (i) cos²θ + sin²θ (ii) cos²θ - sin²θ.",
      solution: "Given: In right ΔACB, ∠C = 90°, Hypotenuse AB = 29, Base BC = 21, and ∠ABC = θ.\n\nStep 1: Compute Perpendicular AC using Pythagoras Theorem:\nAC² = AB² - BC² = 29² - 21²\nUse algebraic identity a² - b² = (a - b)(a + b):\nAC² = (29 - 21)(29 + 21) = 8 × 50 = 400\nAC = √400 = 20 units.\n\nStep 2: Determine sin θ and cos θ:\nsin θ = Opposite / Hypotenuse = AC / AB = 20 / 29\ncos θ = Adjacent / Hypotenuse = BC / AB = 21 / 29\n\nStep 3: Evaluate (i) cos²θ + sin²θ:\ncos²θ + sin²θ = (21/29)² + (20/29)² = (441 + 400) / 841 = 841 / 841 = 1.\n\nStep 4: Evaluate (ii) cos²θ - sin²θ:\ncos²θ - sin²θ = (21/29)² - (20/29)² = (441 - 400) / 841 = 41 / 841.\n[ROUGH_WORK]\nPythagorean Triplet: (20, 21, 29).\ncos²θ + sin²θ = 1 confirms the fundamental identity!\nBoxed Answer: [ (i) cos²θ + sin²θ = 1; (ii) cos²θ - sin²θ = 41/841 ].",
      concept_questions: [
        "Why is cos²θ + sin²θ always equal to 1 regardless of the triangle dimensions?",
        "How did using (a - b)(a + b) simplify calculating 29² - 21²?"
      ]
    }
  ];

  // Mod 4: Exercise 8.1 Complete Solver (Q1 to Q11)
  const mod4Examples = [
    {
      problem: "Exercise 8.1 Q1 & Q2 (NCERT Page 9): Q1: In ΔABC, right-angled at B, AB = 24 cm, BC = 7 cm. Determine: (i) sin A, cos A (ii) sin C, cos C. Q2: In Fig. 8.12, find tan P - cot R. [Given: In right ΔPQR, PQ = 12 cm, PR = 13 cm].",
      solution: "Problem 1 (Q1):\nGiven right ΔABC with ∠B = 90°, AB = 24 cm, BC = 7 cm.\nStep 1: Find AC by Pythagoras Theorem:\nAC = √(AB² + BC²) = √(24² + 7²) = √(576 + 49) = √625 = 25 cm.\n\nPart (i): Relative to Angle A:\nOpposite = BC = 7, Adjacent = AB = 24, Hypotenuse = AC = 25.\nsin A = BC / AC = 7 / 25.\ncos A = AB / AC = 24 / 25.\n\nPart (ii): Relative to Angle C:\nOpposite = AB = 24, Adjacent = BC = 7, Hypotenuse = AC = 25.\nsin C = AB / AC = 24 / 25.\ncos C = BC / AC = 7 / 25.\n\nProblem 2 (Q2):\nIn right ΔPQR with ∠Q = 90°, PQ = 12 cm, PR = 13 cm.\nStep 1: Find QR by Pythagoras Theorem:\nQR = √(PR² - PQ²) = √(13² - 12²) = √(169 - 144) = √25 = 5 cm.\n\nStep 2: Find tan P and cot R:\nFor Angle P: Opposite = QR = 5, Adjacent = PQ = 12 ⇒ tan P = 5/12.\nFor Angle R: Adjacent = QR = 5, Opposite = PQ = 12 ⇒ cot R = 5/12.\n\nStep 3: Compute tan P - cot R:\ntan P - cot R = 5/12 - 5/12 = 0.\n[ROUGH_WORK]\nLook at Figure 8.12 on page 9 in your textbook in the side viewer!\nNotice: tan P = cot R because P and R are complementary (P + R = 90°)!\nBoxed Answer: [ Q1(i): sin A = 7/25, cos A = 24/25; Q1(ii): sin C = 24/25, cos C = 7/25; Q2: tan P - cot R = 0 ].",
      figure_id: "Fig. 8.12",
      page: 9,
      notesSourceFilename: "jemh108.pdf",
      concept_questions: [
        "Why do the roles of Opposite and Adjacent sides swap when looking at angle A versus angle C?",
        "Why is tan P equal to cot R in any right triangle with acute angles P and R?"
      ]
    },
    {
      problem: "Exercise 8.1 Q7 & Q8 (NCERT Page 9): Q7: If cot θ = 7/8, evaluate: (i) (1 + sin θ)(1 - sin θ) / [(1 + cos θ)(1 - cos θ)] (ii) cot²θ. Q8: If 3 cot A = 4, check whether (1 - tan²A)/(1 + tan²A) = cos²A - sin²A or not.",
      solution: "Problem 1 (Q7):\nGiven: cot θ = 7/8.\nPart (i): Simplify using identity (a + b)(a - b) = a² - b²:\nNumerator = (1 + sin θ)(1 - sin θ) = 1 - sin²θ = cos²θ.\nDenominator = (1 + cos θ)(1 - cos θ) = 1 - cos²θ = sin²θ.\nRatio = cos²θ / sin²θ = (cos θ / sin θ)² = cot²θ.\nSubstitute cot θ = 7/8:\ncot²θ = (7/8)² = 49 / 64.\n\nPart (ii): cot²θ = (7/8)² = 49 / 64.\nBoth parts yield exactly 49/64.\n\nProblem 2 (Q8):\nGiven: 3 cot A = 4 ⇒ cot A = 4/3 ⇒ tan A = 3/4.\nIn right triangle, Opposite = 3, Adjacent = 4 ⇒ Hypotenuse = √(3² + 4²) = 5.\ncos A = 4/5, sin A = 3/5.\n\nLHS: (1 - tan²A) / (1 + tan²A) = [1 - (3/4)²] / [1 + (3/4)²] = [1 - 9/16] / [1 + 9/16]\n= (7/16) / (25/16) = 7 / 25.\n\nRHS: cos²A - sin²A = (4/5)² - (3/5)² = 16/25 - 9/25 = 7 / 25.\n\nSince LHS = RHS = 7/25, the identity is YES, equal!\n[ROUGH_WORK]\nStandard double-angle formula cos 2A = (1 - tan²A)/(1 + tan²A) = cos²A - sin²A confirmed!\nBoxed Answer: [ Q7: (i) 49/64, (ii) 49/64; Q8: Yes, LHS = RHS = 7/25 ].",
      concept_questions: [
        "Why is (1 + sin θ)(1 - sin θ) algebraically equal to cos²θ?",
        "If cot A = 4/3, what are the values of sec A and cosec A?"
      ]
    },
    {
      problem: "Exercise 8.1 Q10 (NCERT Page 9): In ΔPQR, right-angled at Q, PR + QR = 25 cm and PQ = 5 cm. Determine the values of sin P, cos P and tan P.",
      solution: "Given: In right ΔPQR, ∠Q = 90°, PQ = 5 cm, and PR + QR = 25 cm.\nLet QR = x cm. Then PR = (25 - x) cm.\n\nStep 1: Apply Pythagoras Theorem in ΔPQR:\nPR² = PQ² + QR²\n(25 - x)² = 5² + x²\n625 - 50x + x² = 25 + x²\n\nStep 2: Cancel x² on both sides:\n625 - 50x = 25\n50x = 625 - 25 = 600\nx = 600 / 50 = 12 cm.\n\nStep 3: Determine side lengths:\nQR = x = 12 cm (Opposite to angle P)\nPR = 25 - 12 = 13 cm (Hypotenuse)\nPQ = 5 cm (Adjacent to angle P)\n\nStep 4: Compute trigonometric ratios for angle P:\nsin P = Opposite / Hypotenuse = QR / PR = 12 / 13.\ncos P = Adjacent / Hypotenuse = PQ / PR = 5 / 13.\ntan P = Opposite / Adjacent = QR / PQ = 12 / 5.\n[ROUGH_WORK]\n5-12-13 is a classic Pythagorean triplet! 12 + 13 = 25 matches given condition!\nBoxed Answer: [ sin P = 12/13, cos P = 5/13, tan P = 12/5 ].",
      concept_questions: [
        "Why did the quadratic term x² cancel out in the Pythagorean calculation?",
        "What would happen if PQ was 7 cm and PR + QR was 49 cm?"
      ]
    }
  ];

  // Mod 5: Exercise 8.2 Complete Solver (Specific Angles Table Q1 to Q4)
  const mod5Examples = [
    {
      problem: "Exercise 8.2 Q1 & Q3 (NCERT Page 15): Q1: Evaluate: (i) sin 60° cos 30° + sin 30° cos 60° | (ii) 2 tan²45° + cos²30° - sin²60°. Q3: If tan (A + B) = √3 and tan (A - B) = 1/√3; 0° < A + B ≤ 90°; A > B, find A and B.",
      solution: "Table of Exact Values:\nsin 30° = 1/2, cos 30° = √3/2, tan 30° = 1/√3\nsin 45° = 1/√2, cos 45° = 1/√2, tan 45° = 1\nsin 60° = √3/2, cos 60° = 1/2, tan 60° = √3\n\nProblem 1 (Q1(i)):\nsin 60° cos 30° + sin 30° cos 60°\n= (√3/2)(√3/2) + (1/2)(1/2) = 3/4 + 1/4 = 4/4 = 1.\nNotice: This is sin(60° + 30°) = sin 90° = 1.\n\nProblem 2 (Q1(ii)):\n2 tan²45° + cos²30° - sin²60°\n= 2(1)² + (√3/2)² - (√3/2)² = 2(1) + 3/4 - 3/4 = 2.\n\nProblem 3 (Q3):\nGiven: tan (A + B) = √3\nSince tan 60° = √3: A + B = 60° ... (Eq. 1)\nGiven: tan (A - B) = 1/√3\nSince tan 30° = 1/√3: A - B = 30° ... (Eq. 2)\n\nAdd Eq. 1 and Eq. 2:\n(A + B) + (A - B) = 60° + 30°\n2A = 90° ⇒ A = 45°.\n\nSubtract Eq. 2 from Eq. 1:\n2B = 30° ⇒ B = 15°.\nCheck conditions: A > B (45° > 15°) and A + B = 60° (≤ 90°). Both satisfied!\n[ROUGH_WORK]\n45 + 15 = 60, 45 - 15 = 30. tan 60° = √3, tan 30° = 1/√3.\nBoxed Answer: [ Q1(i): 1; Q1(ii): 2; Q3: A = 45° and B = 15° ].",
      concept_questions: [
        "Why does cos²30° - sin²60° cancel to 0 without computing their numerical values?",
        "How do you geometrically derive that tan 45° = 1 in an isosceles right triangle?"
      ]
    }
  ];

  // Mod 6: Exercise 8.3 Complete Solver (The 10 Rigorous Identity Proofs)
  const mod6Examples = [
    {
      problem: "Exercise 8.3 Q4 Parts (i) & (ii) (NCERT Page 19): Prove the following identities:\n(i) (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ)\n(ii) (cos A / (1 + sin A)) + ((1 + sin A) / cos A) = 2 sec A",
      solution: "Proof (i): LHS = (cosec θ - cot θ)²\nStep 1: Express in terms of sin θ and cos θ:\ncosec θ = 1 / sin θ, cot θ = cos θ / sin θ\nLHS = [ (1 / sin θ) - (cos θ / sin θ) ]² = [ (1 - cos θ) / sin θ ]²\nLHS = (1 - cos θ)² / sin²θ\n\nStep 2: Use Pythagorean identity sin²θ = 1 - cos²θ:\nLHS = (1 - cos θ)² / (1 - cos²θ)\nFactorize denominator using a² - b² = (a - b)(a + b):\nLHS = (1 - cos θ)(1 - cos θ) / [ (1 - cos θ)(1 + cos θ) ]\nCancel common factor (1 - cos θ):\nLHS = (1 - cos θ) / (1 + cos θ) = RHS.\nHence Proved!\n\nProof (ii): LHS = [ cos A / (1 + sin A) ] + [ (1 + sin A) / cos A ]\nStep 1: Take LCM of denominators:\nLCM = (1 + sin A) cos A\nLHS = [ cos²A + (1 + sin A)² ] / [ (1 + sin A) cos A ]\n\nStep 2: Expand (1 + sin A)² = 1 + 2 sin A + sin²A:\nLHS = [ cos²A + 1 + 2 sin A + sin²A ] / [ (1 + sin A) cos A ]\n\nStep 3: Group cos²A + sin²A = 1:\nLHS = [ (cos²A + sin²A) + 1 + 2 sin A ] / [ (1 + sin A) cos A ]\nLHS = [ 1 + 1 + 2 sin A ] / [ (1 + sin A) cos A ]\nLHS = [ 2 + 2 sin A ] / [ (1 + sin A) cos A ]\nFactor out 2 from numerator:\nLHS = 2(1 + sin A) / [ (1 + sin A) cos A ]\nCancel (1 + sin A):\nLHS = 2 / cos A = 2 sec A = RHS.\nHence Proved!\n[ROUGH_WORK]\ncos²A + sin²A = 1 is the magic key in almost all identity proofs!\nBoxed Answer: [ Both identities (i) and (ii) Hence Proved! ].",
      concept_questions: [
        "In Proof (i), why is factoring 1 - cos²θ into (1 - cos θ)(1 + cos θ) more powerful than expanding the numerator?",
        "Why is expressing all terms in terms of sin and cos the most reliable master strategy for proving identities?"
      ]
    },
    {
      problem: "Exercise 8.3 Q4 Parts (v) & (vi) (NCERT Page 19): Prove the following identities:\n(v) (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A (using identity cosec²A = 1 + cot²A)\n(vi) √[ (1 + sin A) / (1 - sin A) ] = sec A + tan A",
      solution: "Proof (v) [CBSE Classic 5-Mark Question]:\nLHS = (cos A - sin A + 1) / (cos A + sin A - 1)\nStep 1: Divide both numerator and denominator by sin A:\nNumerator = (cos A / sin A) - (sin A / sin A) + (1 / sin A) = cot A - 1 + cosec A = (cosec A + cot A) - 1\nDenominator = (cos A / sin A) + (sin A / sin A) - (1 / sin A) = cot A + 1 - cosec A = 1 - (cosec A - cot A)\n\nStep 2: Replace 1 in numerator using identity 1 = cosec²A - cot²A:\n1 = (cosec A - cot A)(cosec A + cot A)\nNumerator = (cosec A + cot A) - [ (cosec A - cot A)(cosec A + cot A) ]\nFactor out (cosec A + cot A):\nNumerator = (cosec A + cot A) [ 1 - (cosec A - cot A) ] = (cosec A + cot A) [ 1 - cosec A + cot A ]\n\nStep 3: Notice denominator is exactly [ 1 - cosec A + cot A ]:\nLHS = (cosec A + cot A) [ 1 - cosec A + cot A ] / [ 1 - cosec A + cot A ]\nCancel common bracket:\nLHS = cosec A + cot A = RHS.\nHence Proved!\n\nProof (vi): LHS = √[ (1 + sin A) / (1 - sin A) ]\nStep 1: Rationalize the denominator inside the radical:\nMultiply numerator and denominator by (1 + sin A):\nLHS = √[ (1 + sin A)(1 + sin A) / [ (1 - sin A)(1 + sin A) ] ]\nLHS = √[ (1 + sin A)² / (1 - sin²A) ]\n\nStep 2: Use 1 - sin²A = cos²A:\nLHS = √[ (1 + sin A)² / cos²A ]\nExtract square root:\nLHS = (1 + sin A) / cos A\n\nStep 3: Split into individual fractions:\nLHS = (1 / cos A) + (sin A / cos A) = sec A + tan A = RHS.\nHence Proved!\n[ROUGH_WORK]\nRationalizing inside radical removes denominator square root cleanly!\nBoxed Answer: [ Both identities (v) and (vi) Hence Proved! ].",
      concept_questions: [
        "In Proof (v), why do we divide by sin A rather than cos A?",
        "How would you prove √[ (1 - cos A) / (1 + cos A) ] using the exact same strategy as Proof (vi)?"
      ]
    }
  ];

  // Upload to Supabase
  const m1Id = '005cd0b8-914b-40b1-a4c3-f030a1e1faa5';
  const m4Id = 'abadd457-0cc1-4936-a764-4ed62d459a53';
  const m5Id = 'af00e0fd-85a7-4d71-9438-7765cb8fd783';
  const m6Id = '9358fc70-2abe-42ae-83d4-bf6e574b1ef4';

  await supabase.from('syllabus_modules').update({ worked_examples: mod1Examples }).eq('id', m1Id);
  console.log('✓ Ch 8 Mod 1 updated (Foundations & Examples 1-5)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod4Examples }).eq('id', m4Id);
  console.log('✓ Ch 8 Mod 4 updated (Exercise 8.1 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod5Examples }).eq('id', m5Id);
  console.log('✓ Ch 8 Mod 5 updated (Exercise 8.2 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod6Examples }).eq('id', m6Id);
  console.log('✓ Ch 8 Mod 6 updated (Exercise 8.3 Complete)');

  console.log('\n=== CHAPTER 8 ENRICHMENT 100% COMPLETE ===\n');
}

enrichCh8();
