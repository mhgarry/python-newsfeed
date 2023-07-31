from datetime import datetime 
from app.db import Base
from .Vote import Vote # importing our Vote model to create a relationship between our Post and Vote models and add the ability to count the number of votes a post has
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, column_property # adding a column property to our Post model to count the number of votes a post has

class Post(Base): # create a Post class that makes a table called posts
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    vote_count = column_property(
        select([func.count(Vote.id)]).where(Vote.post_id == id) # logic to count the number of votes a post has and the func.count() function to count the number of votes a post has
    )

    user = relationship('User') # create a relationship between our Post and User models
    comments = relationship('Comment', cascade='all,delete') # create a relationship between our Post and Comment models and cascade all deletes to our comments table
    votes = relationship('Vote', cascade='all,delete') # create a relationship between our Post and Vote models and cascade all deletes to our votes table