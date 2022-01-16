from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src.models.identification import HouseholdIdentification


def get_by_code(code: str, db: Session):
    identification = db.query(HouseholdIdentification).filter(HouseholdIdentification.household_code == code)

    if not identification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Member with code {code} is not available")
    return identification.first()


def get_all_by_structure(structure_id: int, db: Session):
    return db.query(HouseholdIdentification).filter(HouseholdIdentification.structure == structure_id).all()



