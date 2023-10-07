from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from user_service.app.api import db_operations, schemas
from user_service.app.api.database import get_db
import services

router = APIRouter()

@router.post('/register')
async def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db_operations.get_user_by_username(db, user_data.username)
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail already Registered")
    access_token_expires = timedelta(minutes=services.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": user_data.username}, expires_delta=access_token_expires
    )
    user = db_operations.create_user(db, user_data)
    user.token = access_token
    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/token')
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db_operations.get_user_by_username(db, form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not db_operations.verify_hashed_password(form_data.password, db_user.password_hashed):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=services.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/me')
async def get_current_user_info(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = services.verify_user(token)
    user = db_operations.get_user_by_username(db, token_data.username)
    delattr(user, "password_hashed")
    return user
