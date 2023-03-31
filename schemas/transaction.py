import uuid
from typing import Optional

from schemas import (Model, ReadModel, WalletRead,
                     CategoryRead)


class TransactionBase(Model):
    amount: float
    description: Optional[str]


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class TransactionRead(TransactionBase, ReadModel):
    amount: Optional[float]
    wallet_id: Optional[uuid.UUID]
    category_id: Optional[uuid.UUID]

    wallet: Optional[WalletRead]
    category: Optional[CategoryRead]
