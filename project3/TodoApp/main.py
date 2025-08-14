
from fastapi import FastAPI
import models 
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

# runs only when todos.db doesnt exist
models.Base.metadata.create_all(bind=engine) # creates table, but if anything changes in the tables, delete table and recreate

# add routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)