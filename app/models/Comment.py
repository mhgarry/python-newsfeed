from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeginKey, DateTime   
from sqlalchemy.orm import relationship # importing relationship to create a one to many relationship between our models

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User') # creating a relationship between our Comment and User models