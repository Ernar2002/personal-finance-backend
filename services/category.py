from models import Category
from schemas import (CategoryCreate, CategoryUpdate)
from .base import ServiceBase


class CategoryService(ServiceBase[Category, CategoryCreate, CategoryUpdate]):
    pass


category_service = CategoryService(Category)
