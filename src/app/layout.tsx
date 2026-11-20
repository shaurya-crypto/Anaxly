import type { Metadata, Viewport } from "next";
import "./globals.css";
import { MascotLazy } from "@/components/mascot/MascotLazy";
import { Analytics } from "@vercel/analytics/next";
import { Inter } from "next/font/google";

// Self-hosted by Next at build time: no render-blocking Google Fonts request.
const inter = Inter({
  subsets: ["latin"],
  axes: ["opsz"],
  style: ["normal", "italic"],
  display: "swap",
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "Anaxly - 1-on-1 Socratic Learning",
  description: "Real-time, low-latency live Socratic AI tutor",
  icons: {
    icon: [
      { url: '/favicon.ico', sizes: 'any' },
      { url: '/icon.svg', type: 'image/svg+xml' },
    ],
    apple: '/icon.svg',
  },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#FAF8F4",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={inter.variable}>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                if (typeof window === 'undefined') return;
                function isIgnorableError(err) {
                  if (!err) return false;
                  var msg = String(err.message || err.reason || err || '');
                  var name = String(err.name || (err.constructor && err.constructor.name) || '');
                  return (
                    msg.indexOf('Client initiated disconnect') !== -1 ||
                    msg.indexOf('Called Disconnect Before A Connecction succeeded') !== -1 ||
                    msg.indexOf('ConnectionError') !== -1 ||
                    name === 'ConnectionError'
                  );
                }
                window.addEventListener('unhandledrejection', function(event) {
                  if (isIgnorableError(event.reason)) {
                    event.preventDefault();
                    if (event.stopImmediatePropagation) event.stopImmediatePropagation();
                    if (event.stopPropagation) event.stopPropagation();
                  }
                }, true);
                window.addEventListener('error', function(event) {
                  if (isIgnorableError(event.error)) {
                    event.preventDefault();
                    if (event.stopImmediatePropagation) event.stopImmediatePropagation();
                    if (event.stopPropagation) event.stopPropagation();
                  }
                }, true);
              })();
            `,
          }}
        />
      </head>
      <body
        className="font-sans bg-canvas min-h-[100dvh] flex flex-col antialiased selection:bg-primary-fixed selection:text-ink-primary"
      >
        {children}
        <MascotLazy />
        <Analytics />
      </body>
    </html>
  );
}
