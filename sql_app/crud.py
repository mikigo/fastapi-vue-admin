from sqlalchemy.orm import Session
# 导入SQLAlchemy模型和Pydantic模型
from . import models, schemas

def get_user(db: Session, user_id: int):
    """通过ID查询用户"""
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """通过email查询用户"""
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """获取所有用户"""
    return db.query(models.User).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    """获取所有项目"""
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    """创建用户"""
    fake_hashed_password = user.password + "notreallyhashed"
    # 获取数据库模型实例
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # add方法添加数据
    db.add(db_user)
    # 提交
    db.commit()
    # 刷新
    db.refresh(db_user)
    return db_user

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item