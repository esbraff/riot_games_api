from typing import List

from .base import BaseModel


class ContentDto(BaseModel):
    locale: str
    content: str


class UpdateDto(BaseModel):
    id: int
    author: str
    publish: bool
    publish_locations: List[str]
    translations: List[ContentDto]
    created_at: str
    updated_at: str


class StatusDto(BaseModel):
    id: int
    maintenance_status: str
    incident_severity: str
    titles: List[ContentDto]
    updates: List[UpdateDto]
    created_at: str
    archive_at: str
    updated_at: str
    platforms: List[str]


class PlatformDataDto(BaseModel):
    id: str
    name: str
    locales: List[str]
    maintances: List[StatusDto]
    incidents: List[StatusDto]
