from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import UUID4
from ..model.review import Review

class ReviewRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_review(self, book_id: int, review_data: Review):
        review = Review(
                    book_id=book_id,
                    user_id=review_data.user_id,
                    review_text=review_data.review_text,
                    rating=review_data.rating
                )
        self.db_session.add(review)
        await self.db_session.commit()
        await self.db_session.refresh(review)
        return review

    async def get_reviews_by_book_id(self, book_id: UUID4):
        result = await self.db_session.execute(select(Review).filter(Review.book_id == book_id))
        print(result)
        return result.scalars().all()
