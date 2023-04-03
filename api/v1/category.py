import uuid
from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from core import get_db
from schemas import (CategoryRead,
                     CategoryUpdate, CategoryCreate)
from services import category_service

router = APIRouter(prefix="/category", tags=["Categories"], dependencies=[Depends(HTTPBearer())])


@router.get("", dependencies=[Depends(HTTPBearer())], response_model=List[CategoryRead],
            summary="Get all Category")
async def get_all(*,
          db: Session = Depends(get_db),
          Authorize: AuthJWT = Depends(),
          skip: int = 0,
          limit: int = 10
    ):
    """
        Get all Category

       - **skip**: int - The number of Category to skip before returning the results. This parameter is optional and defaults to 0.
       - **limit**: int - The maximum number of Category to return in the response. This parameter is optional and defaults to 10.
    """
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    return category_service.get_all_by_user_id(db, user_id, skip, limit)


@router.get('/{id}/', dependencies=[Depends(HTTPBearer())],
            response_model=CategoryRead,
            summary="Get Category by id")
async def get_by_id(*,
        db: Session = Depends(get_db),
        id: uuid.UUID,
        Authorize: AuthJWT = Depends()
    ):
    """
        Get Category by id

        - **id**: UUID - required
    """
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    return category_service.get_by_user_id(db, user_id, id)


@router.post("", status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(HTTPBearer())],
             response_model=CategoryRead,
             summary="Create Category")
async def create(*,
         db: Session = Depends(get_db),
         body: CategoryCreate,
         Authorize: AuthJWT = Depends(),
    ):
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    return category_service.create_category(db, user_id, body)


@router.patch("/{id}/", status_code=status.HTTP_202_ACCEPTED,
              dependencies=[Depends(HTTPBearer())],
              response_model=CategoryRead,
              summary="Update Category")
async def update_category_patch(*,
        db: Session = Depends(get_db),
        id: uuid.UUID,
        body: CategoryUpdate,
        Authorize: AuthJWT = Depends()
    ):
    """
        Update Category

        - **id**: UUID - id of the Category.
        - **type**: str - required
        - **name**: str - required
    """
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    return category_service.update_category(db, id, user_id, body)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(HTTPBearer())],
               summary="Delete Category")
async def delete(*,
        db: Session = Depends(get_db),
        id: uuid.UUID,
        Authorize: AuthJWT = Depends()
    ):
    """
        Delete Category

        - **id**: UUID - id of the Category.
    """
    Authorize.jwt_required()
    return category_service.remove(db, id)
