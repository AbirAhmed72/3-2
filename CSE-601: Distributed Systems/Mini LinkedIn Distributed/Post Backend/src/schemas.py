# # schemas.py
# from datetime import datetime
# from pydantic import BaseModel
# from typing import Optional, List

# from sqlalchemy.sql.sqltypes import Integer, String


# class UserData(BaseModel):
#     uid: int
#     username: str
#     class Config:
#         orm_mode = True
# class UserCreate(BaseModel):
#     username: str
#     password: str
#     class Config:
#         orm_mode = True

# class ResponseUserData(UserData):
#     token: str
#     class Config:
#         orm_mode = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str
#     class Config:
#         orm_mode = True
# class TokenData(BaseModel):
#     username: Optional[str] = None
#     class Config:
#         orm_mode = True
    
        
# class PostCreate(BaseModel):
#     post_text: str
#     image_url: str = None
    
#     class Config:
#         orm_mode = True
# class PostData(PostCreate):
#     post_datetime: float
#     # post_datetime: datetime
#     username: str
#     class Config:
#         orm_mode = True
    

# class NotificationCreate(BaseModel):
#     notification_text: str
#     is_read: bool = False
#     # notification_datetime: float
#     notification_datetime: datetime
#     pid: int
#     username: str
#     class Config:
#         orm_mode = True

# class NotificationData(BaseModel):
#     notification_datetime: datetime
#     notification_text: str

#     class Config:
#         orm_mode = True


from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# User Schema
class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    password_hashed: str

class UserResponse(User):
    uid: int

# Post Schema
class PostCreate(BaseModel):
    post_text: str
    image_url: Optional[str]

class Post(BaseModel):
    post_text: str
    image_url: Optional[str]
    created_at: datetime
    username: str

# Notification Schema
class NotificationCreate(BaseModel):
    username: str
    pid: int
    notification_text: str
    is_read: bool
    created_at: datetime

class Notification(BaseModel):
    username: str
    pid: int
    notification_text: str
    is_read: bool
    created_at: datetime

# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
