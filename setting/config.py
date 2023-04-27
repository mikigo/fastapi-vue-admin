from os import popen
from os.path import abspath
from os.path import dirname
from os.path import join


class _Config:
    DEBUG = True
    APP_NAME = "FeelGood"
    VERSION = "0.1"
    ROOT_DIR = dirname(dirname(abspath(__file__)))
    SETTING_PATH = join(ROOT_DIR, "setting")
    ROUTER_PATH = join(ROOT_DIR, "router")
    STATIC_PATH = join(ROOT_DIR, "static")

    SQLITE_FILE_NAME = "feelgood.db"
    SQLITE_URL = f"sqlite:///{STATIC_PATH}/{SQLITE_FILE_NAME}"

    IP = popen("hostname -I").read().split(" ")[0]
    PORT = 5000
    RELOAD = True


config = _Config()
