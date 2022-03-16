from sys import prefix
from fastapi import APIRouter

from app.api.endpoints import transcribe, touch

api_router = APIRouter()

api_router.include_router(transcribe.router, prefix="/transcribe")
api_router.include_router(touch.router, prefix="/touch")
