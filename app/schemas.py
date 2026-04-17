from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    ID: int
    email: EmailStr

    class Config:
        from_attributes = True

class Post(BaseModel):
    ID: int
    title: str
    content: str
    created_at:datetime
    owner_id: int
    owner:UserOut

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id:int
    dir:conint(ge=0,le=1)