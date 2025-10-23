"""
Export routes
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.content_piece import ContentPiece
from schemas.export_schema import ExportGoogleDocsRequest, ExportGoogleDocsResponse
from utils.auth import get_current_user

router = APIRouter()


@router.post("/google-docs", response_model=ExportGoogleDocsResponse)
async def export_to_google_docs(
    request: ExportGoogleDocsRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Export content to Google Docs"""

    content = db.query(ContentPiece).filter(ContentPiece.id == request.content_id).first()

    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    # TODO: Implement Google Docs API integration
    # For now, return placeholder
    return {
        "doc_url": "https://docs.google.com/document/d/placeholder",
        "doc_id": "placeholder-doc-id",
        "success": False,
        "message": "Google Docs export not implemented yet"
    }
