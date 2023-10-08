# user_service/app/main.py

from fastapi import FastAPI
from app.api.user_apis import user

app = FastAPI(openapi_url="/api/v1/user/openapi.json", docs_url="/api/v1/user/docs")

app.include_router(user, prefix="/api/v1", tags=['User'])
