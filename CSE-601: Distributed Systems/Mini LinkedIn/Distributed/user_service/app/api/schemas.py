from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(UserCreate):
    id: int

# Define other schemas as needed
