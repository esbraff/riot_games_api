from pydantic import BaseModel as PydanticBaseModel
from humps.camel import case as camelcase


class BaseModel(PydanticBaseModel):
    class Config:
        alias_generator = camelcase
        allow_population_by_field_name = True
