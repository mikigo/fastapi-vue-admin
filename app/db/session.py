from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings

# engine = create_engine(settings.DB_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
engine = create_engine(settings.DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
