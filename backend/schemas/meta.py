"""
Meta tags and image suggestion schemas
"""

from pydantic import BaseModel
from typing import List, Dict, Any


class MetaTagsGenerateRequest(BaseModel):
    """Request schema for generating meta tags"""
    content: str
    primary_keyword: str
    client_name: Optional[str] = None


class MetaTagsResponse(BaseModel):
    """Response schema for meta tags"""
    title_tag: str
    meta_description: str
    url_slug: str


class ImageSuggestion(BaseModel):
    """Individual image suggestion"""
    type: str  # "hero", "screenshot", "diagram", "infographic", "product"
    description: str
    alt_text: str
    position: int  # Where in content to place


class ImageSuggestionsResponse(BaseModel):
    """Response schema for image suggestions"""
    suggestions: List[ImageSuggestion]


from typing import Optional
