"""
Content brief routes
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.content_piece import ContentPiece
from schemas.brief import BriefGenerateRequest, BriefResponse, BriefUpdateRequest
from utils.auth import get_current_user

router = APIRouter()


@router.post("/generate")
async def generate_brief(
    request: BriefGenerateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate content brief using Claude AI"""

    # TODO: Implement Claude API integration for brief generation
    # For now, return placeholder data
    return {
        "id": request.content_piece_id,
        "content_piece_id": request.content_piece_id,
        "brief": {
            "project_information": "Project details...",
            "target_keywords": f"Primary: {request.primary_keyword}",
            "content_goal": "Generate leads...",
            "target_audience": "Homeowners...",
            "serp_analysis": "Analysis...",
            "content_outline": "Outline...",
            "required_elements": "Elements...",
            "writing_guidelines": "Guidelines...",
            "seo_checklist": "Checklist...",
            "success_metrics": "Metrics..."
        },
        "approved": False
    }


@router.get("/{brief_id}")
async def get_brief(
    brief_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get content brief by ID"""

    content_piece = db.query(ContentPiece).filter(ContentPiece.id == brief_id).first()

    if not content_piece:
        raise HTTPException(status_code=404, detail="Brief not found")

    return {
        "id": content_piece.id,
        "content_piece_id": content_piece.id,
        "brief": content_piece.brief,
        "approved": content_piece.brief_approved
    }


@router.patch("/{brief_id}")
async def update_brief(
    brief_id: str,
    request: BriefUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update content brief sections"""

    content_piece = db.query(ContentPiece).filter(ContentPiece.id == brief_id).first()

    if not content_piece:
        raise HTTPException(status_code=404, detail="Brief not found")

    content_piece.brief = request.brief
    db.commit()
    db.refresh(content_piece)

    return {
        "id": content_piece.id,
        "content_piece_id": content_piece.id,
        "brief": content_piece.brief,
        "approved": content_piece.brief_approved
    }


@router.post("/{brief_id}/approve")
async def approve_brief(
    brief_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Mark brief as approved"""

    content_piece = db.query(ContentPiece).filter(ContentPiece.id == brief_id).first()

    if not content_piece:
        raise HTTPException(status_code=404, detail="Brief not found")

    content_piece.brief_approved = True
    db.commit()

    return {"message": "Brief approved", "id": brief_id}
