from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories import migration as a
from ..schemas.migration import Migration

migration = APIRouter(
    prefix='/migration',
    tags=['Migration'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@migration.get('', status_code=status.HTTP_200_OK, response_model=List[Migration])
def get_all(db: Session = Depends(get_db), limit: int = 100):
    return a.get_migrations(db, limit)


@migration.get('/{migration_id}', status_code=status.HTTP_200_OK, response_model=Migration)
def get_one(migration_id: int, db: Session = Depends(get_db)):
    return a.get_one_migration(migration_id, db)


@migration.put('', status_code=status.HTTP_202_ACCEPTED)
def update(migration_id: int, request: Migration, db: Session = Depends(get_db)):
    return a.update_migration(migration_id, request, db)


@migration.delete('/{migration_id}', status_code=status.HTTP_201_CREATED)
def remove(migration_id: int, db: Session = Depends(get_db)):
    return a.remove_migration(migration_id, db)
