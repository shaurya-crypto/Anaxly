"""
ch8_mechanical_properties_of_solids.py
CBSE Class 11 Physics - Chapter 8: Mechanical Properties of Solids
Part 2 (Final-Term Examination Syllabus, Unit VII: Properties of Bulk Matter)
Exhaustive, University-Prep & Board-Exam Topper Curriculum Decomposition
"""

import sys
import os
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

import svg_builder_physics11_pt2 as sb2

CURRICULUM_ID = "c11_phy_ch08_solids"
CLASS_LEVEL = "Class 11"
BOARD = "CBSE"
SUBJECT = "Physics"
UNIT = "Unit VII: Properties of Bulk Matter"
SYLLABUS_TERM = "Final-Term Examination"

def get_modules():
    modules = []

    # -------------------------------------------------------------
    # MODULE 1: Elastic Behaviour, Restoring Forces & Types of Stress/Strain
    # Order Index: 45
    # -------------------------------------------------------------
    mod1_svg = sb2.build_stress_strain_curve_svg(
        material="Mild Steel",
        title="Microscopic Origin of Elasticity & Intermolecular Potential",
        caption="Balance of attractive and repulsive interatomic forces modeled by microscopic spring lattice"
    )

    modules.append({
        "order_index": 45,
        "title": "Elastic Behaviour of Matter, Interatomic Forces & Fundamental Types of Stress and Strain",
        "description": "Exploration of elasticity and plasticity at microscopic atomic lattice scales, restoring force mechanisms, formal definitions of deforming force, and rigorous formulation of normal stress (tensile and compressive), tangential/shearing stress, and hydraulic/volumetric stress with corresponding strains.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Rigid body idealization vs real deformable bodies in nature",
            "Microscopic spring-ball lattice model of solid crystal structure",
            "Interatomic potential energy curve U(r) and equilibrium intermolecular separation r₀",
            "Elasticity: Property of a body by virtue of which it regains its original shape and size when deforming forces are removed",
            "Plasticity: Inability of a material to regain original dimensions leading to permanent deformation (e.g., putty, clay, paraffin wax)",
            "Definition of Stress: Internal restoring force per unit area acting on the deformed body (σ = F_int / A, SI Unit: N/m² or Pa, Dimensions: [ML⁻¹T⁻²])",
            "Tensile Stress: Restoring force per unit area when deforming force causes an elongation in length (σ_tensile = F_perp / A)",
            "Compressive Stress: Restoring force per unit area when deforming force causes a contraction in length",
            "Shearing / Tangential Stress: Tangential deforming force per unit area applied parallel to the surface causing angular deformation (σ_shear = F_parallel / A)",
            "Hydraulic / Volumetric Stress: Uniform inward normal force applied by a fluid causing uniform reduction in volume without change in geometric shape (σ_vol = -ΔP)",
            "Definition of Strain: Fractional change in dimension (dimensionless, unitless scalar): Strain = Δdimension / original_dimension",
            "Longitudinal Strain: Change in length per unit original length (ε_long = ΔL / L)",
            "Shearing Strain: Lateral displacement Δx per unit perpendicular distance L, measuring shear angle θ (tan θ ≈ θ = Δx / L)",
            "Volume Strain: Fractional change in volume (ε_vol = ΔV / V)"
        ],
        "key_concepts": [
            "Microscopic Lattice Spring Model & Equilibrium Separation r₀",
            "Tensile, Compressive, Tangential & Hydraulic Stress (σ = F/A)",
            "Longitudinal, Shearing & Volume Strains (Dimensionless Ratio)",
            "Restoring Force vs External Deforming Force Equivalence in Static Equilibrium"
        ],
        "success_criteria": [
            "Distinguish between elastic and plastic behavior with microscopic physical mechanisms",
            "Compute tensile, shearing, and hydraulic stress with precise SI units (Pascals)",
            "Calculate longitudinal strain, shear angle θ in radians, and fractional volume strain",
            "Deduce dimensional formula [ML⁻¹T⁻²] for stress and verify that strain is strictly dimensionless"
        ],
        "chapter_notes": """# Mechanical Properties of Solids: Elasticity & Stress-Strain Foundations
## 1. Microscopic Origin of Elasticity
In a crystalline solid, constituent atoms or molecules are held in equilibrium lattice positions by mutual electrostatic forces. When the solid is in un-deformed equilibrium, the interatomic separation is $r_0$ ($\approx 10^{-10}\\text{ m} = 1\\text{ Å}$), where potential energy $U(r)$ is minimum and net interatomic force is zero:
$$F = -\\frac{dU}{dr} = 0 \\quad \\text{at } r = r_0$$

When an external deforming force displaces atoms:
- If $r > r_0$ (stretched): Attractive interatomic forces pull atoms back.
- If $r < r_0$ (compressed): Strong repulsive electronic shell forces push atoms apart.
Thus, atoms behave as point masses connected by microscopic elastic springs.

## 2. Quantitative Classification of Stress
Stress is defined as the internal restoring force developed per unit area of the deformed cross-section:
$$\\text{Stress } \\sigma = \\frac{F_{\\text{restoring}}}{A} = \\frac{F_{\\text{external}}}{A} \\quad \\text{(in static mechanical equilibrium)}$$
- **SI Unit**: $\\text{N}\\cdot\\text{m}^{-2}$ or Pascal ($\\text{Pa}$)
- **Dimensional Formula**: $[\\text{M}\\text{L}^{-1}\\text{T}^{-2}]$

### Types of Stress:
1. **Normal Stress**: Applied perpendicular to cross-section:
   - **Tensile Stress**: Wire pulled outward, length increases ($+ \\Delta L$).
   - **Compressive Stress**: Column compressed inward, length decreases ($- \\Delta L$).
2. **Tangential / Shearing Stress**: Applied parallel to surface:
   $$\\sigma_{\\text{shear}} = \\frac{F_{\\parallel}}{A}$$
   Produces a change in shape at constant volume.
3. **Hydraulic Stress**: Solid immersed in fluid under uniform pressure $P$:
   $$\\sigma_{\\text{hydraulic}} = \\Delta P$$
   Causes fractional reduction in volume at constant shape.

## 3. Quantitative Classification of Strain
Strain measures relative geometric deformation:
$$\\text{Strain } \\varepsilon = \\frac{\\text{Change in Dimension}}{\\text{Original Dimension}} \\quad (\\text{Dimensionless, } [\\text{M}^0\\text{L}^0\\text{T}^0])$$

1. **Longitudinal Strain**:
   $$\\varepsilon_{\\text{long}} = \\frac{\\Delta L}{L}$$
2. **Shearing Strain**:
   Relative displacement $\\Delta x$ of parallel planes separated by height $L$:
   $$\\theta \\approx \\tan \\theta = \\frac{\\Delta x}{L} \\quad (\\text{in radians})$$
3. **Volume Strain**:
   $$\\varepsilon_{\\text{vol}} = \\frac{\\Delta V}{V}$$
""",
        "worked_examples": [
            {
                "problem": "A structural steel rod has a radius of 10 mm and a length of 2.0 m. A 100 kN force stretches it along its length. Calculate (a) the tensile stress, and (b) the percentage elongation if Young's modulus of steel is 2.0 × 10¹¹ N/m².",
                "given": "Radius r = 10 mm = 1.0 × 10⁻² m, Length L = 2.0 m, Tensile force F = 100 kN = 1.0 × 10⁵ N, Y = 2.0 × 10¹¹ N/m²",
                "formula": "Area A = π r²; Stress σ = F / A; Elongation ΔL = (F · L) / (A · Y); % Elongation = (ΔL / L) × 100",
                "substitution": "A = π × (1.0 × 10⁻²)² = 3.1416 × 10⁻⁴ m²; σ = (1.0 × 10⁵ N) / (3.1416 × 10⁻⁴ m²); ΔL = (1.0 × 10⁵ × 2.0) / (3.1416 × 10⁻⁴ × 2.0 × 10¹¹)",
                "calculation": "σ = 3.183 × 10⁸ N/m²; ΔL = 2.0 × 10⁵ / (6.2832 × 10⁷) = 3.183 × 10⁻³ m = 3.18 mm; % Elongation = (3.183 × 10⁻³ / 2.0) × 100 = 0.159%",
                "finalAnswer": "Tensile stress = 3.18 × 10⁸ N/m², Elongation = 3.18 mm (0.16%)",
                "unit": "N/m² and mm"
            }
        ],
        "common_misconceptions": [
            "Misconception: Stress is identical to external pressure. Reality: Pressure is always normal compressive force per unit area applied externally by a fluid; stress is an internal directional restoring tensor developed within the solid that can be tensile, compressive, or shearing.",
            "Misconception: Strain has units of length or meters. Reality: Strain is a ratio of two lengths (or volumes) and is strictly dimensionless and unitless."
        ],
        "concept_questions": [
            {
                "question": "Why does a piece of rubber regain its shape after stretching, whereas a lump of wet clay remains permanently deformed?",
                "options": [
                    "Rubber has strong restoring intermolecular forces trying to recover equilibrium r₀; wet clay lacks restoring forces and experiences plastic sliding of molecular layers",
                    "Rubber has higher density than clay",
                    "Clay experiences higher gravitational attraction",
                    "Rubber possesses negative Young's modulus"
                ],
                "correctAnswer": "Rubber has strong restoring intermolecular forces trying to recover equilibrium r₀; wet clay lacks restoring forces and experiences plastic sliding of molecular layers",
                "explanation": "In rubber, polymer chains unfold under strain and possess an entropic and intermolecular restoring drive to recoil back to equilibrium configurations. Clay particles slide irreversibly over lubricating water films with zero restoring force, exhibiting pure plasticity.",
                "hint": "Think about internal restoring forces pulling molecules back to their original equilibrium separation r₀.",
                "blooms_level": "Understand"
            },
            {
                "question": "A cylindrical wire of radius r is stretched by a force F. If the radius is doubled to 2r under the exact same tensile force, how does the tensile stress change?",
                "options": [
                    "Stress becomes 1/4th of the initial value",
                    "Stress is halved",
                    "Stress remains unchanged",
                    "Stress increases by a factor of 4"
                ],
                "correctAnswer": "Stress becomes 1/4th of the initial value",
                "explanation": "Cross-sectional area A = π r². When radius doubles (2r), area quadruples: A' = π (2r)² = 4π r² = 4A. Since stress σ = F / A, σ' = F / (4A) = σ / 4.",
                "hint": "Recall that stress is inversely proportional to cross-sectional area A = π r².",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Microscopic Interatomic Potential & Elastic Restoration",
                "diagram_type": "image",
                "diagram_title": "Interatomic Force Curve & Crystal Spring Lattice",
                "why_needed": "Visualizes why solids resist both stretching and compression like an atomic spring network",
                "timing_and_cue": "Stage 1 (Intuition) when introducing elasticity vs plasticity",
                "what_to_explain": "How atoms rest in potential wells at equilibrium r0 and create internal restoring stress",
                "image_search_query": "interatomic potential energy curve elasticity spring ball crystal model physics",
                
                "svg": mod1_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Interatomic Elastic Forces & Stress Types",
                    "diagram_type": "image",
                    "image_search_query": "types of stress tensile shearing hydraulic engineering diagrams",
                    "svg": mod1_svg
                }
            ]
        },
        "ai_system_prompt_context": "TEACHING SENIOR PHYSICS STUDENTS: Ground the distinction between stress and pressure immediately. Emphasize that stress is a tensor representing internal restoring resistance per unit area. Use the Trio Combo on chalkboard when calculating stress and strain."
    })

    # -------------------------------------------------------------
    # MODULE 2: Hooke's Law, Stress-Strain Characteristic Curve & Material Ductility
    # Order Index: 46
    # -------------------------------------------------------------
    mod2_svg = sb2.build_stress_strain_curve_svg(
        material="Structural Mild Steel",
        title="Complete Experimental Stress-Strain Curve for Tensile Wire",
        caption="Proportional Limit (P), Yield Strength (Y), Ultimate Tensile Strength (U), and Fracture Point (F)"
    )

    modules.append({
        "order_index": 46,
        "title": "Hooke's Law, Complete Experimental Stress-Strain Curve & Classification of Materials",
        "description": "Rigorous derivation and analysis of Robert Hooke's empirical law, modulus of elasticity as slope, full walkthrough of the experimental stress-strain tensile curve (proportional limit, elastic limit/yield point, plastic deformation, strain hardening, necking, and rupture), and classification into ductile materials, brittle materials, and elastomers.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Robert Hooke's Law (1676): 'Ut tensio, sic vis' - Within the elastic limit, stress is directly proportional to strain (σ ∝ ε)",
            "Modulus of Elasticity: Slope of linear stress-strain curve (E = σ / ε, SI unit: Pa)",
            "Experimental setup: Universal Testing Machine (UTM) tensile test of standardized metal specimen",
            "Region OA (Proportionality Region): Strict linearity, Hooke's law validity, slope yields Young's Modulus Y",
            "Point A (Proportional Limit): Highest stress level where stress remains proportional to strain",
            "Point B (Elastic Limit / Yield Point σ_y): Maximum stress a material can withstand without permanent deformation",
            "Yield Strength: Value of stress at point B (e.g., ~250 MPa for structural mild steel)",
            "Plastic Region BCDE: Small increase in stress produces large increase in strain; specimen does not return to O upon unloading",
            "Permanent Set: Residual strain (e.g., OP ≈ 0.2% offset) remaining after stress is reduced to zero from beyond elastic limit",
            "Point D (Ultimate Tensile Strength σ_u): Maximum nominal stress the material can sustain before cross-sectional necking begins",
            "Necking Phenomenon: Localized reduction in cross-sectional area where plastic instability accelerates",
            "Point E (Fracture / Rupture Point): Complete physical breakage of the specimen",
            "Classification: Ductile Materials (large plastic region between B and E, can be drawn into thin wires, e.g., copper, aluminium, mild steel)",
            "Classification: Brittle Materials (Point E lies very close to elastic limit B, shatters with negligible plastic strain, e.g., glass, cast iron, concrete)",
            "Classification: Elastomers (substances that can be stretched to enormous strains > 100% without breaking, non-linear stress-strain curve, lack well-defined plastic region, e.g., vulcanized rubber, tissue of aorta)"
        ],
        "key_concepts": [
            "Hooke's Law Validity Range (Strictly within Proportional Limit OA)",
            "Elastic Limit vs Proportional Limit Distinction",
            "Yield Point σ_y, Permanent Set & Plastic Flow",
            "Ultimate Tensile Strength (UTS) & Localized Necking",
            "Ductile vs Brittle vs Elastomer Stress-Strain Characterization"
        ],
        "success_criteria": [
            "Draw and label the complete stress-strain curve with points O, A, B, C, D, and E",
            "Explain the physical significance of the yield point, permanent set, and ultimate tensile strength",
            "Differentiate ductile, brittle, and elastomeric materials from their characteristic curve profiles",
            "Calculate Young's modulus from the slope of the initial linear proportional region"
        ],
        "chapter_notes": """# Hooke's Law & The Universal Stress-Strain Characteristic Curve
## 1. Hooke's Law Formulation
In 1676, Robert Hooke discovered that for small deformations:
$$\\text{Stress} \\propto \\text{Strain} \\implies \\frac{\\text{Stress}}{\\text{Strain}} = E \\quad (\\text{Modulus of Elasticity})$$
The modulus of elasticity $E$ depends purely on the nature of the material and temperature, independent of dimensions.

## 2. Walkthrough of the Stress-Strain Curve (Mild Steel)
1. **Region OA (Linear Elastic Region)**:
   - Stress $\\sigma$ is strictly proportional to strain $\\varepsilon$. Hooke's law is valid.
   - Point $A$ is the **Proportional Limit**. Slope $= \\frac{\\sigma}{\\varepsilon} = Y$.
2. **Region AB (Non-Linear Elastic Region)**:
   - Stress and strain are no longer directly proportional, but if the deforming force is removed at or before Point $B$, the body completely recovers its original dimensions along path $BO$.
   - Point $B$ is the **Elastic Limit** or **Yield Point**. The stress at $B$ is the **Yield Strength** $\\sigma_y$.
3. **Region BD (Plastic Flow & Strain Hardening)**:
   - If stressed beyond $B$, removal of load causes the material to unload along dashed line $OO'$, leaving a permanent deformation $OO'$ called **Permanent Set** (typically $0.1\\% - 0.2\\%$ strain).
   - Even without significant additional stress, the wire undergoes continuous irreversible plastic flow.
4. **Point D (Ultimate Tensile Strength $\\sigma_u$)**:
   - The peak of the nominal engineering stress curve. Represents the maximum load-bearing capacity.
5. **Region DE & Point E (Necking & Fracture)**:
   - A localized constriction ('neck') forms in the specimen. Local stress skyrockets while nominal force drops.
   - At Point $E$, the specimen fractures into two pieces (**Breaking Stress / Rupture**).

## 3. Material Classification by Stress-Strain Topology
- **Ductile Materials**: Plastic region $BE$ is very wide (e.g., Gold, Copper, Aluminium, Mild Steel). Can be drawn into thin wires or rolled into sheets.
- **Brittle Materials**: Plastic region $BE$ is negligible; fracture $E$ occurs immediately after elastic limit $B$ (e.g., Cast Iron, Ceramic, Glass, Chalk).
- **Elastomers**: Enormous elastic deformations (strains up to $500\\%$); non-linear curve, does not obey Hooke's law even at low stresses, negligible plastic region (e.g., Rubber, Aorta of human heart).
""",
        "worked_examples": [
            {
                "problem": "A steel wire of length 4.7 m and cross-sectional area 3.0 × 10⁻⁵ m² stretches by the same amount as a copper wire of length 3.5 m and cross-sectional area 4.0 × 10⁻⁵ m² under a given load. What is the ratio of the Young's modulus of steel to that of copper? (NCERT Example 8.1)",
                "given": "L_steel = 4.7 m, A_steel = 3.0 × 10⁻⁵ m², L_cu = 3.5 m, A_cu = 4.0 × 10⁻⁵ m², ΔL_steel = ΔL_cu = ΔL, Load F_steel = F_cu = F",
                "formula": "Young's modulus Y = (F · L) / (A · ΔL) => Y_steel / Y_cu = (L_steel / A_steel) / (L_cu / A_cu) = (L_steel · A_cu) / (L_cu · A_steel)",
                "substitution": "Y_steel / Y_cu = (4.7 m × 4.0 × 10⁻⁵ m²) / (3.5 m × 3.0 × 10⁻⁵ m²)",
                "calculation": "Numerator = 4.7 × 4.0 = 18.8; Denominator = 3.5 × 3.0 = 10.5; Ratio = 18.8 / 10.5 = 1.79",
                "finalAnswer": "Ratio of Young's modulus Y_steel / Y_cu = 1.79 : 1 (Steel is 1.79 times stiffer than copper)",
                "unit": "Dimensionless ratio"
            }
        ],
        "common_misconceptions": [
            "Misconception: Rubber is more elastic than steel because it stretches more. Reality: In physics, elasticity is measured by the magnitude of the restoring force per unit strain (Young's modulus Y). Since steel requires an enormous stress for a tiny strain compared to rubber (Y_steel ≈ 2 × 10¹¹ Pa vs Y_rubber ≈ 10⁶ Pa), steel is vastly MORE elastic than rubber!",
            "Misconception: Hooke's law applies all the way up to the elastic limit / yield point. Reality: Hooke's law holds strictly up to the proportional limit A; between A and B, the material is elastic but non-linear."
        ],
        "concept_questions": [
            {
                "question": "Two wires of identical length and initial radius are loaded with equal tensile weights. Wire A is made of structural steel (Y = 2 × 10¹¹ Pa) and Wire B is made of copper (Y = 1.1 × 10¹¹ Pa). Which wire undergoes greater elongation?",
                "options": [
                    "Wire B (Copper) undergoes approximately 1.8 times greater elongation than Wire A",
                    "Wire A (Steel) undergoes greater elongation because steel is stronger",
                    "Both elongate by the exact same amount because loads and dimensions are identical",
                    "Neither elongates because both remain within the linear Hooke's limit"
                ],
                "correctAnswer": "Wire B (Copper) undergoes approximately 1.8 times greater elongation than Wire A",
                "explanation": "Elongation ΔL = (F · L) / (A · Y). Since F, L, and A are identical for both, elongation is inversely proportional to Young's modulus (ΔL ∝ 1/Y). Since Y_cu < Y_steel, copper stretches more: ΔL_cu / ΔL_steel = Y_steel / Y_cu = 2.0 / 1.1 ≈ 1.82.",
                "hint": "Recall the formula ΔL = (F · L) / (A · Y) and check inverse proportionality with Y.",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Universal Stress-Strain Curve & Material Failure",
                "diagram_type": "image",
                "diagram_title": "Experimental Tensile Stress-Strain Curve",
                "why_needed": "Mastery of board exam question asking students to draw and explain all 5 characteristic zones",
                "timing_and_cue": "Stage 2 (Formulation) when walking through points O, A, B, C, D, E",
                "what_to_explain": "Proportional limit vs yield point, permanent set, UTS, and necking leading to fracture",
                "image_search_query": "stress strain curve mild steel proportional limit yield strength necking diagram",
                
                "svg": mod2_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Stress-Strain Characterization",
                    "diagram_type": "image",
                    "image_search_query": "stress strain curve mild steel labels",
                    "svg": mod2_svg
                }
            ]
        },
        "ai_system_prompt_context": "SOCRATIC EXAM TIP: Students frequently confuse 'stretchy' with 'elastic'. Debunk the rubber vs steel misconception immediately using the formal definition Y = Stress / Strain."
    })

    # -------------------------------------------------------------
    # MODULE 3: Three Elastic Moduli: Young's Modulus, Shear Modulus & Bulk Modulus
    # Order Index: 47
    # -------------------------------------------------------------
    mod3_svg = sb2.build_stress_strain_curve_svg(
        material="Elastic Moduli Comparison",
        title="Young's Modulus Y, Shear Modulus G & Bulk Modulus B",
        caption="Tensile elongation, angular shearing distortion θ, and volumetric hydrostatic compression"
    )

    modules.append({
        "order_index": 47,
        "title": "Comprehensive Moduli of Elasticity: Young's Modulus, Shear Modulus (Rigidity) & Bulk Modulus",
        "description": "Mathematical formulation and physical interpretation of the three moduli of elasticity: Young's modulus (longitudinal), Shear modulus of rigidity (shape change at constant volume), and Bulk modulus (hydrostatic volume change). Determination of Young's modulus using Searl's apparatus, compressibility as inverse of bulk modulus, and physical comparisons across solids, liquids, and gases.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "General definition of Elastic Modulus: Ratio of stress to strain within Hooke's proportional limit",
            "Young's Modulus (Y): Longitudinal tensile/compressive stress divided by longitudinal strain",
            "Formula for wire stretching: Y = (F / A) / (ΔL / L) = (F · L) / (π r² ΔL)",
            "Experimental measurement of Y: Searle's Apparatus (reference wire, experimental wire, micrometer screw, spirit level, and dead weights to eliminate thermal expansion errors)",
            "Shear Modulus of Rigidity (G or η): Shearing stress divided by shearing strain (angle of shear θ in radians)",
            "Formula for Shear Modulus: G = (F / A) / θ = (F · L) / (A · Δx)",
            "Relation between shear and extension: Pure shear is equivalent to equal tensile and compressive strains along mutually perpendicular 45° directions",
            "Bulk Modulus (B or K): Volumetric / hydraulic stress divided by fractional volume strain",
            "Formula for Bulk Modulus: B = -ΔP / (ΔV / V) = -V (ΔP / ΔV) (negative sign ensures B is positive since volume decreases under pressure)",
            "Compressibility (k): Reciprocal of Bulk Modulus: k = 1 / B = - (1 / V) (ΔV / ΔP) (SI unit: Pa⁻¹ or m²/N)",
            "Comparative moduli across states of matter: Solids have Y, G, and B; Liquids have only B (G = 0, cannot support shear); Gases have only B (highly compressible, B_gas << B_liquid << B_solid)"
        ],
        "key_concepts": [
            "Young's Modulus Y = (F L) / (A ΔL) for Longitudinal Elasticity",
            "Shear Modulus of Rigidity G = (F / A) / θ for Angular Torsion",
            "Bulk Modulus B = -V (ΔP / ΔV) for Hydrostatic Volume Compression",
            "Compressibility k = 1 / B & States of Matter Behavior (Liquids & Gases have G = 0)"
        ],
        "success_criteria": [
            "State formulas, SI units, and dimensional formulas for Y, G, and B",
            "Explain why liquids and gases possess zero shear modulus of rigidity",
            "Calculate Young's modulus from Searle's apparatus experimental parameters",
            "Determine the fractional volume change ΔV / V under deep ocean hydrostatic pressures"
        ],
        "chapter_notes": """# The Three Fundamental Moduli of Elasticity
## 1. Young's Modulus of Elasticity ($Y$)
Governs resistance to linear stretching or compression:
$$Y = \\frac{\\sigma_{\\text{long}}}{\\varepsilon_{\\text{long}}} = \\frac{F / A}{\\Delta L / L} = \\frac{F L}{A \\Delta L} = \\frac{M g L}{\\pi r^2 \\Delta L}$$
- For a perfectly rigid body: $\\Delta L = 0 \\implies Y = \\infty$.
- For liquids and gases: No fixed length under tension $\\implies Y = 0$.

## 2. Shear Modulus of Rigidity ($G$ or $\\eta$)
Governs resistance to shape distortion at constant volume:
$$G = \\frac{\\sigma_{\\text{shear}}}{\\varepsilon_{\\text{shear}}} = \\frac{F_{\\parallel} / A}{\\theta} = \\frac{F_{\\parallel} L}{A \\Delta x}$$
- For most metals: $G \\approx \\frac{1}{3} Y$.
- Fluids have zero static shear modulus ($G_{\\text{fluid}} = 0$) because fluid layers slide freely without restoring elasticity.

## 3. Bulk Modulus ($B$) & Compressibility ($k$)
Governs resistance to uniform hydrostatic compression:
$$B = -\\frac{\\Delta P}{\\Delta V / V} = -V \\frac{\\Delta P}{\\Delta V}$$
The negative sign is introduced because pressure increase ($\\Delta P > 0$) causes a volume reduction ($\\Delta V < 0$), ensuring $B > 0$.

### Compressibility ($k$):
$$k = \\frac{1}{B} = -\\frac{1}{V}\\frac{\\Delta V}{\\Delta P} \\quad (\\text{SI Unit: } \\text{Pa}^{-1} \\text{ or } \\text{m}^2/\\text{N})$$
- Order of Bulk Moduli: $B_{\\text{solid}} \\sim 10^{11}\\text{ Pa} > B_{\\text{liquid}} \\sim 10^9\\text{ Pa} > B_{\\text{gas}} \\sim 10^5\\text{ Pa}$.
- Order of Compressibility: $k_{\\text{gas}} \\sim 10^{-5}\\text{ Pa}^{-1} \\gg k_{\\text{liquid}} \\sim 10^{-9}\\text{ Pa}^{-1} \\gg k_{\\text{solid}} \\sim 10^{-11}\\text{ Pa}^{-1}$.
""",
        "worked_examples": [
            {
                "problem": "The average depth of the Indian Ocean is about 3000 m. Calculate the fractional compression, ΔV/V, of water at the bottom of the ocean, given that the bulk modulus of water is 2.2 × 10⁹ N/m² and density of water is 1000 kg/m³. (NCERT Example 8.4)",
                "given": "Depth h = 3000 m, Density ρ = 1000 kg/m³, g = 9.8 m/s², Bulk modulus of water B = 2.2 × 10⁹ N/m²",
                "formula": "Hydrostatic pressure increase ΔP = ρ · g · h; Bulk modulus B = ΔP / (|ΔV| / V) => |ΔV| / V = ΔP / B",
                "substitution": "ΔP = 1000 kg/m³ × 9.8 m/s² × 3000 m = 2.94 × 10⁷ N/m²; |ΔV| / V = (2.94 × 10⁷ N/m²) / (2.2 × 10⁹ N/m²)",
                "calculation": "Fractional compression = 2.94 / 220 = 0.01336 = 1.34%",
                "finalAnswer": "Fractional volume compression ΔV / V = 0.0134 (or 1.34%)",
                "unit": "Dimensionless ratio / percentage"
            }
        ],
        "common_misconceptions": [
            "Misconception: Water is completely incompressible. Reality: While water is highly incompressible in everyday mechanics compared to air, under deep ocean pressures (300 atmospheres), its volume compresses by roughly 1.34%, which is critical in oceanography and acoustics."
        ],
        "concept_questions": [
            {
                "question": "Why can shear stress and Young's modulus not be defined for an ideal fluid at rest?",
                "options": [
                    "A fluid cannot sustain static tangential or tensile forces; its layers slide continuously without developing internal elastic restoring shear stress",
                    "Fluids have infinite mass density",
                    "Fluids do not contain atoms",
                    "Bulk modulus of fluids is zero"
                ],
                "correctAnswer": "A fluid cannot sustain static tangential or tensile forces; its layers slide continuously without developing internal elastic restoring shear stress",
                "explanation": "By definition, a fluid in static equilibrium cannot sustain any non-zero tangential shearing stress. Any tangential force causes continuous flow (viscous deformation), not an elastic restoring strain. Hence G = 0 and Y = 0 for fluids.",
                "hint": "What happens when you apply a sideways shear force to the surface of water?",
                "blooms_level": "Understand"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Three Moduli of Elasticity",
                "diagram_type": "image",
                "diagram_title": "Comparative Deformation Modes: Tensile, Shear, and Bulk",
                "why_needed": "Visual contrast of length change vs angular distortion vs volumetric compression",
                "timing_and_cue": "Stage 1 when comparing Y, G, and B",
                "what_to_explain": "How each modulus corresponds to a distinct geometric deformation mode",
                "image_search_query": "elastic moduli youngs modulus shear modulus bulk modulus comparison diagram",
                "svg": mod3_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Moduli of Elasticity",
                    "diagram_type": "image",
                    "image_search_query": "searles apparatus youngs modulus experiment diagram",
                    "svg": mod3_svg
                }
            ]
        },
        "ai_system_prompt_context": "TEACHING TIP: Ensure students memorize the negative sign in Bulk Modulus B = -V (ΔP/ΔV) and understand its physical reason: volume always decreases as pressure increases."
    })

    # -------------------------------------------------------------
    # MODULE 4: Poisson's Ratio & Elastic Potential Energy of Stretched Wire
    # Order Index: 48
    # -------------------------------------------------------------
    mod4_svg = sb2.build_stress_strain_curve_svg(
        material="Stretched Wire",
        title="Poisson's Lateral Contraction & Elastic Energy Density",
        caption="Lateral strain / Longitudinal strain = σ | Energy density u = ½ × Stress × Strain = ½ Y ε²"
    )

    modules.append({
        "order_index": 48,
        "title": "Poisson's Ratio, Lateral Strain & Derivation of Elastic Potential Energy Density",
        "description": "Comprehensive study of lateral contraction under longitudinal stretching, mathematical definition of Poisson's ratio σ, theoretical (-1 to 0.5) and practical (0 to 0.5) limits, detailed integration of work done in stretching a wire, derivation of elastic potential energy U = 1/2 F ΔL, and volumetric elastic energy density u = 1/2 × stress × strain = 1/2 Y ε².",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Lateral Strain: Fractional change in transverse dimension (diameter Δd / d or width Δb / b)",
            "Poisson's Ratio (σ or ν): Ratio of lateral strain to longitudinal strain under uniaxial stress",
            "Formula for Poisson's Ratio: σ = - (Δd / d) / (ΔL / L) (negative sign ensures σ > 0 since diameter shrinks as length extends)",
            "Limiting values of Poisson's ratio: Theoretical limits (-1.0 < σ < +0.5); Practical limits for real engineering materials (0 < σ < 0.5)",
            "Special case σ = 0.5: Incompressible material whose volume remains perfectly constant under uniaxial tension (ΔV = 0, e.g., natural rubber)",
            "Special case σ ≈ 0: Cork (used as bottle stoppers because lateral expansion is negligible when compressed into a neck)",
            "Derivation of Work Done in Stretching a Wire: External work stored as microscopic elastic potential energy",
            "Incremental work: dW = F(x) dx = (Y A x / L) dx",
            "Total Elastic Energy: W = ∫₀^{ΔL} (Y A x / L) dx = 1/2 (Y A / L) (ΔL)² = 1/2 F ΔL",
            "Elastic Energy Density (u): Energy per unit volume of the deformed wire: u = U / (A · L) = 1/2 (F / A) (ΔL / L) = 1/2 × Stress × Strain",
            "Alternative Energy Density forms: u = 1/2 Y (Strain)² = (Stress)² / (2 Y)",
            "Thermal dissipation in cyclic loading: Hysteresis loop area represents mechanical energy converted into internal heat during one cycle of stretching and relaxing"
        ],
        "key_concepts": [
            "Poisson's Ratio σ = Lateral Strain / Longitudinal Strain (0 to 0.5)",
            "Elastic Potential Energy of Stretched Wire U = ½ F ΔL",
            "Energy Density Formula u = ½ × Stress × Strain = ½ Y ε²",
            "Elastic Hysteresis & Damping of Shock Absorbers"
        ],
        "success_criteria": [
            "State the definition, formula, and physical significance of Poisson's ratio",
            "Prove that the work done in stretching a wire is U = 1/2 F ΔL",
            "Derive the volumetric energy density u = 1/2 × Stress × Strain = (Stress)² / (2Y)",
            "Explain why cork has σ ≈ 0 while rubber has σ ≈ 0.5"
        ],
        "chapter_notes": """# Poisson's Ratio & Elastic Potential Energy
## 1. Lateral Strain & Poisson's Ratio ($\\sigma$)
When a cylinder or wire of length $L$ and diameter $d$ is stretched longitudinally, its length increases by $\\Delta L$, while its diameter simultaneously contracts by $\\Delta d$:
$$\\text{Longitudinal Strain } \\varepsilon_{\\text{long}} = \\frac{\\Delta L}{L} \\quad (\\text{positive})$$
$$\\text{Lateral Strain } \\varepsilon_{\\text{lat}} = -\\frac{\\Delta d}{d} \\quad (\\text{negative})$$

**Poisson's Ratio** is the ratio of lateral strain to longitudinal strain:
$$\\sigma = -\\frac{\\Delta d / d}{\\Delta L / L}$$
- Dimensionless and unitless scalar.
- Theoretical limits from thermodynamic stability: $-1.0 \\le \\sigma \\le 0.5$.
- Practical engineering limits: $0.20 \\le \\sigma \\le 0.40$ (Steel $\\approx 0.28$, Aluminium $\\approx 0.33$).
- For incompressible materials (volume $V = \\frac{\\pi}{4}d^2 L = \\text{const}$):
  $$\\frac{\\Delta V}{V} = 2\\frac{\\Delta d}{d} + \\frac{\\Delta L}{L} = 0 \\implies -\\frac{\\Delta d / d}{\\Delta L / L} = \\frac{1}{2} = 0.5$$

## 2. Derivation: Elastic Potential Energy Stored in Stretched Wire
Consider a wire of length $L$ and cross-sectional area $A$ with Young's modulus $Y$. When elongated by $x$:
$$F(x) = \\frac{Y A}{L} x$$
The work done in producing an infinitesimal elongation $dx$ is:
$$dW = F(x) dx = \\left(\\frac{Y A}{L} x\\right) dx$$
Integrating from $x = 0$ to final elongation $x = \\Delta L$:
$$W = \\int_0^{\\Delta L} \\frac{Y A}{L} x \\, dx = \\frac{Y A}{L} \\left[\\frac{x^2}{2}\\right]_0^{\\Delta L} = \\frac{1}{2} \\frac{Y A (\\Delta L)^2}{L}$$
Since $F = \\frac{Y A \\Delta L}{L}$:
$$U = \\frac{1}{2} F \\Delta L = \\frac{1}{2} \\times \\text{Load} \\times \\text{Extension}$$

## 3. Elastic Potential Energy Density ($u$)
Energy stored per unit volume of the wire ($V = A \\cdot L$):
$$u = \\frac{U}{A L} = \\frac{1}{2} \\left(\\frac{F}{A}\\right) \\left(\\frac{\\Delta L}{L}\\right) = \\frac{1}{2} \\times \\text{Stress} \\times \\text{Strain}$$
Using Hooke's law ($\\text{Stress} = Y \\times \\text{Strain}$):
$$u = \\frac{1}{2} Y \\varepsilon^2 = \\frac{\\sigma^2}{2Y}$$
- **SI Unit**: $\\text{J}\\cdot\\text{m}^{-3} = \\text{N}\\cdot\\text{m}^{-2} = \\text{Pa}$.
""",
        "worked_examples": [
            {
                "problem": "A steel wire of length 2.0 m and cross-sectional area 2.0 mm² is stretched by a load of 40 kg. Find (a) the tension in the wire, (b) the elongation, and (c) the elastic potential energy stored in the wire. Take Y = 2.0 × 10¹¹ N/m² and g = 9.8 m/s².",
                "given": "L = 2.0 m, A = 2.0 mm² = 2.0 × 10⁻⁶ m², m = 40 kg, g = 9.8 m/s², Y = 2.0 × 10¹¹ N/m²",
                "formula": "Tension F = m · g; Elongation ΔL = (F · L) / (A · Y); Elastic Energy U = 1/2 · F · ΔL",
                "substitution": "F = 40 × 9.8 = 392 N; ΔL = (392 × 2.0) / (2.0 × 10⁻⁶ × 2.0 × 10¹¹); U = 0.5 × 392 × ΔL",
                "calculation": "ΔL = 784 / (4.0 × 10⁵) = 1.96 × 10⁻³ m = 1.96 mm; U = 0.5 × 392 N × 1.96 × 10⁻³ m = 0.384 J",
                "finalAnswer": "Tension = 392 N, Elongation = 1.96 mm, Elastic Energy = 0.384 J",
                "unit": "N, mm, and Joules"
            }
        ],
        "common_misconceptions": [
            "Misconception: Work done in stretching a wire is simply Force × Distance (F · ΔL). Reality: The force is not constant; it starts from 0 and increases linearly to F as the wire stretches. Thus the average force is (0 + F)/2 = F/2, giving U = 1/2 F · ΔL."
        ],
        "concept_questions": [
            {
                "question": "A metal wire is stretched so that its longitudinal strain is 0.002. If its Poisson's ratio is 0.30, what is the fractional change in its diameter?",
                "options": [
                    "Decreases by 0.06% (-0.0006)",
                    "Increases by 0.06% (+0.0006)",
                    "Decreases by 0.6% (-0.006)",
                    "Zero change in diameter"
                ],
                "correctAnswer": "Decreases by 0.06% (-0.0006)",
                "explanation": "By definition, Poisson's ratio σ = - (Δd / d) / (ΔL / L). Therefore, lateral strain Δd / d = - σ × (ΔL / L) = - 0.30 × 0.002 = - 0.0006 = - 0.06% (diameter contracts).",
                "hint": "Recall that lateral strain = - σ × longitudinal strain.",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "Poisson's Ratio & Elastic Energy Density",
                "diagram_type": "image",
                "diagram_title": "Lateral Contraction & Energy Shaded Under Stress-Strain Curve",
                "why_needed": "Visualizes energy density as the area under the stress-strain line",
                "timing_and_cue": "Stage 4 during the derivation of U = 1/2 F ΔL",
                "what_to_explain": "Why the area under the linear stress-strain curve equals volumetric energy density u = 1/2 σ ε",
                "image_search_query": "elastic energy density area under stress strain curve diagram",
                "svg": mod4_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Elastic Energy Integration",
                    "diagram_type": "image",
                    "image_search_query": "poissons ratio lateral contraction diagram cylinder",
                    "svg": mod4_svg
                }
            ]
        },
        "ai_system_prompt_context": "SENIOR PEDAGOGY: Emphasize that the factor 1/2 in U = 1/2 F ΔL arises because the tension grows from 0 to F linearly, perfectly analogous to spring potential energy U = 1/2 k x²."
    })

    # -------------------------------------------------------------
    # MODULE 5: Engineering Applications of Elasticity: Girders, Sagging & Mountain Limit
    # Order Index: 49
    # -------------------------------------------------------------
    mod5_svg = sb2.build_stress_strain_curve_svg(
        material="I-Beam Section",
        title="Structural Engineering: I-Shaped Girders & Maximum Mountain Height",
        caption="Sagging δ = W L³ / (4 b d³ Y) | Maximum mountain height h_max ≈ σ_yield / (ρ g) ≈ 10 km"
    )

    modules.append({
        "order_index": 49,
        "title": "Engineering Applications of Elasticity: I-Shaped Girders, Sagging of Beams & Maximum Mountain Height",
        "description": "Real-world structural engineering design principles based on elasticity: mathematical formula for beam deflection (sagging), why bridge girders have I-shaped cross-sections (maximizing moment of inertia and bending stiffness while minimizing dead weight and buckling), crane cable design, and geological calculation of the theoretical maximum height of mountains on Earth (~10 km).",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 55,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "Bending of a beam supported at ends and loaded at the center",
            "Derivation / Statement of Sagging (Depression δ): δ = (W L³) / (4 b d³ Y)",
            "Role of parameters: Length L, breadth b, depth d, and Young's modulus Y",
            "Why depth d is far more effective than breadth b: δ ∝ 1/d³ vs δ ∝ 1/b (doubling depth reduces sagging by factor of 8)",
            "Problem of Buckling: Thin deep rectangular beams buckle sideways under load",
            "The I-Section Girder Solution: Wide flanges at top and bottom resist high tensile and compressive stresses, while thin web resists shear, maximizing bending resistance per unit weight",
            "Design of Crane Cables: Limiting working stress well below yield strength (safety factor of 5 to 10)",
            "Calculation of crane cable radius: r ≥ √(M g / (π σ_safe))",
            "Geological Application: Maximum height of mountains on Earth",
            "Balance of base pressure and rock shear strength: At the base of a mountain of height h, pressure is P = h ρ g",
            "Elastic shear limit of rocks: Rocks flow plastically when shear stress exceeds ~3 × 10⁸ N/m²",
            "Deduction of mountain height: h_max = σ_yield / (ρ g) ≈ (3 × 10⁸ N/m²) / (3000 kg/m³ × 9.8 m/s²) ≈ 10,200 m ≈ 10 km",
            "Comparison with Mount Everest (8848 m): Confirms that Mount Everest is near the ultimate physical limit imposed by the elastic properties of Earth's crust"
        ],
        "key_concepts": [
            "Beam Depression Formula δ = (W L³) / (4 b d³ Y)",
            "Why I-Section Girders Prevent Buckling and Minimize Weight",
            "Crane Cable Radius Sizing with Safety Factors",
            "Maximum Theoretical Mountain Height Limit on Earth (~10 km)"
        ],
        "success_criteria": [
            "Explain why increasing beam depth d is 4 times more effective than increasing breadth b in reducing depression",
            "Justify why structural steel girders are manufactured with an I-shaped cross section",
            "Calculate minimum cable thickness required to hoist heavy industrial cranes safely",
            "Derive the maximum mountain height on Earth from first principles using rock shear strength"
        ],
        "chapter_notes": """# Engineering Applications of Elasticity
## 1. Bending of Beams & Sagging
A horizontal beam of rectangular cross-section (breadth $b$, depth $d$, length $L$) supported at both ends and carrying a central load $W = M g$ undergoes a central downward depression (sagging) given by:
$$\\delta = \\frac{W L^3}{4 b d^3 Y}$$

### Key Engineering Insights:
- Sagging $\\delta$ is inversely proportional to $Y$: Materials with large Young's modulus (like steel, $Y \\approx 2 \\times 10^{11}\\text{ Pa}$) are chosen for structural construction.
- Sagging depends critically on depth: $\\delta \\propto \\frac{1}{d^3}$.
  - Doubling breadth $b$ halves sagging ($\\\\delta \\to \\delta / 2$).
  - Doubling depth $d$ reduces sagging by an enormous factor of $8$ ($\\\\delta \\to \\delta / 8$)!
  - Therefore, beams are designed with large vertical depth rather than horizontal breadth.

## 2. Why Bridge Girders are I-Shaped
If a beam is made simply with a very large depth $d$ and small breadth $b$, it becomes laterally unstable and undergoes **buckling** (bending sideways and twisting under load).
- To prevent buckling while retaining maximum bending stiffness, girders are manufactured in an **I-cross-section** shape:
  1. The **top and bottom horizontal flanges** provide large width to prevent lateral buckling and sustain the maximum compressive (top) and tensile (bottom) normal stresses.
  2. The **vertical central web** carries vertical shear while keeping total material volume and dead weight minimal.
  3. Saves immense steel tonnage while guaranteeing maximum structural safety.

## 3. Physical Limit to the Height of Mountains on Earth
At the base of a mountain of height $h$, the hydrostatic rock pressure is:
$$P = h \\rho g$$
Rocks at the base experience lateral shearing stress because the surrounding plain does not exert equal lateral containment pressure. Rocks flow plastically like viscous wax when the shear stress exceeds their elastic shear yield strength:
$$\\sigma_{\\text{rock}} \\approx 3 \\times 10^8\\text{ N/m}^2$$
For typical crustal rock, density $\\rho \\approx 3000\\text{ kg/m}^3$:
$$h_{\\text{max}} \\rho g \\le \\sigma_{\\text{rock}} \\implies h_{\\text{max}} = \\frac{\\sigma_{\\text{rock}}}{\\rho g}$$
$$h_{\\text{max}} = \\frac{3 \\times 10^8\\text{ N/m}^2}{3000\\text{ kg/m}^3 \\times 9.8\\text{ m/s}^2} = \\frac{3 \\times 10^8}{29400} \\approx 10,204\\text{ m} \\approx 10.2\\text{ km}$$
This explains why Mount Everest ($8848\\text{ m} \\approx 8.85\\text{ km}$) cannot grow indefinitely: any mountain approaching $10\\text{ km}$ causes its foundation rocks to liquefy and sink plastically into the crust! On Mars, where surface gravity is smaller ($g_{\\text{Mars}} \\approx 3.7\\text{ m/s}^2$), Olympus Mons reaches over $21\\text{ km}$!
""",
        "worked_examples": [
            {
                "problem": "A crane has a maximum load lifting capacity of 10 metric tonnes (10,000 kg). If the safe working stress of steel is 1.5 × 10⁸ N/m² (incorporating a safety factor), what should be the minimum radius of the steel rope? (NCERT Example 8.5)",
                "given": "Mass m = 10 tonnes = 10,000 kg, Load W = m · g = 10,000 × 9.8 = 9.8 × 10⁴ N, Safe stress σ_safe = 1.5 × 10⁸ N/m²",
                "formula": "Stress σ = W / A = W / (π r²) <= σ_safe => r >= √(W / (π σ_safe))",
                "substitution": "r >= √[ (9.8 × 10⁴ N) / (π × 1.5 × 10⁸ N/m²) ]",
                "calculation": "Denominator = 3.1416 × 1.5 × 10⁸ = 4.712 × 10⁸; Fraction = 9.8 × 10⁴ / 4.712 × 10⁸ = 2.0796 × 10⁻⁴; r = √(2.0796 × 10⁻⁴) = 0.0144 m = 1.44 cm",
                "finalAnswer": "Minimum radius of the crane rope = 1.44 cm (minimum diameter = 2.88 cm ≈ 3 cm)",
                "unit": "cm / meters"
            }
        ],
        "common_misconceptions": [
            "Misconception: A mountain can theoretically grow to arbitrary heights if plate tectonics keeps pushing it up. Reality: The elastic yield limit of rocks at high pressure imposes a hard physical ceiling of ~10 km on Earth."
        ],
        "concept_questions": [
            {
                "question": "If the depth of a rectangular beam is doubled while keeping its length, breadth, and central load unchanged, by what factor does its central depression (sagging) change?",
                "options": [
                    "Decreases by a factor of 8 (becomes 1/8th of initial sagging)",
                    "Decreases by a factor of 4",
                    "Halves",
                    "Remains unchanged"
                ],
                "correctAnswer": "Decreases by a factor of 8 (becomes 1/8th of initial sagging)",
                "explanation": "From the beam depression formula δ = (W L³) / (4 b d³ Y), sagging δ is inversely proportional to the cube of depth (δ ∝ 1/d³). When d is doubled (2d), d³ increases by 2³ = 8, so δ becomes 1/8th.",
                "hint": "Check the power of depth d in the formula δ = W L³ / (4 b d³ Y).",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "I-Section Beam & Mountain Height Physics",
                "diagram_type": "image",
                "diagram_title": "I-Beam Cross Section & Stress Distribution",
                "why_needed": "Visualizes why flanges resist bending and web resists shear",
                "timing_and_cue": "Stage 3 when explaining I-shaped girders in railway bridges",
                "what_to_explain": "Stress distribution across top compression flange, neutral axis, and bottom tension flange",
                "image_search_query": "I-shaped girder cross section bending stress neutral axis diagram",
                "svg": mod5_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "Structural Elasticity Applications",
                    "diagram_type": "image",
                    "image_search_query": "maximum height of mountains on earth physics rock shear strength diagram",
                    "svg": mod5_svg
                }
            ]
        },
        "ai_system_prompt_context": "TEACHING HOOK: Hook students with the fascinating geological question: 'Why is there no mountain on Earth taller than 10 km? Why is Olympus Mons on Mars 21 km tall?' Connect directly to g and rock shear strength."
    })

    # -------------------------------------------------------------
    # MODULE 6: Comprehensive NCERT Textbook Exercises 8.1 to 8.21 Solver
    # Order Index: 50
    # -------------------------------------------------------------
    mod6_svg = sb2.build_stress_strain_curve_svg(
        material="NCERT Exercise Master Suite",
        title="NCERT Exercises 8.1 to 8.21 Full Solutions Suite",
        caption="Step-by-step solutions with Given, Formula, Substitution, Calculation & Boxed Answer"
    )

    modules.append({
        "order_index": 50,
        "title": "Comprehensive NCERT Textbook Exercises 8.1 to 8.21 Detailed Numerical Solutions Suite",
        "description": "Exhaustive step-by-step solutions to all end-of-chapter NCERT exercise questions (8.1 to 8.21) on Mechanical Properties of Solids, covering composite wires (steel + brass), thermal stresses, bulk modulus of water/glass, shear modulus of aluminium cubes, Poisson's ratio, and edge boundary conditions.",
        "syllabus_term": SYLLABUS_TERM,
        "syllabus_unit": UNIT,
        "estimated_minutes": 60,
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "subtopics": [
            "NCERT Exercise 8.1: Stress-strain curves for materials A and B - Young's modulus comparison & ductility",
            "NCERT Exercise 8.2: True/False statements on shear modulus of rubber vs steel and stretching of coils",
            "NCERT Exercise 8.3: Stress-strain graphs for rubber and aorta tissue (elastomers)",
            "NCERT Exercise 8.4: Two wires of diameter 0.25 cm (steel and brass) supporting suspended masses",
            "NCERT Exercise 8.5: Edge of aluminium cube 10 cm sheared by tangential force of 9 × 10⁴ N",
            "NCERT Exercise 8.6: Four identical cylindrical pillars of mild steel supporting a massive structure",
            "NCERT Exercise 8.7: Copper piece under hydraulic pressure in deep ocean trench",
            "NCERT Exercise 8.8: Steel cable radius required to support maximum acceleration in high-speed elevators",
            "NCERT Exercise 8.9: Rigid bar of mass 15 kg supported symmetrically by three wires (two copper, one iron in middle)",
            "NCERT Exercise 8.10: Rod of length 1.05 m with negligible mass supported by steel wire and brass wire with suspended weight",
            "NCERT Exercises 8.11 to 8.21: Bulk modulus of glass, compressibility of water, and advanced elasticity numericals"
        ],
        "key_concepts": [
            "Composite Wires in Series (Equal Tension, Additive Extensions)",
            "Composite Wires in Parallel (Equal Extension, Distributed Tensions)",
            "Shear Displacement of Fixed-Base Blocks",
            "Systematic Board Exam Layout: Given -> Formula -> Substitution -> Calculation -> Boxed Answer"
        ],
        "success_criteria": [
            "Solve composite wire problems where tensions or extensions are distributed",
            "Calculate shearing displacement Δx = (F · L) / (A · G) for fixed-base cubes",
            "Determine the position of suspended masses on rigid bars for equal stress or equal strain",
            "Master every authentic numerical pattern appearing in CBSE Class 11 final-term physics examination"
        ],
        "chapter_notes": """# NCERT Chapter 8: Complete Exercise Solutions Master Notes
## Summary of Governing Formulas:
1. **Stress**: $\\sigma = \\frac{F}{A}$ ($[\\text{N/m}^2]$ or $\\text{Pa}$)
2. **Strain**: Longitudinal $\\varepsilon = \\frac{\\Delta L}{L}$, Shear $\\theta = \\frac{\\Delta x}{L}$, Volume $\\varepsilon_v = \\frac{\\Delta V}{V}$
3. **Young's Modulus**: $Y = \\frac{F L}{A \\Delta L}$
4. **Shear Modulus**: $G = \\frac{F_{\\parallel} L}{A \\Delta x}$
5. **Bulk Modulus**: $B = -\\frac{\\Delta P}{\\Delta V / V}$, Compressibility $k = \\frac{1}{B}$
6. **Poisson's Ratio**: $\\sigma = -\\frac{\\Delta d / d}{\\Delta L / L}$
7. **Elastic Energy Density**: $u = \\frac{1}{2} \\sigma \\varepsilon = \\frac{1}{2} Y \\varepsilon^2 = \\frac{\\sigma^2}{2Y}$
8. **Total Elastic Energy**: $U = \\frac{1}{2} F \\Delta L$
9. **Sagging of Beam**: $\\delta = \\frac{W L^3}{4 b d^3 Y}$
""",
        "worked_examples": [
            {
                "problem": "A rigid bar of mass 15 kg is supported symmetrically by three wires each 2.0 m long. Those at each end are of copper and the middle one is of iron. Determine the ratio of their diameters if each is to have the same tension. (NCERT Exercise 8.9)",
                "given": "Length of all wires L = 2.0 m, Mass m = 15 kg, Symmetrical support => T_cu = T_iron = T, Y_cu = 1.1 × 10¹¹ N/m², Y_iron = 1.9 × 10¹¹ N/m²",
                "formula": "Since the bar is rigid and supported symmetrically, extensions are equal: ΔL_cu = ΔL_iron. ΔL = (T · L) / (A · Y) = (4 T L) / (π d² Y) => d² Y = constant => d_cu / d_iron = √(Y_iron / Y_cu)",
                "substitution": "d_cu / d_iron = √(1.9 × 10¹¹ / 1.1 × 10¹¹) = √(1.9 / 1.1)",
                "calculation": "1.9 / 1.1 = 1.727; √(1.727) = 1.314",
                "finalAnswer": "Ratio of diameters d_copper : d_iron = 1.31 : 1",
                "unit": "Dimensionless ratio"
            },
            {
                "problem": "The edge of an aluminium cube is 10 cm long. One face of the cube is firmly fixed to a vertical wall. A mass of 100 kg is then attached to the opposite face of the cube. The shear modulus of aluminium is 25 GPa. What is the vertical deflection of this face? (NCERT Exercise 8.5)",
                "given": "Edge length L = 10 cm = 0.10 m, Face area A = L² = (0.10)² = 0.01 m², Attached mass m = 100 kg, Tangential force F = m · g = 100 × 9.8 = 980 N, G = 25 GPa = 25 × 10⁹ N/m²",
                "formula": "Shear modulus G = (F / A) / (Δx / L) => Vertical deflection Δx = (F · L) / (A · G)",
                "substitution": "Δx = (980 N × 0.10 m) / (0.01 m² × 25 × 10⁹ N/m²)",
                "calculation": "Numerator = 98; Denominator = 2.5 × 10⁸; Δx = 98 / 2.5 × 10⁸ = 3.92 × 10⁻⁷ m = 392 nm",
                "finalAnswer": "Vertical deflection Δx = 3.92 × 10⁻⁷ m (or 3.92 × 10⁻⁴ mm)",
                "unit": "meters / nm"
            }
        ],
        "common_misconceptions": [
            "Misconception: In symmetric support problems with rigid bars, strains are always different. Reality: Because the rigid bar remains horizontal, all three wires must stretch by the exact same extension ΔL."
        ],
        "concept_questions": [
            {
                "question": "An aluminium cube of edge 10 cm has one face fixed to a wall and a tangential shear force F applied to the opposite face. If the edge length of the cube is doubled to 20 cm under the same shear force F, how does the vertical deflection Δx change?",
                "options": [
                    "Vertical deflection is halved (Δx / 2)",
                    "Vertical deflection doubles",
                    "Vertical deflection remains unchanged",
                    "Vertical deflection becomes 1/4th"
                ],
                "correctAnswer": "Vertical deflection is halved (Δx / 2)",
                "explanation": "Deflection Δx = (F · L) / (A · G) = (F · L) / (L² · G) = F / (L · G). Since Δx is inversely proportional to edge length L (Δx ∝ 1/L), doubling L to 2L halves the deflection.",
                "hint": "Express A in terms of L (A = L²) in Δx = (F · L) / (A · G).",
                "blooms_level": "Apply"
            }
        ],
        "concept_visuals": [
            {
                "concept_title": "NCERT Exercise Problem Solving Suite",
                "diagram_type": "image",
                "diagram_title": "Fixed-Base Cube Shearing & Composite Wire Schematics",
                "why_needed": "Guides step-by-step whiteboard layout for end-of-chapter NCERT problems",
                "timing_and_cue": "Stage 4 when solving Exercises 8.4, 8.5, and 8.9",
                "what_to_explain": "Free body diagrams, equal extension constraints, and shear displacement",
                "image_search_query": "shear deformation cube fixed wall diagram physics",
                "svg": mod6_svg
            }
        ],
        "visual_lesson_plan": {
            "concept_visuals": [
                {
                    "concept_title": "NCERT 8 Exercises",
                    "diagram_type": "image",
                    "image_search_query": "searle apparatus diagram wires",
                    "svg": mod6_svg
                }
            ]
        },
        "ai_system_prompt_context": "CHALKBOARD MANDATE: Strictly follow the Trio Combo (Given -> Formula -> Substitution -> [ROUGH_WORK] -> Boxed Answer) for every NCERT exercise numerical."
    })

    return {
        "curriculum_id": CURRICULUM_ID,
        "title": "Chapter 8: Mechanical Properties of Solids",
        "description": "Comprehensive CBSE Class 11 Physics Part 2 curriculum covering Elasticity, Stress-Strain Relations, Hooke's Law, Young's Modulus, Shear Modulus, Bulk Modulus, Poisson's Ratio, Elastic Energy, and Engineering Applications.",
        "category": "Physics",
        "class_level": CLASS_LEVEL,
        "board": BOARD,
        "difficulty_level": "advanced",
        "order_index": 8,
        "syllabus_term": SYLLABUS_TERM,
        "unit_name": UNIT,
        "weightage_marks": "Part of Unit VII-IX Group (20 Marks)",
        "notes_source_filename": "keph201.pdf",
        "modules": modules
    }
