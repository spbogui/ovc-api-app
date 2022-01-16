from pydantic import BaseModel
from typing import Optional


class SupportActivityRequest(BaseModel):
    activity_id: Optional[int]
    structure: Optional[int]
    agent: Optional[int]
    platform: Optional[int]
    cs_code: Optional[str]
    code_household_old: Optional[str]
    code_household: Optional[str]
    date_created: Optional[str]
    day_save: Optional[int]
    month_save: Optional[int]
    year_save: Optional[int]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    commune: Optional[int]
    district: Optional[int]
    household: Optional[int]
    oev: Optional[int]
    member: Optional[str]
    status: Optional[str]
    code_activity: Optional[str]
    need: Optional[str]
    nutritional_support: Optional[str]
    health_support: Optional[str]
    school_support: Optional[str]
    psyco_support: Optional[str]
    economic_support: Optional[str]
    shelters: Optional[str]
    prev: Optional[str]
    legal_support: Optional[str]
    age_range: Optional[str]
    hiv_eligibility: Optional[str]
    clinic_code: Optional[str]
    comment_treatment: Optional[str]
    comment: Optional[str]
    stat: Optional[int]
    voice: Optional[int]
    stat_status: Optional[int]
    stat_del: Optional[int]


class SupportActivity(BaseModel):
    id: Optional[int]
    activity_id: Optional[int]
    structure: Optional[int]
    agent: Optional[int]
    platform: Optional[int]
    cs_code: Optional[str]
    code_household_old: Optional[str]
    code_household: Optional[str]
    date_created: Optional[str]
    day_save: Optional[int]
    month_save: Optional[int]
    year_save: Optional[int]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    commune: Optional[int]
    district: Optional[int]
    household: Optional[int]
    oev: Optional[int]
    member: Optional[str]
    status: Optional[str]
    code_activity: Optional[str]
    need: Optional[str]
    nutritional_support: Optional[str]
    health_support: Optional[str]
    school_support: Optional[str]
    psyco_support: Optional[str]
    economic_support: Optional[str]
    shelters: Optional[str]
    prev: Optional[str]
    legal_support: Optional[str]
    age_range: Optional[str]
    hiv_eligibility: Optional[str]
    clinic_code: Optional[str]
    comment_treatment: Optional[str]
    comment: Optional[str]
    stat: Optional[int]
    voice: Optional[int]
    stat_status: Optional[int]
    stat_del: Optional[int]

    class Config:
        orm_mode = True