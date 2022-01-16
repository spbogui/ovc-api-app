from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from ..models.structure import Structure
from ..models.identification import HouseholdIdentification


def get_structures(db: Session, limit: int = 100):
    return db.query(Structure).filter(Structure.id.in_(db.query(HouseholdIdentification.structure))).limit(limit).all()
    # return db.query(Structure).filter(Structure.id.in_(db.query(HouseholdStructure.structure))).limit(limit).all()


def get_one_structure(structure_id: int, db: Session):
    structure = db.query(Structure).filter(Structure.id == structure_id).first()

    if not structure:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The structure with id {structure_id} is not available.")
    return structure


def get_all_platform_structures(platform_id: int, db: Session):
    structure = db.query(Structure).filter(Structure.platform == platform_id)

    if not structure:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The structure with id {platform_id} is not available.")
    return structure.all()


# def update_structure(structure_id, request: StructureRequest, db: Session):
#     structure = db.query(Structure).filter(Structure.id == structure_id)
#     if not structure.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The structure with id {structure_id} is not available.")
#     structure.update(request)
#     db.commit()
#     return {"result": "updated"}
#
#
# def remove_structure(structure_id: int, db: Session):
#     structure = db.query(Structure).filter(Structure.id == structure_id)
#     if not structure.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The structure with id {structure_id} is not available.")
#     structure.delete(synchronize_session=False)
#     db.commit()
#     return {'result': True}
