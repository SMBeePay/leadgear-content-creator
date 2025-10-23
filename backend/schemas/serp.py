"""
SERP analysis schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class SERPAnalysisRequest(BaseModel):
    """Request schema for SERP analysis"""
    keyword: str
    location: Optional[str] = "United States"
    num_results: int = 10
    content_piece_id: str


class SERPResult(BaseModel):
    """Individual SERP result"""
    rank: int
    url: str
    title: str
    description: Optional[str] = None
    word_count: int = 0
    headers: List[str] = []
    domain_authority: Optional[int] = None


class SERPAnalysisResponse(BaseModel):
    """Response schema for SERP analysis"""
    keyword: str
    serp_results: List[SERPResult]
    content_gaps: List[str] = []
    related_questions: List[str] = []
    average_word_count: int
