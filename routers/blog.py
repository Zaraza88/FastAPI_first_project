from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from user.schemas import ViewUserForBlog
from auth.depends import get_current_user
from blog.schemas import BlogCreateSchema, BlogDisplaySchema
from blog.blog_db import post
from core.database import get_db


router = APIRouter(prefix='/post', tags=['post'])


@router.post('/create', response_model=BlogDisplaySchema)
def create_post(
    request: BlogCreateSchema, 
    db: Session = Depends(get_db), 
    current_user: ViewUserForBlog = Depends(get_current_user)
    ):
    return post.create(request, db, current_user)


@router.get('/all', response_model=List[BlogDisplaySchema])
def get_all_post(db: Session = Depends(get_db)):
    return post.get_all(db)


@router.delete(
    '/delete/{id}', 
    # dependencies=[Depends(get_current_user)]
    )
def delete_post(id: int, db: Session = Depends(get_db)):
    return post.delete(id, db)


@router.get('/get/{id}', response_model=BlogDisplaySchema)
def get_one_post(id: int, db: Session = Depends(get_db)):
    return post.retrieve_one(id, db)


@router.patch(
    '/update/{id}', 
    response_model=BlogDisplaySchema, 
    dependencies=[Depends(get_current_user)]
    )
def update_post(id: int, request: BlogCreateSchema, db: Session = Depends(get_db)):
    return post.update(id, request, db)


@router.get('/search')
def search_post(query: Optional[str], db: Session = Depends(get_db)):
    return post.search(query, db)


@router.get('/filter')
def filter_data(title: Optional[str], text: Optional[str], db: Session = Depends(get_db)):
    return post.filter(title, text, db)