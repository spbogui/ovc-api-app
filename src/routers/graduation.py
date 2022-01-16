from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import graduation as g
from ..schemas.graduation import Graduation, GraduationRequest

graduation = APIRouter(
    prefix='/household-graduation',
    tags=['Household Graduation'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@graduation.get('', status_code=status.HTTP_200_OK, response_model=List[Graduation])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return g.get_graduations(db, limit)


@graduation.get('/{graduation_id}', status_code=status.HTTP_200_OK, response_model=Graduation)
def get_one(graduation_id: int, db: Session = Depends(get_db)):
    return g.get_one_graduation(graduation_id, db)


@graduation.get('/{structure_id}/structure', status_code=status.HTTP_200_OK, response_model=List[Graduation])
def get_all_graduation_by_structure(structure_id: int, db: Session = Depends(get_db)):
    return g.get_all_by_structure(structure_id, db)


# @graduation.put('', status_code=status.HTTP_202_ACCEPTED)
# def update(graduation_id: int, request: GraduationRequest, db: Session = Depends(get_db)):
#     return g.update_graduation(graduation_id, request, db)
#
#
# @graduation.delete('/{graduation_id}', status_code=status.HTTP_201_CREATED)
# def remove(graduation_id: int, db: Session = Depends(get_db)):
#     return g.remove_graduation(graduation_id, db)
