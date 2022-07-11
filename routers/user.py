from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from core.database import get_db
from user.schemas import UserCreateSchemas, UsersDisplaySchemas, SuperUserShemas
from user.crud import user


router = APIRouter(tags=['user'], prefix='/user')


@router.post('/create_user', response_model=UsersDisplaySchemas)
def create_user(request: UserCreateSchemas, db: Session = Depends(get_db)):
    return user.create_a_simple_user(request, db)
    

@router.get('/all', response_model=List[UsersDisplaySchemas])
def get_users(db: Session = Depends(get_db)):
    return user.get_all_users(db)


@router.delete('/delete/{id}')#удалять сможет только админ
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.delete(id, db)


@router.post('/create_superuser', response_model=UsersDisplaySchemas)
def create_superuser(request: SuperUserShemas, db: Session = Depends(get_db)):
    return user.create_superuser(request, db)


@router.patch('/update/{id}')#обновлять сможет только админ
def update_user(request: SuperUserShemas, db: Session = Depends(get_db)):
    return user.update(request, db)