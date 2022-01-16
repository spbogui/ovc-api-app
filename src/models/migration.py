from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from src.config.database import Base


class Migration(Base):
    __tablename__ = "migration"

    id = Column("migration_id", Integer, autoincrement=True, primary_key=True, index=True)
    structure = relationship("Structure", back_populates="STRUCT")
    migration_date = Column("migration_date", Date)
    migration_info = Column("migration_info", String)

