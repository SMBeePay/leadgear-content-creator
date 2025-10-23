"""
Content generation and management routes
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from models.content_piece import ContentPiece
from schemas.content import (
    ContentPieceCreate,
    ContentPieceUpdate,
    ContentPieceResponse,
    ContentImproveRequest,
    ContentValidationResponse
)
from utils.auth import get_current_user

router = APIRouter()


@router.post("/generate")
async def generate_content(
    brief_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate content draft using Claude AI"""

    # TODO: Implement Claude API integration for content generation
    # For now, return placeholder
    return {
        "message": "Content generation not implemented yet",
        "brief_id": brief_id
    }


@router.get("/{content_id}", response_model=ContentPieceResponse)
async def get_content(
    content_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get content piece by ID"""

    content = db.query(ContentPiece).filter(ContentPiece.id == content_id).first()

    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    return content


@router.patch("/{content_id}", response_model=ContentPieceResponse)
async def update_content(
    content_id: str,
    updates: ContentPieceUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update content piece"""

    content = db.query(ContentPiece).filter(ContentPiece.id == content_id).first()

    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    # Update fields
    update_data = updates.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(content, field, value)

    db.commit()
    db.refresh(content)

    return content


@router.post("/{content_id}/improve")
async def improve_content(
    content_id: str,
    request: ContentImproveRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get AI improvement suggestions for selected text"""

    # TODO: Implement Claude API integration for improvements
    return {
        "suggestions": [
            {
                "type": request.improvement_type,
                "original": request.selected_text,
                "improved": f"Improved version of: {request.selected_text}"
            }
        ]
    }


@router.post("/{content_id}/validate", response_model=ContentValidationResponse)
async def validate_content(
    content_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Run quality checks on content"""

    content = db.query(ContentPiece).filter(ContentPiece.id == content_id).first()

    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    # TODO: Implement quality checks
    return {
        "readability_score": 68.0,
        "seo_score": 87.0,
        "keyword_density": 1.2,
        "issues": [],
        "suggestions": []
    }
