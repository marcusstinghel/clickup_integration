from pydantic import BaseModel, Field


class Assignee(BaseModel):
    username: str = Field(default=None, alias='username')
