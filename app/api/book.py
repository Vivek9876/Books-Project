from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import UUID4
from typing import List
from ..model.book import Book
from ..dependencies import get_db
from ..services.book_service import BookService
from ..schema import Book, BookCreate,Review, ReviewCreate, SummaryText

router = APIRouter()

@router.get("/", response_model=List[Book])
async def read_books(db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.list_books()

@router.post("/", response_model=Book)
async def add_book(book_data: BookCreate, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.add_book(book_data)

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: UUID4, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.get_book(book_id)

@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: UUID4, book_data: BookCreate, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.update_book(book_id, book_data)

@router.delete("/{book_id}", response_model=bool)
async def delete_book(book_id: UUID4, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.delete_book(book_id)

@router.post("/{book_id}/reviews", response_model=Review)
async def add_review_for_book(book_id: UUID4, review: ReviewCreate, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.add_review(book_id, review)

@router.get("/{book_id}/reviews", response_model=list[Review])
async def get_reviews_for_book(book_id: UUID4, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.get_reviews_for_book(book_id)

@router.get("/{book_id}/summary", response_model=dict)
async def get_book_summary(book_id: UUID4, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    return await book_service.get_book_summary(book_id)

@router.post("/{book_id}/summary", response_model=SummaryText)
async def generate_summary(book_id: UUID4, text: SummaryText, db: AsyncSession = Depends(get_db)):
    book_service = BookService(db)
    result = await book_service.generate_summary(book_id, text.text)
    return { "text" : result}