# backend/app/core/config.py

from pydantic import BaseSettings
from pydantic import AnyHttpUrl, Field
from typing import List

class Settings(BaseSettings):
    MONGODB_URI: str
    DB_NAME: str = "fitness_tracker"
    API_PREFIX: str = "/api"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = Field(
        default=["http://localhost:3000"]
    )

    class Config:
        env_file = ".env"

settings = Settings()