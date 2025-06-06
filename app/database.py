from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from .models import User
import os
from dotenv import load_dotenv

load_dotenv()

Mongo_url = os.getenv("MONGO_URL")

async def db_init():
    client = AsyncIOMotorClient(Mongo_url)
    await init_beanie(database=client["fastapi_db"],document_models=[User])