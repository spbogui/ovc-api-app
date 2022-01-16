from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.social_center import SocialCenter


def get_social_centers(db: Session, limit: int = 100):
    return db.query(SocialCenter).limit(limit).all()


def get_one_social_center(code: str, db: Session):
    social_center = db.query(SocialCenter).filter(SocialCenter.cs_code == code).first()

    if not social_center:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The social_center with id {code} is not available.")
    return social_center
