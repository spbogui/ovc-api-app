from sqlalchemy import Column, Integer, String
from src.config.database import Base


class Structure(Base):
    __tablename__ = "structures"

    id = Column("STRUCT", Integer, primary_key=True, index=True)
    structureShortName = Column("libstruct", String)
    structureName = Column("FullName", String)
    manager = Column("RESP", String)
    statusStructure = Column("isVisible", String)
    bp = Column("BP", String)
    fax = Column("FAX", String)
    email = Column("EMAIL", String)
    phone = Column("TEL", String)
    address = Column("ADRESS", String)
    platform = Column("PLATFORM", Integer, index=True)
    cs_code = Column("CS_CODE", String, index=True)
    created_by = Column("idadd", String)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", String)
    changed_at = Column("dateheure_modif", String)
