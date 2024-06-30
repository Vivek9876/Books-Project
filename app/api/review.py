from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..model.review import Review
from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=list)
async def read_reviews(db: AsyncSession = Depends(get_db)):
    async with db.begin():
        result = await db.execute(select(Review))
        return result.scalars().all()
