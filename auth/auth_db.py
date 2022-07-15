from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from user.schemas import UserCreateSchemas
from user.models import UserDB
from user.hash import bcrypt, verify

from auth.schemas import Token, Login
from auth.token import create_access_token
from auth.depends import get_by_email


class UserAuthorization:
    """Регистрация и аутентификация"""

    def login(self, request: Login, db: Session):
        """Аутентифицируемся и получаем токен"""
        user = get_by_email(db, request.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Такого пользователя не существует")
        if not verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Неверный пароль")

        return Token(
            access_string=create_access_token(data={'sub': user.email}),
            token_type='Bearer',
            user_id=user.id,
            email=user.email
        )

    def create_user(self, request: UserCreateSchemas, db: Session):
        new_user = UserDB(
            username = request.username, 
            email = request.email, 
            password = bcrypt(request.password),
            date_of_creation = datetime.now()
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


auth = UserAuthorization()
