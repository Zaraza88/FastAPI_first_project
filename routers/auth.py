from fastapi import APIRouter, Depends
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from auth.auth_db import token
from core.database import get_db

from auth.schemas import Login


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/token')
def get_token(request: Login, db: Session = Depends(get_db)):
    return token(request, db)
