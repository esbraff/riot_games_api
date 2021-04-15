from typing import Optional, List

from pydantic import parse_obj_as

from .base import RiotGamesApiBase
from .models.league import LeagueListDto, LeagueEntryDto


class LeagueApiV4(RiotGamesApiBase):
    def get_challenger_queues(
            self,
            queue: str,
            platform: Optional[str] = None
    ) -> LeagueListDto:
        data = self._request(f"/lol/league/v4/challengerleagues/by-queue/{queue}", platform)

        return LeagueListDto.parse_obj(data)

    def get_grandmaster_queues(
            self,
            queue: str,
            platform: Optional[str] = None
    ) -> LeagueListDto:
        data = self._request(f"/lol/league/v4/grandmasterleagues/by-queue/{queue}", platform)

        return LeagueListDto.parse_obj(data)

    def get_master_queues(
            self,
            queue: str,
            platform: Optional[str] = None
    ) -> LeagueListDto:
        data = self._request(f"/lol/league/v4/masterleagues/by-queue/{queue}", platform)

        return LeagueListDto.parse_obj(data)

    def get_leagues(
            self,
            league_id: str,
            platform: Optional[str] = None
    ) -> LeagueListDto:
        data = self._request(f"/lol/league/v4/leagues/{league_id}", platform)

        return LeagueListDto.parse_obj(data)

    def get_entries_by_summoner_id(
            self,
            summoner_id: str,
            platform: Optional[str] = None
    ) -> List[LeagueEntryDto]:
        data = self._request(f"/lol/league/v4/entries/by-summoner/{summoner_id}", platform)

        return parse_obj_as(List[LeagueEntryDto], data)

    def get_entries(
            self,
            queue: str,
            tier: str,
            division: str,
            platform: Optional[str] = None
    ) -> List[LeagueEntryDto]:
        data = self._request(f"/lol/league/v4/entries/{queue}/{tier}/{division}", platform)

        return parse_obj_as(List[LeagueEntryDto], data)
