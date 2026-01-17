# api/index.py - Vercel API route for the backend
import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from src
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from src.api.chat import router as chat_router
from src.database import create_db_and_tables
from src.auth import get_current_user
from src.models.user import User

# Set environment variables for Vercel deployment
os.environ.setdefault("DATABASE_URL", os.getenv("DATABASE_URL", "sqlite:///./todo_chatbot_local.db"))

# Create the FastAPI app
app = FastAPI(title="AI-Powered Todo Chatbot API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "https://localhost:3000",
        "https://localhost:8000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3002",
        os.getenv("FRONTEND_URL", ""),  # Custom domain for frontend
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include the chat router - note: we're not adding /api prefix here since Vercel will handle routing
app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Todo Chatbot API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Example of a protected endpoint
@app.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Create the mangum handler for Vercel
handler = Mangum(app)

# Export the handler for Vercel
def main(event, context):
    return handler(event, context)