"""
KeywordResearch model for storing keyword and SERP data
"""

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from datetime import datetime
import uuid
from database import Base


class KeywordResearch(Base):
    """Keyword research and SERP analysis data"""

    __tablename__ = "keyword_research"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content_piece_id = Column(String, ForeignKey("content_pieces.id"), nullable=False, unique=True)

    # Keywords with metrics
    # Format: [{"keyword": "...", "volume": 1200, "difficulty": 35, "cpc": 2.5, "trend": [...]}, ...]
    keywords = Column(JSON, default=list)

    # SERP Results
    # Format: [{"rank": 1, "url": "...", "title": "...", "word_count": 2450, "headers": [...]}, ...]
    serp_results = Column(JSON, default=list)

    # Content gaps identified
    # Format: ["Cost comparison", "Seasonal tips", ...]
    content_gaps = Column(JSON, default=list)

    # Related questions (from Perplexity + PAA)
    related_questions = Column(JSON, default=list)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    content_piece = relationship("ContentPiece", back_populates="keyword_research")

    def __repr__(self):
        return f"<KeywordResearch for ContentPiece {self.content_piece_id}>"
