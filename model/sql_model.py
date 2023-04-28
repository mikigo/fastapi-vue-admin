#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class User(SQLModel, table=True):
    """用户的数据库表"""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    nickname: str
    hashed_password: str
    sex: Optional[str] = None
    age: Optional[int] = None
    disabled: bool = True
