/**
 * boardLayout.ts - Pure geometry helpers for non-overlapping whiteboard element placement.
 * Guarantees images, diagrams, boxes, and notes stay strictly below titles/underlines
 * and never collide on narrow or wide canvases.
 */

export const BOARD_FONT_FAMILY = 5 as const // Excalidraw FontFamily.Excalifont

export interface BoardRect {
  x: number
  y: number
  right: number
  bottom: number
}

export interface ImagePlacementResult {
  x: number
  y: number
  width: number
  height: number
  dockedRight: boolean
  titleBottomY: number
}

function estimateElementHeight(el: any): number {
  if (typeof el?.height === 'number' && el.height > 0) return el.height
  if (el?.type === 'line') {
    const pts = Array.isArray(el.points) ? el.points : []
    const ys = pts.map((p: any) => (Array.isArray(p) ? Number(p[1] || 0) : 0))
    const span = ys.length > 0 ? Math.max(...ys) - Math.min(...ys) : 0
    return Math.max(4, span)
  }
  if (el?.type === 'text' && el.text) {
    const lines = String(el.text).split('\n').length
    const fs = Number(el.fontSize || 16)
    return lines * Math.round(fs * 1.35) + 8
  }
  if (el?.type === 'rectangle') return 60
  return 30
}

function estimateElementWidth(el: any): number {
  if (typeof el?.width === 'number' && el.width > 0) return el.width
  if (el?.type === 'line') {
    const pts = Array.isArray(el.points) ? el.points : []
    const xs = pts.map((p: any) => (Array.isArray(p) ? Number(p[0] || 0) : 0))
    return xs.length > 0 ? Math.max(0, Math.max(...xs) - Math.min(...xs)) : 0
  }
  if (el?.type === 'text' && el.text) {
    const longest = Math.max(...String(el.text).split('\n').map((l) => l.length))
    return Math.ceil(longest * Number(el.fontSize || 16) * 0.62)
  }
  return 120
}

export function getTitleBottomY(elements: any[]): number {
  if (!Array.isArray(elements) || elements.length === 0) return 40
  let maxBottom = 40
  for (const el of elements) {
    if (!el || el.isDeleted) continue
    if (el.customData?.isTitle === true || el.id?.startsWith('header_')) {
      const top = typeof el.y === 'number' ? el.y : 40
      const bottom = top + estimateElementHeight(el)
      if (bottom > maxBottom) maxBottom = bottom
    }
  }
  return maxBottom
}

export function getRightDockedBounds(elements: any[]): BoardRect | null {
  if (!Array.isArray(elements) || elements.length === 0) return null
  for (const el of elements) {
    if (!el || el.isDeleted) continue
    if (el.customData?.isRightDocked === true || (el.type === 'image' && typeof el.x === 'number' && el.x >= 440)) {
      const x = Number(el.x || 0)
      const y = Number(el.y || 0)
      const w = estimateElementWidth(el)
      const h = estimateElementHeight(el)
      return { x, y, right: x + w, bottom: y + h }
    }
  }
  return null
}

export function computeImagePlacement(params: {
  existingElements: any[]
  startX: number
  startY: number
  inlineStartY: number
  imgWidth: number
  imgHeight: number
  maxInlineWidth: number
  wrapFactor: number
  canvasWidth?: number
}): ImagePlacementResult {
  const {
    existingElements,
    startX,
    startY,
    inlineStartY,
    imgWidth,
    imgHeight,
    maxInlineWidth,
    wrapFactor,
    canvasWidth = 900,
  } = params

  const titleBottomY = getTitleBottomY(existingElements)
  const hasRightImage = Boolean(getRightDockedBounds(existingElements))
  const minClearY = Math.max(titleBottomY + 22, 102)

  // Only dock side-by-side on sufficiently wide boards where two columns won't cramp text
  const canTryRightDock =
    wrapFactor >= 0.72 &&
    !hasRightImage &&
    startY <= Math.max(titleBottomY + 200, 280)

  if (canTryRightDock) {
    const dockW = Math.min(370, imgWidth)
    const dockH = Math.min(270, Math.round(imgHeight * (dockW / Math.max(1, imgWidth))))
    // On extra-wide screens shift image slightly right so left notes get generous horizontal room
    const rightX = Math.max(490, Math.min(680, Math.round(canvasWidth - dockW - 24)))
    let dockY = minClearY

    // Advance dockY past any non-title content whose horizontal bounds enter the right zone
    const collidingEls = (existingElements || []).filter((el) => {
      if (!el || el.isDeleted) return false
      if (el.customData?.isRough === true || el.customData?.isTitle === true || el.id?.startsWith('header_')) {
        return false
      }
      if (typeof el.x !== 'number' || typeof el.y !== 'number') return false
      const elRight = el.x + estimateElementWidth(el)
      return el.x < rightX + dockW + 12 && elRight > rightX - 18
    })

    let adjusted = true
    while (adjusted) {
      adjusted = false
      for (const el of collidingEls) {
        const elTop = Number(el.y)
        const elBottom = elTop + estimateElementHeight(el)
        if (elTop < dockY + dockH + 12 && elBottom > dockY - 12) {
          dockY = elBottom + 18
          adjusted = true
        }
      }
    }

    if (dockY <= Math.max(titleBottomY + 220, 300)) {
      return {
        x: rightX,
        y: dockY,
        width: dockW,
        height: dockH,
        dockedRight: true,
        titleBottomY,
      }
    }
  }

  const finalY = Math.max(inlineStartY, minClearY)
  const finalX = startX + Math.max(0, Math.round((maxInlineWidth - imgWidth) / 2))
  return {
    x: finalX,
    y: finalY,
    width: imgWidth,
    height: imgHeight,
    dockedRight: false,
    titleBottomY,
  }
}
