#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
import typing
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from apps.user.view import get_users as _get_users
from apps.user.view import create_user as _create_user
from apps.user.schema import UserSchema
from apps.user.schema import UserCreate
from db import get_db

user_router = APIRouter(prefix="/user", tags=["用户"])


@user_router.get("/get_user", response_model=typing.List[UserSchema])
async def get_users(db: Session = Depends(get_db), user_id: int = None):
    users = _get_users(db, user_id=user_id)
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="未获取到用户！"
        )
    return users


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")


@user_router.post("/create_user", response_model=UserSchema)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    create_status = _create_user(db, user)
    if not create_status:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="创建用户失败！"
        )
    return user
