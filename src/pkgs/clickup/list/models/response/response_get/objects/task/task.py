from pydantic import BaseModel, Field
from typing import List, Optional
from .objects import Status, Assignee, Tag, Checklist


class Task(BaseModel):
    id: str = Field(default=None, alias='id')
    name: str = Field(default=None, alias='name')
    status: Status = Field(default=None, alias='status')
    assignees: List[Assignee] = Field(default=None, alias='assignees')
    tags: List[Tag] = Field(default=None, alias='tags')
    start_date: Optional[str] = Field(default=None, alias='start_date')
    due_date: Optional[str] = Field(default=None, alias='due_date')
    date_closed: Optional[str] = Field(default=None, alias='date_closed')
    checklists: List[Checklist] = Field(default=None, alias='checklists')
