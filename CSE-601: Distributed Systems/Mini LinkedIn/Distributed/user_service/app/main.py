from fastapi import FastAPI
from user_service.app.api import user_apis

app = FastAPI()

app.include_router(user_apis.router, prefix="/api/v1")
