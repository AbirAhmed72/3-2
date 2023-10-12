# user_service/app/main.py

from fastapi import FastAPI
from app.api.post_apis import post

app = FastAPI(openapi_url="/api/v1/Post/openapi.json", docs_url="/api/v1/post/docs")

app.include_router(post, prefix="/api/v1", tags=['Post'])
