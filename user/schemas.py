import re
from datetime import datetime

from typing import List
from pydantic import BaseModel, EmailStr, validator


class BaseUserSchema(BaseModel):
    username: str
    email: EmailStr

    class Config():
        orm_mode = True
    

class UserCreateSchemas(BaseUserSchema):
    """Какие данные будут вводиться в поле при создании или измененим юзера"""
    password: str
    password2: str

    @validator('username')
    def username_alphanumeric(cls, values):
        assert values.isalnum(), 'Имя должно быть буквенно-цифровым'
        return values

    @validator('password2')
    def password_match(cls, password_two, values, **kwargs):
        pattern2 = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"
        if not re.match(pattern2, values['password']):
            raise ValueError(
                """Пароль должен быть больше 8 символов, 
                иметь символы в обоих регистрах и числа""")

        if password_two != values["password"]:
            raise ValueError('Пароли не совпадают')
        return password_two


class UsersDisplaySchemas(BaseUserSchema):
    id: int
    date_of_creation: datetime
    is_active: bool
    is_admin: bool


class SuperUserShemas(UserCreateSchemas):
    is_active: bool
    is_admin: bool


class ViewUserForBlog(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config():
        orm_mode = True