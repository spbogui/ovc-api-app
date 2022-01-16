from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src.models.school_followup import SchoolFollowup, SchoolFollowupInfo


def get_school_followup_by_id(school_followup_id: int, db: Session):
    school_followup = db.query(SchoolFollowup).filter(SchoolFollowup.id == school_followup_id)
    if not school_followup:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Object with ID {school_followup_id} is not available")
    return school_followup.first()


# def get_school_followup_by_beneficiary(beneficiary_code: str, household_code: str, db: Session):
#     return db.query(SchoolFollowup).filter(
#         SchoolFollowup.beneficiary_code == beneficiary_code and SchoolFollowup.household_code == household_code
#     ).all()


def get_school_followup_info_by_followup_id(school_followup_id: int, db: Session):
    return db.query(SchoolFollowupInfo).filter(SchoolFollowupInfo.school_followup_id == school_followup_id).first()


def get_school_followup_by_beneficiary(beneficiary_code: str, household_code: str, db: Session):
    return db.query(SchoolFollowupInfo).filter(
        SchoolFollowupInfo.beneficiary_code == beneficiary_code and SchoolFollowupInfo.household_code == household_code
    ).all()


def get_all_by_structure(structure_id, db):
    return db.query(SchoolFollowupInfo).filter(SchoolFollowupInfo.structure == structure_id).all()
