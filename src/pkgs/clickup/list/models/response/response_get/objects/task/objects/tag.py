from pydantic import BaseModel, Field


class Tag(BaseModel):
    name: str = Field(default=None, alias='name')
