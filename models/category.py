import enum

from sqlalchemy import Column, UUID, ForeignKey, Enum
from sqlalchemy.orm import relationship

from core import Base
from models import NamedModel


class CategoryTypeEnum(str, enum.Enum):
    INCOME = "Income"
    OUTCOME = "Outcome"


class Category(NamedModel, Base):

    __tablename__ = "categories"
    type = Column(Enum(CategoryTypeEnum), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="categories")
    transactions = relationship("Transaction", back_populates="category")
