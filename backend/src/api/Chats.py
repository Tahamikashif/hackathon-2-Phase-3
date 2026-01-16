# api/chat.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from openai import OpenAI
import os
import json
from ..auth import get_current_user
from ..models.user import User

router = APIRouter(prefix="/api", tags=["chat"])

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ==================== MODELS ====================
class ChatRequest(BaseModel):
    message: str

class ChatRequestWithHistory(BaseModel):
    message: str
    history: Optional[List[Dict[str, str]]] = []

class ToolCall(BaseModel):
    name: str
    arguments: Dict[str, Any]

class ChatResponse(BaseModel):
    response: str
    tool_calls: Optional[List[ToolCall]] = None

# ==================== FUNCTION DEFINITIONS ====================
TODO_FUNCTIONS = [
    {
        "name": "create_todo",
        "description": "Create a new todo item for the user",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The todo title"
                },
                "description": {
                    "type": "string",
                    "description": "The todo description"
                },
                "priority": {
                    "type": "string",
                    "enum": ["low", "medium", "high"],
                    "description": "Priority level"
                },
                "due_date": {
                    "type": "string",
                    "description": "Due date in YYYY-MM-DD format"
                }
            },
            "required": ["title"]
        }
    },
    {
        "name": "list_todos",
        "description": "List all todos for the user",
        "parameters": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["all", "completed", "pending"],
                    "description": "Filter by status"
                },
                "priority": {
                    "type": "string",
                    "enum": ["low", "medium", "high"],
                    "description": "Filter by priority"
                }
            }
        }
    },
    {
        "name": "update_todo",
        "description": "Update an existing todo item",
        "parameters": {
            "type": "object",
            "properties": {
                "todo_id": {
                    "type": "integer",
                    "description": "The ID of the todo to update"
                },
                "title": {
                    "type": "string",
                    "description": "New title"
                },
                "description": {
                    "type": "string",
                    "description": "New description"
                },
                "status": {
                    "type": "string",
                    "enum": ["pending", "completed"],
                    "description": "New status"
                },
                "priority": {
                    "type": "string",
                    "enum": ["low", "medium", "high"],
                    "description": "New priority"
                }
            },
            "required": ["todo_id"]
        }
    },
    {
        "name": "delete_todo",
        "description": "Delete a todo item",
        "parameters": {
            "type": "object",
            "properties": {
                "todo_id": {
                    "type": "integer",
                    "description": "The ID of the todo to delete"
                }
            },
            "required": ["todo_id"]
        }
    },
    {
        "name": "mark_todo_complete",
        "description": "Mark a todo as completed",
        "parameters": {
            "type": "object",
            "properties": {
                "todo_id": {
                    "type": "integer",
                    "description": "The ID of the todo to mark as complete"
                }
            },
            "required": ["todo_id"]
        }
    },
    {
        "name": "search_todos",
        "description": "Search todos by keyword",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query"
                }
            },
            "required": ["query"]
        }
    }
]

# ==================== ENDPOINT 1: Simple Chat (from your code) ====================
@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat_endpoint(
    user_id: str,
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Main chat endpoint using OpenAI Chat Completions with function calling
    This matches your React component's endpoint: /${userId}/chat
    """
    try:
        # Verify user_id matches authenticated user
        if str(current_user.id) != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized access")
        
        # Create chat completion with function calling
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant for managing todos. Help users create, update, delete, and view their todo lists. Be friendly and concise."
                },
                {
                    "role": "user",
                    "content": request.message
                }
            ],
            functions=TODO_FUNCTIONS,
            function_call="auto",
            temperature=0.7
        )
        
        message = response.choices[0].message
        
        # Extract tool calls
        tool_calls = []
        if message.function_call:
            tool_calls.append(ToolCall(
                name=message.function_call.name,
                arguments=json.loads(message.function_call.arguments)
            ))
        
        response_text = message.content if message.content else "I'll help you with that."
        
        return ChatResponse(
            response=response_text,
            tool_calls=tool_calls if tool_calls else None
        )
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")


# ==================== ENDPOINT 2: Chat with History ====================
@router.post("/{user_id}/chat/with-history", response_model=ChatResponse)
async def chat_with_history_endpoint(
    user_id: str,
    request: ChatRequestWithHistory,
    current_user: User = Depends(get_current_user)
):
    """
    Chat endpoint with conversation history support
    """
    try:
        # Verify user_id matches authenticated user
        if str(current_user.id) != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized access")
        
        # Build message history
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant for managing todos. Help users create, update, delete, and view their todo lists."
            }
        ]
        
        # Add conversation history
        for msg in request.history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Add current message
        messages.append({
            "role": "user",
            "content": request.message
        })
        
        # Create completion
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            functions=TODO_FUNCTIONS,
            function_call="auto",
            temperature=0.7
        )
        
        message = response.choices[0].message
        
        # Extract tool calls
        tool_calls = []
        if message.function_call:
            tool_calls.append(ToolCall(
                name=message.function_call.name,
                arguments=json.loads(message.function_call.arguments)
            ))
        
        return ChatResponse(
            response=message.content if message.content else "Processing your request...",
            tool_calls=tool_calls if tool_calls else None
        )
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")


# ==================== ENDPOINT 3: Assistants API ====================
@router.post("/{user_id}/chat/assistant", response_model=ChatResponse)
async def chat_assistant_endpoint(
    user_id: str,
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Chat endpoint using OpenAI Assistants API
    More powerful for complex workflows and maintaining state
    """
    try:
        # Verify user_id matches authenticated user
        if str(current_user.id) != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized access")
        
        # Create or retrieve assistant
        # In production, you should store the assistant_id in database
        assistant = client.beta.assistants.create(
            name="Todo Assistant",
            instructions="You are a helpful assistant for managing todos. Help users create, update, and manage their todo lists efficiently.",
            model="gpt-4-turbo-preview",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "create_todo",
                        "description": "Create a new todo item",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string", "description": "The todo title"},
                                "description": {"type": "string", "description": "The todo description"},
                                "priority": {"type": "string", "enum": ["low", "medium", "high"]}
                            },
                            "required": ["title"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "list_todos",
                        "description": "List all todos for the user",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "status": {"type": "string", "enum": ["all", "completed", "pending"]}
                            }
                        }
                    }
                }
            ]
        )
        
        # Create a thread
        thread = client.beta.threads.create()
        
        # Add user message to thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=request.message
        )
        
        # Run the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        
        # Wait for completion
        import time
        max_attempts = 30
        attempts = 0
        while run.status in ["queued", "in_progress"] and attempts < max_attempts:
            time.sleep(1)
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            attempts += 1
        
        # Handle tool calls if any
        tool_calls = []
        if run.status == "requires_action":
            tool_outputs = []
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                tool_calls.append(ToolCall(
                    name=tool_call.function.name,
                    arguments=json.loads(tool_call.function.arguments)
                ))
                
                # Mock tool execution (implement actual logic)
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": json.dumps({"success": True, "message": "Tool executed successfully"})
                })
            
            # Submit tool outputs
            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )
            
            # Wait again
            attempts = 0
            while run.status in ["queued", "in_progress"] and attempts < max_attempts:
                time.sleep(1)
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
                attempts += 1
        
        # Get messages
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        
        # Get the assistant's response
        assistant_message = next(
            (msg for msg in messages.data if msg.role == "assistant"),
            None
        )
        
        response_text = ""
        if assistant_message and assistant_message.content:
            response_text = assistant_message.content[0].text.value
        
        # Clean up (optional - in production you might want to keep threads)
        client.beta.assistants.delete(assistant.id)
        
        return ChatResponse(
            response=response_text if response_text else "I'm processing your request.",
            tool_calls=tool_calls if tool_calls else None
        )
        
    except Exception as e:
        print(f"Error in assistant endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")


# ==================== ENDPOINT 4: Stream Response ====================
from fastapi.responses import StreamingResponse

@router.post("/{user_id}/chat/stream")
async def chat_stream_endpoint(
    user_id: str,
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Streaming chat endpoint for real-time responses
    """
    try:
        # Verify user_id matches authenticated user
        if str(current_user.id) != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized access")
        
        async def generate():
            response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for managing todos."},
                    {"role": "user", "content": request.message}
                ],
                stream=True
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield f"data: {json.dumps({'content': chunk.choices[0].delta.content})}\n\n"
            
            yield "data: [DONE]\n\n"
        
        return StreamingResponse(generate(), media_type="text/event-stream")
        
    except Exception as e:
        print(f"Error in stream endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")