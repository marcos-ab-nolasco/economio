from fastapi import FastAPI

from app.routers import auth, todos, users

api = FastAPI()

api.include_router(users.router)
api.include_router(auth.router)
api.include_router(todos.router)
