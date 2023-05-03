#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

import settings

hello = APIRouter()

templates = Jinja2Templates(directory="static")

hi = f"""
Hey! I'm Mikigo.Welcome to use {settings.APP_NAME}.
"""

api_url = f"http://{settings.IP}:{settings.PORT}/docs"


@hello.get("/")
async def say_hello(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "hi": hi,
            "api_url": api_url,
        }
    )
