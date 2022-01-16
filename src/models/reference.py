from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.config.database import Base


class CounterReference(Base):
    __tablename__ = "contre_references"

    id = Column("IDCREF", Integer, primary_key=True, index=True)
    platform = Column("PLATFORM", Integer, index=True)
    cs_code = Column("CS_CODE", String, index=True)
    structure = Column("STRUCT", Integer, index=True)
    date_contr_reference = Column("DATCREF", String, index=True)
    id_reference = Column("IDREF", Integer, ForeignKey("refces.IDREF"), index=True)
    reference_service = Column("SCE_REF", String)
    other_service = Column("SCE_AUTRE", String)
    service_offered = Column("SCE_OFFER", String)
    observation = Column("OBS", String)
    agent = Column("AGENT", Integer)
    registration_status_report = Column("Etat_stat", Integer)
    registration_status_remove = Column("Etat_del", Integer)
    created_by = Column("idadd", String)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", String)
    changed_at = Column("dateheure_modif", String)

    reference = relationship("Reference", back_populates="counter_reference")


class Reference(Base):
    __tablename__ = "refces"

    id = Column("IDREF", Integer, primary_key=True, index=True)
    platform = Column("PLATFORM", Integer, index=True)
    cs_code = Column("CS_CODE", String, index=True)
    structure = Column("STRUCT", Integer, index=True)
    date_reference = Column("DATREF", String, index=True)
    code_household = Column("CODEMEN", String, index=True)
    beneficiary_code = Column("CODEBEN", String, index=True)
    beneficiary_contact = Column("CONTACTBEN", String)
    vulnerability = Column("VULNERA", String)
    region = Column("REG", Integer)
    department = Column("DEP", Integer)
    sub_prefecture = Column("SP", Integer)
    commune = Column("COM", Integer)
    district = Column("QUART", Integer)
    domicile = Column("DOMIC", String)
    profession = Column("PROF", String)
    number = Column("NUMBS", String)
    parent_contact = Column("CONTACT_PAR_REF", String)
    hosting_structure = Column("STRUCT_ACC", Integer, index=True)
    hosting_service = Column("SCE_ACC", String)
    service_type = Column("TYPE_SCE", String, index=True)
    motif = Column("MOTIF", String)
    agent = Column("AGENT", Integer)
    registration_status_report = Column("Etat_stat", Integer)
    registration_status_remove = Column("Etat_del", Integer)
    created_by = Column("idadd", String)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", String)
    changed_at = Column("dateheure_modif", String)

    counter_reference = relationship("CounterReference", back_populates="reference")

