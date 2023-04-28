#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from os import popen
from os.path import abspath
from os.path import dirname
from os.path import join
from datetime import datetime

# ==================== PROJECT SETTING ====================
# Debug 模式开启
DEBUG = True
# 应用名称
APP_NAME = "FeelGood"
# 应用版本
VERSION = "0.1"
# 根目录绝对路径
ROOT_DIR = dirname(abspath(__file__))
# router目录绝对路径
ROUTER_PATH = join(ROOT_DIR, "router")

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
SQL_FILE_NAME = "feelgood.db"
SQL_URL = f"sqlite:///{STATIC_PATH}/{SQL_FILE_NAME}"

# ====================== HOST SETTING ======================
# Debug模式开启说明是在开发环境，使用127.0.0.1，Debug模式关闭正式环境，使用真实IP
IP = popen("hostname -I").read().split(" ")[0] if not DEBUG else "127.0.0.1"
# 端口
PORT = 8000
# 热重载
RELOAD = True
