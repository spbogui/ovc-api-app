from sqlalchemy import Column, Integer, String

from src.config.database import Base


class Graduation(Base):
    __tablename__ = "fiche_graduation"

    id = Column("ID_EVA", Integer, primary_key=True, index=True)
    structure = Column("STRUCT", Integer, index=True)
    platform = Column("PLATFORM", Integer, index=True)
    cs_code = Column("CS_CODE", String, index=True)
    code_household = Column("CODEMEN", String, index=True)
    beneficiary = Column("NBENF", Integer)
    date_evaluation = Column("DATEEV", String, index=True)
    agent = Column("AGENT", String, index=True)
    care_giver = Column("donneur_soin", String)
    tel_giver = Column("donneur_tel", String)
    advisor = Column("conseiller", String)
    advisor_tel = Column("conseiller_tel", String)
    region = Column("IDREG", Integer, index=True)
    department = Column("IDDEPART", Integer, index=True)
    sub_prefecture = Column("IDSP", Integer, index=True)
    commune = Column("IDCOM", Integer, index=True)
    district = Column("IDQUAR", Integer, index=True)
    response_sit1 = Column("rep_sit_1", String)
    comment_sit_1 = Column("com_sit_1", String)
    response_sit_2 = Column("rep_sit_2", String)
    comment_sit_2 = Column("com_sit_2", String)
    response_sit_3 = Column("rep_sit_3", String)
    comment_sit_3 = Column("com_sit_3", String)
    response_sit_4 = Column("rep_sit_4", String)
    comment_sit_4 = Column("com_sit_4", String)
    response_sit_5 = Column("rep_sit_5", String)
    comment_sit_5 = Column("com_sit_5", String)
    response_sit_6 = Column("rep_sit_6", String)
    comment_sit_6 = Column("com_sit_6", String)
    response_sit_7 = Column("rep_sit_7", String)
    comment_sit_7 = Column("com_sit_7", String)
    response_sit_8 = Column("rep_sit_8", String)
    comment_sit_8 = Column("com_sit_8", String)
    response_sit_9 = Column("rep_sit_9", String)
    comment_sit_9 = Column("com_sit_9", String)
    response_sit_10 = Column("rep_sit_10", String)
    comment_sit_10 = Column("com_sit_10", String)
    response_sit_11 = Column("rep_sit_11", String)
    comment_sit_11 = Column("com_sit_11", String)
    response_sit_12 = Column("rep_sit_12", String)
    comment_sit_12 = Column("com_sit_12", String)
    response_sit_13 = Column("rep_sit_13", String)
    comment_sit_13 = Column("com_sit_13", String)
    response_sit_14 = Column("rep_sit_14", String)
    comment_sit_14 = Column("com_sit_14", String)
    eligibility = Column("elig", String)
    eligibility_month = Column("elg_mois", String)
    eligibility_year = Column("elg_annee", String)
    eligibility_date = Column("elg_date", String)
    visitor_eligibility = Column("elg_visiteur", String)
    other_visitor = Column("autre_visiteur", String)
    registration_status = Column("Etat", Integer)
    registration_status_change = Column("Etat_modif", Integer)
    registration_status_report = Column("Etat_stat", Integer)
    registration_status_remove = Column("Etat_del", Integer)
    created_by = Column("idadd", String)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", String)
    changed_at = Column("dateheure_modif", String)
