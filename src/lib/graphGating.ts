/**
 * Dynamic Graph Gating, Parsing & Payload Validation for Mathematics and Physics.
 *
 * User Mandates:
 * 1. "dont be fixed let the tutor call itself without any fixed thing" — do NOT restrict graph
 *    opening with a rigid keyword list; allow the AI tutor to dynamically invoke graphing whenever needed.
 * 2. "should also work with physics" — graphing capabilities and tool calls must support Physics
 *    as well as Mathematics whenever a graph is helpful.
 * 3. Under NO circumstances should Cartesian coordinate graphs open for non-STEM or non-mathematical
 *    topics (such as biology cell walls, histology, chemistry bonding, literature, history)
 *    where vector SVG diagrams or flowcharts are the proper visual medium.
 * 4. Strictly reject meaningless default graphs (e.g. y = x line passing through origin with no
 *    diagram, points, segments, or mathematical context).
 * 5. Robust multi-format parsing for formulas, bounded segments with stopping points, and key points
 *    across JSON objects, tuples, string arrays, and coordinate representations.
 */

export interface GraphFormulaItem {
  formula: string
  color?: string
  label?: string
  domain?: [number, number]
}

export interface GraphSegmentItem {
  start: [number, number]
  end: [number, number]
  label?: string
  color?: string
  dashed?: boolean
}

export interface GraphPointItem {
  x: number
  y: number
  label?: string
  color?: string
  callout?: string
}

export interface GraphBarItem {
  label?: string
  x?: number
  x1?: number
  x2?: number
  height: number
  width?: number
  color?: string
}

export interface GraphVectorItem {
  tail?: [number, number]
  tip: [number, number]
  label?: string
  color?: string
  weight?: number
}

export interface GraphPolygonItem {
  points: [number, number][]
  label?: string
  color?: string
  fillOpacity?: number
}

export interface GraphTextItem {
  x: number
  y: number
  text: string
  color?: string
  size?: number
}

export interface GraphCircleItem {
  center: [number, number]
  radius: number
  label?: string
  color?: string
  fillOpacity?: number
}

export interface GraphPayload {
  formula?: string | string[] | GraphFormulaItem[]
  formulas?: Array<string | GraphFormulaItem>
  segments?: Array<GraphSegmentItem | string | [number, number][] | any>
  points?: Array<[number, number] | GraphPointItem | string> | string
  bars?: Array<GraphBarItem | [string, number] | string | any>
  vectors?: Array<GraphVectorItem | string | any>
  polygons?: Array<GraphPolygonItem | [number, number][] | string | any>
  circles?: Array<GraphCircleItem | string | any>
  texts?: Array<GraphTextItem | string | any>
  domain?: [number, number]
  range?: [number, number]
  title?: string
  callout?: string
}

/**
 * Robustly parses key coordinate points from any format:
 * - Array of objects: { x, y, label, color, callout }
 * - Array of coordinate tuples: [x, y]
 * - Array of JSON strings: '{"x": 0, "y": 0, "label": "Origin"}'
 * - Array of coordinate strings: '(0, 0)', '(2, 4)'
 * - Single JSON string: '[{"x": 0, "y": 0}, {"x": 2, "y": 4}]'
 * - Single coordinate tuple string: "(0, -4), (2, 0), (-2, 0)"
 */
export function parseGraphPoints(raw: any): GraphPointItem[] {
  if (!raw) return []
  const result: GraphPointItem[] = []

  const parseSinglePoint = (p: any) => {
    if (!p) return
    if (typeof p === 'string') {
      const trimmed = p.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') parseSinglePoint(parsed)
          return
        } catch {}
      }
      const tupleMatch = trimmed.match(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/)
      if (tupleMatch) {
        const x = parseFloat(tupleMatch[1])
        const y = parseFloat(tupleMatch[2])
        if (!isNaN(x) && !isNaN(y)) {
          result.push({ x, y })
        }
      }
      return
    }

    if (Array.isArray(p) && p.length >= 2) {
      const x = Number(p[0])
      const y = Number(p[1])
      if (!isNaN(x) && !isNaN(y)) {
        result.push({ x, y })
      }
      return
    }

    if (typeof p === 'object' && 'x' in p && 'y' in p) {
      const x = Number(p.x)
      const y = Number(p.y)
      if (!isNaN(x) && !isNaN(y)) {
        result.push({
          x,
          y,
          label: typeof p.label === 'string' ? p.label : undefined,
          color: typeof p.color === 'string' ? p.color : undefined,
          callout: typeof p.callout === 'string' ? p.callout : undefined,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach(parseSinglePoint)
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach(parseSinglePoint)
          return result
        }
      } catch {}
    }

    // Fallback coordinate tuple regex across entire string
    const matches = trimmed.matchAll(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/g)
    for (const m of matches) {
      const px = parseFloat(m[1])
      const py = parseFloat(m[2])
      if (!isNaN(px) && !isNaN(py)) {
        result.push({ x: px, y: py })
      }
    }
    return result
  }

  if (typeof raw === 'object') {
    parseSinglePoint(raw)
  }

  return result
}

/**
 * Robustly parses line segments with start & end stopping points from any format:
 * - Array of objects: { start: [x,y] | {x,y}, end: [x,y] | {x,y}, label, color, dashed }
 * - Array of JSON strings: '{"start": [0,0], "end": [4,8], "label": "OA"}'
 * - Array of point tuples: [[x1, y1], [x2, y2]]
 * - Array of transition strings: '(0, 0) -> (4, 8)' or '[0,0] to [4,8]'
 * - Single JSON string of array of segments
 */
export function parseGraphSegments(raw: any): GraphSegmentItem[] {
  if (!raw) return []
  const result: GraphSegmentItem[] = []

  const extractCoords = (pt: any): [number, number] | null => {
    if (!pt) return null
    if (Array.isArray(pt) && pt.length >= 2) {
      const x = Number(pt[0])
      const y = Number(pt[1])
      return !isNaN(x) && !isNaN(y) ? [x, y] : null
    }
    if (typeof pt === 'object' && 'x' in pt && 'y' in pt) {
      const x = Number(pt.x)
      const y = Number(pt.y)
      return !isNaN(x) && !isNaN(y) ? [x, y] : null
    }
    if (typeof pt === 'string') {
      const m = pt.match(/\(?\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)?/)
      if (m) {
        const x = parseFloat(m[1])
        const y = parseFloat(m[2])
        return !isNaN(x) && !isNaN(y) ? [x, y] : null
      }
    }
    return null
  }

  const parseSingleSegment = (s: any) => {
    if (!s) return

    // 1. String segment item
    if (typeof s === 'string') {
      const trimmed = s.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') parseSingleSegment(parsed)
          return
        } catch {}
      }

      // Check transition format like "(0, 0) -> (4, 8)" or "[0, 0] to [4, 8]"
      const matches = Array.from(trimmed.matchAll(/(?:\(|\[)\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*(?:\)|\])/g))
      if (matches.length >= 2) {
        const x1 = parseFloat(matches[0][1])
        const y1 = parseFloat(matches[0][2])
        const x2 = parseFloat(matches[1][1])
        const y2 = parseFloat(matches[1][2])
        if (!isNaN(x1) && !isNaN(y1) && !isNaN(x2) && !isNaN(y2)) {
          result.push({
            start: [x1, y1],
            end: [x2, y2],
          })
          return
        }
      }
      return
    }

    // 2. Object with start and end
    if (typeof s === 'object' && s !== null && ('start' in s || 'end' in s)) {
      const start = extractCoords(s.start)
      const end = extractCoords(s.end)
      if (start && end) {
        result.push({
          start,
          end,
          label: typeof s.label === 'string' ? s.label : undefined,
          color: typeof s.color === 'string' ? s.color : undefined,
          dashed: Boolean(s.dashed),
        })
        return
      }
    }

    // 3. Raw tuple of points [[x1, y1], [x2, y2]]
    if (Array.isArray(s) && s.length >= 2) {
      const start = extractCoords(s[0])
      const end = extractCoords(s[1])
      if (start && end) {
        result.push({
          start,
          end,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach(parseSingleSegment)
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach(parseSingleSegment)
          return result
        }
      } catch {}
    }

    // Split on pipe or newline if multiple segments represented as strings
    if (trimmed.includes('|') || trimmed.includes('\n') || trimmed.includes(';')) {
      const parts = trimmed.split(/[|\n;]+/).map((p) => p.trim()).filter(Boolean)
      parts.forEach(parseSingleSegment)
      return result
    }

    parseSingleSegment(trimmed)
    return result
  }

  if (typeof raw === 'object') {
    parseSingleSegment(raw)
  }

  return result
}

/**
 * Robustly parses mathematical formulas:
 * - Array of strings: ['2x + 1', '-x + 4']
 * - Array of objects: [{ formula: '2x + 1', label: 'L1', domain: [0, 5] }]
 * - Array of JSON strings: '{"formula": "2x + 1"}'
 * - Multi-formula string: "2x + 1, -x + 4" or "y = 2x + 1; y = -x + 4"
 */
export function parseGraphFormulas(formula?: any, formulas?: any): GraphFormulaItem[] {
  const result: GraphFormulaItem[] = []

  const addFormulaItem = (item: any) => {
    if (!item) return
    if (typeof item === 'string') {
      const trimmed = item.trim()
      if (!trimmed) return
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') {
            addFormulaItem(parsed)
            return
          }
        } catch {}
      }
      result.push({ formula: trimmed })
      return
    }

    if (typeof item === 'object' && item !== null && item.formula) {
      const fStr = typeof item.formula === 'string' ? item.formula.trim() : ''
      if (fStr) {
        let domain: [number, number] | undefined = undefined
        if (Array.isArray(item.domain) && item.domain.length >= 2) {
          const d0 = Number(item.domain[0])
          const d1 = Number(item.domain[1])
          if (!isNaN(d0) && !isNaN(d1)) domain = [d0, d1]
        }
        result.push({
          formula: fStr,
          color: typeof item.color === 'string' ? item.color : undefined,
          label: typeof item.label === 'string' ? item.label : undefined,
          domain,
        })
      }
    }
  }

  if (Array.isArray(formulas)) {
    formulas.forEach(addFormulaItem)
  }

  if (Array.isArray(formula)) {
    formula.forEach(addFormulaItem)
  } else if (typeof formula === 'string' && formula.trim()) {
    let parts: string[] = []
    if (formula.includes(';') || formula.includes('|') || formula.includes('\n')) {
      parts = formula.split(/[;|\n]+/).map((s) => s.trim()).filter(Boolean)
    } else if (formula.includes('and') || formula.includes('&')) {
      parts = formula.split(/\s*(?:and|&)\s*/i).map((s) => s.trim()).filter(Boolean)
    } else if (/y\s*=.*y\s*=/i.test(formula)) {
      parts = formula.split(/,\s*(?=y\s*=)/i).map((s) => s.trim()).filter(Boolean)
    } else if (formula.includes(',') && !formula.includes('(')) {
      parts = formula.split(',').map((s) => s.trim()).filter(Boolean)
    } else {
      parts = [formula.trim()]
    }

    parts.forEach(addFormulaItem)
  }

  return result
}

/**
 * Robustly parses bar chart items for statistical and science data graphs:
 * - Array of objects: [{ label: 'Maths', height: 85, color: '#2563EB' }]
 * - Array of tuples: [['Maths', 85], ['Science', 92]]
 * - Array of numbers: [10, 25, 40, 15]
 * - Histogram bins: [{ x1: 0, x2: 10, height: 5, label: '0-10' }]
 * - Delimited strings: "Maths: 85 | Science: 92 | English: 78"
 */
export function parseGraphBars(raw: any): GraphBarItem[] {
  if (!raw) return []
  const result: GraphBarItem[] = []

  const parseSingleBar = (b: any, index: number) => {
    if (!b) return
    if (typeof b === 'string') {
      const trimmed = b.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') {
            parseSingleBar(parsed, index)
            return
          }
        } catch {}
      }
      // String format: "Label: 85" or "Label = 85" or "Label, 85"
      const m = trimmed.match(/^([^:=,]+)[:=,]\s*([\-\d\.]+)/)
      if (m) {
        const label = m[1].trim()
        const height = parseFloat(m[2])
        if (!isNaN(height)) {
          result.push({ label, height, x: index * 1.5 + 1, width: 0.85 })
          return
        }
      }
      const numOnly = parseFloat(trimmed)
      if (!isNaN(numOnly)) {
        result.push({ label: `Item ${index + 1}`, height: numOnly, x: index * 1.5 + 1, width: 0.85 })
      }
      return
    }

    if (Array.isArray(b) && b.length >= 2) {
      const label = typeof b[0] === 'string' ? b[0] : String(b[0])
      const height = Number(b[1])
      if (!isNaN(height)) {
        result.push({ label, height, x: index * 1.5 + 1, width: 0.85 })
      }
      return
    }

    if (typeof b === 'object' && b !== null) {
      const height = Number(b.height ?? b.value ?? b.y ?? b.frequency ?? b.count)
      if (!isNaN(height)) {
        const label = typeof b.label === 'string' ? b.label : (typeof b.category === 'string' ? b.category : (typeof b.name === 'string' ? b.name : undefined))
        const x = typeof b.x === 'number' ? b.x : index * 1.5 + 1
        const x1 = typeof b.x1 === 'number' ? b.x1 : undefined
        const x2 = typeof b.x2 === 'number' ? b.x2 : undefined
        const width = typeof b.width === 'number' ? b.width : 0.85
        const color = typeof b.color === 'string' ? b.color : undefined
        result.push({ label, height, x, x1, x2, width, color })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach((item, idx) => parseSingleBar(item, idx))
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach((item, idx) => parseSingleBar(item, idx))
          return result
        }
      } catch {}
    }
    if (trimmed.includes('|') || trimmed.includes(';') || trimmed.includes('\n')) {
      const parts = trimmed.split(/[|;\n]+/).map((s) => s.trim()).filter(Boolean)
      parts.forEach((p, idx) => parseSingleBar(p, idx))
      return result
    }
    parseSingleBar(trimmed, 0)
    return result
  }

  if (typeof raw === 'object' && raw !== null) {
    parseSingleBar(raw, 0)
  }

  return result
}

/**
 * Robustly parses physical vectors and force/velocity arrows:
 * - Array of objects: [{ tail: [0, 0], tip: [4, 3], label: 'F1 = 5 N' }]
 * - Array of string transitions: " (0, 0) -> (4, 3) [F1] "
 * - JSON strings
 */
export function parseGraphVectors(raw: any): GraphVectorItem[] {
  if (!raw) return []
  const result: GraphVectorItem[] = []

  const parseSingleVector = (v: any) => {
    if (!v) return
    if (typeof v === 'string') {
      const trimmed = v.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') {
            parseSingleVector(parsed)
            return
          }
        } catch {}
      }
      const matches = Array.from(trimmed.matchAll(/(?:\(|\[)\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*(?:\)|\])/g))
      if (matches.length >= 2) {
        const x1 = parseFloat(matches[0][1])
        const y1 = parseFloat(matches[0][2])
        const x2 = parseFloat(matches[1][1])
        const y2 = parseFloat(matches[1][2])
        if (!isNaN(x1) && !isNaN(y1) && !isNaN(x2) && !isNaN(y2)) {
          const labelMatch = trimmed.match(/(?:\[|\()([a-zA-Z0-9_\s\=]+)(?:\]|\))$/)
          result.push({
            tail: [x1, y1],
            tip: [x2, y2],
            label: labelMatch ? labelMatch[1].trim() : undefined,
          })
          return
        }
      }
      return
    }

    if (typeof v === 'object' && v !== null && ('tip' in v || 'end' in v)) {
      const tipRaw = v.tip || v.end
      const tailRaw = v.tail || v.start || [0, 0]
      let tip: [number, number] | null = null
      let tail: [number, number] = [0, 0]
      if (Array.isArray(tipRaw) && tipRaw.length >= 2) tip = [Number(tipRaw[0]), Number(tipRaw[1])]
      else if (typeof tipRaw === 'object' && 'x' in tipRaw && 'y' in tipRaw) tip = [Number(tipRaw.x), Number(tipRaw.y)]

      if (Array.isArray(tailRaw) && tailRaw.length >= 2) tail = [Number(tailRaw[0]), Number(tailRaw[1])]
      else if (typeof tailRaw === 'object' && 'x' in tailRaw && 'y' in tailRaw) tail = [Number(tailRaw.x), Number(tailRaw.y)]

      if (tip && !isNaN(tip[0]) && !isNaN(tip[1]) && !isNaN(tail[0]) && !isNaN(tail[1])) {
        result.push({
          tail,
          tip,
          label: typeof v.label === 'string' ? v.label : undefined,
          color: typeof v.color === 'string' ? v.color : undefined,
          weight: typeof v.weight === 'number' ? v.weight : undefined,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach(parseSingleVector)
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach(parseSingleVector)
          return result
        }
      } catch {}
    }
    if (trimmed.includes('|') || trimmed.includes('\n') || trimmed.includes(';')) {
      const parts = trimmed.split(/[|\n;]+/).map((s) => s.trim()).filter(Boolean)
      parts.forEach(parseSingleVector)
      return result
    }
    parseSingleVector(trimmed)
  }

  return result
}

/**
 * Robustly parses Cartesian polygon figures (triangles, quadrilaterals, shaded regions):
 */
export function parseGraphPolygons(raw: any): GraphPolygonItem[] {
  if (!raw) return []
  const result: GraphPolygonItem[] = []

  const parseSinglePolygon = (p: any) => {
    if (!p) return
    if (typeof p === 'string') {
      const trimmed = p.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') {
            parseSinglePolygon(parsed)
            return
          }
        } catch {}
      }
      return
    }

    if (Array.isArray(p) && p.length >= 3 && Array.isArray(p[0])) {
      const pts: [number, number][] = []
      for (const pt of p) {
        if (Array.isArray(pt) && pt.length >= 2) {
          const x = Number(pt[0])
          const y = Number(pt[1])
          if (!isNaN(x) && !isNaN(y)) pts.push([x, y])
        }
      }
      if (pts.length >= 3) {
        result.push({ points: pts })
      }
      return
    }

    if (typeof p === 'object' && p !== null && Array.isArray(p.points)) {
      const pts: [number, number][] = []
      for (const pt of p.points) {
        if (Array.isArray(pt) && pt.length >= 2) {
          const x = Number(pt[0])
          const y = Number(pt[1])
          if (!isNaN(x) && !isNaN(y)) pts.push([x, y])
        } else if (typeof pt === 'object' && pt !== null && 'x' in pt && 'y' in pt) {
          const x = Number(pt.x)
          const y = Number(pt.y)
          if (!isNaN(x) && !isNaN(y)) pts.push([x, y])
        }
      }
      if (pts.length >= 3) {
        result.push({
          points: pts,
          label: typeof p.label === 'string' ? p.label : undefined,
          color: typeof p.color === 'string' ? p.color : undefined,
          fillOpacity: typeof p.fillOpacity === 'number' ? p.fillOpacity : undefined,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    if (raw.length >= 3 && Array.isArray(raw[0]) && typeof raw[0][0] === 'number') {
      parseSinglePolygon(raw)
      return result
    }
    raw.forEach(parseSinglePolygon)
    return result
  }

  return result
}

/**
 * Robustly parses custom coordinate text annotations placed anywhere on the graph:
 * - Array of objects: [{ x: 2, y: 3, text: 'Local Maximum', color: '#DC2626' }]
 * - Coordinate string tuples: "(2, 3): Peak Amplitude"
 * - JSON string array
 */
export function parseGraphTexts(raw: any): GraphTextItem[] {
  if (!raw) return []
  const result: GraphTextItem[] = []

  const parseSingleText = (t: any) => {
    if (!t) return
    if (typeof t === 'string') {
      const trimmed = t.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') {
            parseSingleText(parsed)
            return
          }
        } catch {}
      }
      const mCoords = trimmed.match(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/)
      if (mCoords) {
        const x = parseFloat(mCoords[1])
        const y = parseFloat(mCoords[2])
        const textStr = trimmed.replace(mCoords[0], '').replace(/^[:\-–\s]+|[:\-–\s]+$/g, '').trim()
        if (!isNaN(x) && !isNaN(y) && textStr) {
          result.push({ x, y, text: textStr })
          return
        }
      }
      return
    }

    if (typeof t === 'object' && t !== null) {
      const x = Number(t.x ?? t.coords?.[0])
      const y = Number(t.y ?? t.coords?.[1])
      const text = typeof t.text === 'string' ? t.text : (typeof t.label === 'string' ? t.label : (typeof t.content === 'string' ? t.content : ''))
      if (!isNaN(x) && !isNaN(y) && text) {
        result.push({
          x,
          y,
          text,
          color: typeof t.color === 'string' ? t.color : undefined,
          size: typeof t.size === 'number' ? t.size : undefined,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach(parseSingleText)
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach(parseSingleText)
          return result
        }
      } catch {}
    }
    if (trimmed.includes('|') || trimmed.includes('\n') || trimmed.includes(';')) {
      const parts = trimmed.split(/[|\n;]+/).map((s) => s.trim()).filter(Boolean)
      parts.forEach(parseSingleText)
      return result
    }
    parseSingleText(trimmed)
  }

  return result
}

/**
 * Robustly parses circles with center and radius in Cartesian space:
 * - Array of objects: [{ center: [0, 0], radius: 5, label: 'x² + y² = 25' }]
 * - JSON strings
 */
export function parseGraphCircles(raw: any): GraphCircleItem[] {
  if (!raw) return []
  const result: GraphCircleItem[] = []

  const parseSingleCircle = (c: any) => {
    if (!c) return
    if (typeof c === 'string') {
      const trimmed = c.trim()
      if (trimmed.startsWith('{')) {
        try {
          const parsed = JSON.parse(trimmed)
          if (parsed && typeof parsed === 'object') {
            parseSingleCircle(parsed)
            return
          }
        } catch {}
      }
      const mCenter = trimmed.match(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/)
      const mR = trimmed.match(/(?:r|radius)\s*[:=]?\s*([\d\.]+)/i)
      if (mCenter && mR) {
        const cx = parseFloat(mCenter[1])
        const cy = parseFloat(mCenter[2])
        const r = parseFloat(mR[1])
        if (!isNaN(cx) && !isNaN(cy) && !isNaN(r) && r > 0) {
          result.push({ center: [cx, cy], radius: r })
          return
        }
      }
      return
    }

    if (typeof c === 'object' && c !== null) {
      let center: [number, number] = [0, 0]
      if (Array.isArray(c.center) && c.center.length >= 2) center = [Number(c.center[0]), Number(c.center[1])]
      else if (typeof c.x === 'number' && typeof c.y === 'number') center = [c.x, c.y]

      const radius = Number(c.radius ?? c.r)
      if (!isNaN(radius) && radius > 0 && !isNaN(center[0]) && !isNaN(center[1])) {
        result.push({
          center,
          radius,
          label: typeof c.label === 'string' ? c.label : undefined,
          color: typeof c.color === 'string' ? c.color : undefined,
          fillOpacity: typeof c.fillOpacity === 'number' ? c.fillOpacity : undefined,
        })
      }
    }
  }

  if (Array.isArray(raw)) {
    raw.forEach(parseSingleCircle)
    return result
  }

  if (typeof raw === 'string') {
    const trimmed = raw.trim()
    if (trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed)
        if (Array.isArray(parsed)) {
          parsed.forEach(parseSingleCircle)
          return result
        }
      } catch {}
    }
    parseSingleCircle(trimmed)
  }

  return result
}

/**
 * Validates whether a graph payload has substantive mathematical purpose.
 * Rejects empty graphs, placeholder 'x' or 'linear' formulas with no segments or points,
 * or payloads with neither valid formulas nor segments.
 */
export function isValidGraphPayload(payload?: GraphPayload | null): boolean {
  if (!payload || typeof payload !== 'object') return false

  // 1. If bars are present, it's a valid bar graph / histogram
  const parsedBars = parseGraphBars(payload.bars)
  if (parsedBars.length > 0) return true

  // 2. If vectors are present, it's a valid physics vector plot
  const parsedVectors = parseGraphVectors(payload.vectors)
  if (parsedVectors.length > 0) return true

  // 3. If polygons are present, it's a valid coordinate geometry polygon plot
  const parsedPolygons = parseGraphPolygons(payload.polygons)
  if (parsedPolygons.length > 0) return true

  // 4. If circles are present, it's a valid circular figure plot
  const parsedCircles = parseGraphCircles(payload.circles)
  if (parsedCircles.length > 0) return true

  // 5. If custom coordinate texts are present, it's a valid annotated graph
  const parsedTexts = parseGraphTexts(payload.texts)
  if (parsedTexts.length > 0) return true

  // 6. If segments are present and non-empty with valid start/end coordinates, it's valid
  const parsedSegments = parseGraphSegments(payload.segments)
  if (parsedSegments.length > 0) {
    return true
  }

  // 5. Check points
  const parsedPoints = parseGraphPoints(payload.points)
  const hasPoints = parsedPoints.length > 0

  // 6. Collect all formulas
  const parsedFormulas = parseGraphFormulas(payload.formula, payload.formulas)
  const cleanFormulas = parsedFormulas.map((f) => f.formula.trim()).filter((f) => f.length > 0)

  // If no formulas and no segments and no points, reject
  if (cleanFormulas.length === 0 && !hasPoints) {
    return false
  }

  // Check if the only formula is a meaningless default line y = x or 'linear'
  const isMeaninglessLine = (f: string) => {
    const normalized = f.toLowerCase().replace(/\s+/g, '').replace(/^(?:y|f\(x\))=/, '')
    return normalized === 'x' || normalized === 'linear' || normalized === '+x' || normalized === '1*x' || normalized === 'y=x'
  }

  const allAreMeaningless = cleanFormulas.length > 0 && cleanFormulas.every(isMeaninglessLine)

  // If the formulas are solely meaningless y = x lines AND there are no points or segments, reject!
  if (allAreMeaningless && !hasPoints) {
    return false
  }

  // If there are points, even with a line through origin or no formula, it's a valid coordinate plot
  if (hasPoints) {
    return true
  }

  return cleanFormulas.length > 0
}

export function isLegitimateGraphTopic(topic: string, subject: string): boolean {
  const s = (subject || '').toLowerCase().trim();
  const t = (topic || '').toLowerCase().trim();

  // If the topic explicitly mentions graphs, plots, coordinates, bar graphs, histograms, vectors, or curves, it is ALWAYS allowed
  const explicitGraphPhrases = [
    'bar graph', 'bargraph', 'histogram', 'frequency polygon', 'ogive', 'pie chart',
    'coordinate geometry', 'cartesian', 'plot', 'graph', 'curve', 'v-t', 's-t', 'a-t',
    'p-v diagram', 'rate of reaction', 'ohm\'s law', 'vector addition', 'vector diagram',
    'scatter', 'data handling', 'statistics'
  ];
  if (explicitGraphPhrases.some((phrase) => t.includes(phrase))) {
    return true;
  }

  // 1. Non-STEM subjects (Languages, Humanities) are unconditionally barred from graphing
  const nonStemSubjects = [
    'hist', 'civic', 'geog', 'politi',
    'social', 'eng', 'lit', 'lang', 'hindi', 'french', 'german'
  ];
  if (nonStemSubjects.some((sub) => s.includes(sub))) {
    return false;
  }

  // 2. Disallow topics containing purely non-mathematical, biological, or chemical keywords that have NO graphical component
  const strictlyNonMathKeywords = [
    'cell', 'wall', 'tissue', 'histolog', 'organ', 'plant', 'animal',
    'cellulose', 'pectin', 'lignin', 'photosynth', 'digest', 'xylem',
    'phloem', 'parenchyma', 'collenchyma', 'sclerenchyma', 'epithel',
    'covalent', 'ionic', 'bonding', 'periodic table',
    'valency', 'respiration', 'circulat', 'neuron', 'nephron', 'dna', 'rna',
    'chromosome', 'mitosis', 'meiosis', 'endocrine', 'hormone',
    'ecosystem', 'trophic'
  ];
  if (strictlyNonMathKeywords.some((kw) => t.includes(kw)) && !t.includes('graph') && !t.includes('plot') && !t.includes('curve') && !t.includes('rate')) {
    return false;
  }

  // 3. Geometric diagram topics without coordinate/graph context belong to SVG diagram / geometry tool
  const geometricDiagramKeywords = [
    'triangle', 'circle', 'cylinder', 'cone', 'sphere', 'cube',
    'cuboid', 'angle', 'ray', 'optics', 'lens', 'mirror',
    'circuit', 'resistor', 'apparatus'
  ];
  if (geometricDiagramKeywords.some((kw) => t.includes(kw)) && !t.includes('coordinate') && !t.includes('graph') && !t.includes('plot') && !t.includes('cartesian')) {
    return false;
  }

  // 4. Subject must be Mathematics, Physics, Chemistry, or Quantitative Science
  const isMathSubject = s.includes('math') || s.includes('algebra') || s.includes('calculus') || s.includes('geometry') || s.includes('stat') || s.includes('arithmetic');
  const isPhysicsSubject = s.includes('physic') || s.includes('science') || s.includes('mechanic');
  const isChemistryPhysical = s.includes('chem') && (t.includes('graph') || t.includes('curve') || t.includes('rate') || t.includes('kinetics') || t.includes('titrat') || t.includes('phase') || t.includes('temperature') || t.includes('boyle') || t.includes('charles'));
  if (!isMathSubject && !isPhysicsSubject && !isChemistryPhysical) {
    return false;
  }

  // Allow dynamic graph calls for both Mathematics and Physics topics without rigid keyword allowlists
  return true;
}
