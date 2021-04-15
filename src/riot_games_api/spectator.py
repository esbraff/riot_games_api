from typing import Optional

from .base import RiotGamesApiBase
from .models.spectator import CurrentGameInfo


class SpectatorApiV4(RiotGamesApiBase):
    def get_current_game(
            self,
            summoner_id: str,
            platform: Optional[str] = None
    ) -> CurrentGameInfo:
        data = self._request(f"/lol/spectator/v4/active-games/by-summoner/{summoner_id}", platform)

        return CurrentGameInfo.parse_obj(data)
