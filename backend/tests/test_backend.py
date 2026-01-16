import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from unittest.mock import patch
from ..src.main import app
from ..src.database import get_session
from ..src.models.user import User
from ..src.models.task import Task


# Create a test database engine
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", 
        connect_args={"check_same_thread": False}, 
        poolclass=StaticPool
    )
    SQLModel.metadata.create_all(bind=engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_create_user(client: TestClient, session: Session):
    """Test creating a user"""
    user_data = {
        "email": "test@example.com",
        "name": "Test User"
    }
    
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["name"] == user_data["name"]


def test_create_task(client: TestClient, session: Session):
    """Test creating a task"""
    # First create a user
    user_data = {
        "email": "test@example.com",
        "name": "Test User"
    }
    user_response = client.post("/users/", json=user_data)
    user = user_response.json()
    
    # Create a task for the user
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "user_id": user["id"],
        "completed": False
    }
    
    response = client.post(f"/users/{user['id']}/tasks", json=task_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    assert data["completed"] == task_data["completed"]


@patch('src.agents.todo_agent.TodoAgent.run_with_tool_execution')
def test_chat_endpoint(mock_run, client: TestClient, session: Session):
    """Test the chat endpoint"""
    # Mock the agent response
    mock_run.return_value = type('MockResponse', (), {
        'content': 'Task created successfully',
        'tool_calls': [{'name': 'add_task', 'arguments': '{"user_id": "user123", "title": "Test Task"}'}]
    })()
    
    # Create a user first
    user_data = {
        "email": "test@example.com",
        "name": "Test User"
    }
    user_response = client.post("/users/", json=user_data)
    user = user_response.json()
    
    # Test the chat endpoint
    chat_data = {
        "message": "I need to create a task to buy groceries"
    }
    
    response = client.post(f"/api/{user['id']}/chat", json=chat_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "response" in data
    assert "tool_calls" in data
    assert data["response"] == "Task created successfully"


def test_list_tasks(client: TestClient, session: Session):
    """Test listing tasks for a user"""
    # First create a user
    user_data = {
        "email": "test@example.com",
        "name": "Test User"
    }
    user_response = client.post("/users/", json=user_data)
    user = user_response.json()
    
    # Create a task for the user
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "user_id": user["id"],
        "completed": False
    }
    client.post(f"/users/{user['id']}/tasks", json=task_data)
    
    # List tasks
    response = client.get(f"/users/{user['id']}/tasks")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == task_data["title"]