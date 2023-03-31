from pydantic import BaseModel, EmailStr

from .user import UserBase


class LoginForm(BaseModel):
    email: EmailStr
    password: str


class RegistrationForm(UserBase):
    password: str
    re_password: str
