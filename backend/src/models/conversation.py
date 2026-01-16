from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class ConversationBase(SQLModel):
    user_id: str


class Conversation(ConversationBase, table=True):
    """
    Represents a session of interaction between a user and the AI assistant
    """
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ConversationRead(ConversationBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ConversationUpdate(SQLModel):
    pass  # No updatable fields for conversation