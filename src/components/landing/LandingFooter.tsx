'use client'

import React from 'react'
import Link from 'next/link'

export function LandingFooter() {
  return (
    <footer className="w-full px-3 sm:px-6 lg:px-8 py-8 sm:py-14">
      {/* Expanded Width Box Container with Crisp White Background */}
      <div className="mx-auto w-full max-w-[1440px] rounded-3xl sm:rounded-[40px] border border-stone-200/90 bg-white shadow-[0_8px_30px_rgb(0,0,0,0.04),0_1px_3px_rgb(0,0,0,0.03)] overflow-hidden pt-12 sm:pt-16 pb-0">
        <div className="px-6 sm:px-12 text-center">
          {/* Curated Navigation Links — Clean, readable standard font, Zero Icons */}
          <nav
            aria-label="Footer Navigation"
            className="flex flex-wrap items-center justify-center gap-x-8 sm:gap-x-12 gap-y-3.5 text-sm sm:text-base font-medium text-stone-600"
          >
            <Link href="/#experience" className="hover:text-stone-950 transition-colors">
              Product
            </Link>
            <Link href="/#what-it-is" className="hover:text-stone-950 transition-colors">
              About Us
            </Link>
            <Link href="/pricing" className="hover:text-stone-950 transition-colors">
              Pricing
            </Link>
            <a
              href="mailto:careers@anaxly.com?subject=Careers%20at%20Anaxly"
              className="hover:text-stone-950 transition-colors"
            >
              Careers
            </a>
            <Link href="/pricing#faq" className="hover:text-stone-950 transition-colors">
              FAQ
            </Link>
            <a
              href="mailto:support@anaxly.com?subject=Contact%20Anaxly"
              className="hover:text-stone-950 transition-colors"
            >
              Contact
            </a>
            <a
              href="https://twitter.com"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-stone-950 transition-colors inline-flex items-center gap-1"
            >
              <span>Twitter</span>
              <span className="text-stone-400 font-normal text-sm" aria-hidden="true">↗</span>
            </a>
            <a
              href="https://linkedin.com"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-stone-950 transition-colors inline-flex items-center gap-1"
            >
              <span>LinkedIn</span>
              <span className="text-stone-400 font-normal text-sm" aria-hidden="true">↗</span>
            </a>
          </nav>

          {/* Secondary Row: Privacy, Terms & Copyright in standard font */}
          <div className="mt-5 flex flex-wrap items-center justify-center gap-6 text-xs sm:text-sm text-stone-500 font-normal">
            <Link href="/privacy" className="hover:text-stone-900 transition-colors">
              Privacy Policy
            </Link>
            <span className="text-stone-300" aria-hidden="true">&bull;</span>
            <Link href="/terms" className="hover:text-stone-900 transition-colors">
              Terms of Service
            </Link>
            <span className="text-stone-300" aria-hidden="true">&bull;</span>
            <span>&copy; {new Date().getFullYear()} Anaxly Inc.</span>
          </div>
        </div>

        {/* Monumental ANAXLY Big Text (Slightly refined size, in Capital, fading to white floor) */}
        <div className="relative w-full overflow-hidden select-none pointer-events-none mt-8 sm:mt-12 md:mt-14">
          <span
            className="block w-full text-center font-sans font-black tracking-tight leading-[0.78] text-[clamp(4.25rem,16.5vw,19.5rem)] bg-gradient-to-b from-stone-950 via-stone-400/50 to-transparent bg-clip-text text-transparent transform translate-y-2 sm:translate-y-4 md:translate-y-6 uppercase"
            aria-hidden="true"
          >
            ANAXLY
          </span>
        </div>
      </div>
    </footer>
  )
}
