# services.py
import asyncio
import threading
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import Integer
import models, schemas
from jose import JWTError, jwt #JSON Web Token
from datetime import datetime, time, timedelta
import random
from passlib.hash import bcrypt

from sqlalchemy import create_engine, engine
from sqlalchemy.engine import base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

SECRET_KEY = 'e2c6a3bc1aad22372e102e8f9f657bccd65676aef94587815b9d4d2c4960a650'
ALGORITHM = "HS256"

credentials_exception = HTTPException(
        status_code=401,
        detail="Could not Validate the credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

def get_user_by_username(db: Session, username: str):
    print("Checking existing users")
    return db.query(models.User).filter(models.User.username == username).first()

def verify_user(token: str) -> schemas.TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username = username)
        return token_data
    except JWTError:
        raise credentials_exception

def get_post_by_pid(db: Session, pid: int):
    return db.query(models.Post).filter(models.Post.pid == pid).first()

def make_post(db: Session, current_username: str, post_text, image_url: Optional[str] = None):
    db_post = models.Post(
        post_text = post_text,
        image_url = image_url,
        created_at = datetime.utcnow(),
        username = current_username
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_latest_posts(db: Session, user):
    posts = db.query(models.Post).filter(models.Post.username != user.username).order_by(models.Post.created_at.desc()).all()

    latest_posts = []
    for post in posts:
        post_data = schemas.PostData(
            username=post.username,
            post_text=post.post_text,
            image_url=post.image_url,
            post_datetime=post.created_at.timestamp(),
        )
        latest_posts.append(post_data)
    
    return latest_posts
