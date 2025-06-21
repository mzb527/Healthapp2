from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import datetime
from bson import ObjectId

from app.deps import get_db
from app.models.exercise import ExerciseCreate, ExerciseInDB

router = APIRouter(tags=["exercise"])

@router.post("/exercise", response_model=ExerciseInDB)
async def log_exercise(
    payload: ExerciseCreate,
    db = Depends(get_db),
):
    doc = payload.dict()
    doc["timestamp"] = datetime.utcnow()
    result = await db.exercises.insert_one(doc)
    if not result.inserted_id:
        raise HTTPException(500, "Insert failed")
    return ExerciseInDB(
        id=str(result.inserted_id),
        **payload.dict(),
        timestamp=doc["timestamp"],
    )

@router.get("/exercise", response_model=List[ExerciseInDB])
async def list_exercises(
    db = Depends(get_db),
):
    cursor = db.exercises.find().sort("timestamp", -1)
    exercises = []
    async for doc in cursor:
        exercises.append(ExerciseInDB(
            id=str(doc["_id"]),
            activity=doc["activity"],
            duration_minutes=doc["duration_minutes"],
            calories=doc.get("calories"),
            timestamp=doc["timestamp"],
        ))
    return exercises