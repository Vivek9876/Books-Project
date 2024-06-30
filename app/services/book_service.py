from app.schema import SummaryText
from pydantic import UUID4
from ..repositories.review_repository import ReviewRepository
from ..repositories.book_repository import BookRepository
from ..model.book import Book
from ..model.review import Review

class BookService:
    def __init__(self, db_session):
        self.book_repository = BookRepository(db_session)
        self.review_repository = ReviewRepository(db_session)

    async def list_books(self):
        return await self.book_repository.get_all_books()

    async def add_book(self, book_data: Book):
        return await self.book_repository.create_book(book_data)

    async def get_book(self, book_id: UUID4):
        return await self.book_repository.retrieve_book(book_id)

    async def update_book(self, book_id: UUID4, book_data: Book):
        return await self.book_repository.update_book(book_id, book_data)
    
    async def delete_book(self, book_id: UUID4):
        return await self.book_repository.delete_book(book_id)

    async def add_review(self, book_id: UUID4, review_data: Review):
        return await self.review_repository.create_review(book_id, review_data)

    async def get_reviews_for_book(self, book_id: UUID4):
        return await self.review_repository.get_reviews_by_book_id(book_id)

    async def get_book_summary(self, book_id: UUID4):
        return await self.book_repository.get_summary_for_book(book_id)

    async def generate_summary(self, book_id: UUID4, text: str):
        return await self.book_repository.generate_summary(book_id, text)
