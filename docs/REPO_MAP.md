# Repository Map - AI Multi-Agent Content Creation & Marketing System

This document provides a comprehensive overview of the repository structure, explaining the purpose and organization of each folder and file in the AI Multi-Agent Content Creation & Marketing System.

## 📁 Root Directory Structure

```
ai-multi-agent-content-creation-and-marketing/
├── frontend/                 # Next.js 14 + React 18 frontend application
├── backend/                  # FastAPI Python backend application
├── docs/                     # Project documentation and guides
├── scripts/                  # Development and deployment scripts
├── .github/                  # GitHub Actions CI/CD workflows
├── PROJECT_BRIEF.md          # Complete project requirements and specifications
├── README.md                 # Main project readme
└── .gitignore               # Git ignore patterns
```

## 🎨 Frontend Structure (`frontend/`)

The frontend is built with Next.js 14, React 18, TypeScript, and Tailwind CSS.

### Core Files
- `package.json` - Dependencies and scripts
- `next.config.js` - Next.js configuration with optimizations
- `tailwind.config.js` - Tailwind CSS configuration with custom design tokens
- `tsconfig.json` - TypeScript configuration with path aliases

### Source Code (`src/`)
```
src/
├── app/                      # Next.js 13+ App Router
│   ├── layout.tsx           # Root layout with providers
│   ├── page.tsx             # Landing page
│   ├── globals.css          # Global styles and Tailwind directives
│   ├── dashboard/           # Dashboard pages
│   ├── auth/                # Authentication pages
│   └── api/                 # API routes (if needed)
├── components/              # Reusable React components
│   ├── ui/                  # Base UI components (Button, Card, etc.)
│   ├── layout/              # Layout components (Header, Sidebar, etc.)
│   ├── forms/               # Form components
│   ├── providers/           # Context providers
│   └── features/            # Feature-specific components
├── lib/                     # Utility functions and configurations
│   ├── utils.ts             # Common utility functions
│   ├── api.ts               # API client configuration
│   └── auth.ts              # Authentication utilities
├── hooks/                   # Custom React hooks
├── types/                   # TypeScript type definitions
├── stores/                  # State management (Zustand)
└── styles/                  # Additional styles and themes
```

### Key Frontend Features
- **Modern React**: Hooks, Context API, Suspense
- **TypeScript**: Full type safety across the application
- **Tailwind CSS**: Utility-first styling with custom design system
- **Real-time**: WebSocket integration for live collaboration
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: Optimized bundle size and loading times

## 🐍 Backend Structure (`backend/`)

The backend is built with FastAPI, SQLAlchemy 2.0, PostgreSQL, and Redis.

### Core Files
- `requirements.txt` - Python dependencies
- `main.py` - FastAPI application entry point
- `alembic.ini` - Database migration configuration
- `Dockerfile` - Container configuration

### Source Code (`app/`)
```
app/
├── main.py                  # Application entry point
├── core/                    # Core application modules
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database connection and models
│   ├── redis.py            # Redis connection and caching
│   ├── logging.py          # Structured logging setup
│   ├── security.py         # Authentication and authorization
│   └── exceptions.py       # Custom exception handlers
├── api/                     # API endpoints and routers
│   └── v1/                 # API version 1
│       ├── api.py          # Main API router
│       └── endpoints/      # Individual endpoint modules
│           ├── auth.py     # Authentication endpoints
│           ├── content.py  # Content management
│           ├── agents.py   # AI agent orchestration
│           ├── marketing.py # Marketing automation
│           ├── analytics.py # Analytics and reporting
│           └── websocket.py # WebSocket endpoints
├── models/                  # SQLAlchemy database models
│   ├── user.py             # User model
│   ├── content.py          # Content models
│   ├── agent.py            # AI agent models
│   └── marketing.py        # Marketing models
├── schemas/                 # Pydantic request/response schemas
├── services/                # Business logic services
│   ├── auth_service.py     # Authentication logic
│   ├── content_service.py  # Content generation
│   ├── agent_service.py    # AI agent orchestration
│   └── marketing_service.py # Marketing automation
├── agents/                  # AI agent implementations
│   ├── base.py             # Base agent class
│   ├── ideation.py         # Content ideation agent
│   ├── writer.py           # Content writing agent
│   ├── optimizer.py        # Content optimization agent
│   └── distributor.py      # Content distribution agent
└── utils/                   # Utility functions and helpers
```

### Key Backend Features
- **FastAPI**: Modern, fast web framework with automatic API docs
- **Async/Await**: Full async support for high performance
- **SQLAlchemy 2.0**: Modern ORM with async support
- **PostgreSQL**: Primary database with pgvector for AI embeddings
- **Redis**: Caching, sessions, and task queues
- **LangChain**: AI agent orchestration framework
- **WebSockets**: Real-time communication
- **JWT Authentication**: Secure token-based auth

## 📚 Documentation (`docs/`)

```
docs/
├── REPO_MAP.md             # This file - repository structure guide
├── API_SPEC.md             # Complete API documentation
├── CLAUDE.md               # AI collaboration guidelines
├── PROMPT_DECLARATION.md   # Project requirements and constraints
├── DEPLOYMENT.md           # Deployment instructions
├── DEVELOPMENT.md          # Development setup guide
└── ARCHITECTURE.md         # System architecture documentation
```

## 🔧 Scripts (`scripts/`)

```
scripts/
├── dev.sh                  # Development environment setup
├── deploy.sh               # Production deployment
├── test.sh                 # Run all tests
├── lint.sh                 # Code linting and formatting
└── db/                     # Database management scripts
    ├── migrate.sh          # Run database migrations
    └── seed.sh             # Seed database with test data
```

## 🚀 CI/CD (`.github/`)

```
.github/
├── workflows/              # GitHub Actions workflows
│   ├── ci.yml             # Continuous integration
│   ├── cd.yml             # Continuous deployment
│   └── security.yml       # Security scanning
└── ISSUE_TEMPLATE/        # Issue templates
```

## 📋 TODO Markers and Instructions

Throughout the codebase, you'll find TODO markers and `_INSTRUCTIONS.md` files that guide development:

### TODO Marker Examples
```typescript
// TODO: Implement user authentication flow
// TODO: Add real-time collaboration features
// TODO: Integrate with OpenAI GPT-4 API
```

### _INSTRUCTIONS.md Files
Each major folder contains an `_INSTRUCTIONS.md` file explaining:
- Purpose of the folder
- What should be implemented
- Coding conventions
- Integration points

## 🎯 Development Workflow

1. **Frontend Development**: Work in `frontend/src/` with Next.js App Router
2. **Backend Development**: Work in `backend/app/` with FastAPI
3. **Database**: Use Alembic for migrations in `backend/alembic/`
4. **Testing**: Frontend tests in `frontend/__tests__/`, backend in `backend/tests/`
5. **Documentation**: Update relevant files in `docs/`

## 🔗 Integration Points

- **Frontend ↔ Backend**: REST API calls via `/api/v1/` endpoints
- **Real-time**: WebSocket connections for live collaboration
- **Database**: PostgreSQL with pgvector for AI embeddings
- **Caching**: Redis for sessions and performance
- **AI Services**: OpenAI GPT-4 and Anthropic Claude integration
- **Storage**: AWS S3 for file uploads
- **Monitoring**: Prometheus + Grafana for observability

## 📝 File Naming Conventions

- **Components**: PascalCase (e.g., `UserProfile.tsx`)
- **Hooks**: camelCase with `use` prefix (e.g., `useAuth.ts`)
- **Utilities**: camelCase (e.g., `formatDate.ts`)
- **Types**: PascalCase (e.g., `UserTypes.ts`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `API_ENDPOINTS.ts`)
- **Python modules**: snake_case (e.g., `user_service.py`)
- **Python classes**: PascalCase (e.g., `UserService`)

This structure provides a scalable, maintainable foundation for the AI Multi-Agent Content Creation & Marketing System.
