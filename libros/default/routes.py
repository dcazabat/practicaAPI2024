from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

app = APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}

