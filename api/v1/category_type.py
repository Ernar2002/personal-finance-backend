from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT

from models import CategoryTypeEnum

router = APIRouter(prefix="/category_type", tags=["CategoryType"], dependencies=[Depends(HTTPBearer())])


@router.get("", dependencies=[Depends(HTTPBearer())],
            summary="Get all CategoryType")
async def get_all(*,
    Authorize: AuthJWT = Depends()
):
    """
        Get all CategoryType
    """
    Authorize.jwt_required()
    return [ag.value for ag in CategoryTypeEnum]
