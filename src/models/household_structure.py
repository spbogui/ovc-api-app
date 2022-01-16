from sqlalchemy import Column, Integer, String

from src.config.database import Base


class HouseholdStructure(Base):
    __tablename__ = "structure_menage"

    id = Column("STRUCT_MEN_ID", Integer, primary_key=True, index=True)
    platform = Column("PF_ID", Integer)
    social_center = Column("CS_ID", String)
    structure = Column("STRUCT", Integer, index=True)
    code_household = Column("CODEMEN", String, index=True)
    region = Column("REG_ID", Integer)
    department = Column("DEPART_ID", Integer)
    sub_prefecture = Column("SPREF_ID", Integer)
    commune = Column("COM_ID", Integer)
    district = Column("QUAR_ID", Integer)
    agent = Column("AGENT_ID", Integer)
    ilot = Column("SM_ILOT", String)
    lot = Column("SM_LOT", String)
    benchmark = Column("SM_REPERE", String)
    start_date = Column("datedeb", String)
    end_date = Column("datefin", String)
    asset = Column("actif", String)
    registration_status_remove = Column("Etat_del", Integer)
    created_by = Column("idadd", String)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", String)
    changed_at = Column("dateheure_modif", String)
