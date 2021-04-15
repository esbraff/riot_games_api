from typing import Optional, Literal

from requests import Session

from .context import RiotGamesApiContext
from .summoner import SummonerApiV4
from .champion import ChampionApiV3
from .match import MatchApiV4
from .clash import ClashApiV1
from .account import AccountApiV1
from .champion_mastery import ChampionMasteryApiV4
from .spectator import SpectatorApiV4
from .lol_status import LolStatusApiV4
from .league import LeagueApiV4
from .league_exp import LeagueExpApiV4


class RiotGamesApi:
    def __init__(self, token: str, default_platform: Optional[str] = None):
        self._ctx = RiotGamesApiContext(token, default_platform)
        self._session = Session()
        self.summoner = SummonerApiV4(self._ctx, self._session)
        self.champion = ChampionApiV3(self._ctx, self._session)
        self.match = MatchApiV4(self._ctx, self._session)
        self.clash = ClashApiV1(self._ctx, self._session)
        self.account = AccountApiV1(self._ctx, self._session)
        self.champion_mastery = ChampionMasteryApiV4(self._ctx, self._session)
        self.spectator = SpectatorApiV4(self._ctx, self._session)
        self.lol_status = LolStatusApiV4(self._ctx, self._session)
        self.league = LeagueApiV4(self._ctx, self._session)
        self.league_exp = LeagueExpApiV4(self._ctx, self._session)

    def set_default_platform(self, platform: str):
        self._ctx.default_platform = platform
