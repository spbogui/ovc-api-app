from pydantic import BaseModel
from typing import Optional


class HouseholdStructureRequest(BaseModel):
    platform: int
    social_center: str
    structure: int
    code_household: str
    region: int
    department: int
    sub_prefecture: int
    commune: int
    district: int
    agent: int
    ilot: str
    lot: str
    benchmark: str
    start_date: str
    end_date: str
    asset: str
    stat_del: int
    creator: str
    date_created: str
    voice: str
    voice_date: str


class HouseholdStructure(BaseModel):
    id: Optional[int]
    platform: Optional[int]
    social_center: Optional[str]
    structure: Optional[int]
    code_household: Optional[str]
    region: Optional[str]
    department: Optional[str]
    sub_prefecture: Optional[str]
    commune: Optional[int]
    district: Optional[int]
    agent: Optional[str]
    ilot: Optional[str]
    lot: Optional[str]
    benchmark: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    asset: Optional[str]
    stat_del: Optional[str]
    creator: Optional[str]
    date_created: Optional[str]
    voice: Optional[str]
    voice_date: Optional[str]

    class Config:
        orm_mode = True
