# CLAUDE.md — Collaboration & Editing Guidelines

This document is Claude's onboarding guide for the AI Multi-Agent Content Creation & Marketing System.  
It defines the **purpose of the project, coding conventions, editing rules, and collaboration workflow**.  
Claude should always respect these boundaries when generating code.

---

## 📌 Project Overview

**Name:** AI Multi-Agent Content Creation & Marketing System  
**Purpose:** AI-driven content automation platform that orchestrates multiple intelligent agents for ideation, content creation, optimization, and distribution. The system enables businesses, marketers, and creators to generate, optimize, and distribute content at scale through specialized agents working in harmony.  
**Target Users:** Businesses, marketers, content creators, and agencies  
**Goals:** Eliminate repetitive tasks, shorten content cycles by 70%, ensure consistently high-quality output, support thousands of users simultaneously  
**Tech Stack:**  
  - Frontend: Next.js 14 + React 18 + TypeScript + Tailwind CSS + Zustand + React Query  
  - Backend: FastAPI + SQLAlchemy 2.0 + PostgreSQL + Redis + LangChain + OpenAI/Anthropic  
  - Services: OpenAI GPT-4, Anthropic Claude, AWS S3/GCP Storage, SendGrid/Twilio, OAuth integrations  

---

## 📂 Folder & File Structure

```
ai-multi-agent-content-creation-and-marketing/
├── frontend/                    # Next.js 14 frontend application
│   ├── src/
│   │   ├── app/                # Next.js App Router pages
│   │   ├── components/         # React components (UI, layout, features)
│   │   ├── hooks/              # Custom React hooks
│   │   ├── types/              # TypeScript type definitions
│   │   ├── lib/                # Utility functions and API clients
│   │   └── providers/          # Context providers (theme, auth, etc.)
│   ├── public/                 # Static assets
│   ├── package.json            # Frontend dependencies
│   ├── next.config.js          # Next.js configuration
│   ├── tailwind.config.js      # Tailwind CSS configuration
│   ├── tsconfig.json           # TypeScript configuration
│   └── env.example             # Frontend environment variables
├── backend/                     # FastAPI backend application
│   ├── app/
│   │   ├── api/                # API endpoints and routers
│   │   │   └── v1/
│   │   │       ├── endpoints/  # Individual endpoint modules
│   │   │       └── api.py      # Main API router
│   │   ├── core/               # Core application modules
│   │   │   ├── config.py       # Application configuration
│   │   │   ├── database.py     # Database connection and session
│   │   │   ├── redis.py        # Redis connection and caching
│   │   │   └── logging.py      # Structured logging setup
│   │   ├── models/             # SQLAlchemy database models
│   │   ├── services/           # Business logic services
│   │   └── schemas/            # Pydantic schemas
│   ├── main.py                 # FastAPI application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Backend container configuration
│   └── env.example             # Backend environment variables
├── docs/                       # Project documentation
│   ├── REPO_MAP.md            # Repository structure overview
│   ├── API_SPEC.md            # API documentation and specifications
│   ├── PROMPT_DECLARATION.md  # AI prompt guidelines
│   └── CLAUDE.md              # This file
├── scripts/                    # Utility scripts
│   └── dev.sh                 # Development environment setup
├── .github/                    # CI/CD workflows
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD pipeline
├── docker-compose.yml          # Multi-service container orchestration
├── .gitignore                  # Git ignore patterns
└── README.md                   # Project overview and setup instructions
```

### Editable by Claude
- `frontend/src/**/*` (except `_INSTRUCTIONS.md` files)  
- `backend/app/**/*` (except core config files)  
- Tests in `frontend/tests/` and `backend/tests/`  
- Documentation files in `docs/` (except this file)

### Do Not Touch
- `PROJECT_BRIEF.md` (project requirements and specifications)
- Lockfiles (`package-lock.json`, `poetry.lock`, etc.)  
- CI/CD configs (`.github/workflows/*`) unless explicitly requested  
- Auto-generated code or migrations  
- Core configuration files (`package.json`, `requirements.txt`, etc.)
- Docker files unless specifically requested
- This file (`CLAUDE.md`)  

---

## 🎨 Coding Conventions

**Languages:** TypeScript (frontend), Python (backend)  
**Style Guides:**  
  - Frontend: Prettier + ESLint (Next.js rules)  
  - Backend: Black + isort + mypy (PEP8)  
**Naming:**  
  - Components: `PascalCase` (e.g., `ContentEditor`, `AgentStatus`)
  - Variables: `camelCase` (TS), `snake_case` (Python)  
  - Files: `kebab-case` for components, `snake_case` for utilities
  - Branches: `feature/…`, `fix/…`, `docs/…`  
**Commenting:**  
  - Document public components, functions, and non-obvious logic  
  - Use `// TODO:` or `# TODO:` for clear tasks
  - Include JSDoc for complex functions and components
  - Add inline comments for business logic

**Frontend Specific:**
- Use functional components with hooks
- Implement proper TypeScript types for all props and state
- Follow React best practices (key props, proper dependencies)
- Use Tailwind CSS for styling with custom design tokens
- Implement accessibility features (ARIA labels, keyboard navigation)

**Backend Specific:**
- Use async/await for all database and external API calls
- Implement proper error handling with custom exceptions
- Use Pydantic for request/response validation
- Follow FastAPI dependency injection patterns
- Use structured logging with context

---

## 🤝 AI Collaboration Rules

- Always respond with **full file rewrites** if >30 lines are changed.  
- Keep responses **concise in explanation, complete in code**.  
- Never remove error handling, logging, or comments unless replacing them with better versions.  
- Preserve imports and typing.  
- If ambiguity arises:  
  1. Ask up to **2 clarifying questions**  
  2. If unanswered, proceed with best guess and note assumptions
- Always include proper TypeScript types and error handling
- Follow the established patterns in the codebase
- Use the design system components when available

---

## ✍️ Editing Rules

**Editable Files:** All app source code under `frontend/src/` and `backend/app/`  
**Avoid:** lockfiles, auto-generated files, CI configs, core configuration files  
**Format of Responses:**  
  - Full file rewrites for large changes  
  - Patches (with clear diff context) for small fixes  
**Error Handling:** must remain in place at all times  
**TypeScript:** All frontend code must be properly typed
**Testing:** Include unit tests for new functionality

---

## 📦 Project Dependencies

**Frontend:** 
- Next.js 14, React 18, TypeScript 5.0
- Tailwind CSS, Zustand, React Query
- Lucide React, Framer Motion, React Hook Form
- Testing: Jest, React Testing Library

**Backend:** 
- FastAPI, SQLAlchemy 2.0, PostgreSQL, Redis
- LangChain, OpenAI, Anthropic
- Celery/RQ, Prometheus, Grafana
- Testing: Pytest, pytest-asyncio

**Services:** 
- OpenAI GPT-4, Anthropic Claude
- AWS S3/GCP Storage, SendGrid/Twilio
- OAuth providers, Analytics platforms

**Environment:**  
  - Variables in `.env.example` must be respected  
  - Secrets should never be hardcoded  
  - Use environment-specific configurations

---

## 🛠️ Workflow & Tools

**Run locally:**  
  - Use `scripts/dev.sh` to start both frontend and backend
  - Frontend: `npm run dev` (http://localhost:3000)
  - Backend: `uvicorn main:app --reload` (http://localhost:8000)
  - Database: PostgreSQL with pgvector extension
  - Cache: Redis for session management and caching

**FE ↔ BE boundary:** REST JSON via `/api/v1/*` + WebSocket for real-time features  
**Testing:**  
  - Frontend: Jest + React Testing Library  
  - Backend: Pytest + pytest-asyncio  
**CI/CD:** GitHub Actions (lint, type-check, test, build, security scan)  
**Deployment:** Vercel (frontend) + Render/Heroku (backend) + managed PostgreSQL/Redis

**Development Workflow:**
1. Create feature branch from `develop`
2. Implement changes with proper testing
3. Run linting and type checking
4. Submit pull request with description
5. CI/CD pipeline validates changes
6. Code review and merge to `develop`
7. Deploy to staging for testing
8. Merge to `main` for production deployment

---

## 📚 Contextual Knowledge

**Design System:** 
- Color palette: primary (blue), secondary (gray), accent (purple), neutral (gray scale)
- Typography: Inter for UI, JetBrains Mono for code
- Spacing: Consistent 4px grid system
- Components: Button, Card, Badge, Input, Modal, etc.
- Animations: fade-in, slide-up, pulse-slow

**Domain Rules:** 
- Content creation follows marketing best practices
- Multi-agent orchestration requires careful state management
- Real-time collaboration needs conflict resolution
- AI-generated content requires human oversight
- Content approval workflows with role-based access
- Brand compliance validation and safety checks

**Scaffolding Rules:** 
- Scalability categories mirror design categories
- Performance optimization at every level
- Security-first approach with proper authentication
- Accessibility compliance (WCAG 2.1 AA)
- Comprehensive error handling and logging

**UX Principles:** 
- Accessibility (a11y) compliance required
- Empty/loading/error states for all async operations
- Mobile-first responsive design
- Real-time feedback for user actions
- Intuitive navigation and information architecture

**Technical Constraints:**
- Sub-2s page load times
- 99.9% uptime SLA
- 10,000+ concurrent user support
- 90%+ test coverage
- Lighthouse score >95

---

## ✅ Examples

**Good Answer Example**
```tsx
// Good: Full file rewrite, proper TypeScript, error handling, accessibility
import { useEffect, useState } from "react";
import { useQuery } from "react-query";
import { fetchContent } from "@/lib/api";
import { Content, ApiError } from "@/types/content";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";

interface ContentListProps {
  filters?: ContentFilters;
  onContentSelect?: (content: Content) => void;
}

export default function ContentList({ filters, onContentSelect }: ContentListProps) {
  const { data: content, isLoading, error } = useQuery<Content[], ApiError>({
    queryKey: ['content', filters],
    queryFn: () => fetchContent(filters),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  if (isLoading) {
    return (
      <div className="space-y-4">
        {[...Array(3)].map((_, i) => (
          <Card key={i} className="animate-pulse">
            <CardContent className="h-24 bg-gray-200 rounded" />
          </Card>
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-8">
        <p className="text-red-600 mb-4">Error loading content: {error.message}</p>
        <Button onClick={() => window.location.reload()}>Retry</Button>
      </div>
    );
  }

  if (!content?.length) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">No content found</p>
      </div>
    );
  }

  return (
    <div className="space-y-4" role="list">
      {content.map((item) => (
        <Card 
          key={item.id} 
          className="hover:shadow-md transition-shadow cursor-pointer"
          onClick={() => onContentSelect?.(item)}
          role="listitem"
          tabIndex={0}
          onKeyDown={(e) => e.key === 'Enter' && onContentSelect?.(item)}
        >
          <CardHeader>
            <CardTitle className="flex items-center justify-between">
              <span>{item.title}</span>
              <Badge variant={item.status === 'published' ? 'default' : 'secondary'}>
                {item.status}
              </Badge>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600 line-clamp-2">{item.description}</p>
            <div className="flex gap-2 mt-2">
              {item.tags.map((tag) => (
                <Badge key={tag} variant="outline" className="text-xs">
                  {tag}
                </Badge>
              ))}
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
```

**Bad Answer Example**
```tsx
// Bad: No types, no error handling, no accessibility, inconsistent patterns
export default function ContentList() {
  const [content, setContent] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/content').then(res => res.json()).then(setContent);
    setLoading(false);
  }, []);

  if (loading) return <div>Loading...</div>;
  
  return (
    <div>
      {content.map(item => (
        <div key={item.id}>
          <h3>{item.title}</h3>
          <p>{item.description}</p>
        </div>
      ))}
    </div>
  );
}
```

**Backend Good Example**
```python
# Good: Proper async/await, error handling, type hints, logging
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.logging import get_logger
from app.models.content import Content
from app.schemas.content import ContentCreate, ContentResponse, ContentFilters
from app.services.content import ContentService

logger = get_logger(__name__)
router = APIRouter()

@router.get("/", response_model=List[ContentResponse])
async def get_content(
    filters: Optional[ContentFilters] = None,
    db: AsyncSession = Depends(get_db)
) -> List[ContentResponse]:
    """
    Retrieve content items with optional filtering.
    
    Args:
        filters: Optional filters for content query
        db: Database session dependency
        
    Returns:
        List of content items
        
    Raises:
        HTTPException: If database query fails
    """
    try:
        content_service = ContentService(db)
        content_items = await content_service.get_content(filters)
        
        logger.info(f"Retrieved {len(content_items)} content items")
        return [ContentResponse.from_orm(item) for item in content_items]
        
    except Exception as e:
        logger.error(f"Error retrieving content: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve content"
        )

@router.post("/", response_model=ContentResponse, status_code=status.HTTP_201_CREATED)
async def create_content(
    content_data: ContentCreate,
    db: AsyncSession = Depends(get_db)
) -> ContentResponse:
    """Create a new content item."""
    try:
        content_service = ContentService(db)
        content = await content_service.create_content(content_data)
        
        logger.info(f"Created content item with ID: {content.id}")
        return ContentResponse.from_orm(content)
        
    except ValueError as e:
        logger.warning(f"Validation error creating content: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error creating content: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create content"
        )
```

**Backend Bad Example**
```python
# Bad: No error handling, no type hints, no logging, synchronous code
from fastapi import APIRouter
from app.models import Content

router = APIRouter()

@router.get("/")
def get_content():
    content = Content.query.all()
    return content

@router.post("/")
def create_content(data):
    content = Content(**data)
    content.save()
    return content
```




