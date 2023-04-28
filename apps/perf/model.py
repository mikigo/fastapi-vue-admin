#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from typing import Optional

from sqlmodel import Field
from sqlmodel import DateTime
from sqlmodel import Text
from sqlmodel import ForeignKey
from sqlmodel import SQLModel


# class UserSchema(SQLModel, table=True):
#     """用户的数据库表"""
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     nickname: str
#     hashed_password: str
#     sex: Optional[str] = None
#     age: Optional[int] = None
#     disabled: bool = True

class Base(SQLModel):
    create_time: DateTime
    update: DateTime


class AppName(Base):
    "应用表"
    id: Optional[int] = Field(default=None, primary_key=True)
    app_name: str
    package: str
    description: Text


class Framework(Base):
    """架构表"""
    id: Optional[int] = Field(default=None, primary_key=True)
    platform: str
    description: Text


class Scene(Base):
    id: Optional[int] = Field(default=None, primary_key=True)
    app_name: ForeignKey(AppName)
    frame_work: ForeignKey(Framework)
    scene: str
    description: Text
    is_online: bool


class PerfData(Base):
    id: Optional[int] = Field(default=None, primary_key=True)
    app_name: ForeignKey(AppName)
    frame_work: ForeignKey(Framework)
    scene: ForeignKey(Scene)
    number: int
    test_time: DateTime
    report_url: str


class TestApplicationVersion(Base):
    id: Optional[int] = Field(default=None, primary_key=True)
    app_name: ForeignKey(AppName)
    frame_work: ForeignKey(Framework)
    version: str
    test_time: DateTime


class PerfDataDay(Base):
    id: Optional[int] = Field(default=None, primary_key=True)
    app_name: ForeignKey(AppName)
    frame_work: ForeignKey(Framework)
    scene: ForeignKey(Scene)
    time_consume: float
    test_time: DateTime


class TemporaryTable(PerfData):
    """临时表"""
