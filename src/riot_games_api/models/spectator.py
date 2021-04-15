from typing import List

from .base import BaseModel


class GameCustomizationObject(BaseModel):
    category: str
    content: str


class Perks(BaseModel):
    perk_ids: List[int]
    perk_style: int
    perk_sub_style: int


class CurrentGameParticipant(BaseModel):
    champion_id: int
    perks: Perks
    profile_icon_id: int
    bot: bool
    team_id: int
    summoner_name: str
    summoner_id: str
    spell1_id: int
    spell2_id: int
    game_customization_objects: List[GameCustomizationObject]


class Observer(BaseModel):
    encryption_key: str


class BannedChampion(BaseModel):
    pick_turn: int
    champion_id: int
    team_id: int


class CurrentGameInfo(BaseModel):
    game_id: int
    game_type: str
    game_start_time: int
    map_id: int
    game_length: int
    platform_id: str
    game_mode: str
    banned_champions: List[BannedChampion]
    game_queue_config_id: int
    observers: Observer
    participants: List[CurrentGameParticipant]