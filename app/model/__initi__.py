# app/models/__init__.py
from .base import Base  # Ensures Base is available for metadata creation
from .book import Book
from .review import Review

# Optional: Import all SQLAlachemy models for easy access elsewhere
__all__ = [
    "Base",
    "Book",
    "Review"
]
