from typing import List

from .base import BaseModel


class MiniSeriesDto(BaseModel):
    losses: int
    progress: str
    target: int
    wins: int


class LeagueEntryDto(BaseModel):
    league_id: str
    summoner_id: str
    summoner_name: str
    queue_type: str
    tier: str
    rank: str
    league_points: int
    wins: int
    losses: int
    hot_streak: bool
    veteran: bool
    fresh_blood: bool
    inactive: bool
    mini_series: MiniSeriesDto


class LeagueItemDto(BaseModel):
    fresh_blood: bool
    wins: int
    summoner_name: str
    mini_series: MiniSeriesDto
    inactive: bool
    veteran: bool
    hot_streak: bool
    rank: str
    league_points: int
    losses: int
    summoner_id: str


class LeagueListDto(BaseModel):
    league_id: str
    entries: List[LeagueItemDto]
    tier: str
    name: str
    queue: str
