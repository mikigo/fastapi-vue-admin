from typing import List, Union
from pydantic import BaseModel


# ========== item的Pydantic模型 ============
# models里面的Item也有title和description属性
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


# 创建用于读取/返回的Pydantic模型/模式
class Item(ItemBase):
    id: int
    owner_id: int

    # 为 Pydantic 提供配置
    class Config:
        orm_mode = True


# ========== user的Pydantic模型 ============
# models里面的User也有email属性
class UserBase(BaseModel):
    email: str


# 在创建时有一个password属性
class UserCreate(UserBase):
    password: str


# 创建用于读取/返回的Pydantic模型/模式
# 读取用户（从 API 返回）时将使用不包括password的User Pydantic模型
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    # 为 Pydantic 提供配置
    class Config:
        # orm_mode将告诉 Pydantic模型读取数据，即它不是一个dict，而是一个 ORM 模型
        orm_mode = True
