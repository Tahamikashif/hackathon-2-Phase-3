@echo off
echo Starting the AI Todo Chatbot Backend Server...
cd backend
set DATABASE_URL=sqlite:///./todo_chatbot.db
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000