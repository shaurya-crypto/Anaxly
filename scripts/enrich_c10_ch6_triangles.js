const { supabase } = require('./db_helper');

async function enrichCh6() {
  console.log('=== ENRICHING CLASS 10 MATHS - CHAPTER 6: TRIANGLES ===\n');

  // Mod 1: Basic Proportionality Theorem (Theorem 6.1) & Converse (Theorem 6.2) & Examples 1-3
  const mod1Examples = [
    {
      problem: "Theorem 6.1 (Basic Proportionality Theorem / Thales Theorem - NCERT Page 8): If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.",
      solution: "Given: In ΔABC, a line DE is parallel to side BC intersecting AB at D and AC at E (DE || BC).\nTo Prove: AD / DB = AE / EC\n\nConstruction:\n1. Join BE and CD.\n2. Draw DM ⊥ AC and EN ⊥ AB.\n\nProof:\nStep 1: Compute Area of ΔADE:\nArea(ΔADE) = (1/2) × base × height = (1/2) × AD × EN ... (taking AD as base, EN is height)\n\nStep 2: Compute Area of ΔBDE:\nArea(ΔBDE) = (1/2) × BD × EN ... (taking BD as base, EN is height from vertex E)\nRatio 1: Area(ΔADE) / Area(ΔBDE) = [(1/2) × AD × EN] / [(1/2) × BD × EN] = AD / DB ... (Eq. 1)\n\nStep 3: Compute Area of ΔADE and ΔCDE with base AC:\nArea(ΔADE) = (1/2) × AE × DM ... (taking AE as base, DM is height)\nArea(ΔCDE) = (1/2) × EC × DM ... (taking EC as base, DM is height)\nRatio 2: Area(ΔADE) / Area(ΔCDE) = [(1/2) × AE × DM] / [(1/2) × EC × DM] = AE / EC ... (Eq. 2)\n\nStep 4: Relate the denominators:\nNotice that ΔBDE and ΔCDE are on the same base DE and between the same parallels DE and BC.\nBy standard geometric theorem: Area(ΔBDE) = Area(ΔCDE) ... (Eq. 3)\n\nStep 5: Conclusion:\nFrom (Eq. 1), (Eq. 2), and (Eq. 3), the LHS are equal:\nAD / DB = AE / EC.\n[ROUGH_WORK]\nLook at Figure 6.10 on page 8 in your textbook in the side viewer!\nBase × Altitudes cancel out leaving exact side ratios.\nBoxed Answer: [ Hence Proved: AD / DB = AE / EC (Basic Proportionality Theorem) ].",
      figure_id: "Fig. 6.10",
      page: 8,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "Why is altitude EN common to both triangle ADE and triangle BDE?",
        "What theorem guarantees that triangle BDE and triangle CDE have equal areas?"
      ],
      graph_payload: {
        points: [
          { x: 3, y: 7, label: "A (Apex)" },
          { x: 0, y: 0, label: "B" },
          { x: 7, y: 0, label: "C" },
          { x: 1.2, y: 2.8, label: "D" },
          { x: 4.6, y: 4.2, label: "E" }
        ],
        segments: [
          { start: [0, 0], end: [7, 0], label: "BC (Base)" },
          { start: [0, 0], end: [3, 7], label: "AB" },
          { start: [7, 0], end: [3, 7], label: "AC" },
          { start: [1.2, 2.8], end: [4.6, 4.2], label: "DE || BC" },
          { start: [0, 0], end: [4.6, 4.2], label: "BE (Const.)" },
          { start: [7, 0], end: [1.2, 2.8], label: "CD (Const.)" }
        ],
        polygons: [
          { points: [[0, 0], [7, 0], [3, 7]], label: "ΔABC" }
        ]
      }
    },
    {
      problem: "Example 1 (NCERT Page 10): If a line intersects sides AB and AC of a ΔABC at D and E respectively and is parallel to BC, prove that AD / AB = AE / AC.",
      solution: "Given: In ΔABC, DE || BC, with D on AB and E on AC.\nTo Prove: AD / AB = AE / AC\n\nProof:\nStep 1: By Basic Proportionality Theorem (Theorem 6.1):\nSince DE || BC, we have:\nAD / DB = AE / EC\n\nStep 2: Invert the ratio (invertendo):\nDB / AD = EC / AE\n\nStep 3: Add 1 to both sides (componendo):\n(DB / AD) + 1 = (EC / AE) + 1\n(DB + AD) / AD = (EC + AE) / AE\n\nStep 4: Recognize side additions:\nSince D lies on AB, DB + AD = AB.\nSince E lies on AC, EC + AE = AC.\nTherefore: AB / AD = AC / AE\n\nStep 5: Take reciprocal:\nAD / AB = AE / AC.\n[ROUGH_WORK]\nWhole-side ratio follows directly from part-side ratio!\nBoxed Answer: [ Hence Proved: AD / AB = AE / AC ].",
      concept_questions: [
        "What algebraic operation turns AD/DB = AE/EC into AD/AB = AE/AC?",
        "If AD = 2 cm, DB = 3 cm, and AC = 10 cm, what is the length of AE?"
      ]
    },
    {
      problem: "Example 3 (NCERT Page 11): In Fig. 6.16, PS / SQ = PT / TR and ∠PST = ∠PRQ. Prove that ΔPQR is an isosceles triangle.",
      solution: "Given: In ΔPQR, PS / SQ = PT / TR and ∠PST = ∠PRQ.\nTo Prove: ΔPQR is isosceles (i.e. PQ = PR).\n\nProof:\nStep 1: By Converse of Basic Proportionality Theorem (Theorem 6.2):\nSince PS / SQ = PT / TR, the line ST is parallel to QR (ST || QR).\n\nStep 2: Corresponding Angles:\nSince ST || QR and PQ is a transversal:\n∠PST = ∠PQR (Corresponding angles) ... (Eq. 1)\n\nStep 3: Use given angle equality:\nWe are given: ∠PST = ∠PRQ ... (Eq. 2)\n\nStep 4: Equate angles:\nFrom (Eq. 1) and (Eq. 2):\n∠PQR = ∠PRQ\n\nStep 5: Sides opposite equal angles:\nIn ΔPQR, since ∠PQR = ∠PRQ, the sides opposite to them are equal:\nPR = PQ (Sides opposite equal angles of a triangle are equal).\nTherefore, ΔPQR is an isosceles triangle.\n[ROUGH_WORK]\nLook at Figure 6.16 on page 11 in your textbook in the side viewer!\nParallel line creates equal corresponding angle, which chains into base angle equality.\nBoxed Answer: [ Hence Proved: PQ = PR, so ΔPQR is an isosceles triangle ].",
      figure_id: "Fig. 6.16",
      page: 11,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "How did we prove ST || QR in Step 1?",
        "State the Converse of Basic Proportionality Theorem."
      ]
    }
  ];

  // Mod 3: Exercise 6.1 & 6.2 Complete Solver
  const mod3Examples = [
    {
      problem: "Exercise 6.2 Q1 & Q2 (NCERT Page 12): Q1: In Fig. 6.17, (i) and (ii), DE || BC. Find EC in (i) and AD in (ii). [Given in (i): AD = 1.5 cm, DB = 3 cm, AE = 1 cm. Given in (ii): DB = 7.2 cm, AE = 1.8 cm, EC = 5.4 cm]. Q2: E and F are points on sides PQ and PR of ΔPQR. State whether EF || QR when PE = 3.9 cm, EQ = 3 cm, PF = 3.6 cm, FR = 2.4 cm.",
      solution: "Problem 1 (Q1):\nFormula: Since DE || BC, by BPT: AD / DB = AE / EC\n\nPart (i):\n1.5 / 3 = 1 / EC\n1/2 = 1 / EC ⇒ EC = 2 cm.\n\nPart (ii):\nAD / 7.2 = 1.8 / 5.4\nNotice 1.8 / 5.4 = 1/3.\nAD / 7.2 = 1/3 ⇒ AD = 7.2 / 3 = 2.4 cm.\n\nProblem 2 (Q2):\nTest whether EF || QR in ΔPQR:\nCompute PE / EQ = 3.9 / 3 = 1.3\nCompute PF / FR = 3.6 / 2.4 = 36 / 24 = 3/2 = 1.5\nSince PE / EQ (1.3) ≠ PF / FR (1.5), by Converse of BPT, EF is NOT parallel to QR.\n[ROUGH_WORK]\nLook at Figure 6.17 on page 12 in your textbook in the side viewer!\nBoxed Answer: [ Q1(i): EC = 2 cm; Q1(ii): AD = 2.4 cm; Q2: EF is NOT parallel to QR as PE/EQ ≠ PF/FR ].",
      figure_id: "Fig. 6.17",
      page: 12,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "Why is it essential to check the exact decimal ratio before deciding parallelism?",
        "If PE/EQ were equal to PF/FR, what theorem would guarantee EF || QR?"
      ]
    },
    {
      problem: "Exercise 6.2 Q3 & Q4 (NCERT Page 12): Q3: In Fig. 6.18, if LM || CB and LN || CD, prove that AM / AB = AN / AD. Q4: In Fig. 6.19, DE || AC and DF || AE. Prove that BF / FE = BE / EC.",
      solution: "Problem 1 (Q3):\nIn Fig. 6.18, given LM || CB and LN || CD.\nStep 1: In ΔABC, since LM || CB, by BPT corollary:\nAM / AB = AL / AC ... (Eq. 1)\nStep 2: In ΔADC, since LN || CD, by BPT corollary:\nAN / AD = AL / AC ... (Eq. 2)\nStep 3: From (Eq. 1) and (Eq. 2), both ratios equal AL / AC:\nAM / AB = AN / AD.\nHence Proved!\n\nProblem 2 (Q4):\nIn Fig. 6.19, given DE || AC and DF || AE.\nStep 1: In ΔBAC, since DE || AC, by BPT:\nBD / DA = BE / EC ... (Eq. 1)\nStep 2: In ΔBAE, since DF || AE, by BPT:\nBD / DA = BF / FE ... (Eq. 2)\nStep 3: Equate LHS:\nFrom (Eq. 1) and (Eq. 2):\nBF / FE = BE / EC.\nHence Proved!\n[ROUGH_WORK]\nLook at Figure 6.18 and Figure 6.19 on page 12 in your textbook in the side viewer!\nThe common side ratio BD/DA links both triangles perfectly.\nBoxed Answer: [ Q3: Hence Proved AM/AB = AN/AD; Q4: Hence Proved BF/FE = BE/EC ].",
      figure_id: "Fig. 6.18",
      page: 12,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "In Q4, what triangle was used to apply BPT for DF || AE versus DE || AC?",
        "What is the bridge ratio that connects both equations?"
      ]
    },
    {
      problem: "Exercise 6.2 Q9 & Q10 (NCERT Page 13): Q9: ABCD is a trapezium in which AB || DC and its diagonals intersect each other at the point O. Show that AO / BO = CO / DO. Q10: The diagonals of a quadrilateral ABCD intersect each other at the point O such that AO / BO = CO / DO. Show that ABCD is a trapezium.",
      solution: "Problem 1 (Q9 - Trapezium Diagonals):\nGiven: ABCD is a trapezium with AB || DC. Diagonals AC and BD intersect at O.\nTo Prove: AO / BO = CO / DO (or AO / CO = BO / DO)\nConstruction: Through O, draw line OE || AB meeting AD at E. Since AB || DC, OE || DC.\nProof:\nStep 1: In ΔADC, OE || DC. By BPT:\nAE / ED = AO / CO ... (Eq. 1)\nStep 2: In ΔDAB, EO || AB. By BPT:\nDE / EA = DO / BO ⇒ taking reciprocal: AE / ED = BO / DO ... (Eq. 2)\nStep 3: From (Eq. 1) and (Eq. 2):\nAO / CO = BO / DO\nRearranging terms: AO / BO = CO / DO.\nHence Proved!\n\nProblem 2 (Q10 - Converse Trapezium Proof):\nGiven: AO / BO = CO / DO, which means AO / CO = BO / DO ... (Eq. 1)\nTo Prove: ABCD is a trapezium (i.e. AB || DC)\nConstruction: Through O, draw OE || AB meeting AD at E.\nProof:\nIn ΔDAB, since OE || AB, by BPT:\nAE / ED = BO / DO ... (Eq. 2)\nFrom (Eq. 1) and (Eq. 2):\nAE / ED = AO / CO\nIn ΔADC, line OE divides sides AD and AC in the same ratio (AE / ED = AO / CO).\nBy Converse of BPT (Theorem 6.2): OE || DC.\nSince OE || AB (by construction) and OE || DC, we have:\nAB || DC.\nSince one pair of opposite sides is parallel, ABCD is a trapezium.\nHence Proved!\n[ROUGH_WORK]\nTrapezium ↔ Parallel line construction through intersection of diagonals!\nBoxed Answer: [ Q9: Proved AO/BO = CO/DO; Q10: Proved ABCD is a trapezium ].",
      concept_questions: [
        "Why is drawing the auxiliary line OE parallel to one of the bases necessary?",
        "Could Q9 also be proved using similarity of triangles ΔAOB and ΔCOD?"
      ]
    }
  ];

  // Mod 4: Exercise 6.3 Part 1 Solver (Similarity Testing & Angle Chasing Q1 to Q8)
  const mod4Examples = [
    {
      problem: "Exercise 6.3 Q2 & Q3 (NCERT Page 22): Q2: In Fig. 6.35, ΔODC ~ ΔOBA, ∠BOC = 125° and ∠CDO = 70°. Find ∠DOC, ∠DCO and ∠OAB. Q3: Diagonals AC and BD of a trapezium ABCD with AB || DC intersect each other at O. Using a similarity criterion for two triangles, show that OA / OC = OB / OD.",
      solution: "Problem 1 (Q2):\nIn Fig. 6.35, DOB is a straight line.\nStep 1: Compute ∠DOC:\n∠DOC + ∠BOC = 180° (Linear pair)\n∠DOC + 125° = 180° ⇒ ∠DOC = 180° - 125° = 55°.\n\nStep 2: Compute ∠DCO in ΔODC:\nIn ΔODC, sum of angles = 180°:\n∠DCO + ∠CDO + ∠DOC = 180°\n∠DCO + 70° + 55° = 180°\n∠DCO + 125° = 180° ⇒ ∠DCO = 55°.\n\nStep 3: Compute ∠OAB using similarity:\nGiven ΔODC ~ ΔOBA.\nCorresponding angles are equal: ∠OAB = ∠OCD = ∠DCO = 55°.\n\nProblem 2 (Q3):\nIn trapezium ABCD with AB || DC, consider ΔOAB and ΔOCD.\n1. ∠OAB = ∠OCD (Alternate interior angles as AB || DC and AC is transversal)\n2. ∠OBA = ∠ODC (Alternate interior angles as AB || DC and BD is transversal)\n3. ∠AOB = ∠COD (Vertically opposite angles)\nBy AAA Similarity Criterion (or AA Similarity): ΔOAB ~ ΔOCD.\nSince corresponding sides of similar triangles are proportional:\nOA / OC = OB / OD.\nHence Proved!\n[ROUGH_WORK]\nLook at Figure 6.35 on page 22 in your textbook in the side viewer!\nBoxed Answer: [ Q2: ∠DOC = 55°, ∠DCO = 55°, ∠OAB = 55°; Q3: Proved OA/OC = OB/OD via AA similarity ].",
      figure_id: "Fig. 6.35",
      page: 22,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "In Q2, why does ΔODC ~ ΔOBA imply ∠OAB = ∠OCD and not ∠ODC?",
        "Why is AA similarity sufficient to declare two triangles similar?"
      ]
    },
    {
      problem: "Exercise 6.3 Q4 & Q6 (NCERT Page 22): Q4: In Fig. 6.36, QR / QS = QT / PR and ∠1 = ∠2. Show that ΔPQS ~ ΔTQR. Q6: In Fig. 6.37, if ΔABE ≅ ΔACD, show that ΔADE ~ ΔABC.",
      solution: "Problem 1 (Q4):\nGiven: QR / QS = QT / PR and ∠1 = ∠2 (where ∠1 = ∠PQR and ∠2 = ∠PRQ).\nTo Prove: ΔPQS ~ ΔTQR.\nStep 1: In ΔPQR, since ∠1 = ∠2, the sides opposite equal angles are equal:\nPR = PQ ... (Eq. 1)\nStep 2: Substitute PR = PQ into the given ratio:\nQR / QS = QT / PQ ⇒ taking reciprocal: QS / QR = PQ / QT ⇒ PQ / QT = QS / QR ... (Eq. 2)\nStep 3: Compare ΔPQS and ΔTQR:\nFrom (Eq. 2): PQ / QT = QS / QR (Sides including ∠Q are proportional)\nCommon angle: ∠PQS = ∠TQR = ∠1 (Common)\nTherefore, by SAS Similarity Criterion:\nΔPQS ~ ΔTQR.\nHence Proved!\n\nProblem 2 (Q6):\nGiven: ΔABE ≅ ΔACD.\nStep 1: By CPCT:\nAB = AC ... (Eq. 1)\nAE = AD ⇒ AD = AE ... (Eq. 2)\nStep 2: Divide (Eq. 2) by (Eq. 1):\nAD / AB = AE / AC ... (Eq. 3)\nStep 3: Compare ΔADE and ΔABC:\nFrom (Eq. 3): AD / AB = AE / AC (Two pairs of proportional sides)\nCommon angle: ∠DAE = ∠BAC (Common angle ∠A)\nTherefore, by SAS Similarity Criterion:\nΔADE ~ ΔABC.\nHence Proved!\n[ROUGH_WORK]\nLook at Figure 6.36 and Figure 6.37 on page 22 in your textbook in the side viewer!\nCongruence gives equal lengths, which form ratios for similarity!\nBoxed Answer: [ Q4: Proved ΔPQS ~ ΔTQR via SAS; Q6: Proved ΔADE ~ ΔABC via SAS ].",
      figure_id: "Fig. 6.36",
      page: 22,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "What is the difference between congruence (SSS, SAS, ASA) and similarity (AAA, SSS, SAS)?",
        "Why did substituting PR = PQ unlock the SAS similarity in Q4?"
      ]
    }
  ];

  // Mod 5: Exercise 6.3 Part 2 Solver (Lamp-post, Shadows, Median Proportionality Q9 to Q16)
  const mod5Examples = [
    {
      problem: "Exercise 6.3 Q15 & Example 7 (NCERT Page 20 & 24): Q15: A vertical pole of length 6 m casts a shadow 4 m long on the ground and at the same time a tower casts a shadow 28 m long. Find the height of the tower. Example 7: A girl of height 90 cm is walking away from the base of a lamp-post at a speed of 1.2 m/s. If the lamp is 3.6 m above the ground, find the length of her shadow after 4 seconds.",
      solution: "Problem 1 (Q15 - Sun Shadow Proportionality):\nLet AB be pole = 6 m, BC be shadow = 4 m.\nLet PQ be tower = h m, QR be shadow = 28 m.\nAt the same time, the sun's altitude angle is identical: ∠C = ∠R.\nBoth pole and tower are vertical: ∠B = ∠Q = 90°.\nBy AA Similarity: ΔABC ~ ΔPQR.\nRatio of corresponding sides:\nAB / PQ = BC / QR\n6 / h = 4 / 28\n6 / h = 1 / 7 ⇒ h = 6 × 7 = 42 m.\nHeight of the tower = 42 m.\n\nProblem 2 (Example 7 - Moving Shadow Physics):\nLet AB be lamp-post = 3.6 m.\nLet CD be girl = 90 cm = 0.9 m.\nSpeed = 1.2 m/s. Time = 4 s.\nDistance walked BD = speed × time = 1.2 × 4 = 4.8 m.\nLet length of shadow DE = x metres.\nIn ΔABE and ΔCDE:\n1. ∠B = ∠D = 90°\n2. ∠E = ∠E (Common angle of elevation)\nBy AA Similarity: ΔABE ~ ΔCDE.\nCorresponding sides are proportional:\nAB / CD = BE / DE\n3.6 / 0.9 = (BD + DE) / DE\n4 = (4.8 + x) / x\n4x = 4.8 + x ⇒ 3x = 4.8 ⇒ x = 1.6 m.\nLength of shadow after 4 seconds = 1.6 m.\n[ROUGH_WORK]\n3.6 / 0.9 = 4. Shadow multiplier = 1/3 of distance walked = 4.8 / 3 = 1.6 m!\nBoxed Answer: [ Q15: Height of tower = 42 m; Example 7: Length of shadow = 1.6 m ].",
      figure_id: "Fig. 6.33",
      page: 20,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "Why is the angle of elevation of the sun identical for all objects in the same vicinity at the same instant?",
        "If the girl walks faster, does her shadow length increase or decrease after 4 seconds?"
      ],
      graph_payload: {
        points: [
          { x: 0, y: 3.6, label: "A (Lamp top 3.6m)" },
          { x: 0, y: 0, label: "B (Lamp base)" },
          { x: 4.8, y: 0, label: "D (Girl base)" },
          { x: 4.8, y: 0.9, label: "C (Girl top 0.9m)" },
          { x: 6.4, y: 0, label: "E (Shadow tip)" }
        ],
        segments: [
          { start: [0, 0], end: [0, 3.6], label: "Lamp AB = 3.6m" },
          { start: [0, 0], end: [6.4, 0], label: "Ground BE = 6.4m" },
          { start: [0, 3.6], end: [6.4, 0], label: "Light Ray AE" },
          { start: [4.8, 0], end: [4.8, 0.9], label: "Girl CD = 0.9m" }
        ],
        polygons: [
          { points: [[0, 0], [0, 3.6], [6.4, 0]], label: "ΔABE" },
          { points: [[4.8, 0], [4.8, 0.9], [6.4, 0]], label: "ΔCDE" }
        ]
      }
    },
    {
      problem: "Exercise 6.3 Q12 & Q14 (NCERT Page 23): Q12: Sides AB and BC and median AD of a triangle ABC are respectively proportional to sides PQ and QR and median PM of ΔPQR. Show that ΔABC ~ ΔPQR.",
      solution: "Given: In ΔABC and ΔPQR, AD is median to BC (so BD = DC = BC/2) and PM is median to QR (so QM = MR = QR/2).\nProportionality: AB / PQ = BC / QR = AD / PM ... (Eq. 1)\nTo Prove: ΔABC ~ ΔPQR.\n\nProof:\nStep 1: Express BC and QR using half-sides:\nSince D is midpoint of BC, BC = 2BD.\nSince M is midpoint of QR, QR = 2QM.\nSubstitute into (Eq. 1):\nAB / PQ = (2BD) / (2QM) = AD / PM\nAB / PQ = BD / QM = AD / PM ... (Eq. 2)\n\nStep 2: Apply SSS Similarity to left sub-triangles:\nIn ΔABD and ΔPQM, from (Eq. 2), all three pairs of corresponding sides are proportional.\nBy SSS Similarity Criterion:\nΔABD ~ ΔPQM.\n\nStep 3: Corresponding angles:\nSince ΔABD ~ ΔPQM:\n∠B = ∠Q ... (Eq. 3)\n\nStep 4: Now compare the whole triangles ΔABC and ΔPQR:\nFrom (Eq. 1): AB / PQ = BC / QR\nFrom (Eq. 3): ∠B = ∠Q (Included angle)\nTherefore, by SAS Similarity Criterion:\nΔABC ~ ΔPQR.\nHence Proved!\n[ROUGH_WORK]\nLook at Figure 6.41 on page 23 in your textbook in the side viewer!\nMedian splits base into half, enabling sub-triangle similarity to unlock angle B = Q.\nBoxed Answer: [ Hence Proved: ΔABC ~ ΔPQR using median sub-triangle similarity and SAS ].",
      figure_id: "Fig. 6.41",
      page: 23,
      notesSourceFilename: "jemh106.pdf",
      concept_questions: [
        "Why couldn't we use SAS similarity directly without first analyzing the median triangles?",
        "What is the difference between Question 12 (given BC, QR) and Question 14 (given AC, PR)?"
      ]
    }
  ];

  // Upload to Supabase
  const m1Id = '1c56ecfe-cacd-4d40-b7b5-1c5beb985eec';
  const m3Id = '207e2195-010a-4615-a475-204b84f31962';
  const m4Id = 'ee70b498-d81f-489d-a9af-9727f65c605f';
  const m5Id = '952cce23-9a5e-43ab-80cd-0e6314dfd955';

  await supabase.from('syllabus_modules').update({ worked_examples: mod1Examples }).eq('id', m1Id);
  console.log('✓ Ch 6 Mod 1 updated (Theorems 6.1, 6.2 & Examples 1-3)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod3Examples }).eq('id', m3Id);
  console.log('✓ Ch 6 Mod 3 updated (Exercise 6.1 & 6.2 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod4Examples }).eq('id', m4Id);
  console.log('✓ Ch 6 Mod 4 updated (Exercise 6.3 Part 1 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod5Examples }).eq('id', m5Id);
  console.log('✓ Ch 6 Mod 5 updated (Exercise 6.3 Part 2 Complete)');

  console.log('\n=== CHAPTER 6 ENRICHMENT 100% COMPLETE ===\n');
}

enrichCh6();
