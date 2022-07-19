from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from comments.schemas import CommentCreate, Comments
from auth.depends import get_current_user
from core.database import get_db
from comments.comment_db import comment
from user.role import admin_permission


router = APIRouter(tags=['comment'], prefix='/comment')
    

@router.delete('/delete/{id}', dependencies=[Depends(admin_permission)])#удалять сможет только админ
def delete_comment(id: int, db: Session = Depends(get_db)):
    return comment.delete(id, db)


@router.post('/create', response_model=Comments)
def create_comment(
    request: CommentCreate, 
    db: Session = Depends(get_db), 
    current_user: Comments = Depends(get_current_user)):
    return comment.create(request, db, current_user)


@router.patch('/update/{id}')
def update_comment(id: int, request: CommentCreate, db: Session = Depends(get_db)):
    return comment.update(id, request, db)


@router.get('/all/{post_id}', response_model=List[Comments])
def comments(post_id: int, db: Session = Depends(get_db)):
    return comment.get_all(db, post_id)