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
  GripHorizontal 
} from 'lucide-react'

export type GraphDisplayMode = 'docked' | 'floating' | 'maximized' | 'minimized'

export interface MafsGraphCanvasProps {
  formula?: string | string[]
  formulas?: string[]
  domain?: [number, number]
  range?: [number, number]
  title?: string
  callout?: string
  points?: Array<[number, number]> | string
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
  if (!raw) return 'x'
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
  formula = 'x^2 - 4',
  formulas,
  domain = [-5, 5],
  range = [-5, 5],
  title,
  callout,
  points,
  width = 'auto',
  height,
  displayMode = 'docked',
  onModeChange,
  onClose,
}: MafsGraphCanvasProps) {
  // Interactive view bounds with local zoom & pan state
  const [viewDomain, setViewDomain] = useState<[number, number]>(domain)
  const [viewRange, setViewRange] = useState<[number, number]>(range)
  const [showDerivative, setShowDerivative] = useState(false)

  // Reset to initial bounds if incoming props change significantly
  React.useEffect(() => {
    setViewDomain(domain)
    setViewRange(range)
  }, [domain[0], domain[1], range[0], range[1]])

  // Parse discrete points if string or array was provided
  const parsedPoints: [number, number][] = useMemo(() => {
    if (!points) return []
    if (Array.isArray(points)) return points
    const pts: [number, number][] = []
    const matches = points.matchAll(/\(\s*([\-\d\.]+)\s*,\s*([\-\d\.]+)\s*\)/g)
    for (const m of matches) {
      const px = parseFloat(m[1])
      const py = parseFloat(m[2])
      if (!isNaN(px) && !isNaN(py)) {
        pts.push([px, py])
      }
    }
    return pts
  }, [points])

  // Parse multiple formulas: supports array, semicolons, newlines, pipes, or "y = ... , y = ..."
  const formulasList = useMemo(() => {
    if (formulas && Array.isArray(formulas) && formulas.length > 0) {
      return formulas.filter(Boolean)
    }
    if (Array.isArray(formula)) {
      return formula.filter(Boolean)
    }
    if (!formula) return ['x^2 - 4']

    let parts: string[] = []
    if (formula.includes(';') || formula.includes('|') || formula.includes('\n')) {
      parts = formula.split(/[;|\n]+/).map((s) => s.trim()).filter(Boolean)
    } else if (formula.includes('and') || formula.includes('&')) {
      parts = formula.split(/\s*(?:and|&)\s*/i).map((s) => s.trim()).filter(Boolean)
    } else if (/y\s*=.*y\s*=/i.test(formula)) {
      // Split on comma before a new "y =" e.g. "y = x^2 - 4, y = 2x + 1"
      parts = formula.split(/,\s*(?=y\s*=)/i).map((s) => s.trim()).filter(Boolean)
    } else {
      parts = [formula.trim()]
    }
    return parts.length > 0 ? parts : [formula]
  }, [formula, formulas])

  // Compile all formulas into evaluable function curves
  const compiledCurves = useMemo(() => {
    return formulasList.map((f, idx) => {
      const normalized = normalizeMathFormula(f)
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
        return {
          raw: f.replace(/^(?:y|f\(x\))\s*=\s*/i, '').trim(),
          fn,
          color: CURVE_COLORS[idx % CURVE_COLORS.length],
        }
      } catch {
        return {
          raw: f,
          fn: (x: number) => x,
          color: CURVE_COLORS[idx % CURVE_COLORS.length],
        }
      }
    })
  }, [formulasList])

  const primaryFn = compiledCurves[0]?.fn || ((x: number) => x)

  // Numerical derivative function: f'(x) ≈ (f(x+h) - f(x-h)) / 2h
  const derivativeFn = useMemo(() => {
    const h = 0.0001
    return (x: number): number => {
      const y2 = primaryFn(x + h)
      const y1 = primaryFn(x - h)
      if (isNaN(y1) || isNaN(y2)) return NaN
      return (y2 - y1) / (2 * h)
    }
  }, [primaryFn])

  // Auto-detect intersection points when multiple curves are present
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

  const allDisplayPoints = parsedPoints.length > 0 ? parsedPoints : autoIntersections

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
    setViewDomain(domain)
    setViewRange(range)
  }

  const rawFormulaTitle = Array.isArray(formula) ? formula.join(', ') : formula
  const displayTitle = title || (compiledCurves.length > 1 
    ? `Multiple Graphs (${compiledCurves.length} curves)`
    : `Graph: y = ${rawFormulaTitle}`)
  const resolvedHeight = height || (displayMode === 'maximized' ? 620 : displayMode === 'docked' ? 480 : 380)

  return (
    <div className="w-full h-full relative flex flex-col bg-[#FFFFFF] border-2 border-[#E2E8F0] rounded-2xl overflow-hidden shadow-2xl text-[#0F172A] font-sans select-none">
      {/* Top Header & Move Handle Toolbar (Clean Scholastic White Theme) */}
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
            <span className="hidden sm:inline-block text-[10px] font-mono px-2 py-0.5 rounded-md bg-[#EFF6FF] text-[#1D4ED8] border border-[#BFDBFE] truncate max-w-[150px]">
              {callout}
            </span>
          )}

          {/* Toggle Derivative Curve */}
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

      {/* High-Precision Interactive Vector Graph Viewport (Pure White Chalkboard Theme) */}
      <div className="flex-1 w-full bg-[#FFFFFF] relative flex justify-center items-center overflow-hidden mafs-white-viewport">
        {/* Scoped CSS to strictly enforce White Theme on Mafs SVG canvas */}
        <style dangerouslySetInnerHTML={{ __html: `
          .mafs-white-viewport .MafsView {
            --mafs-bg: #FFFFFF !important;
            --mafs-fg: #0F172A !important;
            --mafs-origin-color: #0F172A !important;
            --mafs-line-color: #CBD5E1 !important;
            --grid-line-subdivision-color: #F1F5F9 !important;
            background: #FFFFFF !important;
          }
          .mafs-white-viewport .MafsView text {
            fill: #0F172A !important;
            font-family: 'JetBrains Mono', 'Segoe UI', system-ui, sans-serif !important;
            font-weight: 600 !important;
          }
          .mafs-white-viewport .MafsView line {
            stroke-opacity: 0.9 !important;
          }
        `}} />
        
        <Mafs
          viewBox={{ x: viewDomain, y: viewRange }}
          preserveAspectRatio={false}
          height={resolvedHeight}
          pan={true}
          zoom={{ min: 0.1, max: 10 }}
        >
          {/* High-Resolution Chalkboard Cartesian Grid */}
          <Coordinates.Cartesian
            subdivisions={2}
            xAxis={{ lines: 1, labels: (x) => (x !== 0 ? `${x}` : '') }}
            yAxis={{ lines: 1, labels: (y) => (y !== 0 ? `${y}` : '') }}
          />

          {/* Multi-Function Curves (Simultaneous Multi-Graph Support with Distinct Scholastic Colors) */}
          {compiledCurves.map((curve, idx) => (
            <React.Fragment key={`curve-${idx}-${curve.raw}`}>
              <Plot.OfX
                y={curve.fn}
                color={curve.color}
                weight={3}
              />
            </React.Fragment>
          ))}

          {/* Derivative Curve if toggled (Scholar Emerald Green Dashed) */}
          {showDerivative && (
            <Plot.OfX
              y={derivativeFn}
              color="#16A34A"
              weight={2}
              style="dashed"
            />
          )}

          {/* Critical / Intersect Points with Coordinates */}
          {allDisplayPoints.map(([px, py], idx) => (
            <React.Fragment key={idx}>
              <Point x={px} y={py} color="#DC2626" />
              <Text
                x={px}
                y={py + 0.35}
                color="#0F172A"
                size={13}
              >
                {`(${px}, ${py})`}
              </Text>
            </React.Fragment>
          ))}
        </Mafs>
      </div>

      {/* Coordinate Status Footer Bar with Multi-Curve Legend */}
      <div className="px-3.5 py-2 bg-[#F8FAFC] border-t border-[#E2E8F0] flex flex-wrap items-center justify-between gap-2 text-[11px] text-[#475569] font-mono shrink-0">
        <div className="flex items-center flex-wrap gap-3">
          {compiledCurves.map((curve, idx) => (
            <span key={idx} className="flex items-center gap-1.5 font-bold text-[#0F172A]">
              <span className="w-2.5 h-2.5 rounded-full ring-2 ring-slate-200" style={{ backgroundColor: curve.color }} />
              <span>y = {curve.raw}</span>
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
