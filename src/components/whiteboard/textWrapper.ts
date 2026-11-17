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

/**
 * Formats mathematical derivations, physics calculations, and numerical steps
 * ensuring ONE or AT MOST TWO concise steps per line, followed by a clean newline.
 * Prevents crowded single-line equations and dense walls of text on the digital chalkboard.
 */
export function formatChalkboardSteps(text: string, maxCharsPerLine = 60): string[] {
  if (!text || !text.trim()) return []
  const cleaned = cleanChalkboardTypography(text.trim())
  const rawLines = cleaned.replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n')
  const atomicChunks: string[] = []

  for (const line of rawLines) {
    const trimmed = line.trim()
    if (!trimmed) continue

    // 1. Split on explicit delimiters (semicolons, pipes)
    const delimiterParts = trimmed.split(/\s*[\;\|]\s*/).filter(Boolean)

    for (const part of delimiterParts) {
      // 2. Split on inline step markers if multiple steps were concatenated without semicolons
      // e.g. "Given: m = 2 kg Step 1: F = m × a Step 2: F = 10 N Answer: F = 10 N"
      const inlineParts = part
        .split(/(?<=[^\s])\s+(?=(?:Step\s*\d+|Given|To Find|Formula|Substitution|Calculation|Answer|Final Answer|Case\s*\d+|\([ivxlcdm\d]+\))\s*[:\.\-])/i)
        .filter(Boolean)

      for (const ip of inlineParts) {
        // 3. Chained implications (e.g. A => B => C => D)
        const arrowParts = ip.split(/\s*(?:=>|⇒|→)\s*/).filter(Boolean)
        if (arrowParts.length >= 3) {
          arrowParts.forEach((ap, idx) => {
            atomicChunks.push(idx === 0 ? ap.trim() : `⇒ ${ap.trim()}`)
          })
        } else {
          atomicChunks.push(ip.trim())
        }
      }
    }
  }

  // 4. Group atomic chunks into lines with ONE or AT MOST TWO concise steps per line
  const formattedLines: string[] = []
  let i = 0

  while (i < atomicChunks.length) {
    const current = atomicChunks[i]
    const next = i + 1 < atomicChunks.length ? atomicChunks[i + 1] : null

    // Check if current or next is an explicit labeled step or major section header
    const isCurrentMajor = /^(?:Given|Formula|To Find|Problem|Answer|Final Answer|Step\s*\d+|Case\s*\d+|\([ivxlcdm\d]+\))\s*[:\.\-]/i.test(current)
    const isNextMajor = next ? /^(?:Given|Formula|To Find|Problem|Answer|Final Answer|Step\s*\d+|Case\s*\d+|\([ivxlcdm\d]+\))\s*[:\.\-]/i.test(next) : false

    // Can current and next be paired on one line? (Max 2 steps per line)
    // Both must be concise, neither can be a major labeled step that demands its own line,
    // and combined length must fit comfortably within maxCharsPerLine.
    const canPair =
      next !== null &&
      !isCurrentMajor &&
      !isNextMajor &&
      current.length <= 26 &&
      next.length <= 26 &&
      current.length + next.length + 5 <= maxCharsPerLine

    if (canPair && next) {
      const separator = next.startsWith('⇒') || next.startsWith('→') || next.startsWith('=') ? ' ' : '  ⇒  '
      const pairedLine = `${current}${separator}${next}`
      formattedLines.push(pairedLine)
      i += 2 // Consumed 2 steps on this line
    } else {
      if (current.length > maxCharsPerLine) {
        const wrapped = wrapText(current, maxCharsPerLine)
        formattedLines.push(...wrapped)
      } else {
        formattedLines.push(current)
      }
      i += 1 // Consumed 1 step on this line
    }
  }

  return formattedLines
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
