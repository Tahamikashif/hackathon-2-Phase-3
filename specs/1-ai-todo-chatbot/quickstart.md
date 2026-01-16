# Quickstart Guide: AI-Powered Todo Chatbot

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Git
- Access to OpenAI API
- Access to Neon Serverless PostgreSQL

## Environment Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Install frontend dependencies:
   ```bash
   cd ../frontend
   npm install
   ```

## Configuration

1. Create a `.env` file in the backend directory with the following variables:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   DATABASE_URL=your_neon_database_url_here
   BETTER_AUTH_SECRET=your_auth_secret_here
   BETTER_AUTH_URL=http://localhost:3000
   ```

2. Set up your Neon Serverless PostgreSQL database and update the DATABASE_URL accordingly.

## Running the Application

1. Run database migrations:
   ```bash
   cd backend
   python -m alembic upgrade head
   ```

2. Start the MCP server:
   ```bash
   python mcp_server.py
   ```

3. In a new terminal, start the main backend server:
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

4. In another terminal, start the frontend:
   ```bash
   cd frontend
   npm run dev
   ```

## Using the Chat Interface

1. Navigate to `http://localhost:3000` in your browser
2. Authenticate using the Better Auth login
3. Start chatting with the AI assistant using natural language:
   - "Add a task to buy groceries"
   - "What tasks do I have?"
   - "Mark the meeting task as completed"
   - "Delete the old task"

## API Usage

To interact with the API directly:

```bash
curl -X POST http://localhost:8000/api/user-123/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Add a task to call mom"
  }'
```

## Development

For development, you can run the backend tests:
```bash
cd backend
python -m pytest
```

And frontend tests:
```bash
cd frontend
npm test
```