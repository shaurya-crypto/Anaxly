const { supabase } = require('./db_helper');

async function enrichCh9() {
  console.log('=== ENRICHING CLASS 10 MATHS - CHAPTER 9: APPLICATIONS OF TRIGONOMETRY ===\n');

  // Mod 1: Line of Sight, Angle of Elevation & Depression Foundations
  const mod1Examples = [
    {
      problem: "A vertical communication tower stands on level ground. From a point on the ground 30 m away from the foot of the tower, the angle of elevation of the top of the tower is found to be 30°. Find the height of the tower (use √3 ≈ 1.732).",
      solution: "Given: In right-angled triangle ABC, ∠B = 90°.\nDistance from foot of tower BC = 30 m.\nAngle of elevation ∠ACB = 30°.\nTarget: Height of the tower AB = h.\n\nStep 1: Choose trigonometric ratio relating opposite side AB and adjacent side BC:\ntan θ = Opposite / Adjacent = AB / BC\n\nStep 2: Substitute values:\ntan 30° = h / 30\n1 / √3 = h / 30\n\nStep 3: Solve for h:\nh = 30 / √3 = (30 × √3) / 3 = 10√3 m ≈ 17.32 m.\n[ROUGH_WORK]\n30 / 1.732 = 17.32 m. Exact radical form: 10√3 m.\nBoxed Answer: [ The height of the tower is 10√3 m (approx. 17.32 m) ].",
      concept_questions: [
        "Why is tangent the most frequently used trigonometric ratio in height and distance problems?",
        "What is the difference between an angle of elevation and an angle of depression?"
      ],
      graph_payload: {
        points: [
          { x: 0, y: 0, label: "B (Foot of tower)" },
          { x: 30, y: 0, label: "C (Observer, 30°)" },
          { x: 0, y: 17.32, label: "A (Top of tower, 10√3m)" }
        ],
        segments: [
          { start: [0, 0], end: [30, 0], label: "Base BC = 30m" },
          { start: [0, 0], end: [0, 17.32], label: "Height AB = 10√3m" },
          { start: [30, 0], end: [0, 17.32], label: "Line of Sight AC" }
        ],
        polygons: [
          { points: [[0, 0], [30, 0], [0, 17.32]], label: "Right Triangle ABC" }
        ]
      }
    },
    {
      problem: "An observer 1.5 m tall is standing 28.5 m away from a chimney. The angle of elevation of the top of the chimney from her eyes is 45°. What is the height of the chimney?",
      solution: "Let the observer be CD of height 1.5 m (CD = 1.5 m).\nLet the chimney be AB.\nDistance BC = 28.5 m.\nDraw horizontal line DE parallel to BC intersecting AB at E.\nThen DE = BC = 28.5 m, and BE = CD = 1.5 m.\nAngle of elevation from observer's eyes D to top of chimney A: ∠ADE = 45°.\n\nStep 1: In right triangle ADE, ∠AED = 90°:\ntan 45° = AE / DE\n1 = AE / 28.5\nAE = 28.5 m.\n\nStep 2: Total height of the chimney AB:\nAB = AE + EB = 28.5 m + 1.5 m = 30 m.\n[ROUGH_WORK]\nNotice: At 45°, opposite side equals adjacent side (AE = DE = 28.5 m).\nAdding observer's eye height gives full vertical chimney height: 28.5 + 1.5 = 30 m.\nBoxed Answer: [ The total height of the chimney is 30 m ].",
      concept_questions: [
        "Why must the observer's eye height be added to find the full height of the chimney?",
        "If the angle of elevation was 60° instead of 45°, would the chimney be taller or shorter?"
      ]
    }
  ];

  // Mod 3: Single-Object Problems & Baseline Heights (Exercise 9.1 Part 1)
  const mod3Examples = [
    {
      problem: "A circus artist is climbing a 20 m long rope tightly stretched and tied from the top of a vertical pole to the ground. Find the height of the pole if the angle made by the rope with the ground level is 30°.",
      solution: "In right triangle ABC, ∠B = 90°.\nLet AB be vertical pole of height h.\nAC is the rope of length 20 m (AC = 20 m).\nAngle with ground level: ∠ACB = 30°.\n\nStep 1: Select trigonometric ratio relating Opposite (AB) and Hypotenuse (AC):\nsin θ = Opposite / Hypotenuse\nsin 30° = AB / AC\n\nStep 2: Substitute values:\n1/2 = h / 20\nh = 20 / 2 = 10 m.\n[ROUGH_WORK]\nIn any 30°-60°-90° right triangle, the side opposite 30° is always exactly half the hypotenuse!\nBoxed Answer: [ The height of the pole is 10 m ].",
      concept_questions: [
        "Why is sin θ used when hypotenuse is known, whereas tan θ is used when ground distance is known?",
        "What is the length of ground segment BC in this problem?"
      ],
      graph_payload: {
        points: [
          { x: 0, y: 0, label: "B (90°)" },
          { x: 17.32, y: 0, label: "C (Ground, 30°)" },
          { x: 0, y: 10, label: "A (Pole top, 10m)" }
        ],
        segments: [
          { start: [0, 0], end: [17.32, 0], label: "Ground BC = 10√3m" },
          { start: [0, 0], end: [0, 10], label: "Pole AB = 10m" },
          { start: [17.32, 0], end: [0, 10], label: "Rope AC = 20m" }
        ],
        polygons: [
          { points: [[0, 0], [17.32, 0], [0, 10]], label: "ΔABC" }
        ]
      }
    },
    {
      problem: "A tree breaks due to a storm and the broken part bends so that the top of the tree touches the ground making an angle 30° with it. The distance between the foot of the tree to the point where the top touches the ground is 8 m. Find the original height of the tree.",
      solution: "Let the original vertical tree be AC.\nLet it break at point B.\nThe upper broken part AB bends down to touch ground at point A' with ∠BA'C = 30°.\nDistance CA' = 8 m.\nOriginal total height of tree = BC + A'B (since A'B is the broken part AB).\n\nStep 1: Find standing height BC in right ΔBCA':\ntan 30° = BC / CA'\n1 / √3 = BC / 8 ⇒ BC = 8 / √3 m.\n\nStep 2: Find broken length A'B:\ncos 30° = CA' / A'B\n√3 / 2 = 8 / A'B ⇒ A'B = 16 / √3 m.\n\nStep 3: Total original height of tree:\nHeight = BC + A'B = (8 / √3) + (16 / √3) = 24 / √3 m.\nRationalize denominator:\nHeight = (24 × √3) / 3 = 8√3 m ≈ 13.856 m.\n[ROUGH_WORK]\n24 / 1.732 ≈ 13.86 m. 8 + 16 = 24. 24 / √3 = 8√3 m.\nBoxed Answer: [ The original height of the tree is 8√3 m (approx. 13.86 m) ].",
      concept_questions: [
        "Why must both BC (standing part) and A'B (broken part) be computed to find the tree's original height?",
        "Could you find A'B using Pythagoras Theorem once BC was known?"
      ]
    }
  ];

  // Mod 4: Pedestals, Transmission Towers & River Widths (Exercise 9.1 Part 2)
  const mod4Examples = [
    {
      problem: "From a point on the ground, the angles of elevation of the bottom and the top of a transmission tower fixed at the top of a 20 m high building are 45° and 60° respectively. Find the height of the transmission tower.",
      solution: "Let BC be the building of height 20 m (BC = 20 m).\nLet AB be the transmission tower of height h m sitting on top of the building.\nLet D be the observation point on the ground.\nAngle of elevation of bottom of tower (point B): ∠BDC = 45°.\nAngle of elevation of top of tower (point A): ∠ADC = 60°.\n\nStep 1: In right ΔBCD, find ground distance CD:\ntan 45° = BC / CD\n1 = 20 / CD ⇒ CD = 20 m.\n\nStep 2: In right ΔACD, find total height AC:\ntan 60° = AC / CD\n√3 = (AB + BC) / 20 = (h + 20) / 20\nh + 20 = 20√3\nh = 20√3 - 20 = 20(√3 - 1) m.\n\nStep 3: Evaluate numerical approximation:\nh = 20(1.732 - 1) = 20(0.732) = 14.64 m.\n[ROUGH_WORK]\n20 × 0.732 = 14.64 m.\nBoxed Answer: [ The height of the transmission tower is 20(√3 - 1) m (approx. 14.64 m) ].",
      concept_questions: [
        "Why does ground distance CD remain constant for both angle measurements?",
        "How do two different elevation angles from a single point allow solving for the pedestal/tower structure?"
      ],
      graph_payload: {
        points: [
          { x: 0, y: 0, label: "C (Base)" },
          { x: 20, y: 0, label: "D (Observer point)" },
          { x: 0, y: 20, label: "B (Building top, 20m)" },
          { x: 0, y: 34.64, label: "A (Tower top, 20√3m)" }
        ],
        segments: [
          { start: [0, 0], end: [20, 0], label: "Ground CD = 20m" },
          { start: [0, 0], end: [0, 20], label: "Building BC = 20m" },
          { start: [0, 20], end: [0, 34.64], label: "Tower AB = 20(√3-1)m" },
          { start: [20, 0], end: [0, 20], label: "Line of Sight 45°" },
          { start: [20, 0], end: [0, 34.64], label: "Line of Sight 60°" }
        ]
      }
    },
    {
      problem: "Two poles of equal heights are standing opposite each other on either side of an 80 m wide road. From a point between them on the road, the angles of elevation of the tops of the poles are 60° and 30° respectively. Find the height of the poles and the distances of the point from the poles.",
      solution: "Let AB and CD be the two poles of equal height h (AB = CD = h).\nWidth of the road BD = 80 m.\nLet P be the observation point on the road.\nLet BP = x metres. Then PD = (80 - x) metres.\nAngle of elevation of pole AB: ∠APB = 60°.\nAngle of elevation of pole CD: ∠CPD = 30°.\n\nStep 1: In right ΔABP:\ntan 60° = AB / BP\n√3 = h / x ⇒ h = x√3 ... (Eq. 1)\n\nStep 2: In right ΔCDP:\ntan 30° = CD / PD\n1 / √3 = h / (80 - x) ⇒ h = (80 - x) / √3 ... (Eq. 2)\n\nStep 3: Equate expressions for h:\nx√3 = (80 - x) / √3\nx√3 × √3 = 80 - x\n3x = 80 - x\n4x = 80 ⇒ x = 20 m.\n\nStep 4: Find position of P and height h:\nDistance from pole AB: BP = x = 20 m.\nDistance from pole CD: PD = 80 - 20 = 60 m.\nHeight of poles: h = x√3 = 20√3 m ≈ 34.64 m.\n[ROUGH_WORK]\nCheck h from second pole: 60 / √3 = (60√3)/3 = 20√3 m. Exact match!\nBoxed Answer: [ Height of poles = 20√3 m; point is 20 m from first pole and 60 m from second pole ].",
      concept_questions: [
        "Why is equating the unknown height h between the two triangles the key strategy here?",
        "Why is the closer pole associated with the steeper angle of elevation (60° vs 30°)?"
      ]
    }
  ];

  // Mod 5: Dual Observation, Moving Objects & Multi-Storey Buildings (Exercise 9.1 Part 3)
  const mod5Examples = [
    {
      problem: "From the top of a 7 m high building, the angle of elevation of the top of a cable tower is 60° and the angle of depression of its foot is 45°. Determine the height of the tower.",
      solution: "Let AB be the building of height 7 m (AB = 7 m).\nLet CD be the cable tower.\nFrom top of building A, draw horizontal line AE parallel to ground BD, intersecting tower CD at E.\nThen AE = BD, and ED = AB = 7 m.\nAngle of elevation of top of tower C: ∠CAE = 60°.\nAngle of depression of foot of tower D: ∠EAD = 45°.\nNotice alternate interior angle: ∠ADB = ∠EAD = 45°.\n\nStep 1: In right ΔABD, find ground distance BD:\ntan 45° = AB / BD\n1 = 7 / BD ⇒ BD = 7 m.\nTherefore horizontal line AE = 7 m.\n\nStep 2: In right ΔCAE, find upper tower height CE:\ntan 60° = CE / AE\n√3 = CE / 7 ⇒ CE = 7√3 m.\n\nStep 3: Total height of the cable tower CD:\nCD = CE + ED = 7√3 + 7 = 7(√3 + 1) m.\nNumerical value: 7(1.732 + 1) = 7(2.732) = 19.124 m.\n[ROUGH_WORK]\nNotice: Angle of depression 45° gives horizontal distance equal to building height (7 m).\nBoxed Answer: [ The total height of the cable tower is 7(√3 + 1) m (approx. 19.12 m) ].",
      concept_questions: [
        "Why is the angle of depression from top of building to foot of tower equal to the angle of elevation from foot of tower to top of building?",
        "What geometric rectangle is formed by points A, B, D, and E?"
      ],
      graph_payload: {
        points: [
          { x: 0, y: 0, label: "B (Building base)" },
          { x: 0, y: 7, label: "A (Building top 7m)" },
          { x: 7, y: 0, label: "D (Tower base)" },
          { x: 7, y: 7, label: "E (Horizontal level)" },
          { x: 7, y: 19.12, label: "C (Tower top)" }
        ],
        segments: [
          { start: [0, 0], end: [7, 0], label: "Ground BD = 7m" },
          { start: [0, 0], end: [0, 7], label: "Building AB = 7m" },
          { start: [7, 0], end: [7, 19.12], label: "Tower CD = 7(√3+1)m" },
          { start: [0, 7], end: [7, 7], label: "Horizontal AE = 7m" },
          { start: [0, 7], end: [7, 19.12], label: "Elevation 60°" },
          { start: [0, 7], end: [7, 0], label: "Depression 45°" }
        ]
      }
    },
    {
      problem: "A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of 30°, which is approaching the foot of the tower with a uniform speed. Six seconds later, the angle of depression of the car is found to be 60°. Find the time taken by the car to reach the foot of the tower from this point.",
      solution: "Let AB be the tower of height h (AB = h).\nLet the car travel along the horizontal ground towards B.\nInitial position of car = C, angle of depression = 30° ⇒ ∠ACB = 30°.\nPosition after 6 seconds = D, angle of depression = 60° ⇒ ∠ADB = 60°.\nLet uniform speed of car be v m/s.\nDistance traveled CD = speed × time = 6v metres.\nLet time taken from D to foot B be t seconds. Then distance DB = vt metres.\nTotal ground distance CB = CD + DB = 6v + vt = v(6 + t) metres.\n\nStep 1: In right ΔABD:\ntan 60° = AB / DB\n√3 = h / (vt) ⇒ h = vt√3 ... (Eq. 1)\n\nStep 2: In right ΔABC:\ntan 30° = AB / CB\n1 / √3 = h / [v(6 + t)] ⇒ h = v(6 + t) / √3 ... (Eq. 2)\n\nStep 3: Equate h from (Eq. 1) and (Eq. 2):\nvt√3 = v(6 + t) / √3\nCancel v from both sides (v ≠ 0):\nt√3 × √3 = 6 + t\n3t = 6 + t\n2t = 6 ⇒ t = 3 seconds.\n[ROUGH_WORK]\nNotice: Speed v cancels completely! Ground distance from 60° to foot is always half the distance from 30° to 60°!\nBoxed Answer: [ Time taken by the car to reach the foot of the tower from point D is 3 seconds ].",
      concept_questions: [
        "Why does the car's uniform speed v cancel out completely from the final time equation?",
        "If the initial time interval between 30° and 60° was 10 seconds, what would the remaining time be?"
      ]
    }
  ];

  // Upload to Supabase
  const m1Id = '0b6336b2-9c6b-4f82-a5dd-41dfe5b10597';
  const m3Id = '26d140ac-ed9e-402f-b3bc-cf4e60a90c45';
  const m4Id = '3f39468d-55ec-49f6-8f1d-f8e4dae8042f';
  const m5Id = '1c25cd5c-ebfa-40bd-9bd4-e039edaadbb6';

  await supabase.from('syllabus_modules').update({ worked_examples: mod1Examples }).eq('id', m1Id);
  console.log('✓ Ch 9 Mod 1 updated (Foundations & Elevation/Depression)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod3Examples }).eq('id', m3Id);
  console.log('✓ Ch 9 Mod 3 updated (Exercise 9.1 Part 1 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod4Examples }).eq('id', m4Id);
  console.log('✓ Ch 9 Mod 4 updated (Exercise 9.1 Part 2 Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: mod5Examples }).eq('id', m5Id);
  console.log('✓ Ch 9 Mod 5 updated (Exercise 9.1 Part 3 Complete)');

  console.log('\n=== CHAPTER 9 ENRICHMENT 100% COMPLETE ===\n');
}

enrichCh9();
