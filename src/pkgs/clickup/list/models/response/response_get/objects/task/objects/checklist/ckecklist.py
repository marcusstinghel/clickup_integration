from pydantic import BaseModel, Field
from typing import List
from .objects import Item


class Checklist(BaseModel):
    name: str = Field(default=None, alias='name')
    items: List[Item] = Field(default=None, alias='objects')
