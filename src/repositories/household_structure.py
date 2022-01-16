from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.household_structure import HouseholdStructure
# from ..schemas.household_structure import HouseholdStructureRequest


def get_household_structures(db: Session, limit: int = 100):
    return db.query(HouseholdStructure).limit(limit).all()


def get_all_structure_household(structure_id: int, db: Session):
    household_structures = db.query(HouseholdStructure).filter(HouseholdStructure.structure == structure_id).limit(100)
    # print(" structure id", structure_id)
    # print("structure count", household_structures.all())
    if not household_structures:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The households with id {structure_id} is not available.")
    return household_structures.all()


def get_one_household_structure(household_structure_id: int, db: Session):
    household_structure = db.query(HouseholdStructure).filter(HouseholdStructure.id == household_structure_id).first()

    if not household_structure:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The household_structure with id {household_structure_id} is not available.")
    return household_structure
#
# def update_household_structure(household_structure_id, request: HouseholdStructureRequest, db: Session):
#     household_structure = db.query(HouseholdStructure).filter(HouseholdStructure.id == household_structure_id)
#     if not household_structure.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The household_structure with id {household_structure_id} is not available.")
#     household_structure.update(request)
#     db.commit()
#     return {"result": "updated"}
#
#
# def remove_household_structure(household_structure_id: int, db: Session):
#     household_structure = db.query(HouseholdStructure).filter(HouseholdStructure.id == household_structure_id)
#     if not household_structure.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The household_structure with id {household_structure_id} is not available.")
#     household_structure.delete(synchronize_session=False)
#     db.commit()
#     return {'result': True}
