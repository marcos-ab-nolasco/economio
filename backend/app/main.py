from fastapi import FastAPI

from app.routers import auth, users

api = FastAPI()

api.include_router(users.router)
api.include_router(auth.router)
