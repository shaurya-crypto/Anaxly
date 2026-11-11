"""
ch10_thermal_properties_of_matter.py
CBSE Class 11 Physics - Chapter 10: Thermal Properties of Matter
Part 2 (Final-Term Examination Syllabus, Unit VII: Properties of Bulk Matter)
Exhaustive, University-Prep & Board-Exam Topper Curriculum Decomposition
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11_pt2 as sb2

CURRICULUM_ID = "c11_phy_ch10_thermal"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"
UNIT = "Unit VII: Properties of Bulk Matter"
SYLLABUS_TERM = "Final-Term Examination"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Temperature, Thermometry & Thermal Expansion
    # Order Index: 58
    # -------------------------------------------------------------
    mod1_svg = sb2.build_stress_strain_curve_svg(
        material="Thermal Expansion",
        title="Thermal Expansion Coefficients (α, β, γ) & Anomalous Water Density",
        caption="Linear ΔL = αLΔT | Area ΔA = 2αAΔT | Volume ΔV = 3αVΔT | Water maximum density at 4°C"
    )

    modules.append({
        "order_index": 58,
        "title": "Temperature Scales, Thermometry & Thermal Expansion of Solids, Liquids, and Gases",
        "description": "Distinction between heat (internal energy in transit) and temperature (measure of average microscopic translational kinetic energy), conversion between Celsius, Fahrenheit, and Kelvin scales, gas thermometers, absolute zero, linear expansion (α), areal expansion (β = 2α), volumetric expansion (γ = 3α), thermal stress in clamped rods, and the anomalous expansion of water between 0°C and 4°C preserving aquatic life in frozen lakes.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Definition of Heat: Energy transferred between systems due to temperature difference (SI unit: Joule, traditional unit: Calorie = 4.186 J)",
            "Definition of Temperature: Macroscopic property determining thermal equilibrium direction; measure of average translational KE of molecules",
            "Thermometry & Fixed Points: Ice point (0°C, 32°F, 273.15 K) and Steam point (100°C, 212°F, 373.15 K)",
            "Conversion formula: (T_C - 0) / 100 = (T_F - 32) / 180 = (T_K - 273.15) / 100",
            "Constant-Volume Gas Thermometer & Absolute Zero (T = 0 K = -273.15°C) where gas pressure extrapolates to zero",
            "Linear Thermal Expansion of Solids: Fractional change in length proportional to temperature rise (ΔL / L = α_L ΔT => ΔL = α_L L ΔT)",
            "Coefficient of Linear Expansion (α_L, SI unit: K⁻¹ or °C⁻¹)",
            "Areal / Superficial Expansion: ΔA / A = α_A ΔT where α_A = 2 α_L",
            "Volumetric / Cubical Expansion: ΔV / V = α_V ΔT where α_V = 3 α_L",
            "Thermal Stress in Rigidly Fixed Rods: Compressive stress developed when thermal expansion is prevented: σ = Y (ΔL / L) = Y α_L ΔT; Force F = Y A α_L ΔT",
            "Expansion of Liquids & Apparent Expansion: Apparent coefficient γ_app = γ_real - γ_vessel",
            "Anomalous Expansion of Water: Water contracts as temperature increases from 0°C to 4°C; volume is minimum and density is maximum at 4°C (1000 kg/m³)",
            "Ecological Significance of Anomalous Water Expansion: Deep lake water remains at 4°C under surface ice layer, preserving aquatic marine life through winter"
        ],
        "key_concepts": [
            "Scale Conversion: (T_C / 5) = (T_F - 32) / 9 = (T_K - 273.15) / 5",
            "Expansion Relations: α_L : α_A : α_V = 1 : 2 : 3",
            "Thermal Stress Formula σ = Y α_L ΔT & Force F = Y A α_L ΔT",
            "Anomalous Expansion of Water (Maximum Density at 4°C = 1.000 g/cm³)"
        ],
        "success_criteria": [
            "Convert temperatures accurately across Celsius, Fahrenheit, and Kelvin scales",
            "Prove geometrically that α_A = 2α_L and α_V = 3α_L for isotropic solids",
            "Calculate thermal stress and tension developed in clamped metal rails undergoing temperature shifts",
            "Explain how the anomalous expansion of water allows fish to survive beneath frozen lake ice"
        ],
        "chapter_notes": """# Temperature, Thermometry & Thermal Expansion
## 1. Temperature Scales & Conversion
Temperature is a macroscopic measure of the thermal state of a system:
$$\\frac{T_C - 0}{100} = \\frac{T_F - 32}{180} = \\frac{T_K - 273.15}{100}$$
- **Triple Point of Water**: State where pure ice, liquid water, and water vapor coexist in stable thermodynamic equilibrium:
  $$T_{\\text{tr}} = 273.16\\text{ K} = 0.01^\\circ\\text{C}, \\quad P_{\\text{tr}} = 611.65\\text{ Pa} = 0.006\\text{ atm}$$

## 2. Thermal Expansion in Solids
When temperature increases by $\\Delta T$:
1. **Linear Expansion**:
   $$\\Delta L = \\alpha_L L \\Delta T \\implies L(T) = L_0 (1 + \\alpha_L \\Delta T)$$
2. **Superficial (Areal) Expansion**:
   $$\\Delta A = \\alpha_A A \\Delta T \\implies \\alpha_A = 2\\alpha_L$$
3. **Volume (Cubical) Expansion**:
   $$\\Delta V = \\alpha_V V \\Delta T \\implies \\alpha_V = 3\\alpha_L$$
   $$\\boxed{\\alpha_L : \\alpha_A : \\alpha_V = 1 : 2 : 3}$$

## 3. Thermal Stress in Constrained Bodies
If a rod of length $L$ and cross-section $A$ is rigidly fixed at both ends so it cannot expand:
$$\\text{Thermal Strain } \\varepsilon = \\frac{\\Delta L}{L} = \\alpha_L \\Delta T$$
$$\\text{Thermal Stress } \\sigma = Y \\varepsilon = Y \\alpha_L \\Delta T$$
$$\\text{Compressive Force on Supports: } F = \\sigma A = Y A \\alpha_L \\Delta T$$

## 4. Anomalous Expansion of Water
Almost all liquids expand continuously as temperature rises. Water exhibits an anomalous exception between $0^\\circ\\text{C}$ and $4^\\circ\\text{C}$:
- From $0^\\circ\\text{C}$ to $4^\\circ\\text{C}$: Volume **decreases** (density increases).
- At $4^\\circ\\text{C}$: Density reaches its absolute maximum ($\\rho_{\\text{max}} = 1000\\text{ kg/m}^3$).
- Above $4^\\circ\\text{C}$: Water expands normally (density decreases).
**Ecological Consequence**: In cold winters, surface water cools to $4^\\circ\\text{C}$, becomes heavy, and sinks to the bottom. Once the entire lake reaches $4^\\circ\\text{C}$, further cooling drops surface water to $0^\\circ\\text{C}$, forming an insulating floating sheet of ice. The bottom water remains liquid at $4^\\circ\\text{C}$, ensuring the survival of aquatic life!
""",
        "worked_examples": [
            {
                "problem": "A steel rail of length 12 m and area of cross-section 40 cm² is laid at a temperature of 20°C with no gaps. If the temperature rises to 40°C in summer, what is the thermal stress and the compressive force developed in the rail? Take Y_steel = 2.0 × 10¹¹ N/m² and α_steel = 1.2 × 10⁻⁵ K⁻¹.",
                "given": "Length L = 12 m, Cross-section A = 40 cm² = 40 × 10⁻⁴ m² = 4.0 × 10⁻³ m², T₁ = 20°C, T₂ = 40°C => ΔT = 20 K, Y = 2.0 × 10¹¹ N/m², α = 1.2 × 10⁻⁵ K⁻¹",
                "formula": "Thermal Stress σ = Y · α · ΔT; Compressive Force F = σ · A = Y · A · α · ΔT",
                "substitution": "σ = 2.0 × 10¹¹ N/m² × 1.2 × 10⁻⁵ K⁻¹ × 20 K; F = σ × (4.0 × 10⁻³ m²)",
                "calculation": "σ = 2.0 × 1.2 × 20 × 10⁶ = 48 × 10⁶ N/m² = 4.8 × 10⁷ Pa; F = 4.8 × 10⁷ N/m² × 4.0 × 10⁻³ m² = 1.92 × 10⁵ N ≈ 19.6 tonnes-force!",
                "finalAnswer": "Thermal stress σ = 4.8 × 10⁷ Pa (48 MPa); Compressive force F = 1.92 × 10⁵ N",
                "unit": "Pascals and Newtons"
            }
        ],
        "common_misconceptions": [
            "Misconception: Ice is denser than water because it is a solid. Reality: Due to the open hexagonal hydrogen-bonded crystal structure of ice, ice is actually ~9% LESS dense than liquid water (0.917 g/cm³ vs 1.000 g/cm³), which is why icebergs float on water."
        ],
        "concept_questions": [
            {
                "question": "A circular hole is drilled in a flat copper plate. When the plate is uniformly heated in an oven, what happens to the diameter of the hole?",
                "options": [
                    "The diameter of the hole increases in the exact same proportion as if it were filled with copper",
                    "The diameter of the hole decreases because the surrounding copper expands inward",
                    "The diameter remains unchanged",
                    "The hole becomes elliptical"
                ],
                "correctAnswer": "The diameter of the hole increases in the exact same proportion as if it were filled with copper",
                "explanation": "Thermal expansion is a photographic magnification of every geometric distance in the solid. Every pair of points moves farther apart. If the hole were filled with a copper plug, the plug would expand by Δd = α d ΔT. For the hole to fit the expanded plug, the hole itself must expand by the exact same amount.",
                "hint": "Think of thermal expansion as a photographic zoom: does a hole zoom inward or outward?",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Thermal Expansion & Anomalous Water Density",
                "diagram_type": "image",
                "diagram_title": "Water Density vs Temperature Curve & Frozen Lake Profile",
                "why_needed": "Visualizes the density peak at 4°C and stratification of water under ice",
                "timing_and_cue": "Stage 1 when explaining why lakes freeze from the top down",
                "what_to_explain": "How 4°C water settles at the lake bottom preserving fish",
                "image_search_query": "anomalous expansion of water density temperature curve lake ice diagram",
                "svg": mod1_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Thermal Expansion",
                    "diagram_type": "image",
                    "image_search_query": "thermal expansion hole in sheet physics diagram",
                    "svg": mod1_svg
                }
            ]
        },
        "ai_system_prompt_context": "SOCRATIC HOOK: Start with the classic physics puzzle: 'If you have a metal washer with a hole in the center, and you heat it up, does the hole get bigger or smaller?' Walk through the photographic zoom proof."
    })

    # -------------------------------------------------------------
    # MODULE 2: Specific Heat Capacity, Molar Heat & Calorimetry
    # Order Index: 59
    # -------------------------------------------------------------
    mod2_svg = sb2.build_stress_strain_curve_svg(
        material="Calorimetry",
        title="Principle of Calorimetry: Heat Lost = Heat Gained",
        caption="ΔQ = m s ΔT | Molar Heat: Cp - Cv = R (Mayer's relation) | Water high specific heat 4186 J/(kg·K)"
    )

    modules.append({
        "order_index": 59,
        "title": "Specific Heat Capacity, Molar Specific Heats (Cp, Cv) & Principle of Calorimetry",
        "description": "Thermodynamics of heat absorption: heat capacity S, specific heat capacity s, molar heat capacity C, water's exceptionally high specific heat (4186 J/kg·K) and its moderating effect on maritime climates, constant-pressure vs constant-volume molar heats (Cp and Cv), mechanical equivalent of heat, water equivalent of calorimeters, and the foundational Principle of Calorimetry (Heat Lost = Heat Gained).",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Heat Capacity (S): Heat required to raise the temperature of an entire body by 1 K (S = ΔQ / ΔT, SI: J/K)",
            "Specific Heat Capacity (s or c): Heat required per unit mass to raise temperature by 1 K: s = (1 / m) (ΔQ / ΔT) (SI: J/(kg·K))",
            "Molar Heat Capacity (C): Heat required per mole of substance to raise temperature by 1 K: C = (1 / μ) (ΔQ / ΔT) = M · s (SI: J/(mol·K))",
            "Molar Heat Capacity at Constant Volume (Cv): C_v = (1 / μ) (dQ / dT)_V",
            "Molar Heat Capacity at Constant Pressure (Cp): C_p = (1 / μ) (dQ / dT)_P",
            "Why Cp > Cv: At constant pressure, added heat must not only increase internal kinetic energy but also perform external expansion work (P ΔV)",
            "Exceptionally high specific heat of water: s_water = 4186 J/(kg·K) = 1 cal/(g·°C)",
            "Climatic and biological consequences: Mild maritime coastal climates, ocean thermal buffering, hot water bottles for fermentation, and car engine coolant",
            "Principle of Calorimetry: In an isolated, thermally insulated system, total heat lost by hot bodies equals total heat gained by cold bodies: Heat Lost = Heat Gained",
            "Water equivalent of a calorimeter (W = m_cal · s_cal): Equivalent mass of water that absorbs the same amount of heat as the calorimeter body for the same temperature rise",
            "Experimental determination of specific heat using copper calorimeter"
        ],
        "key_concepts": [
            "Heat Formula ΔQ = m · s · ΔT = μ · C · ΔT",
            "High Specific Heat of Water (4186 J/(kg·K))",
            "Why Cp > Cv (Work Done Against External Pressure P ΔV)",
            "Calorimetry Principle: ∑ Q_lost = ∑ Q_gained",
            "Water Equivalent W = m_cal · (s_cal / s_water)"
        ],
        "success_criteria": [
            "Define heat capacity, specific heat capacity, and molar heat capacity with proper SI units",
            "Explain why Cp is strictly greater than Cv for any substance",
            "Apply the principle of calorimetry to calculate unknown specific heats of alloy spheres",
            "Explain why islands and coastal cities have much smaller diurnal temperature variations than inland deserts"
        ],
        "chapter_notes": """# Specific Heat Capacity & The Science of Calorimetry
## 1. Mathematical Definitions
1. **Heat Capacity ($S$)**:
   $$S = \\frac{\\Delta Q}{\\Delta T} \\quad (\\text{SI Unit: } \\text{J}\\cdot\\text{K}^{-1})$$
2. **Specific Heat Capacity ($s$)**:
   $$s = \\frac{1}{m}\\frac{\\Delta Q}{\\Delta T} \\implies \\Delta Q = m s \\Delta T \\quad (\\text{SI Unit: } \\text{J}\\cdot\\text{kg}^{-1}\\cdot\\text{K}^{-1})$$
3. **Molar Specific Heat Capacity ($C$)**:
   $$C = \\frac{1}{\\mu}\\frac{\\Delta Q}{\\Delta T} = M s \\quad (\\text{SI Unit: } \\text{J}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1})$$
   where $\\mu$ is number of moles and $M$ is molar mass.

## 2. Why $C_p > C_v$
- At constant volume ($V = \\text{const}$), no external work is done ($W = P \\Delta V = 0$). All added heat goes exclusively into raising internal energy:
  $$\\Delta Q_v = \\Delta U = \\mu C_v \\Delta T$$
- At constant pressure ($P = \\text{const}$), the substance expands against external pressure, doing positive work ($W = P \\Delta V$). Heat must supply both internal energy AND external work:
  $$\\Delta Q_p = \\Delta U + P \\Delta V = \\mu C_p \\Delta T$$
  $$C_p - C_v > 0 \\implies C_p > C_v$$

## 3. Principle of Calorimetry
For an insulated container (calorimeter):
$$\\text{Heat Lost by Hot Bodies} = \\text{Heat Gained by Cold Bodies}$$
$$m_1 s_1 (T_1 - T_f) = m_2 s_2 (T_f - T_2) + m_{\\text{cal}} s_{\\text{cal}} (T_f - T_2)$$
$$T_f = \\frac{m_1 s_1 T_1 + m_2 s_2 T_2 + m_{\\text{cal}} s_{\\text{cal}} T_2}{m_1 s_1 + m_2 s_2 + m_{\\text{cal}} s_{\\text{cal}}}$$
""",
        "worked_examples": [
            {
                "problem": "A 0.047 kg block of copper is heated in a furnace to 100°C and then dropped into a copper calorimeter of mass 0.14 kg containing 0.25 kg of water at 20°C. The final steady temperature of the mixture is 23°C. Compute the specific heat capacity of copper. Take specific heat of water = 4.18 × 10³ J/(kg·K). (NCERT Example 10.2)",
                "given": "Mass of hot copper m_cu = 0.047 kg, Initial temp T_cu = 100°C, Mass of water m_w = 0.25 kg, Mass of calorimeter m_cal = 0.14 kg, Initial temp of water & calorimeter T_w = 20°C, Final temp T_f = 23°C, s_w = 4180 J/(kg·K)",
                "formula": "Heat Lost by hot copper = Heat Gained by (water + calorimeter) => m_cu · s_cu · (T_cu - T_f) = (m_w · s_w + m_cal · s_cu) · (T_f - T_w)",
                "substitution": "0.047 × s_cu × (100 - 23) = [ 0.25 × 4180 + 0.14 × s_cu ] × (23 - 20)",
                "calculation": "Left side = 0.047 × 77 × s_cu = 3.619 · s_cu; Right side = [ 1045 + 0.14 · s_cu ] × 3 = 3135 + 0.42 · s_cu; (3.619 - 0.42) · s_cu = 3135 => 3.199 · s_cu = 3135 => s_cu = 3135 / 3.199 = 380 J/(kg·K)",
                "finalAnswer": "Specific heat capacity of copper s_cu = 380 J/(kg·K) = 0.38 J/(g·°C)",
                "unit": "J/(kg·K)"
            }
        ],
        "common_misconceptions": [
            "Misconception: When two liquids of equal mass at different temperatures are mixed, the final equilibrium temperature is always the arithmetic mean (T1 + T2)/2. Reality: The final temperature is the arithmetic mean ONLY if the specific heat capacities are identical! If s1 ≠ s2, the final temperature is heavily weighted towards the liquid with higher heat capacity."
        ],
        "concept_questions": [
            {
                "question": "Equal masses of water (s = 4186 J/kg·K) and ethanol (s = 2440 J/kg·K) at 20°C absorb the exact same amount of heat Q. Which liquid reaches a higher final temperature?",
                "options": [
                    "Ethanol reaches a significantly higher temperature because its specific heat capacity is lower",
                    "Water reaches a higher temperature",
                    "Both reach the exact same temperature because their masses and heat inputs are equal",
                    "Neither warms up"
                ],
                "correctAnswer": "Ethanol reaches a significantly higher temperature because its specific heat capacity is lower",
                "explanation": "Temperature rise ΔT = Q / (m · s). Since heat Q and mass m are identical, ΔT is inversely proportional to specific heat capacity (ΔT ∝ 1/s). Because ethanol has a substantially lower specific heat than water (2440 vs 4186), its temperature rises roughly 1.7 times more than water.",
                "hint": "Check the inverse proportionality between ΔT and specific heat s.",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Principle of Calorimetry & Heat Balance",
                "diagram_type": "image",
                "diagram_title": "Calorimeter Construction & Thermal Energy Exchange",
                "why_needed": "Visualizes insulated jacket, stirrer, thermometer, and heat exchange",
                "timing_and_cue": "Stage 4 when solving calorimetry equations",
                "what_to_explain": "Heat Lost = Heat Gained accounting for calorimeter vessel water equivalent",
                "image_search_query": "calorimeter experiment heat lost heat gained diagram physics",
                "svg": mod2_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Calorimetry Apparatus",
                    "diagram_type": "image",
                    "image_search_query": "copper calorimeter insulated jacket diagram",
                    "svg": mod2_svg
                }
            ]
        },
        "ai_system_prompt_context": "CALORIMETRY MASTER NOTE: Remind students that temperature in ΔT has the same numerical value in Celsius as in Kelvin, so converting ΔT is unnecessary."
    })

    # -------------------------------------------------------------
    # MODULE 3: Change of State, Latent Heat, Regelation & Phase Diagrams
    # Order Index: 60
    # -------------------------------------------------------------
    mod3_svg = sb2.build_stress_strain_curve_svg(
        material="Phase Change",
        title="Phase Transition Curve: Latent Heat of Fusion & Vaporization",
        caption="Q = m L_f (Fusion: 3.33 × 10⁵ J/kg) | Q = m L_v (Vaporization: 2.26 × 10⁶ J/kg) | Regelation"
    )

    modules.append({
        "order_index": 60,
        "title": "Phase Transitions, Latent Heat of Fusion and Vaporization, Regelation & Triple Point",
        "description": "Isothermal phase transitions: melting point, boiling point, latent heat of fusion L_f (3.33 × 10⁵ J/kg for ice), latent heat of vaporization L_v (2.26 × 10⁶ J/kg for steam), why steam burns are far more severe than boiling water burns, pressure dependence of melting point (regelation experiment with weighted wire over ice block), pressure dependence of boiling point (pressure cookers vs high-altitude cooking), sublimation, and phase diagrams with the unique Triple Point of water.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Three states of matter and microscopic phase transitions: Solid <-> Liquid <-> Gas",
            "Isothermal nature of phase change: Temperature remains strictly constant while two phases coexist in equilibrium",
            "Latent Heat (L): Heat absorbed or released per unit mass during phase transition at constant temperature: L = Q / m (SI unit: J/kg)",
            "Latent Heat of Fusion (L_f): Solid to liquid transition at melting point (Ice: L_f = 3.33 × 10⁵ J/kg = 80 cal/g)",
            "Latent Heat of Vaporization (L_v): Liquid to gas transition at boiling point (Water: L_v = 2.26 × 10⁶ J/kg = 540 cal/g)",
            "Why L_v >> L_f: Vaporization completely separates molecules against attractive intermolecular bonds to infinite distance, requiring enormous work",
            "Severe burns from steam: 1 g of steam at 100°C releases 2260 J of latent heat upon condensing PLUS 4.186 J/°C as it cools, inflicting far worse burns than 100°C water",
            "Effect of Pressure on Melting Point: Substances that expand on melting (most solids): melting point rises with pressure; Substances that contract on melting (ice/water): melting point DROPS with pressure",
            "Regelation Phenomenon: Melting under pressure and freezing again when pressure is released (demonstrated by weighted thin wire passing through ice block without cutting it in half)",
            "Ice skating physics: Thin water film created under skate blade due to high localized pressure and frictional heating",
            "Effect of Pressure on Boiling Point: Boiling occurs when saturated vapor pressure equals external atmospheric pressure; High pressure (pressure cooker) elevates boiling point to ~120°C, speeding up cooking; Low pressure (mountains) depresses boiling point, making food take longer to cook",
            "Sublimation: Direct transition from solid to vapor without passing through liquid phase (dry ice / CO₂, iodine, camphor, naphthalene)",
            "Phase Diagram (P-T plane): Fusion curve, Vaporization curve, Sublimation curve, and the Triple Point where all three phases coexist"
        ],
        "key_concepts": [
            "Latent Heat Formula Q = m · L (Constant Temperature)",
            "Ice Fusion L_f = 3.33 × 10⁵ J/kg vs Steam Vaporization L_v = 2.26 × 10⁶ J/kg",
            "Why Steam Burns Are More Lethal Than Boiling Water Burns",
            "Regelation (Ice Melts Under Pressure, Refreezes Upon Release)",
            "Pressure Cooker Elevation of Boiling Point (~120°C)",
            "Triple Point of Water (T = 273.16 K, P = 0.006 atm)"
        ],
        "success_criteria": [
            "Sketch the complete heating curve of water from -10°C ice to 120°C superheated steam with flat latent plateaus",
            "Calculate total heat required to convert ice at -10°C into steam at 100°C",
            "Explain the physical mechanism of regelation and how ice skaters glide with low friction",
            "Deduce why food cooks faster in a pressure cooker using saturated vapor pressure curves"
        ],
        "chapter_notes": """# Phase Transitions, Latent Heat & Phase Diagrams
## 1. Latent Heat Formulation
During a phase change, heat is absorbed or evolved at constant temperature to alter intermolecular potential energy:
$$Q = m L \\implies L = \\frac{Q}{m} \\quad (\\text{SI Unit: } \\text{J}\\cdot\\text{kg}^{-1})$$

1. **Latent Heat of Fusion ($L_f$)**:
   $$\\text{For Ice at } 0^\\circ\\text{C}: L_f = 3.33 \\times 10^5\\text{ J/kg} = 80\\text{ cal/g}$$
2. **Latent Heat of Vaporization ($L_v$)**:
   $$\\text{For Water at } 100^\\circ\\text{C}: L_v = 2.26 \\times 10^6\\text{ J/kg} = 540\\text{ cal/g}$$
   - Notice $L_v \\approx 6.8 \\times L_f$ because boiling breaks all hydrogen bonds and performs expansion work against atmospheric pressure ($\\\\Delta V \\approx 1600\\times$).

## 2. Why Steam Burns Are Far More Severe Than Boiling Water
1 gram of boiling water at $100^\\circ\\text{C}$ cooling to skin temperature ($37^\\circ\\text{C}$) releases:
$$Q_{\\text{water}} = m s \\Delta T = (1\\text{ g})(4.186\\text{ J/g}^\\circ\\text{C})(63^\\circ\\text{C}) \\approx 264\\text{ J}$$
1 gram of steam at $100^\\circ\\text{C}$ condensing to water at $100^\\circ\\text{C}$ and then cooling releases:
$$Q_{\\text{steam}} = m L_v + m s \\Delta T = 2260\\text{ J} + 264\\text{ J} = 2524\\text{ J}$$
Steam dumps almost **10 times more heat** onto the skin!

## 3. Regelation
Substances like ice, bismuth, and antimony **contract upon melting**.
- Le Chatelier's Principle: Increasing external pressure favors the denser phase (liquid water).
- Therefore, the melting point of ice **decreases** below $0^\\circ\\text{C}$ under high pressure ($\\\\Delta T_m \\approx -0.0075^\\circ\\text{C/atm}$).
- **Regelation**: When a fine wire with heavy weights is hung over an ice block, the high pressure under the wire melts the ice at sub-zero temperatures. As the wire sinks, water refreezes above it where pressure is released, leaving the block solid and intact!
""",
        "worked_examples": [
            {
                "problem": "Calculate the total heat required to convert 3.0 kg of ice at -12°C into steam at 100°C at atmospheric pressure. Given: specific heat of ice = 2100 J/(kg·K), specific heat of water = 4186 J/(kg·K), latent heat of fusion of ice = 3.33 × 10⁵ J/kg, latent heat of vaporization of water = 2.26 × 10⁶ J/kg. (NCERT Example 10.3)",
                "given": "Mass m = 3.0 kg, T_initial = -12°C, s_ice = 2100 J/(kg·K), L_f = 3.33 × 10⁵ J/kg, s_water = 4186 J/(kg·K), L_v = 2.26 × 10⁶ J/kg",
                "formula": "Total Heat Q = Q₁ (warm ice to 0°C) + Q₂ (melt ice at 0°C) + Q₃ (heat water to 100°C) + Q₄ (vaporize water at 100°C)",
                "substitution": "Q₁ = 3.0 × 2100 × (0 - (-12)) = 3.0 × 2100 × 12; Q₂ = 3.0 × 3.33 × 10⁵; Q₃ = 3.0 × 4186 × 100; Q₄ = 3.0 × 2.26 × 10⁶",
                "calculation": "Q₁ = 75,600 J = 0.0756 × 10⁶ J; Q₂ = 0.999 × 10⁶ J; Q₃ = 1.2558 × 10⁶ J; Q₄ = 6.78 × 10⁶ J; Total Q = (0.0756 + 0.999 + 1.2558 + 6.78) × 10⁶ J = 9.1104 × 10⁶ J ≈ 9.1 × 10⁶ J",
                "finalAnswer": "Total heat required = 9.11 × 10⁶ J = 9.11 MJ",
                "unit": "Joules (MJ)"
            }
        ],
        "common_misconceptions": [
            "Misconception: Water always boils at 100°C everywhere. Reality: Water boils at 100°C ONLY at 1 atm (sea level). On Mount Everest, atmospheric pressure is ~0.33 atm, so water boils at ~68°C—far too cool to cook potatoes or lentils properly!"
        ],
        "concept_questions": [
            {
                "question": "Why does a pressure cooker cook food in less than half the time of an open pot?",
                "options": [
                    "The tight seal traps steam and raises internal pressure to ~2 atm, elevating the boiling point of water to ~120°C so food cooks at a much higher temperature",
                    "The metal reflects heat inward",
                    "Pressure pushes spices into the food",
                    "Steam destroys bacteria faster"
                ],
                "correctAnswer": "The tight seal traps steam and raises internal pressure to ~2 atm, elevating the boiling point of water to ~120°C so food cooks at a much higher temperature",
                "explanation": "Boiling occurs when saturated vapor pressure equals ambient pressure. By trapping steam, the pressure cooker increases pressure to ~2 atm, raising the boiling point of water to ~120°C. Chemical cooking reactions occur exponentially faster at 120°C than at 100°C.",
                "hint": "What happens to the boiling temperature when the external pressure is doubled?",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Heating Curve & Latent Heat Plateaus",
                "diagram_type": "image",
                "diagram_title": "Temperature vs Heat Added Curve for Water (-10°C to 120°C)",
                "why_needed": "Visualizes constant temperature flat zones during melting and boiling",
                "timing_and_cue": "Stage 2 when defining latent heat",
                "what_to_explain": "Why temperature stays flat at 0°C and 100°C while latent heat is added",
                "image_search_query": "heating curve of water temperature vs heat latent heat fusion vaporization diagram",
                "svg": mod3_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Heating Curve",
                    "diagram_type": "image",
                    "image_search_query": "water phase change heating curve diagram physics",
                    "svg": mod3_svg
                }
            ]
        },
        "ai_system_prompt_context": "SOCRATIC TIP: The severe steam burn question is a perennial favorite in exams. Write the two-step equation for steam (Q = mLv + mcΔT) on the chalkboard to make the 10x difference instantly visible."
    })

    # -------------------------------------------------------------
    # MODULE 4: Heat Transfer: Conduction & Thermal Conductivity
    # Order Index: 61
    # -------------------------------------------------------------
    mod4_svg = sb2.build_stress_strain_curve_svg(
        material="Thermal Conduction",
        title="Thermal Conduction Law & Temperature Gradient",
        caption="Heat Current H = dQ/dt = K A (T₁ - T₂) / L | Thermal Resistance R_th = L / (KA)"
    )

    modules.append({
        "order_index": 61,
        "title": "Modes of Heat Transfer: Conduction, Fourier's Law, Thermal Conductivity & Composite Slabs",
        "description": "Mechanisms of thermal energy transport: comparison of conduction, convection, and radiation. Detailed formulation of thermal conduction: temperature gradient (dT/dx), Fourier's law of heat conduction (H = dQ/dt = -K A dT/dx), coefficient of thermal conductivity K, thermal resistance R_th = L / (K A) analogous to Ohm's law, steady state temperature distribution, and series and parallel combinations of composite insulating slabs.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Three mechanisms of heat transfer: Conduction (microscopic lattice vibrations & free electrons in solids), Convection (macroscopic bulk fluid motion), Radiation (electromagnetic waves requiring no medium)",
            "Definition of Heat Current (H): Rate of flow of thermal energy through a cross-section (H = dQ / dt, SI unit: Watt = J/s)",
            "Temperature Gradient: Rate of change of temperature with distance along heat flow direction (-dT/dx, SI unit: K/m)",
            "Fourier's Law of Heat Conduction: H = dQ / dt = - K A (dT / dx)",
            "Steady State Conduction through a uniform rod of length L and cross-section A with faces at T₁ and T₂ (T₁ > T₂): H = (K A (T₁ - T₂)) / L",
            "Coefficient of Thermal Conductivity (K): SI unit: W/(m·K) or J/(s·m·K), Dimensional formula: [MLT⁻³K⁻¹]",
            "Thermal conductors (Metals: Silver K ≈ 406 W/m·K, Copper K ≈ 385 W/m·K) due to abundant free conduction electrons",
            "Thermal insulators (Wood K ≈ 0.12 W/m·K, Glass K ≈ 0.8 W/m·K, Air K ≈ 0.026 W/m·K, Still air in fiberglass wool)",
            "Electrical Analogy to Ohm's Law: Heat Current H ↔ Electric Current I; Temperature Difference ΔT ↔ Potential Difference ΔV; Thermal Resistance R_th ↔ Electrical Resistance R",
            "Thermal Resistance Formula: R_th = L / (K A) (SI unit: K/W)",
            "H = ΔT / R_th",
            "Composite Slabs in Series: Equal heat current H; Equivalent thermal resistance R_eq = R₁ + R₂ = L₁/(K₁A) + L₂/(K₂A); Junction temperature T_j",
            "Composite Slabs in Parallel: Equal temperature difference; Equivalent thermal resistance 1/R_eq = 1/R₁ + 1/R₂"
        ],
        "key_concepts": [
            "Fourier's Law H = dQ/dt = K A (T₁ - T₂) / L",
            "Thermal Conductivity K (W/(m·K)) & Material Hierarchy",
            "Thermal Resistance Analogy R_th = L / (K A) (Ohm's Law Analogy H = ΔT / R_th)",
            "Composite Slabs in Series (R_eq = R₁ + R₂) & Junction Temperature Formula"
        ],
        "success_criteria": [
            "State Fourier's law of thermal conduction and deduce the dimensions of thermal conductivity K",
            "Calculate heat current and junction temperature in two-layer composite walls",
            "Apply the electrical analogy (R_th = L/KA) to solve complex series/parallel insulating barriers",
            "Explain why winter coats use trapped air pockets (feathers/wool) rather than dense solid materials"
        ],
        "chapter_notes": """# Thermal Conduction & Fourier's Law
## 1. Fourier's Law of Heat Conduction
In steady state, the rate of heat flow $H$ through a slab of cross-sectional area $A$ and thickness $L$ with end faces maintained at temperatures $T_1$ and $T_2$ ($T_1 > T_2$) is:
$$H = \\frac{dQ}{dt} = K A \\frac{T_1 - T_2}{L} = - K A \\frac{dT}{dx}$$
- $K$ is the **Coefficient of Thermal Conductivity**.
- **SI Unit**: $\\text{W}\\cdot\\text{m}^{-1}\\cdot\\text{K}^{-1} = \\text{J}\\cdot\\text{s}^{-1}\\cdot\\text{m}^{-1}\\cdot\\text{K}^{-1}$.
- **Dimensional Formula**: $[\\text{M}\\text{L}\\text{T}^{-3}\\text{K}^{-1}]$.

## 2. Thermal Resistance Analogy (Ohm's Law)
Thermal conduction is mathematically identical to electric conduction:
$$\\text{Heat Current } H = \\frac{T_1 - T_2}{R_{\\text{th}}} \\iff \\text{Electric Current } I = \\frac{V_1 - V_2}{R}$$
$$\\boxed{R_{\\text{th}} = \\frac{L}{K A} \\quad (\\text{Thermal Resistance, } [\\text{K/W}])}$$

## 3. Composite Slabs in Series
Two slabs of thicknesses $L_1, L_2$, areas $A$, and conductivities $K_1, K_2$ are placed in series:
- Since heat cannot accumulate at the junction in steady state:
  $$H = \\frac{T_1 - T_j}{R_1} = \\frac{T_j - T_2}{R_2} = \\frac{T_1 - T_2}{R_1 + R_2}$$
- **Junction Temperature ($T_j$)**:
  $$T_j = \\frac{\\frac{K_1}{L_1} T_1 + \\frac{K_2}{L_2} T_2}{\\frac{K_1}{L_1} + \\frac{K_2}{L_2}}$$
- **Equivalent Thermal Conductivity ($K_{\\text{eq}}$)** for two equal thickness slabs ($L_1 = L_2 = L$):
  $$R_{\\text{eq}} = \\frac{2L}{K_{\\text{eq}} A} = \\frac{L}{K_1 A} + \\frac{L}{K_2 A} \\implies \\boxed{K_{\\text{eq}} = \\frac{2 K_1 K_2}{K_1 + K_2} \\quad (\\text{Harmonic Mean})}$$
""",
        "worked_examples": [
            {
                "problem": "What is the temperature of the steel-copper junction in the steady state of the system shown below? Length of the steel rod = 15.0 cm, length of the copper rod = 10.0 cm, temperature of the furnace = 300°C, temperature of the other end = 0°C. The area of cross section of the steel rod is twice that of the copper rod (A_steel = 2 A_cu). Thermal conductivities: K_steel = 50.2 J/(s·m·K), K_cu = 385 J/(s·m·K). (NCERT Example 10.5)",
                "given": "L_steel = 15.0 cm = 0.15 m, L_cu = 10.0 cm = 0.10 m, T₁ = 300°C, T₂ = 0°C, A_steel = 2 A_cu, K_steel = 50.2 W/(m·K), K_cu = 385 W/(m·K)",
                "formula": "In steady state, Heat Current H_steel = H_cu => (K_steel · A_steel · (T₁ - T_j)) / L_steel = (K_cu · A_cu · (T_j - T₂)) / L_cu",
                "substitution": "[ 50.2 × (2 A_cu) × (300 - T_j) ] / 0.15 = [ 385 × A_cu × (T_j - 0) ] / 0.10",
                "calculation": "(100.4 / 0.15) · (300 - T_j) = (385 / 0.10) · T_j => 669.33 · (300 - T_j) = 3850 · T_j => 200,800 - 669.33 T_j = 3850 T_j => 4519.33 T_j = 200,800 => T_j = 200,800 / 4519.33 = 44.4°C",
                "finalAnswer": "Junction temperature T_j = 44.4°C",
                "unit": "°C"
            }
        ],
        "common_misconceptions": [
            "Misconception: A metal chair feels colder than a wooden table at room temperature because the metal is at a lower temperature. Reality: Both are at the EXACT same room temperature (say 20°C). The metal feels colder because its thermal conductivity K is hundreds of times higher, drawing heat away from your 37°C finger much faster!"
        ],
        "concept_questions": [
            {
                "question": "Two slabs of identical dimensions are joined in series. Slab 1 has conductivity K and Slab 2 has conductivity 3K. What is the equivalent thermal conductivity of the combination?",
                "options": [
                    "1.5 K (Harmonic mean combination)",
                    "2.0 K (Arithmetic mean)",
                    "0.75 K",
                    "4.0 K"
                ],
                "correctAnswer": "1.5 K (Harmonic mean combination)",
                "explanation": "For equal thickness slabs in series, K_eq is the harmonic mean: K_eq = (2 K₁ K₂) / (K₁ + K₂) = (2 × K × 3K) / (K + 3K) = (6 K²) / (4 K) = 1.5 K.",
                "hint": "Recall the formula K_eq = 2K₁K₂ / (K₁ + K₂) for series slabs of equal thickness.",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Thermal Conduction & Composite Junction",
                "diagram_type": "image",
                "diagram_title": "Fourier Heat Flow & Series Slab Electrical Analogy Circuit",
                "why_needed": "Visualizes temperature gradient slope and junction temperature calculation",
                "timing_and_cue": "Stage 4 when solving NCERT Example 10.5",
                "what_to_explain": "Why temperature drops faster through poor conductors (steeper gradient)",
                "image_search_query": "thermal conduction composite slab junction temperature diagram physics",
                "svg": mod4_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Heat Conduction",
                    "diagram_type": "image",
                    "image_search_query": "thermal resistance series slabs conduction diagram",
                    "svg": mod4_svg
                }
            ]
        },
        "ai_system_prompt_context": "SOCRATIC TIP: Use the electrical Ohm's law analogy (H = ΔT / R_th) on the chalkboard. Students who find conduction difficult immediately grasp it once mapped to V = I R."
    })

    # -------------------------------------------------------------
    # MODULE 5: Thermal Convection & Atmospheric Fluid Circulation
    # Order Index: 62
    # -------------------------------------------------------------
    mod5_svg = sb2.build_stress_strain_curve_svg(
        material="Thermal Convection",
        title="Natural & Forced Convection: Sea Breeze & Land Breeze",
        caption="Buoyancy-driven circulation: Hot fluid expands, density drops, and rises, replaced by cooler fluid"
    )

    modules.append({
        "order_index": 62,
        "title": "Thermal Convection, Buoyancy-Driven Fluid Loops & Atmospheric Circulations",
        "description": "Mechanism of thermal convection in fluids: macroscopic mass motion, natural (free) convection driven by gravity and thermal expansion density gradients vs forced convection driven by mechanical pumps/blowers, Rayleigh-Bénard cells, human circulatory blood cooling system, and planetary meteorological phenomena: diurnal coastal sea breezes and land breezes, and trade wind circulation.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Convection definition: Heat transfer accompanied by the actual macroscopic physical motion of heated fluid matter",
            "Gravity prerequisite for natural convection: Without gravity (e.g., in orbit inside ISS), buoyant forces are zero and natural convection cannot occur (a candle flame in zero-g is spherical and smothers in its own CO₂)",
            "Mechanism of Natural Convection: Fluid at base heats up, expands thermally, density decreases, and rises due to buoyant force; colder, denser fluid from top sinks to replace it, establishing a closed convection loop",
            "Forced Convection: Fluid is forced to circulate by an external mechanical pump, fan, or blower (e.g., car radiator cooling system, human heart pumping blood to skin for thermal regulation, air conditioners)",
            "Sea Breeze (Daytime phenomenon): Land has lower specific heat capacity than sea water; land heats up faster under sunshine; hot air over land rises, creating low pressure; cool air from sea blows inland as Sea Breeze",
            "Land Breeze (Nighttime phenomenon): Land cools down faster than water at night due to low specific heat; water remains warmer; air over sea rises; cool air blows from land to sea as Land Breeze",
            "Trade Winds: Intense equatorial heating causes air to rise, flowing towards poles at high altitudes and returning towards equator at surface, deflected westward by Earth's rotation (Coriolis effect)"
        ],
        "key_concepts": [
            "Natural Convection Driven by Gravity and Density Differences (Δρ)",
            "Forced Convection Driven by Mechanical Pumps/Blowers",
            "Sea Breeze (Daytime Sea to Land) vs Land Breeze (Nighttime Land to Sea)",
            "Why Candle Flames in Zero-G are Spherical and Dim (Zero Natural Convection)"
        ],
        "success_criteria": [
            "Differentiate between natural and forced convection with practical engineering examples",
            "Explain why natural convection is impossible in an orbiting spacecraft under weightlessness",
            "Explain the physical origin of diurnal sea breezes and land breezes using specific heat differences",
            "Trace the convection loop inside a boiling water kettle"
        ],
        "chapter_notes": """# Thermal Convection & Atmospheric Fluid Circulation
## 1. Natural vs Forced Convection
- **Natural (Free) Convection**: Fluid motion is induced purely by density differences caused by temperature gradients in the presence of a gravitational field:
  $$\\text{Bottom fluid heated} \\implies \\rho \\text{ decreases} \\implies \\text{Upward Buoyancy Force } F_b = V (\\rho_{\\text{cold}} - \\rho_{\\text{hot}}) g$$
  - In zero-gravity, natural convection ceases completely.
- **Forced Convection**: Fluid is driven by external mechanical means (fans, blowers, or pumps):
  - Automobile cooling: Water pump circulates water around engine cylinders and through radiator fins.
  - Human body: The heart pumps warm blood from core organs to skin capillaries for evaporative and radiative cooling.

## 2. Diurnal Coastal Winds (Sea Breeze & Land Breeze)
Specific heat of water ($s_{\\text{water}} = 4186\\text{ J/kg}\\cdot\\text{K}$) is roughly $5\\times$ higher than dry soil/sand ($s_{\\text{soil}} \\approx 800\\text{ J/kg}\\cdot\\text{K}$).
1. **Sea Breeze (Daytime)**:
   - Sunlight heats land much faster than the sea.
   - Warm air over land expands, rises, creating localized low pressure.
   - Dense, cool air over the sea moves inland: **Sea Breeze**.
2. **Land Breeze (Nighttime)**:
   - At night, land cools rapidly by radiation, while the sea retains heat.
   - Air over the sea is warmer and rises.
   - Cool air from the land blows out to sea: **Land Breeze**.
""",
        "worked_examples": [
            {
                "problem": "Explain qualitatively why a domestic room heater or radiator is always placed on the floor near the ground, while an air conditioner is installed high up near the ceiling.",
                "given": "Warm air is less dense and rises; cold air is denser and sinks.",
                "formula": "Natural Convection Loop formation: Upward movement of hot fluid, downward movement of cold fluid.",
                "substitution": "Heater at floor heats bottom air => hot air rises, displacing top cold air downward to heater, circulating warmth throughout room. AC near ceiling cools top air => cold dense air sinks to floor, creating uniform cooling loop.",
                "calculation": "If heater were on ceiling: hot air stays trapped at ceiling, floor stays freezing. If AC were on floor: cold air stays trapped at floor, upper room stays hot.",
                "finalAnswer": "Heater on floor and AC on ceiling maximize complete natural convection loops across the entire room volume.",
                "unit": "Qualitative reasoning"
            }
        ],
        "common_misconceptions": [
            "Misconception: Natural convection can happen in deep space or orbit. Reality: Without gravity (g = 0), buoyant force F_b = V Δρ g = 0! Density differences cannot create upward motion without gravity."
        ],
        "concept_questions": [
            {
                "question": "What happens to a candle flame inside the International Space Station in microgravity?",
                "options": [
                    "The flame becomes perfectly spherical and burns very dimly, eventually suffocating in its own combustion products (CO₂ and water vapor)",
                    "The flame flickers upward with greater brightness",
                    "The candle explodes immediately",
                    "The flame turns into a flat sheet"
                ],
                "correctAnswer": "The flame becomes perfectly spherical and burns very dimly, eventually suffocating in its own combustion products (CO₂ and water vapor)",
                "explanation": "On Earth, buoyant forces drive hot exhaust gases upward, drawing fresh oxygen in from below to sustain the teardrop flame. In zero-g, natural convection ceases; oxygen can reach the wick only via slow molecular diffusion, creating a faint, spherical, slow-burning dome of fire.",
                "hint": "Does hot air rise in the absence of gravity?",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Thermal Convection & Coastal Wind Circulation",
                "diagram_type": "image",
                "diagram_title": "Daytime Sea Breeze & Nighttime Land Breeze Convection Loops",
                "why_needed": "Visualizes cyclic circulation of warm and cool air over land and ocean",
                "timing_and_cue": "Stage 3 when explaining maritime weather",
                "what_to_explain": "Differential heating rates due to water's high specific heat capacity",
                "image_search_query": "sea breeze land breeze convection circulation diagram physics",
                "svg": mod5_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Convection Currents",
                    "diagram_type": "image",
                    "image_search_query": "convection current liquid heating kettle diagram",
                    "svg": mod5_svg
                }
            ]
        },
        "ai_system_prompt_context": "TEACHING TIP: Connect sea breeze and land breeze directly back to Module 59's core concept: water's huge specific heat capacity compared to sand."
    })

    # -------------------------------------------------------------
    # MODULE 6: Thermal Radiation, Stefan-Boltzmann, Wien & Newton's Cooling
    # Order Index: 63
    # -------------------------------------------------------------
    mod6_svg = sb2.build_stress_strain_curve_svg(
        material="Thermal Radiation",
        title="Thermal Radiation: Stefan's Law, Wien's Law & Newton's Cooling",
        caption="E = e σ A T⁴ | Wien's Law: λ_max T = b = 2.898 × 10⁻³ m·K | Newton's Cooling: dT/dt = -k(T - T₀)"
    )

    modules.append({
        "order_index": 63,
        "title": "Thermal Radiation, Blackbody Radiation, Stefan-Boltzmann Law, Wien's Law & Newton's Law of Cooling",
        "description": "Electromagnetic nature of thermal radiation: emission of infrared photons by all bodies at T > 0 K, ideal blackbody absorption and emission, Prevost's theory of heat exchanges, Kirchhoff's law of radiation, Stefan-Boltzmann law (E = e σ A T⁴), net radiative exchange with surroundings (E_net = e σ A (T⁴ - T₀⁴)), Wien's Displacement Law (λ_max T = b = 2.898 × 10⁻³ m·K), derivation of Sir Isaac Newton's Law of Cooling for small temperature excesses (dT/dt = -k (T - T₀)), and experimental cooling curves.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Thermal Radiation: Electromagnetic radiation emitted by all matter having temperature above absolute zero (0 K)",
            "Prevost's Theory of Heat Exchanges: All bodies constantly radiate energy to surroundings and absorb energy from surroundings; thermal equilibrium implies rate of emission = rate of absorption",
            "Blackbody definition: Ideal body that absorbs 100% of all incident electromagnetic radiation of all wavelengths falling on it (absorptivity a = 1)",
            "Fery's Blackbody: Double-walled hollow spherical enclosure with a tiny pinhole aperture and pointed conical projection",
            "Kirchhoff's Law of Radiation: At any temperature, the ratio of emissive power to absorptive power is constant for all bodies and equal to the emissive power of a perfect blackbody (e / a = E_b; Good absorbers are good emitters)",
            "Stefan-Boltzmann Law (1879, 1884): Total radiant energy emitted per second by a blackbody of area A at absolute temperature T: E = σ A T⁴",
            "Stefan-Boltzmann constant: σ = 5.670 × 10⁻⁸ W/(m²·K⁴)",
            "Real non-blackbody radiation: E = e σ A T⁴ (where emissivity 0 < e < 1)",
            "Net radiative heat loss in surroundings at temperature T₀: E_net = e σ A (T⁴ - T₀⁴)",
            "Wien's Displacement Law (1893): Wavelength of peak spectral emission λ_max is inversely proportional to absolute temperature T: λ_max · T = b = 2.898 × 10⁻³ m·K",
            "Astrophysical applications: Determining surface temperatures of stars (Sun: T ≈ 5778 K => λ_max ≈ 500 nm green-yellow light)",
            "Sir Isaac Newton's Law of Cooling: Rate of loss of heat of a hot body is directly proportional to temperature difference between body and surroundings: -dQ/dt = k' (T - T₀)",
            "Derivation from Stefan's law: (T⁴ - T₀⁴) ≈ 4 T₀³ (T - T₀) for small ΔT = T - T₀ << T₀",
            "Differential equation for temperature: dT / dt = - k (T - T₀) => ln(T - T₀) = - k t + C => T(t) = T₀ + (T_initial - T₀) e^{-kt}"
        ],
        "key_concepts": [
            "Stefan-Boltzmann Law E = e σ A T⁴ (σ = 5.67 × 10⁻⁸ W/(m²·K⁴))",
            "Net Radiative Exchange E_net = e σ A (T⁴ - T₀⁴)",
            "Wien's Displacement Law λ_max · T = b = 2.898 × 10⁻³ m·K",
            "Newton's Law of Cooling dT/dt = -k (T - T₀) & Exponential Cooling Profile"
        ],
        "success_criteria": [
            "State the Stefan-Boltzmann law and Wien's displacement law with numerical constants and SI units",
            "Derive Newton's law of cooling from Stefan's law for small temperature excesses (T - T₀ << T₀)",
            "Estimate stellar surface temperatures using Wien's displacement constant and peak emission wavelength",
            "Solve cooling curve numericals using both exact integration and average temperature approximations"
        ],
        "chapter_notes": """# Thermal Radiation, Blackbody Laws & Newton's Law of Cooling
## 1. Stefan-Boltzmann Law
Total energy radiated per second by a blackbody of surface area $A$ at absolute temperature $T$:
$$E = \\sigma A T^4$$
where $\\sigma = 5.67037 \\times 10^{-8}\\text{ W}\\cdot\\text{m}^{-2}\\cdot\\text{K}^{-4}$ is **Stefan's Constant**.
For a real body of emissivity $e$ ($0 \\le e \\le 1$):
$$E = e \\sigma A T^4$$
If placed in an enclosure at ambient temperature $T_0$:
$$\\text{Net Rate of Heat Loss } E_{\\text{net}} = \\frac{dQ}{dt} = e \\sigma A (T^4 - T_0^4)$$

## 2. Wien's Displacement Law
As a body heats up, its radiation peak shifts to shorter wavelengths (higher frequencies):
$$\\lambda_{\\text{max}} T = b = 2.898 \\times 10^{-3}\\text{ m}\\cdot\\text{K} \\quad (\\text{Wien's Constant})$$
- Sun: $\\lambda_{\\text{max}} \\approx 500\\text{ nm} \\implies T_{\\text{sun}} = \\frac{2.898 \\times 10^{-3}}{500 \\times 10^{-9}} \\approx 5800\\text{ K}$.
- Human Body ($T \\approx 310\\text{ K}$): $\\lambda_{\\text{max}} \\approx 9.35\\,\\mu\\text{m}$ (Thermal Infrared).

## 3. Derivation: Newton's Law of Cooling
For a small temperature excess $\\Delta T = T - T_0 \\ll T_0$:
$$T = T_0 + \\Delta T = T_0 \\left(1 + \\frac{\\Delta T}{T_0}\\right)$$
Using binomial expansion:
$$T^4 = T_0^4 \\left(1 + \\frac{\\Delta T}{T_0}\\right)^4 \\approx T_0^4 \\left(1 + 4\\frac{\\Delta T}{T_0}\\right) = T_0^4 + 4 T_0^3 \\Delta T$$
$$T^4 - T_0^4 \\approx 4 T_0^3 (T - T_0)$$
Substituting into Stefan's law:
$$\\frac{dQ}{dt} = e \\sigma A \\cdot 4 T_0^3 (T - T_0)$$
Since $dQ = m s dT$:
$$m s \\frac{dT}{dt} = - 4 e \\sigma A T_0^3 (T - T_0)$$
$$\\boxed{\\frac{dT}{dt} = - k (T - T_0)} \\quad \\text{where } k = \\frac{4 e \\sigma A T_0^3}{m s}$$
Integrating gives exponential decay:
$$T(t) = T_0 + (T_{\\text{initial}} - T_0) e^{-kt}$$
""",
        "worked_examples": [
            {
                "problem": "A pan filled with hot food cools from 94°C to 86°C in 2 minutes when the room temperature is at 20°C. How long will it take to cool from 70°C to 66°C? (NCERT Example 10.8)",
                "given": "Stage 1: T_initial = 94°C, T_final = 86°C, time t₁ = 2 min, T₀ = 20°C. Stage 2: T_initial = 70°C, T_final = 66°C, find t₂.",
                "formula": "Newton's Cooling Approximation: (T₁ - T₂) / t = k · [ (T₁ + T₂) / 2 - T₀ ]",
                "substitution": "Stage 1: (94 - 86) / 2 = k · [ (94 + 86) / 2 - 20 ] => 8 / 2 = k · [ 90 - 20 ] => 4 = k · 70 => k = 4 / 70 = 2 / 35 min⁻¹. Stage 2: (70 - 66) / t₂ = k · [ (70 + 66) / 2 - 20 ] => 4 / t₂ = (4 / 70) · [ 68 - 20 ]",
                "calculation": "4 / t₂ = (4 / 70) × 48 => 1 / t₂ = 48 / 70 => t₂ = 70 / 48 = 1.458 minutes = 1 min 28 seconds",
                "finalAnswer": "Time taken to cool from 70°C to 66°C = 1.46 minutes (approx. 1 min 28 s)",
                "unit": "minutes"
            }
        ],
        "common_misconceptions": [
            "Misconception: Newton's law of cooling applies at any temperature difference. Reality: Newton's law of cooling is strictly valid ONLY for small temperature differences (T - T₀ <= 30°C). For large temperature differences, the full non-linear Stefan T⁴ law must be used."
        ],
        "concept_questions": [
            {
                "question": "A spherical star of radius R has surface temperature T. A second star has radius 2R and surface temperature 2T. What is the ratio of their total radiated powers P₁ : P₂?",
                "options": [
                    "1 : 64",
                    "1 : 16",
                    "1 : 32",
                    "1 : 8"
                ],
                "correctAnswer": "1 : 64",
                "explanation": "From the Stefan-Boltzmann law, radiated power is P = σ A T⁴ = σ (4π R²) T⁴ ∝ R² T⁴. For Star 2: P₂ ∝ (2R)² (2T)⁴ = 4 R² × 16 T⁴ = 64 R² T⁴ = 64 P₁. Therefore, P₁ : P₂ = 1 : 64.",
                "hint": "Calculate the power dependence: P ∝ Area × T⁴ = R² · T⁴.",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Thermal Radiation & Blackbody Spectra",
                "diagram_type": "image",
                "diagram_title": "Blackbody Spectral Radiation Curves & Wien Peak Shift",
                "why_needed": "Visualizes Planck radiation curves, T⁴ Stefan area, and Wien displacement peak",
                "timing_and_cue": "Stage 2 during blackbody radiation formulation",
                "what_to_explain": "How higher temperature increases total radiated area (T⁴) and shifts peak left (Wien)",
                "image_search_query": "blackbody radiation spectrum wien displacement law planck curve diagram",
                "svg": mod6_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Blackbody Radiation",
                    "diagram_type": "image",
                    "image_search_query": "stefan boltzmann wien law blackbody curves diagram",
                    "svg": mod6_svg
                }
            ]
        },
        "ai_system_prompt_context": "BOARD TOPPER TIP: NCERT Example 10.8 (cooling of the pan) is a classic 3-mark CBSE question. Solve it using the average temperature method on the chalkboard."
    })

    # -------------------------------------------------------------
    # MODULE 7: Comprehensive NCERT Textbook Exercises 10.1 to 10.22 Solver
    # Order Index: 64
    # -------------------------------------------------------------
    mod7_svg = sb2.build_stress_strain_curve_svg(
        material="NCERT 10 Suite",
        title="NCERT Exercises 10.1 to 10.22 Full Solutions Suite",
        caption="Step-by-step solutions for Thermometry, Expansion, Calorimetry, Conduction, and Cooling"
    )

    modules.append({
        "order_index": 64,
        "title": "Comprehensive NCERT Textbook Exercises 10.1 to 10.22 Detailed Numerical Solutions Suite",
        "description": "Exhaustive step-by-step solutions to all end-of-chapter NCERT exercise questions (10.1 to 10.22) on Thermal Properties of Matter, covering neon/CO₂ triple points, Celsius/Fahrenheit scale coincidences, steel measuring tapes calibrated at 27°C, drilled holes in copper sheets, thermal stress in brass-steel bars, specific heat calorimetry of alloys, and Newton's cooling curve equations.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "NCERT Exercise 10.1: Triple points of neon (24.57 K) and carbon dioxide (216.55 K) on Celsius and Fahrenheit scales",
            "NCERT Exercise 10.2: Two absolute temperature scales A and B with defined triple points",
            "NCERT Exercise 10.3: Electrical resistance thermometer calibration at ice and steam points",
            "NCERT Exercise 10.4: Conceptual questions on triple point invariance and thermal equilibrium",
            "NCERT Exercise 10.5: Saturated vapor pressure measurements of helium and nitrogen",
            "NCERT Exercise 10.6: Steel measuring tape calibrated at 27°C measuring a rod on a hot summer day at 45°C",
            "NCERT Exercise 10.7: Large steel wheel to be fitted onto a shaft of slightly larger diameter by heating",
            "NCERT Exercise 10.8: Hole drilled in copper sheet at 27°C heated to 227°C",
            "NCERT Exercise 10.9: Brass wire of diameter 1 mm clamped between two rigid supports cooled from 100°C to 20°C",
            "NCERT Exercise 10.10: Brass rod and steel rod joined in series under temperature change",
            "NCERT Exercises 10.11 to 10.22: Calorimeter ice melting, heat transfer through composite glass windows, and Newton's law of cooling"
        ],
        "key_concepts": [
            "Measuring Tape Calibration Errors (L_true = L_scale (1 + α ΔT))",
            "Shrink-Fitting Wheels on Shafts (Thermal Expansion Fit)",
            "Hole Expansion Invariance (Photographic Zoom Proof)",
            "Systematic Board Exam Layout: Given -> Formula -> Substitution -> Calculation -> Boxed Answer"
        ],
        "success_criteria": [
            "Solve thermal measuring tape calibration problems distinguishing true length from scale reading",
            "Determine the temperature required to expand metal collars for shrink-fitting onto shafts",
            "Calculate tension developed in clamped wires cooled through large temperature drops",
            "Master every authentic numerical pattern appearing in CBSE Class 11 final-term physics examination"
        ],
        "chapter_notes": """# NCERT Chapter 10: Complete Exercise Solutions Master Notes
## Summary of Master Equations:
1. **Temperature Scale**: $\\frac{T_C}{5} = \\frac{T_F - 32}{9} = \\frac{T_K - 273.15}{5}$
2. **Linear Expansion**: $\\Delta L = \\alpha_L L \\Delta T$
3. **Volume Expansion**: $\\Delta V = \\gamma V \\Delta T$ ($\\gamma = 3\\alpha$)
4. **Thermal Stress**: $\\sigma = Y \\alpha \\Delta T$, Force $F = Y A \\alpha \\Delta T$
5. **Specific Heat**: $Q = m s \\Delta T$
6. **Latent Heat**: $Q = m L$
7. **Calorimetry**: $\\sum Q_{\\text{lost}} = \\sum Q_{\\text{gained}}$
8. **Conduction (Fourier)**: $H = \\frac{dQ}{dt} = \\frac{K A (T_1 - T_2)}{L} = \\frac{\\Delta T}{R_{\\text{th}}}$
9. **Stefan-Boltzmann Law**: $E_{\\text{net}} = e \\sigma A (T^4 - T_0^4)$
10. **Wien's Law**: $\\lambda_{\\text{max}} T = 2.898 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$
11. **Newton's Cooling**: $\\frac{T_1 - T_2}{t} = k \\left( \\frac{T_1 + T_2}{2} - T_0 \\right)$
""",
        "worked_examples": [
            {
                "problem": "A steel tape 1 m long is correctly calibrated at 27.0°C. The length of a steel rod measured by this tape is found to be 63.0 cm on a hot day when the temperature is 45.0°C. What is the actual length of the steel rod on that day? What is the length of the same steel rod on a day when the temperature is 27.0°C? Take coefficient of linear expansion of steel = 1.20 × 10⁻⁵ K⁻¹. (NCERT Exercise 10.6)",
                "given": "Calibration temp T₀ = 27.0°C, Hot day temp T₁ = 45.0°C => ΔT = 18.0 K, Scale reading L_scale = 63.0 cm, α_steel = 1.20 × 10⁻⁵ K⁻¹",
                "formula": "At 45°C, each cm division on the tape has expanded: 1 division = 1 cm × (1 + α ΔT); Actual length L_actual(45°C) = L_scale × (1 + α ΔT); At 27°C, the rod shrinks: L_actual(27°C) = L_actual(45°C) / (1 + α ΔT) = L_scale = 63.0 cm",
                "substitution": "L_actual(45°C) = 63.0 cm × [ 1 + 1.20 × 10⁻⁵ × 18.0 ] = 63.0 × [ 1 + 2.16 × 10⁻⁴ ]",
                "calculation": "L_actual(45°C) = 63.0 × 1.000216 = 63.0136 cm",
                "finalAnswer": "Actual length of the steel rod at 45.0°C = 63.0136 cm (63.014 cm); Length of rod at 27.0°C = 63.0 cm",
                "unit": "cm"
            },
            {
                "problem": "A hole is drilled in a copper sheet. The diameter of the hole is 4.24 cm at 27.0°C. What is the change in the diameter of the hole when the sheet is heated to 227°C? Coefficient of linear expansion of copper = 1.70 × 10⁻⁵ K⁻¹. (NCERT Exercise 10.8)",
                "given": "Initial diameter d = 4.24 cm, Initial temp T₁ = 27.0°C, Final temp T₂ = 227°C => ΔT = 200 K, α_cu = 1.70 × 10⁻⁵ K⁻¹",
                "formula": "Δd = d · α_cu · ΔT",
                "substitution": "Δd = 4.24 cm × (1.70 × 10⁻⁵ K⁻¹) × 200 K",
                "calculation": "Δd = 4.24 × 3.40 × 10⁻³ = 1.4416 × 10⁻² cm = 0.0144 cm",
                "finalAnswer": "Change in diameter Δd = +0.0144 cm (Final diameter = 4.2544 cm)",
                "unit": "cm"
            }
        ],
        "common_misconceptions": [
            "Misconception: When measuring with an expanded tape, the reading is larger than true length. Reality: Since each marking on the tape has expanded, FEWER markings fit along the measured object. Therefore, the tape reading is smaller than actual length! L_true = L_reading (1 + α ΔT)."
        ],
        "concept_questions": [
            {
                "question": "At what temperature do the Celsius and Fahrenheit scales read the exact same numerical value?",
                "options": [
                    "-40° (-40°C = -40°F)",
                    "0°",
                    "+40°",
                    "-273°"
                ],
                "correctAnswer": "-40° (-40°C = -40°F)",
                "explanation": "Set T_C = T_F = x in the conversion formula: x / 5 = (x - 32) / 9 => 9x = 5x - 160 => 4x = -160 => x = -40. Thus -40°C is identically equal to -40°F.",
                "hint": "Set T_C = T_F = x in (T_C / 5) = (T_F - 32) / 9.",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "NCERT 10 Exercise Problem Solving Suite",
                "diagram_type": "image",
                "diagram_title": "Measuring Tape Calibration Error & Copper Hole Expansion",
                "why_needed": "Visualizes thermal expansion numerical setups on chalkboard",
                "timing_and_cue": "Stage 4 when solving Exercises 10.6 and 10.8",
                "what_to_explain": "Why expanded ruler divisions result in under-reading true length",
                "image_search_query": "thermal expansion steel tape error hole copper diagram physics",
                "svg": mod7_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "NCERT 10 Exercises",
                    "diagram_type": "image",
                    "image_search_query": "thermal expansion steel measuring tape diagram physics",
                    "svg": mod7_svg
                }
            ]
        },
        "ai_system_prompt_context": "CHALKBOARD MANDATE: Strictly follow the Trio Combo for all NCERT Chapter 10 exercise numericals. Highlight the tape calibration logic clearly in [ROUGH_WORK]."
    })

    return {
        "curriculum_id": CURRICULUM_ID,
        "title": "Chapter 10: Thermal Properties of Matter",
        "description": "Comprehensive CBSE Class 11 Physics Part 2 curriculum covering Temperature Scales, Thermal Expansion of Solids/Liquids/Gases, Anomalous Expansion of Water, Specific Heat Capacity, Calorimetry, Latent Heat, Phase Transitions, Conduction (Fourier's Law), Convection, Stefan-Boltzmann Law, Wien's Law, and Newton's Law of Cooling.",
        "category": "Physics",
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "difficulty_level": "advanced",
        "order_index": 10,
        "syllabus_term": SYLLABUS_TERM,
        "unit_name": UNIT,
        "weightage_marks": "Part of Unit VII-IX Group (20 Marks)",
        "notes_source_filename": "keph203.pdf",
        "modules": modules
    }
