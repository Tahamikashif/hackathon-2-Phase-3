# AI-Powered Todo Chatbot

An AI-powered Todo chatbot that allows users to manage tasks using natural language. The system uses OpenAI Agents SDK for reasoning and Model Context Protocol (MCP) for task operations, following a stateless server architecture where all conversation and task state is persisted in a database.

## Features

- Natural language task management
- AI-powered task operations via MCP tools
- Persistent conversation context
- Stateless backend architecture
- User authentication

## Tech Stack

- **Backend**: FastAPI, SQLModel, PostgreSQL (Neon)
- **AI Layer**: OpenAI Agents SDK
- **MCP**: Model Context Protocol SDK
- **Frontend**: ChatKit UI
- **Authentication**: Better Auth

## Setup

1. Clone the repository
2. Install backend dependencies: `cd backend && pip install -r requirements.txt`
3. Install frontend dependencies: `cd frontend && npm install`
4. Set up environment variables (see `.env.example`)
5. Run database migrations: `cd backend && alembic upgrade head`
6. Start the MCP server: `cd backend && python mcp_server.py`
7. Start the backend: `cd backend && uvicorn main:app --reload`
8. Start the frontend: `cd frontend && npm run dev`

## Architecture

The system follows a stateless architecture where all conversation and task state is persisted in the database. The AI agent uses MCP tools to perform task operations.

### Request Flow

1. Client sends message to `POST /api/{user_id}/chat`
2. Backend fetches conversation + messages from database
3. Message history is assembled for the agent
4. User message is persisted
5. Agent is executed with MCP tools
6. Agent invokes MCP tool(s) as needed
7. Tool results are returned to the agent
8. Assistant response is generated
9. Assistant response and tool calls are persisted
10. Response is returned to client