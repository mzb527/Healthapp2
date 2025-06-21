from typing import AsyncGenerator
from app.db.mongodb import db

async def get_db() -> AsyncGenerator:
    yield db