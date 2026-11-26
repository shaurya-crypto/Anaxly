'use client'

import React, { useMemo, useState } from 'react'
import {
  Mafs,
  Coordinates,
  Plot,
  Line,
  Point,
  Text,
  Polygon,
  Vector,
  Polyline,
  Circle,
  Theme,
} from 'mafs'
import 'mafs/core.css'
import 'mafs/font.css'
import { compile } from 'mathjs'
import { 
  Activity, 
  X, 
  Maximize2, 
  Minimize2, 
  Move, 
  RotateCcw, 
  ZoomIn, 
  ZoomOut, 
  PanelRight, 
  GripHorizontal,
  Layers,
  Info,
  BarChart2
} from 'lucide-react'
import {
  parseGraphPoints,
  parseGraphSegments,
  parseGraphFormulas,
  parseGraphBars,
  parseGraphVectors,
  parseGraphPolygons,
  parseGraphTexts,
  parseGraphCircles,
  parseGraphPies,
  parseGraphLineSeries,
  parseGraphShadedRegions,
  type GraphFormulaItem,
  type GraphSegmentItem,
  type GraphPointItem,
  type GraphBarItem,
  type GraphVectorItem,
  type GraphPolygonItem,
  type GraphTextItem,
  type GraphCircleItem,
  type GraphPieSliceItem,
  type GraphLineSeriesItem,
  type GraphShadedRegionItem,
} from '@/lib/graphGating'

export type GraphDisplayMode = 'docked' | 'floating' | 'maximized' | 'minimized'

export interface MafsGraphCanvasProps {
  formula?: string | string[] | GraphFormulaItem[]
  formulas?: Array<string | GraphFormulaItem>
  segments?: Array<GraphSegmentItem | string | any>
  points?: Array<[number, number] | GraphPointItem | string> | string
  bars?: Array<GraphBarItem | [string, number] | string | any>
  vectors?: Array<GraphVectorItem | string | any>
  polygons?: Array<GraphPolygonItem | [number, number][] | string | any>
  circles?: Array<GraphCircleItem | string | any>
  texts?: Array<GraphTextItem | string | any>
  pies?: Array<GraphPieSliceItem | string | any> | string
  lineSeries?: Array<GraphLineSeriesItem | any> | string
  shadedRegions?: Array<GraphShadedRegionItem | any> | string
  domain?: [number, number]
  range?: [number, number]
  title?: string
  callout?: string
  width?: number | 'auto'
  height?: number
  displayMode?: GraphDisplayMode
  onModeChange?: (mode: GraphDisplayMode) => void
  onClose?: () => void
}

/**
 * Solves standard implicit linear equations in two variables (ax + by = c, ax + by + c = 0)
 * for y in terms of x: y = (c - ax) / b.
 */
function solveLinearEquationForY(eqStr: string): string | null {
  const clean = eqStr.replace(/\s+/g, '')
  // Match forms like ax+by=c or by+ax=c
  // e.g. 2x+3y=6, x-y=1, -x+2y=-4
  const matchStandard = clean.match(/^([+-]?\d*\.?\d*)x([+-]\d*\.?\d*)y=([+-]?\d*\.?\d+)$/i)
  if (matchStandard) {
    const aStr = matchStandard[1]
    const bStr = matchStandard[2]
    const cStr = matchStandard[3]
    const a = aStr === '' || aStr === '+' ? 1 : aStr === '-' ? -1 : parseFloat(aStr)
    const b = bStr === '' || bStr === '+' ? 1 : bStr === '-' ? -1 : parseFloat(bStr)
    const c = parseFloat(cStr)
    if (!isNaN(a) && !isNaN(b) && b !== 0 && !isNaN(c)) {
      return `(${c} - (${a}) * x) / (${b})`
    }
  }
  // Match forms like ax+by+c=0
  // e.g. 3x+4y-12=0
  const matchZero = clean.match(/^([+-]?\d*\.?\d*)x([+-]\d*\.?\d*)y([+-]\d*\.?\d*)=0$/i)
  if (matchZero) {
    const aStr = matchZero[1]
    const bStr = matchZero[2]
    const cStr = matchZero[3]
    const a = aStr === '' || aStr === '+' ? 1 : aStr === '-' ? -1 : parseFloat(aStr)
    const b = bStr === '' || bStr === '+' ? 1 : bStr === '-' ? -1 : parseFloat(bStr)
    const c = parseFloat(cStr)
    if (!isNaN(a) && !isNaN(b) && b !== 0 && !isNaN(c)) {
      return `(-(${c}) - (${a}) * x) / (${b})`
    }
  }
  return null
}

/**
 * Normalizes user / LLM mathematical formula string into a mathjs-evaluable expression.
 * Handles implicit multiplication (2x -> 2*x), trigonometric notation, powers (^ -> **), and constants.
 */
function normalizeMathFormula(raw: string): string {
  if (!raw) return ''
  let clean = raw.trim()
  // Check if it's an implicit linear equation like 2x + 3y = 6
  if (clean.includes('y') && clean.includes('=')) {
    const solved = solveLinearEquationForY(clean)
    if (solved) return solved
  }
  // Strip "y =" or "f(x) =" prefix
  clean = clean.replace(/^(?:y|f\(x\))\s*=\s*/i, '')
  // Replace implicit multiplication like 2x with 2*x
  clean = clean.replace(/(\d+)([a-zA-Z])/g, '$1 * $2')
  // Replace brackets if any
  clean = clean.replace(/\[/g, '(').replace(/\]/g, ')')
  return clean
}

// Scholastic Ink & Aristotle Palette for clean white background
const CURVE_COLORS = [
  '#2563EB', // 1. Aristotle Royal Blue
  '#DC2626', // 2. Scholar Crimson Red
  '#16A34A', // 3. Emerald Green
  '#D97706', // 4. Warm Amber
  '#7C3AED', // 5. Vivid Violet
  '#0891B2', // 6. Deep Cyan
]

/**
 * Compiles a mathematical expression into a safe real-valued evaluator f(x).
 */
function compileFormulaFn(rawFormula: string): ((x: number) => number) | null {
  const normalized = normalizeMathFormula(rawFormula)
  if (!normalized) return null
  try {
    const expr = compile(normalized)
    return (x: number): number => {
      try {
        const res = expr.evaluate({ x, e: Math.E, pi: Math.PI })
        return typeof res === 'number' && isFinite(res) ? res : NaN
      } catch {
        return NaN
      }
    }
  } catch {
    return null
  }
}

/**
 * Samples a closed polygon tracing upperFn(x) forward and lowerFn(x) backward across [d0, d1].
 */
function buildShadedRegionPolygon(
  upperFn: (x: number) => number,
  lowerFn: ((x: number) => number) | null,
  domain: [number, number],
  progress: number
): [number, number][] {
  const d0 = Math.min(domain[0], domain[1])
  const d1 = d0 + (Math.max(domain[0], domain[1]) - d0) * Math.max(0.02, Math.min(1, progress))
  if (d1 <= d0) return []
  const steps = 48
  const upperPts: [number, number][] = []
  const lowerPts: [number, number][] = []
  for (let i = 0; i <= steps; i++) {
    const x = d0 + (i / steps) * (d1 - d0)
    const yu = upperFn(x)
    const yl = lowerFn ? lowerFn(x) : 0
    if (Number.isFinite(yu) && Number.isFinite(yl)) {
      upperPts.push([x, yu])
      lowerPts.unshift([x, yl])
    }
  }
  return upperPts.length >= 2 ? [...upperPts, ...lowerPts] : []
}

export function MafsGraphCanvas({
  formula,
  formulas,
  segments,
  points,
  bars,
  vectors,
  polygons,
  circles,
  texts,
  pies,
  lineSeries,
  shadedRegions,
  domain = [-5, 5],
  range = [-5, 5],
  title,
  callout,
  width = 'auto',
  height,
  displayMode = 'docked',
  onModeChange,
  onClose,
}: MafsGraphCanvasProps) {
  // 1. Parse discrete key points with coordinates and labels using resilient parser
  const parsedPoints: GraphPointItem[] = useMemo(() => {
    return parseGraphPoints(points)
  }, [points])

  // 1b. Parse bar chart items for statistics and science data
  const parsedBars: GraphBarItem[] = useMemo(() => {
    return parseGraphBars(bars)
  }, [bars])

  // 1c. Parse physics vectors with directional arrows
  const parsedVectors: GraphVectorItem[] = useMemo(() => {
    return parseGraphVectors(vectors)
  }, [vectors])

  // 1d. Parse Cartesian coordinate polygons (triangles, quadrilaterals)
  const parsedPolygons: GraphPolygonItem[] = useMemo(() => {
    return parseGraphPolygons(polygons)
  }, [polygons])

  // 1e. Parse circles in Cartesian space
  const parsedCircles: GraphCircleItem[] = useMemo(() => {
    return parseGraphCircles(circles)
  }, [circles])

  // 1e2. Parse pie slices, discrete line series, and shaded regions
  const parsedPies: GraphPieSliceItem[] = useMemo(() => {
    return parseGraphPies(pies)
  }, [pies])

  const parsedLineSeries: GraphLineSeriesItem[] = useMemo(() => {
    return parseGraphLineSeries(lineSeries).map((s, idx) => ({
      ...s,
      color: s.color || CURVE_COLORS[idx % CURVE_COLORS.length],
    }))
  }, [lineSeries])

  const parsedShadedRegions: GraphShadedRegionItem[] = useMemo(() => {
    return parseGraphShadedRegions(shadedRegions)
  }, [shadedRegions])

  // 1f. Parse multiple freeform text annotations placed anywhere on the graph
  const parsedTexts: GraphTextItem[] = useMemo(() => {
    const raw = parseGraphTexts(texts)
    // Filter out duplicate text labels that repeat point coordinates or point labels directly on top of or near a point
    return raw.filter((txt) => {
      const isDuplicateOfPoint = parsedPoints.some((pt) => {
        const dx = Math.abs(txt.x - pt.x)
        const dy = Math.abs(txt.y - pt.y)
        if (dx <= 1.2 && dy <= 1.2) {
          const cleanTxt = txt.text.replace(/\s+/g, '')
          const ptCoordTxt = `(${pt.x},${pt.y})`
          const ptLabelTxt = (pt.label || '').replace(/\s+/g, '')
          if (cleanTxt === ptCoordTxt || (ptLabelTxt && cleanTxt === ptLabelTxt)) {
            return true // Duplicate found, exclude it
          }
        }
        return false
      })
      return !isDuplicateOfPoint
    })
  }, [texts, parsedPoints])

  // 2. Parse bounded line segments with start and end stopping points using resilient parser
  const parsedSegments: GraphSegmentItem[] = useMemo(() => {
    const segs = parseGraphSegments(segments)
    return segs.map((s, idx) => ({
      ...s,
      color: s.color || CURVE_COLORS[(idx + 1) % CURVE_COLORS.length],
    }))
  }, [segments])

  // 3. Normalize and parse 2-3 functions/lines at once using resilient parser
  const rawFormulasList = useMemo(() => {
    const list = parseGraphFormulas(formula, formulas)
    return list.map((item, idx) => ({
      ...item,
      color: item.color || CURVE_COLORS[idx % CURVE_COLORS.length],
    }))
  }, [formula, formulas])

  // 4. Auto-fit initial view bounds to encompass all points, segment endpoints, formula domains, bars, vectors, circles, and texts
  const autoBounds = useMemo<{ domain: [number, number]; range: [number, number] }>(() => {
    const xs: number[] = []
    const ys: number[] = []

    parsedPoints.forEach((p) => {
      xs.push(p.x)
      ys.push(p.y)
    })

    parsedBars.forEach((b, idx) => {
      const x1 = b.x1 ?? (b.x != null && b.width != null ? b.x - b.width / 2 : idx * 1.5 + 1 - 0.45)
      const x2 = b.x2 ?? (b.x != null && b.width != null ? b.x + b.width / 2 : idx * 1.5 + 1 + 0.45)
      xs.push(x1, x2)
      ys.push(0, b.height)
    })

    parsedVectors.forEach((v) => {
      const tail = v.tail || [0, 0]
      xs.push(tail[0], v.tip[0])
      ys.push(tail[1], v.tip[1])
    })

    parsedPolygons.forEach((poly) => {
      poly.points.forEach((p) => {
        xs.push(p[0])
        ys.push(p[1])
      })
    })

    parsedCircles.forEach((c) => {
      xs.push(c.center[0] - c.radius, c.center[0] + c.radius)
      ys.push(c.center[1] - c.radius, c.center[1] + c.radius)
    })

    parsedTexts.forEach((t) => {
      xs.push(t.x)
      ys.push(t.y)
    })

    parsedSegments.forEach((s) => {
      xs.push(s.start[0], s.end[0])
      ys.push(s.start[1], s.end[1])
    })

    parsedLineSeries.forEach((series) => {
      series.points.forEach(([px, py]) => {
        xs.push(px)
        ys.push(py)
      })
      if (series.filled) {
        ys.push(0)
      }
    })

    parsedShadedRegions.forEach((reg) => {
      if (reg.domain) {
        xs.push(reg.domain[0], reg.domain[1])
      }
    })

    rawFormulasList.forEach((f) => {
      if (f.domain) {
        xs.push(f.domain[0], f.domain[1])
      }
    })

    // If explicit domain / range were passed and are NOT default [-5, 5], respect them
    const isCustomDomain = domain && (domain[0] !== -5 || domain[1] !== 5)
    const isCustomRange = range && (range[0] !== -5 || range[1] !== 5)

    if (isCustomDomain && isCustomRange) {
      return { domain, range }
    }

    if (xs.length > 0 && ys.length > 0) {
      let minX = Math.min(...xs)
      let maxX = Math.max(...xs)
      let minY = Math.min(...ys)
      let maxY = Math.max(...ys)

      // Ensure minimum span
      if (maxX - minX < 2) {
        const mid = (minX + maxX) / 2
        minX = mid - 1
        maxX = mid + 1
      }
      if (maxY - minY < 2) {
        const mid = (minY + maxY) / 2
        minY = mid - 1
        maxY = mid + 1
      }

      // Add generous margin (20% or at least 1 unit) so points and endpoints are well inside viewport
      const spanX = maxX - minX
      const spanY = maxY - minY
      const padX = Math.max(spanX * 0.2, 1)
      const padY = Math.max(spanY * 0.2, 1)

      const finalDomain: [number, number] = isCustomDomain ? domain : [Math.floor(minX - padX), Math.ceil(maxX + padX)]
      const finalRange: [number, number] = isCustomRange ? range : [Math.floor(minY - padY), Math.ceil(maxY + padY)]

      return { domain: finalDomain, range: finalRange }
    }

    return { domain, range }
  }, [domain, range, parsedPoints, parsedBars, parsedVectors, parsedPolygons, parsedCircles, parsedTexts, parsedSegments, parsedLineSeries, parsedShadedRegions, rawFormulasList])

  // Smooth progressive draw-in animation (0 -> 1) whenever a new graph payload arrives
  const graphAnimKey = useMemo(
    () =>
      JSON.stringify({
        formula,
        formulas,
        segments,
        points,
        bars,
        vectors,
        polygons,
        circles,
        texts,
        pies,
        lineSeries,
        shadedRegions,
        title,
      }),
    [formula, formulas, segments, points, bars, vectors, polygons, circles, texts, pies, lineSeries, shadedRegions, title]
  )

  const prefersReducedMotion =
    typeof window !== 'undefined' &&
    typeof window.matchMedia === 'function' &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches

  const [animT, setAnimT] = useState<number>(prefersReducedMotion ? 1 : 0)
  const [animRunId, setAnimRunId] = useState<number>(0)

  React.useEffect(() => {
    if (prefersReducedMotion) {
      setAnimT(1)
      return
    }
    setAnimT(0)
    let rafId = 0
    const durationMs = 950
    const startTime = performance.now()
    const tick = (now: number) => {
      const raw = Math.min(1, (now - startTime) / durationMs)
      const eased = 1 - Math.pow(1 - raw, 3)
      setAnimT(eased)
      if (raw < 1) {
        rafId = requestAnimationFrame(tick)
      }
    }
    rafId = requestAnimationFrame(tick)
    return () => {
      if (rafId) cancelAnimationFrame(rafId)
    }
  }, [graphAnimKey, animRunId, prefersReducedMotion])

  // Interactive view bounds with local zoom & pan state
  const [viewDomain, setViewDomain] = useState<[number, number]>(autoBounds.domain)
  const [viewRange, setViewRange] = useState<[number, number]>(autoBounds.range)
  const [showDerivative, setShowDerivative] = useState(false)

  // Reset to initial bounds if incoming props or autoBounds change significantly
  React.useEffect(() => {
    setViewDomain(autoBounds.domain)
    setViewRange(autoBounds.range)
  }, [autoBounds.domain[0], autoBounds.domain[1], autoBounds.range[0], autoBounds.range[1]])

  // Compile all formulas into evaluable function curves with labels, domains, and optional area fill
  const compiledCurves = useMemo(() => {
    return rawFormulasList
      .map((item, idx) => {
        const fn = compileFormulaFn(item.formula)
        if (!fn) return null
        const rawClean = item.formula.replace(/^(?:y|f\(x\))\s*=\s*/i, '').trim()
        return {
          raw: rawClean,
          label: item.label || (rawFormulasList.length > 1 ? `y${idx + 1} = ${rawClean}` : `y = ${rawClean}`),
          fn,
          color: item.color || CURVE_COLORS[idx % CURVE_COLORS.length],
          fillColor: item.fillColor,
          fillOpacity: item.fillOpacity,
          filled: Boolean(item.filled || item.fillColor),
          domain: item.domain,
        }
      })
      .filter((c): c is NonNullable<typeof c> => c !== null)
  }, [rawFormulasList])

  const compiledShadedRegions = useMemo(() => {
    return parsedShadedRegions
      .map((reg, idx) => {
        const upperFn = compileFormulaFn(reg.upperFormula || reg.formula || '')
        if (!upperFn) return null
        const lowerFn = reg.lowerFormula ? compileFormulaFn(reg.lowerFormula) : null
        const color = reg.color || reg.fillColor || CURVE_COLORS[(idx + 2) % CURVE_COLORS.length]
        return {
          upperFn,
          lowerFn,
          domain: reg.domain,
          color,
          fillColor: reg.fillColor || color,
          fillOpacity: reg.fillOpacity ?? 0.25,
          label: reg.label,
        }
      })
      .filter((r): r is NonNullable<typeof r> => r !== null)
  }, [parsedShadedRegions])

  const isPieOnlyChart =
    parsedPies.length > 0 &&
    compiledCurves.length === 0 &&
    parsedBars.length === 0 &&
    parsedSegments.length === 0 &&
    parsedPolygons.length === 0 &&
    parsedCircles.length === 0 &&
    parsedLineSeries.length === 0 &&
    compiledShadedRegions.length === 0 &&
    parsedVectors.length === 0

  const primaryFn = compiledCurves[0]?.fn || null

  // Numerical derivative function: f'(x) ≈ (f(x+h) - f(x-h)) / 2h
  const derivativeFn = useMemo(() => {
    if (!primaryFn) return null
    const h = 0.0001
    return (x: number): number => {
      const y2 = primaryFn(x + h)
      const y1 = primaryFn(x - h)
      if (isNaN(y1) || isNaN(y2)) return NaN
      return (y2 - y1) / (2 * h)
    }
  }, [primaryFn])

  // Auto-detect intersection points between multiple curves when manual points are absent
  const autoIntersections: [number, number][] = useMemo(() => {
    if (parsedPoints.length > 0 || compiledCurves.length < 2) return []
    const pts: [number, number][] = []
    const [minX, maxX] = viewDomain
    const [minY, maxY] = viewRange

    for (let i = 0; i < Math.min(compiledCurves.length - 1, 2); i++) {
      for (let j = i + 1; j < Math.min(compiledCurves.length, 3); j++) {
        const f1 = compiledCurves[i].fn
        const f2 = compiledCurves[j].fn
        const steps = 100
        const dx = (maxX - minX) / steps
        let prevDiff = f1(minX) - f2(minX)

        for (let s = 1; s <= steps; s++) {
          const x = minX + s * dx
          const diff = f1(x) - f2(x)
          if (!isNaN(prevDiff) && !isNaN(diff) && (prevDiff * diff <= 0 || Math.abs(diff) < 1e-4)) {
            let left = x - dx
            let right = x
            for (let iter = 0; iter < 12; iter++) {
              const mid = (left + right) / 2
              const dMid = f1(mid) - f2(mid)
              if (Math.abs(dMid) < 1e-6) {
                left = mid
                right = mid
                break
              }
              if ((f1(left) - f2(left)) * dMid <= 0) {
                right = mid
              } else {
                left = mid
              }
            }
            const rootX = (left + right) / 2
            const rootY = f1(rootX)
            if (!isNaN(rootY) && rootY >= minY - 0.5 && rootY <= maxY + 0.5) {
              const roundedX = Math.round(rootX * 100) / 100
              const roundedY = Math.round(rootY * 100) / 100
              if (!pts.some(([ex, ey]) => Math.abs(ex - roundedX) < 0.1 && Math.abs(ey - roundedY) < 0.1)) {
                pts.push([roundedX, roundedY])
              }
            }
          }
          prevDiff = diff
        }
      }
    }
    return pts
  }, [compiledCurves, viewDomain, viewRange, parsedPoints.length])

  const handleZoom = (factor: number) => {
    setViewDomain(([min, max]) => {
      const span = (max - min) * factor
      const mid = (min + max) / 2
      return [mid - span / 2, mid + span / 2]
    })
    setViewRange(([min, max]) => {
      const span = (max - min) * factor
      const mid = (min + max) / 2
      return [mid - span / 2, mid + span / 2]
    })
  }

  const handleReset = () => {
    setViewDomain(autoBounds.domain)
    setViewRange(autoBounds.range)
    setAnimRunId((n) => n + 1)
  }

  const rawFormulaTitle = Array.isArray(formula)
    ? formula.map((f) => (typeof f === 'string' ? f : f?.formula)).filter(Boolean).join(', ')
    : typeof formula === 'string'
    ? formula
    : ''

  const displayTitle =
    title ||
    (isPieOnlyChart
      ? `Pie Chart Distribution (${parsedPies.length} slices)`
      : parsedBars.length > 0
      ? `Statistical Bar Graph (${parsedBars.length} categories)`
      : parsedVectors.length > 0
      ? `Physics Vector Diagram (${parsedVectors.length} vectors)`
      : parsedPolygons.length > 0
      ? `Geometric Polygon (${parsedPolygons[0]?.points?.length || 3}-sided)`
      : parsedCircles.length > 0
      ? `Geometric Circle (r = ${parsedCircles[0]?.radius || 1})`
      : parsedLineSeries.length > 0
      ? `Line Graph (${parsedLineSeries.length} series)`
      : compiledShadedRegions.length > 0
      ? `Shaded Area Graph (${compiledShadedRegions.length} regions)`
      : compiledCurves.length > 1
      ? `Comparative Graphs (${compiledCurves.length} curves)`
      : compiledCurves.length === 1
      ? `Graph: ${compiledCurves[0].label}`
      : parsedSegments.length > 0
      ? `Coordinate Segments (${parsedSegments.length} segments)`
      : parsedTexts.length > 0
      ? `Annotated Coordinate Plane`
      : `Mathematical Graph: ${rawFormulaTitle || 'Functions'}`)

  const resolvedHeight =
    height || (displayMode === 'maximized' ? 640 : displayMode === 'docked' ? 500 : 400)

  const pieTotal = parsedPies.reduce((sum, s) => sum + Math.max(0, s.value), 0)

  return (
    <div className="w-full h-full relative flex flex-col bg-[#FFFFFF] border-2 border-[#E2E8F0] rounded-2xl overflow-hidden shadow-2xl text-[#0F172A] font-sans select-none">
      {/* 1. Top Header & Toolbar (High-Taste Scholastic Layout) */}
      <div className="px-3.5 py-2.5 bg-[#F8FAFC] border-b border-[#E2E8F0] flex items-center justify-between gap-2 shrink-0">
        <div className="flex items-center gap-2 min-w-0">
          <div 
            className="drag-handle-graph cursor-grab active:cursor-grabbing p-1 rounded-md hover:bg-[#F1F5F9] text-[#64748B] hover:text-[#0F172A] transition-colors" 
            title="Drag to move graph box"
          >
            <GripHorizontal className="w-4 h-4" />
          </div>
          <Activity className="w-4 h-4 text-[#2563EB] animate-pulse shrink-0" />
          <h4 className="text-xs font-bold tracking-wide text-[#0F172A] uppercase font-mono truncate">
            {displayTitle}
          </h4>
        </div>

        {/* Action Controls & Mode Switcher */}
        <div className="flex items-center gap-1.5 shrink-0">
          {callout && (
            <span className="hidden sm:inline-block text-[10px] font-mono px-2 py-0.5 rounded-md bg-[#EFF6FF] text-[#1D4ED8] border border-[#BFDBFE] truncate max-w-[160px]">
              {callout}
            </span>
          )}

          {/* Toggle Derivative Curve (dy/dx) */}
          {!isPieOnlyChart && compiledCurves.length > 0 && (
            <button
              onClick={() => setShowDerivative((prev) => !prev)}
              className={`px-2 py-0.5 rounded-md text-[10px] font-mono border transition-colors ${
                showDerivative
                  ? 'bg-[#EFF6FF] text-[#2563EB] border-[#93C5FD] font-bold shadow-xs'
                  : 'bg-white text-[#64748B] border-[#E2E8F0] hover:bg-[#F1F5F9] hover:text-[#0F172A]'
              }`}
              title="Toggle first derivative f'(x)"
            >
              dy/dx
            </button>
          )}

          {/* Cartesian Zoom / Reset Controls */}
          {!isPieOnlyChart && (
            <>
              <button
                onClick={() => handleZoom(0.8)}
                className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                title="Zoom in graph"
              >
                <ZoomIn className="w-3.5 h-3.5" />
              </button>
              <button
                onClick={() => handleZoom(1.25)}
                className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                title="Zoom out graph"
              >
                <ZoomOut className="w-3.5 h-3.5" />
              </button>
              <button
                onClick={handleReset}
                className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                title="Reset coordinate axes"
              >
                <RotateCcw className="w-3.5 h-3.5" />
              </button>
            </>
          )}

          {/* Dock vs Floating toggle */}
          {onModeChange && (
            <>
              {displayMode !== 'docked' && (
                <button
                  onClick={() => onModeChange('docked')}
                  className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                  title="Dock graph to right side of chalkboard"
                >
                  <PanelRight className="w-3.5 h-3.5" />
                </button>
              )}
              {displayMode !== 'floating' && (
                <button
                  onClick={() => onModeChange('floating')}
                  className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                  title="Float graph as moveable box"
                >
                  <Move className="w-3.5 h-3.5" />
                </button>
              )}
              {displayMode !== 'maximized' ? (
                <button
                  onClick={() => onModeChange('maximized')}
                  className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                  title="Maximize graph full board"
                >
                  <Maximize2 className="w-3.5 h-3.5" />
                </button>
              ) : (
                <button
                  onClick={() => onModeChange('docked')}
                  className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                  title="Restore dock view"
                >
                  <Minimize2 className="w-3.5 h-3.5" />
                </button>
              )}
              <button
                onClick={() => onModeChange('minimized')}
                className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
                title="Minimize graph to pill"
              >
                <Minimize2 className="w-3.5 h-3.5" />
              </button>
            </>
          )}

          {/* Close button */}
          {onClose && (
            <button
              onClick={onClose}
              className="p-1.5 rounded-md text-[#94A3B8] hover:text-[#DC2626] hover:bg-[#FEE2E2] transition-colors ml-1 shadow-xs"
              title="Close graph view"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
        </div>
      </div>

      {/* 2. Formula Badges Strip: High-Taste Color Badges for Functions, Line Series & Segments */}
      {(compiledCurves.length > 0 || parsedLineSeries.length > 0 || compiledShadedRegions.length > 0 || parsedSegments.length > 0 || parsedPoints.length > 0 || isPieOnlyChart) && (
        <div className="px-3 py-1.5 bg-[#FFFFFF] border-b border-[#F1F5F9] flex flex-wrap items-center gap-2 text-xs font-mono shrink-0">
          {/* Function Badges */}
          {compiledCurves.map((curve, idx) => (
            <div
              key={`badge-curve-${idx}`}
              className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md text-[11px] font-semibold border shadow-2xs transition-all"
              style={{
                backgroundColor: `${curve.color}0D`,
                borderColor: `${curve.color}33`,
                color: curve.color,
              }}
            >
              <span className="w-2 h-2 rounded-full" style={{ backgroundColor: curve.color }} />
              <span>{curve.label}</span>
              {curve.domain && (
                <span className="text-[10px] opacity-75 font-normal">
                  [{curve.domain[0]}, {curve.domain[1]}]
                </span>
              )}
            </div>
          ))}

          {/* Discrete Line Series Badges */}
          {parsedLineSeries.map((series, idx) => (
            <div
              key={`badge-series-${idx}`}
              className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md text-[11px] font-semibold border shadow-2xs"
              style={{
                backgroundColor: `${series.fillColor || series.color || CURVE_COLORS[idx % CURVE_COLORS.length]}14`,
                borderColor: `${series.color || CURVE_COLORS[idx % CURVE_COLORS.length]}40`,
                color: series.color || CURVE_COLORS[idx % CURVE_COLORS.length],
              }}
            >
              <span className="w-2.5 h-0.5 rounded" style={{ backgroundColor: series.color || CURVE_COLORS[idx % CURVE_COLORS.length] }} />
              <span>{series.label || `Series ${idx + 1}`}</span>
            </div>
          ))}

          {/* Segment Badges */}
          {parsedSegments.map((seg, idx) => (
            <div
              key={`badge-seg-${idx}`}
              className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md text-[11px] font-semibold border shadow-2xs"
              style={{
                backgroundColor: `${seg.color}0D`,
                borderColor: `${seg.color}33`,
                color: seg.color,
              }}
            >
              <span className="w-3 h-0.5 rounded" style={{ backgroundColor: seg.color }} />
              <span>{seg.label || `Segment ${idx + 1}`}</span>
              <span className="text-[10px] opacity-75 font-normal">
                ({seg.start[0]}, {seg.start[1]}) → ({seg.end[0]}, {seg.end[1]})
              </span>
            </div>
          ))}

          {/* Key Points Badge Count */}
          {parsedPoints.length > 0 && (
            <div className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[10px] font-medium bg-[#F1F5F9] text-[#475569] border border-[#E2E8F0]">
              <span className="w-1.5 h-1.5 rounded-full bg-[#DC2626]" />
              <span>{parsedPoints.length} Critical Points</span>
            </div>
          )}

          {/* Pie Chart Summary Pill */}
          {isPieOnlyChart && (
            <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md text-[11px] font-semibold bg-[#EFF6FF] text-[#1D4ED8] border border-[#BFDBFE]">
              <BarChart2 className="w-3 h-3" />
              <span>Total: {pieTotal} ({parsedPies.length} categories)</span>
            </div>
          )}
        </div>
      )}

      {/* 3. High-Precision Interactive Vector Graph / Pie Chart Viewport (Pure White Chalkboard Theme) */}
      <div className="flex-1 w-full bg-[#FFFFFF] relative flex justify-center items-center overflow-hidden mafs-white-viewport">
        {isPieOnlyChart ? (
          <div className="w-full h-full flex flex-col sm:flex-row items-center justify-center gap-6 p-5 overflow-y-auto bg-white">
            {pieTotal <= 0 ? (
              <p className="text-xs text-[#64748B] font-mono">No positive slice values to chart.</p>
            ) : (
              <>
                <svg viewBox="0 0 220 220" className="w-52 h-52 sm:w-60 sm:h-60 shrink-0 drop-shadow-xs" aria-label={displayTitle}>
                  {(() => {
                    const cx = 110
                    const cy = 110
                    const r = 90
                    const sweepProgress = prefersReducedMotion ? 1 : animT
                    const maxSweepAngle = -Math.PI / 2 + 2 * Math.PI * sweepProgress
                    let accFraction = 0

                    return parsedPies.map((slice, idx) => {
                      const val = Math.max(0, slice.value)
                      const fraction = val / pieTotal
                      const sliceColor = slice.color || CURVE_COLORS[idx % CURVE_COLORS.length]
                      const fullStart = accFraction * 2 * Math.PI - Math.PI / 2
                      const fullEnd = (accFraction + fraction) * 2 * Math.PI - Math.PI / 2
                      accFraction += fraction

                      const visibleEnd = Math.min(fullEnd, maxSweepAngle)
                      if (fraction <= 0 || visibleEnd <= fullStart) return null

                      const spanAngle = visibleEnd - fullStart
                      const midAngle = (fullStart + fullEnd) / 2
                      const labelX = cx + r * 0.62 * Math.cos(midAngle)
                      const labelY = cy + r * 0.62 * Math.sin(midAngle)
                      const pctLabel = `${Math.round(fraction * 1000) / 10}%`

                      if (spanAngle >= 2 * Math.PI - 0.002) {
                        return (
                          <g key={`pie-slice-${idx}`}>
                            <circle cx={cx} cy={cy} r={r} fill={sliceColor} stroke="#FFFFFF" strokeWidth={2} />
                            {animT >= 0.7 && (
                              <text x={cx} y={cy} textAnchor="middle" dominantBaseline="central" fill="#FFFFFF" fontSize="12" fontWeight="700">
                                {pctLabel}
                              </text>
                            )}
                          </g>
                        )
                      }

                      const x1 = cx + r * Math.cos(fullStart)
                      const y1 = cy + r * Math.sin(fullStart)
                      const x2 = cx + r * Math.cos(visibleEnd)
                      const y2 = cy + r * Math.sin(visibleEnd)
                      const largeArc = spanAngle > Math.PI ? 1 : 0
                      const pathD = `M ${cx} ${cy} L ${x1.toFixed(2)} ${y1.toFixed(2)} A ${r} ${r} 0 ${largeArc} 1 ${x2.toFixed(2)} ${y2.toFixed(2)} Z`

                      return (
                        <g key={`pie-slice-${idx}`} className="transition-opacity hover:opacity-90">
                          <path d={pathD} fill={sliceColor} stroke="#FFFFFF" strokeWidth={2} />
                          {fullEnd - fullStart >= 0.35 && animT >= 0.7 && (
                            <text
                              x={labelX}
                              y={labelY}
                              textAnchor="middle"
                              dominantBaseline="central"
                              fill="#FFFFFF"
                              fontSize="11"
                              fontWeight="700"
                            >
                              {pctLabel}
                            </text>
                          )}
                        </g>
                      )
                    })
                  })()}
                </svg>

                <div className="flex flex-col gap-2 w-full max-w-[240px]">
                  {parsedPies.map((slice, idx) => {
                    const sliceColor = slice.color || CURVE_COLORS[idx % CURVE_COLORS.length]
                    const val = Math.max(0, slice.value)
                    const pct = pieTotal > 0 ? Math.round((val / pieTotal) * 1000) / 10 : 0
                    const deg = pieTotal > 0 ? Math.round((val / pieTotal) * 3600) / 10 : 0
                    return (
                      <div
                        key={`pie-legend-${idx}`}
                        className="flex items-center justify-between gap-3 px-2.5 py-1.5 rounded-lg bg-[#F8FAFC] border border-[#E2E8F0] text-xs"
                      >
                        <div className="flex items-center gap-2 min-w-0">
                          <span className="w-3 h-3 rounded-sm shrink-0" style={{ backgroundColor: sliceColor }} />
                          <span className="font-semibold text-[#0F172A] truncate">{slice.label}</span>
                        </div>
                        <div className="font-mono text-[11px] text-[#475569] shrink-0">
                          {slice.value} ({pct}% • {deg}°)
                        </div>
                      </div>
                    )
                  })}
                </div>
              </>
            )}
          </div>
        ) : (
        <>
        {/* Scoped CSS to enforce Crisp White Theme, Clear Axis Ticks & High Legibility */}
        <style dangerouslySetInnerHTML={{ __html: `
          .mafs-white-viewport .MafsView {
            --mafs-bg: #FFFFFF !important;
            --mafs-fg: #0F172A !important;
            --mafs-origin-color: #0F172A !important;
            --mafs-line-color: #E2E8F0 !important;
            --grid-line-subdivision-color: #F8FAFC !important;
            background: #FFFFFF !important;
          }
          .mafs-white-viewport .MafsView text {
            fill: #1E293B !important;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace !important;
            font-weight: 600 !important;
            font-size: 11px !important;
          }
          .mafs-white-viewport .MafsView line {
            stroke-opacity: 0.85 !important;
          }
        `}} />
        
        <Mafs
          viewBox={{ x: viewDomain, y: viewRange }}
          preserveAspectRatio={false}
          height={resolvedHeight}
          pan={true}
          zoom={{ min: 0.1, max: 10 }}
        >
          {/* High-Resolution Cartesian Grid with Visible Tick Labels */}
          <Coordinates.Cartesian
            subdivisions={2}
            xAxis={{ lines: 1, labels: (x) => (x !== 0 ? `${x}` : '') }}
            yAxis={{ lines: 1, labels: (y) => (y !== 0 ? `${y}` : '') }}
          />

          {/* Shaded Area Under / Between Curves (Smooth Sweep Fill) */}
          {compiledShadedRegions.map((reg, idx) => {
            const regDomain = reg.domain || viewDomain
            const polyPts = buildShadedRegionPolygon(
              reg.upperFn,
              reg.lowerFn,
              regDomain,
              prefersReducedMotion ? 1 : animT
            )
            if (polyPts.length < 3) return null
            const midX = (regDomain[0] + regDomain[1]) / 2
            const midY = reg.upperFn(midX)
            return (
              <React.Fragment key={`shaded-region-${idx}`}>
                <Polygon
                  points={polyPts}
                  color={reg.fillColor}
                  fillOpacity={reg.fillOpacity}
                  weight={0}
                />
                {reg.label && animT >= 0.8 && Number.isFinite(midY) && (
                  <Text x={midX} y={midY * 0.5} color="#0F172A" size={11}>
                    {reg.label}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Multi-Function Curves (Simultaneous Multi-Graph Support with Optional Fill & Smooth Sweep) */}
          {compiledCurves.map((curve, idx) => {
            const fullDomain = curve.domain || viewDomain
            const span = fullDomain[1] - fullDomain[0]
            const activeDomain: [number, number] =
              animT >= 0.995 || prefersReducedMotion
                ? fullDomain
                : [fullDomain[0], fullDomain[0] + span * Math.max(0.03, animT)]
            const fillPts = curve.filled
              ? buildShadedRegionPolygon(curve.fn, null, fullDomain, prefersReducedMotion ? 1 : animT)
              : []
            return (
              <React.Fragment key={`curve-${idx}-${curve.raw}`}>
                {fillPts.length >= 3 && (
                  <Polygon
                    points={fillPts}
                    color={curve.fillColor || curve.color}
                    fillOpacity={curve.fillOpacity ?? 0.2}
                    weight={0}
                  />
                )}
                <Plot.OfX
                  y={curve.fn}
                  color={curve.color}
                  weight={3}
                  domain={activeDomain}
                />
              </React.Fragment>
            )
          })}

          {/* Discrete Multi-Point Line Graph Series with Optional Shaded Color Fill */}
          {parsedLineSeries.map((series, idx) => {
            const pts = series.points
            if (pts.length < 2) return null
            const progress = prefersReducedMotion ? 1 : animT
            const totalSegs = pts.length - 1
            const segProgress = progress * totalSegs
            const fullIdx = Math.floor(segProgress)
            const frac = segProgress - fullIdx
            const visiblePts: [number, number][] = pts.slice(0, fullIdx + 1)
            if (fullIdx < totalSegs) {
              const p0 = pts[fullIdx]
              const p1 = pts[fullIdx + 1]
              visiblePts.push([p0[0] + (p1[0] - p0[0]) * frac, p0[1] + (p1[1] - p0[1]) * frac])
            }
            const sColor = series.color || CURVE_COLORS[idx % CURVE_COLORS.length]
            const sFillColor = series.fillColor || sColor
            const fillPolygonPts: [number, number][] =
              series.filled && visiblePts.length >= 2
                ? [
                    [visiblePts[0][0], 0],
                    ...visiblePts,
                    [visiblePts[visiblePts.length - 1][0], 0],
                  ]
                : []
            return (
              <React.Fragment key={`line-series-${idx}`}>
                {fillPolygonPts.length >= 4 && (
                  <Polygon
                    points={fillPolygonPts}
                    color={sFillColor}
                    fillOpacity={series.fillOpacity ?? 0.22}
                    weight={0}
                  />
                )}
                {visiblePts.length >= 2 && (
                  series.dashed ? (
                    visiblePts.slice(0, -1).map((pt, segIdx) => (
                      <Line.Segment
                        key={`series-${idx}-seg-${segIdx}`}
                        point1={pt}
                        point2={visiblePts[segIdx + 1]}
                        color={sColor}
                        style="dashed"
                        weight={2.5}
                      />
                    ))
                  ) : (
                    <Polyline
                      points={visiblePts}
                      color={sColor}
                      weight={2.5}
                    />
                  )
                )}
                {pts.map((pt, pIdx) =>
                  progress >= pIdx / totalSegs ? (
                    <Point
                      key={`series-${idx}-pt-${pIdx}`}
                      x={pt[0]}
                      y={pt[1]}
                      color={sColor}
                      svgCircleProps={{ r: 4.5, stroke: '#FFFFFF', strokeWidth: 1.5 }}
                    />
                  ) : null
                )}
                {series.label && progress >= 0.85 && (
                  <Text
                    x={pts[pts.length - 1][0]}
                    y={pts[pts.length - 1][1] + 0.45}
                    color={sColor}
                    size={11}
                  >
                    {series.label}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Line Segments with Smooth Lerp Draw-In & Stopping Points */}
          {parsedSegments.map((seg, idx) => {
            const isSettled = animT >= 0.995 || prefersReducedMotion
            const curEnd: [number, number] = isSettled
              ? seg.end
              : [
                  seg.start[0] + (seg.end[0] - seg.start[0]) * animT,
                  seg.start[1] + (seg.end[1] - seg.start[1]) * animT,
                ]
            return (
              <React.Fragment key={`segment-${idx}`}>
                {/* Segment Line */}
                {isSettled ? (
                  <Line.Segment
                    point1={seg.start}
                    point2={seg.end}
                    color={seg.color}
                    style={seg.dashed ? 'dashed' : 'solid'}
                    weight={3}
                  />
                ) : (
                  <Line.Segment
                    point1={seg.start}
                    point2={curEnd}
                    color={seg.color}
                    style={seg.dashed ? 'dashed' : 'solid'}
                    weight={3}
                  />
                )}
                {/* Start Point (Filled Circle with White Border) */}
                <Point
                  x={seg.start[0]}
                  y={seg.start[1]}
                  color={seg.color}
                  svgCircleProps={{ r: 6 * Math.min(1, animT * 2.5), stroke: '#FFFFFF', strokeWidth: 2 }}
                />
                {/* End Point (Hollow Circle with Colored Border - Explicit Stopping Point) */}
                {animT >= 0.35 && (
                  <Point
                    x={curEnd[0]}
                    y={curEnd[1]}
                    color="#FFFFFF"
                    svgCircleProps={{ r: 6, fill: '#FFFFFF', stroke: seg.color, strokeWidth: 2.5 }}
                  />
                )}
                {/* Segment Midpoint Label if specified */}
                {seg.label && animT >= 0.65 && (
                  <Text
                    x={(seg.start[0] + seg.end[0]) / 2}
                    y={(seg.start[1] + seg.end[1]) / 2 + 0.35}
                    color={seg.color}
                    size={12}
                  >
                    {seg.label}
                  </Text>
                )}
                {/* Start & End Coordinate Badges */}
                {animT >= 0.3 && (
                  <Text
                    x={seg.start[0]}
                    y={seg.start[1] - 0.4}
                    color="#475569"
                    size={11}
                  >
                    {`(${seg.start[0]}, ${seg.start[1]})`}
                  </Text>
                )}
                {animT >= 0.8 && (
                  <Text
                    x={seg.end[0]}
                    y={seg.end[1] + 0.4}
                    color="#475569"
                    size={11}
                  >
                    {`(${seg.end[0]}, ${seg.end[1]})`}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Derivative Curve if toggled (Scholar Emerald Green Dashed) */}
          {showDerivative && derivativeFn && (
            <Plot.OfX
              y={derivativeFn}
              color="#16A34A"
              weight={2}
              style="dashed"
            />
          )}

          {/* Key Critical Points with Staged Reveal */}
          {parsedPoints.map((pt, idx) => {
            const pointT = prefersReducedMotion ? 1 : Math.min(1, Math.max(0, (animT - idx * 0.05) * 1.8))
            if (pointT <= 0.05) return null
            const hasCoordsInLabel = pt.label && pt.label.includes('(')
            const labelText = pt.label && pt.callout
              ? `${pt.label} [${pt.callout}]`
              : pt.label || pt.callout || ''
            const fullText = labelText
              ? (hasCoordsInLabel ? labelText : `${labelText} (${pt.x}, ${pt.y})`)
              : `(${pt.x}, ${pt.y})`

            return (
              <React.Fragment key={`point-${idx}`}>
                <Point
                  x={pt.x}
                  y={pt.y}
                  color={pt.color || '#DC2626'}
                  svgCircleProps={{ r: 6.5 * pointT, stroke: '#FFFFFF', strokeWidth: 2 }}
                />
                <Point
                  x={pt.x}
                  y={pt.y}
                  color="#FFFFFF"
                  svgCircleProps={{ r: 2.5 * pointT, fill: '#FFFFFF' }}
                />
                {pointT >= 0.6 && (
                  <Text
                    x={pt.x}
                    y={pt.y + 0.45}
                    color="#0F172A"
                    size={12}
                  >
                    {fullText}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Auto Intersections if Multiple Curves are Active and Manual Points Absent */}
          {parsedPoints.length === 0 &&
            animT >= 0.75 &&
            autoIntersections.map(([ix, iy], idx) => (
              <React.Fragment key={`auto-intersect-${idx}`}>
                <Point
                  x={ix}
                  y={iy}
                  color="#DC2626"
                  svgCircleProps={{ r: 5, stroke: '#FFFFFF', strokeWidth: 1.5 }}
                />
                <Text
                  x={ix}
                  y={iy + 0.38}
                  color="#0F172A"
                  size={12}
                >
                  {`(${ix}, ${iy})`}
                </Text>
              </React.Fragment>
            ))}
          {/* Statistical Bar Graphs & Histograms (Smooth Height Growth + Custom Fill Color) */}
          {parsedBars.map((bar, idx) => {
            const x1 = bar.x1 ?? (bar.x != null && bar.width != null ? bar.x - bar.width / 2 : idx * 1.5 + 1 - 0.45)
            const x2 = bar.x2 ?? (bar.x != null && bar.width != null ? bar.x + bar.width / 2 : idx * 1.5 + 1 + 0.45)
            const barT = prefersReducedMotion ? 1 : Math.min(1, Math.max(0.02, (animT - idx * 0.04) / 0.75))
            const h = bar.height * barT
            const strokeColor = bar.color || bar.fillColor || CURVE_COLORS[idx % CURVE_COLORS.length]
            const fillColor = bar.fillColor || strokeColor
            const fillOp = bar.fillOpacity ?? 0.65
            const midX = (x1 + x2) / 2
            const barPts: [number, number][] = [
              [x1, 0],
              [x1, h],
              [x2, h],
              [x2, 0],
            ]

            return (
              <React.Fragment key={`bar-${idx}-${bar.label || idx}`}>
                {fillColor !== strokeColor ? (
                  <>
                    <Polygon points={barPts} color={fillColor} fillOpacity={fillOp} strokeOpacity={0} weight={0} />
                    <Polygon points={barPts} color={strokeColor} fillOpacity={0} weight={2} />
                  </>
                ) : (
                  <Polygon points={barPts} color={strokeColor} fillOpacity={fillOp} weight={2} />
                )}
                {barT >= 0.8 && (
                  <Text
                    x={midX}
                    y={bar.height + (bar.height >= 0 ? 0.45 : -0.45)}
                    color="#0F172A"
                    size={12}
                  >
                    {String(bar.height)}
                  </Text>
                )}
                {bar.label && (
                  <Text
                    x={midX}
                    y={-0.5}
                    color="#475569"
                    size={11}
                  >
                    {bar.label}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Physics Vectors & Arrows (Smooth Tail -> Tip Draw-In) */}
          {parsedVectors.map((vec, idx) => {
            const tail = vec.tail || [0, 0]
            const tip = vec.tip
            const isSettled = animT >= 0.995 || prefersReducedMotion
            const curTip: [number, number] = isSettled
              ? tip
              : [
                  tail[0] + (tip[0] - tail[0]) * Math.max(0.05, animT),
                  tail[1] + (tip[1] - tail[1]) * Math.max(0.05, animT),
                ]
            const vColor = vec.color || CURVE_COLORS[idx % CURVE_COLORS.length]
            return (
              <React.Fragment key={`vec-${idx}-${vec.label || idx}`}>
                <Vector
                  tail={tail}
                  tip={curTip}
                  color={vColor}
                  weight={vec.weight || 3}
                />
                {vec.label && animT >= 0.75 && (
                  <Text
                    x={tip[0] + 0.35}
                    y={tip[1] + 0.35}
                    color={vColor}
                    size={12}
                  >
                    {vec.label}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Geometric Polygons in Cartesian Space (Progressive Perimeter Trace + Custom Fill) */}
          {parsedPolygons.map((poly, idx) => {
            const isSettled = animT >= 0.995 || prefersReducedMotion
            const polyColor = poly.color || '#7C3AED'
            const polyFill = poly.fillColor || polyColor
            const polyFillOpacity = poly.fillOpacity ?? 0.28
            if (isSettled) {
              return (
                <React.Fragment key={`poly-${idx}`}>
                  {polyFill !== polyColor ? (
                    <>
                      <Polygon points={poly.points} color={polyFill} fillOpacity={polyFillOpacity} strokeOpacity={0} weight={0} />
                      <Polygon points={poly.points} color={polyColor} fillOpacity={0} weight={2} />
                    </>
                  ) : (
                    <Polygon
                      points={poly.points}
                      color={polyColor}
                      fillOpacity={polyFillOpacity}
                      weight={2}
                    />
                  )}
                  {poly.label && (
                    <Text
                      x={poly.points.reduce((acc, p) => acc + p[0], 0) / poly.points.length}
                      y={poly.points.reduce((acc, p) => acc + p[1], 0) / poly.points.length}
                      color="#0F172A"
                      size={12}
                    >
                      {poly.label}
                    </Text>
                  )}
                </React.Fragment>
              )
            }
            const closedPts = [...poly.points, poly.points[0]]
            const totalEdges = closedPts.length - 1
            const edgeProgress = animT * totalEdges
            const completedEdges = Math.floor(edgeProgress)
            const partialFrac = edgeProgress - completedEdges
            const tracedPts: [number, number][] = closedPts.slice(0, completedEdges + 1)
            if (completedEdges < totalEdges) {
              const pA = closedPts[completedEdges]
              const pB = closedPts[completedEdges + 1]
              tracedPts.push([
                pA[0] + (pB[0] - pA[0]) * partialFrac,
                pA[1] + (pB[1] - pA[1]) * partialFrac,
              ])
            }
            const fillFade = Math.max(0, (animT - 0.65) / 0.35)
            return (
              <React.Fragment key={`poly-${idx}`}>
                {fillFade > 0 && (
                  <Polygon
                    points={poly.points}
                    color={polyFill}
                    fillOpacity={polyFillOpacity * fillFade}
                    strokeOpacity={0}
                    weight={0}
                  />
                )}
                {tracedPts.length >= 2 && (
                  <Polyline
                    points={tracedPts}
                    color={polyColor}
                    weight={2.5}
                  />
                )}
                {poly.label && animT >= 0.8 && (
                  <Text
                    x={poly.points.reduce((acc, p) => acc + p[0], 0) / poly.points.length}
                    y={poly.points.reduce((acc, p) => acc + p[1], 0) / poly.points.length}
                    color="#0F172A"
                    size={12}
                  >
                    {poly.label}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Geometric Circles in Cartesian Space (Smooth Compass Arc Sweep + Custom Fill) */}
          {parsedCircles.map((c, idx) => {
            const isSettled = animT >= 0.995 || prefersReducedMotion
            const cColor = c.color || '#2563EB'
            const cFill = c.fillColor || cColor
            const cFillOpacity = c.fillOpacity ?? 0.16
            if (isSettled) {
              return (
                <React.Fragment key={`circle-${idx}`}>
                  {cFill !== cColor ? (
                    <>
                      <Circle center={c.center} radius={c.radius} color={cFill} fillOpacity={cFillOpacity} strokeOpacity={0} weight={0} />
                      <Circle center={c.center} radius={c.radius} color={cColor} fillOpacity={0} weight={2} />
                    </>
                  ) : (
                    <Circle
                      center={c.center}
                      radius={c.radius}
                      color={cColor}
                      fillOpacity={cFillOpacity}
                      weight={2}
                    />
                  )}
                  <Point
                    x={c.center[0]}
                    y={c.center[1]}
                    color={cColor}
                    svgCircleProps={{ r: 4, stroke: '#FFFFFF', strokeWidth: 1.5 }}
                  />
                  {c.label && (
                    <Text
                      x={c.center[0]}
                      y={c.center[1] + c.radius + 0.4}
                      color="#0F172A"
                      size={12}
                    >
                      {c.label}
                    </Text>
                  )}
                </React.Fragment>
              )
            }
            const arcSteps = Math.max(6, Math.round(64 * animT))
            const maxAngle = 2 * Math.PI * animT
            const arcPts: [number, number][] = []
            for (let s = 0; s <= arcSteps; s++) {
              const theta = (s / arcSteps) * maxAngle
              arcPts.push([
                c.center[0] + c.radius * Math.cos(theta),
                c.center[1] + c.radius * Math.sin(theta),
              ])
            }
            const fillFade = Math.max(0, (animT - 0.7) / 0.3)
            return (
              <React.Fragment key={`circle-${idx}`}>
                {fillFade > 0 && (
                  <Circle
                    center={c.center}
                    radius={c.radius}
                    color={cFill}
                    fillOpacity={cFillOpacity * fillFade}
                    strokeOpacity={0}
                    weight={0}
                  />
                )}
                {arcPts.length >= 2 && (
                  <Polyline
                    points={arcPts}
                    color={cColor}
                    weight={2.5}
                  />
                )}
                <Point
                  x={c.center[0]}
                  y={c.center[1]}
                  color={cColor}
                  svgCircleProps={{ r: 4, stroke: '#FFFFFF', strokeWidth: 1.5 }}
                />
                {c.label && animT >= 0.75 && (
                  <Text
                    x={c.center[0]}
                    y={c.center[1] + c.radius + 0.4}
                    color="#0F172A"
                    size={12}
                  >
                    {c.label}
                  </Text>
                )}
              </React.Fragment>
            )
          })}

          {/* Custom Multiple Freeform Text Annotations in Cartesian Space */}
          {animT >= 0.7 && parsedTexts.map((txt, idx) => (
            <React.Fragment key={`custom-text-${idx}`}>
              <Text
                x={txt.x}
                y={txt.y}
                color={txt.color || '#0F172A'}
                size={txt.size || 12}
              >
                {txt.text}
              </Text>
            </React.Fragment>
          ))}
        </Mafs>
        </>
        )}
      </div>

      {/* 4. Coordinate Status Footer Bar with Legend & Viewport Details */}
      <div className="px-3.5 py-2 bg-[#F8FAFC] border-t border-[#E2E8F0] flex flex-wrap items-center justify-between gap-2 text-[11px] text-[#475569] font-mono shrink-0">
        <div className="flex items-center flex-wrap gap-3">
          {compiledCurves.map((curve, idx) => (
            <span key={idx} className="flex items-center gap-1.5 font-bold text-[#0F172A]">
              <span className="w-2.5 h-2.5 rounded-full ring-2 ring-slate-200" style={{ backgroundColor: curve.fillColor || curve.color }} />
              <span>{curve.label}</span>
            </span>
          ))}
          {parsedLineSeries.map((series, idx) => (
            <span key={`footer-series-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-2.5 rounded-sm" style={{ backgroundColor: series.fillColor || series.color || CURVE_COLORS[idx % CURVE_COLORS.length] }} />
              <span>{series.label || `Series ${idx + 1}`}</span>
            </span>
          ))}
          {compiledShadedRegions.map((reg, idx) => (
            <span key={`footer-shade-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-2.5 rounded-sm" style={{ backgroundColor: reg.fillColor }} />
              <span>{reg.label || `Shaded Region ${idx + 1}`}</span>
            </span>
          ))}
          {parsedSegments.map((seg, idx) => (
            <span key={`footer-seg-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-1 rounded" style={{ backgroundColor: seg.color }} />
              <span>{seg.label || `Seg ${idx + 1}`}</span>
            </span>
          ))}
          {parsedBars.map((bar, idx) => (
            <span key={`footer-bar-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-2.5 rounded-sm" style={{ backgroundColor: bar.fillColor || bar.color || CURVE_COLORS[idx % CURVE_COLORS.length] }} />
              <span>{bar.label ? `${bar.label}: ${bar.height}` : `Bar ${idx + 1}: ${bar.height}`}</span>
            </span>
          ))}
          {parsedVectors.map((vec, idx) => (
            <span key={`footer-vec-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-3 h-0.5" style={{ backgroundColor: vec.color || CURVE_COLORS[idx % CURVE_COLORS.length] }} />
              <span>{vec.label || `Vector ${idx + 1}`}</span>
            </span>
          ))}
          {parsedPolygons.map((poly, idx) => (
            <span key={`footer-poly-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-2.5 rounded-xs" style={{ backgroundColor: poly.fillColor || poly.color || '#7C3AED' }} />
              <span>{poly.label || `Polygon (${poly.points.length}v)`}</span>
            </span>
          ))}
          {parsedCircles.map((c, idx) => (
            <span key={`footer-circle-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-2.5 rounded-full border" style={{ backgroundColor: `${c.fillColor || c.color || '#2563EB'}33`, borderColor: c.color || '#2563EB' }} />
              <span>{c.label || `Circle (r=${c.radius})`}</span>
            </span>
          ))}
          {isPieOnlyChart && parsedPies.map((slice, idx) => (
            <span key={`footer-pie-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: slice.color || CURVE_COLORS[idx % CURVE_COLORS.length] }} />
              <span>{slice.label}: {slice.value}</span>
            </span>
          ))}
          {parsedTexts.length > 0 && (
            <span className="text-[#64748B] text-[10px] hidden sm:inline">
              ({parsedTexts.length} annotations)
            </span>
          )}
          {showDerivative && !isPieOnlyChart && (
            <span className="text-[#16A34A] text-[10px] font-semibold hidden sm:inline">(dashed: dy/dx)</span>
          )}
          {autoIntersections.length > 0 && parsedPoints.length === 0 && !isPieOnlyChart && (
            <span className="text-[#DC2626] text-[10px] font-semibold hidden sm:inline">
              (Auto Intersections: {autoIntersections.length})
            </span>
          )}
        </div>
        <div className="text-[10px] text-[#64748B]">
          {isPieOnlyChart
            ? `Slices: ${parsedPies.length} | Total: ${pieTotal}`
            : `x: [${viewDomain[0].toFixed(1)}, ${viewDomain[1].toFixed(1)}] | y: [${viewRange[0].toFixed(1)}, ${viewRange[1].toFixed(1)}]`}
        </div>
      </div>
    </div>
  )
}
