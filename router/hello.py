#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from fastapi import APIRouter

hello = APIRouter()


@hello.get("/")
async def sayhello():
    return {"msg": "Hello FeelGood! "}
