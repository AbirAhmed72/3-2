# user_service/app/api/user_apis.py
from datetime import timedelta
import io
from typing import List
import uuid
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api import schemas, database, services, models
from minio import Minio
from datetime import datetime, timedelta, time




post = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/api/v1/login")

minio_client = Minio(
    "127.0.0.1:9000",
    access_key="Abir",
    secret_key="12345678",
    secure=False  # Set to True if using HTTPS
)



@post.post('/post')
async def create_post(post_text: str, image: UploadFile = File(None), token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    token_data = services.verify_user(token)

    user = services.get_user_by_username(db, username=token_data.username)
    print(user.username)
    if user is None:
        raise services.credentials_exception

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

    # services.make_post(db, token_data.username, post_text, image_url)

    # Create the post
    new_post = services.make_post(db, token_data.username, post_text, image_url)

    # Get all users (except the one who posted)
    all_users_except_poster = db.query(models.User).filter(models.User.username != user.username).all()

    # Create a notification for each user
    for user_to_notify in all_users_except_poster:
        notification_data = schemas.NotificationCreate(
            notification_text=f"{user.username} made a new post...",
            pid=new_post.pid,
            username=user_to_notify.username,
            notification_datetime=datetime.utcnow()
        )

        services.make_notification(db, notification_data)

    return{"message" : "Post uploaded successfully!"}


@post.get('/post', response_model=List[schemas.PostData])
async def get_posts(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    token_data = services.verify_user(token)

    user = services.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise services.credentials_exception
    
    # Get all posts except the current user's posts
    latest_posts = services.get_latest_posts(db, user )
    # posts = await db.query(models.Post).filter(models.Post.username != user.username).order_by(models.Post.created_at.desc()).all()

    # latest_posts = []
    # for post in posts:
    #     post_data = schemas.PostData(
    #         username=post.username,
    #         post_text=post.post_text,
    #         image_url=post.image_url,
    #         post_datetime=post.created_at.timestamp(),
    #     )
    #     latest_posts.append(post_data)

    return latest_posts
