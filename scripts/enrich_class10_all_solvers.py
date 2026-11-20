import json
import os
import glob

DIR_10 = "scripts/science_class10_modules"

def build_all_class10_solvers():
    # Chapter 2: Acids, Bases, Salts
    ch2_solver = [
        {
            "problem": "In-Text Question (Section 2.1, p. 6): Why should curd and sour substances not be kept in brass and copper vessels?",
            "given": "Curd and sour food items contain organic acids (lactic acid).",
            "formula": "Acid + Metal -> Salt + Hydrogen gas.",
            "substitution": "Organic acids react with copper and brass (copper-zinc alloy).",
            "calculation": "Acids react with brass and copper to form soluble toxic metallic salts and liberate gas. These metal compounds make food poisonous and cause heavy metal toxicity.",
            "finalAnswer": "Sour substances contain acids that react with copper and brass to produce toxic, poisonous metallic salts.",
            "unit": "Chemical reactivity",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "curd sour substances brass copper vessels reaction",
            "page": 6,
            "section": "Section 2.1"
        },
        {
            "problem": "In-Text Question (Section 2.2, p. 9): Why do HCl, HNO3 show acidic characters in aqueous solutions while alcohol and glucose solutions do not?",
            "given": "HCl, HNO3 vs C2H5OH, C6H12O6 in aqueous medium.",
            "formula": "Arrhenius acid definition: Acids dissociate in water to release mobile H+(aq) or H3O+(aq) ions.",
            "substitution": "HCl -> H+ + Cl-; Glucose and ethanol do not ionize in water.",
            "calculation": "HCl and HNO3 are polar electrolytes that ionise completely in polar water to generate hydronium ions (H3O+), which are responsible for acidic properties and electrical conductance. Alcohol and glucose consist of covalent bonds that do not dissociate into ions in water, showing no acidic behavior.",
            "finalAnswer": "HCl and HNO3 release mobile H3O+ ions in water, whereas alcohol and glucose do not ionise.",
            "unit": "Ionisation mechanics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "acid dissociation hcl vs glucose water ionisation",
            "page": 9,
            "section": "Section 2.2"
        },
        {
            "problem": "In-Text Question (Section 2.3, p. 12): Five solutions A, B, C, D and E when tested with universal indicator showed pH of 4, 1, 11, 7 and 9 respectively. Which solution is: (a) Neutral, (b) Strongly alkaline, (c) Strongly acidic, (d) Weakly acidic, (e) Weakly alkaline? Arrange in increasing order of H+ concentration.",
            "given": "pH values: A=4, B=1, C=11, D=7, E=9.",
            "formula": "pH = -log10[H+]. pH < 7 is acidic, pH = 7 is neutral, pH > 7 is basic. Lower pH indicates higher [H+].",
            "substitution": "Correlate each pH value with acidity/alkalinity scale.",
            "calculation": "(a) Neutral: D (pH = 7).\n(b) Strongly alkaline: C (pH = 11).\n(c) Strongly acidic: B (pH = 1).\n(d) Weakly acidic: A (pH = 4).\n(e) Weakly alkaline: E (pH = 9).\nIncreasing order of [H+] (lowest to highest H+ ion concentration):\npH 11 < pH 9 < pH 7 < pH 4 < pH 1 => C < E < D < A < B.",
            "finalAnswer": "(a) D (neutral); (b) C (strongly basic); (c) B (strongly acidic); (d) A (weakly acidic); (e) E (weakly basic). [H+] order: C < E < D < A < B.",
            "unit": "pH scale analysis",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "ph scale universal indicator color chart acid base",
            "page": 12,
            "section": "Section 2.3"
        },
        {
            "problem": "End-of-Chapter Exercise Q7 & Q8 (p. 18): (a) Write balanced chemical equations for reactions between dilute sulphuric acid and zinc granules, and dilute hydrochloric acid and magnesium ribbon. (b) Why does distilled water not conduct electricity, whereas rainwater does?",
            "given": "Acid-metal displacement; Electrical conductivity of water samples.",
            "formula": "Zn + H2SO4 -> ZnSO4 + H2; Mg + 2HCl -> MgCl2 + H2; Electrolytic conduction requires mobile ions.",
            "substitution": "Distilled water lacks dissolved electrolytes; Rainwater dissolves atmospheric CO2, SO2 forming carbonic acid.",
            "calculation": "(a) Zn(s) + H2SO4(aq) -> ZnSO4(aq) + H2(g); Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g).\n(b) Distilled water is pure molecular H2O with negligible ionisation ([H+] = [OH-] = 10^-7 M), lacking mobile charge carriers. Rainwater absorbs atmospheric gases (CO2, SO2) forming weak acids like H2CO3 that dissociate into mobile ions (H+, HCO3-), conducting electric current.",
            "finalAnswer": "(a) Zn + H2SO4 -> ZnSO4 + H2; Mg + 2HCl -> MgCl2 + H2; (b) Rainwater dissolves atmospheric gases forming conducting ions, whereas distilled water lacks free ions.",
            "unit": "Chemical equations & conductivity",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "distilled water vs rainwater electricity conduction experiment",
            "page": 18,
            "section": "Exercises"
        },
        {
            "problem": "End-of-Chapter Exercise Q14 & Q15 (p. 19): (a) What is Plaster of Paris? Why should it be stored in a moisture-proof container? (b) Give two important industrial uses each of washing soda and baking soda.",
            "given": "Hydrated salts: CaSO4.1/2H2O, Na2CO3.10H2O, NaHCO3.",
            "formula": "POP setting reaction: CaSO4.1/2H2O + 1.5H2O -> CaSO4.2H2O (Gypsum, hard solid mass).",
            "substitution": "Chemical property analysis of industrial sodium and calcium salts.",
            "calculation": "(a) Plaster of Paris (Calcium sulphate hemihydrate, CaSO4.1/2H2O) absorbs atmospheric moisture exothermically to form a hard, rigid crystalline mass of gypsum (CaSO4.2H2O), permanently losing its moulding properties. Hence it must be sealed in airtight moisture-proof bags.\n(b) Washing Soda (Na2CO3.10H2O): 1. Permanent hardness removal from water. 2. Glass, soap, and paper manufacturing.\nBaking Soda (NaHCO3): 1. Leavening agent in baking powder (releases CO2 on heating). 2. Antacid in medicines to neutralise excess stomach acid.",
            "finalAnswer": "(a) POP forms hard gypsum upon absorbing moisture; (b) Washing soda softens hard water and manufactures glass; Baking soda acts as leavening agent and medicinal antacid.",
            "unit": "Inorganic salt chemistry",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "plaster of paris gypsum reaction baking washing soda uses",
            "page": 19,
            "section": "Exercises"
        }
    ]

    # Chapter 3: Metals and Non-Metals
    ch3_solver = [
        {
            "problem": "In-Text Question (Section 3.1 & 3.2, p. 4 & p. 10): (a) Give an example of a metal that: is a liquid at room temperature; can be easily cut with a knife; is the best conductor of heat. (b) Explain the meanings of malleable and ductile.",
            "given": "Physical characteristics of metals and non-metals.",
            "formula": "Metallic lattice properties: Delocalised electron sea allows plastic slip (malleability/ductility) and high thermal/electrical conductivity.",
            "substitution": "Correlate specific metals with anomalous and superlative properties.",
            "calculation": "(a) Liquid metal: Mercury (Hg). Cut with knife: Sodium (Na) / Potassium (K). Best conductor: Silver (Ag).\n(b) Malleable: Property of metals allowing them to be beaten or hammered into thin sheets without shattering (e.g. Gold, Aluminium foil). Ductile: Property allowing metals to be drawn into long, thin wires without breaking (e.g. 1 g of gold can be drawn into a 2 km wire).",
            "finalAnswer": "(a) Liquid: Mercury; Cut with knife: Sodium; Best conductor: Silver; (b) Malleable = beaten into thin sheets; Ductile = drawn into thin wires.",
            "unit": "Physical metallurgy",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "properties of metals malleability ductility conductivity mercury",
            "page": 4,
            "section": "Section 3.1"
        },
        {
            "problem": "In-Text Question (Section 3.2, p. 13 & p. 17): (a) Why is sodium kept immersed in kerosene oil? (b) Write equations for the reaction of iron with steam and calcium with water.",
            "given": "Reactivity of alkali and alkaline earth metals with oxygen and water.",
            "formula": "4Na + O2 -> 2Na2O (exothermic spontaneous oxidation); 3Fe + 4H2O(g) -> Fe3O4 + 4H2; Ca + 2H2O -> Ca(OH)2 + H2.",
            "substitution": "Reactivity series dynamics.",
            "calculation": "(a) Sodium is an exceptionally reactive alkali metal. When exposed to open air, it reacts violently with atmospheric oxygen and moisture, releasing hydrogen which catches fire with an explosion. Immersing in non-polar kerosene shields it from air and moisture.\n(b) 1. Iron with steam: 3Fe(s) + 4H2O(g) -> Fe3O4(s) + 4H2(g) (Red-hot iron forms magnetic iron oxide).\n2. Calcium with water: Ca(s) + 2H2O(l) -> Ca(OH)2(aq) + H2(g) (The reaction is less violent; liberated hydrogen bubbles stick to the calcium surface, causing it to float).",
            "finalAnswer": "(a) Kept in kerosene to prevent explosive reaction with atmospheric air and moisture; (b) 3Fe + 4H2O(g) -> Fe3O4 + 4H2; Ca + 2H2O -> Ca(OH)2 + H2.",
            "unit": "Metal reactivity equations",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "sodium reaction with water kerosene iron steam experiment",
            "page": 13,
            "section": "Section 3.2"
        },
        {
            "problem": "End-of-Chapter Exercise Q6, Q7, Q8 (p. 20): (a) What are amphoteric oxides? Give two examples with balanced chemical equations. (b) Differentiate between roasting and calcination in metallurgy.",
            "given": "Metal oxide acid-base behavior; Metallurgical concentration and conversion techniques.",
            "formula": "Amphoteric: Reacts with both acids and bases to give salt and water (Al2O3, ZnO).",
            "substitution": "Al2O3 + 6HCl -> 2AlCl3 + 3H2O; Al2O3 + 2NaOH -> 2NaAlO2 + H2O.",
            "calculation": "(a) Metal oxides that show both acidic and basic behaviors, reacting with acids as well as bases to yield salt and water, are termed AMPHOTERIC OXIDES.\nEquations with Al2O3:\n1. With acid: Al2O3 + 6HCl -> 2AlCl3 + 3H2O\n2. With base: Al2O3 + 2NaOH -> 2NaAlO2 (Sodium aluminate) + H2O\n(b) Roasting vs Calcination:\n- Roasting: Heating ore strongly in the PRESENCE of excess air below its melting point; applied to SULPHIDE ores (e.g. 2ZnS + 3O2 -> 2ZnO + 2SO2).\n- Calcination: Heating ore strongly in the ABSENCE or limited supply of air; applied to CARBONATE or hydrated ores (e.g. ZnCO3 -> ZnO + CO2).",
            "finalAnswer": "(a) Amphoteric oxides react with both acids and bases (Al2O3, ZnO); (b) Roasting heats sulphide ores in excess air, while calcination heats carbonate ores in limited/no air.",
            "unit": "Chemical metallurgy",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "amphoteric oxides aluminum oxide roasting calcination metallurgy",
            "page": 20,
            "section": "Exercises"
        }
    ]

    # Chapter 4: Carbon and Its Compounds
    ch4_solver = [
        {
            "problem": "In-Text Question (Section 4.1 & 4.2, p. 4 & p. 11): (a) Draw the electron dot structures of: Carbon dioxide (CO2), Methane (CH4), and Nitrogen molecule (N2). (b) What are the two unique properties of carbon that lead to the formation of a huge variety of organic compounds?",
            "given": "Covalent bonding in carbon; Valency and electronic configuration.",
            "formula": "Octet rule; Catenation (self-linking via strong C-C covalent bonds) and Tetravalency.",
            "substitution": "Carbon shares 4 valence electrons; N shares 3 pairs (triple bond); O shares 2 pairs with C (double bonds).",
            "calculation": "(a) Electron Dot Structures:\n1. Methane (CH4): Central C shares 1 electron pair each with 4 H atoms (4 single C-H covalent bonds).\n2. Carbon dioxide (CO2): Central C forms double covalent bonds with two O atoms: O=C=O (4 shared electron pairs).\n3. Nitrogen (N2): Two N atoms share three electron pairs forming a stable triple bond (:N≡N:).\n(b) Two properties:\n1. CATENATION: The unique ability of carbon to form strong, stable covalent bonds with other carbon atoms to form straight chains, branched networks, and rings.\n2. TETRAVALENCY: Having 4 valence electrons, carbon bonds with H, O, N, halogens, creating immense functional diversity.",
            "finalAnswer": "(a) CO2 has double bonds (O=C=O), CH4 has 4 single C-H bonds, N2 has a triple bond (:N≡N:); (b) Catenation and Tetravalency.",
            "unit": "Covalent chemical structure",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Electron dot structures of methane, carbon dioxide, and nitrogen",
            "image_search_query": "electron dot structure methane carbon dioxide nitrogen class 10",
            "page": 4,
            "section": "Section 4.1"
        },
        {
            "problem": "End-of-Chapter Exercise Q6, Q7, Q8 (p. 20): (a) How can ethanol and ethanoic acid be differentiated on the basis of their physical and chemical properties? (b) Explain the cleansing action of soaps with a micelle diagram.",
            "given": "Ethanol (C2H5OH) vs Ethanoic acid (CH3COOH); Soap surfactant cleansing mechanics.",
            "formula": "Esterification, carbonate effervescence: 2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2; Soap micelle hydrophilic head and hydrophobic hydrocarbon tail.",
            "substitution": "Contrast chemical reactions and micelle formation.",
            "calculation": "(a) Distinguishing Tests:\n1. Sodium hydrogen carbonate test: Ethanoic acid reacts with NaHCO3 with brisk effervescence liberating CO2 gas (turns lime water milky). Ethanol does not react.\n2. Litmus test: Ethanoic acid turns blue litmus red. Ethanol is neutral and causes no color change.\n(b) Cleansing Action of Soap:\nSoap molecules are sodium/potassium salts of long-chain carboxylic acids (e.g. C17H35COONa). They have two distinct ends: a hydrophobic hydrocarbon tail and a hydrophilic ionic carboxylate head (COO- Na+). In water containing greasy dirt, the hydrophobic tails dissolve into the oil droplet while ionic heads orient outward facing polar water. This forms spherical clusters called MICELLES that trap dirt in the center, allowing it to be rinsed away as an emulsion.",
            "finalAnswer": "(a) Ethanoic acid gives brisk effervescence with NaHCO3 and turns blue litmus red; ethanol does not; (b) Soap forms micelles with hydrophobic tails trapping oil inside and hydrophilic heads facing water.",
            "unit": "Organic chemistry & micelles",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Soap micelle structure trapping oily dirt particle",
            "image_search_query": "soap cleansing action micelle structure diagram class 10",
            "page": 20,
            "section": "Exercises"
        }
    ]

    # Chapter 5: Life Processes
    ch5_solver = [
        {
            "problem": "In-Text Question (Nutrition & Respiration): (a) What are the necessary conditions for autotrophic nutrition and what are its by-products? (b) Differentiate between aerobic and anaerobic respiration in terms of ATP yield and end-products.",
            "given": "Photosynthetic and respiratory biochemical pathways.",
            "formula": "Photosynthesis: 6CO2 + 12H2O + Sunlight + Chlorophyll -> C6H12O6 + 6O2 + 6H2O. Aerobic yield = 36-38 ATP; Anaerobic yield = 2 ATP.",
            "substitution": "Analyze metabolic equations.",
            "calculation": "(a) Necessary conditions: Chlorophyll pigment, solar radiation (sunlight), carbon dioxide (CO2), and water (H2O). By-products: Oxygen gas (O2) and water.\n(b) Aerobic vs Anaerobic Respiration:\n1. Aerobic: Occurs in mitochondria in the presence of oxygen. Glucose is completely broken down to CO2 and H2O, yielding high energy (36–38 ATP per glucose molecule).\n2. Anaerobic: Occurs in cytoplasm in the absence of oxygen. In yeast (fermentation), end-products are Ethanol + CO2 + 2 ATP. In human muscle cells during strenuous exercise, end-product is Lactic Acid + 2 ATP (causing muscle fatigue and cramps).",
            "finalAnswer": "(a) Conditions: Sunlight, chlorophyll, CO2, H2O; by-product is O2; (b) Aerobic yields 36-38 ATP with CO2 + H2O; Anaerobic yields only 2 ATP with ethanol/lactic acid.",
            "unit": "Biochemical bioenergetics",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "aerobic versus anaerobic respiration pathways glucose breakdown",
            "page": 10,
            "section": "In-Text Nutrition"
        },
        {
            "problem": "In-Text Question (Transportation & Excretion): (a) What is double circulation in human beings and why is it necessary? (b) Describe the structure and functioning of a nephron in human kidneys.",
            "given": "Cardiovascular double loop and renal filtration units.",
            "formula": "Double circulation: Pulmonary circuit (heart -> lungs -> heart) + Systemic circuit (heart -> body -> heart).",
            "substitution": "Trace blood flow and ultrafiltration in nephron.",
            "calculation": "(a) Double circulation: Blood flows through the four-chambered heart twice during one complete cycle through the body (pulmonary circulation to oxygenate blood, systemic circulation to supply tissues). Necessity: Completely separates oxygenated and deoxygenated blood, ensuring high oxygen delivery efficiency to maintain constant homeostatic body temperature (endothermy).\n(b) Nephron Function: 1. Ultrafiltration: High hydrostatic pressure in glomerulus forces water, glucose, amino acids, salts, and urea into Bowman's capsule forming glomerular filtrate. 2. Selective Reabsorption: Along proximal tubule and loop of Henle, useful substances (glucose, ions, water) are reabsorbed into peritubular capillaries. 3. Tubular Secretion: Extra ions and urea are secreted into collecting duct to form urine.",
            "finalAnswer": "(a) Double circulation passes blood twice through the heart, ensuring complete separation of oxygenated/deoxygenated blood; (b) Nephron filters blood in glomerulus, reabsorbs nutrients in tubules, and collects urine.",
            "unit": "Physiological organ systems",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Structure of a nephron showing glomerulus, tubule, and collecting duct",
            "image_search_query": "nephron structure and function diagram human kidney class 10",
            "page": 20,
            "section": "In-Text Excretion"
        }
    ]

    # Chapter 9: Light - Reflection and Refraction
    ch9_solver = [
        {
            "problem": "In-Text Question (Section 9.2, p. 12): A concave mirror produces three times magnified real image of an object placed at 10 cm in front of it. Where is the image located? What is the focal length of the mirror?",
            "given": "Object distance u = -10 cm (sign convention); Magnification m = -3 (real, inverted image).",
            "formula": "Magnification $m = -\\frac{v}{u}$; Mirror Formula: $\\frac{1}{f} = \\frac{1}{v} + \\frac{1}{u}$.",
            "substitution": "$-3 = -\\frac{v}{-10} \\implies -3 = \\frac{v}{10} \\implies v = -30\\text{ cm}$.",
            "calculation": "1. Image distance: $v = -30\\text{ cm}$ (located 30 cm in front of the concave mirror on the same side as object).\n2. Focal length:\n   $\\frac{1}{f} = \\frac{1}{-30} + \\frac{1}{-10} = \\frac{-1 - 3}{30} = \\frac{-4}{30} = -\\frac{2}{15}$.\n   $f = -\\frac{15}{2} = -7.5\\text{ cm}$.",
            "finalAnswer": "Image is located at 30 cm in front of the mirror (v = -30 cm); Focal length of the mirror is -7.5 cm.",
            "unit": "centimeters (cm)",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Concave mirror real magnified image ray diagram",
            "image_search_query": "concave mirror real magnified image ray diagram optics",
            "page": 12,
            "section": "Section 9.2"
        },
        {
            "problem": "In-Text Question (Section 9.3, p. 17): Light enters from air to glass having refractive index 1.50. What is the speed of light in glass? (Speed of light in vacuum c = 3 * 10^8 m s^-1).",
            "given": "Refractive index of glass n = 1.50; Speed of light in vacuum $c = 3 \\times 10^8\\text{ m s}^{-1}$.",
            "formula": "Absolute Refractive Index $n = \\frac{c}{v} \\implies v = \\frac{c}{n}$.",
            "substitution": "$v = \\frac{3 \\times 10^8}{1.50}$.",
            "calculation": "$v = 2.0 \\times 10^8\\text{ m s}^{-1}$.",
            "finalAnswer": "The speed of light in glass is 2.0 * 10^8 m s^-1.",
            "unit": "m s⁻¹",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "refraction of light speed in medium snell law calculation",
            "page": 17,
            "section": "Section 9.3"
        },
        {
            "problem": "End-of-Chapter Exercise Q10 (p. 26): An object 5 cm in length is held 25 cm away from a converging lens of focal length 10 cm. Draw the ray diagram and find the position, size, and the nature of the image formed.",
            "given": "Object height $h_1 = +5\\text{ cm}$; Object distance $u = -25\\text{ cm}$; Focal length of convex lens $f = +10\\text{ cm}$.",
            "formula": "Lens Formula: $\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u} \\implies \\frac{1}{v} = \\frac{1}{f} + \\frac{1}{u}$; Magnification $m = \\frac{v}{u} = \\frac{h_2}{h_1}$.",
            "substitution": "$\\frac{1}{v} = \\frac{1}{10} + \\frac{1}{-25} = \\frac{1}{10} - \\frac{1}{25} = \\frac{5 - 2}{50} = \\frac{3}{50}$.",
            "calculation": "1. Image distance: $v = +\\frac{50}{3} \\approx +16.67\\text{ cm}$ (formed on opposite side of lens, real).\n2. Image height: $h_2 = h_1 \\times \\frac{v}{u} = 5 \\times \\frac{50/3}{-25} = 5 \\times \\left(-\\frac{2}{3}\\right) = -\\frac{10}{3} \\approx -3.33\\text{ cm}$.\n3. Nature: Real, inverted, and diminished (height 3.33 cm).",
            "finalAnswer": "Image is real, inverted, located at +16.67 cm behind the lens with height -3.33 cm.",
            "unit": "centimeters (cm)",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Convex lens real inverted diminished image ray diagram",
            "image_search_query": "convex lens ray diagram real inverted image focal length",
            "page": 26,
            "section": "Exercises"
        }
    ]

    # Chapter 11: Electricity
    ch11_solver = [
        {
            "problem": "In-Text Question (Section 11.1 & 11.2, p. 2 & p. 4): (a) A current of 0.5 A is drawn by a filament of an electric bulb for 10 minutes. Find the amount of electric charge that flows through the circuit. (b) How much work is done in moving a charge of 2 C across two points having a potential difference 12 V?",
            "given": "(a) Current I = 0.5 A; Time t = 10 min = 600 s.\n(b) Charge Q = 2 C; Potential difference V = 12 V.",
            "formula": "(a) Electric charge $Q = I \\times t$; (b) Work done $W = V \\times Q$.",
            "substitution": "(a) $Q = 0.5 \\times 600$; (b) $W = 12 \\times 2$.",
            "calculation": "(a) $Q = 300\\text{ Coulombs (C)}$.\n(b) $W = 24\\text{ Joules (J)}$.",
            "finalAnswer": "(a) Amount of charge is 300 C; (b) Work done is 24 J.",
            "unit": "Coulombs and Joules",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "electric charge current time potential difference formula",
            "page": 2,
            "section": "Section 11.1"
        },
        {
            "problem": "In-Text Question (Section 11.5, p. 15): How can three resistors of resistances 2 Ω, 3 Ω, and 6 Ω be connected to give a total resistance of: (a) 4 Ω, (b) 1 Ω?",
            "given": "Resistors $R_1 = 2\\,\\Omega$, $R_2 = 3\\,\\Omega$, $R_3 = 6\\,\\Omega$.",
            "formula": "Series: $R_s = R_1 + R_2$; Parallel: $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}$.",
            "substitution": "(a) Parallel combination of 3 Ω and 6 Ω in series with 2 Ω.\n(b) All three resistors in parallel.",
            "calculation": "1. Case (a): Connect 3 Ω and 6 Ω in parallel:\n   $R_p = \\frac{3 \\times 6}{3 + 6} = \\frac{18}{9} = 2\\,\\Omega$.\n   Connect this combination in series with the 2 Ω resistor:\n   $R_{\\text{total}} = 2\\,\\Omega + R_p = 2 + 2 = 4\\,\\Omega$.\n2. Case (b): Connect all three resistors in parallel:\n   $\\frac{1}{R_p} = \\frac{1}{2} + \\frac{1}{3} + \\frac{1}{6} = \\frac{3 + 2 + 1}{6} = \\frac{6}{6} = 1\\,\\Omega \\implies R_p = 1\\,\\Omega$.",
            "finalAnswer": "(a) Connect 3 Ω and 6 Ω in parallel, then in series with 2 Ω (total 4 Ω); (b) Connect all three resistors in parallel (total 1 Ω).",
            "unit": "Ohms (Ω)",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Circuit combination of three resistors in series and parallel",
            "image_search_query": "resistors combination series parallel circuit diagram class 10",
            "page": 15,
            "section": "Section 11.5"
        },
        {
            "problem": "End-of-Chapter Exercise Q11 & Q12 (p. 23): (a) An electric iron of resistance 20 Ω takes a current of 5 A. Calculate the heat developed in 30 s. (b) An electric motor takes 5 A from a 220 V line. Determine the power of the motor and the energy consumed in 2 hours.",
            "given": "(a) $R = 20\\,\\Omega$, $I = 5\\text{ A}$, $t = 30\\text{ s}$.\n(b) $I = 5\\text{ A}$, $V = 220\\text{ V}$, $t = 2\\text{ h} = 7200\\text{ s}$.",
            "formula": "(a) Joule's Law of Heating: $H = I^2 R t$; (b) Electric Power $P = V \\times I$; Energy $E = P \\times t$.",
            "substitution": "(a) $H = (5)^2 \\times 20 \\times 30$; (b) $P = 220 \\times 5$; $E = 1100 \\times 7200$.",
            "calculation": "(a) $H = 25 \\times 20 \\times 30 = 500 \\times 30 = 15,000\\text{ J} = 15\\text{ kJ}$.\n(b) Power: $P = 1100\\text{ W} = 1.1\\text{ kW}$.\nEnergy: $E = 1.1\\text{ kW} \\times 2\\text{ h} = 2.2\\text{ kWh}$ (or $1100 \\times 7200 = 7.92 \\times 10^6\\text{ J} = 7.92\\text{ MJ}$).",
            "finalAnswer": "(a) Heat developed is 15 kJ; (b) Power of motor is 1.1 kW (1100 W) and energy consumed is 2.2 kWh (7.92 MJ).",
            "unit": "kJ and kWh",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "joules heating law power energy electricity calculation",
            "page": 23,
            "section": "Exercises"
        }
    ]

    # Chapter 12: Magnetic Effects of Electric Current
    ch12_solver = [
        {
            "problem": "In-Text Question (Section 12.1 & 12.2, p. 6 & p. 9): (a) State Right-Hand Thumb Rule and Maxwell's Corkscrew Rule. (b) Why don't two magnetic field lines ever intersect each other?",
            "given": "Magnetic field geometry surrounding current-carrying conductors and solenoids.",
            "formula": "Biot-Savart Law / Ampere's circuital law; Tangent to field line gives magnetic field direction vector B.",
            "substitution": "Geometric vector direction at intersection point.",
            "calculation": "(a) Right-Hand Thumb Rule: Imagine grasping a straight current-carrying wire in your right hand with the thumb pointing in the direction of current. Your curled fingers will point in the direction of concentric magnetic field lines.\n(b) Intersection impossibility: The tangent to a magnetic field line at any point gives the unique direction of the magnetic field vector B at that point. If two lines intersected, a magnetic compass needle placed at the intersection would have to point in two different directions simultaneously, which is physically impossible. Hence magnetic field lines never intersect.",
            "finalAnswer": "(a) Thumb points along current, curled fingers give magnetic field direction; (b) Field lines never cross because the magnetic field can have only one unique direction at any given point.",
            "unit": "Magnetic field physics",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Right-hand thumb rule and non-intersecting magnetic field lines",
            "image_search_query": "right hand thumb rule magnetic field lines intersection physics",
            "page": 6,
            "section": "Section 12.1"
        },
        {
            "problem": "End-of-Chapter Exercise Q6 & Q7 (p. 13): (a) State Fleming's Left-Hand Rule and its application. (b) What is the function of an earth wire in domestic electrical appliances? Why must metallic appliances be earthed?",
            "given": "Lorentz magnetic force on current carrier; Domestic electrical safety.",
            "formula": "Lorentz force $\\vec{F} = I(\\vec{L} \\times \\vec{B})$; Earth connection provides low-resistance path to ground ($R_{\\text{earth}} \\to 0$).",
            "substitution": "Forefinger = Field B, Centre finger = Current I, Thumb = Force F.",
            "calculation": "(a) Fleming's Left-Hand Rule: Stretch the thumb, forefinger, and middle finger of the left hand mutually perpendicular. If the forefinger points in direction of magnetic field (B) and middle finger in direction of current (I), the thumb indicates the direction of mechanical motion/force (F) acting on the conductor. Applied in electric motors.\n(b) Earth Wire: The green earth wire connects the metallic outer casing of high-power appliances (refrigerators, irons, toasters) directly to a buried copper earth plate. If live wire insulation fails and touches the metallic body, the low-resistance ground path shunts fault current into the earth, blowing the fuse or tripping the circuit breaker immediately and preventing lethal electric shocks to the user.",
            "finalAnswer": "(a) Fleming's Left-Hand Rule determines direction of motor force (Thumb = Force, Forefinger = Field, Middle = Current); (b) Earth wire channels leakage current safely into ground, preventing lethal electric shock.",
            "unit": "Electrical safety & motor rule",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Fleming's left-hand rule and domestic three-pin earth wiring",
            "image_search_query": "flemings left hand rule domestic earthing safety diagram",
            "page": 13,
            "section": "Exercises"
        }
    ]

    # Chapter 13: Our Environment
    ch13_solver = [
        {
            "problem": "In-Text Question (Section 13.1 & 13.2, p. 5 & p. 9): (a) What are trophic levels? Give an example of a 4-step food chain and state the trophic level of each organism. (b) Explain the 10% Law of energy transfer in an ecosystem.",
            "given": "Ecological energy dynamics and Lindeman's 10% efficiency law.",
            "formula": "Energy at trophic level $(n+1) = 0.10 \\times \\text{Energy at level } n$.",
            "substitution": "Grass (10,000 J) -> Deer (1,000 J) -> Tiger (100 J).",
            "calculation": "(a) Trophic levels are the sequential feeding steps or nutritional tiers in an ecological food chain:\nExample 4-step grassland food chain:\n1. Grass / Producers (T1: First trophic level)\n2. Grasshopper / Primary Consumer (T2: Second trophic level)\n3. Frog / Secondary Consumer (T3: Third trophic level)\n4. Snake / Tertiary Consumer (T4: Fourth trophic level)\n(b) Lindeman's 10% Law: Only approximately 10% of the energy stored in organic biomass is transferred from one trophic level to the next. The remaining 90% is dissipated as respiratory heat, used for metabolic maintenance, reproduction, and unassimilated waste. Because energy drops drastically ($10,000\\text{ J} \\to 1,000\\text{ J} \\to 100\\text{ J} \\to 10\\text{ J}$), food chains rarely exceed 4 to 5 trophic tiers.",
            "finalAnswer": "(a) Trophic levels are feeding tiers in a food chain (Producer -> Primary Consumer -> Secondary Consumer -> Tertiary Consumer); (b) Only 10% of biomass energy passes to the next trophic level; 90% is lost as metabolic heat.",
            "unit": "Ecosystem energy dynamics",
            "has_diagram": True,
            "diagram_source": "image_search",
            "figure_caption": "Ecological pyramid of energy showing 10% transfer between trophic levels",
            "image_search_query": "trophic levels 10 percent energy law pyramid ecosystem",
            "page": 5,
            "section": "Section 13.1"
        },
        {
            "problem": "End-of-Chapter Exercise Q6 & Q7 (p. 9): (a) What is biological magnification? Will the concentration of levels of this magnification be different at different levels of the ecosystem? (b) What is ozone and how does it affect any ecosystem? What causes the depletion of the ozone layer?",
            "given": "Ecotoxicological bioaccumulation; Stratospheric O3 layer photochemistry.",
            "formula": "Ozone creation: O2 + UV -> O + O; O + O2 -> O3. CFC radical catalytic ozone destruction.",
            "substitution": "Biomagnification of non-biodegradable pesticides (DDT) up trophic chains.",
            "calculation": "(a) Biological Magnification is the progressive increase in the concentration of non-biodegradable chemical toxins (such as pesticides, DDT, heavy metals) per unit biomass at progressively higher trophic levels of a food chain. Because these toxins cannot be metabolized or excreted, they accumulate. Concentration is HIGHEST at the top carnivore tier (e.g. humans or predatory birds).\n(b) Ozone (O3) in the stratosphere acts as a planetary protective shield absorbing harmful solar ultraviolet (UV-B) radiation, preventing skin cancer, cataracts, and phytoplankton mortality. Depletion is caused by Chlorofluorocarbons (CFCs), which release free chlorine radicals under UV that catalytically destroy thousands of ozone molecules ($Cl + O3 -> ClO + O2$).",
            "finalAnswer": "(a) Biological magnification is progressive toxic accumulation, reaching maximum concentration at top trophic levels; (b) Stratospheric ozone shields Earth from lethal UV rays; depleted by CFCs.",
            "unit": "Environmental ecotoxicology",
            "has_diagram": False,
            "diagram_source": "image_search",
            "figure_caption": "",
            "image_search_query": "biological magnification food chain ozone layer depletion cfcs",
            "page": 9,
            "section": "Exercises"
        }
    ]

    # Map solvers to chapter json files
    solvers = {
        "chapter_2_acids_bases_and_salts.json": ch2_solver,
        "chapter_3_metals_and_non_metals.json": ch3_solver,
        "chapter_4_carbon_and_its_compounds.json": ch4_solver,
        "chapter_5_life_processes.json": ch5_solver,
        "chapter_9_light_reflection_and_refraction.json": ch9_solver,
        "chapter_11_electricity.json": ch11_solver,
        "chapter_12_magnetic_effects_of_electric_current.json": ch12_solver,
        "chapter_13_our_environment.json": ch13_solver
    }

    for fname, examples in solvers.items():
        fpath = os.path.join(DIR_10, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            mods = json.load(f)
        
        m_solver = mods[-1]
        m_solver["worked_examples"] = examples
        m_solver["title"] = "NCERT In-Text & Chapter-End Exercises Master Solver"
        
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(mods, f, indent=2)
        print(f"Updated {fname} with {len(examples)} exhaustive solver questions!")

if __name__ == "__main__":
    build_all_class10_solvers()
