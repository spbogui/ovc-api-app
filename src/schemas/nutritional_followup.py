from typing import Optional
from pydantic import BaseModel


class NutritionalFollowup(BaseModel):
    # followup_id: Optional[int]
    structure: Optional[int]
    # platform: Optional[int]
    # agent: Optional[int]
    # social_center_code: Optional[str]
    site: Optional[str]
    # region: Optional[int]
    # department: Optional[int]
    # sub_prefecture: Optional[int]
    # village: Optional[int]
    # neighborhood: Optional[int]
    # household_id: Optional[int]
    # household_code: Optional[int]
    # beneficiary_id: Optional[int]
    # beneficiary_code: Optional[int]
    clinic_code: Optional[str]
    registration_status: Optional[int]
    registration_status_reason: Optional[int]
    registration_status_status: Optional[int]
    registration_remove_status: Optional[int]
    # created_by: Optional[int]
    # created_at: Optional[int]
    # changed_by: Optional[int]
    # changed_at: Optional[int]

    class Config:
        orm_mode = True


class NutritionalFollowupInfo(BaseModel):
    followup_info_id: Optional[int]
    followup_id: Optional[int]
    structure: Optional[int]
    platform: Optional[int]
    social_center_code: Optional[str]
    old_household_code: Optional[str]
    household_code: Optional[str]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    village: Optional[int]
    neighborhood: Optional[int]
    household_id: Optional[int]
    beneficiary_id: Optional[int]
    beneficiary_code: Optional[str]
    visit_date_day: Optional[str]
    visit_date_month: Optional[str]
    visit_date_year: Optional[str]
    age: Optional[str]
    category: Optional[str]
    location: Optional[str]
    status: Optional[str]
    hiv_treatment: Optional[str]
    weight: Optional[str]
    height: Optional[str]
    score: Optional[str]
    bmi: Optional[str]
    PB: Optional[str]
    food: Optional[str]
    edema: Optional[str]
    nutritional_status: Optional[str]
    action: Optional[str]
    comment: Optional[str]
    registration_status: Optional[int]
    registration_status_reason: Optional[int]
    registration_status_status: Optional[int]
    registration_remove_status: Optional[int]
    followup: NutritionalFollowup

    class Config:
        orm_mode = True
