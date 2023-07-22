from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from fastapi import UploadFile
from sqlalchemy.sql.sqltypes import Integer, String


class UserData(BaseModel):
    uid: int
    username: str
    class Config:
        orm_mode = True
class UserCreate(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True

class ResponseUserData(UserData):
    token: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True
class TokenData(BaseModel):
    username: Optional[str] = None
    class Config:
        orm_mode = True
    

class PostCreate(BaseModel):
    post_text: str
    image_url: Optional[str]
    class Config:
        orm_mode = True
class PostData(PostCreate):
    post_datetime: datetime
    username: str
    class Config:
        orm_mode = True
    

class NotificationCreate(BaseModel):
    notification_text: str
    is_read: bool
    notification_datetime: float
    # notification_datetime: datetime
    pid: int
    uid: int
    class Config:
        orm_mode = True
class NotificationData(NotificationCreate):
    nid: int
    class Config:
        orm_mode = True
