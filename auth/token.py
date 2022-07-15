from jose import jwt

from datetime import datetime, timedelta

from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.settings import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


class JWTBearer(HTTPBearer):
    """Достаем и проверяем барьер токен"""
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            token = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
            if token is None:
                return HTTPException(status_code=status.HTTP_403_FORBIDDEN)
            return credentials.credentials
        else:
            return HTTPException(status_code=status.HTTP_403_FORBIDDEN)


def create_access_token(data: dict):
    """Создание токена"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)