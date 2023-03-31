from sqlalchemy import Column, UUID, ForeignKey, TEXT, Float
from sqlalchemy.orm import relationship

from core import Base
from models import Model


class Transaction(Model, Base):

    __tablename__ = "transactions"

    amount = Column(Float, nullable=False)
    description = Column(TEXT, nullable=True)
    wallet_id = Column(UUID(as_uuid=True), ForeignKey("wallets.id"), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=False)

    wallet = relationship("Wallet", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
