from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    settings = get_settings()
    app.mongodb_conn = AsyncIOMotorClient(settings.MONGODB_URI)
    app.db_client = app.mongodb_conn[settings.MONGODB_DATABASE]
    yield
    
    # shutdown
    app.mongodb_conn.close()

app = FastAPI(lifespan=lifespan)



app.include_router(base.base_router)
app.include_router(data.data_router)

