from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, validator


class BaseBlogSchema(BaseModel):
    title: str
    text: str
    date_of_creation: datetime
    

class BlogDisplaySchema(BaseBlogSchema):
    id: int #чисто для проверки(потом убрать)
    #user
    #comment

    class Config:
        orm_mode = True


class BlogCreateSchema(BaseBlogSchema):
    pass


class BaseCommentSchema(BaseModel):
    id: int
    text: str



