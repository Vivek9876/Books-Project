from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .model.base import Base  # Ensure all models are imported here

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/booksdb"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)

async def create_tables():
    async with engine.begin() as conn:
        # This line creates all tables defined in your models
        await conn.run_sync(Base.metadata.create_all)
