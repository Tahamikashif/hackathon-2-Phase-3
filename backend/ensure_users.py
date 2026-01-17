import sys
import os
from uuid import uuid4

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.database import get_session, create_db_and_tables
from src.models.user import User

def ensure_default_user():
    # Create tables if they don't exist
    create_db_and_tables()
    
    # Create a default user that the frontend can use
    default_user = User(
        id="default-user",  # This matches what the frontend might use initially
        email="default@example.com",
        name="Default User"
    )
    
    # Add to database
    session_gen = get_session()
    session = next(session_gen)
    
    # Check if user already exists
    existing_user = session.get(User, "default-user")
    if existing_user:
        print(f"Default user already exists: {existing_user.email}")
    else:
        session.add(default_user)
        session.commit()
        print(f"Created default user with ID: {default_user.id}")
        
    # Also create a test user for general testing
    test_user = User(
        id="test_user_123",
        email="test@example.com",
        name="Test User"
    )
    
    existing_test_user = session.get(User, "test_user_123")
    if existing_test_user:
        print(f"Test user already exists: {existing_test_user.email}")
    else:
        session.add(test_user)
        session.commit()
        print(f"Created test user with ID: {test_user.id}")

if __name__ == "__main__":
    ensure_default_user()