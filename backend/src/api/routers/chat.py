from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from ...database import get_session
from ...models.conversation import Conversation
from ...models.message import Message, MessageRead
from ...models.user import User
from ...agents.todo_agent import TodoAgent
from ...agents.todo_agent import MockResponse
from ...tools.task_operations import (
    add_task_tool, list_tasks_tool, complete_task_tool,
    delete_task_tool, update_task_tool
)
from ...Agent_sdk.main import OpenAIAgentSDK, is_general_question
import json


router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
    conversation_id: Optional[int] = None
    message: str
    model_provider: Optional[str] = "openai"  # Default to openai for backward compatibility


class ChatResponse(BaseModel):
    conversation_id: int
    response: str
    tool_calls: List[Dict[str, Any]]


@router.post("/{user_id}", response_model=ChatResponse)
async def chat(user_id: str, request: ChatRequest, session: Session = Depends(get_session)):
    """
    Chat endpoint that accepts a user message and returns an AI response
    along with any tool calls made by the agent.
    Supports both task operations and general questions.
    """
    try:
        # Verify user exists, create if not found
        user = session.exec(select(User).where(User.id == user_id)).first()
        if not user:
            # Create a new user with the provided ID
            from datetime import datetime
            user = User(
                id=user_id,
                email=f"{user_id}@example.com",  # Default email format
                name=user_id  # Use the user_id as the name
            )
            session.add(user)
            session.commit()
            session.refresh(user)

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
        # Convert SQLModel objects to dictionaries for the agent
        messages = []
        for msg in conversation_history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        # Determine if the message is a general question or task-related
        is_general = is_general_question(request.message)

        # Import tools at the beginning to avoid scoping issues
        from ...tools.task_operations import (
            add_task_tool, list_tasks_tool, complete_task_tool,
            delete_task_tool, update_task_tool
        )

        # Prepare tools for the agent
        tools = [
            add_task_tool.model_dump(),
            list_tasks_tool.model_dump(),
            complete_task_tool.model_dump(),
            delete_task_tool.model_dump(),
            update_task_tool.model_dump()
        ]

        # Handle different model providers based on request
        if request.model_provider == "openai":
            # Use OpenAI Agents SDK for general questions with OpenAI
            try:
                agent_sdk = OpenAIAgentSDK(model_provider=request.model_provider)
                # Pass the full conversation history to maintain context
                agent_response = await agent_sdk.process_general_question_with_history(messages, user_id)

                # Format response to match expected structure
                formatted_response = MockResponse(
                    content=agent_response.get('content', ''),
                    tool_calls=agent_response.get('tool_calls', [])
                )

                # If the agent response contains tool calls, execute them
                if agent_response.get('tool_calls'):
                    for tool_call in agent_response.get('tool_calls', []):
                        # Execute the appropriate task operation based on the tool call
                        try:
                            if tool_call.get('name') == 'add_task':
                                # Execute add task operation
                                result = add_task_tool(**tool_call.get('arguments', {}), user_id=user_id)
                            elif tool_call.get('name') == 'list_tasks':
                                # Execute list tasks operation
                                result = list_tasks_tool(user_id=user_id)
                            elif tool_call.get('name') == 'complete_task':
                                # Execute complete task operation
                                task_id = tool_call.get('arguments', {}).get('task_id')
                                if task_id is not None:
                                    result = complete_task_tool(task_id=task_id, user_id=user_id)
                                else:
                                    print("Missing task_id for complete_task operation")
                            elif tool_call.get('name') == 'delete_task':
                                # Execute delete task operation
                                task_id = tool_call.get('arguments', {}).get('task_id')
                                if task_id is not None:
                                    result = delete_task_tool(task_id=task_id, user_id=user_id)
                                else:
                                    print("Missing task_id for delete_task operation")
                            elif tool_call.get('name') == 'update_task':
                                # Execute update task operation
                                task_id = tool_call.get('arguments', {}).get('task_id')
                                if task_id is not None:
                                    result = update_task_tool(task_id=task_id, user_id=user_id, **tool_call.get('arguments', {}))
                                else:
                                    print("Missing task_id for update_task operation")
                        except Exception as tool_error:
                            print(f"Error executing tool call {tool_call.get('name', 'unknown')}: {tool_error}")

            except Exception as e:
                print(f"Error with OpenAI Agents SDK: {e}")
                # Fallback to the original TodoAgent for task-related operations
                if not is_general:
                    # Run the agent with tool execution
                    try:
                        agent = TodoAgent(model_provider=request.model_provider)
                        formatted_response = agent.run_with_tool_execution(messages, tools, user_id)
                    except Exception as e:
                        print(f"Error initializing or running agent: {e}")
                        # Fallback to mock agent with explicit mock mode
                        from ...agents.todo_agent import TodoAgent
                        agent = TodoAgent(model_provider="openai")  # Use openai which defaults to mock mode
                        formatted_response = agent.run_with_tool_execution(messages, tools, user_id)

                        # If that still fails, create a basic mock response
                        if not formatted_response or not formatted_response.content:
                            formatted_response = MockResponse(
                                content="I'm here to help you manage your tasks. You can ask me to add, list, update, or complete tasks.",
                                tool_calls=[]
                            )
                else:
                    # For general questions, return an error message
                    formatted_response = MockResponse(
                        content=f"Sorry, I encountered an error processing your request: {str(e)}",
                        tool_calls=[]
                    )
        else:
            # For other model providers (like Gemini), use the original TodoAgent
            # Run the agent with tool execution
            try:
                agent = TodoAgent(model_provider=request.model_provider)
                formatted_response = agent.run_with_tool_execution(messages, tools, user_id)
            except Exception as e:
                print(f"Error initializing or running agent with provider {request.model_provider}: {e}")
                # Fallback to mock agent with explicit mock mode
                from ...agents.todo_agent import TodoAgent
                agent = TodoAgent(model_provider="openai")  # Use openai which defaults to mock mode
                formatted_response = agent.run_with_tool_execution(messages, tools, user_id)

                # If that still fails, create a basic mock response
                if not formatted_response or not formatted_response.content:
                    formatted_response = MockResponse(
                        content="I'm here to help you manage your tasks. You can ask me to add, list, update, or complete tasks.",
                        tool_calls=[]
                    )

        # Process tool calls if any
        tool_calls_result = []
        if hasattr(formatted_response, 'tool_calls') and formatted_response.tool_calls:
            for tool_call in formatted_response.tool_calls:
                if hasattr(tool_call, 'function'):
                    try:
                        tool_calls_result.append({
                            "name": tool_call.function.name,
                            "arguments": json.loads(tool_call.function.arguments)
                        })
                    except json.JSONDecodeError:
                        print(f"Error decoding arguments for tool call: {tool_call.function.name}")
                        tool_calls_result.append({
                            "name": tool_call.function.name,
                            "arguments": {}
                        })
                else:
                    # Handle tool calls from Agent SDK which might be formatted differently
                    tool_calls_result.append({
                        "name": tool_call.get('name', 'unknown'),
                        "arguments": tool_call.get('arguments', {})
                    })

        # Save assistant response
        assistant_message = Message(
            conversation_id=conversation.id,
            user_id=user_id,  # This could be an AI user ID in a real implementation
            role="assistant",
            content=formatted_response.content or "I'm sorry, but I couldn't generate a response to your message."
        )
        session.add(assistant_message)
        session.commit()

        return ChatResponse(
            conversation_id=conversation.id,
            response=formatted_response.content or "I'm sorry, but I couldn't generate a response to your message.",
            tool_calls=tool_calls_result
        )
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        print(f"Unexpected error in chat endpoint: {e}")
        # Log the error and return a user-friendly message
        return ChatResponse(
            conversation_id=request.conversation_id or 0,
            response="I'm sorry, but I encountered an unexpected error. Please try again later.",
            tool_calls=[]
        )