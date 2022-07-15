from fastapi import APIRouter, Depends
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from auth.auth_db import auth
from auth.schemas import Login
from core.database import get_db
from user.schemas import UserCreateSchemas


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/login')
def get_login(request: Login, db: Session = Depends(get_db)):
    return auth.login(request, db)


@router.post('/register')
def register(request: UserCreateSchemas, db: Session = Depends(get_db)):
    return auth.create_user(request, db)