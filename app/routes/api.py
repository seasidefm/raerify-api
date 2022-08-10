from fastapi import APIRouter

from app.src.endpoints.discogs import router as discogs_router

router = APIRouter()
router.include_router(discogs_router)
