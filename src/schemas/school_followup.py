from typing import Optional
from pydantic import BaseModel


class SchoolFollowup(BaseModel):
    id: Optional[int]
    technical_partner: Optional[str]
    platform: Optional[int]
    social_center_code: str
    structure: Optional[int]
    household_code: str
    beneficiary_code: str
    status: Optional[int]
    status_reason: Optional[int]
    remove_status: Optional[int]
    # followup_info: SchoolFollowupInfo
    # created_at: str
    # changed_at: str
    # status_status: Optional[int]

    class Config:
        orm_mode = True


class SchoolFollowupInfo(BaseModel):
    id: Optional[int]
    school_followup_id: Optional[int]
    agent: Optional[int]
    beneficiary_code: Optional[str]
    begin_year: Optional[int]
    end_year: Optional[int]
    age: Optional[str]
    school_class: Optional[int]
    school: Optional[str]
    average_1: Optional[str] = None
    service_1: Optional[str] = None
    average_2: Optional[str] = None
    service_2: Optional[str] = None
    average_3: Optional[str] = None
    service_3: Optional[str] = None
    decision: Optional[str] = None
    comment: Optional[str] = None
    vide: Optional[str]

    followup: SchoolFollowup

    class Config:
        orm_mode = True
