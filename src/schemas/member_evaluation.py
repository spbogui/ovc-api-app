from pydantic import BaseModel
from typing import Optional


class EvaluationRequest(BaseModel):
    structure: Optional[int]
    code_old: Optional[str]
    code: Optional[str]
    platform: Optional[int]
    cs_code: Optional[str]
    old_household_code: Optional[str]
    household_code: Optional[str]
    age: Optional[str]
    sex: Optional[str]
    evaluation_date_1: Optional[str]
    evaluation_date_2: Optional[str]
    category: Optional[str]
    agent: Optional[int]
    hiv_status: Optional[str]
    eligibility: Optional[str]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    commune: Optional[int]
    district: Optional[int]
    id_num: Optional[int]
    code_oev: Optional[int]
    beneficiary_code: Optional[str]
    nutrition_security_score_1: Optional[str]
    nutrition_growth_score_1: Optional[str]
    nutrition_need: Optional[str]
    well_being_health_score_1: Optional[str]
    health_care: Optional[str]
    motor_development_score_1: Optional[str]
    need_health: Optional[str]
    performance_score_1: Optional[str]
    education_score_1: Optional[str]
    dev_educ_score_1: Optional[str]
    need_educ: Optional[str]
    emotion_score_1: Optional[int]
    social_behavior_score_1: Optional[int]
    emotional_dev_score_1: Optional[int]
    finance_management_score_1: Optional[str]
    autonomy_score_1: Optional[str]
    needs_renf: Optional[str]
    needs_psycho_score_1: Optional[str]
    housing_score_1: Optional[int]
    care_score_1: Optional[int]
    needs_shelter: Optional[str]
    abuse_score_1: Optional[int]
    legal_protection_score_1: Optional[int]
    need_protection: Optional[str]
    nutrition_security_score_2: Optional[str]
    nutrition_growth_score_2: Optional[str]
    well_being_health_score_2: Optional[str]
    health_care_score_2: Optional[str]
    motor_development_score_2: Optional[str]
    performance_score_2: Optional[str]
    education_score_2: Optional[str]
    dev_educ_score_2: Optional[str]
    emotion_score_2: Optional[str]
    social_behavior_score_2: Optional[str]
    emotional_dev_score_2: Optional[str]
    finance_management_score_2: Optional[str]
    autonomy_score_2: Optional[str]
    housing_score_2: Optional[str]
    care_score_2: Optional[str]
    abuse_score_2: Optional[str]
    legal_protection_score_2: Optional[str]
    information_source: Optional[str]
    other_information_source: Optional[str]
    events: Optional[str]
    other_event: Optional[str]
    comment: Optional[str]
    delays_realization_a: Optional[str]
    delays_realization_b: Optional[str]
    delays_realization_c: Optional[str]
    delays_realization_d: Optional[str]
    delays_realization_e: Optional[str]
    delays_realization_f: Optional[str]
    delays_realization_g: Optional[str]
    follow_a: Optional[str]
    follow_b: Optional[str]
    follow_c: Optional[str]
    follow_d: Optional[str]
    follow_e: Optional[str]
    follow_f: Optional[str]
    follow_g: Optional[str]
    creator:  str
    date_created: Optional[str]
    voice: Optional[str]
    voice_date: Optional[str]
    stat: Optional[int]
    voice_stat: Optional[int]
    stat_status: Optional[int]
    stat_del: Optional[int]


class Evaluation(BaseModel):
    id: Optional[int]
    structure: Optional[int]
    code_old: Optional[str]
    code: Optional[str]
    platform: Optional[int]
    cs_code: Optional[str]
    old_household_code: Optional[str]
    household_code: Optional[str]
    age: Optional[str]
    sex: Optional[str]
    evaluation_date_1: Optional[str]
    evaluation_date_2: Optional[str]
    category: Optional[str]
    agent: Optional[int]
    hiv_status: Optional[str]
    eligibility: Optional[str]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    commune: Optional[int]
    district: Optional[int]
    id_num: Optional[int]
    code_oev: Optional[int]
    beneficiary_code: Optional[str]
    nutrition_security_score_1: Optional[str]
    nutrition_growth_score_1: Optional[str]
    nutrition_need: Optional[str]
    well_being_health_score_1: Optional[str]
    health_care: Optional[str]
    motor_development_score_1: Optional[str]
    need_health: Optional[str]
    performance_score_1: Optional[str]
    education_score_1: Optional[str]
    dev_educ_score_1: Optional[str]
    need_educ: Optional[str]
    emotion_score_1: Optional[int]
    social_behavior_score_1: Optional[int]
    emotional_dev_score_1: Optional[int]
    finance_management_score_1: Optional[str]
    autonomy_score_1: Optional[str]
    needs_renf: Optional[str]
    needs_psycho_score_1: Optional[str]
    housing_score_1: Optional[int]
    care_score_1: Optional[int]
    needs_shelter: Optional[str]
    abuse_score_1: Optional[int]
    legal_protection_score_1: Optional[int]
    need_protection: Optional[str]
    nutrition_security_score_2: Optional[str]
    nutrition_growth_score_2: Optional[str]
    well_being_health_score_2: Optional[str]
    health_care_score_2: Optional[str]
    motor_development_score_2: Optional[str]
    performance_score_2: Optional[str]
    education_score_2: Optional[str]
    dev_educ_score_2: Optional[str]
    emotion_score_2: Optional[str]
    social_behavior_score_2: Optional[str]
    emotional_dev_score_2: Optional[str]
    finance_management_score_2: Optional[str]
    autonomy_score_2: Optional[str]
    housing_score_2: Optional[str]
    care_score_2: Optional[str]
    abuse_score_2: Optional[str]
    legal_protection_score_2: Optional[str]
    information_source: Optional[str]
    other_information_source: Optional[str]
    events: Optional[str]
    other_event: Optional[str]
    comment: Optional[str]
    delays_realization_a: Optional[str]
    delays_realization_b: Optional[str]
    delays_realization_c: Optional[str]
    delays_realization_d: Optional[str]
    delays_realization_e: Optional[str]
    delays_realization_f: Optional[str]
    delays_realization_g: Optional[str]
    follow_a: Optional[str]
    follow_b: Optional[str]
    follow_c: Optional[str]
    follow_d: Optional[str]
    follow_e: Optional[str]
    follow_f: Optional[str]
    follow_g: Optional[str]
    registration_status:  str
    registration_status_change: Optional[str]
    registration_status_report: Optional[str]
    registration_status_remove: Optional[str]
    created_by: Optional[int]
    created_at: Optional[str]
    changed_by: Optional[int]
    changed_at: Optional[int]

    class Config:
        orm_mode = True
