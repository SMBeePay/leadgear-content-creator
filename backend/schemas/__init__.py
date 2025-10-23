"""
Pydantic schemas for API request/response validation
"""

from schemas.user import UserCreate, UserLogin, UserResponse, Token
from schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse, ProjectListResponse
from schemas.content import (
    ContentPieceCreate,
    ContentPieceUpdate,
    ContentPieceResponse,
    ContentImproveRequest,
    ContentValidationResponse
)
from schemas.keyword import KeywordResearchRequest, KeywordResearchResponse, KeywordData
from schemas.serp import SERPAnalysisRequest, SERPAnalysisResponse
from schemas.brief import BriefGenerateRequest, BriefResponse, BriefUpdateRequest
from schemas.meta import MetaTagsGenerateRequest, MetaTagsResponse, ImageSuggestionsResponse
from schemas.export_schema import ExportGoogleDocsRequest, ExportGoogleDocsResponse

__all__ = [
    "UserCreate", "UserLogin", "UserResponse", "Token",
    "ProjectCreate", "ProjectUpdate", "ProjectResponse", "ProjectListResponse",
    "ContentPieceCreate", "ContentPieceUpdate", "ContentPieceResponse",
    "ContentImproveRequest", "ContentValidationResponse",
    "KeywordResearchRequest", "KeywordResearchResponse", "KeywordData",
    "SERPAnalysisRequest", "SERPAnalysisResponse",
    "BriefGenerateRequest", "BriefResponse", "BriefUpdateRequest",
    "MetaTagsGenerateRequest", "MetaTagsResponse", "ImageSuggestionsResponse",
    "ExportGoogleDocsRequest", "ExportGoogleDocsResponse"
]
