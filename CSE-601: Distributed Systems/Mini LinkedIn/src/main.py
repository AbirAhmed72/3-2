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
        
def verify_user(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, services.SECRET_KEY, algorithms=[services.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username = username)
        return token_data
    except JWTError:
        raise credentials_exception

@app.post('/register')
async def register_user(user_data: schemas.UserCreate,  db: Session = Depends(get_db)):
    db_user = services.get_user_by_username(db, user_data.username)
    if db_user:
         raise HTTPException(status_code=400, detail="E-mail already Registered")
    access_token_expires = timedelta(minutes=services.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": user_data.username}, expires_delta=access_token_expires
    )
    data = services.create_user(db, user_data)
    data.token = access_token
    return data

@app.post('/token')
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_dict = services.get_user_by_username(db, form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=401,
            detail="Invalid username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not services.verify_hashed_password(form_data.password, user_dict.password_hashed):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=services.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": user_dict.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    # return {"username": user_dict.name}
    

@app.get('/post')
def get_posts():
    return {"message": "Hello World"}

@app.post('/post')
async def create_post(post_text: str, image: UploadFile = File(None), token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_user(token)

    user = services.get_user_by_username(db, username=token_data.username)
    print(user.username)
    if user is None:
        raise credentials_exception

    image_url = None
    if image:
        # Generate a unique filename for the image
        image_filename = f"{user.username}_{uuid.uuid4().hex}.jpg"
        print(image_filename)

        # Save the image to bytes and send to MinIO bucket
        image_bytes = await image.read()
        
        minio_client.put_object(
            "minilinkedin",
            image_filename,
            io.BytesIO(image_bytes),  
            length=len(image_bytes),
            content_type="image/jpeg"
        )

        # Construct the image URL based on MinIO server URL and bucket name
        image_url = f"http://127.0.0.1:9000/minilinkedin/{image_filename}"
        print(image_url)
    
    services.make_post(db, token_data.username, post_text, image_url)

    return{"message" : "Post uploaded successfully!"}

    
    token_data = verify_user(token)
    user = services.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return services.make_post(db, token_data.username, post_data)

@app.get('/notification')
def get_notifications():
    return {"message": "Hello World"}

@app.post('/notification')
def create_notification ():
    return {"message": "Hello World"}



@app.get('/notification')
def get_notifications():
    return {"message": "Hello World"}
