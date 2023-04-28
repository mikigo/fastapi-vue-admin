#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
:Author: mikigo
:Date: 2022/11/19 上午9:47
:Desc:
"""
from passlib.context import CryptContext

from apps.user.model import UserModel
from apps.user.schema import UserCreate, UserInDB

from sqlalchemy.orm import Session


def get_users(db: Session, user_id: int = None):
    if user_id:
        return db.query(UserModel).filter(UserModel.id == user_id).one_or_none()
    return db.query(UserModel).all()


# openssl rand -hex 32
SECRET_KEY = "82e17f299b6f5e3bda7a56d6c262a61d7b11bb3deefee2b8be9c6054c6d71497"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_user(db: Session, user: UserCreate):
    users = db.query(UserModel)
    user_obj = users.filter(UserModel.name == user.name).one_or_none()
    if user_obj:
        return False
    user.hashed_password = get_password_hash(user.hashed_password)
    print(user)
    db.add(user)
    db.commit()
    return True


if __name__ == '__main__':
    from db import SessionLocal

    db = SessionLocal()
    user = create_user(
        UserCreate(**
                   {
                       "id": 3,
                       "name": "feelgood",
                       "nickname": "feelgood",
                       "hashed_password": "123456",
                       "sex": "mail",
                       "age": 30,
                       "disabled": False,
                   }
                   ),
        db
    )
    print(user)
    db.close()
