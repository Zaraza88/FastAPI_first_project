from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from blog.schemas import BlogCreateSchema, BlogDisplaySchema, BaseBlogSchema
from core.database import get_db
from blog.models import PostDB
from blog.crud import post


router = APIRouter(prefix='/post', tags=['post'])


@router.post('/create', response_model=BlogDisplaySchema)
def create_post(request: BlogCreateSchema, db: Session = Depends(get_db)):
    return post.create(request, db)


@router.get('/all', response_model=List[BlogDisplaySchema])
def get_all_post(db: Session = Depends(get_db)):
    return post.get_all(db)


@router.delete('/delete/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    return post.delete(id, db)


@router.get('/get/{id}', response_model=BlogDisplaySchema)
def get_one_post(id: int, db: Session = Depends(get_db)):
    return post.retrieve_one(id, db)


@router.patch('/update/{id}', response_model=BlogDisplaySchema)
def update_post(id: int, request: BlogCreateSchema, db: Session = Depends(get_db)):
    return post.update(id, request, db)