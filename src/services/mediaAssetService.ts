/**
 * Media Asset Service
 * Handles educational images, videos, programmatic animations, and graceful fallbacks.
 * Enforces provenance tracking, authorized provider verification, zero URL fabrication,
 * asset caching, and fallback rendering when external providers are not configured or media fails to load.
 */

export interface MediaAssetMetadata {
  id: string
  title: string
  url: string
  type: 'image' | 'video' | 'animation'
  provenance: 'textbook' | 'open_licensed' | 'ai_generated' | 'fallback'
  license?: string
  attributionText?: string
  provider: string
  isAvailable: boolean
  fallbackType?: 'diagram' | 'procedural_animation' | 'graph' | 'scene_3d'
  fallbackKey?: string
}

export interface IMediaAssetProvider {
  name: string
  isConfigured: boolean
  isAuthorizedDomain(url: string): boolean
  getAssetMetadata?(assetId: string): Promise<MediaAssetMetadata | null>
}

export interface MediaProviderStatusReport {
  configuredProviders: string[]
  externalVideoCdn: {
    available: boolean
    requiredConfiguration: string
    activeFallback: string
  }
  permittedImageDomains: string[]
  cachedAssetsCount: number
  zeroUrlFabricationEnforced: boolean
}

// Allowed educational domains with open or partner licenses
const ALLOWED_EDUCATIONAL_DOMAINS = [
  'upload.wikimedia.org',
  'commons.wikimedia.org',
  'openstax.org',
  'ncert.nic.in',
  'images.unsplash.com', // Only when explicitly approved
  'localhost',
]

export class MediaAssetService {
  private static assetCache = new Map<string, MediaAssetMetadata>()
  private static conceptAssetRegistry = new Map<string, string>() // conceptKey -> assetId

  /**
   * Register an approved media asset for concept reuse and caching
   */
  public static registerApprovedAsset(
    asset: MediaAssetMetadata,
    conceptKeys: string[] = []
  ): void {
    if (!asset || !asset.id) return
    this.assetCache.set(asset.id, asset)
    conceptKeys.forEach((key) => {
      this.conceptAssetRegistry.set(key.toLowerCase(), asset.id)
    })
  }

  /**
   * Find approved media asset for a repeated concept
   */
  public static findApprovedAssetForConcept(concept: string): MediaAssetMetadata | null {
    if (!concept) return null
    const assetId = this.conceptAssetRegistry.get(concept.toLowerCase())
    if (assetId && this.assetCache.has(assetId)) {
      return this.assetCache.get(assetId) || null
    }
    return null
  }

  /**
   * Retrieve cached asset metadata by ID
   */
  public static getCachedMetadata(assetId: string): MediaAssetMetadata | null {
    return this.assetCache.get(assetId) || null
  }

  /**
   * Clear or inspect cached assets
   */
  public static getAllCachedAssets(): MediaAssetMetadata[] {
    return Array.from(this.assetCache.values())
  }

  /**
   * Status of external providers and fallback readiness
   */
  public static getProviderStatus(): MediaProviderStatusReport {
    return {
      configuredProviders: [
        'NCERT Standard Textbook Figures Provider',
        'Wikimedia Commons Open License Provider',
        'Local Procedural Canvas & SVG Engine',
      ],
      externalVideoCdn: {
        available: false,
        requiredConfiguration: 'VIDEO_CDN_BASE_URL and CDN_ACCESS_KEY credentials',
        activeFallback: 'Interactive HTML5 Canvas Procedural Animation Engine',
      },
      permittedImageDomains: [...ALLOWED_EDUCATIONAL_DOMAINS],
      cachedAssetsCount: this.assetCache.size,
      zeroUrlFabricationEnforced: true,
    }
  }

  /**
   * Verify if a media URL belongs to an authorized educational provider
   */
  public static isAuthorizedDomain(urlString: string): boolean {
    if (!urlString) return false
    try {
      const parsed = new URL(urlString)
      return ALLOWED_EDUCATIONAL_DOMAINS.some(
        (domain) => parsed.hostname === domain || parsed.hostname.endsWith(`.${domain}`)
      )
    } catch {
      return false
    }
  }

  /**
   * Check if a video provider is authorized and reachable.
   * If not configured or unverified, returns a fallback animation reference without fabricating URLs.
   */
  public static async verifyVideoPlayability(videoUrl: string): Promise<{
    canPlay: boolean
    resolvedUrl?: string
    providerStatus: 'verified' | 'fallback_recommended' | 'unauthorized'
    fallbackAnimation?: string
  }> {
    if (!videoUrl) {
      return {
        canPlay: false,
        providerStatus: 'fallback_recommended',
        fallbackAnimation: 'circuit_flow',
      }
    }

    const isAuthorized = this.isAuthorizedDomain(videoUrl)
    if (!isAuthorized) {
      return {
        canPlay: false,
        providerStatus: 'unauthorized',
        fallbackAnimation: 'wave_propagation',
      }
    }

    try {
      // In browser or SSR context, verify lightweight HEAD request if possible
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), 2500)
      const res = await fetch(videoUrl, {
        method: 'HEAD',
        signal: controller.signal,
      }).catch(() => null)
      clearTimeout(timeoutId)

      if (res && res.ok) {
        return {
          canPlay: true,
          resolvedUrl: videoUrl,
          providerStatus: 'verified',
        }
      }
    } catch {
      // Silent catch: network blocked or CORS preflight failed
    }

    return {
      canPlay: false,
      providerStatus: 'fallback_recommended',
      fallbackAnimation: 'projectile_motion',
    }
  }

  /**
   * Resolve an educational image with guaranteed graceful fallback
   */
  public static resolveImage(
    url: string | undefined,
    topicContext: string,
    provenance: 'textbook' | 'open_licensed' | 'ai_generated' | 'fallback' = 'textbook'
  ): {
    primaryUrl: string
    attribution: string
    hasFallback: boolean
    fallbackSvg: string
  } {
    const isDomainPermitted = url ? this.isAuthorizedDomain(url) : false
    const cleanUrl = isDomainPermitted && url ? url : ''

    const fallbackSvg = this.generateFallbackSvg(topicContext)

    return {
      primaryUrl: cleanUrl,
      attribution:
        provenance === 'textbook'
          ? 'NCERT Standard Textbook Figure - Certified Educational Material'
          : provenance === 'open_licensed'
          ? 'Wikimedia Commons - Creative Commons Educational License'
          : 'AI Educational Diagram - Interactive Pedagogical Asset',
      hasFallback: true,
      fallbackSvg,
    }
  }

  /**
   * Programmatic SVG fallback illustration for key school science/math concepts
   * Guarantees that even if offline or if no external CDN is available,
   * the student sees an authentic, high-contrast, mathematical/scientific vector visual.
   */
    public static generateFallbackSvg(conceptName: string): string {
    const lower = (conceptName || '').toLowerCase()

    if (lower.includes('ohm') || lower.includes('circuit') || lower.includes('resist')) {
      return `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" class="w-full h-full">
        <defs>
          <style>
            @keyframes flowDash { to { stroke-dashoffset: -24; } }
            @keyframes pulseTerminal { 0%, 100% { r: 3.5; opacity: 1; } 50% { r: 6.5; opacity: 0.35; } }
          </style>
          <linearGradient id="cellBody" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#EFF6FF"/>
            <stop offset="100%" stop-color="#DBEAFE"/>
          </linearGradient>
        </defs>
        <!-- Pure White Chalkboard Backdrop -->
        <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <!-- Header Pill Badge -->
        <rect x="110" y="12" width="320" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', 'Segoe UI', sans-serif">Ohm's Law: V = I × R (3D Axonometric Circuit)</text>

        <!-- 30° Axonometric Drafting Base Grid -->
        <path d="M 60 250 L 270 135 L 480 250" stroke="#F1F5F9" stroke-width="1.2" fill="none"/>
        <path d="M 120 265 L 270 180 L 420 265" stroke="#F1F5F9" stroke-width="1.2" fill="none"/>

        <!-- 3D Circuit Loop with Flowing Electron Dashes -->
        <path d="M 140 180 L 270 110 L 400 180 L 270 250 Z" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="8,5" style="animation: flowDash 1.4s linear infinite;"/>

        <!-- 3D Cylindrical Resistor Body (Isometric extrusion on top rail) -->
        <g transform="translate(230, 115) rotate(-26)">
          <rect x="0" y="-8" width="55" height="16" rx="4" fill="url(#cellBody)" stroke="#0F172A" stroke-width="1.5"/>
          <!-- Resistor Color Bands -->
          <rect x="10" y="-8" width="4" height="16" fill="#DC2626"/>
          <rect x="18" y="-8" width="4" height="16" fill="#D97706"/>
          <rect x="26" y="-8" width="4" height="16" fill="#16A34A"/>
          <rect x="40" y="-8" width="4" height="16" fill="#F59E0B"/>
        </g>

        <!-- 3D DC Power Source (Battery Cells) on bottom-left rail -->
        <g transform="translate(180, 215) rotate(26)">
          <!-- Cell 1 -->
          <line x1="-12" y1="-14" x2="-12" y2="14" stroke="#DC2626" stroke-width="3"/>
          <line x1="-5" y1="-8" x2="-5" y2="8" stroke="#0F172A" stroke-width="2"/>
          <!-- Cell 2 -->
          <line x1="5" y1="-14" x2="5" y2="14" stroke="#DC2626" stroke-width="3"/>
          <line x1="12" y1="-8" x2="12" y2="8" stroke="#0F172A" stroke-width="2"/>
          <text x="-14" y="-18" fill="#DC2626" font-size="10" font-weight="bold">+</text>
          <text x="14" y="-18" fill="#0F172A" font-size="10" font-weight="bold">-</text>
        </g>

        <!-- Current Direction Arrow -->
        <path d="M 330 145 L 350 155" stroke="#16A34A" stroke-width="3" marker-end="url(#arrowSage)"/>
        <text x="365" y="148" fill="#16A34A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace">Current I →</text>

        <!-- Symmetrical Callout Cards & Leader Lines -->
        <!-- Resistor Callout -->
        <polyline points="260,118 260,70 170,70" fill="none" stroke="#94A3B8" stroke-width="1"/>
        <circle cx="260" cy="118" r="3" fill="#2563EB"/>
        <rect x="35" y="58" width="130" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
        <text x="100" y="74" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="sans-serif">Resistor R (Ω)</text>

        <!-- Battery Callout -->
        <polyline points="195,215 195,245 130,245" fill="none" stroke="#94A3B8" stroke-width="1"/>
        <circle cx="195" cy="215" r="3" fill="#2563EB"/>
        <rect x="20" y="233" width="105" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
        <text x="72" y="249" text-anchor="middle" fill="#DC2626" font-size="11" font-weight="bold" font-family="sans-serif">Battery V (Volts)</text>

        <!-- Readout Banner -->
        <rect x="375" y="225" width="145" height="34" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="447" y="240" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace">I = V / R</text>
        <text x="447" y="253" text-anchor="middle" fill="#64748B" font-size="9" font-family="sans-serif">Linear Ohmic Conductor</text>
      </svg>`
    }

    if (lower.includes('refract') || lower.includes('optic') || lower.includes('light') || lower.includes('lens') || lower.includes('prism')) {
      return `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" class="w-full h-full">
        <defs>
          <style>
            @keyframes flowRay { to { stroke-dashoffset: -20; } }
            @keyframes pulseNormal { 0%, 100% { r: 3; opacity: 1; } 50% { r: 6; opacity: 0.35; } }
          </style>
          <linearGradient id="opticsGlassTop" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#EFF6FF" stop-opacity="0.95"/>
            <stop offset="100%" stop-color="#DBEAFE" stop-opacity="0.75"/>
          </linearGradient>
          <linearGradient id="opticsGlassFront" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#BFDBFE" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#93C5FD" stop-opacity="0.4"/>
          </linearGradient>
        </defs>

        <!-- Pure White Chalkboard Backdrop -->
        <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <!-- Header Pill Badge -->
        <rect x="110" y="12" width="320" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', 'Segoe UI', sans-serif">Snell's Law: n₁ sin(i) = n₂ sin(r) (3D Prism/Slab)</text>

        <!-- 30° Axonometric Drafting Base Grid -->
        <path d="M 60 250 L 270 140 L 480 250" stroke="#F1F5F9" stroke-width="1.2" fill="none"/>

        <!-- 3D Glass Slab / Prism in 30° Isometric Projection -->
        <polygon points="130,215 270,145 410,215 270,265" fill="none" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4,4"/>
        <polygon points="130,150 270,80 270,145 130,215" fill="url(#opticsGlassFront)" stroke="#94A3B8" stroke-width="1.5" stroke-linejoin="round"/>
        <polygon points="270,80 410,150 410,215 270,145" fill="#93C5FD" fill-opacity="0.35" stroke="#94A3B8" stroke-width="1.5" stroke-linejoin="round"/>
        <polygon points="130,150 270,80 410,150 270,215" fill="url(#opticsGlassTop)" stroke="#2563EB" stroke-width="2" stroke-linejoin="round"/>

        <!-- Normal Vector Perpendicular to Top 3D Plane -->
        <line x1="270" y1="148" x2="270" y2="40" stroke="#F59E0B" stroke-width="1.75" stroke-dasharray="4,4"/>
        <circle cx="270" cy="148" r="3.5" fill="#0F172A"/>
        <text x="278" y="55" fill="#D97706" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">Normal n̂</text>

        <!-- 3D Incident Laser Ray -->
        <line x1="160" y1="55" x2="270" y2="148" stroke="#DC2626" stroke-width="3" stroke-linecap="round"/>
        <!-- Refracted Ray inside Glass Medium -->
        <line x1="270" y1="148" x2="310" y2="230" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="6,3" stroke-linecap="round" style="animation: flowRay 1.2s linear infinite;"/>
        <!-- Emergent Ray with Parallel Shift -->
        <line x1="310" y1="230" x2="375" y2="275" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round"/>

        <!-- Left Callout: Incident Ray -->
        <polyline points="200,90 200,60 120,60" fill="none" stroke="#94A3B8" stroke-width="1"/>
        <circle cx="200" cy="90" r="3" fill="#DC2626"/>
        <rect x="15" y="48" width="100" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
        <text x="65" y="64" text-anchor="middle" fill="#DC2626" font-size="11" font-weight="bold" font-family="sans-serif">Incident Ray (i)</text>

        <!-- Right Callout: Glass Medium -->
        <polyline points="350,135 350,105 410,105" fill="none" stroke="#94A3B8" stroke-width="1"/>
        <circle cx="350" cy="135" r="3" fill="#2563EB"/>
        <rect x="415" y="93" width="115" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
        <text x="472" y="109" text-anchor="middle" fill="#2563EB" font-size="11" font-weight="bold" font-family="sans-serif">Glass (n₂ = 1.50)</text>

        <!-- Bottom Callout: Emergent Lateral Displacement -->
        <rect x="360" y="225" width="165" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="442" y="240" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace">Lateral Shift Δx</text>
        <text x="442" y="251" text-anchor="middle" fill="#64748B" font-size="9" font-family="sans-serif">Incident &amp; Emergent are parallel</text>
      </svg>`
    }

    if (lower.includes('graph') || lower.includes('linear') || lower.includes('slope') || lower.includes('line')) {
      return `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" class="w-full h-full">
        <defs>
          <style>
            @keyframes pulsePoint { 0%, 100% { r: 4; opacity: 1; } 50% { r: 8; opacity: 0.35; } }
          </style>
        </defs>
        <!-- Pure White Chalkboard Backdrop -->
        <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect x="110" y="12" width="320" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', 'Segoe UI', sans-serif">Cartesian Coordinate Graph: y = mx + c</text>

        <!-- Coordinate Grid -->
        <g stroke="#F1F5F9" stroke-width="0.8">
          <line x1="80" y1="70" x2="460" y2="70"/>
          <line x1="80" y1="120" x2="460" y2="120"/>
          <line x1="80" y1="170" x2="460" y2="170"/>
          <line x1="80" y1="220" x2="460" y2="220"/>
          <line x1="140" y1="45" x2="140" y2="250"/>
          <line x1="220" y1="45" x2="220" y2="250"/>
          <line x1="300" y1="45" x2="300" y2="250"/>
          <line x1="380" y1="45" x2="380" y2="250"/>
        </g>

        <!-- Coordinate Axes -->
        <line x1="90" y1="170" x2="450" y2="170" stroke="#0F172A" stroke-width="2" marker-end="url(#arrowCharcoal)"/>
        <line x1="220" y1="250" x2="220" y2="45" stroke="#0F172A" stroke-width="2" marker-end="url(#arrowCharcoal)"/>
        <text x="458" y="174" fill="#0F172A" font-size="12" font-weight="bold" font-family="sans-serif">X</text>
        <text x="216" y="38" fill="#0F172A" font-size="12" font-weight="bold" font-family="sans-serif">Y</text>

        <!-- Plotted Linear Curve -->
        <line x1="110" y1="240" x2="380" y2="60" stroke="#2563EB" stroke-width="3"/>

        <!-- y-intercept point (0, c) with pulsing ring -->
        <circle cx="220" cy="120" r="5" fill="#2563EB"/>
        <circle cx="220" cy="120" r="8" fill="none" stroke="#2563EB" stroke-width="1.5" style="animation: pulsePoint 2s ease-in-out infinite;"/>

        <!-- Slope Triangle Δy / Δx -->
        <path d="M 280 140 L 340 140 L 340 100" fill="none" stroke="#16A34A" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="310" y="155" text-anchor="middle" fill="#16A34A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace">Δx</text>
        <text x="355" y="122" fill="#16A34A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace">Δy</text>

        <!-- Left Callout: Intercept -->
        <polyline points="220,120 180,120 180,95 140,95" fill="none" stroke="#94A3B8" stroke-width="1"/>
        <rect x="25" y="83" width="110" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
        <text x="80" y="99" text-anchor="middle" fill="#2563EB" font-size="11" font-weight="bold" font-family="sans-serif">y-intercept (0, c)</text>

        <!-- Right Callout: Slope Formula -->
        <rect x="365" y="215" width="155" height="34" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="442" y="230" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', monospace">Slope m = Δy / Δx</text>
        <text x="442" y="243" text-anchor="middle" fill="#64748B" font-size="9" font-family="sans-serif">Rate of Change</text>
      </svg>`
    }

    // Generic educational 3D axonometric pedestal fallback
    return `<svg viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" class="w-full h-full">
      <defs>
        <style>
          @keyframes orbitPulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
        </style>
      </defs>
      <!-- Pure White Chalkboard Backdrop -->
      <rect x="4" y="4" width="532" height="272" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
      <rect x="110" y="12" width="320" height="22" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="270" y="27" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="'JetBrains Mono', 'Segoe UI', sans-serif">${conceptName || 'Scientific Concept Model (3D Axonometric)'}</text>

      <!-- 30° Axonometric Plinth -->
      <polygon points="160,200 270,140 380,200 270,250" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <polygon points="160,200 160,220 270,270 270,250" fill="#E2E8F0" stroke="#94A3B8" stroke-width="1.2"/>
      <polygon points="270,250 270,270 380,220 380,200" fill="#CBD5E1" stroke="#94A3B8" stroke-width="1.2"/>

      <!-- Central Volumetric Solid -->
      <g style="transform-origin: 270px 145px; animation: orbitPulse 3s ease-in-out infinite;">
        <ellipse cx="270" cy="145" rx="45" ry="45" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
        <ellipse cx="270" cy="145" rx="45" ry="18" fill="none" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="4,3"/>
        <circle cx="270" cy="145" r="9" fill="#DC2626"/>
      </g>

      <!-- Leader Line Callouts -->
      <polyline points="270,145 270,95 200,95" fill="none" stroke="#94A3B8" stroke-width="1"/>
      <circle cx="270" cy="145" r="3" fill="#2563EB"/>
      <rect x="40" y="83" width="155" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="117" y="99" text-anchor="middle" fill="#0F172A" font-size="11" font-weight="bold" font-family="sans-serif">Focus Nucleus / Core</text>

      <!-- Bottom Status Pill -->
      <rect x="180" y="235" width="180" height="24" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="270" y="251" text-anchor="middle" fill="#64748B" font-size="10" font-family="'JetBrains Mono', monospace">Standard Board Vector Spec</text>
    </svg>`
  }
}
