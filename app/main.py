from typing import Union
from fastapi import FastAPI

from app.routes import api

app = FastAPI()

app.include_router(api.router)


@app.get("/health")
async def health_check():
    return "OK"
