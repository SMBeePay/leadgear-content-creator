"""
Lead Gear Content Creation Tool - FastAPI Backend
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routes
from routes import projects, keywords, serp, briefs, content, meta, export_routes, auth

# Import database
from database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events"""
    # Startup
    print("🚀 Starting Lead Gear Content Creation Tool...")
    print(f"📊 Database: {os.getenv('DATABASE_URL', 'sqlite:///./leadgear.db')}")
    print(f"🔴 Redis: {os.getenv('REDIS_URL', 'redis://localhost:6379')}")

    yield

    # Shutdown
    print("👋 Shutting down...")


# Initialize FastAPI app
app = FastAPI(
    title="Lead Gear Content Creation Tool API",
    description="AI-powered SEO content creation platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configure CORS
# Allow both development and production origins
allowed_origins = [
    "http://localhost:3000",
    os.getenv("FRONTEND_URL", "http://localhost:3000"),
]

# Add Vercel preview and production URLs if configured
if os.getenv("VERCEL_URL"):
    allowed_origins.append(f"https://{os.getenv('VERCEL_URL')}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_origin_regex=r"https://.*\.vercel\.app",  # Allow all Vercel preview URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(keywords.router, prefix="/api/keywords", tags=["Keywords"])
app.include_router(serp.router, prefix="/api/serp", tags=["SERP Analysis"])
app.include_router(briefs.router, prefix="/api/briefs", tags=["Content Briefs"])
app.include_router(content.router, prefix="/api/content", tags=["Content"])
app.include_router(meta.router, prefix="/api/meta", tags=["Meta Tags"])
app.include_router(export_routes.router, prefix="/api/export", tags=["Export"])


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "name": "Lead Gear Content Creation Tool API",
        "version": "1.0.0",
        "status": "healthy",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",
        "redis": "connected",  # TODO: Add actual Redis check
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
