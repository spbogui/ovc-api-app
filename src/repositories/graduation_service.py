from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.graduation_service import GraduationService
from ..schemas.graduation_service import GraduationServiceRequest


def get_graduation_services(db: Session, limit: int = 100):
    return db.query(GraduationService).limit(limit).all()


def get_one_graduation_service(graduation_presta_id: int, db: Session):
    graduation_presta = db.query(GraduationService).filter(GraduationService.id == graduation_presta_id).first()

    if not graduation_presta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The graduation_presta with id {graduation_presta_id} is not available.")
    return graduation_presta


def update_graduation_service(graduation_presta_id, request: GraduationServiceRequest, db: Session):
    graduation_presta = db.query(GraduationService).filter(GraduationService.id == graduation_presta_id)
    if not graduation_presta.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The graduation_presta with id {graduation_presta_id} is not available.")
    graduation_presta.update(request)
    db.commit()
    return {"result": "updated"}


def remove_graduation_service(graduation_presta_id: int, db: Session):
    graduation_presta = db.query(GraduationService).filter(GraduationService.id == graduation_presta_id)
    if not graduation_presta.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The graduation_presta with id {graduation_presta_id} is not available.")
    graduation_presta.delete(synchronize_session=False)
    db.commit()
    return {'result': True}
