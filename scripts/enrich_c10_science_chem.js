const { supabase } = require('./db_helper');

async function enrichScienceChem() {
  console.log('=== ENRICHING CLASS 10 SCIENCE: CHEMISTRY (CHAPTERS 1 TO 4) ===\n');

  // Chapter 1: Chemical Reactions and Equations (Mod 6: e53978d2-8aa2-4c33-9103-bb9eaf4b43f9)
  const ch1Questions = [
    {
      problem: "NCERT Exercise Q1 & In-Text Q1: (i) Why should a magnesium ribbon be cleaned before burning in air? (ii) Write a balanced chemical equation with state symbols for the reaction between hydrogen and chlorine, and sodium and water.",
      solution: "Part (i): Magnesium ribbon cleaning:\nReason: Magnesium is a reactive metal. When stored, it reacts with atmospheric oxygen to form a thin, stable protective layer of basic magnesium oxide (MgO) on its surface.\nThis oxide coating prevents further contact of oxygen with underlying magnesium, hindering burning.\nTo ensure smooth, complete ignition and direct contact with oxygen, the ribbon is rubbed with sandpaper before burning.\nReaction: 2Mg(s) + O₂(g) → 2MgO(s) + Heat + Dazzling White Light.\n\nPart (ii): Balanced Chemical Equations with State Symbols:\n1. Hydrogen + Chlorine → Hydrogen chloride:\nH₂(g) + Cl₂(g) → 2HCl(g)\n\n2. Sodium + Water → Sodium hydroxide + Hydrogen gas:\n2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) + Heat\n[ROUGH_WORK]\nNotice: Sodium reaction is highly exothermic. Hydrogen catches fire with yellow-orange flame.\nBoxed Answer: [ (i) Cleaned to remove protective MgO layer; (ii) H₂(g) + Cl₂(g) → 2HCl(g) and 2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) ].",
      concept_questions: [
        "Why is magnesium oxide layer considered protective?",
        "What type of flame is observed when magnesium burns in air?"
      ]
    },
    {
      problem: "NCERT Exercise Q6 & Q7: Balance the following chemical equations:\n(a) HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + H₂O\n(b) NaOH + H₂SO₄ → Na₂SO₄ + H₂O\n(c) NaCl + AgNO₃ → AgCl + NaNO₃\n(d) BaCl₂ + H₂SO₄ → BaSO₄ + HCl",
      solution: "Balancing Principle: Law of Conservation of Mass (total number of atoms of each element on reactant side must equal product side).\n\n(a) HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + H₂O:\nReactants: H=3, N=1, O=5, Ca=1\nProducts: H=2, N=2, O=7, Ca=1\nStep 1: Balance Nitrate (NO₃) by putting 2 in front of HNO₃:\n2HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + H₂O\nStep 2: Balance Hydrogen and Oxygen by putting 2 in front of H₂O:\n2HNO₃(aq) + Ca(OH)₂(aq) → Ca(NO₃)₂(aq) + 2H₂O(l) (Balanced!)\n\n(b) NaOH + H₂SO₄ → Na₂SO₄ + H₂O:\nPut 2 in front of NaOH to balance Na: 2NaOH + H₂SO₄ → Na₂SO₄ + H₂O\nPut 2 in front of H₂O to balance H and O:\n2NaOH(aq) + H₂SO₄(aq) → Na₂SO₄(aq) + 2H₂O(l) (Balanced!)\n\n(c) NaCl + AgNO₃ → AgCl + NaNO₃:\nCheck atom counts: Na=1, Cl=1, Ag=1, N=1, O=3 on both sides.\nNaCl(aq) + AgNO₃(aq) → AgCl(s)↓ + NaNO₃(aq) (Already Balanced! AgCl forms white precipitate).\n\n(d) BaCl₂ + H₂SO₄ → BaSO₄ + HCl:\nPut 2 in front of HCl to balance Cl and H:\nBaCl₂(aq) + H₂SO₄(aq) → BaSO₄(s)↓ + 2HCl(aq) (Balanced! BaSO₄ forms white precipitate).\n[ROUGH_WORK]\nBoth (c) and (d) are classic Double Displacement & Precipitation reactions!\nBoxed Answer: [ (a) 2HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + 2H₂O; (b) 2NaOH + H₂SO₄ → Na₂SO₄ + 2H₂O; (d) BaCl₂ + H₂SO₄ → BaSO₄ + 2HCl ].",
      concept_questions: [
        "What physical law necessitates the balancing of chemical equations?",
        "What type of chemical reaction is occurring in (d)?"
      ]
    },
    {
      problem: "NCERT Exercise Q8 & Q10: (i) Why is respiration considered an exothermic reaction? Explain with equation. (ii) What is the difference between displacement and double displacement reactions? Give one equation for each.",
      solution: "Part (i): Respiration as an Exothermic Reaction:\nExplanation: In our body, food is broken down during digestion to form glucose (C₆H₁₂O₆).\nDuring respiration, glucose combines with oxygen in the cells of our body and undergoes slow combustion to release energy in the form of ATP, along with carbon dioxide and water.\nSince energy is released during this process, respiration is classified as an exothermic reaction.\nEquation:\nC₆H₁₂O₆(aq) + 6O₂(aq) → 6CO₂(aq) + 6H₂O(l) + Energy (38 ATP)\n\nPart (ii): Displacement vs Double Displacement Reaction:\n1. Displacement Reaction:\nA reaction in which a more reactive element displaces a less reactive element from its aqueous salt solution.\nExample: Iron nail in copper sulphate solution:\nFe(s) + CuSO₄(aq) [Blue] → FeSO₄(aq) [Light Green] + Cu(s) [Brown deposit]\nHere, Fe is more reactive than Cu, so it displaces Cu.\n\n2. Double Displacement Reaction:\nA reaction in which two compounds react by an exchange of ions to form two new compounds, often producing an insoluble precipitate.\nExample: Sodium sulphate and Barium chloride:\nNa₂SO₄(aq) + BaCl₂(aq) → BaSO₄(s)↓ [White precipitate] + 2NaCl(aq)\nHere, Ba²⁺ and Na⁺ ions exchange partners with SO₄²⁻ and Cl⁻ ions.\n[ROUGH_WORK]\nSingle partner switch = Displacement. Mutual exchange of ions = Double displacement.\nBoxed Answer: [ Respiration releases energy (exothermic): C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy. Displacement involves one element displacing another; double displacement involves mutual exchange of ions ].",
      concept_questions: [
        "Why does the blue color of copper sulphate solution fade when an iron nail is immersed in it?",
        "What is a precipitation reaction?"
      ]
    },
    {
      problem: "NCERT Exercise Q13, Q14 & Q17: (i) What happens when copper powder is heated in a china dish? Write the reaction and identify what is oxidised and reduced. (ii) Why do we apply paint on iron articles? (iii) Oil and fat containing food items are flushed with nitrogen. Why?",
      solution: "Part (i): Heating Copper Powder:\nObservation: The brown surface of copper powder becomes coated with a black substance.\nExplanation: Copper reacts with oxygen in air to form black copper(II) oxide (CuO).\nReaction 1: 2Cu(s) [Brown] + O₂(g) → 2CuO(s) [Black]\nIf hydrogen gas is passed over this heated black CuO, the black coating turns brown again as the reverse reaction occurs:\nReaction 2: CuO(s) + H₂(g) → Cu(s) + H₂O(l)\nIn Reaction 2:\nCuO loses oxygen → Reduced to Cu (CuO is oxidising agent).\nH₂ gains oxygen → Oxidised to H₂O (H₂ is reducing agent).\nThis is a classic Redox Reaction.\n\nPart (ii): Painting Iron Articles:\nReason: Rusting of iron (Fe₂O₃·xH₂O) requires the simultaneous presence of both moist air (water vapor) and oxygen.\nPaint forms a physical protective barrier between the iron metal surface and atmospheric moisture/oxygen, preventing corrosion.\n\nPart (iii): Flushing Oily Food with Nitrogen:\nReason: Oils and fats present in food items react with atmospheric oxygen when exposed to air (aerial oxidation), forming volatile bad-smelling aldehydes and carboxylic acids—a process called Rancidity.\nRancidity alters the taste, smell, and nutritional value of food.\nNitrogen is an unreactive (inert) gas. Flushing snack packets with nitrogen displaces oxygen, preventing oxidation and keeping the food fresh.\n[ROUGH_WORK]\nOxidation of fat = Rancidity. Oxidation of metal = Corrosion.\nBoxed Answer: [ (i) 2Cu + O₂ → 2CuO (black); CuO + H₂ → Cu + H₂O (Redox); (ii) Paint acts as barrier against O₂ and H₂O; (iii) Nitrogen is inert and prevents aerial oxidation (rancidity) ].",
      concept_questions: [
        "In the reaction CuO + H₂ → Cu + H₂O, which substance acts as the reducing agent?",
        "Name two antioxidants commonly added to oily foods."
      ]
    }
  ];

  // Chapter 2: Acids, Bases and Salts (Mod 5: 292b89a2-63f2-473a-935e-abf431a17c94)
  const ch2Questions = [
    {
      problem: "NCERT Exercise Q1 & In-Text Q1-Q3: (i) Why should curd and sour substances not be kept in brass and copper vessels? (ii) Which gas is usually liberated when an acid reacts with a metal? Illustrate with an example and describe the test for this gas. (iii) Why do HCl, HNO₃ show acidic character in aqueous solutions while glucose and alcohol do not?",
      solution: "Part (i): Curd in Brass and Copper:\nReason: Curd and sour foodstuffs contain organic acids (e.g. lactic acid in curd).\nAcids react with brass and copper metals to form toxic metallic salts and hydrogen gas:\nAcid + Metal → Toxic Metallic Salt + H₂\nThese poisonous compounds make the food unfit for human consumption (food poisoning). Hence, brass and copper vessels are tinned or avoided.\n\nPart (ii): Metal + Acid Reaction & Gas Test:\nGas liberated: Hydrogen gas (H₂).\nExample: Granulated zinc reacting with dilute sulphuric acid:\nZn(s) + H₂SO₄(aq) → ZnSO₄(aq) + H₂(g)↑\nTest for Hydrogen Gas:\nPass the gas through a soap solution; bubbles filled with gas rise into the air.\nBring a burning splinter or candle near the gas bubble.\nThe bubble bursts and the gas burns with a characteristic 'POP' sound.\n\nPart (iii): HCl vs Glucose Conduction:\nAcidic behavior requires the generation of free hydrogen ions (H⁺) or hydronium ions (H₃O⁺) in aqueous solution:\nHCl(aq) + H₂O(l) → H₃O⁺(aq) + Cl⁻(aq) (Complete ionization → releases H⁺ → conducts electricity, turns blue litmus red).\nIn contrast, compounds like glucose (C₆H₁₂O₆) and alcohol (C₂H₅OH) have covalent bonds. In aqueous solution, they do not ionize to furnish free H⁺ ions.\nBecause they lack mobile ions, they do not conduct electricity or show acidic properties.\n[ROUGH_WORK]\nNo H⁺ ions = No acidic character! Electricity conduction in liquids requires mobile ions.\nBoxed Answer: [ (i) Acids react with copper/brass forming toxic salts; (ii) H₂ gas liberated, confirmed by pop sound; (iii) HCl ionizes to form H₃O⁺ ions in water, while glucose and alcohol do not ionize ].",
      concept_questions: [
        "Why can hydrogen ions not exist independently in water without forming H₃O⁺?",
        "Does distilled water conduct electricity? Why or why not?"
      ]
    },
    {
      problem: "NCERT Exercise Q4 & Q5: (i) While diluting an acid, why is it recommended that the acid should be added to water and not water to the acid? (ii) How is the concentration of hydronium ions (H₃O⁺) affected when a solution of an acid is diluted?",
      solution: "Part (i): Acid Dilution Rule (Acid to Water, NEVER Water to Acid):\nExplanation: The process of dissolving a concentrated mineral acid (like conc. H₂SO₄ or conc. HNO₃) in water is highly exothermic (generates a large amount of heat energy).\nIf water is added to concentrated acid:\nThe small amount of water added immediately boils due to the concentrated heat at the surface.\nThe localized boiling causes violent splashing of the corrosive acid, which can cause severe acid burns on the skin, face, and clothes.\nThe excessive local heating may also cause the glass container to crack or shatter.\nCorrect Method: Always add concentrated acid slowly to a large volume of water with continuous stirring. The large heat capacity of water absorbs the heat safely.\n\nPart (ii): Effect on Hydronium Ion Concentration:\nDilution means adding more water to a fixed amount of acid.\nAlthough the total number of H₃O⁺ ions in solution remains constant, the volume of the solution increases.\nTherefore, the concentration of hydronium ions per unit volume [H₃O⁺]/V decreases.\nThis results in a decrease in acidity and an increase in pH (moving closer to 7).\n[ROUGH_WORK]\nConcentration = moles / volume. Increasing volume decreases [H₃O⁺] and increases pH.\nBoxed Answer: [ (i) Always add acid to water slowly with stirring to prevent violent exothermic splashing; (ii) [H₃O⁺] per unit volume decreases upon dilution ].",
      concept_questions: [
        "What happens to the pH of an acidic solution when it is diluted?",
        "Can the pH of an acidic solution ever exceed 7 upon infinite dilution with pure water?"
      ]
    },
    {
      problem: "NCERT Exercise Q7, Q8 & Q10: (i) Five solutions A, B, C, D and E when tested with universal indicator showed pH as 4, 1, 11, 7 and 9 respectively. Which solution is: (a) neutral (b) strongly alkaline (c) strongly acidic (d) weakly acidic (e) weakly alkaline? Arrange in increasing order of H⁺ concentration. (ii) Write the chemical formulas and one use each of: Bleaching Powder, Baking Soda, Washing Soda, and Plaster of Paris.",
      solution: "Part (i): pH Classification & Ordering:\npH Scale (0–14): pH < 7 is acidic, pH = 7 is neutral, pH > 7 is basic.\n(a) Neutral: Solution D (pH = 7)\n(b) Strongly alkaline: Solution C (pH = 11)\n(c) Strongly acidic: Solution B (pH = 1)\n(d) Weakly acidic: Solution A (pH = 4)\n(e) Weakly alkaline: Solution E (pH = 9)\n\nIncreasing order of H⁺ ion concentration:\nRemember: Lower pH means higher [H⁺] concentration!\nOrder: C (pH 11) < E (pH 9) < D (pH 7) < A (pH 4) < B (pH 1).\n\nPart (ii): Important Chemical Salts:\n1. Bleaching Powder: Calcium oxychloride, CaOCl₂.\nPreparation: Dry slaked lime + Chlorine gas:\nCa(OH)₂ + Cl₂ → CaOCl₂ + H₂O\nUse: Disinfecting drinking water, bleaching cotton and linen in textile industry.\n\n2. Baking Soda: Sodium hydrogen carbonate, NaHCO₃.\nPreparation: Solvay process (NaCl + H₂O + CO₂ + NH₃ → NH₄Cl + NaHCO₃)\nUse: Ingredient in baking powder (releases CO₂ to make cakes fluffy), antacid to neutralize stomach acidity.\n\n3. Washing Soda: Sodium carbonate decahydrate, Na₂CO₃·10H₂O.\nPreparation: Recrystallization of anhydrous sodium carbonate (soda ash):\nNa₂CO₃ + 10H₂O → Na₂CO₃·10H₂O\nUse: Removing permanent hardness of water, manufacture of glass and soap.\n\n4. Plaster of Paris (POP): Calcium sulphate hemihydrate, CaSO₄·½H₂O.\nPreparation: Heating gypsum (CaSO₄·2H₂O) carefully at 373 K (100°C):\nCaSO₄·2H₂O → CaSO₄·½H₂O + 1½H₂O\nUse: Setting fractured bones in correct position, making decorative statues and false ceilings.\n[ROUGH_WORK]\nIf gypsum is heated above 373 K, all water is lost, forming dead burnt plaster (CaSO₄)!\nBoxed Answer: [ (i) Neutral: D, Strong acid: B, Strong base: C, Weak acid: A, Weak base: E. [H⁺] order: C < E < D < A < B. (ii) Formulas: CaOCl₂, NaHCO₃, Na₂CO₃·10H₂O, CaSO₄·½H₂O ].",
      concept_questions: [
        "Why is Plaster of Paris called 'hemihydrate' if half a water molecule cannot physically exist?",
        "What happens when Plaster of Paris is mixed with water?"
      ]
    }
  ];

  // Chapter 3: Metals and Non-metals (Mod 6: 2a4c67f1-36ed-4e94-b710-2bae7a129384)
  const ch3Questions = [
    {
      problem: "NCERT Exercise Q1-Q3 & In-Text: (i) What are amphoteric oxides? Give two examples and write their reactions with both acid and base. (ii) Name two metals which react with very dilute HNO₃ to evolve H₂ gas. (iii) Why does calcium float in water?",
      solution: "Part (i): Amphoteric Oxides:\nDefinition: Metal oxides that react with both acids as well as bases to produce salt and water are called amphoteric oxides.\nExamples: Aluminium oxide (Al₂O₃) and Zinc oxide (ZnO).\n\nReactions of Aluminium Oxide (Al₂O₃):\n1. Reaction with Acid (acting as basic oxide):\nAl₂O₃(s) + 6HCl(aq) → 2AlCl₃(aq) + 3H₂O(l)\n\n2. Reaction with Base (acting as acidic oxide):\nAl₂O₃(s) + 2NaOH(aq) → 2NaAlO₂(aq) [Sodium aluminate] + H₂O(l)\n\nPart (ii): Metals evolving H₂ with dilute HNO₃:\nGeneral fact: Dilute HNO₃ is a strong oxidising agent; it oxidises H₂ produced to water and itself gets reduced to nitrogen oxides (N₂O, NO, NO₂).\nException: Magnesium (Mg) and Manganese (Mn) are so reactive that they react with very dilute (1%) HNO₃ to evolve hydrogen gas:\nMg(s) + 2HNO₃(aq) → Mg(NO₃)₂(aq) + H₂(g)↑\nMn(s) + 2HNO₃(aq) → Mn(NO₃)₂(aq) + H₂(g)↑\n\nPart (iii): Why Calcium Floats in Water:\nReaction: Ca(s) + 2H₂O(l) → Ca(OH)₂(aq) + H₂(g)↑\nCalcium reacts with cold water less violently than sodium. The heat evolved is insufficient for hydrogen to catch fire.\nThe bubbles of hydrogen gas (H₂) formed during the reaction stick to the surface of the calcium metal pieces.\nThe buoyant force of these attached gas bubbles makes calcium float.\n[ROUGH_WORK]\nAluminium oxide + base = Sodium Aluminate (NaAlO₂). Zinc oxide + base = Sodium Zincate (Na₂ZnO₂).\nBoxed Answer: [ (i) Oxides reacting with both acids and bases (Al₂O₃, ZnO); (ii) Magnesium and Manganese; (iii) Calcium floats because H₂ bubbles stick to its surface ].",
      concept_questions: [
        "Why is nitric acid generally unable to evolve hydrogen gas when reacting with metals?",
        "What is the chemical formula of sodium zincate?"
      ]
    },
    {
      problem: "NCERT Exercise Q8, Q9 & Q12: (i) Differentiate between Roasting and Calcination with chemical equations. (ii) What is the Thermite reaction? Write its equation and practical application. (iii) Draw electron dot structures for sodium, oxygen and magnesium, and show the formation of Na₂O and MgO by transfer of electrons.",
      solution: "Part (i): Roasting vs Calcination:\n1. Roasting:\nProcess of heating sulfide ores strongly in the presence of excess air to convert them into metal oxides.\nExample: Zinc blende (ZnS):\n2ZnS(s) + 3O₂(g) --Heat--> 2ZnO(s) + 2SO₂(g)↑\n\n2. Calcination:\nProcess of heating carbonate ores strongly in limited or absence of air to decompose them into metal oxides and CO₂.\nExample: Calamine (ZnCO₃):\nZnCO₃(s) --Heat--> ZnO(s) + CO₂(g)↑\n\nPart (ii): Thermite Reaction:\nDefinition: Highly exothermic reduction reaction between a metal oxide (like iron(III) oxide) and aluminium powder.\nThe heat released is so immense that the iron is produced in molten state.\nEquation:\nFe₂O₃(s) + 2Al(s) → 2Fe(l) [Molten Iron] + Al₂O₃(s) + Huge Heat\nPractical Application: Used to join cracked railway tracks or heavy cracked machine parts on-site (Thermite welding).\n\nPart (iii): Formation of Ionic Compounds:\n1. Magnesium Oxide (MgO):\nMg (Atomic No 12): 2, 8, 2 → loses 2 electrons → Mg²⁺ [2, 8]\nO (Atomic No 8): 2, 6 → gains 2 electrons → O²⁻ [2, 8]\nMg: + :Ö: → [Mg]²⁺ [:Ö:]²⁻ → MgO\n\n2. Sodium Oxide (Na₂O):\n2 Na atoms (Atomic No 11): each 2, 8, 1 → each loses 1 electron → 2 Na⁺\nO (Atomic No 8): 2, 6 → gains 2 electrons → O²⁻\n2 Na• + :Ö: → 2[Na]⁺ [:Ö:]²⁻ → Na₂O\nIonic compounds are held together by strong electrostatic forces of attraction.\n[ROUGH_WORK]\nRoasting = Air present (Sulfide ore). Calcination = Carbonate ore heated in limited air.\nBoxed Answer: [ (i) Roasting: 2ZnS + 3O₂ → 2ZnO + 2SO₂; Calcination: ZnCO₃ → ZnO + CO₂; (ii) Fe₂O₃ + 2Al → 2Fe + Al₂O₃ for railway welding; (iii) Transfer of valence electrons forms Mg²⁺O²⁻ and (Na⁺)₂O²⁻ ].",
      concept_questions: [
        "Why are sulfide and carbonate ores first converted into oxides before reduction?",
        "Why do ionic compounds have high melting and boiling points?"
      ]
    }
  ];

  // Chapter 4: Carbon and its Compounds (Mod 6: 53286dec-0503-4d12-91a2-04801f0eb34e)
  const ch4Questions = [
    {
      problem: "NCERT Exercise Q1-Q3 & In-Text: (i) What are the two properties of carbon which lead to the huge number of carbon compounds we see around us? (ii) What is a homologous series? State two characteristics. (iii) Draw the electron dot structures of: (a) Ethanoic acid (CH₃COOH) (b) Propanone (CH₃COCH₃) (c) Cyclopentane (C₅H₁₀).",
      solution: "Part (i): Two Unique Properties of Carbon:\n1. Catenation: The unique ability of carbon atoms to form strong, stable covalent bonds with other carbon atoms, forming long straight chains, branched chains, or closed rings. Carbon-carbon bond energy is high (347 kJ/mol) due to small atomic size.\n2. Tetravalency: Carbon has valency 4. It can bond with four other atoms of carbon or other monovalent/divalent elements (H, O, N, S, halogens).\n\nPart (ii): Homologous Series:\nDefinition: A family of organic compounds having the same functional group and similar chemical properties in which successive members differ by a -CH₂- unit.\nCharacteristics:\n1. Molecular Formula difference: Any two successive members differ by a -CH₂- unit and a molecular mass of 14 u (C=12, H=2).\n2. Chemical & Physical trends: Members show identical chemical properties (governed by the functional group) and a regular gradation in physical properties (melting point, boiling point, density increase with molecular mass).\n\nPart (iii): Electron Dot Structures:\n(a) Ethanoic acid (CH₃COOH):\nCarbon 1 has 3 single bonds with H and 1 single bond with Carbon 2.\nCarbon 2 has a double bond with O (:O::) and a single bond with -OH (C:O:H).\n\n(b) Propanone (Acetone, CH₃COCH₃):\nCentral carbon has a double bond with oxygen (C=O) and single bonds with two methyl carbons (H₃C-C(=O)-CH₃).\n\n(c) Cyclopentane (C₅H₁₀):\nRing of 5 carbon atoms in a pentagon, each carbon bonded to 2 adjacent carbons and 2 hydrogen atoms via single covalent bonds (total 15 single covalent bonds = 30 shared electrons).\n[ROUGH_WORK]\nHomologous series difference = -CH₂- = 14 u. General formula of alkanes: C_n H_{2n+2}.\nBoxed Answer: [ (i) Catenation and Tetravalency; (ii) Successive members differ by -CH₂- (14 u) with identical functional groups; (iii) Validated covalent electron dot structures for CH₃COOH, CH₃COCH₃, and C₅H₁₀ ].",
      concept_questions: [
        "Why does carbon form covalent bonds rather than C⁴⁺ cation or C⁴⁻ anion?",
        "What is the general formula for the homologous series of alkenes?"
      ]
    },
    {
      problem: "NCERT Exercise Q8, Q11 & Q15: (i) Differentiate between Ethanol and Ethanoic acid on the basis of a chemical test. (ii) What is hydrogenation? What is its industrial application? (iii) Explain the mechanism of the cleansing action of soaps. Why does soap not work in hard water?",
      solution: "Part (i): Chemical Test to Distinguish Ethanol vs Ethanoic Acid:\nTest: Reaction with Sodium Hydrogen Carbonate (NaHCO₃ / Baking soda):\n1. Add a pinch of NaHCO₃ to Ethanoic Acid (CH₃COOH):\nBrisk effervescence of colourless, odourless Carbon Dioxide (CO₂) gas is produced, which turns lime water milky:\nCH₃COOH(aq) + NaHCO₃(s) → CH₃COONa(aq) + H₂O(l) + CO₂(g)↑\n2. Add NaHCO₃ to Ethanol (C₂H₅OH):\nNo reaction or effervescence occurs because ethanol is neutral and cannot displace CO₂ from carbonates.\n\nPart (ii): Hydrogenation & Industrial Application:\nDefinition: The addition of hydrogen to unsaturated hydrocarbons (alkenes or alkynes with double or triple bonds) in the presence of a nickel (Ni) or palladium catalyst to form saturated hydrocarbons.\nEquation:\nR₂C=CR₂ + H₂ --Ni Catalyst / 473 K--> R₂CH-CHR₂\nIndustrial Application: Hydrogenation of liquid vegetable oils (containing unsaturated fatty acids, healthy) to form solid vegetable ghee/vanaspati (saturated fats).\n\nPart (iii): Cleansing Action of Soap & Micelle Formation:\nA soap molecule (e.g. sodium stearate, C₁₇H₃₅COO⁻Na⁺) has two ends:\n1. Ionic end (COO⁻Na⁺): Hydrophilic (water-loving), dissolves in water.\n2. Hydrocarbon tail (C₁₇H₃₅): Hydrophobic (water-fearing / lipophilic), dissolves in oil and grease.\n\nMechanism:\nWhen soap is dissolved in water, the molecules arrange themselves into spherical clusters called Micelles.\nThe hydrophobic hydrocarbon tails point inwards towards the center, trapping the oily dirt droplet.\nThe hydrophilic ionic heads face outward into the surrounding water.\nThis forms an emulsion in water. When agitated and rinsed, the micelles holding the dirt are washed away.\n\nHard Water Issue:\nHard water contains dissolved calcium (Ca²⁺) and magnesium (Mg²⁺) salts.\nSoap molecules react with these ions to form an insoluble sticky white precipitate called Scum:\n2C₁₇H₃₅COONa + Ca²⁺ → (C₁₇H₃₅COO)₂Ca↓ [Scum] + 2Na⁺\nScum wastes soap and adheres to fabric. Synthetic detergents solve this because their charged ends (-SO₃⁻Na⁺) do not form insoluble precipitates with Ca²⁺ and Mg²⁺.\n[ROUGH_WORK]\nSoap + hard water = Scum. Detergent + hard water = Clean foam.\nBoxed Answer: [ (i) NaHCO₃ gives brisk effervescence with ethanoic acid; (ii) Hydrogenation converts unsaturated vegetable oils to saturated fats; (iii) Soap forms micelles with hydrophobic tails trapping dirt; hard water forms insoluble scum with Ca²⁺/Mg²⁺ ].",
      concept_questions: [
        "Why are detergents able to lather easily even in hard water?",
        "What is an esterification reaction, and what characteristic odor do esters possess?"
      ]
    }
  ];

  // Upload to Supabase
  const ch1Mod6Id = 'e53978d2-8aa2-4c33-9103-bb9eaf4b43f9';
  const ch2Mod5Id = '292b89a2-63f2-473a-935e-abf431a17c94';
  const ch3Mod6Id = '2a4c67f1-36ed-4e94-b710-2bae7a129384';
  const ch4Mod6Id = '53286dec-0503-4d12-91a2-04801f0eb34e';

  await supabase.from('syllabus_modules').update({ worked_examples: ch1Questions }).eq('id', ch1Mod6Id);
  console.log('✓ Class 10 Science Ch 1 Solver updated (Chemical Reactions & Equations Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: ch2Questions }).eq('id', ch2Mod5Id);
  console.log('✓ Class 10 Science Ch 2 Solver updated (Acids, Bases & Salts Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: ch3Questions }).eq('id', ch3Mod6Id);
  console.log('✓ Class 10 Science Ch 3 Solver updated (Metals & Non-metals Complete)');

  await supabase.from('syllabus_modules').update({ worked_examples: ch4Questions }).eq('id', ch4Mod6Id);
  console.log('✓ Class 10 Science Ch 4 Solver updated (Carbon & its Compounds Complete)');

  console.log('\n=== CHEMISTRY CHAPTERS ENRICHMENT 100% COMPLETE ===\n');
}

enrichScienceChem();
