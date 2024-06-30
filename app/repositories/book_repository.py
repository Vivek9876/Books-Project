from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException  # Ensure correct import path
from pydantic import UUID4
from ..model.book import Book as ORMBook  # Ensure this is the ORM model
from ..schema import Book as SchemaBook


class BookRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_all_books(self):
        result = await self.db_session.execute(select(ORMBook))
        return result.scalars().all()

    async def create_book(self, book_data: SchemaBook):
        orm_book = ORMBook(**book_data.dict())  # Convert schema to ORM model
        self.db_session.add(orm_book)
        await self.db_session.commit()
        await self.db_session.refresh(orm_book)
        return orm_book

    async def retrieve_book(self, book_id: int):
        result = await self.db_session.execute(select(ORMBook).filter(ORMBook.id == book_id))
        book = result.scalars().first()
        return book

    async def update_book(self, book_id: int, book_data: dict):
        existing_book = await self.db_session.get(ORMBook, book_id)
        if existing_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        for var, value in book_data:
            if value is not None:
                setattr(existing_book, var, value)
        await self.db_session.commit()
        return existing_book

    async def delete_book(self, book_id: int):
        existing_book = await self.db_session.get(ORMBook, book_id)
        if existing_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        await self.db_session.delete(existing_book)
        await self.db_session.commit()
        return True  # Deletion successful

    async def get_summary_for_book(self, book_id: UUID4):
        result = await self.db_session.execute(
            select(ORMBook.summary)
            .where(ORMBook.id == book_id)
        )
        book_summary = result.scalar()

        if book_summary:
            return {"summary": book_summary}
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    
    async def generate_summary(self, book_id: UUID4,text: str):
        existing_book = await self.db_session.get(ORMBook, book_id)
        # book = existing_book.scalars().first()
        existing_book.summary = text
        await self.db_session.commit()
        return text
