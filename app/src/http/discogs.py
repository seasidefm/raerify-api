import requests

from app.src.models.Discogs import DiscogsApiInfo

APP_USER_AGENT = "RaerifyMe-FastAPI/0.1 +http://raerify.me"

DISCOGS_HEADERS: dict = {
    "Accept": "application/json",
    "User-Agent": APP_USER_AGENT,
}

class DiscogsApi:
    def __init__(self):
        self.headers = DISCOGS_HEADERS
    
    def get_api_root(self) -> DiscogsApiInfo:
        """Get Discogs API root"""
        return requests.get(url="https://api.discogs.com/", headers=self.headers).json()

    def check_health(self):
        """Check Discogs API health"""
        return requests.get(url="https://api.discogs.com/health", headers=self.headers).json()
    
