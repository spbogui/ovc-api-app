from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.config.database import get_db
from ..helpers.oauth2 import get_current_user
from ..models.user import User
from ..repositories import school_followup as sf
from ..schemas.school_followup import SchoolFollowup, SchoolFollowupInfo

school_followup = APIRouter(
    prefix='/school-followup',
    tags=['Member School Followup'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@school_followup.get('/{school_followup_id}', status_code=status.HTTP_200_OK, response_model=SchoolFollowupInfo)
def get_by_id(school_followup_id: int, db: Session = Depends(get_db),
              # current_user: User = Depends(get_current_user)
              ):
    return sf.get_school_followup_info_by_followup_id(school_followup_id, db)


@school_followup.get('/{beneficiary_code}/{household_code}', status_code=status.HTTP_200_OK,
                     response_model=List[SchoolFollowupInfo])
def get_by_beneficiary(beneficiary_code: str, household_code, db: Session = Depends(get_db),
                       # current_user: User = Depends(get_current_user)
                       ):
    return sf.get_school_followup_by_beneficiary(beneficiary_code, household_code, db)


@school_followup.get('/{structure_id}/structure', status_code=status.HTTP_200_OK,
                     response_model=List[SchoolFollowupInfo])
def get_all_by_structure(structure_id: int, db: Session = Depends(get_db)):
    return sf.get_all_by_structure(structure_id, db)

#
# @router.get('/{school_followup_id}', status_code=status.HTTP_200_OK, response_model=SchoolFollowupInfo)
# def get_by_school_followup_id(school_followup_id: int, db: Session = Depends(get_db),
#                               # current_user: User = Depends(get_current_user)
#                               ):
#     return sf.get_school_followup_info_by_followup_id(db, school_followup_id)
#
#
# @router.get('/{beneficiary_code}/{household_code}', status_code=status.HTTP_200_OK,
#             response_model=List[SchoolFollowupInfo])
# def get_by_beneficiary(beneficiary_code: str, household_code, db: Session = Depends(get_db),
#                        # current_user: User = Depends(get_current_user)
#                        ):
#     return sf.get_school_followup_by_beneficiary(db, beneficiary_code, household_code)
