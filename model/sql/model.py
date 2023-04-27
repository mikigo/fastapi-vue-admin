from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import create_engine
from sqlmodel import select

import settings

engine = create_engine(settings.SQLITE_URL, echo=True)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    nickname: str
    hashed_password: str
    sex: Optional[str] = None
    age: Optional[int] = None
    disabled: bool = True


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_user(user: User):
    exsit_users = select_user()
    with Session(engine) as session:
        if exsit_users:
            for e_user in exsit_users:
                if user.name == e_user.name:
                    return False
        user.hashed_password = "fakehashed" + user.hashed_password
        session.add(user)
        session.commit()
        session.refresh(user)
    return True


def select_user(name: str = None):
    with Session(engine) as session:
        if name:
            statement = select(User).where(User.name == name)
            res = session.exec(statement).one_or_none()
            return res
        else:
            statement = select(User)
            res = session.exec(statement).all()
            return res


def update_user(user: User):
    with Session(engine) as session:
        statement = select(User).where(User.name == user.name)
        res = session.exec(statement).one_or_none()
        if not res:
            return False
        res.age = user.age
        res.hashed_password = "fakehashed" + user.hashed_password
        res.nickname = user.nickname
        res.disabled = user.disabled
        session.add(res)
        session.commit()
        session.refresh(res)
    return True


def delete_user(name: str):
    with Session(engine) as session:
        statement = select(User).where(User.name == name)
        res = session.exec(statement).one_or_none()
        if not res:
            return False
        session.delete(res)
        session.commit()
        return True


# if __name__ == '__main__':
    # create_db_and_tables()
    # create_user(
    # update_user(
    #     User(
    #         name="mikigo",
    #         nickname="mikigo",
    #         hashed_password="123456",
    #         sex="mail",
    #         age="20",
    #         disabled=False,
    #
    #     )
    # )
    # select_user()
    # delete_user("http")
