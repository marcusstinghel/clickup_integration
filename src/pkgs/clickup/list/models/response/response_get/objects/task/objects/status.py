from pydantic import BaseModel, Field


class Status(BaseModel):
    name: str = Field(default=None, alias='status')
