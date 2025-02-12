from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.tron.routers import router as tron_router
from src.config.database.db_config import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Tron Info Microservice", lifespan=lifespan)

app.include_router(tron_router)
