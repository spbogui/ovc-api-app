from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import household_evaluation as em
from ..schemas.household_evaluation import HouseholdEvaluation, HouseholdEvaluationRequest

household_evaluation = APIRouter(
    prefix='/household-evaluation',
    tags=['Household Evaluation'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@household_evaluation.get('', status_code=status.HTTP_200_OK, response_model=List[HouseholdEvaluation])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return em.get_household_evaluations(db, limit)


@household_evaluation.get('/{household_evaluation_id}', status_code=status.HTTP_200_OK, response_model=HouseholdEvaluation)
def get_one(household_evaluation_id: int, db: Session = Depends(get_db)):
    return em.get_one_household_evaluation(household_evaluation_id, db)


@household_evaluation.get('/{structure_id}/structure', status_code=status.HTTP_200_OK, response_model=List[HouseholdEvaluation])
def get_all_by_structure(structure_id: int, db: Session = Depends(get_db)):
    return em.get_all_by_structure(structure_id, db)


# @household_evaluation.put('', status_code=status.HTTP_202_ACCEPTED)
# def update(household_evaluation_id: int, request: HouseholdEvaluationRequest, db: Session = Depends(get_db)):
#     return em.update_household_evaluation(household_evaluation_id, request, db)
#
#
# @household_evaluation.delete('/{household_evaluation_id}', status_code=status.HTTP_201_CREATED)
# def remove(household_evaluation_id: int, db: Session = Depends(get_db)):
#     return em.remove_household_evaluation(household_evaluation_id, db)
