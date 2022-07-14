from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from user.models import UserDB
from user.hash import verify

from auth.schemas import Token, Login
from auth.token import create_access_token


def token(request: Login, db: Session):
    """Авторизуемся и получаем токен"""
    user = db.query(UserDB).filter(UserDB.email == request.email).first()
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



