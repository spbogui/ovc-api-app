from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import graduation_service as gp
from ..schemas.graduation_service import GraduationService, GraduationServiceRequest

graduation_service = APIRouter(
    prefix='/graduation_service',
    tags=['Graduation Service'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@graduation_service.get('', status_code=status.HTTP_200_OK, response_model=List[GraduationService])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return gp.get_graduation_services(db, limit)


@graduation_service.get('/{graduation_service_id}', status_code=status.HTTP_200_OK, response_model=GraduationService)
def get_one(graduation_service_id: int, db: Session = Depends(get_db)):
    return gp.get_one_graduation_service(graduation_service_id, db)


# @graduation_service.put('/{graduation_service_id}', status_code=status.HTTP_202_ACCEPTED)
# def update(graduation_service_id: int, request: GraduationServiceRequest, db: Session = Depends(get_db)):
#     return gp.update_graduation_service(graduation_service_id, request, db)
#
#
# @graduation_service.delete('/{graduation_service_id}', status_code=status.HTTP_201_CREATED)
# def remove(graduation_service_id: int, db: Session = Depends(get_db)):
#     return gp.remove_graduation_service(graduation_service_id, db)
