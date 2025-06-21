from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class NutritionBase(BaseModel):
    name: str
    calories: int = Field(gt=0)
    notes: Optional[str]

class NutritionCreate(NutritionBase):
    pass

class NutritionInDB(NutritionBase):
    id: str
    timestamp: datetime

    class Config:
        orm_mode = True