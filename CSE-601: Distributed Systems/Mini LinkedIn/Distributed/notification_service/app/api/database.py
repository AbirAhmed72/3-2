# post_service/app/api/database.py

import os
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/Notification"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()

    # yield db
    try:
        yield db
    finally:
        db.close()
