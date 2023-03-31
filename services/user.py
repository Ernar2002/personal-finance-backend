from sqlalchemy.orm import Session

from models import User
from schemas import (UserCreate, UserUpdate)
from .base import ServiceBase


class UserService(ServiceBase[User, UserCreate, UserUpdate]):

    def get_by_email(self, db: Session, email: str):

        user = db.query(self.model).filter(User.email == email).first()

        return user


user_service = UserService(User)
