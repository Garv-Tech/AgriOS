from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime


class CoreModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        frozen = True  # core truth must not mutate
