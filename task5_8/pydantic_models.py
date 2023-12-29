from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str