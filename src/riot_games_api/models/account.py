from typing import Optional

from .base import BaseModel


class AccountDto(BaseModel):
    puuid: str
    game_name: Optional[str]
    tag_line: Optional[str]
