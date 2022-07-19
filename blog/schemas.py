from datetime import datetime
from typing import List
from pydantic import BaseModel

from comments.schemas import ViewCommentForBlog
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
    comments: List[ViewCommentForBlog]

    class Config:
        orm_mode = True


class BlogCreateSchema(BaseBlogSchema):
    """Схема создания постов"""
    pass

