from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def _touch():
    return {"status": "ok"}
