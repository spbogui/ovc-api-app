from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.config.database import get_db
from ..repositories import nutritional_followup as nf
from ..schemas.nutritional_followup import NutritionalFollowupInfo

nutritional_followup = APIRouter(
    prefix='/nutritional-followup',
    tags=['Member Nutritional Followup'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@nutritional_followup.get('/{followup_id}', status_code=status.HTTP_200_OK, response_model=NutritionalFollowupInfo)
def get_by_id(followup_id: int, db: Session = Depends(get_db)):
    return nf.get_by_followup_id(followup_id, db)


@nutritional_followup.get('/{beneficiary_code}/{household_code}',
                          status_code=status.HTTP_200_OK,
                          response_model=List[NutritionalFollowupInfo])
def get_by_beneficiary(beneficiary_code: str, household_code, db: Session = Depends(get_db)):
    return nf.get_all_by_beneficiary(beneficiary_code, household_code, db)


@nutritional_followup.get('/{structure_id}/structure',
                          status_code=status.HTTP_200_OK,
                          response_model=List[NutritionalFollowupInfo])
def get_all_by_structure(structure_id: int, db: Session = Depends(get_db)):
    return nf.get_all_by_structure(structure_id, db)
