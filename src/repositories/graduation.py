from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.graduation import Graduation
from ..schemas.graduation import GraduationRequest


def get_graduations(db: Session, limit: int = 100):
    return db.query(Graduation).limit(limit).all()


def get_one_graduation(graduation_id: int, db: Session):
    graduation = db.query(Graduation).filter(Graduation.id == graduation_id).first()

    if not graduation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The graduation with id {graduation_id} is not available.")
    return graduation


def update_graduation(graduation_id, request: GraduationRequest, db: Session):
    graduation = db.query(Graduation).filter(Graduation.id == graduation_id)
    if not graduation.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The graduation with id {graduation_id} is not available.")
    graduation.update(request)
    db.commit()
    return {"result": "updated"}


def remove_graduation(graduation_id: int, db: Session):
    graduation = db.query(Graduation).filter(Graduation.id == graduation_id)
    if not graduation.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The graduation with id {graduation_id} is not available.")
    graduation.delete(synchronize_session=False)
    db.commit()
    return {'result': True}


def get_all_by_structure(structure_id: int, db: Session):
    graduations = db.query(Graduation).filter(Graduation.structure == structure_id)

    if not graduations:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The graduation with id {structure_id} is not available.")
    return graduations.all()
