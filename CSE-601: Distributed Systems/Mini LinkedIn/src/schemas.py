from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

from sqlalchemy.sql.sqltypes import Integer, String


class UserData(BaseModel):
    uid: int
    name: str
    email: str
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
    
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    class Config:
        orm_mode = True
        
class PostData(BaseModel):
    pid: int
    post: str
    post_datetime: float
    # post_datetime: datetime
    uid: int
    class Config:
        orm_mode = True
    
class NotificationData(BaseModel):
    nid: int
    notification: str
    notification_datetime: float
    # notification_datetime: datetime
    pid: int
    uid: int
    class Config:
        orm_mode = True
