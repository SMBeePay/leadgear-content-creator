"""
Keyword research schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class KeywordData(BaseModel):
    """Individual keyword data"""
    keyword: str
    volume: int
    difficulty: int
    cpc: Optional[float] = None
    trend: Optional[List[int]] = None


class KeywordResearchRequest(BaseModel):
    """Request schema for keyword research"""
    seed_keywords: List[str]
    location: Optional[str] = "United States"
    language: str = "en"
    project_id: str


class KeywordResearchResponse(BaseModel):
    """Response schema for keyword research"""
    keywords: List[KeywordData]
    total_count: int
