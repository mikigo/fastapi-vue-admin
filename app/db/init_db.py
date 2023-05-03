from sqlalchemy.orm import Session

import settings
from app import crud, schemas
from app.db import base  # noqa: F401


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841


if __name__ == '__main__':
    # from app.db.base_class import Base
    # from app.db.session import engine
    # Base.metadata.create_all(bind=engine)

    from app.crud.crud_user import CRUDUser
    from app.db.session import SessionLocal
    from app.schemas.user import UserCreate
    from app.models.user import User

    db = SessionLocal()
    CRUDUser(User).create(
        db=db,
        obj_in=UserCreate(
            full_name="admin",
            email="admin@163.com",
            password="admin",
            is_active=True,
            is_superuser=True,

        )
    )