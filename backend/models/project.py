"""
Project model representing a client/project
"""

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from datetime import datetime
import uuid
from database import Base


class Project(Base):
    """Project/Client model"""

    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    # Basic Information
    name = Column(String, nullable=False)
    website_url = Column(String, nullable=False)
    industry = Column(String)

    # Business Details (JSON arrays)
    target_locations = Column(JSON, default=list)  # ["Dallas, TX", "Houston, TX"]
    main_services = Column(JSON, default=list)  # ["HVAC Repair", "Installation"]
    competitors = Column(JSON, default=list)  # ["https://competitor1.com", ...]
    business_goals = Column(Text)  # Long-form text

    # Google OAuth Tokens (for this specific project)
    # Note: In production, encrypt these
    google_search_console_token = Column(Text, nullable=True)
    google_analytics_token = Column(Text, nullable=True)

    # Baseline Metrics (fetched from Google APIs)
    baseline_organic_traffic = Column(Integer, default=0)
    baseline_keywords = Column(Integer, default=0)
    baseline_top_pages = Column(JSON, default=list)  # [{"url": "...", "clicks": 100}, ...]

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="projects")
    content_pieces = relationship("ContentPiece", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project {self.name}>"
