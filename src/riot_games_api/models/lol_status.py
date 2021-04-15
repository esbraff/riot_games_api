from .base import BaseModel


class ContentDto(BaseModel):
    locale: str
    content: str


class UpdateDto(BaseModel):
    id: int
    author: str
    publish: bool
    publish_locations: list[str]
    translations: list[ContentDto]
    created_at: str
    updated_at: str


class StatusDto(BaseModel):
    id: int
    maintenance_status: str
    incident_severity: str
    titles: list[ContentDto]
    updates: list[UpdateDto]
    created_at: str
    archive_at: str
    updated_at: str
    platforms: list[str]


class PlatformDataDto(BaseModel):
    id: str
    name: str
    locales: list[str]
    maintances: list[StatusDto]
    incidents: list[StatusDto]
