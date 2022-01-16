from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.config.database import get_db
from ..repositories import member_identification as i
from ..schemas.identification import Member

member = APIRouter(
    prefix='/member',
    tags=['Member'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@member.get('/{code}', status_code=status.HTTP_200_OK, response_model=Member)
def get_by_id(code: str, db: Session = Depends(get_db)):
    return i.get_by_code(code, db)


@member.get('/{structure}/structure',
            status_code=status.HTTP_200_OK,
            response_model=List[Member])
def get_by_structure(structure: int, db: Session = Depends(get_db)):
    return i.get_all_by_structure(structure, db)
