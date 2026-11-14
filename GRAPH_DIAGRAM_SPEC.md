# Dynamic Graph-Based Diagram Specification & AI Prompt Engine
## Standards for CBSE, ICSE & IB Mathematics and Physics (Classes 6–12)
*Version: v1.0 • Maintained by Lead AI Engineer & Lead Prompt Engineer*

---

## 1. Executive Mission & Pedagogical Rationale

Textbooks in Mathematics and Physics (NCERT, Selina Concise, Morning Star, Cambridge IB) do not depict abstract phenomena as cartoon sketches; they depict them as **scaled, rigorous coordinate geometry plots and mathematical curves**.

### The Core Problem Solved
1. **Zero Fake/Sketched Graphs**: Mathematical concepts (such as $y = 2x + 1$, projectile parabolas, or velocity-time motion) must NEVER be rendered as static cartoon SVGs with fake hand-drawn axes.
2. **Textbook Verbatim Alignment**: Diagrams representing functions, coordinates, rates, forces, or kinematic progressions must be dynamically plotted on the digital chalkboard using the **Mafs.dev** vector engine with exact mathematical equations.
3. **Chalkboard Synchronization**: Every plotted graph MUST be paired with its algebraic derivation on the chalkboard (`Given -> Formula -> Substitution -> Calculation -> Boxed Answer`), ensuring the whiteboard remains the single source of truth for student notes.

---

## 2. Decision Matrix: Graph Plotting vs. Hairline Vector SVG

The AI model and curriculum ingestion pipeline must classify every diagram into one of two distinct rendering engines:

```
                              Diagram Requirement
                                       │
        ┌──────────────────────────────┴──────────────────────────────┐
        ▼                                                             ▼
[Mathematical / Coordinate / Rate]                       [Physical Apparatus / Anatomy / 3D]
  - Functions: y = ax + b, y = ax² + bx + c               - Biological cells & tissues
  - Coordinate Geometry: Points, lines, triangles         - 3D Solids (Cylinders, cones, spheres)
  - Kinematics: s-t, v-t, a-t curves                      - Optical ray tracing across glass prisms
  - Physical Laws: W = F·d, V = I·R, F = k·x              - Electric circuits & chemical apparatus
        │                                                             │
        ▼                                                             ▼
`plot_mathematical_graph`                                   `render_svg_diagram`
(Mafs Vector Canvas)                                        (Hairline 30° Axonometric Vector SVG)
```

### Table of Subject Taxonomy & Tool Selection

| Domain / Concept | Characteristic | Tool to Invoke | Parameters Required |
| :--- | :--- | :--- | :--- |
| **Linear Polynomials & Lines** | $y = 2x + 1$, parallel triads $y = 2x + b$ | `plot_mathematical_graph` | `formula="2*x + 1; 2*x + 5"`, `domain="[-4, 4]"`, `range="[-4, 8]"`, `points="(0, 1), (0, 5)"` |
| **Quadratic Parabolas** | Roots, vertex, axis of symmetry $y = x^2 - 4$ | `plot_mathematical_graph` | `formula="x^2 - 4"`, `domain="[-4, 4]"`, `range="[-5, 5]"`, `points="(-2, 0), (2, 0), (0, -4)"` |
| **Kinematics (Physics)** | Uniform acceleration $v(t) = u + at$ | `plot_mathematical_graph` | `formula="4 + 2*x"`, `domain="[0, 10]"`, `range="[0, 25]"`, `title="v-t Graph (u=4 m/s, a=2 m/s²)"` |
| **Work & Force Equations** | Physics Work-Distance $W = 3d$ | `plot_mathematical_graph` | `formula="3*x"`, `domain="[0, 6]"`, `range="[0, 20]"`, `points="(0, 0), (2, 6)"`, `callout="Slope = Force = 3 N"` |
| **Ohm's Law (Electricity)** | Current vs Potential $V = I \cdot R$ | `plot_mathematical_graph` | `formula="5*x"`, `domain="[0, 5]"`, `range="[0, 25]"`, `title="V-I Characteristic (R = 5 Ω)"` |
| **Trigonometric Waves** | $\sin(x), \cos(x)$, phase shifts | `plot_mathematical_graph` | `formula="sin(x)"`, `domain="[-6.28, 6.28]"`, `range="[-2, 2]"`, `points="(0, 0), (1.57, 1)"` |
| **Apparatus & Circuits** | Resistor in series with battery, ammeter | `render_svg_diagram` | Clean Hairline 30° axonometric projection with white background |
| **Optics & Refraction** | Ray through triangular prism, angles | `render_svg_diagram` | Hairline vector SVG with incidence, refraction, and deviation angles |
| **Cell Biology & Histology** | Plant cell wall, xylem, stomata | `render_svg_diagram` | Hairline histological cross-section with leader line callouts |

---

## 3. The `plot_mathematical_graph` Production Schema

### Tool Declaration Specification
```typescript
{
  name: "plot_mathematical_graph",
  description: "Plot an interactive mathematical or kinematic function graph directly on the whiteboard canvas matching textbook specifications. MANDATORY for linear systems, quadratics, polynomials, coordinate geometry, calculus, kinematics (s-t, v-t), and physical rates (W=Fd, V=IR). Must be accompanied by step-by-step mathematical calculations on the chalkboard.",
  parameters: {
    type: "OBJECT",
    properties: {
      formula: {
        type: "STRING",
        description: "Standard mathematical formula in terms of x. Separate multiple simultaneous curves with semicolons (e.g. '2*x + 1; 2*x + 5' for parallel lines, or 'x^2 - 4; 2*x' for parabola and line intersection).",
      },
      domain: {
        type: "STRING",
        description: "Horizontal axis range in format '[xMin, xMax]' (e.g. '[-5, 5]' or '[0, 10]').",
      },
      range: {
        type: "STRING",
        description: "Vertical axis range in format '[yMin, yMax]' (e.g. '[-10, 10]' or '[0, 30]').",
      },
      title: {
        type: "STRING",
        description: "Academic title of the graph matching the textbook section (e.g. 'Parallel Triad: y = 2x + b' or 'Velocity-Time: Constant Acceleration').",
      },
      callout: {
        type: "STRING",
        description: "Core pedagogical invariant or formula note (e.g. 'Equal slope a = 2 => Lines never intersect | Area under curve = Displacement').",
      },
      points: {
        type: "STRING",
        description: "Critical coordinate points to mark and label with coordinates (e.g. '(0, 5), (0, 1), (0, -1)' or 'Roots: (-2, 0), (2, 0)').",
      },
    },
    required: ["formula"],
  },
}
```

---

## 4. Full Production Prompt Template for AI Tutor (Next Chapters Ingestion)

This exact prompt block is integrated into every curriculum ingestion from Chapter 3 onward:

```markdown
========================================================================================
MATHEMATICAL & PHYSICS GRAPH-BASED DIAGRAM ENGINE (TEXTBOOK EXACT):
========================================================================================
You are an expert CBSE/ICSE/IB STEM educator. Whenever the curriculum presents a concept
that can be expressed mathematically on a coordinate plane, you MUST use `plot_mathematical_graph`
to plot the exact function curve rather than describing it or drawing flat sketches!

1. MANDATORY MULTI-CURVE SYNCHRONIZATION:
   - When demonstrating systems of equations, parallel lines, intersecting lines, or family of curves:
     Pass all functions separated by semicolons into `formula`:
     Example: plot_mathematical_graph(
       formula="2*x + 5; 2*x + 1; 2*x - 1",
       domain="[-4, 4]",
       range="[-4, 8]",
       title="Parallel Family: y = 2x + b",
       points="(0, 5), (0, 1), (0, -1)",
       callout="Equal slopes (a = 2) guarantee strict parallelism"
     )

2. COMPANION WHITEBOARD DERIVATION MANDATE:
   - A graph must NEVER appear in isolation.
   - On the chalkboard, you must write the exact mathematical work:
     * write_chalkboard(action="draw_note", content="Equation: y = ax + b", color="botanical")
     * write_chalkboard(action="draw_step", content="Intercept: (0, b) | Slope: Δy/Δx = a", color="amber")
     * write_chalkboard(action="draw_rough_work", content="Rough: Table of values (x, y)", color="white")

3. PHYSICS KINEMATICS & DYNAMICS CURVES:
   - For uniform motion: s(t) = vt -> formula="v*x"
   - For uniformly accelerated motion: v(t) = u + at -> formula="u + a*x"
   - For displacement under gravity: s(t) = ut - 0.5gt² -> formula="20*x - 4.9*x^2"
   - For Force-Work relationships: W(d) = Fd -> formula="3*x"

4. NEVER CALL GRAPH FOR NON-MATHEMATICAL TOPICS:
   - Strictly prohibited for Biology, Cell Anatomy, Chemistry, History, or Literature.
   - For non-mathematical topics, call `render_svg_diagram` or `draw_flowchart`.
```

---

## 5. Exemplar Multi-Curve Implementations (Maths & Physics)

### Exemplar A: Systems of Linear Equations (CBSE Class 9 & 10)
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "formula": "x + 2; -0.5*x + 5",
    "domain": "[-2, 6]",
    "range": "[-1, 8]",
    "title": "Intersection of Linear System: L1 and L2",
    "points": "(2, 4)",
    "callout": "Unique Solution at Point of Intersection (2, 4)"
  }
}
```

### Exemplar B: Kinematics Velocity-Time Graph (CBSE Class 9 Physics Motion)
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "formula": "2*x; 10; 10 - 2*(x - 10)",
    "domain": "[0, 15]",
    "range": "[0, 12]",
    "title": "Three-Stage Motion v-t Graph (Acceleration, Uniform, Deceleration)",
    "points": "(0, 0), (5, 10), (10, 10), (15, 0)",
    "callout": "Area under v-t curve = Total Displacement = 100 m"
  }
}
```

### Exemplar C: Quadratic Parabola Vertex & Roots (Class 10 Polynomials)
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "formula": "x^2 - 2*x - 3",
    "domain": "[-3, 5]",
    "range": "[-5, 8]",
    "title": "Quadratic Parabola: y = x² - 2x - 3",
    "points": "(-1, 0), (3, 0), (1, -4)",
    "callout": "Roots at x = -1, 3 | Minimum Vertex at (1, -4)"
  }
}
```

---

## 6. Chapter Ingestion Standard Operating Procedure (SOP)
Starting from Chapter 3 (*"The World of Numbers"*) and all subsequent Science & Math chapters:
1. When a section contains a geometric line, coordinate pattern, scale, or function, the `ai_system_prompt_context` in `syllabus_modules` MUST include the exact `plot_mathematical_graph(...)` call with:
   - Mathematical formula(s)
   - Coordinate domain and range
   - Labeled intercept points
   - Mathematical callout note
2. The companion vector SVG card rendered on the chalkboard will mirror the coordinate plot with crisp `.halo` text, pure `#FFFFFF` background, and animated line strokes.
3. The tutor's live Socratic instruction will guide the student to observe the coordinate intercepts before moving to the numerical problem solving.

---
*Approved and Enforced across all AI Tutor Services.*
