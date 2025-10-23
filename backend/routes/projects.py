"""
Project management routes
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.user import User
from models.project import Project
from models.content_piece import ContentPiece
from schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse, ProjectListResponse
from utils.auth import get_current_user

router = APIRouter()


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    project_data: ProjectCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new project"""

    new_project = Project(
        user_id=current_user.id,
        name=project_data.name,
        website_url=project_data.website_url,
        industry=project_data.industry,
        target_locations=project_data.target_locations,
        main_services=project_data.main_services,
        competitors=project_data.competitors,
        business_goals=project_data.business_goals
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("", response_model=List[ProjectListResponse])
async def list_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all projects for current user"""

    projects = db.query(Project).filter(Project.user_id == current_user.id).all()

    # Add content count for each project
    result = []
    for project in projects:
        content_count = db.query(ContentPiece).filter(ContentPiece.project_id == project.id).count()
        result.append(
            ProjectListResponse(
                id=project.id,
                name=project.name,
                website_url=project.website_url,
                content_count=content_count,
                updated_at=project.updated_at
            )
        )

    return result


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific project"""

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.patch("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: str,
    project_data: ProjectUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a project"""

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Update fields
    update_data = project_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(project, field, value)

    db.commit()
    db.refresh(project)

    return project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a project"""

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return None


@router.get("/{project_id}/baseline")
async def get_baseline_metrics(
    project_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Fetch baseline metrics from Google Search Console and Analytics"""

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # TODO: Implement Google Search Console and Analytics integration
    # For now, return placeholder data
    return {
        "organic_traffic": 0,
        "total_keywords": 0,
        "top_pages": [],
        "average_position": 0.0,
        "total_clicks": 0,
        "message": "Google API integration pending"
    }
