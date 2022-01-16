from pydantic import BaseModel
from typing import Optional


class GraduationServiceRequest(BaseModel):
    evaluation: Optional[str]
    need: Optional[str]
    service_date: Optional[str]
    manager: Optional[str]


class GraduationService(BaseModel):
    id: Optional[int]
    evaluation: Optional[str]
    need: Optional[str]
    service_date: Optional[str]
    manager: Optional[str]

    class Config:
        orm_mode = True
