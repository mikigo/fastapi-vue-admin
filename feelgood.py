#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import settings
from apps.hello import hello
from apps.user.router.user import user_router

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESC,
    redoc_url=None,
)

if settings.TEMPLATE:
    app.mount(
        f"/{settings.TEMPLATE}",
        StaticFiles(directory=settings.TEMPLATE),
        name=settings.TEMPLATE
    )

app.include_router(hello)
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run(
        app="feelgood:app",
        host=settings.IP,
        port=settings.PORT,
        reload=settings.RELOAD
    )
