from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import re


def validate_email(email: str) -> str:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format")
    return email


class UserBase(SQLModel):
    email: str = Field(sa_column_kwargs={"unique": True}, nullable=False)
    name: Optional[str] = Field(default=None)


class User(UserBase, table=True):
    """
    Represents individuals using the system
    """
    id: str = Field(primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserRead(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime


class UserUpdate(SQLModel):
    name: Optional[str] = None