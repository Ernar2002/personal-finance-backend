from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from core import Base
from models import Model


class User(Model, Base):

    __tablename__ = "users"

    email = Column(String(150), nullable=True, unique=True)
    password = Column(String(255), nullable=False)
    username = Column(String(20), nullable=True)

    wallets = relationship("Wallet", back_populates="user")
    categories = relationship("Category", back_populates="user")
