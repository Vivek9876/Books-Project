from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..model.user import User  # Make sure the import is correct
from ..schema import UserCreate, Token, LoginForm, UserRegistered
from ..auth import create_access_token, get_password_hash, verify_password
from ..dependencies import get_db

router = APIRouter()

@router.post("/create", response_model=UserRegistered)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    async with db as session:
        stmt = select(User).where(User.username == user.username)
        result = await session.execute(stmt)
        db_user = result.scalars().first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        hashed_password = get_password_hash(user.password)
        db_user = User(username=user.username, hashed_password=hashed_password)
        session.add(db_user)
        await session.commit()
        return {"message": "user registered"}
    

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: LoginForm = Depends(), db: AsyncSession = Depends(get_db)):
    async with db as session:
        stmt = select(User).where(User.username == form_data.username)
        result = await session.execute(stmt)
        user = result.scalars().first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        return {"access_token": create_access_token({"sub": user.username}), "token_type": "bearer"}