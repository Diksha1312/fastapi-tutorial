# where we set up the database connection and session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' # relative path to the database file

# opens the database connection, connect_args args to avoid threading issues with SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# creates a session local class, each instance of this class will be a database session, bind it to the engine that we created
# autocommit and autoflush are set to false so that we can control when to commit and flush
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for our models to inherit from, this base class maintains a catalog of classes and tables
Base = declarative_base()
