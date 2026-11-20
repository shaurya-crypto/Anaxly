'use client'

import React, { useMemo, useState } from 'react'
import {
  Mafs,
  Coordinates,
  Plot,
  Line,
  Point,
  Text,
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
  Info
} from 'lucide-react'
import {
  parseGraphPoints,
  parseGraphSegments,
  parseGraphFormulas,
  type GraphFormulaItem,
  type GraphSegmentItem,
  type GraphPointItem,
} from '@/lib/graphGating'

export type GraphDisplayMode = 'docked' | 'floating' | 'maximized' | 'minimized'

export interface MafsGraphCanvasProps {
  formula?: string | string[] | GraphFormulaItem[]
  formulas?: Array<string | GraphFormulaItem>
  segments?: Array<GraphSegmentItem | string | any>
  points?: Array<[number, number] | GraphPointItem | string> | string
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

export function MafsGraphCanvas({
  formula,
  formulas,
  segments,
  points,
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

  // 4. Auto-fit initial view bounds to encompass all points, segment endpoints, and formula domains
  const autoBounds = useMemo<{ domain: [number, number]; range: [number, number] }>(() => {
    const xs: number[] = []
    const ys: number[] = []

    parsedPoints.forEach((p) => {
      xs.push(p.x)
      ys.push(p.y)
    })

    parsedSegments.forEach((s) => {
      xs.push(s.start[0], s.end[0])
      ys.push(s.start[1], s.end[1])
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
  }, [domain, range, parsedPoints, parsedSegments, rawFormulasList])

  // Interactive view bounds with local zoom & pan state
  const [viewDomain, setViewDomain] = useState<[number, number]>(autoBounds.domain)
  const [viewRange, setViewRange] = useState<[number, number]>(autoBounds.range)
  const [showDerivative, setShowDerivative] = useState(false)

  // Reset to initial bounds if incoming props or autoBounds change significantly
  React.useEffect(() => {
    setViewDomain(autoBounds.domain)
    setViewRange(autoBounds.range)
  }, [autoBounds.domain[0], autoBounds.domain[1], autoBounds.range[0], autoBounds.range[1]])

  // Compile all formulas into evaluable function curves with labels and domains
  const compiledCurves = useMemo(() => {
    return rawFormulasList
      .map((item, idx) => {
        const normalized = normalizeMathFormula(item.formula)
        if (!normalized) return null

        try {
          const expr = compile(normalized)
          const fn = (x: number): number => {
            try {
              const res = expr.evaluate({ x, e: Math.E, pi: Math.PI })
              return typeof res === 'number' && isFinite(res) ? res : NaN
            } catch {
              return NaN
            }
          }
          const rawClean = item.formula.replace(/^(?:y|f\(x\))\s*=\s*/i, '').trim()
          return {
            raw: rawClean,
            label: item.label || (rawFormulasList.length > 1 ? `y${idx + 1} = ${rawClean}` : `y = ${rawClean}`),
            fn,
            color: item.color || CURVE_COLORS[idx % CURVE_COLORS.length],
            domain: item.domain,
          }
        } catch {
          return null
        }
      })
      .filter((c): c is NonNullable<typeof c> => c !== null)
  }, [rawFormulasList])

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
  }

  const rawFormulaTitle = Array.isArray(formula)
    ? formula.map((f) => (typeof f === 'string' ? f : f?.formula)).filter(Boolean).join(', ')
    : typeof formula === 'string'
    ? formula
    : ''

  const displayTitle =
    title ||
    (compiledCurves.length > 1
      ? `Comparative Graphs (${compiledCurves.length} curves)`
      : compiledCurves.length === 1
      ? `Graph: ${compiledCurves[0].label}`
      : parsedSegments.length > 0
      ? `Coordinate Segments (${parsedSegments.length} segments)`
      : `Mathematical Graph: ${rawFormulaTitle || 'Functions'}`)

  const resolvedHeight =
    height || (displayMode === 'maximized' ? 640 : displayMode === 'docked' ? 500 : 400)

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
          {compiledCurves.length > 0 && (
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

          {/* Zoom In */}
          <button
            onClick={() => handleZoom(0.8)}
            className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
            title="Zoom in graph"
          >
            <ZoomIn className="w-3.5 h-3.5" />
          </button>

          {/* Zoom Out */}
          <button
            onClick={() => handleZoom(1.25)}
            className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
            title="Zoom out graph"
          >
            <ZoomOut className="w-3.5 h-3.5" />
          </button>

          {/* Reset Zoom */}
          <button
            onClick={handleReset}
            className="p-1.5 rounded-md bg-white border border-[#E2E8F0] text-[#475569] hover:text-[#0F172A] hover:bg-[#F1F5F9] transition-colors shadow-xs"
            title="Reset coordinate axes"
          >
            <RotateCcw className="w-3.5 h-3.5" />
          </button>

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

      {/* 2. Formula Badges Strip: High-Taste Color Badges for Functions & Segments */}
      {(compiledCurves.length > 0 || parsedSegments.length > 0 || parsedPoints.length > 0) && (
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
        </div>
      )}

      {/* 3. High-Precision Interactive Vector Graph Viewport (Pure White Chalkboard Theme) */}
      <div className="flex-1 w-full bg-[#FFFFFF] relative flex justify-center items-center overflow-hidden mafs-white-viewport">
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

          {/* Multi-Function Curves (Simultaneous Multi-Graph Support with Color Hierarchy) */}
          {compiledCurves.map((curve, idx) => (
            <React.Fragment key={`curve-${idx}-${curve.raw}`}>
              <Plot.OfX
                y={curve.fn}
                color={curve.color}
                weight={3}
                domain={curve.domain}
              />
            </React.Fragment>
          ))}

          {/* Line Segments with Start and End Stopping Points */}
          {parsedSegments.map((seg, idx) => (
            <React.Fragment key={`segment-${idx}`}>
              {/* Segment Line */}
              <Line.Segment
                point1={seg.start}
                point2={seg.end}
                color={seg.color}
                style={seg.dashed ? 'dashed' : 'solid'}
                weight={3}
              />
              {/* Start Point (Filled Circle with White Border) */}
              <Point
                x={seg.start[0]}
                y={seg.start[1]}
                color={seg.color}
                svgCircleProps={{ r: 6, stroke: '#FFFFFF', strokeWidth: 2 }}
              />
              {/* End Point (Hollow Circle with Colored Border - Explicit Stopping Point) */}
              <Point
                x={seg.end[0]}
                y={seg.end[1]}
                color="#FFFFFF"
                svgCircleProps={{ r: 6, fill: '#FFFFFF', stroke: seg.color, strokeWidth: 2.5 }}
              />
              {/* Segment Midpoint Label if specified */}
              {seg.label && (
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
              <Text
                x={seg.start[0]}
                y={seg.start[1] - 0.4}
                color="#475569"
                size={11}
              >
                {`(${seg.start[0]}, ${seg.start[1]})`}
              </Text>
              <Text
                x={seg.end[0]}
                y={seg.end[1] + 0.4}
                color="#475569"
                size={11}
              >
                {`(${seg.end[0]}, ${seg.end[1]})`}
              </Text>
            </React.Fragment>
          ))}

          {/* Derivative Curve if toggled (Scholar Emerald Green Dashed) */}
          {showDerivative && derivativeFn && (
            <Plot.OfX
              y={derivativeFn}
              color="#16A34A"
              weight={2}
              style="dashed"
            />
          )}

          {/* Key Critical Points with Callouts / Tooltips */}
          {parsedPoints.map((pt, idx) => {
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
                  svgCircleProps={{ r: 6.5, stroke: '#FFFFFF', strokeWidth: 2 }}
                />
                <Point
                  x={pt.x}
                  y={pt.y}
                  color="#FFFFFF"
                  svgCircleProps={{ r: 2.5, fill: '#FFFFFF' }}
                />
                <Text
                  x={pt.x}
                  y={pt.y + 0.45}
                  color="#0F172A"
                  size={12}
                >
                  {fullText}
                </Text>
              </React.Fragment>
            )
          })}

          {/* Auto Intersections if Multiple Curves are Active and Manual Points Absent */}
          {parsedPoints.length === 0 &&
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
        </Mafs>
      </div>

      {/* 4. Coordinate Status Footer Bar with Legend & Viewport Details */}
      <div className="px-3.5 py-2 bg-[#F8FAFC] border-t border-[#E2E8F0] flex flex-wrap items-center justify-between gap-2 text-[11px] text-[#475569] font-mono shrink-0">
        <div className="flex items-center flex-wrap gap-3">
          {compiledCurves.map((curve, idx) => (
            <span key={idx} className="flex items-center gap-1.5 font-bold text-[#0F172A]">
              <span className="w-2.5 h-2.5 rounded-full ring-2 ring-slate-200" style={{ backgroundColor: curve.color }} />
              <span>{curve.label}</span>
            </span>
          ))}
          {parsedSegments.map((seg, idx) => (
            <span key={`footer-seg-${idx}`} className="flex items-center gap-1.5 text-[#334155]">
              <span className="w-2.5 h-1 rounded" style={{ backgroundColor: seg.color }} />
              <span>{seg.label || `Seg ${idx + 1}`}</span>
            </span>
          ))}
          {showDerivative && (
            <span className="text-[#16A34A] text-[10px] font-semibold hidden sm:inline">(dashed: dy/dx)</span>
          )}
          {autoIntersections.length > 0 && parsedPoints.length === 0 && (
            <span className="text-[#DC2626] text-[10px] font-semibold hidden sm:inline">
              (Auto Intersections: {autoIntersections.length})
            </span>
          )}
        </div>
        <div className="text-[10px] text-[#64748B]">
          x: [{viewDomain[0].toFixed(1)}, {viewDomain[1].toFixed(1)}] | y: [{viewRange[0].toFixed(1)}, {viewRange[1].toFixed(1)}]
        </div>
      </div>
    </div>
  )
}
