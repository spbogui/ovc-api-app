from sqlalchemy import Column, Integer, String

from src.config.database import Base


class GraduationService(Base):
    __tablename__ = "fiche_graduation_presta"

    id = Column("ID_GRAD", Integer, primary_key=True, index=True)
    evaluation = Column("ID_EVA", String, index=True)
    need = Column("besoin", String)
    service_date = Column("date_serv", String)
    manager = Column("respo", String)
