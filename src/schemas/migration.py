from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.schemas.structure import Structure


class Migration(BaseModel):
    id: Optional[int]
    structure: Structure
    migration_date: datetime
    migration_info: str

    class Config:
        orm_mode = True
