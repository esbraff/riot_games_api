from typing import Optional

from pydantic import parse_obj_as

from .models.clash import PlayerDto, TeamDto, TournamentDto
from .base import RiotGamesApiBase


class ClashApiV1(RiotGamesApiBase):
    def get_clash_teams(
            self,
            summoner_id: str,
            platform: Optional[str] = None
    ) -> list[PlayerDto]:
        data = self._request(f"/lol/clash/v1/players/by-summoner/{summoner_id}", platform)

        return parse_obj_as(list[PlayerDto], data)

    def get_team(
            self,
            team_id: str,
            platform: Optional[str] = None
    ) -> TeamDto:
        data = self._request(f"/lol/clash/v1/teams/{team_id}", platform)

        return TeamDto.parse_obj(data)

    def get_tournaments(
            self,
            platform: Optional[str] = None
    ) -> list[TournamentDto]:
        data = self._request(f"/lol/clash/v1/tournaments", platform)

        return parse_obj_as(list[TournamentDto], data)

    def get_tournament_by_team(
            self,
            team_id: str,
            platform: Optional[str] = None
    ) -> TournamentDto:
        data = self._request(f"/lol/clash/v1/tournaments/by-team/{team_id}", platform)

        return TournamentDto.parse_obj(data)

    def get_tournament(
            self,
            tournament_id: int,
            platform: Optional[str] = None
    ) -> TournamentDto:
        data = self._request(f"/lol/clash/v1/tournaments/{tournament_id}", platform)

        return TournamentDto.parse_obj(data)
