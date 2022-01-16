from pydantic import BaseModel
from typing import Optional


class GraduationRequest(BaseModel):
    structure: Optional[int]
    platform: Optional[int]
    cs_code: Optional[str]
    code_household: Optional[str]
    beneficiary: Optional[int]
    date_evaluation: Optional[str]
    agent: Optional[str]
    care_giver: Optional[str]
    tel_giver: Optional[str]
    advisor: Optional[str]
    advisor_tel: Optional[str]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    commune: Optional[int]
    district: Optional[int]
    response_sit1: Optional[str]
    comment_sit_1: Optional[str]
    response_sit_2: Optional[str]
    comment_sit_2: Optional[str]
    response_sit_3: Optional[str]
    comment_sit_3: Optional[str]
    response_sit_4: Optional[str]
    comment_sit_4: Optional[str]
    response_sit_5: Optional[str]
    comment_sit_5: Optional[str]
    response_sit_6: Optional[str]
    comment_sit_6: Optional[str]
    response_sit_7: Optional[str]
    comment_sit_7: Optional[str]
    response_sit_8: Optional[str]
    comment_sit_8: Optional[str]
    response_sit_9: Optional[str]
    comment_sit_9: Optional[str]
    response_sit_10: Optional[str]
    comment_sit_10: Optional[str]
    response_sit_11: Optional[str]
    comment_sit_11: Optional[str]
    response_sit_12: Optional[str]
    comment_sit_12: Optional[str]
    response_sit_13: Optional[str]
    comment_sit_13: Optional[str]
    response_sit_14: Optional[str]
    comment_sit_14: Optional[str]
    eligibility: Optional[str]
    eligibility_month: Optional[str]
    eligibility_year: Optional[str]
    eligibility_date: Optional[str]
    visitor_eligibility: Optional[str]
    other_visitor: Optional[str]
    creator: Optional[str]
    date_created: Optional[str]
    voice: Optional[str]
    voice_date: Optional[str]
    stat: Optional[int]
    stat_voice: Optional[int]
    stat_status: Optional[int]
    stat_tel: Optional[int]


class Graduation(BaseModel):
    id: Optional[int]
    structure: Optional[int]
    platform: Optional[int]
    cs_code: Optional[str]
    code_household: Optional[str]
    beneficiary: Optional[int]
    date_evaluation: Optional[str]
    agent: Optional[str]
    care_giver: Optional[str]
    tel_giver: Optional[str]
    advisor: Optional[str]
    advisor_tel: Optional[str]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    commune: Optional[int]
    district: Optional[int]
    response_sit1: Optional[str]
    comment_sit_1: Optional[str]
    response_sit_2: Optional[str]
    comment_sit_2: Optional[str]
    response_sit_3: Optional[str]
    comment_sit_3: Optional[str]
    response_sit_4: Optional[str]
    comment_sit_4: Optional[str]
    response_sit_5: Optional[str]
    comment_sit_5: Optional[str]
    response_sit_6: Optional[str]
    comment_sit_6: Optional[str]
    response_sit_7: Optional[str]
    comment_sit_7: Optional[str]
    response_sit_8: Optional[str]
    comment_sit_8: Optional[str]
    response_sit_9: Optional[str]
    comment_sit_9: Optional[str]
    response_sit_10: Optional[str]
    comment_sit_10: Optional[str]
    response_sit_11: Optional[str]
    comment_sit_11: Optional[str]
    response_sit_12: Optional[str]
    comment_sit_12: Optional[str]
    response_sit_13: Optional[str]
    comment_sit_13: Optional[str]
    response_sit_14: Optional[str]
    comment_sit_14: Optional[str]
    eligibility: Optional[str]
    eligibility_month: Optional[str]
    eligibility_year: Optional[str]
    eligibility_date: Optional[str]
    visitor_eligibility: Optional[str]
    other_visitor: Optional[str]
    creator: Optional[str]
    date_created: Optional[str]
    voice: Optional[str]
    voice_date: Optional[str]
    stat: Optional[int]
    stat_voice: Optional[int]
    stat_status: Optional[int]
    stat_tel: Optional[int]

    class Config:
        orm_mode = True