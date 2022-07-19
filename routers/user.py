from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from core.database import get_db
from user.schemas import UsersDisplaySchemas, SuperUserShemas
from user.user_db import user_crud
from user.role import admin_permission


router = APIRouter(tags=['user'], prefix='/user')
    

@router.get('/all', response_model=List[UsersDisplaySchemas], dependencies=[Depends(admin_permission)])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_all(db)


@router.delete('/delete/{id}', dependencies=[Depends(admin_permission)])
def delete_user(id: int, db: Session = Depends(get_db)):
    return user_crud.delete(id, db)


@router.post('/create_superuser', response_model=UsersDisplaySchemas, dependencies=[Depends(admin_permission)])
def create_superuser(request: SuperUserShemas, db: Session = Depends(get_db)):
    return user_crud.create_superuser(request, db)


@router.patch('/update/{id}', dependencies=[Depends(admin_permission)])
def update_user(id: int, request: SuperUserShemas, db: Session = Depends(get_db)):
    return user_crud.update(id, request, db)
