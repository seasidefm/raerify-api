from fastapi import APIRouter

from app.src.http.discogs import DiscogsApi
from app.src.models.Discogs import DiscogsApiInfo, DiscogsHealthResponse

router = APIRouter(
    prefix="/discogs",
    tags=["Discogs"],
)

discogs_api = DiscogsApi()


@router.get("/", response_model=DiscogsApiInfo)
async def root():
    """Get Discogs root API message"""
    return discogs_api.get_api_root()


@router.get("/health", response_model=DiscogsHealthResponse)
async def health():
    """Check Discogs API health"""

    return discogs_api.check_health()
