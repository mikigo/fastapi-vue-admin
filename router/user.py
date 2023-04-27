from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from model.sql_model.model import User
from model.sql_model.model import create_user as _create_user
from model.sql_model.model import select_user as _select_user
from model.sql_model.model import update_user as _update_user
from model.sql_model.model import delete_user as _delete_user

user_router = APIRouter(prefix="/user", tags=["用户"])


@user_router.get("/query")
async def select_user(name: str = None):
    return {"data": _select_user(name=name)}


@user_router.post("/create")
async def create_user(user: User):
    status_code = _create_user(user)
    if status_code:
        return {"status_code": status.HTTP_200_OK}
    else:
        raise HTTPException(
            status_code=status.HTTP_201_CREATED,
            detail="用户已经存在！"
        )


@user_router.post("/update")
async def update_user(user: User):
    status_code = _update_user(user)
    if status_code:
        return {"status_code": status.HTTP_200_OK}
    else:
        raise HTTPException(
            status_code=status.HTTP_201_CREATED,
            detail="用户不存在，无法更新！"
        )


@user_router.post("/delete_user")
async def delete_user(name: str):
    status_code = _delete_user(name)
    if status_code:
        return {"status_code": status.HTTP_200_OK}
    else:
        raise HTTPException(
            status_code=status.HTTP_201_CREATED,
            detail="用户不存在，无法删除！"
        )
