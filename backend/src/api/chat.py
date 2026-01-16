from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from ..database import get_session
from ..models.conversation import Conversation
from ..models.message import Message, MessageRead
from ..models.user import User
from ..agents.todo_agent import TodoAgent
from ..agents.todo_agent import MockResponse
from ..tools.task_operations import (
    add_task_tool, list_tasks_tool, complete_task_tool,
    delete_task_tool, update_task_tool
)
import json


router = APIRouter(prefix="/api", tags=["chat"])


class ChatRequest(BaseModel):
    conversation_id: Optional[int] = None
    message: str
    model_provider: Optional[str] = "openai"  # Default to openai for backward compatibility


class ChatResponse(BaseModel):
    conversation_id: int
    response: str
    tool_calls: List[Dict[str, Any]]


@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat(user_id: str, request: ChatRequest, session: Session = Depends(get_session)):
    """
    Chat endpoint that accepts a user message and returns an AI response
    along with any tool calls made by the agent.
    """
    # Verify user exists
    user = session.exec(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    # Get or create conversation
    conversation = None
    if request.conversation_id:
        conversation = session.get(Conversation, request.conversation_id)
        if not conversation or conversation.user_id != user_id:
            raise HTTPException(status_code=404, detail="Conversation not found or does not belong to user")
    else:
        # Create new conversation
        conversation = Conversation(user_id=user_id)
        session.add(conversation)
        session.commit()
        session.refresh(conversation)

    # Save user message
    user_message = Message(
        conversation_id=conversation.id,
        user_id=user_id,
        role="user",
        content=request.message
    )
    session.add(user_message)
    session.commit()

    # Get conversation history
    conversation_history = session.exec(
        select(Message)
        .where(Message.conversation_id == conversation.id)
        .order_by(Message.created_at)
    ).all()

    # Format messages for the agent
    messages = []
    for msg in conversation_history:
        messages.append({
            "role": msg.role,
            "content": msg.content,
            "user_id": user_id  # Always include user_id for all messages
        })

    # Prepare tools for the agent
    tools = [
        add_task_tool.model_dump(),
        list_tasks_tool.model_dump(),
        complete_task_tool.model_dump(),
        delete_task_tool.model_dump(),
        update_task_tool.model_dump()
    ]

    # Run the agent with tool execution
    try:
        agent = TodoAgent(model_provider=request.model_provider)
        agent_response = agent.run_with_tool_execution(messages, tools, user_id)
    except Exception as e:
        print(f"Error initializing or running agent: {e}")
        # Fallback to mock agent with explicit mock mode
        from ..agents.todo_agent import TodoAgent
        agent = TodoAgent(model_provider="openai")  # Use openai which defaults to mock mode
        agent_response = agent.run_with_tool_execution(messages, tools, user_id)

        # If that still fails, create a basic mock response
        if not agent_response or not agent_response.content:
            agent_response = MockResponse(
                content="I'm here to help you manage your tasks. You can ask me to add, list, update, or complete tasks.",
                tool_calls=[]
            )

    # Process tool calls if any
    tool_calls_result = []
    if hasattr(agent_response, 'tool_calls') and agent_response.tool_calls:
        for tool_call in agent_response.tool_calls:
            tool_calls_result.append({
                "name": tool_call.function.name,
                "arguments": json.loads(tool_call.function.arguments)
            })

    # Save assistant response
    assistant_message = Message(
        conversation_id=conversation.id,
        user_id=user_id,  # This could be an AI user ID in a real implementation
        role="assistant",
        content=agent_response.content or ""
    )
    session.add(assistant_message)
    session.commit()

    return ChatResponse(
        conversation_id=conversation.id,
        response=agent_response.content or "",
        tool_calls=tool_calls_result
    )