from typing import List

from .base import BaseModel


class ChampionInfo(BaseModel):
    max_new_player_level: int
    free_champion_ids_for_new_players: List[int]
    free_champion_ids: List[int]
