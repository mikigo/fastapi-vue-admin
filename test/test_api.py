#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from feelgood import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
