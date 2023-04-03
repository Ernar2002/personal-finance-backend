from fastapi import APIRouter

from .auth import router as auth_router
from .category_type import router as category_type_router
from .category import router as category_router

router = APIRouter(prefix="/v1")

router.include_router(auth_router)
router.include_router(category_type_router)
router.include_router(category_router)
