from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine

app = FastAPI(title="InfraTrack API")

@app.get("/")
def read_root():
    return {"message": "InfraTrack backend running"}

@app.get("/health/db")
def health_db():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"database": "ok"}
