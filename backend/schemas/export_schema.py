"""
Export schemas
"""

from pydantic import BaseModel
from typing import Optional


class ExportOptions(BaseModel):
    """Options for Google Docs export"""
    include_meta: bool = True
    include_checklist: bool = True
    include_images: bool = True
    doc_name: Optional[str] = None


class ExportGoogleDocsRequest(BaseModel):
    """Request schema for exporting to Google Docs"""
    content_id: str
    options: ExportOptions


class ExportGoogleDocsResponse(BaseModel):
    """Response schema for Google Docs export"""
    doc_url: str
    doc_id: str
    success: bool
    message: str
