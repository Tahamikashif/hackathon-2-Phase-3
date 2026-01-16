#!/usr/bin/env python3
"""Script to recreate the database with correct schema"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.src.database import create_db_and_tables
from sqlmodel import Session, select
from backend.src.models.user import User
from backend.src.database import get_session

def main():
    print("Recreating database with correct schema...")
    
    # Create the database and tables with correct schema
    create_db_and_tables()
    
    # Add the test user using SQLModel
    session_gen = next(get_session())
    
    try:
        # Check if user already exists
        existing_user = session_gen.exec(select(User).where(User.id == "demo-user-123")).first()
        
        if not existing_user:
            # Create new user
            test_user = User(
                id="demo-user-123",
                email="demo@example.com",
                name="Demo User"
            )
            session_gen.add(test_user)
            session_gen.commit()
            print("Test user created successfully!")
        else:
            print("Test user already exists!")
    except Exception as e:
        print(f"Error creating user: {e}")
        session_gen.rollback()
    finally:
        session_gen.close()
    
    print("Database recreation complete!")

if __name__ == "__main__":
    main()