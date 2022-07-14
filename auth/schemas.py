from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    """Вывод инфы о пользователе после авторизации"""
    access_string: str
    token_type: str
    user_id: int
    email: EmailStr


class Login(BaseModel):
    """Поля авторизации"""
    email: EmailStr
    password: str
