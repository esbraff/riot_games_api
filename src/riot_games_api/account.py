from typing import Optional

from .models.account import AccountDto
from .base import RiotGamesApiBase


class AccountApiV1(RiotGamesApiBase):
    def get_account_by_puuid(
            self,
            puuid: str,
            platform: Optional[str]
    ) -> AccountDto:
        data = self._request(f"/riot/account/v1/accounts/by-puuid/{puuid}", platform)

        return AccountDto.parse_obj(data)

    def get_account_by_riot_id(
            self,
            game_name: str,
            tag_line: str,
            platform: Optional[str] = None
    ) -> AccountDto:
        data = self._request(f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}", platform)

        return AccountDto.parse_obj(data)

    def get_account_by_game_and_puuid(
            self,
            game: str,
            puuid: str,
            platform: Optional[str] = None
    ) -> AccountDto:
        data = self._request(f"/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}", platform)

        return AccountDto.parse_obj(data)
