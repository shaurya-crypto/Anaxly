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

async function seedScienceChapter1() {
  console.log('Seeding Class 9 Science Chapter 1: Exploration...');

  const { data: existing } = await supabase
    .from('curriculums')
    .select('id')
    .eq('class_level', 'Class 9')
    .eq('title', 'Chapter 1: Exploration: Entering the World of Secondary Science');

  if (!existing || existing.length === 0) {
    console.error('Curriculum not found!');
    return;
  }
  const curriculumId = existing[0].id;

  const modules = [
    {
      curriculum_id: curriculumId,
      order_index: 1,
      title: 'The Spirit of Scientific Inquiry & Observation vs Inference',
      description: 'Explore the fundamental foundation of scientific thinking: distinguishing objective sensory observation from subjective mental inference, formulating testable scientific questions, and constructing plausible hypotheses.',
      class_level: 'Class 9',
      board: 'CBSE',
      estimated_minutes: 20,
      ai_system_prompt_context: 'CBSE Class 9 Science Chapter 1 Module 1: The Spirit of Scientific Inquiry & Observation vs Inference. Guide the student to distinguish between direct sensory data and theoretical inferences, formulate testable scientific questions, and construct falsifiable hypotheses using real-life experiments like the rusting of iron nails.',
      key_concepts: [
        'Observation vs Inference: An observation is objective data gathered directly through the five physical senses or measuring instruments; an inference is a logical deduction or explanation constructed to interpret the observed data.',
        'Formulating Testable Questions: Scientific inquiry begins with focused, measurable questions (e.g., "How does temperature affect the rate of seed germination?") rather than untestable opinions.',
        'Hypothesis as a Testable Prediction: A scientific hypothesis is a tentative, testable explanation framed as an "If... then... because..." proposition that can be verified or falsified by empirical testing.',
        'Qualitative vs Quantitative Observations: Qualitative data describes observable qualities (color changes, state changes), whereas quantitative data provides numerical measurements with standardized units.'
      ],
      subtopics: [
        'Sensory Observation vs Mental Deduction',
        'Criteria for Testable Scientific Questions',
        'Hypothesis Construction & Falsifiability',
        'Qualitative vs Quantitative Data Collection'
      ],
      worked_examples: [
        {
          problem: 'Activity 1.1 / Section 1.1: A student observes that iron nails left in a moist open beaker develop a reddish-brown flaky coating over 3 days, whereas identical nails kept in a sealed test tube containing dry silica gel remain shiny. Distinguish the direct observation from the scientific inference, and formulate a testable hypothesis.',
          given: 'Setup A: Moist open beaker with iron nails -> turns reddish-brown in 3 days. Setup B: Sealed tube with dry silica gel -> nails remain shiny.',
          formula: 'Scientific Reasoning: Direct Observation (Sensory Data) vs Logical Inference (Mechanism Deduction).',
          substitution: 'Observation = Visual color change from metallic shiny to reddish-brown flake in Setup A; no change in Setup B. Inference = Moisture and air together cause the chemical corrosion (rusting) of iron.',
          calculation: 'Step 1: Record sensory data (color, texture, timeline) without assuming causes.\nStep 2: Compare experimental vs control setup.\nStep 3: Hypothesize: If iron is exposed simultaneously to both oxygen and water vapor, then corrosion will proceed, because oxidation requires both reactants.',
          finalAnswer: 'Observation: Reddish-brown flaky coating formed only in the presence of air and moisture. Inference: Rusting requires both air and moisture. Hypothesis: If iron is isolated from moisture, then rusting cannot occur.',
          unit: 'Qualitative & Deductive',
          has_diagram: true,
          image_search_query: 'rusting of iron nails experiment test tubes water oil silica gel'
        }
      ],
      visual_lesson_plan: {
        title: 'Scientific Method & Observation vs Inference Flow',
        diagram_idea: 'Flowchart comparing direct sensory observations with logical inferences, leading to hypothesis testing.',
        concept_visuals: [
          {
            concept: 'Observation vs Inference',
            image_search_query: 'scientific method observation hypothesis experiment conclusion diagram',
            video_search_query: 'observation vs inference scientific method animation'
          }
        ]
      },
      quiz_questions: [
        {
          question: 'Which of the following is a pure scientific observation rather than an inference?',
          options: [
            'The liquid boiled because heat increased particle kinetic energy.',
            'The liquid produced bubbles of gas when the temperature reached 100 °C.',
            'The liquid was pure water because it boiled smoothly.',
            'The heat source was too hot for the liquid.'
          ],
          correct_answer: 'The liquid produced bubbles of gas when the temperature reached 100 °C.',
          explanation: 'Recording that bubbles appeared at 100 °C is an objective sensory measurement. Explaining particle energy or identity is an inference.'
        }
      ]
    },
    {
      curriculum_id: curriculumId,
      order_index: 2,
      title: 'Designing Fair Investigations: Variables & Control Groups',
      description: 'Master the design of rigorous scientific experiments by isolating the independent variable, measuring the dependent variable, and maintaining strict control variables.',
      class_level: 'Class 9',
      board: 'CBSE',
      estimated_minutes: 20,
      ai_system_prompt_context: 'CBSE Class 9 Science Chapter 1 Module 2: Designing Fair Investigations: Variables & Control Groups. Emphasize the principle of a fair test where only one variable is changed, define independent, dependent, and controlled variables with concrete laboratory cases, and explain why control groups are required.',
      key_concepts: [
        'The Principle of a Fair Test: In any valid experiment, only one factor must be deliberately altered at a time while all other conditions are kept strictly constant.',
        'Independent Variable (Manipulated): The single factor deliberately changed by the investigator (e.g., concentration of salt solution).',
        'Dependent Variable (Responding): The factor that changes in response and is quantitatively measured (e.g., percentage change in mass of potato strip).',
        'Controlled Variables (Constants): All external factors kept identical across all trials (temperature, volume, container dimensions, duration).',
        'Role of the Control Group: An experimental baseline kept in natural conditions to provide a standard comparison against experimental treatments.'
      ],
      subtopics: [
        'Fair Test Fundamentals',
        'Independent vs Dependent Variables',
        'Identifying and Maintaining Controlled Variables',
        'Baseline Control Groups in Scientific Design'
      ],
      worked_examples: [
        {
          problem: 'Section 1.2 Investigation Design: An experiment is designed to test how temperature affects the rate at which baking soda reacts with vinegar to produce carbon dioxide gas. Identify the independent variable, dependent variable, at least three controlled variables, and the control setup.',
          given: 'Reaction: NaHCO₃ + CH₃COOH -> CH₃COONa + H₂O + CO₂ (gas). Tested at 10°C, 25°C, 40°C, and 60°C.',
          formula: 'Experimental Architecture: Independent Variable -> Causes change in Dependent Variable under Controlled Constants.',
          substitution: 'Independent = Temperature of reactants; Dependent = Time taken for reaction to cease (or volume of CO₂ gas collected per second).',
          calculation: 'Step 1: Identify what is manipulated: Temperature (°C).\nStep 2: Identify what is measured: Volume of gas (mL) collected per unit time (s).\nStep 3: Identify constants: Mass of baking soda (5.0 g), volume of vinegar (50 mL), concentration of vinegar (5% acetic acid), stirring rate.\nStep 4: Establish control group: Room temperature reaction (25°C baseline).',
          finalAnswer: 'Independent Variable: Temperature of vinegar. Dependent Variable: Volume of CO₂ evolved per unit time. Controlled Variables: Mass of baking soda, volume and concentration of vinegar, shape of reaction flask. Control: Baseline test at 25°C.',
          unit: 'Experimental Architecture',
          has_diagram: true,
          image_search_query: 'laboratory apparatus collecting gas displacement of water inverted cylinder'
        }
      ],
      visual_lesson_plan: {
        title: 'Experimental Variables & Controlled Setup Architecture',
        diagram_idea: 'Three-column comparison table and apparatus schematic showing Independent, Dependent, and Controlled variables.',
        concept_visuals: [
          {
            concept: 'Experimental Variables',
            image_search_query: 'independent dependent controlled variables experiment diagram science',
            video_search_query: 'independent vs dependent variables science experiment animation'
          }
        ]
      },
      quiz_questions: [
        {
          question: 'Why must all variables except the independent variable be kept constant during an experiment?',
          options: [
            'To ensure the experiment finishes quickly.',
            'To guarantee that any observed change in the dependent variable is caused solely by the manipulated factor.',
            'To prevent chemical reactions from slowing down.',
            'To make the experimental apparatus look uniform.'
          ],
          correct_answer: 'To guarantee that any observed change in the dependent variable is caused solely by the manipulated factor.',
          explanation: 'Controlling variables ensures a fair test, eliminating confounding factors so cause-and-effect can be established.'
        }
      ]
    },
    {
      curriculum_id: curriculumId,
      order_index: 3,
      title: 'Scientific Measurements, SI Units, Precision & Uncertainty',
      description: 'Acquire rigorous experimental measurement habits: standard SI base and derived units, reading analog scales without parallax error, identifying systematic vs random errors, and reporting experimental uncertainty.',
      class_level: 'Class 9',
      board: 'CBSE',
      estimated_minutes: 20,
      ai_system_prompt_context: 'CBSE Class 9 Science Chapter 1 Module 3: Scientific Measurements, SI Units, Precision & Uncertainty. Teach the standard SI base units, distinguish accuracy from precision with the target-bullseye analogy, explain parallax error during volume readings, and demonstrate how repeat readings reduce random uncertainty.',
      key_concepts: [
        'International System of Units (SI): Standard global measurement system (Length: meter [m], Mass: kilogram [kg], Time: second [s], Temperature: Kelvin [K]).',
        'Precision vs Accuracy: Accuracy indicates how close a measured value is to the true value; precision reflects the reproducibility and degree of exactness among repeated measurements.',
        'Parallax Error: Reading a graduated scale at an angle rather than with the line of sight perpendicular to the meniscus or scale marking.',
        'Systematic vs Random Errors: Systematic errors (e.g., zero error on a balance) shift all readings in one direction; random errors fluctuate unpredictably and are reduced by taking multiple readings and calculating the mean.'
      ],
      subtopics: [
        'SI Base Units & Unit Conversions',
        'Accuracy vs Precision Bullseye Concept',
        'Meniscus Reading & Parallax Elimination',
        'Systematic Zero Errors vs Random Scatter'
      ],
      worked_examples: [
        {
          problem: 'Section 1.3 / Activity 1.3: Five students measure the diameter of a steel ball bearing using a vernier calliper and obtain: 12.4 mm, 12.6 mm, 12.5 mm, 12.4 mm, and 12.6 mm. The manufacturer specification specifies the true diameter as 12.50 mm. Calculate the mean measured diameter, evaluate the accuracy and precision, and state the measurement uncertainty.',
          given: 'Readings: x₁ = 12.4, x₂ = 12.6, x₃ = 12.5, x₄ = 12.4, x₅ = 12.6 mm. True value x_true = 12.50 mm.',
          formula: 'Mean x_mean = (∑ x_i) / n; Range = x_max - x_min; Uncertainty = ± (Range / 2).',
          substitution: 'x_mean = (12.4 + 12.6 + 12.5 + 12.4 + 12.6) / 5 = 62.5 / 5 = 12.50 mm. Range = 12.6 - 12.4 = 0.2 mm.',
          calculation: 'Step 1: Calculate Mean: x_mean = 62.5 / 5 = 12.50 mm.\nStep 2: Assess Accuracy: Mean (12.50 mm) exactly matches the true specification (12.50 mm) -> High Accuracy.\nStep 3: Assess Precision: All values lie within a tight span of 0.2 mm -> High Precision.\nStep 4: Report uncertainty: 12.5 ± 0.1 mm.',
          finalAnswer: 'Mean diameter = 12.50 mm. The measurement shows high accuracy (matches true value) and high precision (low scatter). Reported value: 12.5 ± 0.1 mm.',
          unit: 'mm',
          has_diagram: true,
          image_search_query: 'vernier caliper measuring cylinder reading meniscus parallax error'
        }
      ],
      visual_lesson_plan: {
        title: 'Precision, Accuracy & Meniscus Reading Protocols',
        diagram_idea: 'Dual diagram: Bullseye targets for Accuracy vs Precision, and horizontal eye-level alignment on a graduated cylinder meniscus.',
        concept_visuals: [
          {
            concept: 'Accuracy vs Precision',
            image_search_query: 'accuracy vs precision target diagram bullseye science',
            video_search_query: 'accuracy vs precision scientific measurements animation'
          }
        ]
      },
      quiz_questions: [
        {
          question: 'How should the volume of an aqueous liquid in a graduated glass cylinder be read to avoid parallax error?',
          options: [
            'At the upper curve of the meniscus from slightly above.',
            'At the bottom of the concave meniscus with the eye level directly horizontal to the liquid line.',
            'At the midpoint between upper and lower edges.',
            'From any angle as long as the cylinder is well illuminated.'
          ],
          correct_answer: 'At the bottom of the concave meniscus with the eye level directly horizontal to the liquid line.',
          explanation: 'Water forms a concave meniscus in glass; correct measurement requires viewing horizontally at the bottom of the curve.'
        }
      ]
    },
    {
      curriculum_id: curriculumId,
      order_index: 4,
      title: 'Scientific Models, Data Tables & Graphical Representations',
      description: 'Construct scientific models to visualize abstract and microscopic phenomena, organize multi-trial laboratory data into structured tables, and plot line graphs to reveal empirical mathematical relationships.',
      class_level: 'Class 9',
      board: 'CBSE',
      estimated_minutes: 20,
      ai_system_prompt_context: 'CBSE Class 9 Science Chapter 1 Module 4: Scientific Models, Data Tables & Graphical Representations. Train the student to build structured data tables with brackets for units, assign independent variable to the x-axis and dependent to y-axis, interpret slopes as rates of change, and appreciate the explanatory power and limitations of scientific models.',
      key_concepts: [
        'Role and Limits of Scientific Models: Models (physical, conceptual, mathematical) represent complex or invisible phenomena (e.g., ball-and-stick atomic models, ray diagrams) to explain behavior, but all models have limitations and simplifications.',
        'Structuring Scientific Data Tables: Tables must feature descriptive column headings, explicit symbols, and SI units in header brackets [e.g., "Time t [s]", "Distance s [m]"].',
        'Graphing Independent vs Dependent Variables: Independent variable is always plotted on the horizontal x-axis; dependent variable is plotted on the vertical y-axis.',
        'Interpreting Slopes and Patterns: Linear graphs indicate direct proportionality (y ∝ x); plateaus indicate phase changes or saturation limits.'
      ],
      subtopics: [
        'Purpose and Boundary Limits of Scientific Models',
        'Standard Tabular Formatting for Experimental Data',
        'Coordinate Axis Selection & Scale Calibration',
        'Curve Interpretation: Direct Proportionality vs Asymptotes'
      ],
      worked_examples: [
        {
          problem: 'Section 1.3 / Activity 1.4: During an investigation on cooling, water temperature is recorded every 2 minutes: at t = 0 min, T = 80°C; at t = 2 min, T = 65°C; at t = 4 min, T = 54°C; at t = 6 min, T = 46°C; at t = 8 min, T = 40°C; at t = 10 min, T = 36°C (room temp = 25°C). Tabulate the data, describe the graph shape, and explain why the rate of cooling decreases over time.',
          given: 'Time t [min]: [0, 2, 4, 6, 8, 10]; Temp T [°C]: [80, 65, 54, 46, 40, 36]; Room temp = 25°C.',
          formula: 'Newton\'s Law of Cooling / Empirical observation: Rate of heat loss dQ/dt ∝ (T - T_room).',
          substitution: 'ΔT in first 2 min = 80 - 65 = 15°C. ΔT in last 2 min = 40 - 36 = 4°C.',
          calculation: 'Step 1: Calculate temperature drop per interval: (0-2m: 15°C), (2-4m: 11°C), (4-6m: 8°C), (6-8m: 6°C), (8-10m: 4°C).\nStep 2: Note decreasing slope: The curve is steep initially and flattens asymptotically towards ambient room temperature (25°C).\nStep 3: Scientific reasoning: Heat transfer rate is directly proportional to temperature difference (T - T_room). As water cools, the gradient narrows, slowing cooling.',
          finalAnswer: 'The cooling curve is exponentially decaying. Initial cooling rate is 7.5°C/min; final cooling rate slows to 2.0°C/min because heat transfer slows as temperature approaches room equilibrium.',
          unit: '°C/min',
          has_diagram: true,
          image_search_query: 'cooling curve of hot water temperature time graph asymptotic'
        }
      ],
      visual_lesson_plan: {
        title: 'Scientific Data Tables & Coordinate Graph Plotting',
        diagram_idea: 'Dual panel: Tabular data representation alongside a continuous non-linear cooling curve showing tangent slopes.',
        concept_visuals: [
          {
            concept: 'Scientific Graphs',
            image_search_query: 'scientific graph axes independent dependent variable line of best fit',
            video_search_query: 'how to plot scientific graph line of best fit animation'
          }
        ]
      },
      quiz_questions: [
        {
          question: 'Why do scientists construct physical or digital models of atoms and solar systems even though they are not 100% exact?',
          options: [
            'Because real objects cannot be photographed.',
            'Because models allow scientists to visualize unobservable scales, make predictions, and communicate mechanisms.',
            'Because models replace the need to perform real experiments.',
            'Because mathematical equations are always inaccurate.'
          ],
          correct_answer: 'Because models allow scientists to visualize unobservable scales, make predictions, and communicate mechanisms.',
          explanation: 'Models simplify complex reality to make mechanisms understandable, testable, and communicable.'
        }
      ]
    },
    {
      curriculum_id: curriculumId,
      order_index: 5,
      title: 'Evidence-Based Deductions & Chapter Review Exercises',
      description: 'Synthesize all foundational scientific inquiry principles: distinguishing correlation from causation, drawing evidence-backed conclusions, peer review, and solving all chapter-end exercise problems.',
      class_level: 'Class 9',
      board: 'CBSE',
      estimated_minutes: 25,
      ai_system_prompt_context: 'CBSE Class 9 Science Chapter 1 Module 5: Evidence-Based Deductions & Chapter Review Exercises. Focus on the distinction between correlation and causation (the ice-cream and drowning fallacy), the Claim-Evidence-Reasoning (CER) framework, laboratory safety essentials, and step-by-step solving of all chapter exercises.',
      key_concepts: [
        'Correlation vs Causation: Just because two variables change together (correlation) does not prove that one causes the other (causation); a controlled mechanism is required.',
        'Evidence-Based Conclusion Framework: Claim (what you assert) -> Evidence (empirical data collected) -> Reasoning (scientific laws explaining why the evidence supports the claim).',
        'Replication and Peer Review: An experimental finding is scientifically acceptable only if other independent laboratories can replicate the exact procedure with matching results.',
        'Safety Protocols in School Science Laboratories: Personal protective equipment (goggles, lab aprons), proper chemical handling, wafting vapors rather than inhaling, and waste disposal.'
      ],
      subtopics: [
        'Correlation vs Causation & Confounding Variables',
        'The Claim-Evidence-Reasoning (CER) Protocol',
        'Peer Review & Experimental Reproducibility',
        'Laboratory Safety & Hazard Protocols'
      ],
      worked_examples: [
        {
          problem: 'Chapter End Exercise 1: A researcher observes that cities with higher ice cream sales also report higher frequencies of drowning incidents. Explain why concluding that "eating ice cream causes drowning" is a logical fallacy, and identify the confounding variable.',
          given: 'Correlation: Ice cream sales increase in parallel with drowning incidents.',
          formula: 'Scientific Reasoning: Correlation ≠ Causation; evaluate confounding third variables (lurking variables).',
          substitution: 'Confounding variable = Hot summer weather / High ambient temperature.',
          calculation: 'Step 1: Identify variable A (Ice cream consumption) and variable B (Drowning incidents).\nStep 2: Evaluate physical mechanism: Eating ice cream does not impair swimming ability to cause drowning.\nStep 3: Identify common underlying driver: Warm summer weather causes more people to buy ice cream AND causes far more people to swim in lakes and oceans, elevating exposure to drowning hazards.',
          finalAnswer: 'The conclusion is a false cause fallacy (cum hoc ergo propter hoc). The two variables are correlated due to a common third confounding variable: hot summer weather.',
          unit: 'Critical Reasoning',
          has_diagram: true,
          image_search_query: 'correlation vs causation scatter plot confounding variable illustration'
        },
        {
          problem: 'Chapter End Exercise 2: State three essential laboratory safety rules when heating a test tube containing a volatile liquid over a Bunsen burner.',
          given: 'Laboratory heating of test tube with volatile chemical.',
          formula: 'Standard School Laboratory Safety Protocol (CBSE/NCERT).',
          substitution: 'Safety steps: Goggles, test tube holder, pointing mouth of tube away from all persons, gentle agitation in water bath.',
          calculation: 'Step 1: Always use a water bath when heating volatile or flammable liquids (never direct open flame).\nStep 2: Hold tube with test-tube holder at 45° angle, pointing open mouth away from oneself and lab partners.\nStep 3: Wear protective chemical splash goggles at all times.',
          finalAnswer: '1. Use an indirect water bath instead of a direct flame. 2. Point the open mouth away from all persons at a 45° angle. 3. Wear protective splash goggles.',
          unit: 'Safety Protocol',
          has_diagram: false
        }
      ],
      visual_lesson_plan: {
        title: 'Correlation vs Causation & Lab Safety Mandate',
        diagram_idea: 'Triangular flowchart showing Confounding Variable (Heat) driving both Ice Cream and Drowning, plus lab safety icon infographic.',
        concept_visuals: [
          {
            concept: 'Correlation vs Causation',
            image_search_query: 'correlation does not imply causation third variable diagram',
            video_search_query: 'correlation vs causation explained clearly animation'
          }
        ]
      },
      quiz_questions: [
        {
          question: 'What is the most critical requirement before an experimental claim can be accepted as a valid scientific finding?',
          options: [
            'It must be published in a popular social media blog.',
            'It must be independently replicated and confirmed by other researchers using the same experimental procedure.',
            'It must use the most expensive laboratory apparatus available.',
            'It must agree with common intuition without contradicting older theories.'
          ],
          correct_answer: 'It must be independently replicated and confirmed by other researchers using the same experimental procedure.',
          explanation: 'Replicability under peer review is the cornerstone of empirical science.'
        }
      ]
    }
  ];

  for (const mod of modules) {
    const { data: inserted, error: iErr } = await supabase.from('syllabus_modules').insert(mod).select('id, title');
    if (iErr) {
      console.error(`Error inserting module ${mod.order_index}:`, iErr);
    } else {
      console.log(`Inserted module ${mod.order_index}: ${inserted[0].title} (ID: ${inserted[0].id})`);
    }
  }

  console.log('✅ Class 9 Science Chapter 1 modules inserted successfully!');
}

seedScienceChapter1();
