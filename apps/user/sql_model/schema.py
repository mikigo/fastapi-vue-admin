#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    name: str
    nickname: str
    sex: str
    age: int
    disabled: bool


class UserCreate(UserBase):
    hashed_password: str


class UserSchema(UserBase):
    class Config:
        orm_mode = True
