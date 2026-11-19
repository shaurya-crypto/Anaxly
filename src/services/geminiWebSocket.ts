import { GoogleGenAI, Type, Behavior, FunctionResponseScheduling, StartSensitivity, EndSensitivity } from '@google/genai';
import { cleanChalkboardTypography } from '../components/whiteboard/chalkboardTypography';
import { PedagogicalStateManager } from './pedagogicalStateManager';

export interface CustomizedAvatarConfig {
  imageData?: string;
  imageMimeType?: string;
}

export interface LiveAvatarConfig {
  avatarName?: string;
  customizedAvatar?: CustomizedAvatarConfig;
  audioBitrateBps?: number;
  videoBitrateBps?: number;
}

export interface GeminiLiveCallbacks {
  onSetupComplete: () => void;
  onAudioData: (pcmData: Int16Array, sampleRate: number) => void;
  onVideoData?: (data: string, mimeType: string) => void;
  onInterrupted: () => void;
  onTurnComplete: () => void;
  onTranscript: (text: string, sender: "user" | "teacher") => void;
  onError: (error: Error) => void;
  onClose: (event: CloseEvent) => void;
  onUserSpeechStart?: () => void;
  onChalkboardToolCall?: (action: string, content: any, color?: string) => void;
  onVisualAction?: (action: string, params: Record<string, any>) => void;
  onGetBoardContent?: () => string;
  onHighlightText?: (text: string, target?: string, color?: string) => void;
}

export class GeminiLiveClient {
  private ai: GoogleGenAI;
  private session: any | null = null;
  private pedagogicalStateManager: PedagogicalStateManager;
  private apiKey: string;
  private model: string;
  private voiceName: string;
  private supportedLanguages: string[];
  private languageCode: string;
  private thinkingLevel: string;
  private systemInstruction: string;
  private callbacks: GeminiLiveCallbacks;
  private isManuallyClosed: boolean = false;
  private isConnected: boolean = false;
  private hasSentKickoff: boolean = false;
  private pendingKickoffText: string | null = null;
  private enableFunctionCalling: boolean = false;
  private avatarConfig?: LiveAvatarConfig;
  private executedToolCallIds = new Set<string>();
  private lastExecutedToolCalls = new Map<string, number>();
  private pendingBoardContext: string | null = null;
  private isModelGenerating: boolean = false;
  private turnToolCallsExecuted: number = 0;
  private turnEmittedAudio: boolean = false;
  private lastExecutedToolAction: string | null = null;
  private silentTurnNudgeCount: number = 0;

  constructor(
    authTokenOrApiKey: string,
    callbacks: GeminiLiveCallbacks,
    options?: {
      model?: string;
      voiceName?: string;
      systemInstruction?: string;
      enableFunctionCalling?: boolean;
      avatarConfig?: LiveAvatarConfig;
      supportedLanguages?: string[];
      languageCode?: string;
      preferredLanguage?: string;
      thinkingLevel?: string;
      pedagogicalStateManager?: PedagogicalStateManager;
    }
  ) {
    this.apiKey = authTokenOrApiKey;
    this.callbacks = callbacks;
    this.pedagogicalStateManager = options?.pedagogicalStateManager || new PedagogicalStateManager();
    let model = options?.model || "gemini-3.8-live";
    if (model.startsWith("models/")) {
      model = model.replace("models/", "");
    }
    // Low latency invariant: Do NOT use gemini-3.8-live-extended; strictly keep gemini-3.8-live
    if (model.includes("extended-thinking")) {
      model = "gemini-3.8-live";
    }
    this.model = model;
    
    this.supportedLanguages =
      options?.supportedLanguages && options.supportedLanguages.length > 0
        ? options.supportedLanguages
        : ["en-IN", "hi-IN"];
    this.languageCode =
      options?.languageCode ||
      (options?.preferredLanguage?.toLowerCase().includes("hindi") ? "hi-IN" : "en-IN");
    
    // Dynamic voice adaptation
    this.voiceName = options?.voiceName || (this.languageCode === "hi-IN" ? "Fenrir" : "Leda");
    
    this.thinkingLevel = options?.thinkingLevel || "minimal";
    this.enableFunctionCalling = options?.enableFunctionCalling ?? false;
    this.avatarConfig = options?.avatarConfig;
    this.systemInstruction = options?.systemInstruction || `You are a friendly, expert tutor for Classes 6-12. 
    1. Language Style: ALWAYS use simple, colloquial Hinglish, Hindi, or English. NO heavy, complex, or academic words. Talk like a friendly local teacher; use conversational phrases like "samjhe," "dekho," "bilkul," "chalo" to make concepts clear.
    2. Socratic Cadence: Strictly enforce the 6-stage Socratic cycle: (1)Intuition, (2)Formulation, (3)Example, (4)Numerical, (5)Checkpoint, (6)Board-Exam Numerical.
    3. Progression: NEVER advance stages, concepts, or pages until the student confirms understanding or explicitly commands "next concept." Wait for student input at every stage.
    4. Chalkboard: Write step-by-step in "Topper Layout" (Given -> Formula -> Substitution -> Calculation -> Answer). Write 1 or at most 2 steps per line using textbook notation, NO code operators.
    STEP-BY-STEP PROBLEM SOLVING & HUMAN-UNDERSTANDABLE NUMERICAL LAYOUT:
    When presenting worked examples, solving numericals, or writing derivations on the chalkboard, you MUST ALWAYS follow the authentic CBSE/ICSE board-exam layout with ONE OR AT MOST TWO CONCISE STEPS PER LINE.
    Never dump multiple steps, entire derivations, or paragraphs into a single step or line. Every line must be short, clear, and easy to read:
    - Given line (e.g. Given: m = 2 kg, a = 5 m/s²)
    - Formula line (e.g. Formula: F = m × a)
    - Substitution line (e.g. Step 1: F = 2 kg × 5 m/s²)
    - Calculation line (e.g. Step 2: F = 10 N)
    - Boxed Answer line (e.g. Answer: Force F = 10 N)`;
    this.ai = new GoogleGenAI({
      apiKey: this.apiKey,
      httpOptions: { apiVersion: "v1alpha" },
    });
  }

  private extractAndExecuteEmbeddedToolCalls(rawText: string): string {
    if (!rawText) return rawText;

    // 1. Match pseudo-code: write_chalkboard(...) or write_board(action="...", content="...", color="...")
    const chalkboardRegex = /(?:write_chalkboard|write_chalkboardd|write_board|draw_board|chalkboard)\s*\(\s*(?:action\s*=\s*)?["']?([a-zA-Z0-9_\-]+)["']?\s*(?:,\s*(?:content\s*=\s*)?(?:["']([^"']*)["']|([^"',\)]*)))?(?:\s*,\s*(?:color\s*=\s*)?["']?([a-zA-Z0-9_#]+)["']?)?\s*\)/gi;
    let m;
    while ((m = chalkboardRegex.exec(rawText)) !== null) {
      const action = m[1]?.trim() || "";
      const content = (m[2] ?? m[3] ?? "").trim();
      const color = m[4]?.trim() || undefined;
      if (action) {
        this.handleSingleToolCall("write_chalkboard", { action, content, color });
      }
    }

    // 1a2. Match pseudo-code: highlight_text(...) or highlight_word(...)
    const highlightRegex = /(?:highlight_text|highlight_word|highlight_sentence)\s*\(\s*(?:(?:text|targetText|content)\s*=\s*)?(?:["']([^"']*)["']|([^"',\)]*))(?:\s*,\s*(?:target\s*=\s*)?["']?([a-zA-Z0-9_\-]+)["']?)?(?:\s*,\s*(?:color\s*=\s*)?["']?([a-zA-Z0-9_#]+)["']?)?\s*\)/gi;
    let hm;
    while ((hm = highlightRegex.exec(rawText)) !== null) {
      const text = (hm[1] ?? hm[2] ?? "").trim();
      const target = hm[3]?.trim() || "both";
      const color = hm[4]?.trim() || "amber";
      if (text) {
        this.handleSingleToolCall("highlight_text", { text, target, color });
      }
    }

    // 1b. Match bracket directives: [NOTE: ...], [STEP: ...], [DEFINITION: ...], [HIGHLIGHT: ...], etc.
    const bracketRegex = /\[(NOTE|INTUITION|INSIGHT|DEFINITION|LAW|FORMULA|HIGHLIGHT|HIGHLIGHT_WORD|HIGHLIGHT_SENTENCE|FOCUS_WORD|FOCUS_PHRASE|EXAMPLE|ILLUSTRATION|STEP|DERIVATION|CALCULATION|QUESTION|CHECKPOINT_QUESTION|BOARD_QUESTION|STUDENT_ANSWER|STUDENT|VERDICT|ANSWER_VERDICT|CORRECTION|CONCEPT_FOCUS|NUMERICAL|BOARD_NUMERICAL|WORKED_EXAMPLE|SOLVE|MATH_SOLVE):\s*([^\]]+)\]/gi;
    let bm;
    while ((bm = bracketRegex.exec(rawText)) !== null) {
      const type = bm[1]?.toUpperCase() || "";
      const content = bm[2]?.trim() || "";
      if (!content) continue;
      if (type === "NOTE" || type === "INTUITION" || type === "INSIGHT") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_note", content: type === "INTUITION" ? `Intuition: ${content}` : content, color: "botanical" });
      } else if (type === "HIGHLIGHT_WORD" || type === "HIGHLIGHT_SENTENCE" || type === "FOCUS_WORD" || type === "FOCUS_PHRASE") {
        this.handleSingleToolCall("highlight_text", { text: content, target: "both", color: "amber" });
      } else if (type === "HIGHLIGHT") {
        if (content.length <= 45) {
          this.handleSingleToolCall("highlight_text", { text: content, target: "both", color: "amber" });
        } else {
          this.handleSingleToolCall("write_chalkboardd", { action: "draw_highlight_box", content: content, color: "coral" });
        }
      } else if (type === "DEFINITION" || type === "LAW" || type === "FORMULA") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_highlight_box", content: content, color: "coral" });
      } else if (type === "EXAMPLE" || type === "ILLUSTRATION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_note", content: `Example: ${content}`, color: "blue" });
      } else if (type === "STEP" || type === "DERIVATION" || type === "CALCULATION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_step", content: content, color: "amber" });
      } else if (type === "QUESTION" || type === "CHECKPOINT_QUESTION" || type === "BOARD_QUESTION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_question", content: content, color: "amber" });
      } else if (type === "STUDENT_ANSWER" || type === "STUDENT") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_student_answer", content: content, color: "blue" });
      } else if (type === "VERDICT" || type === "ANSWER_VERDICT" || type === "CORRECTION") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_answer_verdict", content: content, color: "botanical" });
      } else if (type === "NUMERICAL" || type === "BOARD_NUMERICAL" || type === "WORKED_EXAMPLE" || type === "SOLVE" || type === "MATH_SOLVE") {
        this.handleSingleToolCall("write_chalkboardd", { action: "draw_numerical", content: content });
      } else if (type === "CONCEPT_FOCUS") {
        this.handleSingleToolCall("concept_focus", { conceptName: content });
      }
    }

    // 2. Match execute_visual_action(action="...", parameters={...})
    const visualRegex = /execute_visual_action\s*\(\s*(?:action\s*=\s*)?["']?([a-zA-Z0-9_\-]+)["']?\s*(?:,\s*(?:parameters\s*=\s*)?(\{.*?\})|\s*,\s*([^,\)]+))?\s*\)/gi;
    let vm;
    while ((vm = visualRegex.exec(rawText)) !== null) {
      const action = vm[1]?.trim() || "";
      let parameters: Record<string, any> = {};
      const rawParams = vm[2] || vm[3];
      if (rawParams) {
        try {
          parameters = JSON.parse(rawParams);
        } catch {
          // ignore parsing error
        }
      }
      if (action) {
        this.handleSingleToolCall("execute_visual_action", { action, parameters });
      }
    }

    // 3. Match draw_shape(...)
    const shapeRegex = /draw_shape\s*\(\s*([^()]+)\)/gi;
    let sm;
    while ((sm = shapeRegex.exec(rawText)) !== null) {
      const argStr = sm[1];
      try {
        if (argStr.trim().startsWith('{')) {
          this.handleSingleToolCall("draw_shape", JSON.parse(argStr.trim()));
        } else {
          this.handleSingleToolCall("draw_shape", { shape: argStr.trim() });
        }
      } catch {}
    }

    // 3b. Match plot_mathematical_graph(...)
    const graphRegex = /plot_mathematical_graph\s*\(([\s\S]*?)\)/gi;
    let gm;
    while ((gm = graphRegex.exec(rawText)) !== null) {
      const body = gm[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          this.handleSingleToolCall("plot_mathematical_graph", parsed);
        } catch {}
      } else {
        const explicitFormula = body.match(/\bformula\s*=\s*["']([^"']*)["']/i);
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitDomain = body.match(/\bdomain\s*=\s*["']([^"']*)["']/i);
        const explicitRange = body.match(/\brange\s*=\s*["']([^"']*)["']/i);
        const explicitCallout = body.match(/\bcallout\s*=\s*["']([^"']*)["']/i);
        const explicitPoints = body.match(/\bpoints\s*=\s*["']([^"']*)["']/i);
        const formula = explicitFormula ? explicitFormula[1] : body.split(',')[0]?.replace(/^["']|["']$/g, '').trim() || 'x';
        this.handleSingleToolCall("plot_mathematical_graph", {
          formula,
          title: explicitTitle ? explicitTitle[1] : undefined,
          domain: explicitDomain ? explicitDomain[1] : undefined,
          range: explicitRange ? explicitRange[1] : undefined,
          callout: explicitCallout ? explicitCallout[1] : undefined,
          points: explicitPoints ? explicitPoints[1] : undefined,
        });
      }
    }

    // 4. Match render_svg_diagram(...)
    const svgRegex = /render_svg_diagram\s*\(([\s\S]*?)\)/gi;
    let svgm;
    while ((svgm = svgRegex.exec(rawText)) !== null) {
      const body = svgm[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          if (parsed.title || parsed.svg || parsed.what) {
            this.handleSingleToolCall("render_svg_diagram", {
              title: parsed.title || "Educational Diagram",
              svg: parsed.svg || "",
              caption: parsed.caption || "",
              what: parsed.what || "",
            });
          }
        } catch {}
      } else {
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitSvg = body.match(/\bsvg\s*=\s*["']([\s\S]*?)["'](?:\s*,\s*[a-zA-Z_]+\s*=|\s*$)/i);
        const explicitCaption = body.match(/\bcaption\s*=\s*["']([^"']*)["']/i);
        const explicitWhat = body.match(/\bwhat\s*=\s*["']([^"']*)["']/i);
        if (explicitTitle || explicitSvg || explicitWhat) {
          const title = explicitTitle ? explicitTitle[1] : "Educational Diagram";
          const svg = explicitSvg ? explicitSvg[1] : "";
          const caption = explicitCaption ? explicitCaption[1] : "";
          const what = explicitWhat ? explicitWhat[1] : "";
          this.handleSingleToolCall("render_svg_diagram", { title, svg, caption, what });
        } else {
          const posMatch = body.match(/["']([^"']*)["'](?:\s*,\s*["']([\s\S]*?)["'])?(?:\s*,\s*["']([^"']*)["'])?/);
          if (posMatch && posMatch[1]) {
            this.handleSingleToolCall("render_svg_diagram", {
              title: posMatch[1],
              svg: posMatch[2] || "",
              caption: posMatch[3] || "",
            });
          }
        }
      }
    }

    // 4a2. Match search_and_show_image(...)
    const searchImgRegex = /search_and_show_image\s*\(([\s\S]*?)\)/gi;
    let sim;
    while ((sim = searchImgRegex.exec(rawText)) !== null) {
      const body = sim[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          this.handleSingleToolCall("search_and_show_image", parsed);
        } catch {}
      } else {
        const explicitQuery = body.match(/\bquery\s*=\s*["']([^"']*)["']/i);
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitCaption = body.match(/\bcaption\s*=\s*["']([^"']*)["']/i);
        const query = explicitQuery ? explicitQuery[1] : body.split(',')[0]?.replace(/^["']|["']$/g, '').trim() || '';
        const title = explicitTitle ? explicitTitle[1] : body.split(',')[1]?.replace(/^["']|["']$/g, '').trim() || query;
        const caption = explicitCaption ? explicitCaption[1] : body.split(',')[2]?.replace(/^["']|["']$/g, '').trim() || '';
        if (query) {
          this.handleSingleToolCall("search_and_show_image", { query, title, caption });
        }
      }
    }

    // 4a3. Match search_and_show_video(...)
    const searchVidRegex = /search_and_show_video\s*\(([\s\S]*?)\)/gi;
    let svm;
    while ((svm = searchVidRegex.exec(rawText)) !== null) {
      const body = svm[1]?.trim() || "";
      if (!body) continue;
      if (body.startsWith("{")) {
        try {
          const parsed = JSON.parse(body);
          this.handleSingleToolCall("search_and_show_video", parsed);
        } catch {}
      } else {
        const explicitQuery = body.match(/\bquery\s*=\s*["']([^"']*)["']/i);
        const explicitTitle = body.match(/\btitle\s*=\s*["']([^"']*)["']/i);
        const explicitDesc = body.match(/\b(?:description|caption)\s*=\s*["']([^"']*)["']/i);
        const query = explicitQuery ? explicitQuery[1] : body.split(',')[0]?.replace(/^["']|["']$/g, '').trim() || '';
        const title = explicitTitle ? explicitTitle[1] : body.split(',')[1]?.replace(/^["']|["']$/g, '').trim() || query;
        const description = explicitDesc ? explicitDesc[1] : body.split(',')[2]?.replace(/^["']|["']$/g, '').trim() || '';
        if (query) {
          this.handleSingleToolCall("search_and_show_video", { query, title, description });
        }
      }
    }


    // 4c. Match concept_focus(...)
    const conceptFocusRegex = /(?:concept_focus|focus_concept)\s*\(\s*(?:(?:conceptName|concept)\s*=\s*)?["']?([^"'\)]*)["']?\s*\)/gi;
    let cfm;
    while ((cfm = conceptFocusRegex.exec(rawText)) !== null) {
      const cName = cfm[1]?.trim() || "";
      this.handleSingleToolCall("concept_focus", { conceptName: cName });
    }

    // 5. Strip any leaked tool calls and bracket directives from spoken transcript text
    const stripCall = (name: string) => new RegExp(`${name}\\s*\\((?:'[^']*'|"[^"]*"|[^()]*|\\([^()]*\\))*\\)`, "gi");
    return rawText
      .replace(stripCall("write_chalkboardd"), "")
      .replace(stripCall("write_board"), "")
      .replace(stripCall("draw_board"), "")
      .replace(stripCall("chalkboard"), "")
      .replace(stripCall("execute_visual_action"), "")
      .replace(stripCall("plot_mathematical_graph"), "")
      .replace(stripCall("open_interactive_simulation"), "")
      .replace(stripCall("update_interactive_simulation"), "")
      .replace(stripCall("draw_shape"), "")
      .replace(stripCall("solve_step_by_step_numerical"), "")
      .replace(stripCall("conclude_and_open_quiz"), "")
      .replace(stripCall("concept_completed"), "")
      .replace(stripCall("concept_done"), "")
      .replace(stripCall("next_concept"), "")
      .replace(stripCall("advance_concept"), "")
      .replace(stripCall("concept_focus"), "")
      .replace(stripCall("focus_concept"), "")
      .replace(stripCall("highlight_text"), "")
      .replace(stripCall("highlight_word"), "")
      .replace(stripCall("highlight_sentence"), "")
      .replace(stripCall("render_svg_diagram"), "")
      .replace(/render_svg_diagram\s*\([\s\S]*?\)/gi, "")
      .replace(stripCall("search_and_show_image"), "")
      .replace(/search_and_show_image\s*\([\s\S]*?\)/gi, "")
      .replace(stripCall("search_and_show_video"), "")
      .replace(/search_and_show_video\s*\([\s\S]*?\)/gi, "")
      .replace(/\[[A-Z_]+(?::\s*[^\]]*)?\]/gi, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  private handleSingleToolCall(name: string, args: any, callId?: string): any {
    if (!this.pedagogicalStateManager.handleToolCall(name)) {
      return { result: "Progression blocked: finish current stage first" };
    }
    if (callId) {
      if (this.executedToolCallIds.has(callId)) {
        return;
      }
      this.executedToolCallIds.add(callId);
      if (this.executedToolCallIds.size > 200) {
        const first = this.executedToolCallIds.values().next().value;
        if (first) this.executedToolCallIds.delete(first);
      }
    }

    const argKey = typeof args === 'string' ? args : JSON.stringify(args);
    const callSignature = `${name}:${argKey}`;
    const now = Date.now();
    const lastTime = this.lastExecutedToolCalls.get(callSignature);
    if (lastTime && (now - lastTime) < 2500) {
      return;
    }
    this.lastExecutedToolCalls.set(callSignature, now);
    if (this.lastExecutedToolCalls.size > 200) {
      for (const [k, t] of this.lastExecutedToolCalls.entries()) {
        if (now - t > 60000) this.lastExecutedToolCalls.delete(k);
      }
    }
    this.lastExecutedToolAction = name;
    // Wrap callback execution in a microtask or setTimeout to ensure it's non-blocking
    setTimeout(() => {
        if (
          name === "write_chalkboard" ||
          name === "write_chalkboardd" ||
          name === "write_board" ||
          name === "chalkboard" ||
          name === "whiteboard" ||
          name === "draw_chalkboard" ||
          name === "draw_board"
        ) {
          let action = args.action || "";
          let textContent = args.content ?? args.text ?? args.note ?? args.step ?? args.title ?? args.question ?? "";
          let color = args.color || "";
    
          if (!action) {
            if (args.note) action = "draw_note";
            else if (args.step) action = "draw_step";
            else if (args.title) action = "draw_title";
            else if (args.question) { action = "draw_question"; textContent = args.question; }
            else if (args.highlight) { action = "draw_highlight_box"; textContent = args.highlight; }
            else if (args.formula) { action = "draw_step"; textContent = args.formula; }
            else {
              action = "draw_note";
              if (typeof args === "string") textContent = args;
            }
          }
          this.lastExecutedToolAction = action;
    
          if (typeof textContent === "string") {
            textContent = cleanChalkboardTypography(textContent);
          }
    
          if (action === "draw_numerical" || action === "numerical") {
            let numericalPayload: any = args.content !== undefined ? args.content : args;
            if (typeof numericalPayload === 'string') {
              try {
                const parsed = JSON.parse(numericalPayload);
                if (parsed && typeof parsed === 'object') {
                  numericalPayload = parsed;
                }
              } catch {
                // Keep as raw string (pipe-separated)
              }
            }
            this.callbacks.onChalkboardToolCall?.("draw_numerical", numericalPayload);
          } else if (action === "highlight_text" || action === "highlight_word" || action === "highlight_sentence") {
            this.callbacks.onHighlightText?.(textContent, "both", color || "amber");
          } else {
            this.callbacks.onChalkboardToolCall?.(action, textContent, color);
          }
        } else if (name === "highlight_text" || name === "highlight_word" || name === "highlight_sentence") {
          const textToHighlight = args.text || args.content || args.word || args.sentence || (typeof args === "string" ? args : "");
          const target = args.target || "both";
          const color = args.color || "amber";
          this.callbacks.onHighlightText?.(textToHighlight, target, color);
        } else if (name === "execute_visual_action") {
          const action = args.action || "";
          const parameters = args.parameters || {};
          this.callbacks.onVisualAction?.(action, parameters);
        } else if (name === "plot_mathematical_graph") {
          const formulasList = Array.isArray(args.formulas) ? args.formulas.join('; ') : '';
          const formulaStr = args.formula || formulasList || 'linear';
          const formatted = [
            formulaStr ? `formula=${formulaStr}` : '',
            formulasList ? `formulas=${formulasList}` : '',
            args.domain ? `domain=${typeof args.domain === 'string' ? args.domain : JSON.stringify(args.domain)}` : '',
            args.range ? `range=${typeof args.range === 'string' ? args.range : JSON.stringify(args.range)}` : '',
            args.title ? `title=${args.title}` : '',
            args.callout ? `callout=${args.callout}` : '',
            args.points ? `points=${typeof args.points === 'string' ? args.points : JSON.stringify(args.points)}` : '',
            args.slope ? `slope=true` : '',
            args.overwrite ? `overwrite=true` : '',
          ].filter(Boolean).join(' | ');
          this.callbacks.onChalkboardToolCall?.("draw_graph", formatted);
        } else if (name === "open_interactive_simulation") {
          const sceneType = args.sceneType || "geometry";
          const parameters = args.parameters || {};
          const title = args.title || parameters.title;
          this.callbacks.onVisualAction?.("SHOW_SCENE", { sceneType, title, ...parameters });
        } else if (name === "update_interactive_simulation") {
          const parameters = args.parameters || args;
          const title = args.title || parameters.title;
          this.callbacks.onVisualAction?.("UPDATE_SCENE", { title, ...parameters });
        } else if (name === "draw_shape") {
          this.callbacks.onChalkboardToolCall?.("draw_shape", args, args.color);
        } else if (name === "solve_step_by_step_numerical") {
          this.callbacks.onChalkboardToolCall?.("draw_numerical", args);
        } else if (name === "render_svg_diagram") {
          const title = args.title || "Educational Diagram";
          const svg = args.svg || "";
          const caption = args.caption || "";
          const what = args.what || "";
          this.callbacks.onChalkboardToolCall?.("render_svg_diagram", { title, svg, caption, what });
        } else if (name === "search_and_show_image") {
          const query = args.query || args.searchQuery || args.q || "";
          const title = args.title || query || "Scientific Diagram";
          const caption = args.caption || "";
          if (query && typeof window !== "undefined") {
            fetch("/api/diagram/search-image", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ query }),
            })
              .then((res) => res.json())
              .then(async (data) => {
                const candidateImages = data.images || [];
                let displayed = false;
                for (const img of candidateImages) {
                  if (!img?.url) continue;
                  try {
                    const check = await fetch(`/api/diagram/proxy?dataUrl=true&url=${encodeURIComponent(img.url)}`);
                    if (check.ok) {
                      const pData = await check.json();
                      if (pData.success && pData.dataURL) {
                        this.callbacks.onChalkboardToolCall?.("draw_image", {
                          url: pData.dataURL,
                          title: title || img.title,
                          caption: caption || img.description || "",
                        });
                        displayed = true;
                        break;
                      }
                    }
                  } catch {
                    // Failover to next candidate image
                  }
                }
                if (!displayed) {
                  // Only fall back to SVG diagram if all online image search candidates fail
                  this.callbacks.onChalkboardToolCall?.("render_svg_diagram", {
                    title,
                    caption,
                  });
                }
              })
              .catch((err) => {
                console.warn("[GeminiLive] search_and_show_image error:", err);
                this.callbacks.onChalkboardToolCall?.("render_svg_diagram", {
                  title,
                  caption,
                });
              });
          }
        } else if (name === "search_and_show_video") {
          const query = args.query || args.searchQuery || args.q || "";
          const title = args.title || query || "Demonstration Video";
          const description = args.description || args.caption || "";
          if (query && typeof window !== "undefined") {
            fetch("/api/diagram/search-video", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ query }),
            })
              .then((res) => res.json())
              .then((data) => {
                const firstVid = data.videos?.[0];
                if (firstVid?.url) {
                  this.callbacks.onChalkboardToolCall?.("draw_video", {
                    url: firstVid.url,
                    title: title || firstVid.title,
                    description: description || firstVid.description || "",
                    mimeType: firstVid.mimeType || "video/mp4",
                  });
                } else {
                  this.callbacks.onChalkboardToolCall?.("draw_video", {
                    url: "",
                    title,
                    description,
                  });
                }
              })
              .catch((err) => {
                console.warn("[GeminiLive] search_and_show_video error:", err);
                this.callbacks.onChalkboardToolCall?.("draw_video", {
                  url: "",
                  title,
                  description,
                });
              });
          }
        } else if (name === "conclude_and_open_quiz") {
          if (args.summary) {
            this.callbacks.onChalkboardToolCall?.("chapter_summary", args.summary);
          }
          this.callbacks.onChalkboardToolCall?.("open_quiz", args.summary || "10-MCQ Diagnostic Evaluation");
        } else if (name === "get_board_content" || name === "read_board_content" || name === "get_board_state") {
          const boardState = this.callbacks.onGetBoardContent?.() || "";
          return {
            result: "ok",
            chalkboard_content: boardState || "Digital chalkboard is active. No notes written yet.",
          };
        } else if (name === "close_graph" || ((name === "write_chalkboard" || name === "write_chalkboardd") && args?.action === "close_graph")) {
          this.callbacks.onChalkboardToolCall?.("close_graph", "");
        } else if (name === "concept_completed" || name === "next_concept" || name === "advance_concept") {
          const cName = args.conceptName || args.concept || (typeof args === "string" ? args : "");
          this.callbacks.onChalkboardToolCall?.("concept_done", cName);
        } else if (name === "concept_focus" || name === "focus_concept") {
          const cName = args.conceptName || args.concept || (typeof args === "string" ? args : "");
          this.callbacks.onChalkboardToolCall?.("concept_focus", cName);
        } else {
          this.callbacks.onChalkboardToolCall?.(name, typeof args === 'string' ? args : JSON.stringify(args));
        }
    }, 0);
  }

  public async connect(kickoffPrompt?: string): Promise<void> {
    if (this.session) return;
    this.isManuallyClosed = false;
    this.hasSentKickoff = false;
    if (kickoffPrompt) {
      this.pendingKickoffText = kickoffPrompt;
    }

    try {
      console.log(`[GeminiLive] Connecting session with model: ${this.model}, voice: ${this.voiceName}, enableFunctionCalling: ${this.enableFunctionCalling}`);

      const responseModalities = this.avatarConfig
        ? ["VIDEO" as any, "AUDIO" as any]
        : ["AUDIO" as any];

      const liveConfig: any = {
        responseModalities,
        systemInstruction: { parts: [{ text: this.systemInstruction }] },
        realtimeInputConfig: {
          automaticActivityDetection: {
            disabled: false,
            startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_HIGH,
            endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_HIGH,
            prefixPaddingMs: 40,
            silenceDurationMs: 2500,
          },
        },
        contextWindowCompression: {
          slidingWindow: {},
        },
        speechConfig: {
          voiceConfig: {
            prebuiltVoiceConfig: {
              voiceName: this.voiceName,
            },
          },
        },
        inputAudioTranscription: {
          languageCodes: this.supportedLanguages,
        },
        outputAudioTranscription: {
          languageCodes: this.supportedLanguages,
        },
      };

      if (this.avatarConfig) {
        liveConfig.avatarConfig = this.avatarConfig;
      }

      if (this.model.includes("extended-thinking")) {
        liveConfig.thinkingConfig = {
          thinkingLevel: this.thinkingLevel || "minimal",
        };
      }

      if (this.enableFunctionCalling) {
        liveConfig.tools = [
          {
            functionDeclarations: [
              {
                name: "write_chalkboard",
                description: "MANDATORY CHALKBOARD TOOL: You MUST invoke this tool in EVERY spoken turn to write notes, definitions, steps, formulas, worked examples, and questions on the student's live chalkboard. Speaking without calling this tool is strictly prohibited. For mathematics and physics problem solving, write cleanly with 1 or at most 2 steps per line in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    action: {
                      type: Type.STRING,
                      enum: [
                        "draw_title",
                        "draw_note",
                        "draw_step",
                        "draw_highlight_box",
                        "draw_question",
                        "draw_answer_verdict",
                        "draw_exam_question",
                        "draw_flowchart",
                        "draw_table",
                        "draw_numerical",
                        "concept_focus",
                        "concept_done",
                        "close_graph",
                        "set_color",
                        "new_page",
                      ],
                      description: "The chalkboard action to perform (e.g. draw_note, draw_step, draw_highlight_box, draw_question, draw_answer_verdict, draw_exam_question, draw_flowchart, draw_table, draw_numerical, close_graph, concept_focus, concept_done, set_color, new_page)",
                    },
                    content: {
                      type: Type.STRING,
                      description: "The text to write, equation, table markup, flowchart text, or color name to apply to the chalkboard. For problem solving or derivations, format with 1 or max 2 steps per line (separated by newlines or semicolons) in standard topper layout (Given -> Formula -> Substitution -> Calculation -> Boxed Answer).",
                    },
                    color: {
                      type: Type.STRING,
                      enum: [
                        "white",
                        "primary",
                        "botanical",
                        "green",
                        "coral",
                        "red",
                        "amber",
                        "yellow",
                        "blue",
                        "cyan",
                        "purple",
                        "lavender",
                        "rose",
                      ],
                      description: "Optional chalk color to write with (botanical, coral, amber, blue, purple, white). Use botanical/green for biology/definitions, coral/red for laws & boxed formulas, blue for physics/derivations, amber/yellow for SI units/highlights, purple for terms, white for standard text.",
                    },
                  },
                  required: ["action"],
                },
              },
              {
                name: "close_graph",
                description: "Dismiss or close the currently active interactive mathematical or physics graph on the student's whiteboard.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {},
                },
              },
              {
                name: "highlight_text",
                description: "LIVE AI HIGHLIGHTER: Temporarily highlight key words, terms, laws, formulas, or sentences on the student's chalkboard notes and/or live spoken subtitle streamer with an animated golden/amber glow pill marker. Call this dynamically while speaking to direct the student's visual focus to critical terms, exam keywords, or specific derivations.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    text: {
                      type: Type.STRING,
                      description: "The specific word, phrase, key term, or sentence to highlight (e.g. 'Photosynthesis', 'F = ma', 'Cellulose microfibrils', 'SI unit: Newton').",
                    },
                    target: {
                      type: Type.STRING,
                      enum: ["both", "chalkboard", "subtitles"],
                      description: "Where to render the highlight: 'both' (default), 'chalkboard' (marks text on the digital board), or 'subtitles' (glows in the live speech streamer).",
                    },
                    color: {
                      type: Type.STRING,
                      enum: ["amber", "yellow", "cyan", "botanical", "coral"],
                      description: "Chalk marker color: 'amber' (default golden marker), 'yellow', 'cyan', 'botanical', 'coral'.",
                    },
                  },
                  required: ["text"],
                },
              },
              {
                name: "plot_mathematical_graph",
                description: "CRITICAL GRAPH GATING: Plot an interactive mathematical function or physics kinematic/dynamic curve directly on the whiteboard canvas (e.g. quadratic parabola, calculus derivative, trigonometric curve, kinematics velocity-time or distance-time curve) whenever a visual curve or coordinate graph aids understanding with actual mathematical coordinates AND WORKED CALCULATIONS (roots, intercepts, vertex, slope, or table of values). Seamlessly supports both Mathematics and Physics. NEVER call this tool for non-mathematical topics (Biology, Anatomy, Histology, Chemical Bonding, Tissue Structures, Literature, History) — use render_svg_diagram or draw_flowchart instead. Call close_graph or write_chalkboard(action='close_graph') when moving on.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    formula: {
                      type: Type.STRING,
                      description: "The mathematical formula to plot, e.g. 'x^2 - 4' or '2x + 1' or 'velocity-time' or 'sin(x)'",
                    },
                    domain: {
                      type: Type.STRING,
                      description: "Domain range for x-axis, e.g. '[-5, 5]'",
                    },
                    range: {
                      type: Type.STRING,
                      description: "Range for y-axis, e.g. '[-10, 10]'",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Graph title, e.g. 'Quadratic Parabola: y = x^2 - 4'",
                    },
                    callout: {
                      type: Type.STRING,
                      description: "Key features or annotations, e.g. 'Roots at x = -2, 2 | Minimum at (0, -4)'",
                    },
                    points: {
                      type: Type.STRING,
                      description: "Critical coordinate points to highlight, e.g. '(0, -4), (2, 0), (-2, 0)'",
                    },
                    formulas: {
                      type: Type.ARRAY,
                      items: { type: Type.STRING },
                      description: "Optional list of multiple formulas for comparative multi-curve graphs (e.g. ['2x + 1', '-x + 4']).",
                    },
                    slope: {
                      type: Type.BOOLEAN,
                      description: "Whether to render a slope triangle (Delta y / Delta x) displaying rate of change or velocity.",
                    },
                    overwrite: {
                      type: Type.BOOLEAN,
                      description: "Set to true to overwrite/update the existing graph on the current page instead of adding another.",
                    },
                  },
                  required: ["formula"],
                },
              },
              {
                name: "render_svg_diagram",
                description: "MANDATORY PROACTIVE CHALKBOARD DIAGRAM TOOL: Call this tool proactively on Step 1 of EACH concept to render a clean, high-precision 3D axonometric Hairline vector SVG educational diagram directly on the chalkboard. For all physical apparatus, optics, circuits, and 3D geometry, render 30Â° isometric projection with rounded wireframe solids, leader callouts, and clean white background. The student will NOT ask you for a diagram â€” you MUST draw it automatically on cue. Provide concise title (e.g. 'Plant Cell Wall', 'Reflection of Light', 'Simple Circuit'). You may optionally supply svg markup; if omitted, the high-precision vector diagram is rendered automatically.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    title: {
                      type: Type.STRING,
                      description: "Concise academic title of the diagram (e.g. 'Plant Cell Wall & Cellulose Microfibrils', 'Reflection of Light at Plane Mirror', 'Simple Resistor-Battery Circuit')",
                    },
                    what: {
                      type: Type.STRING,
                      description: "Detailed specification of anatomical parts, components, arrows, coordinate axes, and labels to draw.",
                    },
                    svg: {
                      type: Type.STRING,
                      description: "Optional complete, well-formed XML <svg> element with xmlns='http://www.w3.org/2000/svg'. If omitted, an authentic vector diagram is automatically generated and rendered.",
                    },
                    caption: {
                      type: Type.STRING,
                      description: "1-2 sentence pedagogical explanation or key takeaway highlighting the governing law or anatomical feature.",
                    },
                  },
                  required: ["title"],
                },
              },
              {
                name: "draw_shape",
                description: "Draw custom 2D or 3D geometric shapes (rectangle, square, circle, ellipse, triangle, right_triangle, cylinder, cube, polygon, line, arrow) on the whiteboard with complete control over width, height, radius, labels, and colors.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    shape: {
                      type: Type.STRING,
                      enum: [
                        "rectangle",
                        "square",
                        "circle",
                        "ellipse",
                        "triangle",
                        "right_triangle",
                        "cylinder",
                        "cube",
                        "cuboid",
                        "polygon",
                        "line",
                        "arrow",
                      ],
                      description: "The geometric shape to draw",
                    },
                    width: {
                      type: Type.NUMBER,
                      description: "Width in pixels (e.g. 80 to 720)",
                    },
                    height: {
                      type: Type.NUMBER,
                      description: "Height in pixels (e.g. 40 to 450)",
                    },
                    radius: {
                      type: Type.NUMBER,
                      description: "Radius in pixels for circle or cylinder (e.g. 30 to 200)",
                    },
                    label: {
                      type: Type.STRING,
                      description: "Educational formula, dimension callout, or label (e.g. 'Length = 30cm, Breadth = 15cm | Area = 450cmÂ²')",
                    },
                    values: {
                      type: Type.OBJECT,
                      description: "Custom dimension and angle values to display on the figure (e.g. { length: '12 cm', breadth: '5 cm', hypotenuse: '13 cm', angleA: '60Â°' }). Use standard school units (cm, m, Â°), NEVER pixels.",
                    },
                    overwrite: {
                      type: Type.BOOLEAN,
                      description: "Set to true to overwrite and update the existing shape on the current page instead of adding a new one below.",
                    },
                    color: {
                      type: Type.STRING,
                      enum: [
                        "botanical",
                        "coral",
                        "blue",
                        "amber",
                        "purple",
                        "white",
                      ],
                      description: "Chalk stroke color",
                    },
                    fillColor: {
                      type: Type.STRING,
                      description: "Optional background fill color",
                    },
                  },
                  required: ["shape"],
                },
              },
              {
                name: "open_interactive_simulation",
                description: "Summon an interactive 3D WebGL geometry solid or cross-section model directly on the whiteboard stage with full control over title, shape, and dimensions.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    sceneType: {
                      type: Type.STRING,
                      enum: [
                        "geometry_3d",
                        "geometry_cross_section",
                      ],
                      description: "The 3D geometric simulation scene to open ('geometry_3d' for 3D solids or 'geometry_cross_section' for cutting plane slices)",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Custom title for the 3D model simulation",
                    },
                    parameters: {
                      type: Type.OBJECT,
                      description: "Dynamic simulation parameters and values (e.g. { shape: 'cylinder', radius: 4, height: 8 })",
                    },
                  },
                  required: ["sceneType"],
                },
              },
              {
                name: "update_interactive_simulation",
                description: "Update values, variables, sliders, or title of the currently active 3D simulation scene in real time (e.g. adjust shape, change radius or height, alter slice angle).",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    title: {
                      type: Type.STRING,
                      description: "Updated title for the simulation",
                    },
                    parameters: {
                      type: Type.OBJECT,
                      description: "Updated parameters and values to apply to the 3D model",
                    },
                  },
                },
              },
              {
                name: "conclude_and_open_quiz",
                description: "Conclude the teaching capsule, write the comprehensive chapter synthesis summary on the whiteboard, and prompt the student to open the 10-MCQ evaluation quiz. Call ONLY when ALL concepts in the capsule key concepts roadmap have been fully taught and mastered. NEVER call mid-lesson.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    summary: {
                      type: Type.STRING,
                      description: "The chapter synthesis summary covering all key definitions, formulas, and laws taught",
                    },
                  },
                  required: ["summary"],
                },
              },
              {
                name: "concept_completed",
                description: "CONCEPT ADVANCEMENT TOOL: Call this tool ONLY after the student has successfully solved the Stage 5/6 checkpoint question on the current concept, OR if the student explicitly commands 'next concept' or 'next page'. STRICT FORBIDDEN RULE: NEVER call this tool during Stages 1 to 4 (Intuition, Formulation, Worked Application, Board Numerical), and NEVER call it on conversational affirmations ('yes', 'ok', 'haan', 'understood') during initial explanations, and NEVER call it when the student asks a question or has a doubt! Advancing to the next concept unlocks a clean chalkboard page for the new concept.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    conceptName: {
                      type: Type.STRING,
                      description: "The name of the concept that was just mastered.",
                    },
                  },
                  required: ["conceptName"],
                },
              },
              {
                name: "search_and_show_image",
                description: "Search the web for an authentic, high-resolution scientific educational diagram, electron micrograph, real apparatus, or histology slide and display it directly on the student's chalkboard. Use proactively when teaching structural concepts or when the student hesitates, is confused, or requests to see another picture or real-life view.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    query: {
                      type: Type.STRING,
                      description: "Mandatory fully-detailed, specific educational search query. NEVER use vague 1-word terms like 'circuit' or 'cell'. Specify the exact system and components (e.g. for circuits: 'series electric circuit diagram with battery cells, closed plug key switch, ammeter in series, resistors in series, and direction of electric current'; for biology/optics: 'human eye labeled anatomy diagram showing cornea, iris, lens, retina, and optic nerve').",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Title for the chalkboard image card",
                    },
                    caption: {
                      type: Type.STRING,
                      description: "Key educational note or legend",
                    },
                  },
                  required: ["query", "title"],
                },
              },
              {
                name: "search_and_show_video",
                description: "Search for and display an educational demonstration video or experimental animation directly on the student's chalkboard. Use proactively when teaching physical motion, dynamic biological processes, laboratory apparatus experiments, or when the student asks for a video demonstration.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {
                    query: {
                      type: Type.STRING,
                      description: "Mandatory fully-detailed educational experiment or demonstration video search query (e.g. 'series electric circuit connection with battery bulb and ammeter laboratory experiment demonstration' or 'verification of Ohm's law physics laboratory experiment demonstration' or 'vibrating rubber band producing sound experiment demonstration').",
                    },
                    title: {
                      type: Type.STRING,
                      description: "Title for the demonstration video card",
                    },
                    description: {
                      type: Type.STRING,
                      description: "Brief 1-line educational description of what the video demonstrates",
                    },
                  },
                  required: ["query", "title"],
                },
              },
              {
                name: "get_board_content",
                description: "Inspect and read the current digital chalkboard contents, including all notes, definitions, formulas, student responses, answer verdicts, and rough work scratchpad currently visible on the board. Call this whenever the student asks about what is on the board, refers to board content, or before writing new notes to avoid duplication.",
                behavior: Behavior.NON_BLOCKING,
                parameters: {
                  type: Type.OBJECT,
                  properties: {},
                },
              },
            ],
          },
        ];
      }

      const sessionCallbacks = {
        onopen: () => {
          console.log("[GeminiLive] WebSocket TCP connection open; awaiting setupComplete...");
        },
        onmessage: (msg: any) => {
           const content = msg.serverContent;
           
           // Server Voice Activity Detection (VAD) events
           const isVoiceActivityStart = msg.voiceActivity?.voiceActivityType === "ACTIVITY_START" || msg.voiceActivity?.type === "ACTIVITY_START";
           if (isVoiceActivityStart) {
              this.callbacks.onUserSpeechStart?.();
           }

           // Handle root tool calls for chalkboard writing, visual stage, and dedicated tools
           if (msg.toolCall && msg.toolCall.functionCalls) {
             const responses: any[] = [];
             const isExtendedThinking = this.model.includes("extended-thinking");
             for (const call of msg.toolCall.functionCalls) {
               if (!call.id || this.executedToolCallIds.has(call.id)) {
                 continue;
               }
               const allowed = this.pedagogicalStateManager.handleToolCall(call.name, call.args);
               let toolResult: any;
               if (!allowed) {
                 toolResult = { result: "Progression blocked: complete checkpoint first" };
               } else {
                 toolResult = this.handleSingleToolCall(call.name, call.args || {}, call.id);
               }
               const responsePayload = (toolResult && typeof toolResult === 'object') ? toolResult : { result: "ok" };
               const isQuestionTool = (
                 (call.name === 'write_chalkboard' || call.name === 'write_chalkboardd') &&
                 (call.args?.action === 'draw_question' || call.args?.action === 'draw_exam_question')
               ) || call.name === 'draw_question' || call.name === 'draw_exam_question';

               const fnResponse: any = {
                  id: call.id,
                  name: call.name,
                  response: {
                    ...responsePayload,
                    scheduling: isQuestionTool
                      ? FunctionResponseScheduling.SILENT
                      : (!isExtendedThinking ? FunctionResponseScheduling.WHEN_IDLE : undefined)
                  },
               };
               responses.push(fnResponse);
             }
             if (responses.length > 0 && this.session) {
               try {
                 this.session.sendToolResponse({ functionResponses: responses });
               } catch (e) {
                 console.warn("[GeminiLive] Failed to send tool response:", e);
               }
             }
           }

           if (!content) return;

           if (content.interrupted) {
             this.isModelGenerating = false;
             this.turnToolCallsExecuted = 0;
             this.turnEmittedAudio = false;
             this.silentTurnNudgeCount = 0;
             this.pendingBoardContext = null;
             this.callbacks.onInterrupted();
             return;
           }
           
           // Transcripts extraction
           if (content.inputTranscription && content.inputTranscription.text) {
             this.callbacks.onTranscript(content.inputTranscription.text, "user");
           }
           if (content.inputTranscription && content.inputTranscription.parts) {
             for (const part of content.inputTranscription.parts) {
                 if (part.text) {
                     this.callbacks.onTranscript(part.text, "user");
                 }
             }
           }
           
           let hasTeacherTranscript = false;
           if (content.outputTranscription && content.outputTranscription.text) {
             const cleaned = this.extractAndExecuteEmbeddedToolCalls(content.outputTranscription.text);
              if (cleaned) this.callbacks.onTranscript(cleaned, "teacher");
             hasTeacherTranscript = true;
           } else if (content.outputTranscription && content.outputTranscription.parts) {
             for (const part of content.outputTranscription.parts) {
               if (part.text) {
                 const cleaned = this.extractAndExecuteEmbeddedToolCalls(part.text);
                 if (cleaned) {
                   this.callbacks.onTranscript(cleaned, "teacher");
                   hasTeacherTranscript = true;
                 }
               }
             }
           }

           // Incoming audio, video frames, or text model turns
           if (content.modelTurn && content.modelTurn.parts) {
             this.isModelGenerating = true;
             for (const part of content.modelTurn.parts) {
               if (part.inlineData && part.inlineData.data) {
                 this.turnEmittedAudio = true;
                 this.silentTurnNudgeCount = 0;
                 const mime = part.inlineData.mimeType || "audio/pcm;rate=24000";
                 if (mime.startsWith("video/") || mime.startsWith("image/")) {
                   // Native Gemini 3.8 Live Avatar video frame streaming
                   this.callbacks.onVideoData?.(part.inlineData.data, mime);
                 } else {
                   const pcm16 = this.base64ToInt16(part.inlineData.data);
                   this.callbacks.onAudioData(pcm16, 24000); // SDK returns 24kHz
                 }
               }
               // Deliver model turn text if it contains chalkboard bracket tags or if no audio transcript was emitted
               if (part.text) {
                 const cleaned = this.extractAndExecuteEmbeddedToolCalls(part.text);
                 if (cleaned && (part.text.includes("[") || part.text.includes("write_chalkboard") || part.text.includes("write_chalkboardd") || !hasTeacherTranscript)) {
                   this.callbacks.onTranscript(cleaned, "teacher");
                 }
               }
               if (part.functionCall) {
                 const call = part.functionCall;
                 if (call.id && !this.executedToolCallIds.has(call.id)) {
                   this.turnToolCallsExecuted++;
                   const allowed = this.pedagogicalStateManager.handleToolCall(call.name, call.args);
                   let toolResult: any;
                   if (!allowed) {
                     toolResult = { result: "Progression blocked: complete checkpoint first" };
                   } else {
                     toolResult = this.handleSingleToolCall(call.name, call.args || {}, call.id);
                   }
                   const isExtendedThinking = this.model.includes("extended-thinking");
                   const responsePayload = (toolResult && typeof toolResult === 'object') ? toolResult : { result: "ok" };
                   const isQuestionTool = (
                     (call.name === 'write_chalkboard' || call.name === 'write_chalkboardd') &&
                     (call.args?.action === 'draw_question' || call.args?.action === 'draw_exam_question')
                   ) || call.name === 'draw_question' || call.name === 'draw_exam_question';

                   const fnResponse: any = {
                     id: call.id,
                     name: call.name,
                     response: {
                       ...responsePayload,
                       scheduling: isQuestionTool
                         ? FunctionResponseScheduling.SILENT
                         : (!isExtendedThinking ? FunctionResponseScheduling.WHEN_IDLE : undefined)
                     },
                   };

                   try {
                     this.session?.sendToolResponse({
                       functionResponses: [fnResponse],
                     });
                   } catch (e) {
                     console.warn(`[GeminiLive] Failed to send tool response for ${call.name}:`, e);
                   }
                 }
               }
             }
           }

           const currentStatus = content.interactionStatus || msg.interactionStatus;
           const isTurnDone = Boolean(content.turnComplete || currentStatus === "IDLE");
           if (isTurnDone && currentStatus !== "IN_PROGRESS") {
             this.isModelGenerating = false;
             if (this.turnToolCallsExecuted > 0 && !this.turnEmittedAudio && this.isConnected && !this.isManuallyClosed && this.silentTurnNudgeCount < 2) {
               this.silentTurnNudgeCount++;
               const isQuestionTool = this.lastExecutedToolAction === "draw_question" || this.lastExecutedToolAction === "draw_exam_question";
               const nudgePrompt = isQuestionTool
                 ? "Please read the question out loud to the student, then stop speaking and wait silently for their answer. Do NOT reveal or solve the question!"
                 : "Please continue speaking and explaining out loud now.";
               console.log(`[GeminiLive] Turn ended with chalkboard tool calls (${this.lastExecutedToolAction}) but zero audio. Prompting spoken delivery automatically...`);
               try {
                 this.session?.sendClientContent({
                   turns: [{ role: "user", parts: [{ text: nudgePrompt }] }],
                   turnComplete: true,
                 });
               } catch {}
             }
             this.turnToolCallsExecuted = 0;
             this.turnEmittedAudio = false;
             this.callbacks.onTurnComplete();
             this.pendingBoardContext = null;
           }
        },
        onerror: (err: any) => {
          if (!this.isManuallyClosed) {
            console.error("[GeminiLive] Connection error:", err);
            this.callbacks.onError(new Error(err.message || "Connection to Gemini Live was interrupted."));
          }
        },
        onclose: (event: any) => {
          this.isConnected = false;
          this.hasSentKickoff = false;
          console.log(`[GeminiLive] WebSocket closed: code=${event?.code}, reason=${event?.reason || '(none)'}, wasClean=${event?.wasClean}`);
          if (!this.isManuallyClosed) {
             this.callbacks.onClose(event as CloseEvent);
          }
          this.session = null;
        }
      };

      try {
        this.session = await this.ai.live.connect({
          model: this.model,
          config: liveConfig,
          callbacks: sessionCallbacks,
        });
        // Generic kickoff removed. The session will now await the user-provided dynamic kickoff.
        if (!this.hasSentKickoff) {
          // No hardcoded greeting.
        }
      } catch (connectError: any) {
        if (this.model.includes("extended-thinking")) {
          console.warn("[GeminiLive] Extended thinking live model unavailable or rejected. Self-healing fallback to standard gemini-3.8-live:", connectError);
          this.model = "gemini-3.8-live";
          delete liveConfig.thinkingConfig;
          try {
            this.session = await this.ai.live.connect({
              model: this.model,
              config: liveConfig,
              callbacks: sessionCallbacks,
            });
          } catch (retryError: any) {
            if (this.avatarConfig) {
              console.warn("[GeminiLive] Native video avatar modality rejected. Fallback to audio stream:", retryError);
              this.avatarConfig = undefined;
              liveConfig.responseModalities = ["AUDIO" as any];
              delete liveConfig.avatarConfig;
              this.session = await this.ai.live.connect({
                model: this.model,
                config: liveConfig,
                callbacks: sessionCallbacks,
              });
            } else {
              throw retryError;
            }
          }
        } else if (this.avatarConfig) {
          console.warn("[GeminiLive] Native video avatar modality rejected or unsupported by current endpoint/credentials. Self-healing fallback to high-fidelity audio stream:", connectError);
          this.avatarConfig = undefined;
          liveConfig.responseModalities = ["AUDIO" as any];
          delete liveConfig.avatarConfig;
          this.session = await this.ai.live.connect({
            model: this.model,
            config: liveConfig,
            callbacks: sessionCallbacks,
          });
        } else {
          throw connectError;
        }
      }

      this.isConnected = true;
      console.log("[GeminiLive] Handshake verified and session ready.");
      this.callbacks.onSetupComplete();

      if (this.pendingKickoffText && !this.hasSentKickoff) {
        setTimeout(() => this.sendKickoff(this.pendingKickoffText!), 500);
      }
    } catch (err: any) {
      console.error("[GeminiLive] Connection error during setup:", err);
      this.callbacks.onError(new Error(`Connection failed: ${err.message}`));
    }
  }

  public sendKickoff(text: string): void {
    if (this.hasSentKickoff) {
      console.log("[GeminiLive] Kickoff already dispatched, ignoring repeat.");
      return;
    }
    if (!this.session) {
      console.log("[GeminiLive] Queued kickoff prompt while session connects.");
      this.pendingKickoffText = text;
      return;
    }
    // Proactive Greeting and Topic Writing
    const topicHeading = text.includes('Topic:')
      ? text.split('Topic:')[1]?.split('\n')[0]?.trim()
      : text.split(':')[0]?.replace(/^\[.*?\]/, '').trim() || 'Learning Session';
    this.handleSingleToolCall("write_chalkboard", { action: "draw_title", content: `Topic: ${topicHeading}` });

    // Use sendClientContent with a user-role turn to trigger the model to respond with audio speech.
    // If text already contains full kickoff instructions (from page.tsx), use it directly.
    const kickoffInstruction = (text.includes('[SESSION START') || text.includes('Speak FIRST'))
      ? text
      : `The student has just joined the class. The topic is: ${text}. Begin the class NOW by warmly greeting the student and immediately starting to teach. You MUST speak your greeting and explanation aloud (produce audio) AND write key points on the chalkboard simultaneously. Start speaking immediately.`;

    try {
      this.session.sendClientContent({
        turns: [{ role: "user", parts: [{ text: kickoffInstruction }] }],
        turnComplete: true,
      });
      console.log("[GeminiLive] Kickoff instruction dispatched via sendClientContent.");
    } catch (err) {
      console.error("[GeminiLive] Failed to send kickoff via sendClientContent:", err);
      // Fallback: try sendRealtimeInput with text
      try {
        this.session.sendRealtimeInput({ text: kickoffInstruction });
        console.log("[GeminiLive] Kickoff fallback dispatched via sendRealtimeInput.");
      } catch (fallbackErr) {
        console.error("[GeminiLive] Failed to send kickoff via sendRealtimeInput:", fallbackErr);
      }
    }
    this.hasSentKickoff = true;
  }

  private lastSentBoardContextHash: string = '';
  private latestBoardState: string = '';

  public sendTextMessage(text: string): void {
    if (!this.session || !text?.trim()) return;
    try {
      let messageToSend = text.trim();
      const currentStage = this.pedagogicalStateManager?.getStage?.() || 'REAL_LIFE_INTUITION';
      if (!messageToSend.includes('[TEACHING STATE') && !messageToSend.includes('[SESSION START')) {
        messageToSend = `[TEACHING STATE: Stage = ${currentStage}]\n${messageToSend}`;
      }
      if (
        this.latestBoardState &&
        !messageToSend.includes('[CURRENT_BOARD_STATE]') &&
        this.lastSentBoardContextHash !== this.latestBoardState
      ) {
        this.lastSentBoardContextHash = this.latestBoardState;
        messageToSend = `[CURRENT_BOARD_STATE]\n${this.latestBoardState}\n[CONTINUATION MANDATE: The notes and diagrams above are ALREADY VISIBLE on the student's chalkboard. Continue teaching directly without duplicating.]\n\n${messageToSend}`;
      }

      console.log("[GeminiLive] Dispatching text turn to model:", messageToSend.slice(0, 100));
      this.session.sendClientContent({
        turns: [
          {
            role: "user",
            parts: [{ text: messageToSend }],
          },
        ],
        turnComplete: true,
      });
    } catch (err) {
      console.warn("[GeminiLive] Failed to send text message via sendClientContent, trying sendRealtimeInput fallback:", err);
      try {
        this.session.sendRealtimeInput({ text: text.trim() });
      } catch (fallbackErr) {
        console.warn("[GeminiLive] Failed to send text fallback:", fallbackErr);
      }
    }
  }

  public sendAudioChunk(base64Chunk: string): void {
    if (!this.session) return;
    try {
      this.session.sendRealtimeInput({
        audio: {
          mimeType: "audio/pcm;rate=16000",
          data: base64Chunk,
        }
      });
    } catch (err) {
      console.warn("Failed to send audio chunk", err);
    }
  }

  public sendAudioStreamEnd(): void {
    if (!this.session) return;
    try {
      this.session.sendRealtimeInput({ audioStreamEnd: true });
    } catch (err) {
      console.warn("Failed to send audioStreamEnd", err);
    }
  }

  public sendTurnComplete(): void {
    if (!this.session) return;
    try {
      this.session.sendClientContent({ turnComplete: true });
    } catch (err) {
      console.warn("Failed to send turnComplete", err);
    }
  }

  public sendBoardContext(summaryText: string): void {
    if (!summaryText?.trim()) return;
    // Block disruptive system notices from being injected as user turns
    if (summaryText.includes('[SYSTEM NOTICE:') || summaryText.includes('SYSTEM NOTICE')) {
      return;
    }
    const trimmed = summaryText.trim();
    this.latestBoardState = trimmed;
  }

  private base64ToInt16(base64: string): Int16Array {
    const binary = window.atob(base64);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
      bytes[i] = binary.charCodeAt(i);
    }
    return new Int16Array(bytes.buffer);
  }

  public disconnect(): void {
    this.isManuallyClosed = true;
    this.isConnected = false;
    this.hasSentKickoff = false;
    this.pendingKickoffText = null;
    if (this.session) {
      try {
        this.session.close();
      } catch (err) {}
      this.session = null;
    }
  }
}
