from jose import jwt

from fastapi import HTTPException, Depends, status
from fastapi.param_functions import Depends
from pydantic import EmailStr
from sqlalchemy.orm.session import Session

from core.database import get_db
from core.settings import SECRET_KEY, ALGORITHM
from auth.token import JWTBearer
from user.models import UserDB

#не забыть переместить и порешать с импортами
def get_by_email(db: Session, email: EmailStr):
    return db.query(UserDB).filter(UserDB.email == email).first()


def get_current_user(token: str = Depends(JWTBearer()), db: Session = Depends(get_db)):
    """Получение текущего пользователя"""
    creadentials_exceprion = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='oshibka 401',
        headers={"WWW-Authenticate": "Bearer"}
    )
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload is None:
        raise creadentials_exceprion

    email: str = payload.get('sub')
    if email is None:
        raise creadentials_exceprion

    user = get_by_email(db, email)
    if user is None:
        raise creadentials_exceprion

    return user
