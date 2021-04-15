from typing import Optional

from .base import RiotGamesApiBase
from .models.lol_status import PlatformDataDto


class LolStatusApiV4(RiotGamesApiBase):
    def get_status(
            self,
            platform: Optional[str] = None
    ) -> PlatformDataDto:
        data = self._request(f"/lol/status/v4/platform-data", platform)

        return PlatformDataDto.parse_obj(data)
