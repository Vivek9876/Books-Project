from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    book_id = Column(UUID(as_uuid=True), ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, nullable=False)  # Placeholder for actual user reference
    review_text = Column(Text)
    rating = Column(Float)

    # Relationship to books
    book = relationship("Book", back_populates="reviews")