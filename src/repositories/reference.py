from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.reference import Reference


def get_references(db: Session, limit: int = 100):
    return db.query(Reference).limit(limit).all()


def get_one_reference(reference_id: int, db: Session):
    reference = db.query(Reference).filter(Reference.id == reference_id).first()

    if not reference:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The reference with id {reference_id} is not available.")
    return reference


# def update_reference(reference_id, request: ReferenceRequest, db: Session):
#     reference = db.query(Reference).filter(Reference.id == reference_id)
#     if not reference.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The reference with id {reference_id} is not available.")
#     reference.update(request)
#     db.commit()
#     return {"result": "updated"}
#
#
# def remove_reference(reference_id: int, db: Session):
#     reference = db.query(Reference).filter(Reference.id == reference_id)
#     if not reference.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The reference with id {reference_id} is not available.")
#     reference.delete(synchronize_session=False)
#     db.commit()
#     return {'result': True}


def get_all_by_structure(structure_id: int, db: Session):
    return db.query(Reference).filter(Reference.structure == structure_id).all()
