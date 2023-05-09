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

fadmin = APIRouter()

templates = Jinja2Templates(directory="static")


@fadmin.get("/admin")
async def admin(request: Request):
    return templates.TemplateResponse(
        "admin/index.html",
        {
            "request": request,
        }
    )
