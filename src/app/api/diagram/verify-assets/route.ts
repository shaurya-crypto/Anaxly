import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'

const BROWSER_USER_AGENT =
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
const WIKIMEDIA_USER_AGENT = 'SobiAITutor/2.0 (https://sobi-ai-tutor.edu; mailto:support@sobi-ai-tutor.edu)'

// Initialize server-side Supabase client
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || ''
const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || ''
const supabase = (supabaseUrl && supabaseKey) ? createClient(supabaseUrl, supabaseKey) : null

interface MediaItem {
  title?: string
  url?: string
  query?: string
  description?: string
  mimeType?: string
}

async function verifyUrl(url: string, isVideo: boolean = false): Promise<boolean> {
  if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) return false
  if (!isVideo) {
    const cleanLower = url.toLowerCase().split('?')[0]
    if (
      cleanLower.endsWith('.tif') ||
      cleanLower.endsWith('.tiff') ||
      cleanLower.endsWith('.psd') ||
      cleanLower.endsWith('.eps') ||
      cleanLower.endsWith('.ai') ||
      cleanLower.endsWith('.djvu') ||
      cleanLower.endsWith('.pdf')
    ) {
      return false
    }
  }

  try {
    const controller = new AbortController()
    const timer = setTimeout(() => controller.abort(), 1800)
    let res = await fetch(url, {
      method: 'HEAD',
      signal: controller.signal,
      headers: {
        'User-Agent': BROWSER_USER_AGENT,
        'Accept': isVideo ? 'video/*,*/*' : 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
      },
    })
    if (!isVideo && (res.status === 403 || res.status === 405)) {
      res = await fetch(url, {
        method: 'GET',
        signal: controller.signal,
        headers: {
          'User-Agent': BROWSER_USER_AGENT,
          'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
          'Range': 'bytes=0-1024',
        },
      })
    }
    clearTimeout(timer)
    if (!res.ok && res.status !== 206 && res.status !== 304) return false
    const ct = (res.headers.get('content-type') || '').toLowerCase()
    if (isVideo) {
      return ct.startsWith('video/') || ct.includes('webm') || ct.includes('mp4') || ct.includes('ogg')
    }
    if (
      ct.includes('tiff') ||
      ct.includes('djvu') ||
      ct.includes('photoshop') ||
      ct.includes('pdf') ||
      ct.includes('postscript')
    ) {
      return false
    }
    return ct.startsWith('image/') || ct.includes('svg')
  } catch {
    return false
  }
}

async function searchLiveImage(query: string): Promise<string | null> {
  try {
    const cleanQ = query
      .trim()
      .replace(/^["']|["']$/g, '')
      .replace(/^(?:Activity|Concept|Module|Experiment|Lab|Chapter|Section)\s*[\d\.]*\s*[:\-\)]?\s*/i, '')
      .replace(/[\(\)\[\]\{\}]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim()

    // 1. Tier 1A: Search broad web images via Bing Images Async
    try {
      const controller = new AbortController()
      const timer = setTimeout(() => controller.abort(), 2200)
      const bUrl = `https://www.bing.com/images/async?q=${encodeURIComponent(cleanQ)}&first=1&count=10&mmasync=1`
      const bRes = await fetch(bUrl, {
        signal: controller.signal,
        headers: {
          'User-Agent': BROWSER_USER_AGENT,
          Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        },
      })
      clearTimeout(timer)

      if (bRes.ok) {
        const html = await bRes.text()
        const murls = [...html.matchAll(/&quot;murl&quot;:&quot;(https?:\/\/[^&"]+)&quot;/g)]
        for (const match of murls.slice(0, 5)) {
          const imgUrl = match[1]
          if (imgUrl && !imgUrl.toLowerCase().endsWith('.tif') && !imgUrl.toLowerCase().endsWith('.tiff')) {
            const ok = await verifyUrl(imgUrl, false)
            if (ok) return imgUrl
          }
        }
      }
    } catch {
      // Fall through to Wikipedia / Wikimedia
    }

    // 2. Tier 1B: Search Wikipedia PageImages API
    try {
      const controller = new AbortController()
      const timer = setTimeout(() => controller.abort(), 1800)
      const wikiPageUrl = `https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(
        cleanQ
      )}&gsrlimit=5&prop=pageimages&pithumbsize=1200&format=json`
      const wikiPageRes = await fetch(wikiPageUrl, {
        signal: controller.signal,
        headers: { 'User-Agent': WIKIMEDIA_USER_AGENT, Accept: 'application/json' },
      })
      clearTimeout(timer)

      if (wikiPageRes.ok) {
        const data = await wikiPageRes.json().catch(() => ({}))
        const pages = Object.values<any>(data.query?.pages || {})
        for (const page of pages) {
          const thumbUrl = page.thumbnail?.source
          if (thumbUrl && (await verifyUrl(thumbUrl, false))) {
            return thumbUrl
          }
        }
      }
    } catch {
      // Fall through to Wikimedia Commons
    }

    // 3. Tier 2: Search Wikimedia Commons
    const url = `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(
      cleanQ.includes('filetype:') ? cleanQ : `${cleanQ} filetype:bitmap|drawing`
    )}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|mime&format=json&gsrlimit=6`

    const res = await fetch(url, {
      headers: { 'User-Agent': WIKIMEDIA_USER_AGENT, Accept: 'application/json' },
    })
    if (!res.ok) return null
    const data = await res.json().catch(() => ({}))
    const pages = Object.values<any>(data.query?.pages || {})

    for (const page of pages) {
      const info = page.imageinfo?.[0]
      if (!info?.url) continue
      const mime = (info.mime || '').toLowerCase()
      if (!mime.startsWith('image/') || mime.includes('tiff') || mime.includes('djvu')) continue

      const isOk = await verifyUrl(info.url, false)
      if (isOk) return info.url
    }
    return null
  } catch {
    return null
  }
}

async function searchLiveVideo(query: string): Promise<string | null> {
  try {
    const cleanQ = query.trim().replace(/^["']|["']$/g, '').replace(/[^\w\s-]/g, ' ')
    const searchTerms = [`${cleanQ} filemime:video/webm`, `${cleanQ} filemime:video`]

    for (const term of searchTerms) {
      const url = `https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(
        term
      )}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|mime&format=json&gsrlimit=6`

      const res = await fetch(url, {
        headers: { 'User-Agent': WIKIMEDIA_USER_AGENT, Accept: 'application/json' },
      })
      if (!res.ok) continue
      const data = await res.json().catch(() => ({}))
      const pages = Object.values<any>(data.query?.pages || {})

      for (const page of pages) {
        const info = page.imageinfo?.[0]
        if (!info?.url) continue
        const mime = (info.mime || '').toLowerCase()
        if (!mime.startsWith('video/')) continue

        const isOk = await verifyUrl(info.url, true)
        if (isOk) return info.url
      }
    }
    return null
  } catch {
    return null
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json().catch(() => ({}))
    const moduleId = body.moduleId
    let rawImages: MediaItem[] = body.images || []
    let rawVideos: MediaItem[] = body.videos || []

    // If moduleId is provided and media arrays are empty, load from database
    if (moduleId && supabase && rawImages.length === 0 && rawVideos.length === 0) {
      const { data: mod } = await supabase
        .from('syllabus_modules')
        .select('title, visual_lesson_plan')
        .eq('id', moduleId)
        .maybeSingle()

      if (mod?.visual_lesson_plan) {
        const vlp = typeof mod.visual_lesson_plan === 'string'
          ? JSON.parse(mod.visual_lesson_plan)
          : mod.visual_lesson_plan

        if (Array.isArray(vlp.concept_visuals)) {
          rawImages = vlp.concept_visuals.map((v: any) => ({
            title: v.diagram_title || v.concept_title || mod.title,
            url: v.image_url || v.url,
            query: v.image_search_query || v.concept_title || v.diagram_title || mod.title,
            description: v.what_to_make,
          }))
        }

        if (vlp.demonstration_video_url) {
          rawVideos.push({
            title: vlp.demonstration_video_title || `${mod.title} Video Demonstration`,
            url: vlp.demonstration_video_url,
            query: mod.title,
            description: vlp.demonstration_video_description || 'Scientific experimental proof',
          })
        }
      }
    }

    let repairedCount = 0

    // 1. Verify and resolve images
    const verifiedImages: Array<MediaItem & { verified: boolean; replaced?: boolean }> = []
    for (const img of rawImages) {
      const initialUrl = img.url || ''
      const isInitialValid = initialUrl ? await verifyUrl(initialUrl, false) : false

      if (isInitialValid) {
        verifiedImages.push({
          ...img,
          url: initialUrl,
          verified: true,
        })
      } else {
        // Query live image replacement
        const searchQuery = img.query || img.title || 'science experiment diagram'
        const freshUrl = await searchLiveImage(searchQuery)
        if (freshUrl) {
          repairedCount++
          verifiedImages.push({
            ...img,
            url: freshUrl,
            verified: true,
            replaced: true,
          })
        } else {
          verifiedImages.push({
            ...img,
            verified: false,
          })
        }
      }
    }

    // 2. Verify and resolve videos
    const verifiedVideos: Array<MediaItem & { verified: boolean; replaced?: boolean }> = []
    for (const vid of rawVideos) {
      const initialUrl = vid.url || ''
      const isInitialValid = initialUrl ? await verifyUrl(initialUrl, true) : false

      if (isInitialValid) {
        verifiedVideos.push({
          ...vid,
          url: initialUrl,
          verified: true,
        })
      } else {
        const searchQuery = vid.query || vid.title || 'science experiment'
        const freshUrl = await searchLiveVideo(searchQuery)
        if (freshUrl) {
          repairedCount++
          verifiedVideos.push({
            ...vid,
            url: freshUrl,
            verified: true,
            replaced: true,
          })
        } else {
          verifiedVideos.push({
            ...vid,
            verified: false,
          })
        }
      }
    }

    // 3. Formulate concise Live AI direct visual context
    const validImageDirectives = verifiedImages
      .filter((img) => img.verified && img.url)
      .map(
        (img) =>
          `[READY_IMAGE]: "${img.title || 'Diagram'}" -> call write_chalkboard(action="draw_image", content="${img.url} | ${img.title || 'Diagram'} | ${img.description || ''}")`
      )

    const validVideoDirectives = verifiedVideos
      .filter((vid) => vid.verified && vid.url)
      .map(
        (vid) =>
          `[READY_VIDEO]: "${vid.title || 'Video Demo'}" -> call write_chalkboard(action="draw_video", content="${vid.url} | ${vid.title || 'Demo'} | ${vid.description || ''}")`
      )

    const aiDirectives = [
      'PRE-VERIFIED MEDIA ASSETS FOR THIS LESSON:',
      ...validImageDirectives,
      ...validVideoDirectives,
      'DYNAMIC MEDIA SEARCH INSTRUCTION:',
      'If the student requests more visuals, asks to see an experiment, or appears confused, you are NOT restricted to the above assets. Dynamically call search_and_show_image(query="...") or search_and_show_video(query="...") to retrieve live verified media on demand.',
    ].join('\n')

    return NextResponse.json({
      success: true,
      verifiedImages,
      verifiedVideos,
      repairedCount,
      aiDirectives,
    })
  } catch (err: any) {
    console.error('verify-assets route error:', err)
    return NextResponse.json({ success: false, error: err.message }, { status: 500 })
  }
}
