from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src.models.identification import MemberIdentification


def get_by_code(code: str, db: Session):
    identification = db.query(MemberIdentification).filter(MemberIdentification.member_code == code)

    if not identification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Member with Code {code} is not available")
    return identification.first()


def get_all_by_structure(structure_id: int, db: Session):
    return db.query(MemberIdentification).filter(MemberIdentification.structure == structure_id).all()



