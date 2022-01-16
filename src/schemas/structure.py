from pydantic import BaseModel
from typing import Optional


class StructureRequest(BaseModel):
    id: Optional[int]
    structureShortName: str
    structureName: str
    manager: str
    statusStructure: str
    bp: str
    fax: str
    email: str
    phone: str
    address: Optional[str]
    platform: int
    cs_code: Optional[str]
    creator: Optional[str]
    date_created: Optional[str]
    voice: Optional[str]
    date_voice: Optional[str]


class Structure(BaseModel):
    id: Optional[int]
    structureShortName: Optional[str]
    structureName: Optional[str]
    manager: Optional[str]
    statusStructure: Optional[str]
    bp: Optional[str]
    fax: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    platform: Optional[int]
    cs_code: Optional[str]
    creator: Optional[str]
    date_created: Optional[str]
    voice: Optional[str]
    date_voice: Optional[str]

    class Config:
        orm_mode = True
