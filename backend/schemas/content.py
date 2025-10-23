"""
Content schemas
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ContentPieceCreate(BaseModel):
    """Schema for creating content piece"""
    project_id: str
    primary_keyword: str
    secondary_keywords: List[str] = []


class ContentPieceUpdate(BaseModel):
    """Schema for updating content piece"""
    content_html: Optional[str] = None
    content_markdown: Optional[str] = None
    title_tag: Optional[str] = None
    meta_description: Optional[str] = None
    url_slug: Optional[str] = None
    status: Optional[str] = None


class ContentPieceResponse(BaseModel):
    """Schema for content piece response"""
    id: str
    project_id: str
    primary_keyword: str
    secondary_keywords: List[str]
    content_html: Optional[str] = None
    content_markdown: Optional[str] = None
    word_count: int
    target_word_count: int
    title_tag: Optional[str] = None
    meta_description: Optional[str] = None
    url_slug: Optional[str] = None
    readability_score: float
    seo_score: float
    keyword_density: float
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ContentImproveRequest(BaseModel):
    """Request schema for AI content improvement"""
    selected_text: str
    improvement_type: str  # "make_concise", "add_detail", "make_conversational", etc.
    context: Optional[str] = None


class ContentValidationResponse(BaseModel):
    """Response schema for content validation"""
    readability_score: float
    seo_score: float
    keyword_density: float
    issues: List[Dict[str, Any]]
    suggestions: List[str]
