from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.household_evaluation import HouseholdEvaluation
from ..schemas.household_evaluation import HouseholdEvaluationRequest


def get_household_evaluations(db: Session, limit: int = 100):
    return db.query(HouseholdEvaluation).limit(limit).all()


def get_one_household_evaluation(household_evaluation_id: int, db: Session):
    household_evaluation = db.query(HouseholdEvaluation).filter(HouseholdEvaluation.id == household_evaluation_id).first()

    if not household_evaluation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The household_evaluation with id {household_evaluation_id} is not available.")
    return household_evaluation

#
# def update_household_evaluation(household_evaluation_id, request: HouseholdEvaluationRequest, db: Session):
#     household_evaluation = db.query(HouseholdEvaluation).filter(HouseholdEvaluation.id == household_evaluation_id)
#     if not household_evaluation.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The household_evaluation with id {household_evaluation_id} is not available.")
#     household_evaluation.update(request)
#     db.commit()
#     return {"result": "updated"}
#
#
# def remove_household_evaluation(household_evaluation_id: int, db: Session):
#     household_evaluation = db.query(HouseholdEvaluation).filter(HouseholdEvaluation.id == household_evaluation_id)
#     if not household_evaluation.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The household_evaluation with id {household_evaluation_id} is not available.")
#     household_evaluation.delete(synchronize_session=False)
#     db.commit()
#     return {'result': True}


def get_all_by_structure(structure_id: int, db: Session):
    household_evaluations = db.query(HouseholdEvaluation).filter(HouseholdEvaluation.structure == structure_id)

    if not household_evaluations:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The household_evaluations with structure id {structure_id} is not available.")
    return household_evaluations.all()
