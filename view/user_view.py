#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from fastapi import Depends, HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import create_engine
from sqlmodel import select

import settings
from model.sql_model import User

engine = create_engine(settings.SQLITE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_user(user: User):
    exsit_users = select_user()
    with Session(engine) as session:
        if exsit_users:
            for e_user in exsit_users:
                if user.name == e_user.name:
                    return False
        user.hashed_password = "fakehashed" + user.hashed_password
        session.add(user)
        session.commit()
        session.refresh(user)
    return True


def select_user(name: str = None):
    with Session(engine) as session:
        if name:
            statement = select(User).where(User.name == name)
            res = session.exec(statement).one_or_none()
            return res
        else:
            statement = select(User)
            res = session.exec(statement).all()
            return res


def update_user(user: User):
    with Session(engine) as session:
        statement = select(User).where(User.name == user.name)
        res = session.exec(statement).one_or_none()
        if not res:
            return False
        res.age = user.age
        res.hashed_password = "fakehashed" + user.hashed_password
        res.nickname = user.nickname
        res.disabled = user.disabled
        session.add(res)
        session.commit()
        session.refresh(res)
    return True


def delete_user(name: str):
    with Session(engine) as session:
        statement = select(User).where(User.name == name)
        res = session.exec(statement).one_or_none()
        if not res:
            return False
        session.delete(res)
        session.commit()
        return True


# Oauth2 认证
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")


def fake_hash_password(password: str):
    return f"fakehashed{password}"


def fake_decode_token(token: str):
    user = select_user(token)
    return user


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="未激活的用户！"
        )
    return current_user
