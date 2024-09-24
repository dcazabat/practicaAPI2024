from fastapi import APIRouter

default = APIRouter()

@default.get("/")
def read_root():
    return {"Trabajo": "FASTAPI & SQLITE"}