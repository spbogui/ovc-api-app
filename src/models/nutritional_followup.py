from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.config.database import Base


class NutritionalFollowup(Base):
    __tablename__ = "suiv"

    followup_id = Column("ID_SUIV", Integer, primary_key=True, index=True)
    structure = Column("STRUCT", Integer, index=True)
    platform = Column("PLATFORM", Integer, index=True)
    agent = Column("AGENT", Integer)
    social_center_code = Column("CS_CODE", String, index=True)
    site = Column("SITE", String)
    region = Column("IDREG", Integer)
    department = Column("IDDEPART", Integer)
    sub_prefecture = Column("IDSP", Integer)
    village = Column("IDCOM", Integer)
    neighborhood = Column("IDQUAR", Integer)
    household_id = Column("IDNUM", Integer)
    household_code = Column("CODEMEN", String, index=True)
    beneficiary_id = Column("IDOEV", Integer)
    beneficiary_code = Column("CODEBEN", String, index=True)
    clinique_code = Column("CODECLN", String)
    registration_status = Column("Etat", Integer)
    registration_status_reason = Column("Etat_modif", Integer)
    registration_status_status = Column("Etat_stat", Integer)
    registration_remove_status = Column("Etat_del", Integer)
    created_by = Column("idadd", String)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", String)
    changed_at = Column("dateheure_modif", String)
    followup_info = relationship("NutritionalFollowupInfo", back_populates="followup")


class NutritionalFollowupInfo(Base):
    __tablename__ = "suivchd"

    followup_info_id = Column("ID_SUIVD", Integer, primary_key=True, index=True)
    followup_id = Column("ID_SUIV", Integer, ForeignKey("suiv.ID_SUIV"), index=True)
    structure = Column("STRUCT", Integer, index=True)
    platform = Column("PLATFORM", Integer, index=True)
    agent = Column("AGENT", Integer)
    social_center_code = Column("CS_CODE", String, index=True)
    old_household_code = Column("CODEMEN_OLD", String)
    household_code = Column("CODEMEN", String, index=True)
    region = Column("IDREG", Integer)
    department = Column("IDDEPART", Integer)
    sub_prefecture = Column("IDSP", Integer)
    village = Column("IDCOM", Integer)
    neighbourhood = Column("IDQUAR", Integer)
    household_id = Column("IDNUM", Integer)
    beneficiary_id = Column("IDOEV", Integer)
    beneficiary_code = Column("CODEBEN", String, index=True)
    visit_date_day = Column("DVISITJ", String, index=True)
    visit_date_month = Column("DVISITM", String, index=True)
    visit_date_year = Column("DVISITA", String, index=True)
    age = Column("AGE", String, index=True)
    category = Column("CATEGORIE", String)
    location = Column("LIEU", String)
    status = Column("STATUT", String)
    hiv_treatment = Column("TRMT", String)
    weight = Column("POIDS", String)
    height = Column("TAILLE", String)
    score = Column("SCORE", String)
    bmi = Column("IMC", String)
    PB = Column("PB", String)
    food = Column("ALIMENT", String)
    oedema = Column("OEDEME", String)
    nutritional_status = Column("ETATN", String)
    action = Column("ACTION", String)
    comment = Column("COMENT", String)
    registration_status = Column("Etat", Integer)
    registration_status_reason = Column("Etat_modif", Integer)
    registration_status_status = Column("Etat_stat", Integer)
    registration_remove_status = Column("Etat_del", Integer)

    followup = relationship("NutritionalFollowup", back_populates="followup_info")
