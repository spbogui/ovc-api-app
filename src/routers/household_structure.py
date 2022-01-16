from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import household_structure as h
from ..schemas.household_structure import HouseholdStructure, HouseholdStructureRequest

household_structure = APIRouter(
    prefix='/household-structure',
    tags=['Household Structure'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@household_structure.get('', status_code=status.HTTP_200_OK, response_model=List[HouseholdStructure])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return h.get_household_structures(db, limit)


@household_structure.get('/{household_structure_id}',
                         status_code=status.HTTP_200_OK, response_model=HouseholdStructure)
def get_one(household_structure_id: int, db: Session = Depends(get_db)):
    return h.get_one_household_structure(household_structure_id, db)


@household_structure.get('/{structure_id}/household',
                         status_code=status.HTTP_200_OK, response_model=List[HouseholdStructure])
def get_all_structure_households(structure_id: int, db: Session = Depends(get_db)):
    return h.get_all_structure_household(structure_id, db)


# @household_structure.put('', status_code=status.HTTP_202_ACCEPTED)
# def update(householdStructure_id: int, request: HouseholdStructureRequest, db: Session = Depends(get_db)):
#     return h.update_household_structure(householdStructure_id, request, db)
#
#
# @household_structure.delete('/{householdStructure_id}', status_code=status.HTTP_201_CREATED)
# def remove(householdStructure_id: int, db: Session = Depends(get_db)):
#     return h.remove_household_structure(householdStructure_id, db)
