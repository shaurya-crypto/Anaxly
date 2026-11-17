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
  const atomicChunks: { text: string; isArrowTransition: boolean }[] = []

  // Comprehensive list of academic, textbook, and exam section headers that demand their own line
  const MAJOR_HEADER_REGEX = /^(?:Given(?:\s+that)?|Formula|Theorem|Law|To\s+(?:Find|Prove|Evaluate|Calculate|Determine)|Construction|Proof|Substitution|Calculation|Working|Rough|Problem|Question|Answer|Final\s+Answer|Boxed\s+Answer|Ans|Case\s*\d+|Hence\s+Proved|Result|Therefore|Step\s*\d+|Step\s*[A-Za-z]|\([ivxlcdm\d]+\)|\([a-z]\)|\d+[\.\)])\s*[:\.\-]/i

  // Delimiter for splitting concatenated inline step headers
  const INLINE_STEP_REGEX = /(?<=[^\s])\s+(?=(?:Step\s*\d+|Step\s*[A-Za-z]|Given(?:\s+that)?|To\s+(?:Find|Prove|Evaluate|Calculate|Determine)|Formula|Theorem|Law|Construction|Proof|Substitution|Calculation|Working|Rough|Answer|Final\s+Answer|Boxed\s+Answer|Ans|Problem|Question|Case\s*\d+|Hence\s+Proved|Therefore|Result|\([ivxlcdm\d]+\)|\([a-z]\)|\d+[\.\)])\s*[:\.\-])/i

  // Delimiter for splitting explicit step delimiters: semicolons and pipe separators (surrounded by whitespace)
  // Preserves mathematical modulus (|x|) and parallel geometry (|| or ∥)
  const DELIMITER_REGEX = /\s*;\s*|\s+(?<!\|)\|(?!\|)\s+/

  for (const line of rawLines) {
    const trimmed = line.trim()
    if (!trimmed) continue

    // 1. Split on explicit delimiters (semicolons, standalone pipes)
    const delimiterParts = trimmed.split(DELIMITER_REGEX).filter(Boolean)

    for (const part of delimiterParts) {
      // 2. Split on inline step markers if multiple steps were concatenated without semicolons
      // e.g. "Given: m = 2 kg Step 1: F = m × a Step 2: F = 10 N Answer: F = 10 N"
      const inlineParts = part.split(INLINE_STEP_REGEX).filter(Boolean)

      for (const ip of inlineParts) {
        // 3. Chained implications (e.g. A => B => C => D)
        const arrowParts = ip.split(/\s*(?:=>|⇒|→)\s*/).filter(Boolean)
        if (arrowParts.length >= 2) {
          arrowParts.forEach((ap, idx) => {
            atomicChunks.push({ text: ap.trim(), isArrowTransition: idx > 0 })
          })
        } else {
          atomicChunks.push({ text: ip.trim(), isArrowTransition: false })
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
    const isCurrentMajor = MAJOR_HEADER_REGEX.test(current.text)
    const isNextMajor = next ? MAJOR_HEADER_REGEX.test(next.text) : false

    // Can current and next be paired on one line? (Max 2 steps per line)
    // Both must be concise, neither can be a major labeled step that demands its own line,
    // and combined length must fit comfortably within maxCharsPerLine.
    const canPair =
      next !== null &&
      !isCurrentMajor &&
      !isNextMajor &&
      current.text.length <= 26 &&
      next.text.length <= 26 &&
      current.text.length + next.text.length + 5 <= maxCharsPerLine

    if (canPair && next) {
      let separator: string
      if (next.isArrowTransition) {
        separator = next.text.startsWith('⇒') || next.text.startsWith('→') || next.text.startsWith('=') ? ' ' : '  ⇒  '
      } else if (next.text.startsWith('⇒') || next.text.startsWith('→') || next.text.startsWith('=')) {
        separator = ' '
      } else {
        separator = ', '
      }
      const curText = current.isArrowTransition && !current.text.startsWith('⇒') ? `⇒ ${current.text}` : current.text
      const pairedLine = `${curText}${separator}${next.text}`
      formattedLines.push(pairedLine)
      i += 2 // Consumed 2 steps on this line
    } else {
      let lineText = current.text
      if (current.isArrowTransition && !lineText.startsWith('⇒') && !lineText.startsWith('→') && !lineText.startsWith('=')) {
        lineText = `⇒ ${lineText}`
      }
      if (lineText.length > maxCharsPerLine) {
        const wrapped = wrapText(lineText, maxCharsPerLine)
        formattedLines.push(...wrapped)
      } else {
        formattedLines.push(lineText)
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
