from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import member_evaluation as e
from ..schemas.member_evaluation import Evaluation, EvaluationRequest

evaluation = APIRouter(
    prefix='/member-evaluation',
    tags=['Member Evaluation'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@evaluation.get('', status_code=status.HTTP_200_OK, response_model=List[Evaluation])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return e.get_evaluations(db, limit)


@evaluation.get('/{structure_id}/structure', status_code=status.HTTP_200_OK, response_model=List[Evaluation])
def get_all_by_structure(structure_id: int, db: Session = Depends(get_db)):
    return e.get_all_by_structure(structure_id, db)


@evaluation.get('/{evaluation_id}', status_code=status.HTTP_200_OK, response_model=Evaluation)
def get_one(evaluation_id: int, db: Session = Depends(get_db)):
    return e.get_one_evaluation(evaluation_id, db)


# @evaluation.put('', status_code=status.HTTP_202_ACCEPTED)
# def update(evaluation_id: int, request: EvaluationRequest, db: Session = Depends(get_db)):
#     return e.update_evaluation(evaluation_id, request, db)
#
#
# @evaluation.delete('/{evaluation_id}', status_code=status.HTTP_201_CREATED)
# def remove(evaluation_id: int, db: Session = Depends(get_db)):
#     return e.remove_evaluation(evaluation_id, db)
