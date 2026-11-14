/**
 * textWrapper.ts - Whitespace and hyphenation wrapping engine for whiteboard cards
 * Guarantees zero text spillage outside card boundaries (CBSE/ICSE/IB layouts)
 */

import { cleanChalkboardTypography } from './chalkboardTypography'

export { cleanChalkboardTypography }

export function wrapText(text: string, maxCharsPerLine = 70): string[] {
  if (!text || !text.trim()) return []
  const cleaned = cleanChalkboardTypography(text)
  const normalized = cleaned.replace(/\r\n/g, '\n').replace(/\r/g, '\n')
  const paragraphs = normalized.split('\n')
  const result: string[] = []

  for (const para of paragraphs) {
    const trimmedPara = para.trim()
    if (!trimmedPara) {
      result.push('')
      continue
    }

    const words = trimmedPara.split(/\s+/)
    let currentLine = ''

    for (let rawWord of words) {
      // Hyphenate oversized tokens
      while (rawWord.length > maxCharsPerLine) {
        const splitIndex = Math.max(1, maxCharsPerLine - 1)
        const chunk = rawWord.slice(0, splitIndex) + '-'
        if (currentLine) {
          result.push(currentLine)
          currentLine = ''
        }
        result.push(chunk)
        rawWord = rawWord.slice(splitIndex)
      }

      if (!currentLine) {
        currentLine = rawWord
      } else if (currentLine.length + 1 + rawWord.length <= maxCharsPerLine) {
        currentLine += ' ' + rawWord
      } else {
        result.push(currentLine)
        currentLine = rawWord
      }
    }

    if (currentLine) {
      result.push(currentLine)
    }
  }

  while (result.length > 0 && result[result.length - 1] === '') {
    result.pop()
  }

  return result
}

let measureCtx: CanvasRenderingContext2D | null | undefined

/**
 * Measures text width in px using the board's hand-drawn font (Excalidraw fontFamily 1).
 * Falls back to a conservative per-character estimate when no canvas is available (SSR).
 */
export function measureBoardText(text: string, fontSize: number): number {
  if (measureCtx === undefined) {
    measureCtx = typeof document !== 'undefined' ? document.createElement('canvas').getContext('2d') : null
  }
  if (!measureCtx) return text.length * fontSize * 0.68
  measureCtx.font = `${fontSize}px Virgil, Excalifont, "Segoe UI Emoji", sans-serif`
  // Small safety margin: Excalidraw renders with slight stroke jitter
  return measureCtx.measureText(text).width * 1.04
}

/**
 * Pixel-accurate wrapping: guarantees every line fits inside maxWidth px at the given font size,
 * so text can never spill outside the card/box drawn around it.
 */
export function wrapTextToWidth(text: string, fontSize: number, maxWidth: number, maxLines?: number): string[] {
  if (!text || !text.trim()) return []
  const cleaned = cleanChalkboardTypography(text).replace(/\r\n?/g, '\n')
  const result: string[] = []

  for (const para of cleaned.split('\n')) {
    const words = para.trim().split(/\s+/).filter(Boolean)
    let line = ''
    for (let word of words) {
      // Hard-split tokens wider than the box (long URLs, formulas)
      while (measureBoardText(word, fontSize) > maxWidth && word.length > 1) {
        let cut = word.length - 1
        while (cut > 1 && measureBoardText(word.slice(0, cut) + '-', fontSize) > maxWidth) cut--
        if (line) { result.push(line); line = '' }
        result.push(word.slice(0, cut) + '-')
        word = word.slice(cut)
      }
      const candidate = line ? `${line} ${word}` : word
      if (!line || measureBoardText(candidate, fontSize) <= maxWidth) {
        line = candidate
      } else {
        result.push(line)
        line = word
      }
    }
    if (line) result.push(line)
  }

  if (maxLines && result.length > maxLines) {
    const kept = result.slice(0, maxLines)
    let last = kept[maxLines - 1]
    while (last.length > 1 && measureBoardText(`${last}…`, fontSize) > maxWidth) last = last.slice(0, -1)
    kept[maxLines - 1] = `${last.trimEnd()}…`
    return kept
  }
  return result
}
