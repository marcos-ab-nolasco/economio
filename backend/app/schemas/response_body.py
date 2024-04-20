from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]
