from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: str = Field(..., min_length=10)

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    summary: str | None

    model_config = {
        "from_attributes": True
    }
