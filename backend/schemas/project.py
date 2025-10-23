"""
Project schemas
"""

from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict, Any
from datetime import datetime


class ProjectCreate(BaseModel):
    """Schema for creating a project"""
    name: str
    website_url: str
    industry: Optional[str] = None
    target_locations: List[str] = []
    main_services: List[str] = []
    competitors: List[str] = []
    business_goals: Optional[str] = None


class ProjectUpdate(BaseModel):
    """Schema for updating a project"""
    name: Optional[str] = None
    website_url: Optional[str] = None
    industry: Optional[str] = None
    target_locations: Optional[List[str]] = None
    main_services: Optional[List[str]] = None
    competitors: Optional[List[str]] = None
    business_goals: Optional[str] = None


class ProjectResponse(BaseModel):
    """Schema for project response"""
    id: str
    user_id: str
    name: str
    website_url: str
    industry: Optional[str] = None
    target_locations: List[str]
    main_services: List[str]
    competitors: List[str]
    business_goals: Optional[str] = None
    baseline_organic_traffic: int
    baseline_keywords: int
    baseline_top_pages: List[Dict[str, Any]]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProjectListResponse(BaseModel):
    """Schema for project list response"""
    id: str
    name: str
    website_url: str
    content_count: int = 0
    updated_at: datetime

    class Config:
        from_attributes = True


class BaselineMetricsResponse(BaseModel):
    """Schema for baseline metrics from Google Search Console/Analytics"""
    organic_traffic: int
    total_keywords: int
    top_pages: List[Dict[str, Any]]
    average_position: float
    total_clicks: int
