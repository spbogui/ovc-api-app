from sqlalchemy import Column, String
from src.config.database import Base


class SocialCenter(Base):
    __tablename__ = "centre_sociaux"

    cs_code = Column("CS_CODE", String, primary_key=True, index=True)
    name = Column("libcs", String)
    platform = Column("PLATFORM", String)
