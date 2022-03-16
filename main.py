from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from app.api.api import api_router


app = FastAPI(title="deepslate")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
