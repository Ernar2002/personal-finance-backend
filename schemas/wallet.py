import uuid
from typing import Optional

from schemas import NamedModel, ReadNamedModel, UserRead


class WalletBase(NamedModel):
    balance: float


class WalletCreate(WalletBase):
    pass


class WalletUpdate(WalletBase):
    pass


class WalletRead(WalletBase, ReadNamedModel):
    balance: Optional[float]
    user_id: Optional[uuid.UUID]

    user: Optional[UserRead]
