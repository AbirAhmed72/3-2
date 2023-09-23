# # schemas.py

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
    notification_text: str
    created_at: datetime

# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
