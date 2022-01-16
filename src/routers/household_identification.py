from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.config.database import get_db
from ..repositories import household_identification as i
from ..schemas.identification import Household

household = APIRouter(
    prefix='/household',
    tags=['Household'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@household.get('/{code}', status_code=status.HTTP_200_OK, response_model=Household)
def get_by_id(code: str, db: Session = Depends(get_db)):
    return i.get_by_code(code, db)


@household.get('/{structure}/structure',
               status_code=status.HTTP_200_OK,
               response_model=List[Household])
def get_by_structure(structure: int, db: Session = Depends(get_db)):
    return i.get_all_by_structure(structure, db)
