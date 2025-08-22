# THE PROJECT BRIEF #
Multi-Agent Content Creation & Marketing System

# Project Name #

# Product Description / Presentation #


Multi-Agent Content Creation & Marketing System

This system represents the next frontier of AI-driven content automation. By orchestrating multiple
intelligent agents working in harmony, it enables businesses, marketers, and creators to generate,
optimize, and distribute content at scale. The platform integrates specialized agents for ideation,
content drafting, optimization, compliance, and distribution, all coordinated seamlessly through
advanced multi-agent orchestration.

Key features include:
- Multi-agent coordination for content creation and marketing automation
- AI-powered ideation and intelligent content generation
- Real-time collaboration with human-in-the-loop workflows
- Automated distribution across multiple marketing channels
- Built-in hallucination correction and compliance validation
- Scalable, production-ready architecture supporting thousands of users

Teams love it because it eliminates repetitive tasks, shortens content cycles, and ensures
consistently high-quality output.
Framework Choice and Why
The system uses LangChain + FastAPI orchestration combined with OpenAI GPT-4 and Anthropic
Claude for advanced reasoning. LangChain is chosen for its composability, integrations, and agentbased framework. FastAPI powers the backend due to its async-first, production-grade
performance. Together, they provide scalability, extensibility, and strong developer ergonomics.

1. Backend Architecture
- FastAPI (Python 3.9+) for backend API
- SQLAlchemy 2.0 ORM with async/await
- PostgreSQL with pgvector extension for AI-powered semantic search
- Redis for caching and session management
- JWT-based authentication and secure session management
- LangChain integration for AI pipeline orchestration
- Real-time WebSocket support for collaboration
- Task queues with Celery or RQ for background jobs
- Structured logging and monitoring with Prometheus + Grafana
- REST + WebSocket hybrid endpoints
2. Frontend Architecture
- Next.js 14 + React 18 frontend
- TypeScript for type safety
- Tailwind CSS for design system
- Modular React components with hooks/context- Dark/light mode theming
- Responsive, mobile-first UI
- Real-time content updates via WebSockets
- WCAG 2.1 AA accessibility compliance
- State management with Zustand or Context API
- API integration layer for seamless backend communication
3. Design Requirements
- Minimalist, modern UI with marketing-focused branding
- Color schemes customizable per brand
- Smooth animations and micro-interactions
- Onboarding flows tailored for marketers
- Collaboration-first UX with real-time feedback indicators
- Accessibility-first design
- Optimized typography for readability
- Mobile-first, touch-friendly layouts
4. Core Integrations
- OpenAI GPT-4 for ideation and content generation
- Anthropic Claude for advanced reasoning and compliance
- LangChain agents for orchestration
- Cloud storage (AWS S3 / GCP Storage) for file management
- Email/SMS notifications (SendGrid/Twilio)
- OAuth for social media integrations
- Analytics integration (GA4, Mixpanel)
5. Deliverables Required
- Fully functional Next.js 14 frontend
- FastAPI backend with complete API set
- PostgreSQL schema with pgvector
- Redis caching setup
- LangChain agent orchestration pipelines
- Real-time WebSocket server
- File upload + cloud storage system
- Email notification system
- Documentation (APIs + Dev Guide)
- Deployment configs for Vercel + Render
6. Success Criteria
- Production-ready, scalable deployment
- 99.9% uptime SLA
- Sub-2s page load times
- 10,000+ concurrent user support
- API documentation (Swagger/OpenAPI)- 90%+ test coverage
- Lighthouse score >95
- WCAG 2.1 AA compliance
- Secure storage and transport of sensitive data
7. Implementation Guidelines
- Modern React best practices with hooks/context
- Strong TypeScript typing across codebase
- FastAPI dependency injection and async APIs
- SQLAlchemy 2.0 ORM with migrations
- Centralized error handling + logging
- Use environment variables for config
- Security-first coding (rate limiting, input validation)
- CI/CD with GitHub Actions
- Pre-commit hooks (lint, format, test)
- Unit, integration, and E2E test coverage
8. Security & Compliance
- JWT-based authentication with refresh tokens
- TLS/HTTPS for all communications
- Role-based access control (RBAC)
- GDPR/CCPA compliance for user data
- Data encryption at rest and in transit
- Regular security audits and penetration testing
- API rate limiting and abuse prevention
- Logging/auditing for compliance
- SOC 2 and ISO 27001 alignment

Claude Critical Prompts

PROMPT 1: PROJECT SETUP & ARCHITECTURE
Create the complete project structure and architecture for this multi-agent AI and marketing
application. Include frontend, backend, database, AI integrations, and deployment configs.
PROMPT 2: CORE BACKEND IMPLEMENTATION
Implement the FastAPI backend with PostgreSQL, pgvector, Redis, JWT authentication, LangChain
integration, and REST + WebSocket endpoints.
PROMPT 3: FRONTEND COMPONENTS & UI
Build the Next.js + React frontend with TypeScript, Tailwind CSS, real-time updates, accessibility
compliance, and dark/light mode.
PROMPT 4: AI INTEGRATION & FEATURES
Integrate OpenAI GPT-4 + Claude APIs via LangChain for content generation and marketing orchestration. Add cloud storage, notifications, and AI-powered workflows.
PROMPT 5: DEPLOYMENT & OPTIMIZATION
Configure deployments (Vercel + Render), optimize for performance, implement CI/CD, add
monitoring, and ensure security best practices.



FOLLOW THIS 8 STEP PLAN TO PREPARE THE INFRASTRUCTURE
-----------------------------------------------------

# 🚀 Claude Fullstack Repo Prep – Optimized 8 Step Plan

  
The goal: build an extensive frontend + backend scaffold so Claude Code only has to finish ~20% of the work.  
Each step must be **completed ** before advancing  (this is important).
IMPORTANT: YOU ARE BUILDING ONLY THE INFRASTRUCTURE OF THE APPLICATION NOT THE APPLICATION ITSELF !!!. FOLLOW THE STEPS IN NUMERICAL ORDER !!! starting from step 1.
You are doing the groundwork for the application, including setting up the folder structure, configuration files, and any necessary boilerplate code.
IMPORTANT: the checklist in each step has to be checked off 100% before moving to the next step. And always provide comments to your code blocks so that even a non-tech person can understand what you have done.

---

## STEP 1 — Build the Rich Infrastructure
Create a **deep scaffold** for both frontend and backend so Claude code can recognize the architecture immediately.

- Build a **frontend app shell** with routing, placeholder pages, components, and styling setup.  
- Build a **backend app shell** with API structure, health endpoint, and config in place.  
- Include `REPO_MAP.md`, `API_SPEC.md`, and a draft `CLAUDE.md` in the `docs/` folder.  (create the docs folder if it does not  already exist)
- Add **TODO markers and folder-level `_INSTRUCTIONS.md`** files so Claude knows exactly where to add logic.

**Deliverables**
- Frontend app shell with routing, placeholder pages, components, and styling setup  
- Backend app shell with API structure, health endpoint, and config  
- `docs/REPO_MAP.md`, `docs/API_SPEC.md` (stub), and draft `docs/CLAUDE.md`  
- TODO markers + folder-level `_INSTRUCTIONS.md` files  

**Checklist**
- [ ] Frontend scaffold built  
- [ ] Backend scaffold built 
- [ ] Docs folder created with drafts (`REPO_MAP.md`, `API_SPEC.md`, `CLAUDE.md`)  
- [ ] TODO markers and `_INSTRUCTIONS.md` stubs in place  

---

## STEP 2 — Enrich the Scaffold
If the repo looks shallow, enrich it so Claude needs fewer leaps of imagination.  

Add:
- Sample frontend routes and components (`/`, `/about`, `/dashboard`)  
- Domain model stubs and types/interfaces  
- Mock data + fixtures for UI flows  
- README files with quick run instructions for both frontend and backend  
- Instructions embedded in folders (e.g. `CLAUDE_TASK: …`)

**Deliverables**
- Sample routes and pages (`/`, `/about`, `/dashboard`)  
- Domain model stubs and type definitions  
- Mock data and fixtures for UI flows  
- README files for frontend and backend with run instructions  
- Folder-level instructions (`_INSTRUCTIONS.md`)  

**Checklist**
- [ ] At least 2–3 sample routes/pages exist  
- [ ] Domain types/interfaces stubbed out  
- [ ] Mock data + fixtures included  
- [ ] README_FRONTEND.md and README_BACKEND.md added  
- [ ] Each folder has `_INSTRUCTIONS.md` where relevant 

---

## STEP 3 — Audit for Alignment
Check that the scaffold actually matches the product brief, tech specs, and UX /UI goals.
Add additional UI/UX elements (if needed) to make the application visually appealing (and update the design requirements after that)

- Do navigation and pages reflect the product’s main flows?  
- Do API endpoints match the UI needs?  
- Is the chosen tech stack consistent (no unused or conflicting libraries)?  
- Is the UX direction reflected (design tokens, layout, component stubs)?

**Deliverables**
- Alignment review across Product ↔ UI/UX ↔ Tech  
- Identify any missing flows, mismatched libraries, or conflicting instructions  

**Checklist**
- [ ] Navigation structure matches product journeys  
- [ ] Components/pages map to required features  
- [ ] API endpoints cover MVP needs  
- [ ] No contradictory or unused technologies  

---

## STEP 4 — Document the Architecture
Now make the docs **Claude-ready**:

- **REPO_MAP.md**: Full repo breakdown with roles of each folder  
- **API_SPEC.md**: Endpoints, payloads, error handling  
- **CLAUDE.md**: Editing rules, coding conventions, AI collaboration guidelines  

These three files are the **context backbone** Claude will use to understand the repo.

**Deliverables**
- `REPO_MAP.md`: full repo breakdown with folder purposes  
- `API_SPEC.md`: endpoints, models, error conventions  
- `CLAUDE.md`: collaboration rules, editing boundaries  

**Checklist**
- [ ] REPO_MAP.md fully describes structure  
- [ ] API_SPEC.md covers all MVP endpoints and schemas  
- [ ] CLAUDE.md includes project overview, editing rules, examples  

---

## STEP 5 — Improve the Prompt
Enhance the prompt (in `docs/PROMPT_DECLARATION.md`) with details Claude needs:

- FE/BE boundaries and data contracts  
- UX guidelines (states, accessibility, interaction patterns)  
- Performance budgets (bundle size, API latency)  
- Security constraints (auth, rate limits, PII handling)  
- Testing expectations (unit, integration, end-to-end)

**Deliverables**
- FE/BE boundaries and contracts  
- UX guidelines (states, accessibility, patterns)  
- Performance budgets (bundle size, latency targets)  
- Security constraints (auth, PII, rate limits)  
- Testing expectations  

**Checklist**
- [ ] Prompt includes FE/BE division of responsibility  
- [ ] UX principles and design tokens specified  
- [ ] Performance/security/testing requirements added  
- [ ] Prompt is concrete and actionable for Claude  

---

## STEP 6 — Expert Audit of the Prompt
Now do a **meticulous audit** of the one-page prompt declaration.

- Add Frontend Architecture, Backend Architecture, Design requirements, Core Integrations, Success Criteria, Implementation Guidelines and Security & Compliance categories from this Project Brief to the prompt declaration.
- Remove inconsistencies, duplicates, or unused technologies  
- Ensure Tech Stack → Product → Scaffold alignment (no mismatches)  
- Add UI/UX details that make the product visually appealing and usable  
- Double-check frontend and backend folders are ready  
- Confirm editing boundaries are clear (what Claude can/can’t touch)  
- Make the declaration **battle-tested and handoff-ready**

**Deliverables**
- Remove inconsistencies/duplicates  
- Ensure stack ↔ product ↔ scaffold alignment  
- Add UI/UX and accessibility details  
- Clarify file boundaries (editable vs do-not-touch)  
- Confirm prompt uses Claude-friendly syntax  

**Checklist**
- [ ] No unused or contradictory tech remains  
- [ ] UI/UX directives are product-specific and sufficient  
- [ ] Editing boundaries explicitly defined  
- [ ] Prompt syntax uses clear, imperative instructions  

---

## STEP 7 — Bird’s-Eye Repo Review
Do a quick top-level scan for missing pieces:

- All folders contain either code or `_INSTRUCTIONS.md`  
- `.env.example` files exist for both frontend and backend  
- CI/CD config is present and not trivially broken  
- Run scripts (`npm run dev`, `uvicorn …`) work end-to-end  
- No orphan TODOs without clear ownership

**Deliverables**
- Verify all core files exist  
- Confirm environment, CI, and scripts work end-to-end  

**Checklist**
- [ ] Every folder has code or `_INSTRUCTIONS.md`  
- [ ] `.env.example` present for both frontend and backend  
- [ ] CI pipeline triggers and passes basic checks  
- [ ] Dev script (`scripts/dev.sh`) runs both FE and BE  

---

## STEP 8 — Finalize CLAUDE.md
This is where Claude gets its **onboarding pack**. Make sure `CLAUDE.md` includes:

- **Project Overview**: one-paragraph purpose, stack, goals, target users  
- **Folder & File Structure**: what’s editable vs do-not-touch  
- **Coding Conventions**: style guides, naming rules, commenting expectations  
- **AI Collaboration Rules**: response format, edit rules, ambiguity handling  
- **Editing Rules**: full-file vs patches, locked files  
- **Dependencies & Setup**: frameworks, services, env vars  
- **Workflow & Tools**: how to run locally, FE/BE boundary, deployment notes  
- **Contextual Knowledge**: product quirks, domain rules, business logic caveats  
- **Examples**: good vs bad AI answer

**Deliverables**
- Project overview (purpose, stack, goals, users)  
- Folder & file structure with editable vs do-not-touch  
- Coding conventions (style, naming, commenting)  
- AI collaboration rules (response style, edit rules, ambiguity handling)  
- Dependencies and setup instructions  
- Workflow, deployment notes, contextual knowledge  
- Good vs bad answer examples  
- Fill out all the missing information in the CLAUDE.md file

**Checklist**
- [ ] Project overview section filled in  
- [ ] File boundaries clearly defined  
- [ ] Coding/style conventions included  
- [ ] AI collaboration & editing rules written  
- [ ] Dependencies & env notes covered  
- [ ] Workflow & deployment info added  
- [ ] Contextual knowledge documented  
- [ ] Good vs bad examples included  
- [ ] CLAUDE.md file does not miss any important information

---

# ✅ Outcome
When this 8-step plan is followed:
- The repo is a **rich, opinionated scaffold** (80% done).  
- Docs give Claude **clear boundaries + context**.  
- The one-page prompt is **battle-tested** and aligned.  
- Claude Code can safely and efficiently generate the missing 20%.  












