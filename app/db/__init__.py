from os import getenv # importing getenv from the os module the os module provides a portable way of using operating system dependent functionality.
from sqlalchemy.ext.declarative import declarative_base # importing declarative_base from sqlalchemy.ext.declarative
from sqlalchemy.orm import sessionmaker # importing sessionmaker from sqlalchemy.orm
from sqlalchemy import create_engine
 # importing create_engine from sqlalchemy
from dotenv import load_dotenv # importing load_dotenv from dotenv

load_dotenv() # load_dotenv() loads the values from our .env file into our script's environment

# The following line of code creates a database engine that will interact with our database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0) # the pool size and max_overflow parameters are used to control the number of connections that are kept in the connection pool. The echo parameter is used to control the verbosity of the database engine logging.
Session = sessionmaker(bind=engine) # The sessionmaker() function creates a Session class. The sessionmaker() function returns a class, not an instance. We pass the engine to the sessionmaker() function to bind the engine to the Session class. This will create a new Session object whenever we call sessionmaker().
Base = declarative_base() # The declarative_base() function creates a new base class from which all mapped classes should inherit. When the class definition is completed, a new Table and mapper() will have been generated.