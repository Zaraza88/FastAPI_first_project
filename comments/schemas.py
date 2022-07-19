from pydantic import BaseModel

from user.schemas import BaseUserSchema


class ViewCommentForBlog(BaseModel):
    """Схема для вывода комментариев под постом"""
    id: int
    text: str
    user_comment: BaseUserSchema

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    """Создание и обновление комментариев"""
    text: str
    post_id: int


class Comments(BaseModel):
    """Вывод комментария после его создания или обновления. 
    Так же вывод всех комментариев под постом"""
    id: int
    post_id: int
    text: str
    user_comment: BaseUserSchema

    class Config:
        orm_mode = True