from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# dependency(connecting db)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/register')
def register_user():
    return {"message": "Hello World"}

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