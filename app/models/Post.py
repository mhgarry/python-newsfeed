from datetime import datetime 
from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base): # create a Post class that makes a table called posts
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User') # create a relationship between our Post and User models
    comments = relationship('Comment', cascade='all,delete') # create a relationship between our Post and Comment models and cascade all deletes to our comments table