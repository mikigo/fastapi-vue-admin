#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from typing import Union

from pydantic import BaseModel


class Base(BaseModel):
    id: int
    name: str
    nickname: str
    sex: str
    age: int
    disabled: bool


class UserCreate(Base):
    hashed_password: str


class UserSchema(Base):
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserInDB(UserSchema):
    hashed_password: str
