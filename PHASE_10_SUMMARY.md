# Phase 10: Universal Multi-Type Graph Engine & Mandatory Dual Visuals Architecture

## 1. Executive Summary
Phase 10 upgrades Anaxly's classroom visual and graphical capabilities into a production-grade multi-modality system. It fulfills two major mandates:
1. **Mandatory Dual Visuals (Image + Video)**: On turn 1 of every module and concept, the AI tutor must summon BOTH an authoritative educational diagram (`search_and_show_image`) AND a real-world demonstration video (`search_and_show_video`), with client-side pre-fetching to prime both cards before speech commences.
2. **Universal Multi-Type Graph Engine**: Extends the digital chalkboard's graphing canvas (`MafsGraphCanvas.tsx` & `graphGating.ts`) to support seven distinct coordinate modalities: mathematical curves, bounded line segments with stopping points, physics vectors, statistical bar charts and histograms, geometric polygons (triangles, quadrilaterals), circles, and freeform coordinate text annotations. The engine includes dynamic autoBounds calculation and enforces a micro-visual calling mandate where the tutor summons graphs whenever solving questions or explaining quantitative concepts.

---

## 2. Universal Multi-Type Graph Engine Specifications

### 2.1 The Seven Coordinate Modalities
The chalkboard graph engine is powered by pure vector SVG math using **Mafs.dev**:

1. **Function Curves ($y = f(x)$)**:
   - Evaluates single and comparative mathematical formulas separated by semicolons (e.g. `2*x + 1; 2*x + 5`).
   - Supports polynomials, quadratics, kinematics ($s-t, v-t, a-t$), Ohm's law ($V-I$), thermodynamics ($P-V$).
   - Automatically finds numerical roots and intersection coordinates.

2. **Bounded Line Segments & Explicit Lengths (`segments`)**:
   - Renders discrete line segments between explicit start `[x1, y1]` and end `[x2, y2]` stopping points.
   - Accompanying midpoint length labels (e.g. `"AB = 5 cm"`, `"d = 10 units"`).
   - Eliminates unbounded lines through origin when teaching coordinate distance, triangle sides, or segment geometry.

3. **Critical Coordinate Points (`points`)**:
   - Highlights coordinate points with filled markers, coordinate labels `(x, y)`, and pedagogical callouts (roots, intercepts, vertex, local extrema).

4. **Statistical Bar Graphs & Histograms (`bars`)**:
   - Renders discrete categorical bars and continuous class frequency intervals as shaded Cartesian polygons.
   - Values are stamped above each bar, and category labels or bin intervals are positioned below the x-axis.
   - Fully compliant with CBSE and ICSE Class 9/10 Statistics curricula.

5. **Physics Vectors (`vectors`)**:
   - Visualizes 2D force, velocity, acceleration, and ray vectors with directional arrowheads, tail markers, and magnitude/angle labels (e.g. `F = 10 N (θ = 37°)`).
   - Enables visual parallelogram vector addition and component resolution ($F_x = F\cos\theta, F_y = F\sin\theta$).

6. **Geometric Polygons & Circles (`polygons`, `circles`)**:
   - Polygons: Closed triangles, quadrilaterals, and shaded areas under curves rendered with semi-transparent fills and accented borders.
   - Circles: Cartesian circles rendered with center point marker, circular boundary, and radius annotation line.

7. **Multiple Coordinate Text Annotations (`texts`)**:
   - Allows the AI tutor to place arbitrary pedagogical notes, slope formulas, and step labels at specific $(x, y)$ coordinates directly on the graph plane.

### 2.2 Dynamic AutoBounds Viewport Calculation
When explicit `domain` and `range` are omitted, `MafsGraphCanvas.tsx` dynamically inspects all present elements (bars, vectors, polygons, circles, segments, points, and formula curves) and calculates:
```typescript
xSpan = Math.max(xMax - xMin, 6);
ySpan = Math.max(yMax - yMin, 6);
xMargin = xSpan * 0.20;
yMargin = ySpan * 0.20;
domain = [xMin - xMargin, xMax + xMargin];
range = [yMin - yMargin, yMax + yMargin];
```
This guarantees zero visual clipping and ensures all geometric shapes, vectors, and bar charts are centered and legible.

---

## 3. Mandatory Dual Visuals Architecture (Image + Video)

### 3.1 Turn 1 Visual Directive
In `src/app/dashboard/[id]/class/[moduleId]/page.tsx` and `src/services/geminiWebSocket.ts`, the tutor persona instructions mandate:
```
TURN 1 MANDATORY VISUAL PAIR:
You MUST emit BOTH:
1. search_and_show_image(query="...") - High-resolution educational diagram
2. search_and_show_video(query="...") - Real-world demonstration video
```

### 3.2 Proactive Frontend Pre-fetching
The client-side `ensureConceptVisualSynthesized` function automatically fires background requests to `/api/diagram/search-image` and `/api/diagram/search-video` as soon as a concept is activated. Both the image card and the responsive YouTube classroom player are primed and ready on the digital chalkboard before speech begins.

### 3.3 Search Engine First & SafeSearch=Strict Guard
- **Engine Priority**: Bing Images web search engine runs FIRST, authoritative Wikipedia PageImages SECOND, and Wikimedia Commons THIRD.
- **Safety**: Queries include `&adlt=strict` to enforce SafeSearch=Strict. Political election results, ballot initiatives, and watermarked stock imagery are permanently filtered.
- **Bespoke LLM SVG Fallback**: If zero online results are found, `/api/diagram/generate` acts as a last-resort fallback with a strict 15-second abort controller.

---

## 4. Micro-Visual & Question Solving Mandate

The AI tutor adheres to the following behavioral invariants:
1. **Always Plot Graph Questions**: Whenever a textbook problem asks to plot, find intercepts, calculate slope, determine area under a curve, or solve graphically, the tutor MUST invoke `plot_mathematical_graph`.
2. **Proactive Micro-Visuals**: When explaining small concepts (such as a 6 cm segment, a force vector, or coordinate points), the tutor proactively calls `plot_mathematical_graph` rather than speaking purely in abstract terms.
3. **No Unbounded Lines**: Empty graphs or lines through origin with no points, segments, or figures are strictly prohibited.

---

## 5. Verification & Testing

- `npx tsx src/tests/enhancedGraphUIAndGatingVerification.ts`: **46/46 tests passed**.
- `npx tsx src/tests/multiTypeGraphAndDualVisualVerification.ts`: **24/24 tests passed**.
- `npx tsc --noEmit`: **0 errors**.
- All 70 automated verification assertions signed off and committed to `main`.
