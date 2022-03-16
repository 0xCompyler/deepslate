from sys import prefix
from fastapi import APIRouter

from app.api.endpoints import transcribe

api_router = APIRouter()

api_router.include_router(transcribe.router, prefix="/transcribe")
