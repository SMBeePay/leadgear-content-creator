"""
Content brief schemas
"""

from pydantic import BaseModel
from typing import Dict, Any, Optional


class BriefGenerateRequest(BaseModel):
    """Request schema for generating content brief"""
    project_id: str
    primary_keyword: str
    secondary_keywords: List[str]
    content_piece_id: str


class BriefResponse(BaseModel):
    """Response schema for content brief"""
    id: str
    content_piece_id: str
    brief: Dict[str, Any]  # All 10 sections
    approved: bool

    class Config:
        from_attributes = True


class BriefUpdateRequest(BaseModel):
    """Request schema for updating brief sections"""
    brief: Dict[str, Any]


from typing import List
