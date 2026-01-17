import sys
import os
from uuid import uuid4

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.database import get_session, create_db_and_tables
from src.models.user import User

def create_test_user():
    # Create tables if they don't exist
    create_db_and_tables()
    
    # Create a test user
    test_user = User(
        id="test_user_123",
        email="test@example.com",
        name="Test User"
    )
    
    # Add to database
    session_gen = get_session()
    session = next(session_gen)
    
    # Check if user already exists
    existing_user = session.get(User, "test_user_123")
    if existing_user:
        print(f"User with ID test_user_123 already exists: {existing_user.email}")
    else:
        session.add(test_user)
        session.commit()
        print(f"Created test user with ID: {test_user.id}")

if __name__ == "__main__":
    create_test_user()