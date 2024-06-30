from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .base import Base

class TokenBlacklist(Base):
    __tablename__ = 'token_blacklist'
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, nullable=False)
    blacklisted_on = Column(DateTime, default=func.now())
