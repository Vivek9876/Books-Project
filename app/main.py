from fastapi import FastAPI
from .databse import create_tables



app = FastAPI(title="My Awesome API",
    description="A detailed description of my API.",
    version="1.0.0")

# Include the API router with all sub-routers
from .api.router import api_router


@app.get("/health")
def read_root():
    return {"message": "Healthy Repo Happy Repo."}

app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    # Initialize database (create tables, etc.)
    await create_tables()
