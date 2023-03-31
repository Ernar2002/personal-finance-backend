import uuid
from typing import Optional

from models import CategoryTypeEnum
from schemas import (NamedModel, ReadNamedModel, WalletRead,
                     UserRead)


class CategoryBase(NamedModel):
    type: CategoryTypeEnum


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryRead(CategoryBase, ReadNamedModel):
    type: Optional[CategoryTypeEnum]
    user_id: Optional[uuid.UUID]

    user: Optional[UserRead]
