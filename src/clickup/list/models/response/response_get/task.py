from pydantic import BaseModel, Field


class Task(BaseModel):
    id: str = Field(default=None, alias='id')
