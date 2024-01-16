from pydantic import BaseModel
from typing import Optional

# Pydantic schemas for Todo
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Pydantic schemas for User
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic schemas for Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
