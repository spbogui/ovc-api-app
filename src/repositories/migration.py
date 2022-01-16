from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..models.migration import Migration
from ..schemas.migration import Migration as MigrationSchema


def get_migrations(db: Session, limit: int = 100):
    return db.query(Migration).limit(limit).all()


def get_one_migration(migration_id: int, db: Session):
    migration = db.query(Migration).filter(Migration.id == migration_id).first()

    if not migration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The migration with id {migration_id} is not available.")
    return migration


def update_migration(migration_id, request: MigrationSchema, db: Session):
    migration = db.query(Migration).filter(Migration.id == migration_id)
    if not migration.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The migration with id {migration_id} is not available.")
    migration.update(request)
    db.commit()
    return {"result": "updated"}


def remove_migration(migration_id: int, db: Session):
    migration = db.query(Migration).filter(Migration.id == migration_id)
    if not migration.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The migration with id {migration_id} is not available.")
    migration.delete(synchronize_session=False)
    db.commit()
    return {'result': True}
