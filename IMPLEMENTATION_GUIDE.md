# Lead Gear Content Creation Tool - Implementation Guide

## Status: Foundation Complete ✅

**Version:** 1.0.0-alpha
**Last Updated:** October 23, 2025
**Branch:** `claude/process-prd-file-011CUQZvyuo54emVceBgEJPW`

---

## Table of Contents

1. [What's Been Built](#whats-been-built)
2. [Getting Started](#getting-started)
3. [Architecture Overview](#architecture-overview)
4. [Next Steps (Roadmap)](#next-steps-roadmap)
5. [API Integration Guide](#api-integration-guide)
6. [Testing Strategy](#testing-strategy)
7. [Deployment Guide](#deployment-guide)

---

## What's Been Built

### ✅ Completed (Week 1-2 Foundation)

#### Backend Infrastructure
- **FastAPI Application** (`backend/main.py`)
  - Auto-generated API documentation at `/docs`
  - CORS middleware configured for frontend
  - Health check endpoints
  - Lifespan management

- **Database Layer** (`backend/database.py`)
  - SQLAlchemy ORM configuration
  - SQLite for development (easy PostgreSQL migration)
  - Session management with dependency injection

- **Data Models** (`backend/models/`)
  - `User`: Authentication and user management
  - `Project`: Client/project information
  - `ContentPiece`: Blog posts with all metadata
  - `KeywordResearch`: SERP analysis data storage

- **Authentication System** (`backend/utils/auth.py`, `backend/routes/auth.py`)
  - JWT token-based authentication
  - Bcrypt password hashing
  - Registration and login endpoints
  - Protected route middleware

- **API Routes** (`backend/routes/`)
  - ✅ `/api/auth/*` - Registration, login, user info
  - ✅ `/api/projects/*` - Full CRUD operations
  - 🔄 `/api/keywords/research` - Placeholder (needs DataForSEO)
  - 🔄 `/api/serp/analyze` - Placeholder (needs scraping)
  - 🔄 `/api/briefs/*` - Placeholder (needs Claude integration)
  - 🔄 `/api/content/*` - Placeholder (needs Claude integration)
  - 🔄 `/api/meta/*` - Placeholder (needs Claude integration)
  - 🔄 `/api/export/google-docs` - Placeholder (needs Google API)

- **Pydantic Schemas** (`backend/schemas/`)
  - Request/response validation for all endpoints
  - Type safety and auto-documentation

- **Celery Task Queue** (`backend/tasks/`)
  - Configured for long-running operations
  - Placeholder tasks for content generation
  - Progress tracking support

#### Frontend Application
- **React + TypeScript Setup** (`frontend/`)
  - Vite for fast development
  - Tailwind CSS for styling
  - TypeScript for type safety

- **State Management** (`frontend/src/stores/`)
  - Zustand for global state
  - Auth state with persistence
  - Token management

- **Routing** (`frontend/src/App.tsx`)
  - Protected routes
  - Public routes (login/register)
  - Nested layout structure

- **API Client** (`frontend/src/services/api.ts`)
  - Axios with interceptors
  - Automatic token injection
  - Error handling and 401 redirects
  - Organized API methods by domain

- **UI Pages** (`frontend/src/pages/`)
  - ✅ Login page with form validation
  - ✅ Register page
  - ✅ Home dashboard
  - ✅ Projects list with loading states
  - 🔄 Project details (placeholder)
  - 🔄 Keyword research (placeholder)
  - 🔄 Content editor (placeholder)

- **Components** (`frontend/src/components/`)
  - Layout with header and navigation
  - Responsive design
  - Loading states and error handling

#### Infrastructure
- **Docker Setup** (`docker-compose.yml`)
  - Frontend container (React + Vite)
  - Backend container (FastAPI + Uvicorn)
  - Redis container (Celery broker)
  - Celery worker container
  - Hot-reload for development

- **Configuration** (`.env.example`, `backend/config.py`)
  - Environment variable management
  - API keys configuration
  - Feature flags and settings

- **Documentation** (`README.md`)
  - Setup instructions
  - Architecture overview
  - Getting started guide

---

## Getting Started

### Prerequisites
```bash
# Required
- Docker & Docker Compose
- Git

# Optional (for local development without Docker)
- Node.js 18+
- Python 3.11+
- Redis
```

### Quick Start

1. **Clone and setup:**
```bash
git clone <repository-url>
cd leadgear-content-creator
cp .env.example .env
```

2. **Configure API keys in `.env`:**
```bash
# Required for full functionality (add later as features are implemented)
ANTHROPIC_API_KEY=sk-ant-...           # Claude API
DATAFORSEO_LOGIN=...                   # DataForSEO
DATAFORSEO_PASSWORD=...                # DataForSEO
PERPLEXITY_API_KEY=pplx-...           # Perplexity
GOOGLE_CLIENT_ID=...                   # Google OAuth
GOOGLE_CLIENT_SECRET=...               # Google OAuth

# Generated automatically
JWT_SECRET=your-secret-key-here
```

3. **Start the application:**
```bash
docker-compose up
```

4. **Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Redis: localhost:6379

5. **Create your first account:**
- Navigate to http://localhost:3000/register
- Create an account
- Login and explore!

### Development Without Docker

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Redis + Celery:**
```bash
# Terminal 1: Redis
docker run -d -p 6379:6379 redis:7-alpine

# Terminal 2: Celery worker
cd backend
celery -A tasks.celery_app worker --loglevel=info
```

---

## Architecture Overview

### System Diagram
```
┌─────────────────────────────────────────────────────────┐
│                  React Frontend (Port 3000)              │
│  ┌─────────────┐ ┌──────────────┐ ┌─────────────────┐  │
│  │  Auth Flow  │ │  Projects    │ │   Content       │  │
│  │  (Working)  │ │  (Working)   │ │   (Placeholder) │  │
│  └─────────────┘ └──────────────┘ └─────────────────┘  │
└────────────────────────┬────────────────────────────────┘
                         │ REST API (JWT Auth)
┌────────────────────────▼────────────────────────────────┐
│              FastAPI Backend (Port 8000)                 │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Routes: auth ✅ projects ✅ content 🔄          │  │
│  │  Models: User, Project, ContentPiece             │  │
│  │  Auth: JWT + Bcrypt                              │  │
│  └──────────────────────────────────────────────────┘  │
└─────────┬───────────────┬─────────────────┬────────────┘
          │               │                 │
┌─────────▼───┐  ┌───────▼────────┐  ┌────▼──────────┐
│   SQLite    │  │  Redis + Celery │  │  External APIs│
│  (Working)  │  │  (Configured)   │  │  (TODO)       │
└─────────────┘  └─────────────────┘  └───────────────┘
```

### Database Schema

**Users Table:**
- id (UUID, PK)
- email (unique)
- hashed_password
- full_name
- google_access_token
- google_refresh_token
- created_at, updated_at

**Projects Table:**
- id (UUID, PK)
- user_id (FK → users)
- name, website_url, industry
- target_locations (JSON)
- main_services (JSON)
- competitors (JSON)
- business_goals (text)
- google_search_console_token
- google_analytics_token
- baseline_organic_traffic
- baseline_keywords
- baseline_top_pages (JSON)
- created_at, updated_at

**Content Pieces Table:**
- id (UUID, PK)
- project_id (FK → projects)
- primary_keyword, secondary_keywords (JSON)
- keyword_data (JSON)
- brief (JSON) - All 10 SOP-005 sections
- brief_approved (boolean)
- serp_analysis (JSON)
- content_html, content_markdown
- word_count, target_word_count
- title_tag, meta_description, url_slug
- readability_score, seo_score, keyword_density
- image_suggestions (JSON)
- status (draft/review/approved/exported)
- google_doc_url, exported_at
- created_at, updated_at

**Keyword Research Table:**
- id (UUID, PK)
- content_piece_id (FK → content_pieces, unique)
- keywords (JSON)
- serp_results (JSON)
- content_gaps (JSON)
- related_questions (JSON)
- created_at, updated_at

### API Endpoints Summary

| Endpoint | Method | Status | Description |
|----------|--------|--------|-------------|
| `/api/auth/register` | POST | ✅ Working | Register new user |
| `/api/auth/login` | POST | ✅ Working | Login with credentials |
| `/api/auth/me` | GET | ✅ Working | Get current user |
| `/api/projects` | GET | ✅ Working | List user's projects |
| `/api/projects` | POST | ✅ Working | Create new project |
| `/api/projects/:id` | GET | ✅ Working | Get project details |
| `/api/projects/:id` | PATCH | ✅ Working | Update project |
| `/api/projects/:id` | DELETE | ✅ Working | Delete project |
| `/api/projects/:id/baseline` | GET | 🔄 TODO | Fetch Google metrics |
| `/api/keywords/research` | POST | 🔄 TODO | Research keywords (DataForSEO) |
| `/api/serp/analyze` | POST | 🔄 TODO | Analyze SERP + scrape |
| `/api/briefs/generate` | POST | 🔄 TODO | Generate brief (Claude) |
| `/api/briefs/:id` | GET/PATCH | 🔄 TODO | Get/update brief |
| `/api/briefs/:id/approve` | POST | 🔄 TODO | Approve brief |
| `/api/content/generate` | POST | 🔄 TODO | Generate content (Claude) |
| `/api/content/:id` | GET/PATCH | 🔄 TODO | Get/update content |
| `/api/content/:id/improve` | POST | 🔄 TODO | AI improvements |
| `/api/content/:id/validate` | POST | 🔄 TODO | Quality checks |
| `/api/meta/generate` | POST | 🔄 TODO | Generate meta tags |
| `/api/export/google-docs` | POST | 🔄 TODO | Export to Google Docs |

---

## Next Steps (Roadmap)

### Week 3-4: Core Integrations

#### Priority 1: DataForSEO Integration
**File:** `backend/integrations/dataforseo_client.py`

```python
# Create DataForSEO API client
class DataForSEOClient:
    def __init__(self, login: str, password: str):
        self.auth = (login, password)
        self.base_url = "https://api.dataforseo.com/v3"

    async def keyword_suggestions(self, keywords: List[str], location: str = "United States"):
        """Fetch keyword suggestions with metrics"""
        # Implementation details in PRD Section 5.2
        pass

    async def serp_organic(self, keyword: str, location: str, num_results: int = 10):
        """Fetch organic SERP results"""
        # Implementation details in PRD Section 5.3
        pass
```

**Update route:** `backend/routes/keywords.py`
- Replace placeholder with actual DataForSEO calls
- Add error handling for API failures
- Implement caching (24-hour TTL) to reduce costs
- Store results in `KeywordResearch` table

**Frontend update:** `frontend/src/pages/KeywordResearchPage.tsx`
- Build keyword input form
- Display results in sortable table
- Add filters (volume, difficulty, question keywords)
- Allow primary/secondary keyword selection

#### Priority 2: SERP Analysis + Web Scraping
**File:** `backend/integrations/scraper.py`

```python
# Create web scraper for SERP results
class ContentScraper:
    async def scrape_url(self, url: str) -> dict:
        """Scrape content, headers, word count from URL"""
        # Use BeautifulSoup or Playwright
        # Extract: word count, H2/H3 headers, content structure
        pass
```

**Create Celery task:** `backend/tasks/content_tasks.py`
- Update `analyze_serp` task with real implementation
- Scrape top 10 URLs concurrently
- Extract headers, word counts, content structure
- Identify content gaps
- Use Perplexity for related questions
- Update progress state for real-time UI updates

**Frontend update:**
- Create SERP analysis UI
- Show loading progress (real-time updates via WebSocket or polling)
- Display competitor analysis table
- Show content gaps and related questions

#### Priority 3: Claude API Integration (Content Briefs)
**File:** `backend/integrations/claude_client.py`

```python
import anthropic

class ClaudeClient:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    async def generate_content_brief(self, project_data: dict, keyword_data: dict, serp_analysis: dict) -> dict:
        """Generate 10-section content brief following SOP-005"""
        prompt = self._build_brief_prompt(project_data, keyword_data, serp_analysis)

        message = await self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )

        # Parse response into 10 sections
        brief = self._parse_brief_response(message.content)
        return brief

    def _build_brief_prompt(self, project_data, keyword_data, serp_analysis):
        """Build comprehensive prompt following PRD Section 5.4"""
        # See PRD for exact prompt structure
        pass
```

**Update route:** `backend/routes/briefs.py`
- Implement `generate_brief` endpoint
- Call Claude API with structured prompt
- Store result in `ContentPiece.brief`
- Handle API errors gracefully

**Frontend update:** `frontend/src/pages/BriefEditorPage.tsx`
- Create expandable sections UI for 10 brief sections
- Allow inline editing of each section
- Add "Regenerate" button for each section
- Show loading state during generation

#### Priority 4: Claude API Integration (Content Generation)
**Update:** `backend/integrations/claude_client.py`

```python
async def generate_content(self, brief: dict, stream: bool = True):
    """Generate content following SOP-006 guidelines"""
    prompt = self._build_content_prompt(brief)

    if stream:
        # Stream response for real-time UI updates
        async with self.client.messages.stream(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            async for text in stream.text_stream:
                yield text
    else:
        # Non-streaming response
        message = await self.client.messages.create(...)
        return message.content
```

**Update route:** `backend/routes/content.py`
- Implement streaming endpoint with Server-Sent Events (SSE)
- Generate content section-by-section
- Update `ContentPiece` in database

**Frontend update:** `frontend/src/pages/ContentEditorPage.tsx`
- Integrate TipTap rich text editor
- Stream content as it generates
- Show progress indicator
- Allow real-time editing

### Week 5-6: Content Editor & Quality Checks

#### Priority 5: TipTap Rich Text Editor
**File:** `frontend/src/components/RichTextEditor.tsx`

```typescript
import { useEditor, EditorContent } from '@tiptap/react'
import StarterKit from '@tiptap/starter-kit'

export default function RichTextEditor({ content, onChange }) {
  const editor = useEditor({
    extensions: [StarterKit],
    content,
    onUpdate: ({ editor }) => {
      onChange(editor.getHTML())
    },
  })

  return (
    <div className="rich-text-editor">
      <EditorContent editor={editor} />
    </div>
  )
}
```

Features to implement:
- Bold, italic, lists, headers
- AI improvement button (highlight text → suggest improvements)
- Image placeholder insertion
- Internal link suggestions
- Word count tracker
- Auto-save every 30 seconds

#### Priority 6: Quality Checks
**File:** `backend/utils/quality_checker.py`

```python
import textstat

class QualityChecker:
    def __init__(self):
        self.ai_cliches = [
            "game-changer", "dive deeper", "in today's world",
            # ... full list from PRD Section 21
        ]

    def check_readability(self, text: str) -> float:
        """Calculate Flesch Reading Ease score"""
        return textstat.flesch_reading_ease(text)

    def check_seo(self, content: str, primary_keyword: str, secondary_keywords: List[str]) -> dict:
        """Run 15+ SEO validation rules"""
        # Keyword in first 100 words
        # Keyword in H1
        # Keyword in 2-3 H2s
        # Internal/external links
        # Word count target
        # etc.
        pass

    def check_keyword_density(self, text: str, keyword: str) -> float:
        """Calculate keyword density (target 0.5-1.5%)"""
        pass

    def detect_ai_cliches(self, text: str) -> List[str]:
        """Find AI writing patterns"""
        found = []
        for cliche in self.ai_cliches:
            if cliche.lower() in text.lower():
                found.append(cliche)
        return found
```

**Frontend update:**
- Create quality dashboard sidebar
- Show real-time scores
- Highlight issues in editor
- Provide fix suggestions

### Week 7-8: Meta Tags & Images

#### Priority 7: Meta Tag Generation
**Update:** `backend/integrations/claude_client.py`

```python
async def generate_meta_tags(self, content: str, primary_keyword: str, client_name: str) -> dict:
    """Generate title tag, meta description, URL slug"""
    prompt = f"""Generate SEO-optimized meta tags...

    PRIMARY KEYWORD: {primary_keyword}
    CONTENT SUMMARY: {content[:500]}
    CLIENT: {client_name}

    Generate:
    1. Title tag (50-60 chars)
    2. Meta description (140-155 chars)
    3. URL slug
    """
    # Implementation
    pass
```

#### Priority 8: Image Suggestions
- Scan content for visual opportunities
- Suggest 5-8 image placements
- Generate descriptive alt text
- Categorize by type (hero, screenshot, diagram, etc.)

### Week 9-10: Google APIs Integration

#### Priority 9: Google OAuth & Search Console
**File:** `backend/integrations/google_client.py`

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class GoogleClient:
    def __init__(self, credentials: dict):
        self.creds = Credentials(**credentials)

    async def get_search_console_data(self, site_url: str) -> dict:
        """Fetch baseline metrics from GSC"""
        service = build('searchconsole', 'v1', credentials=self.creds)
        # Fetch top queries, pages, metrics
        pass

    async def get_analytics_data(self, property_id: str) -> dict:
        """Fetch baseline metrics from GA"""
        # Fetch organic traffic, top pages
        pass
```

**OAuth flow:**
1. User clicks "Connect Google Account"
2. Redirect to Google OAuth consent screen
3. Receive authorization code
4. Exchange for access token + refresh token
5. Store encrypted tokens in database
6. Auto-refresh when expired

#### Priority 10: Google Docs Export
**Update:** `backend/integrations/google_client.py`

```python
async def export_to_google_docs(self, content: dict, options: dict) -> str:
    """Create Google Doc and return URL"""
    service = build('docs', 'v1', credentials=self.creds)

    # Create document
    doc = service.documents().create(body={'title': options['doc_name']}).execute()
    doc_id = doc['documentId']

    # Format content (convert HTML to Google Docs format)
    requests = self._build_doc_requests(content, options)

    # Batch update
    service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()

    return f"https://docs.google.com/document/d/{doc_id}"
```

### Week 11-12: Polish & Testing

#### Priority 11: Error Handling & Validation
- Comprehensive error messages
- Request validation
- API retry logic
- Graceful degradation

#### Priority 12: Testing
- Unit tests (pytest for backend, vitest for frontend)
- Integration tests (API endpoints)
- E2E tests (Playwright)
- Manual QA checklist

#### Priority 13: Documentation
- API documentation (auto-generated)
- User guide
- Developer guide
- Deployment guide

---

## API Integration Guide

### DataForSEO Setup

1. **Get credentials:**
   - Sign up at https://dataforseo.com/
   - Get login + password from dashboard

2. **Configure:**
```bash
# .env
DATAFORSEO_LOGIN=your-email@example.com
DATAFORSEO_PASSWORD=your-api-password
```

3. **Test connection:**
```bash
curl -u "login:password" https://api.dataforseo.com/v3/dataforseo_labs/google/keyword_suggestions/live
```

### Claude API Setup

1. **Get API key:**
   - Sign up at https://console.anthropic.com/
   - Create new API key

2. **Configure:**
```bash
# .env
ANTHROPIC_API_KEY=sk-ant-api03-...
```

3. **Test:**
```python
import anthropic
client = anthropic.Anthropic(api_key="sk-ant-...")
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(message.content)
```

### Google APIs Setup

1. **Create Google Cloud Project:**
   - Go to https://console.cloud.google.com/
   - Create new project
   - Enable APIs:
     - Google Search Console API
     - Google Analytics API
     - Google Docs API
     - Google Drive API

2. **Create OAuth 2.0 Credentials:**
   - Go to Credentials → Create Credentials → OAuth 2.0 Client ID
   - Application type: Web application
   - Authorized redirect URIs: `http://localhost:8000/api/auth/google/callback`
   - Download client_secret.json

3. **Configure:**
```bash
# .env
GOOGLE_CLIENT_ID=123456789-abc.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-...
```

---

## Testing Strategy

### Backend Tests
```bash
cd backend
pytest tests/ -v --cov=. --cov-report=html
```

**Test structure:**
```
backend/tests/
├── test_auth.py          # Auth endpoints
├── test_projects.py      # Project CRUD
├── test_keywords.py      # Keyword research
├── test_content.py       # Content generation
├── test_quality.py       # Quality checks
└── conftest.py          # Fixtures
```

### Frontend Tests
```bash
cd frontend
npm test
```

### E2E Tests
```bash
npx playwright test
```

**Test scenarios:**
1. User registration → login → create project
2. Keyword research → SERP analysis → brief generation
3. Content generation → editing → quality check → export

---

## Deployment Guide

### Production Checklist

- [ ] Change `JWT_SECRET` to secure random string
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up SSL/TLS certificates
- [ ] Configure proper CORS origins
- [ ] Set up error tracking (Sentry)
- [ ] Set up logging (CloudWatch, Datadog)
- [ ] Configure database backups
- [ ] Set up CI/CD pipeline
- [ ] Load test API endpoints
- [ ] Security audit

### Environment Variables (Production)
```bash
# Database
DATABASE_URL=postgresql://user:password@host:5432/leadgear

# Redis
REDIS_URL=redis://redis-host:6379

# Security
JWT_SECRET=<generate-with-openssl-rand-hex-32>

# APIs (same as development)
ANTHROPIC_API_KEY=...
DATAFORSEO_LOGIN=...
# etc.
```

### Deployment Options

**Option 1: DigitalOcean App Platform**
- Easiest deployment
- Auto-scaling
- Managed database and Redis
- ~$50/month for small deployment

**Option 2: AWS (Docker + ECS)**
- More control
- Auto-scaling with ECS
- RDS for PostgreSQL, ElastiCache for Redis
- ~$100-200/month

**Option 3: Self-hosted (VPS)**
- Full control
- Cheapest (~$20-40/month)
- Requires manual management
- Use Docker Compose

---

## Troubleshooting

### Common Issues

**1. Database errors:**
```bash
# Reset database
rm backend/leadgear.db
# Restart backend to recreate tables
```

**2. Frontend can't connect to backend:**
```bash
# Check VITE_API_URL in .env
# Ensure backend is running on port 8000
```

**3. Celery tasks not running:**
```bash
# Check Redis is running
docker ps | grep redis

# Check Celery worker logs
docker-compose logs celery
```

**4. Permission errors:**
```bash
# Fix Docker volume permissions
sudo chown -R $USER:$USER .
```

---

## Support & Contributions

For questions, issues, or contributions:
1. Check existing issues in GitHub
2. Create new issue with detailed description
3. Follow code style guidelines (ESLint, Black)
4. Write tests for new features
5. Update documentation

---

**Happy Coding! 🚀**
