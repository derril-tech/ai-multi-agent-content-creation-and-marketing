import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Providers } from '@/components/providers/Providers'
import { Toaster } from 'react-hot-toast'

// Load Inter font for consistent typography
const inter = Inter({ subsets: ['latin'] })

// Metadata for SEO and browser
export const metadata: Metadata = {
  title: 'AI Multi-Agent Content Creation & Marketing',
  description: 'Next-generation AI-driven content automation platform with multi-agent orchestration for businesses and marketers.',
  keywords: ['AI', 'content creation', 'marketing automation', 'multi-agent', 'LangChain'],
  authors: [{ name: 'AI Multi-Agent Team' }],
  viewport: 'width=device-width, initial-scale=1',
  robots: 'index, follow',
}

// Root layout component that wraps all pages
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${inter.className} antialiased`}>
        {/* Global providers for state management, theming, etc. */}
        <Providers>
          {/* Main application content */}
          {children}
          
          {/* Global toast notifications */}
          <Toaster
            position="top-right"
            toastOptions={{
              duration: 4000,
              style: {
                background: '#363636',
                color: '#fff',
              },
              success: {
                duration: 3000,
                iconTheme: {
                  primary: '#10b981',
                  secondary: '#fff',
                },
              },
              error: {
                duration: 5000,
                iconTheme: {
                  primary: '#ef4444',
                  secondary: '#fff',
                },
              },
            }}
          />
        </Providers>
      </body>
    </html>
  )
}
