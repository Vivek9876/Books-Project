from fastapi import APIRouter, Depends
from ..auth import get_current_user
from .book import router as books_router
from .review import router as reviews_router
from .user import router as user_router

api_router = APIRouter()

api_router.include_router(books_router, prefix="/books", tags=["Books"], dependencies=[Depends(get_current_user)])
api_router.include_router(reviews_router, prefix="/reviews", tags=["Reviews"])
api_router.include_router(user_router, prefix="/users", tags=["Users"])
