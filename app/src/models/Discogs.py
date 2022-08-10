from typing import Literal
from pydantic import BaseModel


class DiscogsApiInfo(BaseModel):
    hello: str
    api_version: str
    documentation_url: str
    statistics: dict  # {"releases": 15483972, "artists": 8217783, "labels": 1882539}


class DiscogsHealthResponse(BaseModel):
    status: Literal["ok"]
