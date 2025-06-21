from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import datetime

from app.deps import get_db
from app.models.nutrition import NutritionCreate, NutritionInDB

router = APIRouter(tags=["nutrition"])

@router.post("/nutrition", response_model=NutritionInDB)
async def log_meal(
    payload: NutritionCreate,
    db = Depends(get_db),
):
    doc = payload.dict()
    doc["timestamp"] = datetime.utcnow()
    result = await db.nutrition.insert_one(doc)
    if not result.inserted_id:
        raise HTTPException(500, "Insert failed")
    return NutritionInDB(
        id=str(result.inserted_id),
        **payload.dict(),
        timestamp=doc["timestamp"],
    )

@router.get("/nutrition", response_model=List[NutritionInDB])
async def list_meals(
    db = Depends(get_db),
):
    cursor = db.nutrition.find().sort("timestamp", -1)
    meals = []
    async for doc in cursor:
        meals.append(NutritionInDB(
            id=str(doc["_id"]),
            name=doc["name"],
            calories=doc["calories"],
            notes=doc.get("notes"),
            timestamp=doc["timestamp"],
        ))
    return meals