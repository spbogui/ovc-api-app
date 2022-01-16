from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.config.database import Base


class SchoolFollowup(Base):
    __tablename__ = "suivisco"

    id = Column("IDSUIV_SCO", Integer, primary_key=True, index=True)
    technical_partner = Column("PART_TECH", String)
    platform = Column("PLATFORM", Integer, index=True)
    social_center_code = Column("CS_CODE", String, index=True)
    structure = Column("STRUCT", Integer, index=True)
    household_code = Column("CODEMEN", String, index=True)
    beneficiary_code = Column("CODEBEN", String, index=True)
    status = Column("Etat", Integer)
    status_reason = Column("Etat_modif", Integer)
    status_status = Column("Etat_stat", Integer)
    remove_status = Column("Etat_del", Integer)
    created_by = Column("idadd", Integer)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", Integer)
    changed_at = Column("dateheure_modif", String)

    followup_info = relationship("SchoolFollowupInfo", back_populates="followup")


class SchoolFollowupInfo(Base):
    __tablename__ = "suiviscochd"

    id = Column("IDSUIV_SCOD", Integer, primary_key=True, index=True)
    school_followup_id = Column("IDSUIV_SCO", Integer, ForeignKey("suivisco.IDSUIV_SCO"), index=True)
    agent = Column("AGENT", Integer, index=True)
    platform = Column("PLATFORM", Integer)
    social_center_code = Column("CS_CODE", String)
    structure = Column("STRUCT", Integer)
    region = Column("IDREG", Integer)
    department = Column("IDDEPART", Integer)
    sub_prefecture = Column("IDSP", Integer)
    village = Column("IDCOM", Integer)
    neighbourhood = Column("IDQUAR", Integer)
    household_code = Column("CODEMEN", String)
    beneficiary_code = Column("CODEBEN", String)
    begin_year = Column("ANNEE_DEB", Integer)
    end_year = Column("ANNEE_FIN", Integer)
    age = Column("AGE", String)
    school_class = Column("CLASSE_ENC", Integer)
    school = Column("ETBLS", String)
    average_1 = Column("MOY_1", String)
    service_1 = Column("SERVICE_1", String)
    average_2 = Column("MOY_2", String)
    service_2 = Column("SERVICE_2", String)
    average_3 = Column("MOY_3", String)
    service_3 = Column("SERVICE_3", String)
    decision = Column("DECISION", String)
    comment = Column("COMMENT", String)
    vide = Column("vide", Integer)
    added_by = Column("idadd", Integer)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", Integer)
    changed_at = Column("dateheure_modif", String)
    status = Column("Etat", Integer)
    status_reason = Column("Etat_modif", Integer)
    status_status = Column("Etat_stat", Integer)
    status_deleted = Column("Etat_del", Integer)

    followup = relationship("SchoolFollowup", back_populates="followup_info")
