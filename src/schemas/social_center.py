from pydantic import BaseModel


class SocialCenter(BaseModel):
    cs_code: str
    name: str
    platform: str

    class Config:
        orm_mode = True
