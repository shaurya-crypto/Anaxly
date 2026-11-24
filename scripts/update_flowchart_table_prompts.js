const fs = require('fs');

// 1. Update src/services/geminiWebSocket.ts
const gwsPath = 'src/services/geminiWebSocket.ts';
let gws = fs.readFileSync(gwsPath, 'utf8');
const isGwsCrlf = gws.includes('\r\n');
if (isGwsCrlf) gws = gws.replace(/\r\n/g, '\n');

// 1A. Thinking level latency guard
const oldThinking = `      if (this.model.includes("extended-thinking") || this.thinkingLevel) {
        liveConfig.thinkingConfig = {
          thinkingLevel: this.thinkingLevel || "low",
        };
      }`;

const newThinking = `      // Zero Latency Degradation Invariant: Use 'low' thinking level for enhanced reasoning without audio latency spikes
      // Medium or High thinking levels introduce multi-second silence in conversational streaming audio
      if (this.model.includes("extended-thinking") || this.thinkingLevel) {
        const safeThinkingLevel =
          this.thinkingLevel === "high" || this.thinkingLevel === "medium"
            ? "low"
            : this.thinkingLevel || "low";
        liveConfig.thinkingConfig = {
          thinkingLevel: safeThinkingLevel,
        };
      }`;

if (!gws.includes(oldThinking)) {
  console.error("oldThinking not found in geminiWebSocket.ts");
  process.exit(1);
}
gws = gws.replace(oldThinking, newThinking);

// 1B. Connection error fallback for thinkingConfig
const oldFallback = `        if (this.model.includes("extended-thinking")) {
          console.warn("[GeminiLive] Extended thinking live model unavailable or rejected. Self-healing fallback to standard gemini-3.8-live:", connectError);
          this.model = "gemini-3.8-live";
          delete liveConfig.thinkingConfig;`;

const newFallback = `        if (liveConfig.thinkingConfig && !this.model.includes("extended-thinking")) {
          console.warn("[GeminiLive] Thinking config rejected by endpoint. Instant fallback without thinkingConfig for zero-latency audio streaming:", connectError);
          delete liveConfig.thinkingConfig;
          try {
            this.session = await this.ai.live.connect({
              model: this.model,
              config: liveConfig,
              callbacks: sessionCallbacks,
            });
            return;
          } catch (noThinkingErr) {
            console.warn("[GeminiLive] Standard connection retry with thinking disabled failed, cascading to next fallback:", noThinkingErr);
          }
        }
        if (this.model.includes("extended-thinking")) {
          console.warn("[GeminiLive] Extended thinking live model unavailable or rejected. Self-healing fallback to standard gemini-3.8-live:", connectError);
          this.model = "gemini-3.8-live";
          delete liveConfig.thinkingConfig;`;

if (!gws.includes(oldFallback)) {
  console.error("oldFallback not found in geminiWebSocket.ts");
  process.exit(1);
}
gws = gws.replace(oldFallback, newFallback);

// 1C. Tool description in write_chalkboard
const oldToolDesc = `                name: "write_chalkboard",
                description: "MANDATORY CHALKBOARD TOOL: You MUST invoke this tool in EVERY spoken turn to write notes, definitions, steps, formulas, worked examples, and questions on the student's live chalkboard. Speaking without calling this tool is strictly prohibited. For mathematics and physics problem solving, write cleanly with 1 or at most 2 steps per line in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",`;

const newToolDesc = `                name: "write_chalkboard",
                description: "MANDATORY CHALKBOARD TOOL: You MUST invoke this tool in EVERY spoken turn to write notes, definitions, steps, formulas, worked examples, questions, comparison tables, or flowcharts on the student's live chalkboard. Speaking without calling this tool is strictly prohibited. PROACTIVE VISUAL MASTERY: Whenever comparing, contrasting, or listing differences between concepts, ALWAYS call action='draw_table' with a rich comparison table. Whenever explaining groups, hierarchies, taxonomies, decision trees, or process cycles, ALWAYS call action='draw_flowchart'. For problem solving, write cleanly with 1 or at most 2 steps per line in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",`;

if (!gws.includes(oldToolDesc)) {
  console.error("oldToolDesc not found in geminiWebSocket.ts");
  process.exit(1);
}
gws = gws.replace(oldToolDesc, newToolDesc);

// 1D. Tool parameter content description in write_chalkboard
const oldContentDesc = `                    content: {
                      type: Type.STRING,
                      description: "The text to write, equation, table markup, flowchart text, or color name to apply to the chalkboard. For problem solving or derivations, format with 1 or max 2 steps per line (separated by newlines or semicolons) in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",
                    },`;

const newContentDesc = `                    content: {
                      type: Type.STRING,
                      description: "The text to write, equation, table markup, flowchart text, or color name to apply to the chalkboard. For comparison tables (action='draw_table'), format as markdown table: 'Parameter | Entity A | Entity B\\nRow 1 | Val A1 | Val B1\\nRow 2 | Val A2 | Val B2'. For flowcharts (action='draw_flowchart'), format as branching trees ('Root -> Branch A | Branch B; Branch A -> Sub 1 | Sub 2'), cyclical loops ('cycle: Step 1 -> Step 2 -> Step 3 -> Step 1'), or sequential pathways ('Step 1 -> Step 2 -> Step 3'). For problem solving or derivations, format with 1 or max 2 steps per line in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",
                    },`;

if (!gws.includes(oldContentDesc)) {
  console.error("oldContentDesc not found in geminiWebSocket.ts");
  process.exit(1);
}
gws = gws.replace(oldContentDesc, newContentDesc);

// 1E. System instructions in geminiWebSocket.ts
const oldSystemInst = `       - Pure Mathematical Typography: Use standard textbook notation and Unicode superscripts/symbols (x², v², 10⁸, θ, α, ×, ÷, √, ±). NEVER output raw programming syntax (*, **, ^, //).
    5. Visual Tools & Flexible Diagram Presentation:`;

const newSystemInst = `       - Pure Mathematical Typography: Use standard textbook notation and Unicode superscripts/symbols (x², v², 10⁸, θ, α, ×, ÷, √, ±). NEVER output raw programming syntax (*, **, ^, //).
    5. Proactive Complex Tables & Flowcharts (Real Master Teacher Invariant):
       - Teach visually with ultra-rich chalkboard diagrams like an iconic faculty mentor. Do NOT wait for the student to ask for a table or flowchart! Sketch them proactively whenever useful.
       - Comparison & Difference Tables (action="draw_table"): Whenever explaining differences, distinctions, comparisons, or properties of two or more entities (e.g. Plant vs Animal Cell, Xylem vs Phloem, Distance vs Displacement, Speed vs Velocity, Mitosis vs Meiosis, Real vs Virtual Images, Acids vs Bases, Metals vs Non-metals), PROACTIVELY DRAW A STRUCTURED COMPARISON TABLE:
         * write_chalkboard(action="draw_table", content="Parameter | Entity A | Entity B\\nFeature 1 | Detail A1 | Detail B1\\nFeature 2 | Detail A2 | Detail B2\\nFeature 3 | Detail A3 | Detail B3")
       - Hierarchical Flow Trees & Classifications (action="draw_flowchart"): Whenever breaking down a concept into groups, taxonomies, or decision trees (e.g. Classification of Matter, Plant/Animal Tissues, Real Number System, Organic Reaction Pathways, Types of Sets), PROACTIVELY DRAW A BRANCHING FLOW TREE:
         * write_chalkboard(action="draw_flowchart", content="Root -> Group 1 | Group 2; Group 1 -> Sub 1 | Sub 2; Group 2 -> Sub 3 | Sub 4")
       - Cyclical Mechanisms & Process Pathways (action="draw_flowchart"): For biological or geochemical cycles (Nitrogen cycle, Carbon cycle, Cardiac cycle, Calvin cycle, Water cycle), prefix with 'cycle:':
         * write_chalkboard(action="draw_flowchart", content="cycle: Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 1")
       - Multi-Step Physiological / Reaction Pathways (action="draw_flowchart"):
         * write_chalkboard(action="draw_flowchart", content="Stimulus -> Sensory Receptor -> Sensory Neuron -> Spinal Cord -> Motor Neuron -> Effector Muscle -> Action")
    6. Visual Tools & Flexible Diagram Presentation:`;

const oldInstRemainder = `    6. Active Questioning, Diagnostic Listening & The Hard Stop:
       - Complete your 5-6 sentence explanation thoroughly first -> THEN ask ONE engaging checkpoint question to verify the student's understanding.
       - THE HARD STOP: Once you ask a question, IMMEDIATELY STOP SPEAKING. Wait silently for the student's response. Do NOT answer your own question! Do NOT guess what they might say!
       - Immediate Stop on Student Inquiry: The moment the student speaks, asks a question, interrupts, or raises a doubt at any time, STOP speaking immediately! Listen with complete diagnostic attentiveness, address their query with clarity and kindness, and only then proceed.
       - Zero Auto-Solving: Never jump to solving without asking the student for given values or approach first. Co-solve together line-by-line.
    7. Strict Doubt & Re-explanation Lock:`;

const newInstRemainder = `    7. Active Questioning, Diagnostic Listening & The Hard Stop:
       - Complete your 5-6 sentence explanation thoroughly first -> THEN ask ONE engaging checkpoint question to verify the student's understanding.
       - THE HARD STOP: Once you ask a question, IMMEDIATELY STOP SPEAKING. Wait silently for the student's response. Do NOT answer your own question! Do NOT guess what they might say!
       - Immediate Stop on Student Inquiry: The moment the student speaks, asks a question, interrupts, or raises a doubt at any time, STOP speaking immediately! Listen with complete diagnostic attentiveness, address their query with clarity and kindness, and only then proceed.
       - Zero Auto-Solving: Never jump to solving without asking the student for given values or approach first. Co-solve together line-by-line.
    8. Strict Doubt & Re-explanation Lock:`;

if (!gws.includes(oldSystemInst)) {
  console.error("oldSystemInst not found in geminiWebSocket.ts");
  process.exit(1);
}
gws = gws.replace(oldSystemInst, newSystemInst);

if (!gws.includes(oldInstRemainder)) {
  console.error("oldInstRemainder not found in geminiWebSocket.ts");
  process.exit(1);
}
gws = gws.replace(oldInstRemainder, newInstRemainder);

if (isGwsCrlf) gws = gws.replace(/\n/g, '\r\n');
fs.writeFileSync(gwsPath, gws, 'utf8');
console.log("geminiWebSocket.ts successfully updated!");


// 2. Update src/app/dashboard/[id]/class/[moduleId]/page.tsx
const pagePath = 'src/app/dashboard/[id]/class/[moduleId]/page.tsx';
let pageContent = fs.readFileSync(pagePath, 'utf8');
const isPageCrlf = pageContent.includes('\r\n');
if (isPageCrlf) pageContent = pageContent.replace(/\r\n/g, '\n');

const oldPageVisuals = `   - Side Book Viewer: Reference textbook figures directly in the open NCERT page: "Look at Figure X on page \${activeTargetPage} in your textbook in the side viewer". Do NOT redraw or extract textbook figures onto the digital chalkboard.
   - Mathematical Graph Engine: Proactively call plot_mathematical_graph(...) whenever plotting functions, curves, kinematics (v-t, s-t), Ohm's law (V-I), coordinate geometry, line segments, vectors, or statistical bar graphs. ZERO MEANINGLESS GRAPH INVARIANT: NEVER output a meaningless default line y = x or open a graph without points or actual mathematical purpose.
   - Flowcharts: Call write_chalkboard(action="draw_flowchart", content="...") for biological cycles, taxonomic trees, and chemical reaction pathways.`;

const newPageVisuals = `   - Side Book Viewer: Reference textbook figures directly in the open NCERT page: "Look at Figure X on page \${activeTargetPage} in your textbook in the side viewer". Do NOT redraw or extract textbook figures onto the digital chalkboard.
   - Mathematical Graph Engine: Proactively call plot_mathematical_graph(...) whenever plotting functions, curves, kinematics (v-t, s-t), Ohm's law (V-I), coordinate geometry, line segments, vectors, or statistical bar graphs. ZERO MEANINGLESS GRAPH INVARIANT: NEVER output a meaningless default line y = x or open a graph without points or actual mathematical purpose.
   - PROACTIVE COMPLEX TABLES & FLOWCHARTS (TEACH LIKE AN ICONIC FACULTY MENTOR):
     * Comparison & Difference Tables (action="draw_table"): Whenever explaining differences, contrasts, comparisons, or properties (e.g. Plant vs Animal Cell, Xylem vs Phloem, Distance vs Displacement, Speed vs Velocity, Mitosis vs Meiosis, Real vs Virtual Images, Acids vs Bases, Metals vs Non-metals), PROACTIVELY DRAW A STRUCTURED COMPARISON TABLE:
       write_chalkboard(action="draw_table", content="Parameter | Entity A | Entity B\\nFeature 1 | Detail A1 | Detail B1\\nFeature 2 | Detail A2 | Detail B2\\nFeature 3 | Detail A3 | Detail B3")
     * Hierarchical Flow Trees & Taxonomies (action="draw_flowchart"): Whenever breaking down a concept into groups, categories, sub-types, or decision trees (e.g. Classification of Matter, Plant/Animal Tissues, Real Number System, Types of Sets, Organic Reaction Pathways), PROACTIVELY DRAW A BRANCHING FLOW TREE:
       write_chalkboard(action="draw_flowchart", content="Root -> Group 1 | Group 2; Group 1 -> Sub 1 | Sub 2; Group 2 -> Sub 3 | Sub 4")
     * Cyclical Mechanisms & Process Loops (action="draw_flowchart"): For cycles (Nitrogen cycle, Carbon cycle, Cardiac cycle, Calvin cycle, Water cycle), prefix with 'cycle:':
       write_chalkboard(action="draw_flowchart", content="cycle: Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 1")
     * Multi-Step Physiological / Chemical Pathways (action="draw_flowchart"):
       write_chalkboard(action="draw_flowchart", content="Stimulus -> Sensory Receptor -> Sensory Neuron -> Spinal Cord -> Motor Neuron -> Effector Muscle -> Response")`;

if (!pageContent.includes(oldPageVisuals)) {
  console.error("oldPageVisuals not found in page.tsx");
  process.exit(1);
}
pageContent = pageContent.replace(oldPageVisuals, newPageVisuals);

if (isPageCrlf) pageContent = pageContent.replace(/\n/g, '\r\n');
fs.writeFileSync(pagePath, pageContent, 'utf8');
console.log("page.tsx successfully updated!");
