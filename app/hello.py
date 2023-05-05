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
Hey! I'm Mikigo. Welcome to use {settings.APP_NAME} {settings.VERSION}.
"""

api_url = f"http://{settings.IP}:{settings.PORT}/docs"
admin_url = f"http://{settings.IP}:{settings.PORT}/admin"
about_url = "https://github.com/mikigo/feelgood"
background_img = "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA12rZ8k.img"


@hello.get("/")
async def say_hello(request: Request):
    return templates.TemplateResponse(
        "hello.html",
        {
            "request": request,
            "hi": hi,
            "api_url": api_url,
            "admin_url": admin_url,
            "about_url": about_url,
            "background_img": background_img,
        }
    )
