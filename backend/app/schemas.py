from pydantic import BaseModel, ConfigDict, EmailStr

from app.models import TodoState


class Message(BaseModel):
    message: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState


class TodoPublic(BaseModel):
    id: int
    title: str
    description: str
    state: TodoState


class TodoList(BaseModel):
    todos: list[TodoPublic]