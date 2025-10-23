# Quick Start Guide

## Get Running in 5 Minutes

### Step 1: Setup Environment
```bash
# Copy environment template
cp .env.example .env

# Edit .env and add a JWT secret (required for authentication)
# You can generate a secure secret with:
openssl rand -hex 32

# Add API keys (optional for now, but required for full functionality later):
# - ANTHROPIC_API_KEY (for Claude AI)
# - DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD (for keyword research)
# - PERPLEXITY_API_KEY (for research)
# - Google OAuth credentials (for Search Console, Analytics, Docs)
```

### Step 2: Start the Application
```bash
# Start all services with Docker
docker-compose up

# Wait for services to start (usually 30-60 seconds)
# You should see:
# ✅ Frontend ready at http://localhost:3000
# ✅ Backend ready at http://localhost:8000
# ✅ Redis connected
# ✅ Celery worker started
```

### Step 3: Create Your Account
1. Open http://localhost:3000 in your browser
2. Click "Register" and create an account
3. Login with your credentials

### Step 4: Explore!
- **Home Dashboard**: Overview and quick start guide
- **Projects**: Create your first client project
- **API Docs**: Visit http://localhost:8000/docs to explore the API

## What Works Right Now

✅ **Authentication**: Full user registration and login
✅ **Projects**: Create, edit, delete, and list client projects
✅ **API Infrastructure**: All endpoints scaffolded and documented
✅ **Database**: SQLite with all models ready
✅ **Task Queue**: Celery configured for async operations

## What's Coming Next

🔄 **Keyword Research**: DataForSEO integration (Week 3)
🔄 **SERP Analysis**: Web scraping and competitor analysis (Week 3)
🔄 **Content Briefs**: AI-generated briefs with Claude (Week 4)
🔄 **Content Generation**: Full draft generation (Week 4)
🔄 **Rich Text Editor**: TipTap integration (Week 5)
🔄 **Quality Checks**: SEO, readability, keyword density (Week 6)
🔄 **Google Integration**: OAuth, Search Console, Analytics, Docs (Week 9-10)

## Quick Test

### Test the Backend API:
```bash
# Register a new user
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "full_name": "Test User"
  }'

# Login (get token)
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'

# Copy the "access_token" from the response and use it:
export TOKEN="your-token-here"

# Create a project
curl -X POST http://localhost:8000/api/projects \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "name": "Test HVAC Company",
    "website_url": "https://example-hvac.com",
    "industry": "HVAC Services",
    "target_locations": ["Dallas, TX"],
    "main_services": ["HVAC Repair", "Installation"],
    "competitors": ["https://competitor1.com"],
    "business_goals": "Generate more leads for HVAC services"
  }'
```

## Need Help?

- **API Documentation**: http://localhost:8000/docs (interactive Swagger UI)
- **Implementation Guide**: See `IMPLEMENTATION_GUIDE.md` for detailed architecture and roadmap
- **README**: See `README.md` for full setup instructions

## Troubleshooting

**Can't access http://localhost:3000?**
```bash
# Check if containers are running
docker-compose ps

# View logs
docker-compose logs frontend
```

**Backend errors?**
```bash
# View backend logs
docker-compose logs backend

# Common fix: Restart containers
docker-compose down && docker-compose up
```

**Database issues?**
```bash
# Reset database (WARNING: Deletes all data)
docker-compose down
rm backend/leadgear.db
docker-compose up
```

## Development Tips

**Hot Reload**: Both frontend and backend support hot reload - just edit files and see changes!

**View Database**: Use a SQLite browser to inspect the database:
```bash
# Install sqlite3 or use a GUI tool like DB Browser for SQLite
sqlite3 backend/leadgear.db
```

**Check Redis**:
```bash
# Connect to Redis CLI
docker-compose exec redis redis-cli
> PING
PONG
```

**Monitor Celery Tasks**:
```bash
# View Celery worker logs in real-time
docker-compose logs -f celery
```

---

**Ready to build amazing content!** 🚀
