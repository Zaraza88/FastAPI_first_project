from sqlalchemy import (
    Column, DateTime, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship     

from core.database import Base
from user.models import UserDB


class PostDB(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    date_of_creation = Column(DateTime)
    # image_url = Column(String)
    # image_url_type = Column(String)
    user = relationship('UserDB', back_populates='posts') 
    user_id = Column(Integer, ForeignKey('user.id'))
    comments = relationship('CommentDB', back_populates='post')
    

class CommentDB(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    user_comment = relationship('UserDB', back_populates='commented') 
    user_id = Column(Integer, ForeignKey('user.id'))
    date_of_creation = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('PostDB', back_populates='comments')