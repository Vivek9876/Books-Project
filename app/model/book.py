from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Book(Base):
    __tablename__ = 'books'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year_published = Column(Integer)
    summary = Column(Text, default="")

    # Relationship to reviews
    reviews = relationship("Review", back_populates="book")