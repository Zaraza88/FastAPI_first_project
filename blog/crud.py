from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from typing import List

from blog.schemas import BlogCreateSchema, BlogDisplaySchema
from blog.models import PostDB


class Post:
    """CRUD поста"""

    def create(self, request: BlogCreateSchema, db: Session):
        new_article = PostDB(
            title = request.title, 
            text = request.text, 
            date_of_creation = datetime.now()
        )
        db.add(new_article)
        db.commit()
        db.refresh(new_article)
        return new_article

    def get_all(self, db: Session):
        return db.query(PostDB).all()

    def retrieve_one(self, id: int, db: Session):
        post = db.query(PostDB).filter(PostDB.id == id).first()
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Поста с id {id} не существует'
            )
        return post

    def delete(self, id: int, db: Session):
        post = db.query(PostDB).filter(PostDB.id == id).first()
        if post:
            db.delete(post)
            db.commit()
            return 'ok'
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Поста с id {id} не существует'
            )

    def update(self, id: int, request: BlogCreateSchema, db: Session):
        post = db.query(PostDB).filter(PostDB.id == id)
        if not post.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Поста с id {id} не существует'
            )
        post.update({
            PostDB.title: request.title,
            PostDB.text: request.text,
            PostDB.date_of_creation: datetime.now()
        })
        db.commit()
        return post.first()

post = Post()