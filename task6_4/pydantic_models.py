from pydantic import BaseModel,Field


class TaskIn(BaseModel):
    title: str = Field(max_length=100)
    description: str = Field()
    done: bool = Field(None)

class TaskOut(TaskIn):
    id:int
