from datetime import datetime

from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm.session import Session

from user.schemas import UserCreateSchemas, UsersDisplaySchemas
from user.models import UserDB
from user.logic import HashPassword as hash


class User:
    """CRUD юзера"""

    def create_a_simple_user(self, request: UserCreateSchemas, db: Session):
        new_user = UserDB(
            username = request.username, 
            email = request.email, 
            password = hash.bcrypt(request.password),
            date_of_creation = datetime.now()
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_all_users(self, db: Session):
        return db.query(UserDB).all()

    def create_superuser(self, request: UserCreateSchemas, db: Session,):
        new_user = UserDB(
            username = request.username, 
            email = request.email, 
            password = hash.bcrypt(request.password),
            date_of_creation = datetime.now(),
            is_active = request.is_active,
            is_admin = request.is_admin
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_by_email(db: Session, email: EmailStr):
        return db.query(UserDB).filter(UserDB.email == email).first()

    def delete(self, id: int, db: Session):
        post = db.query(UserDB).filter(UserDB.id == id).first()
        if post:
            db.delete(post)
            db.commit()
            return 'ok'
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Пользователя с id {id} не существует'
            )

    def update(self, id: int, request: UserCreateSchemas, db: Session):
        post = db.query(UserDB).filter(UserDB.id == id)
        if not post.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Пользователя с id {id} не существует'
            )
        post.update({
            UserDB.username: request.title,
            UserDB.email: request.text,
            UserDB.password: hash.bcrypt(request.password),
            UserDB.date_of_creation: datetime.now(),
            UserDB.is_active: request.text,
            UserDB.is_admin: request.text,
        })
        db.commit()
        return post.first()

    def is_active(self, user: UserDB):
        return user.is_active

    def is_admin(self, user: UserDB):
        return user.is_admin


user = User()