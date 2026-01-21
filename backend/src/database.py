from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy import event
from sqlalchemy.engine import Engine
from pathlib import Path
import os
from typing import Generator
from dotenv import load_dotenv
from .models.task import Task
from .models.conversation import Conversation
from .models.message import Message
from .models.user import User

# Load environment variables from .env file
load_dotenv()

# Use database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_chatbot_local.db")

# For PostgreSQL, use: postgresql+psycopg2://user:password@localhost/dbname
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def create_db_and_tables():
    """Create database tables"""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get database session"""
    with Session(engine) as session:
        yield session