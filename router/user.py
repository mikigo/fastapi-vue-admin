#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from model.sql_model import User
from view.user_view import ACCESS_TOKEN_EXPIRE_MINUTES
from view.user_view import oauth2_scheme
from view.user_view import Token
from view.user_view import authenticate_user
from view.user_view import create_access_token_by_jwt
from view.user_view import create_user as _create_user
from view.user_view import delete_user as _delete_user
from view.user_view import fake_hash_password
from view.user_view import get_current_active_user
from view.user_view import select_user as _select_user
from view.user_view import update_user as _update_user

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


@user_router.get("/oauth2_password_bearer")
async def get_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@user_router.post("/bearer/token")  # 地址和oauth2_scheme保持一致
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = _select_user(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名或密码不正确！"
        )
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名或密码不正确！"
        )

    return {"access_token": user.name, "token_type": "bearer"}


@user_router.post("/jwt/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码不正确！",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 令牌过期时间创建 timedelta 对象
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 创建并返回真正的 JWT 访问令牌
    access_token = create_access_token_by_jwt(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
