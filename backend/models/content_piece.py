"""
ContentPiece model representing a single piece of content
"""

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from datetime import datetime
import uuid
from database import Base


class ContentPiece(Base):
    """Content piece model for blog posts/articles"""

    __tablename__ = "content_pieces"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = Column(String, ForeignKey("projects.id"), nullable=False)

    # Keywords
    primary_keyword = Column(String, nullable=False)
    secondary_keywords = Column(JSON, default=list)  # ["keyword1", "keyword2"]
    keyword_data = Column(JSON, default=dict)  # {volume: 1200, difficulty: 35, ...}

    # Content Brief (all 10 sections from SOP-005)
    brief = Column(JSON, default=dict)  # {section1: "...", section2: "...", ...}
    brief_approved = Column(Boolean, default=False)

    # SERP Analysis
    serp_analysis = Column(JSON, default=dict)  # Top 10 results, competitor data

    # Content
    content_html = Column(Text)  # HTML version for rich text editor
    content_markdown = Column(Text)  # Markdown version for export
    word_count = Column(Integer, default=0)
    target_word_count = Column(Integer, default=2200)

    # Meta Tags
    title_tag = Column(String)  # 50-60 chars
    meta_description = Column(String)  # 140-155 chars
    url_slug = Column(String)

    # Quality Scores
    readability_score = Column(Float, default=0.0)  # Flesch Reading Ease
    seo_score = Column(Float, default=0.0)  # Composite SEO score
    keyword_density = Column(Float, default=0.0)  # Primary keyword density %

    # Image Suggestions
    image_suggestions = Column(JSON, default=list)  # [{"type": "hero", "description": "...", "alt": "..."}, ...]

    # Status
    status = Column(String, default="draft")  # draft, review, approved, exported

    # Export
    google_doc_url = Column(String, nullable=True)
    exported_at = Column(DateTime, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    project = relationship("Project", back_populates="content_pieces")
    keyword_research = relationship("KeywordResearch", back_populates="content_piece", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<ContentPiece {self.primary_keyword}>"
