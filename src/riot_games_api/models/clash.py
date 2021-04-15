from typing import Optional, List

from .base import BaseModel


class PlayerDto(BaseModel):
    summoner_id: str
    team_id: Optional[str]
    position: str
    role: str


class TeamDto(BaseModel):
    id: str
    tournament_id: int
    name: str
    icon_id: int
    tier: int
    captain: str
    abbreviation: str
    players: List[PlayerDto]


class TournamentPhaseDto(BaseModel):
    id: int
    registration_time: int
    start_time: int
    cancelled: bool


class TournamentDto(BaseModel):
    id: int
    theme_id: int
    name_key: str
    name_key_secondary: str
    schedule: List[TournamentPhaseDto]
