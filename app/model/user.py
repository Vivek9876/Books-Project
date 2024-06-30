from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
