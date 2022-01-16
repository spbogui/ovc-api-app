from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src.models.nutritional_followup import NutritionalFollowupInfo


def get_by_followup_id(followup_id: int, db: Session):
    followup = db.query(NutritionalFollowupInfo).filter(NutritionalFollowupInfo.followup_id == followup_id)

    if not followup:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Object with ID {followup_id} is not available")
    return followup.first()


def get_all_by_beneficiary(beneficiary_code, household_code, db: Session):
    return db.query(NutritionalFollowupInfo).filter(
        NutritionalFollowupInfo.beneficiary_code == beneficiary_code and
        NutritionalFollowupInfo.household_code == household_code
    ).all()


def get_all_by_structure(structure_id: int, db: Session):
    return db.query(NutritionalFollowupInfo).filter(
        NutritionalFollowupInfo.structure == structure_id
    ).all()
