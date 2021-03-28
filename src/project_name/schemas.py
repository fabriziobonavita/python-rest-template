from datetime import datetime

from pydantic import BaseModel


class EntityBase(BaseModel):
    id: int
    created_at: datetime
    modified_at: datetime
