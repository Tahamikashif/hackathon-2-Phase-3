# AI-Powered Todo Chatbot Backend

This is the backend for the AI-powered todo chatbot application. It provides REST APIs for managing tasks and conversations with the AI assistant.

## Features

- **Task Management**: Create, read, update, and delete tasks
- **AI Chat Interface**: Natural language processing for task management
- **User Management**: User authentication and authorization
- **Conversation Tracking**: Maintain conversation history with the AI assistant

## API Endpoints

### Task Management
- `GET /api/v1/users/{user_id}/tasks` - Get all tasks for a user
- `POST /api/v1/users/{user_id}/tasks` - Create a new task
- `PUT /api/v1/users/{user_id}/tasks/{task_id}` - Update a task
- `PATCH /api/v1/users/{user_id}/tasks/{task_id}/complete` - Mark a task as completed
- `DELETE /api/v1/users/{user_id}/tasks/{task_id}` - Delete a task

### Chat Interface
- `POST /api/v1/conversations/{user_id}` - Send a message to the AI assistant

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:
```
DATABASE_URL=sqlite:///./todo_chatbot_local.db
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

3. Start the server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

## Database Models

- **User**: Represents a user in the system
- **Task**: Represents a task with title, description, and completion status
- **Conversation**: Represents a conversation thread
- **Message**: Represents individual messages within a conversation

## Architecture

The backend follows a modular architecture with:

- `src/models/` - Database models using SQLModel
- `src/tools/` - Task operation tools for the AI agent
- `src/api/routers/` - API routes for different functionalities
- `src/agents/` - AI agent implementations
- `src/database.py` - Database connection and setup