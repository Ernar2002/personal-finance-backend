from sqlalchemy import Column, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core import Base
from models import NamedModel


class Wallet(NamedModel, Base):

    __tablename__ = "wallets"

    balance = Column(Float, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="wallets", cascade="all, delete")
    transactions = relationship("Transaction", back_populates="wallet")
