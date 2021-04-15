from typing import Optional

from .models.summoner import SummonerDto
from .base import RiotGamesApiBase


class SummonerApiV4(RiotGamesApiBase):
    def get_summoner_by_account_id(
            self,
            account_id: str,
            platform: Optional[str] = None
    ) -> SummonerDto:
        data = self._request(f"/lol/summoner/v4/summoners/by-account/{account_id}", platform)

        return SummonerDto.parse_obj(data)

    def get_summoner_by_name(
            self,
            summoner_name: str,
            platform: Optional[str] = None
    ) -> SummonerDto:
        data = self._request(f"/lol/summoner/v4/summoners/by-name/{summoner_name}", platform)

        return SummonerDto.parse_obj(data)

    def get_summoner_by_puuid(
            self,
            puuid: str,
            platform: Optional[str] = None
    ) -> SummonerDto:
        data = self._request(f"/lol/summoner/v4/summoners/by-puuid/{puuid}", platform)

        return SummonerDto.parse_obj(data)

    def get_summoner_by_summoner_id(
            self,
            summoner_id: str,
            platform: Optional[str] = None
    ) -> SummonerDto:
        data = self._request(f"/lol/summoner/v4/summoners/{summoner_id}", platform)

        return SummonerDto.parse_obj(data)
