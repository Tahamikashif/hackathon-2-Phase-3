from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class MessageBase(SQLModel):
    conversation_id: int = Field(nullable=False)
    user_id: str = Field(nullable=False)
    role: str = Field(nullable=False)
    content: str = Field(nullable=False)


class Message(MessageBase, table=True):
    """
    Represents individual exchanges within a conversation
    """
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class MessageRead(MessageBase):
    id: int
    created_at: datetime


class MessageUpdate(SQLModel):
    content: Optional[str] = None