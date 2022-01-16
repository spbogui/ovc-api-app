from sqlalchemy import Column, Integer, String

from src.config.database import Base


class Evaluation(Base):
    __tablename__ = "evaluation"

    id = Column("ID_EVA", Integer, primary_key=True, index=True)
    structure = Column("STRUCT", Integer, index=True)
    code_old = Column("CODE_OLD", String)
    code = Column("CODE", String)
    platform = Column("PLATFORM", Integer, index=True)
    cs_code = Column("CS_CODE", String, index=True)
    old_household_code = Column("CODEMEN_OLD", String)
    household_code = Column("CODEMEN", String, index=True)
    age = Column("AGE", String)
    sex = Column("SEXE", String)
    evaluation_date_1 = Column("DATEEV_1", String, index=True)
    evaluation_date_2 = Column("DATEEV_2", String, index=True)
    category = Column("CATG", String)
    agent = Column("AGENT", Integer, index=True)
    hiv_status = Column("STATU", String)
    eligibility = Column("ELG_SERO", String)
    region = Column("IDREG", Integer, index=True)
    department = Column("IDDEPART", Integer, index=True)
    sub_prefecture = Column("IDSP", Integer, index=True)
    commune = Column("IDCOM", Integer, index=True)
    district = Column("IDQUAR", Integer, index=True)
    id_num = Column("IDNUM", Integer, index=True)
    code_oev = Column("IDOEV", Integer, index=True)
    beneficiary_code = Column("CODEBEN", String, index=True)
    nutrition_security_score_1 = Column("SEC_1", String)
    nutrition_growth_score_1 = Column("CROIS_1", String)
    nutrition_need = Column("BESALI", String)
    well_being_health_score_1 = Column("BETR_1", String)
    health_care = Column("SOINSTE_1", String)
    motor_development_score_1 = Column("DEVSTE_1", String)
    need_health = Column("BESSTE", String)
    performance_score_1 = Column("PERF_1", String)
    education_score_1 = Column("EDUC_1", String)
    dev_educ_score_1 = Column("DEVEDUC_1", String)
    need_educ = Column("BESEDUC", String)
    emotion_score_1 = Column("EMO_1", Integer)
    social_behavior_score_1 = Column("COMP_1", Integer)
    emotional_dev_score_1 = Column("DEVPS_1", Integer)
    finance_management_score_1 = Column("GESFIN_1", String)
    autonomy_score_1 = Column("AUTON_1", String)
    needs_renf = Column("BESRENF", String)
    needs_psycho_score_1 = Column("BESPS", String)
    housing_score_1 = Column("LOG_1", Integer)
    care_score_1 = Column("SOINAB_1", Integer)
    needs_shelter = Column("BESAB", String)
    abuse_score_1 = Column("ABUS_1", Integer)
    legal_protection_score_1 = Column("PROT_1", Integer)
    need_protection = Column("BESPR", String)
    nutrition_security_score_2 = Column("SEC_2", String)
    nutrition_growth_score_2 = Column("CROIS_2", String)
    well_being_health_score_2 = Column("BETR_2", String)
    health_care_score_2 = Column("SOINSTE_2", String)
    motor_development_score_2 = Column("DEVSTE_2", String)
    performance_score_2 = Column("PERF_2", String)
    education_score_2 = Column("EDUC_2", String)
    dev_educ_score_2 = Column("DEVEDUC_2", String)
    emotion_score_2 = Column("EMO_2", String)
    social_behavior_score_2 = Column("COMP_2", String)
    emotional_dev_score_2 = Column("DEVPS_2", String)
    finance_management_score_2 = Column("GESFIN_2", String)
    autonomy_score_2 = Column("AUTON_2", String)
    housing_score_2 = Column("LOG_2", String)
    care_score_2 = Column("SOINAB_2", String)
    abuse_score_2 = Column("ABUS_2", String)
    legal_protection_score_2 = Column("PROT_2", String)
    information_source = Column("SRCINFO", String)
    other_information_source = Column("AUTRSRCINFO", String)
    events = Column("EVENTS", String)
    other_event = Column("AUTREVENT", String)
    comment = Column("COMMENT", String)
    delays_realization_a = Column("delais_a", String)
    delays_realization_b = Column("delais_b", String)
    delays_realization_c = Column("delais_c", String)
    delays_realization_d = Column("delais_d", String)
    delays_realization_e = Column("delais_e", String)
    delays_realization_f = Column("delais_f", String)
    delays_realization_g = Column("delais_g", String)
    follow_a = Column("suivi_a", String)
    follow_b = Column("suivi_b", String)
    follow_c = Column("suivi_c", String)
    follow_d = Column("suivi_d", String)
    follow_e = Column("suivi_e", String)
    follow_f = Column("suivi_f", String)
    follow_g = Column("suivi_g", String)
    registration_status = Column("Etat", Integer)
    registration_status_change = Column("Etat_modif", Integer)
    registration_status_report = Column("Etat_stat", Integer)
    registration_status_remove = Column("Etat_del", Integer)
    created_by = Column("idadd", String)
    created_at = Column("dateheure", String)
    changed_by = Column("idmodif", String)
    changed_at = Column("dateheure_modif", String)