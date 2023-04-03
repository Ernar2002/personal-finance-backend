from typing import List

from sqlalchemy.orm import Session

from exceptions import NotFoundException
from models import Category
from schemas import (CategoryCreate, CategoryUpdate, CategoryRead)
from services import user_service
from .base import ServiceBase


class CategoryService(ServiceBase[Category, CategoryCreate, CategoryUpdate]):

    def get_all_by_user_id(self,
                           db: Session,
                           user_id: str,
                           skip: int = 0,
                           limit: int = 10
    ) -> List[Category]:
        return db.query(self.model).filter(
            self.model.user_id == user_id
        ).offset(skip).limit(limit).all()

    def get_by_user_id(self, db: Session, user_id: str, id: str):
        return self._get_by_user_id(db, user_id, id)

    def create_category(self,
                        db: Session,
                        user_id: str,
                        body: CategoryCreate
                        ) -> Category:
        user = user_service.get_by_id(db, user_id)

        category = Category(
            name=body.name,
            type=body.type,
            user_id=user.id
        )

        db.add(category)
        db.flush()

        return category

    def update_category(self,
                        db: Session,
                        id: str,
                        user_id: str,
                        body: CategoryUpdate,
                        ):
        category = self._get_by_user_id(db, user_id, id)

        if body.type is not None:
            category.type = body.type
        if body.name is not None:
            category.name = body.name

        db.add(category)
        db.flush()

        return category

    def delete_by_user_id(self,
                          db: Session,
                          user_id: str,
                          id: str):
        self._get_by_user_id(db, user_id, id)

        return super().remove(db, id)

    def _get_by_user_id(self,
                        db: Session,
                        user_id: str,
                        id: str):
        user_service.get_by_id(db, user_id)

        category = db.query(self.model).filter(
            self.model.user_id == user_id,
            self.model.id == id
        ).first()

        if category is None:
            raise NotFoundException(detail=f"Category with id: {id} is not found")

        return category


category_service = CategoryService(Category)
