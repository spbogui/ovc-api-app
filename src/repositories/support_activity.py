from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.support_activity import SupportActivity
from ..schemas.support_activity import SupportActivityRequest



def get_all(db: Session, limit: int = 100):
    return db.query(SupportActivity).limit(limit).all()


def get_one_activity(activity_id: int, db: Session):
    activity = db.query(SupportActivity).filter(SupportActivity.id == activity_id).first()

    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The activity with id {activity_id} is not available.")
    return activity


# def update_activity(activity_id, request: SupportActivityRequest, db: Session):
#     activity = db.query(SupportActivity).filter(SupportActivity.id == activity_id)
#     if not activity.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The activity with id {activity_id} is not available.")
#     activity.update(request)
#     db.commit()
#     return {"result": "updated"}
#
#
# def remove_activity(activity_id: int, db: Session):
#     activity = db.query(SupportActivity).filter(SupportActivity.id == activity_id)
#     if not activity.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"The activity with id {activity_id} is not available.")
#     activity.delete(synchronize_session=False)
#     db.commit()
#     return {'result': True}


def get_all_by_household(code: str, db: Session, limit: int = 100):
    return db.query(SupportActivity).filter(SupportActivity.code_household == code).limit(limit).all()


def get_all_by_structure(structure_id: int, db: Session):
    return db.query(SupportActivity).filter(SupportActivity.structure == structure_id).all()
