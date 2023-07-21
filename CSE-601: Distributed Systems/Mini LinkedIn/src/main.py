import random
import joblib as jb
import models, schemas, services
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Optional

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import Integer

from schemas import TokenData
from sqlalchemy.orm import Session
from database import SessionLocal, engine

from datetime import datetime, timedelta, time
from jose import JWTError,jwt


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

credentials_exception = HTTPException(
        status_code=401,
        detail="Could not Validate the credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
        
# def verify_user(token: str):
#     try:
#         payload = jwt.decode(token, services.SECRET_KEY, algorithms=[services.ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#         token_data = schemas.TokenData(username = email)
#         return token_data
#     except JWTError:
#         raise credentials_exception

@app.post('/register')
async def register_user(user_data: schemas.UserCreate,  db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, user_data.email)
    if db_user:
         raise HTTPException(status_code=400, detail="E-mail already Registered")
    access_token_expires = timedelta(minutes=services.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": user_data.email}, expires_delta=access_token_expires
    )
    data = services.create_user(db, user_data)
    data.token = access_token
    return data

@app.post('/login')
def login_user():
    return {"message": "Hello World"}

@app.get('/post')
def get_posts():
    return {"message": "Hello World"}

@app.post('/post')
def create_post():
    return {"message": "Hello World"}

@app.get('/notification')
def get_notifications():
    return {"message": "Hello World"}

@app.post('/notification')
def create_notification ():
    return {"message": "Hello World"}