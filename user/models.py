from sqlalchemy import (
    Boolean, Column, Integer, String, ForeignKey, DateTime
)
from sqlalchemy.orm import relationship     

from core.database import Base
# from blog.models import PostDB, CommentDB


class UserDB(Base):
    
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    date_of_creation = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    posts = relationship('PostDB', back_populates='user')
    commented = relationship('CommentDB', back_populates='user_comment')