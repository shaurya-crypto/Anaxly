import { GeminiVoice } from '@/types/liveSession'

/**
 * Standard supported language locales for Indian School Board Students (CBSE, ICSE, IB).
 * Passing ["en-IN", "hi-IN"] to the Gemini Live speechConfig and transcription parameters
 * ensures natural Indian English and Hindi inflection regardless of the selected prebuilt voice.
 */
export const DEFAULT_SUPPORTED_LANGUAGES: string[] = ['en-IN', 'hi-IN']

export interface VoiceOption {
  id: GeminiVoice
  name: string
  gender: 'female' | 'male'
  label: string
  desc: string
  bestLanguages: string[]
  isRecommended?: boolean
  inflection: string
}

export const VOICE_OPTIONS: VoiceOption[] = [
  {
    id: 'Charon',
    name: 'Charon',
    gender: 'male',
    label: 'Charon — Realistic, calm, authoritative male mentor (Default)',
    desc: 'Calm, authoritative, deeply patient pedagogical male mentor with articulate cadence for step-by-step problem solving.',
    bestLanguages: ['English', 'Hinglish', 'Hindi', 'German', 'Spanish', 'French'],
    isRecommended: true,
    inflection: 'realistic, calm, authoritative, deeply patient pedagogical male mentor',
  },
  {
    id: 'Puck',
    name: 'Puck',
    gender: 'male',
    label: 'Puck — Upbeat, lively, energetic Indian inflection',
    desc: 'Upbeat, energetic, and engaging cadence with crisp Indian English and Hindi pronunciation.',
    bestLanguages: ['English', 'Hinglish', 'Hindi'],
    isRecommended: true,
    inflection: 'upbeat, lively Indian inflection with high engagement',
  },
  {
    id: 'Fenrir',
    name: 'Fenrir',
    gender: 'male',
    label: 'Fenrir — Confident, energetic, and direct',
    desc: 'Confident, assertive, and direct tone that keeps students attentive.',
    bestLanguages: ['English', 'Spanish'],
    inflection: 'direct, confident cadence',
  },
  {
    id: 'Leda',
    name: 'Leda',
    gender: 'female',
    label: 'Leda — Warm, youthful, natural Indian inflection',
    desc: 'Youthful, warm, and natural conversational cadence with fluid Indian English and Hindi inflection.',
    bestLanguages: ['English', 'Hinglish', 'Hindi'],
    inflection: 'fluid, natural Indian inflection with warm encouraging tone',
  },
  {
    id: 'Aoede',
    name: 'Aoede',
    gender: 'female',
    label: 'Aoede — Breezy, relaxed, and methodical mentor',
    desc: 'Breezy, relaxed, and methodical tone for steady conceptual derivations.',
    bestLanguages: ['English', 'French', 'Spanish'],
    inflection: 'clear, relaxed international cadence',
  },
  {
    id: 'Kore',
    name: 'Kore',
    gender: 'female',
    label: 'Kore — Crisp, attentive, and academically clear',
    desc: 'Gentle, structured, and academically lucid explanations.',
    bestLanguages: ['English', 'German'],
    inflection: 'crisp, attentive cadence',
  },
]

export interface LanguageVoiceMapping {
  language: string
  primaryLanguageCode: string
  supportedLanguageCodes: string[]
  recommendedVoices: GeminiVoice[]
  defaultVoice: GeminiVoice
  accentPromptInstruction: string
}

export const LANGUAGE_VOICE_CONFIGS: Record<string, LanguageVoiceMapping> = {
  English: {
    language: 'English',
    primaryLanguageCode: 'en-IN',
    supportedLanguageCodes: ['en-IN', 'hi-IN', 'en-GB', 'en-US'],
    recommendedVoices: ['Charon', 'Puck', 'Leda'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in English with a natural, fluid Indian accent (en-IN). Use standard Indian educational terminology (sums, steps, marks, derivations) with warm, articulate clarity.',
  },
  'English (Indian)': {
    language: 'English (Indian)',
    primaryLanguageCode: 'en-IN',
    supportedLanguageCodes: ['en-IN', 'hi-IN'],
    recommendedVoices: ['Charon', 'Puck', 'Leda'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in English with a natural, fluid Indian accent (en-IN). Use standard Indian educational terminology (sums, steps, marks, derivations) with warm, articulate clarity.',
  },
  'English (British)': {
    language: 'English (British)',
    primaryLanguageCode: 'en-GB',
    supportedLanguageCodes: ['en-GB', 'en-US'],
    recommendedVoices: ['Charon', 'Fenrir'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in English with a polished, measured British academic accent (en-GB) and scholastic poise.',
  },
  'English (US)': {
    language: 'English (US)',
    primaryLanguageCode: 'en-US',
    supportedLanguageCodes: ['en-US', 'en-GB'],
    recommendedVoices: ['Charon', 'Fenrir'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in clear, warm, engaging American English (en-US) with enthusiastic pedagogical inflection.',
  },
  Hinglish: {
    language: 'Hinglish',
    primaryLanguageCode: 'en-IN',
    supportedLanguageCodes: ['en-IN', 'hi-IN'],
    recommendedVoices: ['Charon', 'Puck', 'Leda'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in natural, conversational Hinglish (hi-IN). Use standard English for scientific laws, formulas, and units while connecting ideas smoothly with warm conversational Hindi (samjhe, dekho, bilkul, chalo).',
  },
  Hindi: {
    language: 'Hindi',
    primaryLanguageCode: 'hi-IN',
    supportedLanguageCodes: ['hi-IN', 'en-IN'],
    recommendedVoices: ['Charon', 'Puck', 'Leda'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in clear, fluent Hindi (hi-IN) with natural conversational warmth. Enunciate technical terms clearly in Hindi alongside standard English terms where commonly used in school boards.',
  },
  Spanish: {
    language: 'Spanish',
    primaryLanguageCode: 'es-ES',
    supportedLanguageCodes: ['es-ES', 'es-419', 'en-US'],
    recommendedVoices: ['Charon', 'Fenrir', 'Aoede'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in clear, warm Castilian or neutral Latin American Spanish with engaging scholastic cadence.',
  },
  French: {
    language: 'French',
    primaryLanguageCode: 'fr-FR',
    supportedLanguageCodes: ['fr-FR', 'en-US'],
    recommendedVoices: ['Charon', 'Aoede'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in articulate, standard French with warm, encouraging scholastic cadence.',
  },
  German: {
    language: 'German',
    primaryLanguageCode: 'de-DE',
    supportedLanguageCodes: ['de-DE', 'en-US'],
    recommendedVoices: ['Charon', 'Kore'],
    defaultVoice: 'Charon',
    accentPromptInstruction:
      'Speak in clear, structured standard German (Hochdeutsch) with precise academic pronunciation.',
  },
}

/**
 * Returns the optimal language parameters and matching voice personas
 * for a student's chosen language.
 */
export function getLanguageVoiceConfig(languageName?: string | null): LanguageVoiceMapping {
  if (!languageName) {
    return LANGUAGE_VOICE_CONFIGS['English']
  }
  const normalized = languageName.trim().toLowerCase()
  if (normalized.includes('british') || normalized.includes('en-gb') || normalized.includes('uk')) {
    return LANGUAGE_VOICE_CONFIGS['English (British)']
  }
  if (normalized.includes('american') || normalized.includes('en-us') || normalized.includes('us')) {
    return LANGUAGE_VOICE_CONFIGS['English (US)']
  }
  if (normalized.includes('indian') || normalized.includes('en-in')) {
    return LANGUAGE_VOICE_CONFIGS['English (Indian)']
  }
  if (normalized.includes('hinglish') || normalized.includes('bilingual')) {
    return LANGUAGE_VOICE_CONFIGS['Hinglish']
  }
  if (normalized.includes('hindi')) {
    return LANGUAGE_VOICE_CONFIGS['Hindi']
  }
  if (normalized.includes('spanish')) {
    return LANGUAGE_VOICE_CONFIGS['Spanish']
  }
  if (normalized.includes('french')) {
    return LANGUAGE_VOICE_CONFIGS['French']
  }
  if (normalized.includes('german')) {
    return LANGUAGE_VOICE_CONFIGS['German']
  }
  return LANGUAGE_VOICE_CONFIGS['English']
}
