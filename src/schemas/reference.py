from pydantic import BaseModel
from typing import Optional


# class ReferenceRequest(BaseModel):
#     platform: Optional[int]
#     cs_code: Optional[str]
#     structure: Optional[int]
#     date_reference: Optional[str]
#     code_household: Optional[str]
#     beneficiary_code: Optional[str]
#     beneficiary_contact: Optional[str]
#     vulnerability: Optional[str]
#     region: Optional[int]
#     department: Optional[int]
#     sub_prefecture: Optional[int]
#     commune: Optional[int]
#     district: Optional[int]
#     domicile: Optional[str]
#     profession: Optional[str]
#     number: Optional[str]
#     parent_contact: Optional[str]
#     hosting_structure: Optional[int]
#     hosting_service: Optional[str]
#     service_type: Optional[str]
#     motif: Optional[str]
#     agent: Optional[int]
#     counter_reference: Optional[CounterReference]
#     creator: Optional[int]
#     date_created: Optional[str]
#     voice: Optional[int]
#     voice_date: Optional[str]
#     stat_status: Optional[int]
#     stat_del: Optional[int]

class CounterReference(BaseModel):
    id: Optional[int]
    platform: Optional[int]
    cs_code: Optional[str]
    structure: Optional[int]
    date_contr_reference: Optional[str]
    id_reference: Optional[int]
    reference_service: Optional[str]
    other_service: Optional[int]
    service_offered: Optional[str]
    observation: Optional[str]
    # agent: int
    # creator: int
    date_created: Optional[str]
    voice: Optional[int]
    voice_date: Optional[str]
    stat_status: Optional[int]
    stat_del: Optional[int]

    class Config:
        orm_mode = True


class Reference(BaseModel):
    id: Optional[int]
    platform: Optional[int]
    cs_code: Optional[str]
    structure: Optional[int]
    date_reference: Optional[str]
    code_household: Optional[str]
    beneficiary_code: Optional[str]
    beneficiary_contact: Optional[str]
    vulnerability: Optional[str]
    region: Optional[int]
    department: Optional[int]
    sub_prefecture: Optional[int]
    commune: Optional[int]
    district: Optional[int]
    domicile: Optional[str]
    profession: Optional[str]
    number: Optional[str]
    parent_contact: Optional[str]
    hosting_structure: Optional[int]
    hosting_service: Optional[str]
    service_type: Optional[str]
    motif: Optional[str]
    agent: Optional[int]
    counter_reference: Optional[CounterReference]
    creator: Optional[int]
    date_created: Optional[str]
    voice: Optional[int]
    voice_date: Optional[str]
    stat_status: Optional[int]
    stat_del: Optional[int]

    class Config:
        orm_mode = True
