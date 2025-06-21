import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import exercise, nutrition

app = FastAPI(title="Fitness Tracker API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers under /api
app.include_router(exercise.router, prefix=settings.API_PREFIX)
app.include_router(nutrition.router, prefix=settings.API_PREFIX)

@app.get("/")
def root():
    return {"message": "Fitness Tracker API is up and running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)