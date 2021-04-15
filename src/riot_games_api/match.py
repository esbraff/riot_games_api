from typing import Optional

from .base import RiotGamesApiBase
from .models.match import MatchDto, MatchlistDto, MatchTimelineDto


class MatchApiV4(RiotGamesApiBase):
    def get_match(
            self,
            match_id: int,
            platform: Optional[str] = None
    ) -> MatchDto:
        data = self._request(f"/lol/match/v4/matches/{match_id}", platform)

        return MatchDto.parse_obj(data)

    def get_matchlists(
            self,
            account_id: str,
            platform: Optional[str] = None,
            *,
            champion: Optional[list[int]] = None,
            queue: Optional[list[int]] = None,
            season: Optional[list[int]] = None,
            end_time: Optional[int] = None,
            begin_time: Optional[int] = None,
            end_index: Optional[int] = None,
            begin_index: Optional[int] = None
    ) -> MatchlistDto:
        params = {
            "champion": champion,
            "queue": queue,
            "season": season,
            "endTime": end_time,
            "beginTime": begin_time,
            "endIndex": end_index,
            "beginIndex": begin_index
        }

        data = self._request(f"/lol/match/v4/matchlists/by-account/{account_id}", platform, params)

        return MatchlistDto.parse_obj(data)

    def get_match_timelines(
            self,
            match_id: int,
            platform: Optional[str] = None
    ) -> MatchTimelineDto:
        data = self._request(f"/lol/match/v4/timelines/by-match/{match_id}", platform)

        return MatchTimelineDto.parse_obj(data)

    def get_match_ids_by_tournament_code(
            self,
            tournament_code: str,
            platform: Optional[str] = None
    ) -> list[int]:
        return self._request(f"/lol/match/v4/matches/by-tournament-code/{tournament_code}/ids", platform)

    def get_match_by_tournament_code(
            self,
            match_id: int,
            tournament_code: str,
            platform: Optional[str] = None
    ) -> MatchDto:
        data = self._request(f"/lol/match/v4/matches/{match_id}/by-tournament-code/{tournament_code}", platform)

        return MatchDto.parse_obj(data)
