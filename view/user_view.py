#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from datetime import datetime
from datetime import timedelta
from typing import Union

from fastapi import Depends, HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import create_engine
from sqlmodel import select

import settings
from model.sql_model import User

engine = create_engine(settings.SQLITE_URL, echo=True)


def create_db_and_tables():
    """创建和生成数据库表"""
    SQLModel.metadata.create_all(engine)


def create_user(user: User):
    """创建用户"""
    exsit_users = select_user()
    with Session(engine) as session:
        if exsit_users:
            for e_user in exsit_users:
                if user.name == e_user.name:
                    return False
        user.hashed_password = get_password_hash(user.hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
    return True


def select_user(name: str = None):
    """查询用户"""
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
    """更新用户"""
    with Session(engine) as session:
        statement = select(User).where(User.name == user.name)
        res = session.exec(statement).one_or_none()
        if not res:
            return False
        res.age = user.age
        res.hashed_password = get_password_hash(user.hashed_password)
        res.nickname = user.nickname
        res.disabled = user.disabled
        session.add(res)
        session.commit()
        session.refresh(res)
    return True


def delete_user(name: str):
    """删除用户，暂时不做密码校验"""
    with Session(engine) as session:
        statement = select(User).where(User.name == name)
        res = session.exec(statement).one_or_none()
        if not res:
            return False
        # if not verify_password(password, res.hashed_password):
        #     return False
        session.delete(res)
        session.commit()
        return True


# Oauth2 认证
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/bearer/token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/jwt/token")


def fake_hash_password(password: str):
    return f"fakehashed{password}"


def fake_decode_token(token: str):
    user = select_user(token)
    return user


def get_current_user_by_bearer(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_active_user(current_user: User = Depends(get_current_user_by_bearer)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="未激活的用户！"
        )
    return current_user


# 密码哈希,使用bcrypt算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """校验密码"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """密码哈希"""
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    """用户&密码传进来，进行验证"""
    user = select_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# 处理 JWT 令牌
#
# 1、生成秘钥
# openssl rand -hex 32
SECRET_KEY = "a616ffdea6ab6fe6e2424d3e46509d1bde2ba2ba078c1408fb0e3341e8c50dcf"
# JWT 令牌签名算法
ALGORITHM = "HS256"
# 令牌过期时间（分钟）
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    "定义token模型"
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


def create_access_token_by_jwt(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    生成新的访问令牌
    传进来的参数加上时间戳，最后生成令牌
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user_by_jwt(token: str = Depends(oauth2_scheme)):
    """获取当前用户"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = select_user(name=token_data.username)
    if user is None:
        raise credentials_exception
    return user


if __name__ == '__main__':
    update_user(
        User(
            name="admin",
            nickname="admin",
            hashed_password="admin",
            sex="mail",
            age="19",
            disabled=False,
        )
    )
