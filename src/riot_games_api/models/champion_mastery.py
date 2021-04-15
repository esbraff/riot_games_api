from .base import BaseModel


class ChampionMasteryDto(BaseModel):
    champion_points_until_next_level: int
    chest_granted: bool
    champion_id: int
    last_play_time: int
    champion_level: int
    summoner_id: str
    champion_points: int
    champion_points_since_last_level: int
    tokens_earned: int
