const fs = require('fs');
const envContent = fs.readFileSync('.env.local', 'utf-8');
const env = {};
envContent.split('\n').forEach(line => {
  const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
  if (match) {
    let val = match[2] || '';
    val = val.trim();
    if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
    env[match[1]] = val.trim();
  }
});
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(env.NEXT_PUBLIC_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY || env.NEXT_PUBLIC_SUPABASE_ANON_KEY);

async function addMissingCh14Exercises() {
  console.log('Auditing and adding missing Chapter 14 exercises (3, 5, 17, 18)...');

  const { data: currs } = await supabase
    .from('curriculums')
    .select('id, title')
    .eq('class_level', 'Class 9')
    .ilike('title', '%Surface Area%');

  const currId = currs[0].id;

  // 1. Fetch Module 1 and Module 6
  const { data: modules } = await supabase
    .from('syllabus_modules')
    .select('*')
    .eq('curriculum_id', currId)
    .in('order_index', [1, 6]);

  const mod1 = modules.find(m => m.order_index === 1);
  const mod6 = modules.find(m => m.order_index === 6);

  // New worked example for Module 1: Exercises 3 & 5
  const newExMod1 = {
    problem: 'Chapter 14, End-of-Chapter Exercises 3 & 5 (Ganita Manjari Part 2, Section 14.7, p. 144):\n(i) Exercise 3 (Godown Packing): The dimensions of a godown are 40 m × 25 m × 10 m. If it is filled with cuboidal boxes, each of dimensions 2 m × 1.25 m × 1 m, find the maximum number of boxes that can be stored in the godown.\n(ii) Exercise 5 (Cube Slicing & Surface Area Scaling): A solid cube of side 4 cm is cut into smaller cubes of side 1 cm. What is the ratio of the surface area of the original cube to the total surface area of all the cut-out cubes? What is the biological significance of this scaling effect?',
    given: '(i) Godown: L = 40 m, W = 25 m, H = 10 m. Box: l = 2 m, w = 1.25 m, h = 1 m.\n(ii) Original cube side a₁ = 4 cm. Smaller cube side a₂ = 1 cm.',
    formula: '(i) Number of boxes N = Volume of godown / Volume of one box = (L × W × H) / (l × w × h).\n(ii) Total Surface Area of cube = 6a²; Number of smaller cubes n = (a₁ / a₂)³ = a₁³ / a₂³; Total SA of cut cubes = n × 6a₂²; Ratio = SA_original / SA_total_cut.',
    substitution: '(i) V_godown = 40 × 25 × 10 = 10,000 m³; V_box = 2 × 1.25 × 1 = 2.5 m³.\n(ii) SA_orig = 6 × (4)² = 96 cm²; n = 4³ / 1³ = 64 cubes; SA_cut = 64 × (6 × 1²) = 384 cm².',
    calculation: 'Step 1 [Exercise 3]:\nCalculate godown volume: V_godown = 40 × 25 × 10 = 10,000 m³.\nCalculate box volume: V_box = 2 × 1.25 × 1 = 2.5 m³.\nCompute count: N = 10,000 / 2.5 = 100,000 / 25 = 4,000 boxes.\n\nStep 2 [Exercise 5]:\nOriginal cube surface area: SA₁ = 6 × 4² = 6 × 16 = 96 cm².\nNumber of cut unit cubes: n = (4 / 1)³ = 64.\nTotal surface area of 64 unit cubes: SA_total = 64 × (6 × 1²) = 384 cm².\nRatio of original SA to total cut SA = 96 / 384 = 1 / 4 (Ratio 1 : 4).\nBiological Insight: When a single solid cell or organism divides into smaller units without changing total volume, its surface-area-to-volume ratio quadruples (4x increase), enabling rapid diffusion of nutrients and oxygen.',
    finalAnswer: '(i) Exercise 3: Exactly 4,000 cuboidal boxes can be stored in the godown.\n(ii) Exercise 5: The ratio of the original cube surface area to the total cut-out surface area is 1 : 4. (Surface area quadruples while volume remains constant).',
    unit: 'boxes & ratio',
    has_diagram: true,
    image_search_query: 'cuboid packing boxes in godown cube cut into smaller cubes diagram'
  };

  // New worked example for Module 6: Exercises 17 & 18
  const newExMod6 = {
    problem: 'Chapter 14, End-of-Chapter Exercises 17 & 18 (Ganita Manjari Part 2, Section 14.7, p. 146):\n(i) Exercise 17 (Culinary & Spherical Fruit Estimation): Estimate how many flat circular chapatis of thickness 2 mm and diameter 16 cm can be rolled out from a spherical lump of dough of radius 8 cm.\n(ii) Exercise 18 (Textbook Space & Storeroom Capacity): Looking at the Ganita Manjari Grade 9 Part 2 textbook (dimensions: 26 cm × 20 cm × 1 cm, 160 pages): (a) If all 160 pages were laid out side-by-side on the floor, would they cover a standard classroom floor of dimensions 8 m × 6 m? (b) What is the maximum number of such textbooks that can fit in a school storeroom of dimensions 15 ft × 20 ft × 30 ft? (Take 1 ft = 30.48 cm).',
    given: '(i) Spherical dough: R = 8 cm. Chapati cylinder: r = 8 cm, h = 2 mm = 0.2 cm.\n(ii) Textbook: l = 26 cm, w = 20 cm, h = 1 cm. Page dimensions: 26 cm × 20 cm, 160 single pages (80 leaves). Classroom floor: 8 m × 6 m = 48 m². Storeroom: 15 ft × 20 ft × 30 ft = 9,000 cu ft.',
    formula: '(i) Volume of sphere V_dough = (4/3)πR³; Volume of one chapati V_chapati = πr²h; Number of chapatis N = V_dough / V_chapati.\n(ii)(a) Total page area A_pages = 160 × (l × w); Compare with Classroom Area = 8 × 6 m².\n(ii)(b) Volume of storeroom V_room = 15 × 20 × 30 ft³; Volume of textbook V_book = 0.26 × 0.20 × 0.01 m³; N_books = V_room / V_book.',
    substitution: '(i) V_dough = (4/3)π(8)³ = (2048/3)π cm³; V_chapati = π(8)²(0.2) = 12.8π cm³.\n(ii)(a) A_pages = 160 × (0.26 × 0.20) = 8.32 m²; Classroom floor = 48 m².\n(ii)(b) V_room = 9,000 ft³ = 9,000 × (0.3048)³ ≈ 254.85 m³; V_book = 0.00052 m³.',
    calculation: 'Step 1 [Exercise 17 - Chapati Estimation]:\nVolume of spherical dough lump: V_dough = (4/3) × π × 8³ = (2048 / 3)π ≈ 682.67π cm³.\nVolume of single rolled chapati (cylinder): V_chapati = π × 8² × 0.2 = 12.8π cm³.\nNumber of chapatis: N = 682.67π / 12.8π = 2048 / 38.4 ≈ 53.3 chapatis (approximately 53 chapatis).\n\nStep 2 [Exercise 18(a) - Page Floor Coverage]:\nArea of one page: A_page = 0.26 m × 0.20 m = 0.052 m².\nTotal area of 160 single pages laid flat: A_total = 160 × 0.052 = 8.32 m².\nClassroom floor area: A_floor = 8 m × 6 m = 48 m².\nComparison: 8.32 m² << 48 m² (the pages cover only ~17.3% of the floor). Therefore, NO, they will not cover the classroom floor.\n\nStep 3 [Exercise 18(b) - Storeroom Capacity]:\nConvert storeroom to SI units: 1 ft = 0.3048 m.\nV_room = (15 × 0.3048) × (20 × 0.3048) × (30 × 0.3048) = 4.572 × 6.096 × 9.144 ≈ 254.85 m³.\nVolume of single textbook: V_book = 0.26 m × 0.20 m × 0.01 m = 0.00052 m³.\nTheoretical maximum packing: N_books = 254.85 / 0.00052 ≈ 490,096 textbooks (approximately 4.9 lakh textbooks).',
    finalAnswer: '(i) Exercise 17: Approximately 53 chapatis can be rolled from the dough lump.\n(ii) Exercise 18: (a) No, all 160 pages laid out cover only 8.32 m², which is far less than the 48 m² classroom floor. (b) The storeroom can accommodate up to ~4.9 lakh textbooks.',
    unit: 'Estimation & Count',
    has_diagram: true,
    image_search_query: 'sphere dough rolling cylindrical chapati textbook stack storeroom volume diagram'
  };

  // Update Module 1
  const updatedMod1Examples = [...mod1.worked_examples, newExMod1];
  const { error: err1 } = await supabase
    .from('syllabus_modules')
    .update({ worked_examples: updatedMod1Examples })
    .eq('id', mod1.id);

  if (err1) console.error('Error updating Module 1:', err1);
  else console.log('✅ Successfully updated Module 1 with Exercises 3 & 5!');

  // Update Module 6
  const updatedMod6Examples = [...mod6.worked_examples, newExMod6];
  const { error: err6 } = await supabase
    .from('syllabus_modules')
    .update({ worked_examples: updatedMod6Examples })
    .eq('id', mod6.id);

  if (err6) console.error('Error updating Module 6:', err6);
  else console.log('✅ Successfully updated Module 6 with Exercises 17 & 18!');
}

addMissingCh14Exercises();
