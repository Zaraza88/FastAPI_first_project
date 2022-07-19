from typing import TypeVar, Generic, Type
from pydantic import BaseModel

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from core.database import Base


ModelType = TypeVar('ModelType', bound=Base)
CreateSchemasType = TypeVar('CreateSchemasType', bound=BaseModel)
UpdateSchemasType = TypeVar('UpdateSchemasType', bound=BaseModel)


class BaseCRUD(Generic[ModelType, CreateSchemasType, UpdateSchemasType]):
    """CRUD поста"""

    def __init__(self, model: Type[ModelType], name_obj: str):
        """model - Модель данных
        name_obj - Наименование объекта(для эксепшенов)
        """
        self.model = model
        self.name_obj = name_obj

    def get_all(self, db: Session, **kwargs):
        return db.query(self.model).all()

    def retrieve_one(self, id: int, db: Session):
        obj = db.query(self.model).filter(self.model.id == id).first()
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.name_obj} с id {id} не существует'
            )
        return obj

    def delete(self, id: int, db: Session):
        obj = db.query(self.model).filter(self.model.id == id).first()
        if obj:
            db.delete(obj)
            db.commit()
            return f'{self.name_obj} с id {id} успешно удален!'
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{self.name_obj} с id {id} не существует'
            )

    def create(self, request: CreateSchemasType, db: Session, **kwargs):
        pass

    def update(self, id: int, request: UpdateSchemasType, db: Session):
        pass