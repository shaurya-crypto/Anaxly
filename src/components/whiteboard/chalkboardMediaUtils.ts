/**
 * Chalkboard Media Utilities
 * Robust base64 data URL sanitization, SVG encoding, and Excalidraw media validation.
 *
 * Guarantees zero `InvalidCharacterError: Failed to execute 'atob' on 'Window'`
 * when Excalidraw processes image/SVG file assets via `excalidrawAPI.addFiles`.
 */

/**
 * Strictly sanitizes and normalizes a base64 data URL.
 * 1. Strips all interior/exterior whitespace and newlines.
 * 2. Normalizes URL-safe base64 characters ('-' -> '+', '_' -> '/').
 * 3. Restores missing '=' padding alignment (length % 4 === 0).
 * 4. Validates base64 character set.
 * 5. Verifies decodability via atob().
 *
 * Returns the normalized data URL string (`data:<mime>;base64,<payload>`), or null if invalid.
 */
export const sanitizeBase64DataUrl = (dataUrl: unknown): string | null => {
  if (typeof dataUrl !== 'string') return null
  const trimmed = dataUrl.trim()
  if (!trimmed.startsWith('data:')) return null
  const commaIdx = trimmed.indexOf(',')
  if (commaIdx === -1) return null

  const header = trimmed.slice(0, commaIdx)
  if (!header.toLowerCase().includes(';base64')) return null

  // Extract clean MIME type
  const mimeMatch = header.match(/^data:([^;,]+)/i)
  const mimeType = mimeMatch ? mimeMatch[1].toLowerCase().trim() : 'image/png'

  // Extract payload, remove all whitespace and newlines, normalize url-safe base64
  let payload = trimmed.slice(commaIdx + 1).replace(/\s+/g, '').replace(/-/g, '+').replace(/_/g, '/')
  if (!payload) return null

  // Fix padding to multiple of 4
  const remainder = payload.length % 4
  if (remainder === 2) {
    payload += '=='
  } else if (remainder === 3) {
    payload += '='
  } else if (remainder === 1) {
    // Single trailing character cannot form valid base64
    return null
  }

  // Validate base64 character set
  if (!/^[A-Za-z0-9+/]+={0,2}$/.test(payload)) return null

  // Verify decodability via atob / Buffer
  try {
    if (typeof window !== 'undefined' && typeof window.atob === 'function') {
      window.atob(payload)
    } else if (typeof atob === 'function') {
      atob(payload)
    } else if (typeof Buffer !== 'undefined') {
      Buffer.from(payload, 'base64')
    }
  } catch {
    return null
  }

  return `data:${mimeType};base64,${payload}`
}

/**
 * Type guard helper checking whether a value is a strictly valid base64 data URL.
 */
export const isValidBase64DataUrl = (dataUrl: unknown): dataUrl is string => {
  return sanitizeBase64DataUrl(dataUrl) !== null
}

/**
 * Safely encodes arbitrary UTF-8 SVG markup to a strictly valid base64 data URL.
 * Handles Unicode, ensures fallback on encoding errors, and validates output.
 */
export const svgToBase64DataUrl = (svgString: string): string => {
  const cleanInput = (svgString || '').trim() || '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"></svg>'
  try {
    if (typeof window !== 'undefined' && typeof window.btoa === 'function') {
      const bytes = new TextEncoder().encode(cleanInput)
      let binary = ''
      const len = bytes.byteLength
      for (let i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i])
      }
      const b64 = window.btoa(binary)
      const dataUrl = `data:image/svg+xml;base64,${b64}`
      return sanitizeBase64DataUrl(dataUrl) || dataUrl
    }
    if (typeof Buffer !== 'undefined') {
      const b64 = Buffer.from(cleanInput, 'utf-8').toString('base64')
      const dataUrl = `data:image/svg+xml;base64,${b64}`
      return sanitizeBase64DataUrl(dataUrl) || dataUrl
    }
    const b64 = window.btoa(unescape(encodeURIComponent(cleanInput)))
    const dataUrl = `data:image/svg+xml;base64,${b64}`
    return sanitizeBase64DataUrl(dataUrl) || dataUrl
  } catch (err) {
    console.warn('svgToBase64DataUrl conversion error:', err)
    try {
      const b64 = window.btoa(unescape(encodeURIComponent(cleanInput)))
      const dataUrl = `data:image/svg+xml;base64,${b64}`
      return sanitizeBase64DataUrl(dataUrl) || dataUrl
    } catch {
      // Guaranteed valid base64 data URL for empty 100x100 SVG
      return 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48L3N2Zz4='
    }
  }
}

/**
 * Pre-validates that an SVG markup string (or base64 SVG data URL) will satisfy
 * Excalidraw's internal `normalizeSVG` function without throwing "Invalid SVG"
 * or encountering DOMParser parsererror elements.
 */
export const validateSvgForExcalidraw = (
  input: string
): { isValid: boolean; cleanSvg: string } => {
  let svgString = input
  if (input.startsWith('data:')) {
    const commaIdx = input.indexOf(',')
    if (commaIdx === -1) return { isValid: false, cleanSvg: '' }
    const b64 = input.slice(commaIdx + 1).replace(/\s+/g, '')
    try {
      let binary = ''
      if (typeof window !== 'undefined' && typeof window.atob === 'function') {
        binary = window.atob(b64)
      } else if (typeof atob === 'function') {
        binary = atob(b64)
      } else if (typeof Buffer !== 'undefined') {
        binary = Buffer.from(b64, 'base64').toString('binary')
      }
      const bytes = new Uint8Array(binary.length)
      for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i)
      svgString = new TextDecoder('utf-8').decode(bytes)
    } catch {
      return { isValid: false, cleanSvg: '' }
    }
  }

  const trimmed = (svgString || '').trim()
  if (!trimmed) return { isValid: false, cleanSvg: '' }

  if (typeof window !== 'undefined' && typeof window.DOMParser !== 'undefined') {
    try {
      const doc = new window.DOMParser().parseFromString(trimmed, 'image/svg+xml')
      const errorNode = doc.querySelector('parsererror')
      const svg = doc.querySelector('svg')
      if (errorNode || !svg || svg.nodeName.toLowerCase() !== 'svg') {
        return { isValid: false, cleanSvg: trimmed }
      }
      return { isValid: true, cleanSvg: trimmed }
    } catch {
      return { isValid: false, cleanSvg: trimmed }
    }
  }

  // Node / Non-DOM environment fallback check
  const lower = trimmed.toLowerCase()
  const hasSvgTag = lower.includes('<svg') && lower.includes('</svg>')
  return { isValid: hasSvgTag, cleanSvg: trimmed }
}

/**
 * Generates an XML-compliant, aesthetically polished chalkboard vector illustration card
 * when external image retrieval, proxying, or CORS conversions fail.
 * Preserves the source host in the card for student lightbox viewing.
 */
export const createFallbackImageSvg = (
  title: string,
  sourceUrl = '',
  width = 480,
  height = 280
): string => {
  const safeTitle = (title || 'Educational Illustration')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;')

  let host = 'External Source'
  if (sourceUrl) {
    try {
      if (sourceUrl.startsWith('http')) {
        host = new URL(sourceUrl).hostname
      } else if (sourceUrl.startsWith('/')) {
        host = 'Local Asset'
      }
    } catch {}
  }
  const safeHost = host
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;')

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}">
  <defs>
    <linearGradient id="fallbackGrad_${width}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0F2E20"/>
      <stop offset="100%" stop-color="#0A1F16"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#fallbackGrad_${width})" rx="10" stroke="#235338" stroke-width="2"/>
  <rect x="16" y="16" width="${width - 32}" height="${height - 32}" fill="none" rx="8" stroke="#347854" stroke-width="1.5" stroke-dasharray="6 4"/>
  <g transform="translate(${width / 2}, ${height / 2 - 25})">
    <circle r="36" fill="#133D29" stroke="#4ADE80" stroke-width="2"/>
    <path d="M-18 10 L-6 -8 L4 4 L14 -12 L22 10 Z" fill="#4ADE80" opacity="0.85"/>
    <circle cx="-6" cy="-14" r="4" fill="#FACC15"/>
  </g>
  <text x="${width / 2}" y="${height / 2 + 35}" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="600" fill="#F1F5F9" text-anchor="middle">${safeTitle}</text>
  <text x="${width / 2}" y="${height / 2 + 56}" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#86EFAC" text-anchor="middle">Source: ${safeHost} &#8226; Click to open high-res original</text>
</svg>`
}
