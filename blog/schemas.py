from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, validator

from user.schemas import ViewUserForBlog


class BaseBlogSchema(BaseModel):
    """Базовая схема постов"""
    title: str
    text: str
    date_of_creation: datetime


class BlogDisplaySchema(BaseBlogSchema):
    """Схева для вывод постов"""
    id: int #чисто для проверки(потом убрать)
    user: ViewUserForBlog
    #comment
    

    class Config:
        orm_mode = True


class BlogCreateSchema(BaseBlogSchema):
    """Схема создания постов"""
    pass


class BaseCommentSchema(BaseModel):
    """Базовая схема комментариев"""
    id: int
    text: str



