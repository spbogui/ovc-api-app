from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import reference as r
from ..schemas.reference import Reference

reference = APIRouter(
    prefix='/reference',
    tags=['Member Reference'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@reference.get('', status_code=status.HTTP_200_OK, response_model=List[Reference])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return r.get_references(db, limit)


@reference.get('/{reference_id}', status_code=status.HTTP_200_OK, response_model=Reference)
def get_one(reference_id: int, db: Session = Depends(get_db)):
    return r.get_one_reference(reference_id, db)


@reference.get('/{structure_id}/structure', status_code=status.HTTP_200_OK, response_model=List[Reference])
def get_all_by_structure(structure_id: int, db: Session = Depends(get_db)):
    return r.get_all_by_structure(structure_id, db)




#
# @reference.put('', status_code=status.HTTP_202_ACCEPTED)
# def update(reference_id: int, request: ReferenceRequest, db: Session = Depends(get_db)):
#     return r.update_reference(reference_id, request, db)
#
#
# @reference.delete('/{reference_id}', status_code=status.HTTP_201_CREATED)
# def remove(reference_id: int, db: Session = Depends(get_db)):
#     return r.remove_reference(reference_id, db)
