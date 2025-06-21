from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ExerciseBase(BaseModel):
    activity: str
    duration_minutes: int = Field(gt=0)
    calories: Optional[int]

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseInDB(ExerciseBase):
    id: str
    timestamp: datetime

    class Config:
        orm_mode = True