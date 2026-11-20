# Dynamic Multi-Modality Graph & Diagram Specification (v2.0)
## Universal Standards for CBSE, ICSE & IB Mathematics and Science (Classes 6–12)
*Version: v2.0 • Maintained by Lead AI Engineer, Lead Architect & Lead Prompt Engineer*

---

## 1. Executive Mission & Pedagogical Rationale

Textbooks in Mathematics, Physics, Chemistry, and Biology (NCERT, Selina Concise, Morning Star, Cambridge IB) do not depict quantitative or geometric phenomena as cartoon sketches; they depict them as **scaled, rigorous coordinate geometry plots, mathematical curves, vector diagrams, statistical charts, and authentic educational figures**.

### The Core Invariants Solved
1. **Zero Meaningless / Fake Graphs**: The chalkboard must NEVER render a generic placeholder line ($y = x$) passing through the origin without purpose, points, stopping segments, or figures.
2. **Universal 7-Modality Coordinate Canvas**: Mathematical functions, bounded line segments, physics vectors, statistical bar charts/histograms, geometric polygons (triangles, quadrilaterals), circles, and freeform coordinate text annotations must be rendered dynamically via **Mafs.dev** pure vector SVG math.
3. **Dual Visuals on Every Concept Start**: At the start of every module and concept, the AI tutor must summon BOTH an authentic high-resolution diagram (`search_and_show_image`) AND a real-world demonstration video (`search_and_show_video`).
4. **Micro-Visual & Question Solving Calling Mandate**: Whenever solving a question that involves graphing or coordinate geometry, or whenever even a small visual aid (a 5 cm line segment, a force vector $\vec{F}$, coordinate vertices) clarifies a concept, the AI tutor MUST immediately call `plot_mathematical_graph`.
5. **Chalkboard Synchronization**: Every plotted graph is paired with its step-by-step algebraic derivation on the chalkboard (`Given -> Formula -> Substitution -> Calculation -> Boxed Answer`), ensuring the whiteboard remains the single source of truth for student master notes.

---

## 2. Decision Matrix: Graph Engine vs. Search Engine Visuals vs. Fallback SVG

The AI model and classroom runtime classify every visual aid into its canonical rendering pipeline:

```
                               Visual Requirement
                                        │
        ┌───────────────────────────────┼──────────────────────────────┐
        ▼                               ▼                              ▼
[Mathematical / Coordinate / Vector]   [Concept Start / Real Phenom]  [3D Solid / Apparatus Fallback]
  - Functions: y = f(x), quadratics,    - Turn 1 of Every Concept:     - 3D solids (frustums, cones)
    kinematics (s-t, v-t, a-t),           * High-res diagram search    - Complex electrical apparatus
    Ohm's law (V-I), P-V curves           * Educational video demo     - Ray optics prism refraction
  - Bounded Line Segments & Lengths     - Real-world biological cells    (Strictly when search engine
  - Statistical Bars & Histograms       - Chemical laboratory setups     finds zero educational candidates)
  - Physics Vectors (Forces, velocity)  - Physical experiments
  - Cartesian Polygons & Circles        - Authentic textbook diagrams
  - Freeform Coordinate Annotations
        │                               │                              │
        ▼                               ▼                              ▼
`plot_mathematical_graph`               `search_and_show_image` +      `render_svg_diagram`
(Mafs Pure Vector Canvas)               `search_and_show_video`        (Hairline Axonometric SVG)
                                        (Bing Images & YouTube Embed)  (15s Abort Controller Fallback)
```

### Table of Subject Taxonomy & Tool Selection

| Domain / Concept | Characteristic | Tool to Invoke | Parameters & Modalities Required |
| :--- | :--- | :--- | :--- |
| **Linear Systems & Families** | $y = 2x + 1$, parallel triads $y = 2x + b$ | `plot_mathematical_graph` | `formula="2*x + 1; 2*x + 5"`, `domain="[-4, 4]"`, `points="(0, 1), (0, 5)"` |
| **Bounded Line Segments** | Line segment $AB = 5\text{ cm}$ with stopping points | `plot_mathematical_graph` | `segments='[{"start":[0,0],"end":[5,0],"label":"AB = 5 cm","color":"sky"}]'` |
| **Quadratic Parabolas** | Roots, vertex, axis of symmetry $y = x^2 - 4$ | `plot_mathematical_graph` | `formula="x^2 - 4"`, `points="(-2, 0), (2, 0), (0, -4)"`, `callout="Roots at x=±2"` |
| **Statistics (Bar Graphs)** | Discrete categories & frequencies | `plot_mathematical_graph` | `bars='[{"label":"A","value":25,"color":"emerald"},{"label":"B","value":40}]'` |
| **Statistics (Histograms)** | Continuous class intervals & frequencies | `plot_mathematical_graph` | `bars='0-10:15:sky; 10-20:30:indigo; 20-30:20:amber'` |
| **Physics Vectors (Dynamics)** | Force vectors $\vec{F}_1, \vec{F}_2$ and resultant $\vec{R}$ | `plot_mathematical_graph` | `vectors='[{"tail":[0,0],"tip":[4,0],"label":"F1 = 4N"},{"tail":[0,0],"tip":[0,3],"label":"F2 = 3N"}]'` |
| **Coordinate Geometry Shapes** | Triangle $\Delta ABC$ with coordinate vertices | `plot_mathematical_graph` | `polygons='[{"points":[[1,1],[5,1],[3,5]],"label":"ΔABC","color":"amber"}]'` |
| **Coordinate Circles** | Circle $(x-h)^2 + (y-k)^2 = r^2$ with radius line | `plot_mathematical_graph` | `circles='[{"center":[2,3],"radius":4,"label":"Center (2,3), r=4"}]'` |
| **Arbitrary Graph Annotations**| Coordinate notes, slope formulas, areas | `plot_mathematical_graph` | `texts='[{"x":2,"y":4,"text":"Slope m = Δy/Δx = 2","color":"slate"}]'` |
| **Kinematics (v-t, s-t, a-t)** | $v(t) = u + at$, area under curve | `plot_mathematical_graph` | `formula="4 + 2*x"`, `polygons='[{"points":[[0,0],[5,0],[5,14],[0,4]],"label":"Area = Displacement"}]'` |
| **Ohm's Law & Characteristic** | Current vs Potential $V = I \cdot R$ | `plot_mathematical_graph` | `formula="5*x"`, `domain="[0, 5]"`, `title="V-I Curve (R = 5 Ω)"` |
| **Concept Start (All Topics)** | Turn 1 Intuition of any module or concept | `search_and_show_image` + `search_and_show_video` | Mandatory dual visual pair (High-res diagram + educational video) |
| **Biology Anatomy / Lab setups**| Plant cell wall, xylem, titrations | `search_and_show_image` | Bing Images SafeSearch=Strict + Wikipedia PageImages |
| **Real Experiments / Phenom** | Rutherford scattering, Brownian motion | `search_and_show_video` | YouTube educational player inside digital chalkboard |

---

## 3. The `plot_mathematical_graph` Tool Specification

### Tool Declaration Schema
```typescript
{
  name: "plot_mathematical_graph",
  description: "Plot an interactive mathematical, kinematic, statistical, or vector coordinate graph directly on the whiteboard canvas matching textbook specifications. MANDATORY for linear systems, quadratics, polynomials, coordinate geometry, calculus, kinematics (s-t, v-t), physical rates (W=Fd, V=IR), statistical bar graphs/histograms, physics vectors, bounded line segments, geometric shapes, and coordinate text annotations. Must be accompanied by step-by-step mathematical calculations on the chalkboard.",
  parameters: {
    type: "OBJECT",
    properties: {
      formula: {
        type: "STRING",
        description: "Standard mathematical formula in terms of x. Separate multiple simultaneous curves with semicolons (e.g. '2*x + 1; 2*x + 5' for parallel lines, or 'x^2 - 4; 2*x' for parabola and line intersection). Optional if plotting bars, vectors, segments, or polygons.",
      },
      domain: {
        type: "STRING",
        description: "Horizontal axis range in format '[xMin, xMax]' (e.g. '[-5, 5]' or '[0, 10]'). If omitted, autoBounds calculates optimal domain.",
      },
      range: {
        type: "STRING",
        description: "Vertical axis range in format '[yMin, yMax]' (e.g. '[-10, 10]' or '[0, 30]'). If omitted, autoBounds calculates optimal range.",
      },
      title: {
        type: "STRING",
        description: "Academic title of the graph matching the textbook section (e.g. 'Parallel Triad: y = 2x + b', 'Velocity-Time: Uniform Acceleration', 'Bar Chart: Class Frequency').",
      },
      callout: {
        type: "STRING",
        description: "Core pedagogical invariant or formula note (e.g. 'Slope = a = 2 => Parallel lines | Area under v-t curve = Displacement | Mode = Highest Bar').",
      },
      points: {
        type: "STRING",
        description: "Critical coordinate points to mark and label (e.g. '(0, 5), (0, 1), (0, -1)' or 'Roots: (-2, 0), (2, 0)').",
      },
      segments: {
        type: "STRING",
        description: "JSON array or pipe-delimited string of bounded line segments with stopping points and explicit lengths. Format: '[{\"start\":[x1,y1],\"end\":[x2,y2],\"label\":\"AB = 5 cm\",\"color\":\"sky\"}]' or 'x1,y1->x2,y2:label:color;...'.",
      },
      bars: {
        type: "STRING",
        description: "JSON array or pipe-delimited string of bar items for bar charts or histograms. Format: '[{\"label\":\"Cat A\",\"value\":25,\"color\":\"emerald\"}]' or 'Label:Value:Color;...'. Renders rectangular polygons with values on top and category labels below the x-axis.",
      },
      vectors: {
        type: "STRING",
        description: "JSON array or pipe-delimited string of physics/math vectors. Format: '[{\"tail\":[0,0],\"tip\":[4,3],\"label\":\"F = 5 N\",\"color\":\"indigo\"}]' or 'x1,y1->x2,y2:label:color;...'. Renders with directional arrowheads, tail markers, and magnitude labels.",
      },
      polygons: {
        type: "STRING",
        description: "JSON array of closed geometric figures or shaded regions on Cartesian plane. Format: '[{\"points\":[[x1,y1],[x2,y2],[x3,y3]],\"label\":\"ΔABC\",\"color\":\"amber\",\"fill\":\"rgba(245,158,11,0.15)\"}]'.",
      },
      circles: {
        type: "STRING",
        description: "JSON array of geometric circles on coordinate plane. Format: '[{\"center\":[h,k],\"radius\":r,\"label\":\"Circle C\",\"color\":\"purple\"}]'. Renders center point marker, circular boundary, and radius annotation.",
      },
      texts: {
        type: "STRING",
        description: "JSON array or pipe-delimited string of coordinate text labels. Format: '[{\"x\":2,\"y\":3,\"text\":\"Slope m = 2\",\"color\":\"slate\"}]' or 'x,y:text:color;...'.",
      },
    },
    required: [],
  },
}
```

---

## 4. The Seven Graphing Modalities & Exemplars

### Modality 1: Multi-Curve Function Plots
Used for polynomials, quadratics, linear systems, kinematics ($s-t, v-t, a-t$), Ohm's law ($V-I$), thermodynamics ($P-V$).
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "formula": "x + 2; -0.5*x + 5",
    "domain": "[-2, 8]",
    "range": "[-1, 8]",
    "title": "System of Linear Equations: L1 and L2",
    "points": "(2, 4)",
    "callout": "Intersection Point (2, 4) is the unique algebraic solution",
    "texts": "[{\"x\": 2, \"y\": 4.6, \"text\": \"Solution (2, 4)\", \"color\": \"indigo\"}]"
  }
}
```

### Modality 2: Bounded Line Segments with Explicit Stopping Points & Lengths
Used for coordinate geometry segments, stopping lines, triangle legs, measurement proofs.
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "title": "Distance Between Two Points on Coordinate Plane",
    "segments": "[{\"start\":[1,2],\"end\":[7,10],\"label\":\"d = √[(7-1)² + (10-2)²] = 10 units\",\"color\":\"sky\"},{\"start\":[1,2],\"end\":[7,2],\"label\":\"Δx = 6\",\"color\":\"slate\"},{\"start\":[7,2],\"end\":[7,10],\"label\":\"Δy = 8\",\"color\":\"slate\"}]",
    "points": "(1, 2), (7, 10), (7, 2)",
    "callout": "Pythagoras on Cartesian Grid: d² = Δx² + Δy² = 36 + 64 = 100 => d = 10"
  }
}
```

### Modality 3: Statistical Bar Graphs & Frequency Histograms
Used for CBSE/ICSE Class 9 and 10 Statistics, data handling, frequency distributions.
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "title": "Class 9 Statistics: Weekly Study Hours Distribution",
    "bars": "[{\"label\":\"0-2h\",\"value\":8,\"color\":\"sky\"},{\"label\":\"2-4h\",\"value\":15,\"color\":\"emerald\"},{\"label\":\"4-6h\",\"value\":24,\"color\":\"indigo\"},{\"label\":\"6-8h\",\"value\":18,\"color\":\"amber\"},{\"label\":\"8+h\",\"value\":10,\"color\":\"rose\"}]",
    "callout": "Modal Class is 4-6 hours with maximum frequency f = 24"
  }
}
```

### Modality 4: Physics Vectors & 2D Force Resolution
Used for Class 9 Motion & Force, Class 11 Vectors, Kinematics, Equilibrium, and Dynamics.
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "title": "Resolution of Force Vector into Rectangular Components",
    "vectors": "[{\"tail\":[0,0],\"tip\":[8,6],\"label\":\"F = 10 N (θ = 36.9°)\",\"color\":\"indigo\"},{\"tail\":[0,0],\"tip\":[8,0],\"label\":\"Fx = F·cosθ = 8 N\",\"color\":\"emerald\"},{\"tail\":[0,0],\"tip\":[0,6],\"label\":\"Fy = F·sinθ = 6 N\",\"color\":\"sky\"}]",
    "callout": "Vector Magnitude: |F| = √(Fx² + Fy²) = √(64 + 36) = 10 N",
    "texts": "[{\"x\":2.5,\"y\":0.8,\"text\":\"θ = 37°\",\"color\":\"slate\"}]"
  }
}
```

### Modality 5: Geometric Polygons (Triangles & Quadrilaterals) on Coordinate Plane
Used for Class 9 & 10 Coordinate Geometry (Area of Triangle, Quadrilateral Vertices, Collinearity).
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "title": "Coordinate Geometry: Area of Triangle ABC",
    "polygons": "[{\"points\":[[1,1],[6,2],[4,7]],\"label\":\"ΔABC (Area = 14.5 sq units)\",\"color\":\"amber\",\"fill\":\"rgba(245,158,11,0.18)\"}]",
    "points": "A(1, 1), B(6, 2), C(4, 7)",
    "callout": "Area = 0.5 · |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)| = 14.5"
  }
}
```

### Modality 6: Coordinate Circles & Tangents
Used for Class 10 Circles, Tangent theorems, Cartesian circle representations.
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "title": "Circle with Center (3, 3) and Radius 4 with Tangent Line",
    "circles": "[{\"center\":[3,3],\"radius\":4,\"label\":\"Circle: (x-3)² + (y-3)² = 16\",\"color\":\"purple\"}]",
    "formula": "7 - 0*(x)",
    "segments": "[{\"start\":[3,3],\"end\":[3,7],\"label\":\"Radius r = 4 (Perpendicular to Tangent)\",\"color\":\"amber\"}]",
    "points": "(3, 3), (3, 7)",
    "callout": "Theorem: Radius is strictly perpendicular to tangent at point of contact (3, 7)"
  }
}
```

### Modality 7: Multiple Coordinate Text Callouts & Explanations
Used to position arbitrary mathematical notes, step annotations, and formulas directly on the coordinate plane.
```json
{
  "tool": "plot_mathematical_graph",
  "args": {
    "formula": "3*x",
    "title": "Work-Distance Relationship W = F · d",
    "points": "(0, 0), (2, 6), (4, 12)",
    "texts": "[{\"x\":2.2,\"y\":6,\"text\":\"Point P(2, 6): W = 6 J at d = 2 m\",\"color\":\"indigo\"},{\"x\":0.5,\"y\":9,\"text\":\"Slope = F = ΔW/Δd = 3 N\",\"color\":\"emerald\"}]",
    "callout": "Slope of Work vs Distance gives the constant applied force F = 3 N"
  }
}
```

---

## 5. Dual Visual Mandate (`search_and_show_image` + `search_and_show_video`)

### Protocol on Concept Start (Step 1 Intuition)
At the start of **every module** and **every concept turn**, the tutor MUST invoke BOTH visual search tools:
```json
// Turn 1 Visual Directive 1:
{
  "tool": "search_and_show_image",
  "args": {
    "query": "concise educational topic keyword diagram apparatus"
  }
}

// Turn 1 Visual Directive 2:
{
  "tool": "search_and_show_video",
  "args": {
    "query": "topic demonstration experiment classroom video"
  }
}
```

### Content Safety & Ranking Invariants
1. **Search Engine First**: Bing Images with `&adlt=strict` runs FIRST. Authoritative Wikipedia PageImages runs SECOND. Wikimedia Commons runs THIRD.
2. **Harmful & Political Guard**: Political elections, ballot propositions, watermarked stock imagery, and non-educational content are permanently filtered and discarded.
3. **Concise Keyword Extraction**: Sentences and lengthy descriptions are automatically distilled into concise 2–5 word academic topic keywords via `extractConciseSearchKeyword`.
4. **YouTube Native Player**: Videos stream directly inside the chalkboard interface via responsive `video/youtube` iframe players.

---

## 6. Micro-Visual & Question Solving Mandate

The AI tutor must adhere to the following strict operational rules:
1. **Solve Graphically on Demand**: Whenever a textbook question asks to "draw the graph", "find the area graphically", "find the point of intersection", "plot the points", "represent the data as a bar chart/histogram", or "illustrate vectors", the tutor MUST call `plot_mathematical_graph`.
2. **Micro-Visual Explanations**: Do not wait for a full-length graph question. When explaining concepts like:
   - A line segment with a specific length ($AB = 6\text{ cm}$)
   - Distance between two coordinates
   - A force acting at an angle ($F = 10\text{ N}$ at $30^\circ$)
   - A velocity vector or displacement
   - A simple linear rate or slope
   The tutor must proactively trigger `plot_mathematical_graph` with bounded segments, vectors, or coordinates to provide visual intuition.
3. **Companion Whiteboard Derivation**:
   Every graph must be accompanied by structured chalkboard notes:
   - `write_chalkboard(action="draw_note", content="Equation / Theorem: ...")`
   - `write_chalkboard(action="draw_step", content="Given / Values: ...")`
   - `write_chalkboard(action="draw_step", content="Substitution & Calculation: ...")`
   - `write_chalkboard(action="draw_note", content="Boxed Result with Units")`

---
*Maintained under Anaxly Core Architecture Standards.*
