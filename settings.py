#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
import secrets
from os import popen
from os.path import abspath
from os.path import dirname
from os.path import join
from typing import List

from pydantic import AnyHttpUrl

# ==================== PROJECT SETTING ====================
# Debug 模式开启


DEBUG = True
# 应用名称
APP_NAME = "FeelGood"
# 应用版本
VERSION = "V1"
# 根目录绝对路径
ROOT_DIR = dirname(abspath(__file__))

# 使用模板引擎，挂载静态文件目录
TEMPLATE = "static"
# API 文档用户界面描述
DESC = f"""
![]({TEMPLATE}/logo.png)
```shell
Version: {VERSION}
Author : mikigo
```
"""
# 静态文件目录绝对路径
STATIC_PATH = join(ROOT_DIR, TEMPLATE)

# ======================= DB SETTING =======================
DB_URL = f"sqlite:///{STATIC_PATH}/feelgood.db"

# ====================== HOST SETTING ======================
# Debug模式开启使用127.0.0.1，Debug模式关闭正式环境，使用真实IP
IP = popen("hostname -I").read().split(" ")[0] if not DEBUG else "127.0.0.1"
# 端口
PORT = 8000
# 热重载
RELOAD = True
# openssl rand -hex 32 随机生成
SECRET_KEY = secrets.token_urlsafe(32)
# token过期时间
ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60
# 跨域白名单
BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [f"http://localhost:{PORT}"]

# Oauth2的API
API_V1_STR: str = "/api/v1"
# 超级用户
FIRST_SUPERUSER = "admin"
FIRST_SUPERUSER_PASSWORD = "admin"
# JWT编码算法
ALGORITHM = "HS256"
