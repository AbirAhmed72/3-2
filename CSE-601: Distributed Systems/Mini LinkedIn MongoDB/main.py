from fastapi import FastAPI
from Routes.user import user

app = FastAPI()
app.include_router(user)

