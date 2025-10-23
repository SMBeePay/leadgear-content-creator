# Lead Gear Content Creation Tool

An AI-powered web application that streamlines SEO content production from keyword research through content generation and Google Docs export.

## Features

- **Project Management**: Track clients, websites, and content pieces
- **Keyword Research**: Automated keyword discovery using DataForSEO
- **SERP Analysis**: Competitive analysis of top-ranking content
- **AI Content Briefs**: Auto-generated briefs following SOP-005 structure
- **AI Content Generation**: Human-quality content following SOP-006 guidelines
- **Quality Checks**: Built-in SEO, readability, and keyword density validation
- **AI Improvements**: Inline suggestions for content enhancement
- **Google Docs Export**: One-click export with formatting

## Technology Stack

**Frontend:**
- React 18+ with TypeScript
- Tailwind CSS + shadcn/ui
- TipTap rich text editor
- Zustand state management

**Backend:**
- Python FastAPI
- SQLAlchemy ORM
- SQLite (MVP) / PostgreSQL (production)
- Celery + Redis for async tasks

**APIs:**
- Anthropic Claude 3.5 Sonnet
- Perplexity AI
- DataForSEO
- Google Search Console, Analytics, Docs

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Environment Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd leadgear-content-creator
```

2. Copy the environment template:
```bash
cp .env.example .env
```

3. Edit `.env` and add your API keys:
   - Get Anthropic API key from https://console.anthropic.com/
   - Get DataForSEO credentials from https://dataforseo.com/
   - Get Perplexity API key from https://www.perplexity.ai/
   - Set up Google OAuth credentials in Google Cloud Console

### Running with Docker

```bash
# Start all services
docker-compose up

# Frontend will be available at http://localhost:3000
# Backend API at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### Local Development (without Docker)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Redis (required for Celery):**
```bash
# Install and start Redis locally, or use Docker:
docker run -d -p 6379:6379 redis:7-alpine
```

**Celery Worker:**
```bash
cd backend
celery -A tasks.celery_app worker --loglevel=info
```

## Project Structure

```
leadgear-content-creator/
├── docker-compose.yml
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API clients
│   │   ├── stores/         # Zustand stores
│   │   ├── types/          # TypeScript types
│   │   └── utils/          # Utility functions
│   ├── package.json
│   └── Dockerfile
├── backend/
│   ├── models/             # SQLAlchemy models
│   ├── routes/             # FastAPI routes
│   ├── services/           # Business logic
│   ├── integrations/       # External API clients
│   ├── tasks/              # Celery tasks
│   ├── utils/              # Utilities
│   ├── main.py            # FastAPI app
│   ├── requirements.txt
│   └── Dockerfile
└── README.md
```

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development Workflow

1. **Create a Project**: Add client information and connect Google accounts
2. **Keyword Research**: Enter seed keywords and select targets
3. **SERP Analysis**: Review competitor analysis
4. **Generate Brief**: AI creates comprehensive content brief
5. **Generate Content**: AI writes full draft
6. **Edit & Refine**: Use inline editor and AI improvements
7. **Quality Check**: Review SEO and readability scores
8. **Export**: Push to Google Docs

## Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Deployment

See deployment documentation in `/docs/deployment.md` (coming soon)

## Contributing

This is an internal tool for Lead Gear SEO team. Contact the project owner for contribution guidelines.

## License

Proprietary - Lead Gear SEO Team

## Support

For issues or questions, contact the development team.
