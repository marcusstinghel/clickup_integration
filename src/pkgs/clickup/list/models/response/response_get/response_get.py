from pydantic import BaseModel, Field
from typing import List
from .objects import Task


class ResponseGet(BaseModel):
    tasks: List[Task] = Field(default=None, alias='tasks')
