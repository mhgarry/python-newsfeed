from app.models import User # importing our user model from the application to use in our seeds file to populate our database with dummy data
from app.db import Session, Base, engine # importing dependencies from our db package to use to populate our database with dummy data

# drop all tables in our database and create new ones when seed is run 
Base.metadata.drop_all(engine) # dropping all tables in our database
Base.metadata.create_all(engine) # creating all tables in our database