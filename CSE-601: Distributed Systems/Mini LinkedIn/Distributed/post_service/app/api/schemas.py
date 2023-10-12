# user_service/app/api/schemas.py

from typing import Optional
from pydantic import BaseModel

class PostCreate(BaseModel):
    post_text: str
    image_url: str = None
    
    class Config:
        from_attributes = True
class PostData(PostCreate):
    post_datetime: float
    # post_datetime: datetime
    username: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        from_attributes = True
class TokenData(BaseModel):
    username: Optional[str] = None
    class Config:
        from_attributes = True

# Define other schemas as needed
