import re
from sys import prefix
from fastapi import APIRouter

from app.api.endpoints import transcribe, touch, comments

api_router = APIRouter()

api_router.include_router(transcribe.router, prefix="/transcribe")
api_router.include_router(touch.router, prefix="/touch")
api_router.include_router(comments.router, prefix="/comments")
