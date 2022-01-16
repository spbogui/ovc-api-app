from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import support_activity as a
from ..schemas.support_activity import SupportActivity, SupportActivityRequest

activity = APIRouter(
    prefix='/support-activity',
    tags=['Member Support Activity'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@activity.get('', status_code=status.HTTP_200_OK, response_model=List[SupportActivity])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return a.get_all(db, limit)


@activity.get('/{activity_id}', status_code=status.HTTP_200_OK, response_model=SupportActivity)
def get_one(activity_id: int, db: Session = Depends(get_db)):
    return a.get_one_activity(activity_id, db)


@activity.get('/household/{code}', status_code=status.HTTP_200_OK, response_model=List[SupportActivity])
def get_all_by_household(code: str, db: Session = Depends(get_db)):
    return a.get_all_by_household(code, db)


@activity.get('/{structure_id}/structure', status_code=status.HTTP_200_OK, response_model=List[SupportActivity])
def get_all_by_structure(structure_id: int, db: Session = Depends(get_db)):
    return a.get_all_by_structure(structure_id, db)


# @activity.put('', status_code=status.HTTP_202_ACCEPTED)
# def update(activity_id: int, request: SupportActivityRequest, db: Session = Depends(get_db)):
#     return a.update_activity(activity_id, request, db)
#
#
# @activity.delete('/{activity_id}', status_code=status.HTTP_201_CREATED)
# def remove(activity_id: int, db: Session = Depends(get_db)):
#     return a.remove_activity(activity_id, db)
