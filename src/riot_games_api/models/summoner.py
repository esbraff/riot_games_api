from .base import BaseModel


class SummonerDto(BaseModel):
    account_id: str
    profile_icon_id: int
    revision_date: int
    name: str
    id: str
    puuid: str
    summoner_level: int
