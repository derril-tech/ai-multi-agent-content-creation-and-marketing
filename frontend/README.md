# Frontend - AI Multi-Agent Content Creation & Marketing System

This is the frontend application for the AI Multi-Agent Content Creation & Marketing System, built with Next.js 14, React 18, TypeScript, and Tailwind CSS.

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running (see backend README)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-multi-agent-content-creation-and-marketing/frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env.local
   # Edit .env.local with your configuration
   ```

4. **Start the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

5. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 📁 Project Structure

```
src/
├── app/                    # Next.js 13+ App Router
│   ├── layout.tsx         # Root layout with providers
│   ├── page.tsx           # Landing page
│   ├── globals.css        # Global styles
│   ├── dashboard/         # Dashboard pages
│   └── auth/              # Authentication pages
├── components/            # Reusable React components
│   ├── ui/               # Base UI components
│   ├── layout/           # Layout components
│   ├── forms/            # Form components
│   └── providers/        # Context providers
├── lib/                  # Utility functions
├── hooks/                # Custom React hooks
├── types/                # TypeScript definitions
└── stores/               # State management
```

## 🛠️ Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking
- `npm run test` - Run tests
- `npm run test:watch` - Run tests in watch mode
- `npm run test:coverage` - Run tests with coverage

## 🎨 Design System

The application uses a custom design system built with Tailwind CSS:

- **Colors**: Primary (blue), Secondary (purple), Accent (yellow), Neutral (gray)
- **Typography**: Inter font family
- **Components**: Reusable UI components in `src/components/ui/`
- **Themes**: Dark/light mode support
- **Accessibility**: WCAG 2.1 AA compliant

## 🔧 Configuration

### Environment Variables

Copy `env.example` to `.env.local` and configure:

```env
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000

# Authentication
NEXT_PUBLIC_AUTH_DOMAIN=your-auth-domain
NEXT_PUBLIC_AUTH_CLIENT_ID=your-client-id

# Analytics (Optional)
NEXT_PUBLIC_GA_TRACKING_ID=your-ga-tracking-id
NEXT_PUBLIC_MIXPANEL_TOKEN=your-mixpanel-token

# Feature Flags
NEXT_PUBLIC_ENABLE_ANALYTICS=true
NEXT_PUBLIC_ENABLE_SOCIAL_LOGIN=true
NEXT_PUBLIC_ENABLE_REAL_TIME_COLLABORATION=true
```

### Tailwind Configuration

Custom design tokens and utilities are configured in `tailwind.config.js`:

- Custom color palette
- Typography settings
- Animation utilities
- Component variants

## 🧪 Testing

The project uses Jest and React Testing Library for testing:

```bash
# Run all tests
npm run test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

## 📦 Build and Deployment

### Development Build

```bash
npm run build
npm run start
```

### Production Deployment

The application is optimized for deployment on Vercel:

1. Connect your repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

### Docker Deployment

```bash
# Build Docker image
docker build -t ai-multi-agent-frontend .

# Run container
docker run -p 3000:3000 ai-multi-agent-frontend
```

## 🔗 API Integration

The frontend communicates with the backend API through:

- **REST API**: HTTP requests to `/api/v1/` endpoints
- **WebSocket**: Real-time communication for live collaboration
- **Authentication**: JWT token-based authentication

### API Client

API calls are handled through a centralized client in `src/lib/api.ts`:

```typescript
import { apiClient } from '@/lib/api'

// Example API call
const content = await apiClient.get('/content')
```

## 🎯 Key Features

- **Modern React**: Hooks, Context API, Suspense
- **TypeScript**: Full type safety
- **Real-time**: WebSocket integration
- **Responsive**: Mobile-first design
- **Accessible**: WCAG 2.1 AA compliance
- **Performance**: Optimized bundle size
- **SEO**: Server-side rendering support

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill process on port 3000
   lsof -ti:3000 | xargs kill -9
   ```

2. **TypeScript errors**
   ```bash
   npm run type-check
   ```

3. **Build errors**
   ```bash
   rm -rf .next
   npm run build
   ```

### Getting Help

- Check the [Next.js documentation](https://nextjs.org/docs)
- Review the [Tailwind CSS documentation](https://tailwindcss.com/docs)
- Open an issue in the repository

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
