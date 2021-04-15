from requests import Session, RequestException
from typing import Optional, Any, Dict
from urllib.parse import urljoin

from .exceptions import RiotGamesApiException
from .context import RiotGamesApiContext


class RiotGamesApiBase:
    def __init__(
            self,
            ctx: RiotGamesApiContext,
            session: Optional[Session] = None
    ):
        self._ctx = ctx
        self._session = session or Session()
    
    def _request(
            self,
            path: str,
            platform: Optional[str] = None,
            params: Optional[Dict[str, Any]] = None
    ):
        try:
            headers = {
                "X-Riot-Token": self._ctx.token
            }
            base_url = self._ctx.get_base_url(platform)

            response = self._session.request(
                "GET",
                urljoin(base_url, path),
                headers=headers,
                params=params
            )
            response.raise_for_status()

            return response.json()
        except RequestException as e:
            raise RiotGamesApiException from e
