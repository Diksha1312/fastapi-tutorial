# where we define the models for our database tables

from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

# 2 tables: users and todos, each table is represented by a class that inherits from Base (database.py) 

class Users(Base):
    __tablename__ = 'users' # name of the table in the database/. 

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    phone_number = Column(String)
    # about_me = Column(String)

class Todos(Base):
    __tablename__ = 'todos' # name of the table in the database
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id")) # foreign key to the users table

