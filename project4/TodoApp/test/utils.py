
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from ..models import Todos, Users
from ..database import Base
from ..main import app
from sqlalchemy.pool import StaticPool
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./testtodosapp.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={'check_same_thread': False},
    poolclass=StaticPool, # tells SQLAlchemy to resue the same connection every time
    )
TestingSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'testClient', 'id': 1, 'user_role': 'admin'}

client = TestClient(app) # calls FastAPI server like an HTTP client wihtout actually running a server

@pytest.fixture # any test function that has test_todo as its param will have this fixture
def test_todo():
    todo = Todos(complete=False, title='Learn fastapi', description='deadline approaching', priority=3, owner_id=1)
    db=TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo # yield gives data to the test, after the test finishes, code after yield runs
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM todos;'))
        connection.commit()

@pytest.fixture
def test_user():
    user = Users(
        username='testClient',
        email='testClient@test.com',
        first_name='test',
        last_name='Client',
        hashed_password=bcrypt_context.hash("test123"),
        role='admin',
        phone_number="(123)-456-789"
    )
    db=TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user # yield gives data to the test, after the test finishes, code after yield runs
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM users;'))
        connection.commit()