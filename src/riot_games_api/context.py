from typing import Literal, Optional

from .exceptions import RiotGamesApiException


class RiotGamesApiContext:
    def __init__(self, token: str, default_platform: Optional[str]):
        self.token = token
        self.default_platform = default_platform

    def get_base_url(self, platform: Optional[str] = None):
        platform = platform or self.default_platform

        if platform is None:
            raise RiotGamesApiException from RuntimeError("platform must be specified")

        return f"https://{platform}.api.riotgames.com/"
