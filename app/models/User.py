from app.db import Base # importing Base from app.db to use a as a base class for our model 
from sqlalchemy import Column, Integer, String # importing rows to populate our columns that populate our table with data 
from sqlalchemy.orm import validates # add validation to our model

class User(Base): # creating a class called User that inherits from Base
    __tablename__ = 'users' # creating a table called users
    id = Column(Integer, primary_key=True) # genarating an id column that is an integer and is the primary key of the users table
    username = Column(String(50), nullable=False) # genearting a required username column that is a string with a max length of 50
    email = Column(String(50), nullable=False, unique=True) # generating a required email column that must be unique and is a string with a max length of 50
    password = Column(String(100), nullable=False) # generating a required password column that is a string with a max length of 100

    @validates('email') # adding validation to our email column to ensure that it is a valid email address 
    def validate_email(self, key, email):
        assert '@' in email

        return email
    
    @validates('password') # adding validation logic to our password column
    def validate_password(self, key, password):
        assert len(password) > 4

        return password
    
    