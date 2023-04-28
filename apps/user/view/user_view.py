#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""

from apps.user.sql_model import model

from sqlalchemy.orm import Session


def get_users(db: Session, user_id: int = None):
    if user_id:
        return db.query(model.User).filter(model.User.id == user_id).one_or_none()
    return db.query(model.User).all()


if __name__ == '__main__':
    from db import SessionLocal

    db = SessionLocal()
    user = get_users(db)
    print(user)
