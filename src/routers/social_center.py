from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import social_center as r
from ..schemas.social_center import SocialCenter

social_center = APIRouter(
    prefix='/social-center',
    tags=['Social Center'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@social_center.get('', status_code=status.HTTP_200_OK, response_model=List[SocialCenter])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return r.get_social_centers(db, limit)


@social_center.get('/{code}', status_code=status.HTTP_200_OK, response_model=SocialCenter)
def get_one(code: str, db: Session = Depends(get_db)):
    return r.get_one_social_center(code, db)
