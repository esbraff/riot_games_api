from typing import Optional

from .base import RiotGamesApiBase
from .models.champion import ChampionInfo


class ChampionApiV3(RiotGamesApiBase):
    def champion_rotations(
            self,
            platform: Optional[str] = None
    ) -> ChampionInfo:
        data = self._request("/lol/platform/v3/champion-rotations", platform)

        return ChampionInfo.parse_obj(data)
