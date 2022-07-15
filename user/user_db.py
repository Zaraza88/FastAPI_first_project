from datetime import datetime

from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm.session import Session

from user.schemas import UserCreateSchemas, SuperUserShemas
from user.models import UserDB
from user.hash import bcrypt
from core.base_crud import BaseCRUD
    

class User(BaseCRUD[UserDB, UserCreateSchemas, SuperUserShemas]):
    """CRUD юзера для пользования администратором"""

    def create_superuser(self, request: UserCreateSchemas, db: Session):
        obj = self.model(
            username = request.username, 
            email = request.email, 
            password = bcrypt(request.password),
            date_of_creation = datetime.now(),
            is_active = request.is_active,
            is_admin = request.is_admin
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, id: int, request: SuperUserShemas, db: Session):
        obj = db.query(self.model).filter(self.model.id == id)
        if not obj.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.name_obj} с id {id} не существует'
            )
        obj.update({
            self.model.username: request.username,
            self.model.email: request.email,
            self.model.password: bcrypt(request.password),
            self.model.date_of_creation: datetime.now(),
            self.model.is_active: request.is_active,
            self.model.is_admin: request.is_admin,
        })
        db.commit()
        return obj.first()


    def is_active(self, user: UserDB):
        return user.is_active

    def is_admin(self, user: UserDB):
        return user.is_admin

    def get_user_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    # def is_staff(self, user: UserDB):
    #     return user.is_staff

    # def is_manager(self, user: UserDB):
    #     return user.is_staff

    # def get_by_email(self, db: Session, email: EmailStr):
    #     return db.query(self.model).filter(self.model.email == email).first()


user_crud = User(UserDB, 'Пользователь')