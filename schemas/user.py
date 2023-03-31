from typing import Optional

from schemas import Model, ReadModel


class UserBase(Model):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserRead(UserBase, ReadModel):
    email: Optional[str]
    username: Optional[str]
