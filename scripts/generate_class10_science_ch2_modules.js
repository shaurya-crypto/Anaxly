/**
 * generate_class10_science_ch2_modules.js
 * Synthesizes 5 exhaustive, publication-grade modules for Class 10 Science Chapter 2: Acids, Bases and Salts
 * strictly adhering to Invariant 10 and 11, with pure typography and dynamic search queries.
 */

const { supabase } = require('./db_helper');

const CH2_MODULES = [
  {
    order_index: 1,
    title: 'Indicators & Chemical Properties of Acids and Bases: Metal Reactions, Carbonate Action & Neutralisation',
    description: 'Explore natural, synthetic, and olfactory indicators. Master acid and base reactions with active metals (hydrogen gas evolution and pop sound test), metal carbonates and hydrogen carbonates (effervescence and lime water test), and the fundamental neutralisation reaction.',
    subtopics: [
      'Natural indicators (Litmus, turmeric, red cabbage) vs synthetic indicators (Phenolphthalein, Methyl Orange)',
      'Olfactory indicators (vanilla essence, chopped onion, clove oil) for sensory detection of acids and bases',
      'Reaction of active metals with acids: Zn + 2HCl → ZnCl₂ + H₂↑ (Laboratory setup and pop-test detection)',
      'Reaction of amphoteric bases with metals: 2NaOH + Zn → Na₂ZnO₂ (Sodium zincate) + H₂↑',
      'Action of acids on metal carbonates: Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂↑',
      'Action of acids on metal hydrogen carbonates: NaHCO₃ + HCl → NaCl + H₂O + CO₂↑',
      'Lime water confirmatory test: Ca(OH)₂ + CO₂ → CaCO₃↓ (milky precipitate) + H₂O',
      'Effect of excess carbon dioxide: CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂ (soluble clear solution)',
      'Neutralisation reaction: Acid + Base → Salt + Water (HCl + NaOH → NaCl + H₂O)',
      'Reaction of metallic oxides with acids (CuO + 2HCl → CuCl₂ + H₂O: Basic nature of metal oxides)',
      'Reaction of non-metallic oxides with bases (Ca(OH)₂ + CO₂ → CaCO₃ + H₂O: Acidic nature of non-metal oxides)'
    ],
    key_concepts: [
      'Acid-Base Indicators: Substances that change color or odor in acidic or basic media. Litmus turns red in acid and blue in base; phenolphthalein remains colorless in acid and turns pink in base; methyl orange turns red in acid and yellow in base.',
      'Active Metal Displacement: Acids react with metals situated above hydrogen in the reactivity series to produce salt and liberate hydrogen gas: Acid + Metal → Salt + H₂↑.',
      'Carbonate & Hydrogen Carbonate Reaction: All metal carbonates and hydrogen carbonates react with acids to give a corresponding salt, carbon dioxide, and water: Metal Carbonate/Bicarbonate + Acid → Salt + CO₂↑ + H₂O.',
      'Carbon Dioxide Confirmatory Test: Passing CO₂ gas through lime water turns it milky due to insoluble calcium carbonate formation; prolonged bubbling clears the turbidity as soluble calcium hydrogen carbonate forms.',
      'Neutralisation Equilibrium: The reaction between an acid and a base giving salt and water: H⁺(aq) + OH⁻(aq) → H₂O(l).'
    ],
    success_criteria: 'Student can classify indicators, write balanced molecular equations for acid-metal and acid-carbonate reactions, explain the lime water test, and derive the neutralisation law.',
    chapter_notes: `### 2.1 Understanding Acids, Bases and Indicators
Acids are sour in taste and change the colour of blue litmus to red. Bases are bitter in taste, soapy to touch, and change red litmus to blue.

#### 1. Chemical Indicators
- **Natural Indicators**: Litmus (extracted from lichens, purple neutral dye), Turmeric (turns reddish-brown with base), Red cabbage juice.
- **Synthetic Indicators**: 
  - *Phenolphthalein*: Colourless in acidic/neutral solution; bright pink in basic solution.
  - *Methyl Orange*: Red in acidic solution; yellow in neutral/basic solution.
- **Olfactory Indicators**: Substances whose odour changes in acidic or basic media (onion extract, vanilla essence, clove oil).

#### 2. Reactions with Active Metals
$$\\text{Acid} + \\text{Metal} \\to \\text{Salt} + \\text{H}_2\\uparrow$$
$$2\\text{HCl}(aq) + \\text{Zn}(s) \\to \\text{ZnCl}_2(aq) + \\text{H}_2(g)$$
$$\\text{H}_2\\text{SO}_4(aq) + \\text{Zn}(s) \\to \\text{ZnSO}_4(aq) + \\text{H}_2(g)$$
- *Hydrogen Gas Test*: Bring a burning candle near the mouth of the test tube. The gas burns with a characteristic **'pop' sound**.
- *Reaction with strong base*:
$$2\\text{NaOH}(aq) + \\text{Zn}(s) \\to \\text{Na}_2\\text{ZnO}_2(aq) \\text{ (Sodium zincate)} + \\text{H}_2(g)$$

#### 3. Reactions with Metal Carbonates and Metal Hydrogen Carbonates
$$\\text{Metal Carbonate} + \\text{Acid} \\to \\text{Salt} + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}$$
$$\\text{Na}_2\\text{CO}_3(s) + 2\\text{HCl}(aq) \\to 2\\text{NaCl}(aq) + \\text{H}_2\\text{O}(l) + \\text{CO}_2(g)$$
$$\\text{NaHCO}_3(s) + \\text{HCl}(aq) \\to \\text{NaCl}(aq) + \\text{H}_2\\text{O}(l) + \\text{CO}_2(g)$$

#### 4. The Lime Water Confirmatory Test for $\\text{CO}_2$
When the evolved gas is passed through lime water (calcium hydroxide solution):
$$\\text{Ca(OH)}_2(aq) + \\text{CO}_2(g) \\to \\text{CaCO}_3(s) \\downarrow \\text{ (Milky precipitate)} + \\text{H}_2\\text{O}(l)$$
On passing excess $\\text{CO}_2$, the milky solution turns completely clear:
$$\\text{CaCO}_3(s) + \\text{H}_2\\text{O}(l) + \\text{CO}_2(g) \\to \\text{Ca(HCO}_3)_2(aq) \\text{ (Soluble calcium bicarbonate)}$$

#### 5. Neutralisation & Oxide Reactions
$$\\text{Acid} + \\text{Base} \\to \\text{Salt} + \\text{Water}$$
$$\\text{HCl}(aq) + \\text{NaOH}(aq) \\to \\text{NaCl}(aq) + \\text{H}_2\\text{O}(l)$$
- **Metallic oxides are basic in nature**:
$$\\text{CuO}(s) \\text{ (Black)} + 2\\text{HCl}(aq) \\to \\text{CuCl}_2(aq) \\text{ (Blue-green solution)} + \\text{H}_2\\text{O}(l)$$
- **Non-metallic oxides are acidic in nature**:
$$\\text{Ca(OH)}_2(aq) + \\text{CO}_2(g) \\to \\text{CaCO}_3(s) + \\text{H}_2\\text{O}(l)$$`,
    worked_examples: [
      {
        problem: 'Textbook Example: A metal compound A reacts with dilute hydrochloric acid to produce effervescence. The gas evolved extinguishes a burning candle and turns lime water milky. Write a balanced chemical equation for the reaction if one of the compounds formed is calcium chloride.',
        given: 'Metal compound A + dilute HCl -> effervescence. Gas extinguishes candle and turns lime water milky. Salt formed = CaCl₂.',
        formula: 'Gas that extinguishes candle and turns lime water milky is CO₂. Carbonates react with acid to give CO₂ and CaCl₂.',
        substitution: 'Compound A = Calcium carbonate (CaCO₃). Acid = HCl.',
        calculation: 'Step 1: The gas that extinguishes fire and turns lime water milky is carbon dioxide (CO₂).\nStep 2: Since calcium chloride (CaCl₂) is one product, the metal must be calcium (Ca).\nStep 3: Metal carbonate + Acid -> Salt + Water + CO₂.\nStep 4: Equation: CaCO₃(s) + 2HCl(aq) -> CaCl₂(aq) + H₂O(l) + CO₂(g)↑.',
        finalAnswer: 'Compound A is Calcium Carbonate (CaCO₃). Balanced equation: CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂↑.',
        unit: 'chemical reaction',
        has_diagram: false
      }
    ],
    common_misconceptions: [
      'Thinking that all metals react with bases to produce hydrogen gas (only amphoteric metals like Zn and Al react with strong alkalis).',
      'Assuming that limestone, chalk, and marble are chemically different compounds (all are physical forms of calcium carbonate CaCO₃).'
    ],
    visual_lesson_plan: {
      syllabus_term: 'Mid-Term Examination',
      syllabus_pacing: 'Mid-Term Examination Syllabus',
      concept_visuals: [
        {
          concept_title: 'Acid-Metal Reaction & Hydrogen Evolution',
          diagram_title: 'Laboratory Preparation of Hydrogen Gas with Pop-Sound Test',
          image_search_query: 'reaction of zinc granules with dilute sulphuric acid laboratory apparatus pop sound test',
          video_search_query: 'reaction of zinc with dilute acid testing hydrogen gas pop sound demonstration',
          diagram_type: 'image_search',
          what_to_explain: 'Demonstrate zinc granules reacting with dilute acid in a test tube fitted with a delivery tube passing through soap solution, forming hydrogen bubbles that pop with a flame.'
        },
        {
          concept_title: 'Lime Water Test for Carbon Dioxide',
          diagram_title: 'Carbon Dioxide Evolution and Lime Water Milkiness Test',
          image_search_query: 'passing carbon dioxide gas through lime water apparatus test tube demonstration',
          video_search_query: 'testing carbon dioxide gas with lime water chemistry experiment',
          diagram_type: 'image_search',
          what_to_explain: 'Explain the formation of insoluble calcium carbonate causing milkiness, followed by dissolution on excess CO2.'
        }
      ],
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Acid Reactions & Indicators',
          questions: [
            {
              question: 'Why should curd and sour substances not be kept in brass and copper vessels?',
              type: 'short_answer',
              ideal_answer: 'Curd and sour substances contain organic acids (such as lactic acid). These acids react with brass and copper to form toxic, poisonous metallic salts that can cause severe food poisoning.',
              socratic_hint: 'Recall that acids react with metals situated above hydrogen to form salts.'
            },
            {
              question: 'Which gas is usually liberated when an acid reacts with a metal? Illustrate with an example and describe how to test for the gas.',
              type: 'short_answer',
              ideal_answer: 'Hydrogen gas (H₂) is liberated. Example: Zn + H₂SO₄ → ZnSO₄ + H₂↑. Test: Bring a burning splinter near the mouth of the gas collection tube; it burns with a distinctive pop sound.',
              socratic_hint: 'Think about what gas creates acoustic pops when ignited in air.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 2,
    title: 'The Molecular Nature of Acidic & Basic Solutions: Hydronium Ions (H₃O⁺), Dilution Thermodynamics & Electrolytic Conduction',
    description: 'Investigate what all acids and bases have in common at the submicroscopic scale. Prove that acidity requires aqueous ionisation (why dry HCl gas fails to affect dry litmus), analyze electrolytic conduction through ions, and master the exothermic thermodynamics of dilution.',
    subtopics: [
      'Electrolytic conduction through acids: The beaker circuit experiment with bulb and battery',
      'Why glucose (C₆H₁₂O₆) and alcohol (C₂H₅OH) solutions do not conduct electricity despite containing hydrogen',
      'The imperative role of water in acid dissociation: Dry HCl gas vs moist blue litmus paper',
      'Hydronium ion formation: H⁺ cannot exist independently and binds with H₂O to form H₃O⁺',
      'Base dissociation in aqueous medium: Generation of hydroxide ions OH⁻(aq)',
      'Definition of Alkalis: Bases that dissolve in water (NaOH, KOH, Ca(OH)₂, Mg(OH)₂)',
      'Thermodynamics of acid dilution: Strongly exothermic dissolution kinetics',
      'Safety protocol for dilution: Always add concentrated acid dropwise to water with continuous stirring'
    ],
    key_concepts: [
      'Ionic Conduction: Acids conduct electricity in aqueous solutions because they dissociate into free-moving cations (H₃O⁺) and anions (e.g. Cl⁻, SO₄²⁻).',
      'Covalent Non-Electrolytes: Compounds like glucose and ethyl alcohol have covalently bonded hydrogen that does not ionise in water; hence, they do not conduct electricity or show acidic properties.',
      'Hydronium Ion Invariant: Hydrogen ions H⁺ are bare protons with high charge density that immediately hydrate in aqueous solutions: HCl + H₂O → H₃O⁺ + Cl⁻.',
      'Alkalis: Soluble bases that produce OH⁻ ions in solution. All alkalis are bases, but not all bases are alkalis (e.g. Fe(OH)₃ is a base but insoluble in water).',
      'Dilution Rule: Dilution decreases the concentration of ions (H₃O⁺ / OH⁻) per unit volume. The process is intensely exothermic; adding water to concentrated acid can cause local superheating, flash boiling, and violent splatter.'
    ],
    success_criteria: 'Student can explain why alcohol is not an acid, write the hydration reaction of H⁺ to H₃O⁺, and explain the safety rationale for acid dilution.',
    chapter_notes: `### 2.2 What Do All Acids and All Bases Have in Common?

#### 1. Electric Conductivity in Acid Solutions
- When an electric circuit containing a battery, bulb, and switch is connected to two graphite/iron electrodes immersed in dilute $\\text{HCl}$ or dilute $\\text{H}_2\\text{SO}_4$, the **bulb glows brightly**.
- The electric current is carried through the solution by **ions**:
$$\\text{HCl}(aq) \\to \\text{H}^+(aq) + \\text{Cl}^-(aq)$$
$$\\text{HNO}_3(aq) \\to \\text{H}^+(aq) + \\text{NO}_3^-(aq)$$
- In contrast, when the experiment is repeated with **glucose** ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) or **alcohol** ($\\text{C}_2\\text{H}_5\\text{OH}$), the bulb **does NOT glow**. Even though they contain hydrogen atoms, their covalent bonds do not dissociate into free ions in water.

#### 2. Do Acids Produce Ions Only in Aqueous Solution?
- When dry $\\text{NaCl}$ is treated with concentrated $\\text{H}_2\\text{SO}_4$, dry $\\text{HCl}$ gas is generated:
$$\\text{NaCl}(s) + \\text{H}_2\\text{SO}_4(l) \\to \\text{NaHSO}_4(s) + \\text{HCl}(g)$$
- If dry $\\text{HCl}$ gas is brought in contact with **dry blue litmus paper**, there is **NO change in colour**.
- When exposed to **moist blue litmus paper**, it turns **bright red**.
- **Reason**: Separation of $\\text{H}^+$ ion from $\\text{HCl}$ molecules occurs only in the presence of water:
$$\\text{HCl} + \\text{H}_2\\text{O} \\to \\text{H}_3\\text{O}^+ \\text{ (Hydronium ion)} + \\text{Cl}^-$$
- Free $\\text{H}^+$ ions cannot exist independently because they are bare protons; they combine with water molecules to form **hydronium ions** $\\text{H}_3\\text{O}^+$.

#### 3. Dissociation of Bases in Water
Bases generate hydroxide ions $\\text{OH}^-(aq)$ in water:
$$\\text{NaOH}(s) \\xrightarrow{\\text{H}_2\\text{O}} \\text{Na}^+(aq) + \\text{OH}^-(aq)$$
$$\\text{KOH}(s) \\xrightarrow{\\text{H}_2\\text{O}} \\text{K}^+(aq) + \\text{OH}^-(aq)$$
$$\\text{Mg(OH)}_2(s) \\xrightarrow{\\text{H}_2\\text{O}} \\text{Mg}^{2+}(aq) + 2\\text{OH}^-(aq)$$
- Bases that are soluble in water are called **alkalis**.

#### 4. Dilution Thermodynamics & Safe Protocol
Mixing an acid or base with water results in decrease in the concentration of ions ($\\text{H}_3\\text{O}^+ / \\text{OH}^-$) per unit volume. This process is called **dilution**.
- **Safety Precaution**: The acid must ALWAYS be added slowly to water with constant stirring.
- *Why not water to acid?* If water is added to concentrated acid, the heat generated is so intense that the mixture may splash out, causing severe chemical burns, and the glass container may break due to excessive local thermal expansion.`,
    worked_examples: [
      {
        problem: 'Textbook In-Text Question: Why does an aqueous solution of an acid conduct electricity, whereas a solution of glucose does not?',
        given: 'Aqueous solutions of an acid (e.g. HCl) and glucose (C₆H₁₂O₆).',
        formula: 'Electrical conduction in liquids requires mobile charged ions.',
        substitution: 'HCl(aq) dissociates into H⁺/H₃O⁺ and Cl⁻ ions; glucose does not ionise.',
        calculation: 'Step 1: An electric current in a liquid solution is transported by the movement of mobile ions toward oppositely charged electrodes.\nStep 2: In aqueous solution, acids ionise completely or partially to release mobile hydronium ions (H₃O⁺) and negative counter-ions.\nStep 3: Glucose (C₆H₁₂O₆) is a covalent molecular compound. In water, it dissolves without breaking into ions; no free charged particles exist to transport electrical current.',
        finalAnswer: 'Aqueous acid conducts electricity because it produces mobile ions (H₃O⁺ and acid anions); glucose dissolves as neutral covalent molecules without generating free ions.',
        unit: 'conceptual deduction',
        has_diagram: false
      }
    ],
    common_misconceptions: [
      'Believing that all hydrogen-containing substances are acidic (glucose and alcohol contain hydrogen but are neutral non-electrolytes).',
      'Thinking that H⁺ exists as a free bare proton floating in aqueous solution (it is always bonded as H₃O⁺ or higher hydrates).'
    ],
    visual_lesson_plan: {
      syllabus_term: 'Mid-Term Examination',
      syllabus_pacing: 'Mid-Term Examination Syllabus',
      concept_visuals: [
        {
          concept_title: 'Electric Conduction in Acid Solution',
          diagram_title: 'Beaker Circuit Showing Acid Conductivity vs Glucose Non-Conductivity',
          image_search_query: 'acid solution conducts electricity beaker bulb battery apparatus experiment diagram',
          video_search_query: 'do acids conduct electricity beaker bulb experiment class 10 science',
          diagram_type: 'image_search',
          what_to_explain: 'Show the beaker with carbon electrodes, battery, and glowing bulb in dilute HCl versus unlit bulb in glucose solution.'
        },
        {
          concept_title: 'Dry HCl Gas vs Moist Litmus Test',
          diagram_title: 'Preparation of Dry HCl Gas and Action on Dry vs Moist Litmus Paper',
          image_search_query: 'preparation of hydrochloric acid gas testing with dry and wet litmus paper diagram',
          video_search_query: 'action of dry hcl gas on dry and moist litmus paper experiment',
          diagram_type: 'image_search',
          what_to_explain: 'Demonstrate that dry HCl gas has zero effect on dry blue litmus, while turning moist blue litmus instantly red due to hydronium ion formation.'
        }
      ],
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Ionisation and Dilution',
          questions: [
            {
              question: 'Why does dry HCl gas not change the colour of dry litmus paper?',
              type: 'short_answer',
              ideal_answer: 'Dry HCl gas does not contain free hydrogen or hydronium ions (H₃O⁺). Ionisation can occur only in the presence of water: HCl + H₂O → H₃O⁺ + Cl⁻. Without water, no acidic character is exhibited.',
              socratic_hint: 'What medium is required for HCl to split into ions?'
            },
            {
              question: 'While diluting an acid, why is it recommended that the acid should be added to water and not water to the acid?',
              type: 'short_answer',
              ideal_answer: 'The dilution of concentrated acid with water is an extremely exothermic process. If water is poured into acid, a large burst of heat is produced in a small volume, causing the acid to flash boil, spatter violently, and potentially shatter the glass container.',
              socratic_hint: 'Consider the high heat capacity of water when absorbing exothermic heat.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 3,
    title: 'Quantitative Acidity: The Universal Indicator, pH Scale (0–14), Logarithmic Hydronium Concentration & Real-Life Significance',
    description: 'Master quantitative measurements of acidity and basicity using universal indicator and the pH scale (0 to 14). Differentiate strong versus weak acids, understand logarithmic hydronium concentration relationships, and explore the crucial role of pH in living organisms, digestion, soil health, and tooth decay.',
    subtopics: [
      'Universal indicator: A mixture of several indicators providing a graded spectrum of color across pH values',
      'The pH scale: Definition from German "potenz" (power); pH = -log₁₀[H⁺]',
      'The neutral benchmark: Pure water at 25°C has [H⁺] = [OH⁻] = 10⁻⁷ M, hence pH = 7',
      'Acidic spectrum (pH < 7) vs Basic/Alkaline spectrum (pH > 7)',
      'Strong acids (HCl, HNO₃, H₂SO₄) vs Weak acids (CH₃COOH, citric, oxalic)',
      'Strong bases (NaOH, KOH) vs Weak bases (NH₄OH, Mg(OH)₂)',
      'pH in human physiology: Blood pH homeostasis (7.35–7.45) and digestive gastric juice (pH ~ 1.2–3.0)',
      'Acid rain: Rainwater with pH < 5.6 and its devastating ecological impact on aquatic ecosystems',
      'Soil pH and agricultural liming: Treatment of acidic soil with CaO, Ca(OH)₂, or CaCO₃',
      'Tooth decay mechanics: Dissolution of enamel Ca₅(PO₄)₃OH below critical threshold pH 5.5',
      'Natural self-defense: Methanoic acid in bee and nettle stings, neutralized by mild bases (baking soda, dock plant)'
    ],
    key_concepts: [
      'The pH Concept: A logarithmic measure of the concentration of free hydronium ions in solution. Lower pH represents higher [H₃O⁺] concentration; every one-unit decrease represents a tenfold increase in hydronium ion concentration.',
      'Strong vs Weak Acid Dissociation: Strong acids dissociate virtually 100% into ions in aqueous solution; weak acids reach an equilibrium where only a small percentage of molecules dissociate.',
      'Physiological pH Tolerance: Living organisms function within a narrow pH range (7.0 to 7.8). Deviations disrupt enzyme conformation and cellular metabolism.',
      'Digestive Acidity & Antacids: The stomach produces hydrochloric acid to activate pepsin. During indigestion, excess acid causes pain, which is neutralized by mild non-corrosive bases called antacids (e.g. Mg(OH)₂ or NaHCO₃).',
      'Enamel Demineralization: Tooth enamel (calcium hydroxyapatite) is the hardest substance in the human body, but undergoes demineralisation when mouth bacteria ferment sugar into lactic acid below pH 5.5.'
    ],
    success_criteria: 'Student can read pH color charts, calculate relative [H⁺] concentration ratios, explain physiological pH buffers, and describe the biochemical causes of tooth decay.',
    chapter_notes: `### 2.3 How Strong Are Acid or Base Solutions?

#### 1. Universal Indicator & The pH Scale
A **universal indicator** is a blend of several indicators that exhibits different colours at different concentrations of hydrogen ions in a solution.
- The scale measuring hydrogen ion concentration is called the **pH scale** ($p$ for *potenz* in German, meaning power):
$$\\text{pH} = -\\log_{10}[\\text{H}^+]$$
- At $25^\\circ\\text{C}$ in neutral pure water: $[\\text{H}^+] = [\\text{OH}^-] = 10^{-7}\\text{ mol/L} \\implies \\text{pH} = 7$.
- **Acidic solutions**: $[\\text{H}^+] > 10^{-7}\\text{ mol/L} \\implies \\mathbf{\\text{pH} < 7}$.
- **Neutral solutions**: $\\mathbf{\\text{pH} = 7}$.
- **Basic solutions**: $[\\text{H}^+] < 10^{-7}\\text{ mol/L} \\implies \\mathbf{\\text{pH} > 7}$.

#### 2. Strong vs Weak Acids and Bases
- **Strong Acids**: Acids that ionise completely in aqueous solution (e.g. $\\text{HCl}$, $\\text{H}_2\\text{SO}_4$, $\\text{HNO}_3$).
- **Weak Acids**: Acids that ionise only partially in solution (e.g. $\\text{CH}_3\\text{COOH}$ acetic acid, $\\text{H}_2\\text{CO}_3$ carbonic acid).
- **Strong Bases**: Bases that dissociate completely into $\\text{OH}^-$ ions (e.g. $\\text{NaOH}$, $\\text{KOH}$).
- **Weak Bases**: Bases that dissociate partially (e.g. $\\text{NH}_4\\text{OH}$, $\\text{Mg(OH)}_2$).

#### 3. Importance of pH in Everyday Life
1. **Living Organisms**: Our body works within a narrow pH range of **7.0 to 7.8**. When the pH of rain water is less than **5.6**, it is termed **acid rain**, which lowers river water pH and endangers aquatic life.
2. **Soil pH**: Most crops grow best in neutral to mildly alkaline soil (pH 6.5–7.5). If soil is too acidic, farmers treat it with **quicklime** ($\\text{CaO}$), **slaked lime** ($\\text{Ca(OH)}_2$), or **chalk** ($\\text{CaCO}_3$).
3. **Digestive System**: The stomach produces hydrochloric acid ($\\text{pH} \\approx 1.2-3.0$) to digest food without harming the stomach wall. Excess acid causes burning and pain, neutralized by **antacids** such as **Milk of Magnesia** ($\\text{Mg(OH)}_2$) or baking soda ($\\text{NaHCO}_3$).
4. **Tooth Decay**: Tooth enamel is made of crystalline **calcium hydroxyapatite** ($\\text{Ca}_5(\\text{PO}_4)_3\\text{OH}$), the hardest substance in the body. When oral pH falls below **5.5**, bacteria fermenting sugars produce organic acids that corrode the enamel. Using basic toothpaste neutralizes this acidity.
5. **Self Defense in Nature**:
   - *Bee sting / Ant bite*: Injects **methanoic acid** (formic acid), causing sharp pain; neutralized with moist baking soda.
   - *Nettle leaf hairs*: Contain stinging hair injecting methanoic acid; traditionally soothed by rubbing leaves of the **dock plant** (which contains mild alkaline sap).`,
    worked_examples: [
      {
        problem: 'Textbook In-Text Problem: You have two solutions, A and B. The pH of solution A is 6 and pH of solution B is 8. Which solution has more hydrogen ion concentration? Which of these is acidic and which is basic?',
        given: 'Solution A has pH = 6. Solution B has pH = 8.',
        formula: 'pH = -log₁₀[H⁺]. Lower pH indicates higher [H⁺] concentration. pH < 7 is acidic; pH > 7 is basic.',
        substitution: '[H⁺]_A = 10⁻⁶ mol/L; [H⁺]_B = 10⁻⁸ mol/L.',
        calculation: 'Step 1: The relationship between pH and hydrogen ion concentration is inverse: [H⁺] = 10^(-pH).\nStep 2: For Solution A, [H⁺] = 10⁻⁶ M. For Solution B, [H⁺] = 10⁻⁸ M.\nStep 3: Comparing the values: 10⁻⁶ / 10⁻⁸ = 10² = 100 times.\nStep 4: Solution A has 100 times greater hydrogen ion concentration than Solution B.\nStep 5: Solution A (pH 6 < 7) is acidic; Solution B (pH 8 > 7) is basic.',
        finalAnswer: 'Solution A has more hydrogen ion concentration (100× higher). Solution A is acidic and Solution B is basic.',
        unit: 'comparative analysis',
        has_diagram: false
      }
    ],
    common_misconceptions: [
      'Assuming that a solution of pH 3 has only three times more hydrogen ions than pH 1 (it is logarithmic, so pH 1 has 100 times more H⁺ than pH 3).',
      'Thinking that basic solutions contain zero H⁺ ions (they still contain H⁺, but [OH⁻] >> [H⁺]).'
    ],
    visual_lesson_plan: {
      syllabus_term: 'Mid-Term Examination',
      syllabus_pacing: 'Mid-Term Examination Syllabus',
      concept_visuals: [
        {
          concept_title: 'Universal Indicator pH Color Scale',
          diagram_title: 'The Full 0 to 14 pH Color Gradient and Common Substance Benchmarks',
          image_search_query: 'universal indicator ph color scale chart 0 to 14 with common substances ncert diagram',
          video_search_query: 'ph scale universal indicator testing household substances experiment',
          diagram_type: 'image_search',
          what_to_explain: 'Display the complete red-yellow-green-blue-violet universal indicator rainbow from 0 (gastric acid) to 7 (pure water) to 14 (sodium hydroxide).'
        },
        {
          concept_title: 'Tooth Enamel Acid Erosion',
          diagram_title: 'Bacterial Fermentation and Demineralisation of Calcium Hydroxyapatite below pH 5.5',
          image_search_query: 'tooth decay ph 5.5 enamel demineralisation diagram',
          video_search_query: 'how tooth decay occurs ph scale explanation science',
          diagram_type: 'image_search',
          what_to_explain: 'Illustrate dental plaque bacteria converting carbohydrates into lactic acid, dropping oral pH below 5.5 and dissolving hydroxyapatite crystals.'
        }
      ],
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'pH Scale and Physiological Applications',
          questions: [
            {
              question: 'Five solutions A, B, C, D and E when tested with universal indicator showed pH as 4, 1, 11, 7 and 9, respectively. Which solution is (a) neutral, (b) strongly alkaline, (c) strongly acidic, (d) weakly acidic, (e) weakly alkaline? Arrange the pH in increasing order of hydrogen ion concentration.',
              type: 'short_answer',
              ideal_answer: '(a) Neutral: D (pH 7), (b) Strongly alkaline: C (pH 11), (c) Strongly acidic: B (pH 1), (d) Weakly acidic: A (pH 4), (e) Weakly alkaline: E (pH 9). Increasing order of [H⁺]: pH 11 < pH 9 < pH 7 < pH 4 < pH 1 (i.e. C < E < D < A < B).',
              socratic_hint: 'Remember that lowest pH corresponds to highest hydrogen ion concentration.'
            },
            {
              question: 'Under what soil condition do you think a farmer would treat the soil of his fields with quicklime (calcium oxide) or slaked lime (calcium hydroxide) or chalk (calcium carbonate)?',
              type: 'short_answer',
              ideal_answer: 'A farmer treats field soil with quicklime, slaked lime, or chalk when the soil becomes excessively acidic (pH < 6.0). These compounds are basic in nature and neutralize soil acidity to bring it to the optimal range (6.5–7.5) required for healthy plant growth.',
              socratic_hint: 'Consider whether calcium oxide and hydroxide are acidic or basic.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 4,
    title: 'The Chemistry of Industrial & Domestic Salts: Chlor-Alkali Process, Bleaching Powder, Baking Soda, Washing Soda, Water of Crystallisation & Plaster of Paris',
    description: 'Master the chemistry, industrial manufacturing, chemical equations, and practical applications of compounds derived from common salt (NaCl): the Chlor-Alkali process (NaOH, Cl₂, H₂), Bleaching Powder (CaOCl₂), Baking Soda (NaHCO₃), Washing Soda (Na₂CO₃·10H₂O), water of crystallisation in copper sulfate, and Plaster of Paris (CaSO₄·½H₂O).',
    subtopics: [
      'Classification and family of salts: Neutral, acidic, and basic salts based on parent acid-base strength',
      'Common Salt (NaCl) as a primary chemical feedstock in industry',
      'The Chlor-Alkali Process: Electrolysis of aqueous sodium chloride (brine) and electrode products',
      'Anode product (Chlorine Cl₂) and cathode product (Hydrogen H₂) and cathode solution (Sodium hydroxide NaOH)',
      'Bleaching Powder (CaOCl₂): Preparation from dry slaked lime and chlorine, properties and industrial uses',
      'Baking Soda (NaHCO₃): Solvay process synthesis, action of heat, and role of tartaric acid in baking powder',
      'Washing Soda (Na₂CO₃·10H₂O): Recrystallisation of anhydrous sodium carbonate and permanent water softening',
      'Water of crystallisation: Hydrated crystalline salts vs anhydrous forms (CuSO₄·5H₂O blue vitriol dehydration)',
      'Plaster of Paris (CaSO₄·½H₂O): Controlled thermal dehydration of Gypsum (CaSO₄·2H₂O) at 373 K (100°C)',
      'The setting mechanism of Plaster of Paris: Rehydration back to hard interlocking crystalline gypsum'
    ],
    key_concepts: [
      'Salt pH Invariants: Strong acid + Strong base → Neutral salt (pH = 7); Strong acid + Weak base → Acidic salt (pH < 7); Weak acid + Strong base → Basic salt (pH > 7).',
      'Chlor-Alkali Electrolysis: When electricity is passed through brine, it decomposes into chlorine at the positive anode, hydrogen at the negative cathode, and sodium hydroxide in solution: 2NaCl(aq) + 2H₂O(l) → 2NaOH(aq) + Cl₂(g) + H₂(g).',
      'Bleaching Powder Mechanics: Formed by the action of chlorine gas on dry slaked lime: Ca(OH)₂ + Cl₂ → CaOCl₂ + H₂O. Acts as a powerful oxidising agent and disinfectant.',
      'Baking Powder vs Baking Soda: Baking soda is pure NaHCO₃; on heating alone, it releases CO₂ but leaves bitter alkaline Na₂CO₃. Baking powder blends NaHCO₃ with a mild edible acid (tartaric acid), which neutralizes Na₂CO₃ to form a pleasant-tasting sodium salt.',
      'Water of Crystallisation & POP: Water of crystallisation is the fixed number of water molecules chemically bonded in one formula unit of a salt. Gypsum CaSO₄·2H₂O heated carefully at 373 K yields Plaster of Paris CaSO₄·½H₂O; above 373 K, all water is lost, forming dead burnt plaster.'
    ],
    success_criteria: 'Student can write manufacturing reactions for all 5 commercial salts, explain the difference between baking soda and baking powder, and calculate water of crystallisation.',
    chapter_notes: `### 2.4 More About Salts & Chemicals from Common Salt

#### 1. pH of Salts
- **Neutral Salt**: Strong Acid + Strong Base $\\to \\text{pH} = 7$ (e.g. $\\text{NaCl}, \\text{K}_2\\text{SO}_4, \\text{NaNO}_3$).
- **Acidic Salt**: Strong Acid + Weak Base $\\to \\text{pH} < 7$ (e.g. $\\text{NH}_4\\text{Cl}, \\text{CuSO}_4$).
- **Basic Salt**: Weak Acid + Strong Base $\\to \\text{pH} > 7$ (e.g. $\\text{CH}_3\\text{COONa}, \\text{Na}_2\\text{CO}_3, \\text{NaHCO}_3$).

#### 2. The Chlor-Alkali Process
When electricity is passed through an aqueous solution of sodium chloride (**brine**):
$$2\\text{NaCl}(aq) + 2\\text{H}_2\\text{O}(l) \\to 2\\text{NaOH}(aq) + \\text{Cl}_2(g) + \\text{H}_2(g)$$
- **At the Anode (+)**: Chlorine gas ($\\text{Cl}_2$) is evolved (used for water treatment, PVC, disinfectants, CFCs).
- **At the Cathode (-)**: Hydrogen gas ($\\text{H}_2$) is evolved (used as fuel, margarine, ammonia for fertilizers).
- **Near the Cathode**: Sodium hydroxide ($\\text{NaOH}$) solution forms (used for de-greasing metals, soaps, paper making).

#### 3. Bleaching Powder ($\\text{CaOCl}_2$)
Produced by the action of chlorine on dry slaked lime:
$$\\text{Ca(OH)}_2(s) + \\text{Cl}_2(g) \\to \\text{CaOCl}_2(s) + \\text{H}_2\\text{O}(l)$$
- *Uses*: Bleaching cotton and linen in textile industry; wood pulp in paper factories; chemical oxidising agent; disinfectant for water.

#### 4. Baking Soda ($\\text{NaHCO}_3$, Sodium Hydrogen Carbonate)
Manufactured via the Solvay process:
$$\\text{NaCl} + \\text{H}_2\\text{O} + \\text{CO}_2 + \\text{NH}_3 \\to \\text{NH}_4\\text{Cl} \\text{ (Ammonium chloride)} + \\text{NaHCO}_3 \\text{ (Sodium hydrogen carbonate)}$$
- It is a mild, non-corrosive basic salt. On heating during cooking:
$$2\\text{NaHCO}_3 \\xrightarrow{\\Delta} \\text{Na}_2\\text{CO}_3 + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow$$
- **Baking Powder**: A mixture of baking soda ($\\text{NaHCO}_3$) and a mild edible acid like **tartaric acid**. When heated in water:
$$\\text{NaHCO}_3 + \\text{H}^+ \\to \\text{CO}_2\\uparrow + \\text{H}_2\\text{O} + \\text{Sodium salt of acid}$$
The evolved $\\text{CO}_2$ gas causes bread and cakes to rise, making them light and spongy.

#### 5. Washing Soda ($\\text{Na}_2\\text{CO}_3\\cdot 10\\text{H}_2\\text{O}$)
Obtained by recrystallisation of sodium carbonate from water:
$$\\text{Na}_2\\text{CO}_3 + 10\\text{H}_2\\text{O} \\to \\text{Na}_2\\text{CO}_3\\cdot 10\\text{H}_2\\text{O}$$
- *Uses*: Glass, soap, and paper industries; manufacturing borax; domestic cleaning agent; **permanent water softening**.

#### 6. Water of Crystallisation & Plaster of Paris
- **Water of crystallisation** is the fixed number of water molecules present in one formula unit of a salt (e.g. $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$, $\\text{FeSO}_4\\cdot 7\\text{H}_2\\text{O}$, $\\text{Na}_2\\text{CO}_3\\cdot 10\\text{H}_2\\text{O}$).
- When blue copper sulfate crystals are heated, water is lost and they turn into white anhydrous $\\text{CuSO}_4$.
- **Plaster of Paris** ($\\text{CaSO}_4\\cdot \\frac{1}{2}\\text{H}_2\\text{O}$, Calcium sulfate hemihydrate):
Prepared by heating Gypsum ($\\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O}$) at **373 K (100°C)**:
$$\\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O} \\xrightarrow{373\\text{ K}} \\text{CaSO}_4\\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O}$$
- *Setting Property*: On mixing with water, it rehydrates to form hard gypsum:
$$\\text{CaSO}_4\\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O} \\to \\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O} \\text{ (Hard solid mass)}$$
- *Uses*: Supporting fractured bones in correct position; making casts for toys, statues, and decorative ornaments; fireproofing.`,
    worked_examples: [
      {
        problem: 'Textbook Example: Plaster of Paris should be stored in a moisture-proof container. Explain why. Write an equation to show the reaction between Plaster of Paris and water.',
        given: 'Plaster of Paris (CaSO₄·½H₂O) stored in unsealed vs moisture-proof container.',
        formula: 'CaSO₄·½H₂O + 1½H₂O → CaSO₄·2H₂O (Gypsum, hard solid).',
        substitution: 'Reaction with atmospheric moisture.',
        calculation: 'Step 1: Plaster of Paris is calcium sulfate hemihydrate (CaSO₄·½H₂O).\nStep 2: When it comes in contact with ambient moisture or water vapor, it readily absorbs water.\nStep 3: This rehydration triggers an exothermic crystallization into gypsum (CaSO₄·2H₂O), which sets into an unworkable, rock-hard solid mass.\nStep 4: Once set, it loses its molding and plastering properties permanently.\nStep 5: Therefore, it must be stored in completely airtight, moisture-proof containers.',
        finalAnswer: 'Plaster of Paris reacts with ambient moisture to set into hard gypsum: CaSO₄·½H₂O + 1½H₂O → CaSO₄·2H₂O. Storing in moisture-proof containers prevents premature hardening.',
        unit: 'chemical explanation',
        has_diagram: false
      }
    ],
    common_misconceptions: [
      'Assuming baking soda and baking powder are identical (baking soda is pure NaHCO₃ which produces bitter Na₂CO₃; baking powder has added tartaric acid to prevent bitterness).',
      'Thinking that half a water molecule can exist in CaSO₄·½H₂O (two formula units of CaSO₄ share one water molecule: 2CaSO₄·H₂O).'
    ],
    visual_lesson_plan: {
      syllabus_term: 'Mid-Term Examination',
      syllabus_pacing: 'Mid-Term Examination Syllabus',
      concept_visuals: [
        {
          concept_title: 'Chlor-Alkali Electrolysis Cell',
          diagram_title: 'Electrolysis of Brine Showing Anode (Cl₂), Cathode (H₂), and NaOH Membrane',
          image_search_query: 'chlor alkali process cell membrane electrolysis brine diagram ncert',
          video_search_query: 'chlor alkali process membrane cell animation chemistry',
          diagram_type: 'image_search',
          what_to_explain: 'Demonstrate the movement of chloride ions to the anode releasing Cl2, water reduction at the cathode releasing H2, and formation of NaOH solution.'
        },
        {
          concept_title: 'Water of Crystallisation Dehydration',
          diagram_title: 'Heating Copper Sulfate Crystals (Blue to White) and Rehydration',
          image_search_query: 'heating copper sulphate crystals test tube water of crystallisation experiment diagram',
          video_search_query: 'heating copper sulphate crystals water of crystallisation demonstration',
          diagram_type: 'image_search',
          what_to_explain: 'Illustrate blue vitriol losing 5 water molecules to become white anhydrous copper sulfate, with water droplets condensing at the test tube rim.'
        }
      ],
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Commercial Salts Synthesis',
          questions: [
            {
              question: 'What is the chemical name and formula of bleaching powder? How is it prepared? Write chemical equation for the reaction.',
              type: 'short_answer',
              ideal_answer: 'Chemical name: Calcium oxychloride. Formula: CaOCl₂. Preparation: It is produced by the action of chlorine gas on dry slaked lime [Ca(OH)₂]: Ca(OH)₂ + Cl₂ → CaOCl₂ + H₂O.',
              socratic_hint: 'Identify the product when slaked lime absorbs chlorine gas.'
            },
            {
              question: 'Give two important uses of washing soda and two of baking soda.',
              type: 'short_answer',
              ideal_answer: 'Washing soda (Na₂CO₃·10H₂O) uses: (1) Removing permanent hardness of water, (2) Manufacturing glass, soap, and paper. Baking soda (NaHCO₃) uses: (1) Ingredient in baking powder to make bread/cakes rise, (2) Active ingredient in antacids to relieve acidity.',
              socratic_hint: 'Recall household baking and laundry applications.'
            }
          ]
        }
      ]
    }
  },
  {
    order_index: 5,
    title: 'Comprehensive NCERT In-Text & Chapter-End Master Numerical & Conceptual Exercise Solver',
    description: 'Resolve every in-text problem and chapter-end exercise question from NCERT Class 10 Chapter 2 with complete, board-exam topper step-by-step layout: balanced equations, given data, formula, chemical logic, and boxed answers.',
    subtopics: [
      'In-text question series 1: Curd storage, metal-acid gas identification, and pop-test detection',
      'In-text question series 2: Aqueous ionisation, conductivity of acids vs glucose, and dry litmus test',
      'In-text question series 3: Hydronium concentration during dilution and comparative pH 6 vs pH 8 analysis',
      'In-text question series 4: Universal indicator identification (pH 4, 1, 11, 7, 9) and soil acidity treatment',
      'In-text question series 5: Bleaching powder synthesis, water softening, and Plaster of Paris rehydration',
      'Chapter-end Exercise Q1-Q5: Multiple choice questions (litmus reaction, egg shell reaction, neutralisation ratios)',
      'Chapter-end Exercise Q6-Q10: Writing word and balanced equations for metal-acid and carbonate-acid reactions',
      'Chapter-end Exercise Q11-Q15: Distilled water vs rain water conductivity, absence of water in acid crystals, and baking/washing soda uses'
    ],
    key_concepts: [
      'Master Board Exam Method: Lay out chemical answers with Given -> Governing Equation -> Chemical Explanation -> Observations -> Final Concluding Answer.',
      'Water Softening Invariant: Washing soda Na₂CO₃ removes permanent hardness (caused by soluble calcium and magnesium chlorides/sulfates) by precipitating insoluble carbonates: Ca²⁺(aq) + CO₃²⁻(aq) → CaCO₃↓.',
      'Electrolytic Disparity: Pure distilled water does not conduct electricity because it contains negligibly small ion concentrations (10⁻⁷ M); rainwater contains dissolved atmospheric gases (CO₂, SO₂, NO₂) that form carbonic, sulfurous, and nitric acids, releasing mobile ions that conduct current.',
      'Dilution Ion Density: Adding water increases total volume, which lowers the number of H₃O⁺ ions per cubic centimeter (decreases concentration), causing the pH to increase toward 7.',
      'Limestone Geochemistry: Limestone, chalk, marble, and egg-shells are all calcium carbonate (CaCO₃); they all effervesce vigorously with dilute acids releasing carbon dioxide.'
    ],
    success_criteria: 'Student can solve any NCERT Class 10 Chapter 2 exercise problem with full marks in CBSE/ICSE board examinations.',
    chapter_notes: `### 2.5 NCERT Comprehensive Exercise Solver

#### Solutions to Crucial Chapter-End Questions:

1. **Why does distilled water not conduct electricity, whereas rain water does?**
   - Distilled water is pure water with no dissolved mineral salts or acids; its degree of ionisation is extremely low ($[\\text{H}^+] = [\\text{OH}^-] = 10^{-7}\\text{ M}$), so it lacks sufficient mobile charge carriers to conduct an electric current.
   - Rain water dissolves atmospheric gases such as carbon dioxide ($\\text{CO}_2$), sulfur dioxide ($\\text{SO}_2$), and nitrogen oxides ($\\text{NO}_x$) to form acids:
$$\\text{CO}_2 + \\text{H}_2\\text{O} \\to \\text{H}_2\\text{CO}_3 \\text{ (Carbonic acid)}$$
$$\\text{H}_2\\text{CO}_3 \\rightleftharpoons 2\\text{H}^+(aq) + \\text{CO}_3^{2-}(aq)$$
   - These mobile ions readily conduct an electric current.

2. **Why do acids not show acidic behaviour in the absence of water?**
   - The acidic behaviour of an acid is exclusively due to the presence of hydrogen/hydronium ions ($\\text{H}_3\\text{O}^+$).
   - An acid molecule cannot dissociate into ions without a polar solvent like water to hydrate the hydrogen ion:
$$\\text{HCl} + \\text{H}_2\\text{O} \\to \\text{H}_3\\text{O}^+ + \\text{Cl}^-$$
   - In the absence of water, covalent acid molecules remain un-ionised, exhibiting zero acidic properties.

3. **A solution turns red litmus blue; its pH is likely to be:**
   - (A) 1, (B) 4, (C) 5, (D) 10.
   - **Answer**: (D) 10. A solution that turns red litmus blue must be basic ($\\text{pH} > 7$).

4. **A solution reacts with crushed egg-shells to give a gas that turns lime-water milky. The solution contains:**
   - (A) $\\text{NaCl}$, (B) $\\text{HCl}$, (C) $\\text{LiCl}$, (D) $\\text{KCl}$.
   - **Answer**: (B) $\\text{HCl}$. Egg-shells consist of calcium carbonate ($\\text{CaCO}_3$). $\\text{CaCO}_3 + 2\\text{HCl} \\to \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow$. $\\text{CO}_2$ turns lime water milky.

5. **$10\\text{ mL}$ of a solution of $\\text{NaOH}$ is found to be completely neutralised by $8\\text{ mL}$ of a given solution of $\\text{HCl}$. If we take $20\\text{ mL}$ of the same solution of $\\text{NaOH}$, the amount $\\text{HCl}$ solution required to neutralise it will be:**
   - (A) $4\\text{ mL}$, (B) $8\\text{ mL}$, (C) $12\\text{ mL}$, (D) $16\\text{ mL}$.
   - **Answer**: (D) $16\\text{ mL}$. Neutralisation stoichiometry is directly proportional: doubling $\\text{NaOH}$ from $10\\text{ mL}$ to $20\\text{ mL}$ requires doubling $\\text{HCl}$ from $8\\text{ mL}$ to $16\\text{ mL}$.`,
    worked_examples: [
      {
        problem: 'NCERT Chapter-End Exercise 7: Write balanced chemical equations for: (a) Dilute sulphuric acid reacts with zinc granules. (b) Dilute hydrochloric acid reacts with magnesium ribbon. (c) Dilute sulphuric acid reacts with aluminium powder. (d) Dilute hydrochloric acid reacts with iron filings.',
        given: 'Four reactions between metals situated above hydrogen and dilute acids.',
        formula: 'Active Metal + Acid -> Metal Salt + Hydrogen gas (H₂↑).',
        substitution: 'Zn, Mg, Al, Fe reacting with HCl and H₂SO₄.',
        calculation: '(a) Zn(s) + H₂SO₄(aq) → ZnSO₄(aq) + H₂(g)↑\n(b) Mg(s) + 2HCl(aq) → MgCl₂(aq) + H₂(g)↑\n(c) 2Al(s) + 3H₂SO₄(aq) → Al₂(SO₄)₃(aq) + 3H₂(g)↑\n(d) Fe(s) + 2HCl(aq) → FeCl₂(aq) + H₂(g)↑ [Note: Iron forms Ferrous chloride FeCl₂, not FeCl₃, because liberated H₂ prevents oxidation].',
        finalAnswer: '(a) Zn + H₂SO₄ → ZnSO₄ + H₂↑\n(b) Mg + 2HCl → MgCl₂ + H₂↑\n(c) 2Al + 3H₂SO₄ → Al₂(SO₄)₃ + 3H₂↑\n(d) Fe + 2HCl → FeCl₂ + H₂↑',
        unit: 'chemical equations',
        has_diagram: false
      },
      {
        problem: 'NCERT Chapter-End Exercise 15: Give two important uses of washing soda and baking soda.',
        given: 'Commercial compounds: Washing soda (Na₂CO₃·10H₂O) and Baking soda (NaHCO₃).',
        formula: 'Industrial and household applications based on chemical properties.',
        substitution: 'Uses derived from alkaline and carbon dioxide liberating characteristics.',
        calculation: 'Washing Soda (Na₂CO₃·10H₂O):\n1. Permanent water softening: Reacts with soluble Ca²⁺ and Mg²⁺ salts to precipitate insoluble CaCO₃ and MgCO₃.\n2. Manufacturing: Used in glass, soap, and paper industries, as well as in the production of borax.\n\nBaking Soda (NaHCO₃):\n1. Leavening agent: Component of baking powder; releases CO₂ when heated with tartaric acid to make cakes soft and spongy.\n2. Medicinal antacid: Mild non-corrosive base used to neutralize excess hydrochloric acid in the stomach.',
        finalAnswer: 'Washing soda softens hard water and manufactures glass/soap. Baking soda acts as an antacid and leavening agent in baking powder.',
        unit: 'industrial uses',
        has_diagram: false
      }
    ],
    common_misconceptions: [
      'Believing that iron forms ferric chloride (FeCl₃) with dilute HCl (it forms ferrous chloride FeCl₂ because liberated hydrogen gas acts as a reducing agent).',
      'Thinking that rainwater is 100% pure neutral water (it naturally dissolves atmospheric gases, forming weak acids and conducting electricity).'
    ],
    visual_lesson_plan: {
      syllabus_term: 'Mid-Term Examination',
      syllabus_pacing: 'Mid-Term Examination Syllabus',
      concept_visuals: [
        {
          concept_title: 'NCERT Exercise Problem Solving Chalkboard',
          diagram_title: 'Step-by-Step Layout of Board Exam Acid-Base Numerical and Chemical Equations',
          image_search_query: 'acids bases and salts class 10 ncert exercise solutions board equations diagram',
          video_search_query: 'acids bases and salts class 10 ncert exercise questions solutions',
          diagram_type: 'image_search',
          what_to_explain: 'Walk students through the 5-step board exam method for writing balanced chemical equations and solving acid-base neutralization problems.'
        }
      ],
      concept_questions: [
        {
          concept_index: 0,
          concept_title: 'Comprehensive Review',
          questions: [
            {
              question: 'Why does an aqueous solution of an acid conduct electricity?',
              type: 'short_answer',
              ideal_answer: 'In water, an acid dissociates into mobile cations (hydronium ions H₃O⁺) and anions (e.g. Cl⁻, SO₄²⁻). These mobile ions move toward oppositely charged electrodes, carrying the electric current through the solution.',
              socratic_hint: 'What type of particles carry electric current in a liquid electrolyte?'
            },
            {
              question: 'Plaster of Paris should be stored in a moisture-proof container. Explain why.',
              type: 'short_answer',
              ideal_answer: 'Plaster of Paris (CaSO₄·½H₂O) readily absorbs moisture from the atmosphere and undergoes an exothermic reaction to form hard gypsum (CaSO₄·2H₂O): CaSO₄·½H₂O + 1½H₂O → CaSO₄·2H₂O. Once set into hard gypsum, it loses its setting and molding properties permanently.',
              socratic_hint: 'What happens to POP when it absorbs water?'
            }
          ]
        }
      ]
    }
  }
];

async function uploadCh2Modules() {
  console.log('========================================================================');
  console.log('SYNTHESIZING & UPLOADING CLASS 10 SCIENCE CH 2 (ACIDS, BASES & SALTS)');
  console.log('========================================================================\n');

  const currId = 'afa18ea6-511f-47a1-8328-4c66b9543dbc';

  // 1. Delete old incomplete single module
  console.log('Cleaning existing incomplete module for Chapter 2...');
  await supabase
    .from('syllabus_modules')
    .delete()
    .eq('curriculum_id', currId);

  // 2. Insert all 5 complete modules
  console.log('Inserting 5 comprehensive, publication-grade modules...\n');
  for (const m of CH2_MODULES) {
    const { error: insErr } = await supabase
      .from('syllabus_modules')
      .insert({
        curriculum_id: currId,
        order_index: m.order_index,
        title: m.title,
        description: m.description,
        class_level: 'Class 10',
        board: 'CBSE',
        subtopics: m.subtopics,
        key_concepts: m.key_concepts,
        success_criteria: m.success_criteria,
        chapter_notes: m.chapter_notes,
        worked_examples: m.worked_examples,
        common_misconceptions: m.common_misconceptions,
        visual_lesson_plan: m.visual_lesson_plan,
        quiz_questions: m.visual_lesson_plan.concept_questions[0].questions.map(q => ({
          question: q.question,
          type: q.type || 'short_answer',
          options: [],
          correct_answer: q.ideal_answer,
          explanation: q.ideal_answer,
          hint: q.socratic_hint || ''
        })),
        estimated_minutes: 45,
        ai_system_prompt_context: `CBSE Class 10 Science Module ${m.order_index}: ${m.title}. Mid-Term Examination Syllabus. Adhere strictly to Socratic teaching cadence, pure Unicode mathematical typography, and step-by-step chemical equations.`
      });

    if (insErr) {
      console.error(`Error inserting Module ${m.order_index}:`, insErr);
    } else {
      console.log(`  [Mod ${m.order_index}] Inserted successfully: ${m.title.substring(0, 50)}...`);
    }
  }

  console.log('\n========================================================================');
  console.log('SUCCESS: Class 10 Science Chapter 2 now has 5 complete modules!');
  console.log('========================================================================\n');
}

uploadCh2Modules().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
