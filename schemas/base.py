import datetime
import uuid
from typing import Optional

from pydantic import BaseModel


class Model(BaseModel):
    pass


class NamedModel(Model):
    name: str


class ReadModel(Model):
    id: Optional[uuid.UUID]
    created_at: Optional[datetime.date]
    updated_at: Optional[datetime.date]

    class Config:
        orm_mode = True


class ReadNamedModel(ReadModel, NamedModel):
    name: Optional[str]
