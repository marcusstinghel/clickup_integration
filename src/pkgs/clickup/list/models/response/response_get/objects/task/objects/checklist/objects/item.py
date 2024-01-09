from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(default=None, alias='name')
