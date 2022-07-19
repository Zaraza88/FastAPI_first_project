from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from comments.schemas import CommentCreate, Comments
from blog.models import CommentDB, PostDB
from auth.depends import get_current_user
from core.base_crud import BaseCRUD


class Comment(BaseCRUD[CommentDB, CommentCreate, CommentCreate]):
    """CRUD комментариев"""

    def get_all(self, db: Session, post_id: int):
        comments_for_post = db.query(self.model).filter(self.model.post_id == post_id).all()
        if not comments_for_post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Комментарии отсутствуют'
            )
        return comments_for_post

    def update(self, id: int, request: CommentCreate, db: Session, **kwargs):
        comment = db.query(self.model).filter(self.model.id == id)
        if not comment.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.name_obj} с {id} не существует')
        comment.update({
            self.model.text: request.text,
        })

    def create(self, request: CommentCreate, db: Session, current_user: Comments = Depends(get_current_user)):
        comment = self.model(
            post_id = request.post_id,
            text = request.text, 
            user_id = current_user.id
        )
        post_ids = [x.id for x in db.query(PostDB.id).distinct()]
        if comment.post_id not in post_ids:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Поста с id {comment.post_id} не существует')
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment


comment = Comment(CommentDB, 'Комментарий')


# {
#   "email": "adminADM123@admin.com",
#   "password": "adminADM123"
# }