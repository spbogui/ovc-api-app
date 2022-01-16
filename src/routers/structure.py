from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import structure as r
from ..schemas.structure import Structure

structure = APIRouter(
    prefix='/structure',
    tags=['Structure'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@structure.get('', status_code=status.HTTP_200_OK, response_model=List[Structure])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return r.get_structures(db, limit)


@structure.get('/{structure_id}', status_code=status.HTTP_200_OK, response_model=Structure)
def get_one(structure_id: int, db: Session = Depends(get_db)):
    return r.get_one_structure(structure_id, db)


@structure.get('/{platform_id}/platform', status_code=status.HTTP_200_OK, response_model=List[Structure])
def get_all_platform_structures(platform_id: int, db: Session = Depends(get_db)):
    return r.get_all_platform_structures(platform_id, db)


# @structure.delete('/{structure_id}', status_code=status.HTTP_201_CREATED)
# def remove(structure_id: int, db: Session = Depends(get_db)):
#     return r.remove_structure(structure_id, db)
