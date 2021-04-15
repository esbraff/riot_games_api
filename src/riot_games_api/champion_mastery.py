from typing import Optional, List

from pydantic import parse_obj_as

from .models.champion_mastery import ChampionMasteryDto
from .base import RiotGamesApiBase


class ChampionMasteryApiV4(RiotGamesApiBase):
    def get_masteries(
            self,
            summoner_id: str,
            platform: Optional[str] = None
    ) -> List[ChampionMasteryDto]:
        data = self._request(f"/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}", platform)

        return parse_obj_as(list[ChampionMasteryDto], data)

    def get_mastery(
            self,
            summoner_id: str,
            champion_id: int,
            platform: Optional[str] = None
    ) -> ChampionMasteryDto:
        data = self._request(
            f"/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}",
            platform
        )

        return ChampionMasteryDto.parse_obj(data)

    def get_mastery_score(
            self,
            summoner_id: str,
            platform: Optional[str] = None
    ) -> int:
        return self._request(f"/lol/champion-mastery/v4/scores/by-summoner/{summoner_id}", platform)
