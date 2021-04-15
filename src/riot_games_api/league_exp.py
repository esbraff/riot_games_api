from typing import Optional, List

from pydantic import parse_obj_as

from .models.league import LeagueEntryDto
from .base import RiotGamesApiBase


class LeagueExpApiV4(RiotGamesApiBase):
    def get_entries(
            self,
            queue: str,
            tier: str,
            division: str,
            platform: Optional[str] = None
    ) -> List[LeagueEntryDto]:
        data = self._request(f"/lol/league-exp/v4/entries/{queue}/{tier}/{division}", platform)

        return parse_obj_as(List[LeagueEntryDto], data)
