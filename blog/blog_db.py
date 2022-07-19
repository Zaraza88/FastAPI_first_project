from datetime import datetime

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from user.schemas import ViewUserForBlog
from blog.schemas import BlogCreateSchema
from blog.models import PostDB
from auth.depends import get_current_user
from core.base_crud import BaseCRUD


class Post(BaseCRUD[PostDB, BlogCreateSchema, BlogCreateSchema]):
    """CRUD поста"""
    
    def create(self, request: BlogCreateSchema, db: Session, current_user: ViewUserForBlog = Depends(get_current_user)):
        obj = self.model(
            title = request.title, 
            text = request.text, 
            date_of_creation = datetime.now(),
            user_id = current_user.id
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, id: int, request: BlogCreateSchema, db: Session):
        obj = db.query(self.model).filter(self.model.id == id)
        if not obj.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.name_obj} с id {id} не существует'
            )
        obj.update({
            self.model.title: request.title,
            self.model.text: request.text,
            self.model.date_of_creation: datetime.now()
        })
        db.commit()
        return obj.first()


post = Post(PostDB, 'Пост')
