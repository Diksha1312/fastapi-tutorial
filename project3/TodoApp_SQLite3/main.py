# where we initialize the FastAPI app and include all the routers

from fastapi import FastAPI
import models 
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

# runs only when todos.db doesnt exist
# models.Base.metadata refers to the Base class in models.py, which is inherited by the Users and Todos classes
# create_all method creates all tables in the database, which are defined by the classes that inherit from Base
# bind=engine binds the engine (database connection) to the metadata of the Base class
models.Base.metadata.create_all(bind=engine) # creates table in the database defined in models.py

# add routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

