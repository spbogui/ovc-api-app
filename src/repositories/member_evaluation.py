from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.evaluation import Evaluation


def get_evaluations(db: Session, limit: int = 100):
    return db.query(Evaluation).limit(limit).all()


def get_one_evaluation(evaluation_id: int, db: Session):
    evaluation = db.query(Evaluation).filter(Evaluation.id == evaluation_id).first()

    if not evaluation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The evaluation with id {evaluation_id} is not available.")
    return evaluation


def get_all_by_structure(structure_id: int, db: Session):
    evaluations = db.query(Evaluation).filter(Evaluation.structure == structure_id)

    if not evaluations:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The evaluation with id {structure_id} is not available.")
    return evaluations.all()


# def update_evaluation(evaluation_id, request: EvaluationRequest, db: Session):
#     evaluation = db.query(Evaluation).filter(Evaluation.id == evaluation_id)
#     if not evaluation.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The evaluation with id {evaluation_id} is not available.")
#     evaluation.update(request)
#     db.commit()
#     return {"result": "updated"}


# def remove_evaluation(evaluation_id: int, db: Session):
#     evaluation = db.query(Evaluation).filter(Evaluation.id == evaluation_id)
#     if not evaluation.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The evaluation with id {evaluation_id} is not available.")
#     evaluation.delete(synchronize_session=False)
#     db.commit()
#     return {'result': True}
