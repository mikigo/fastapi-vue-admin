from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    nickname: str
    hashed_password: str
    sex: Optional[str] = None
    age: Optional[int] = None
    disabled: bool = True
