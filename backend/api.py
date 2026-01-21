import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.api.routers.chat import router as chat_router
from src.database import create_db_and_tables

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="AI-Powered Todo Chatbot API")

# Add CORS middleware - expanded to include more potential frontend origins
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
        "http://localhost:3004",
        "http://localhost:3005",
        "http://localhost:3006",
        "http://localhost:3007",
        "http://localhost:3008",
        "http://localhost:3009",
        "https://*.vercel.app",  # Allow any Vercel deployment
        "https://*.netlify.app",  # Allow Netlify deployments
        "https://*.now.sh",  # Legacy Now.sh domains
        "https://your-frontend-deployment.vercel.app"  # Replace with your actual frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    """Create database tables on startup"""
    try:
        create_db_and_tables()
    except Exception as e:
        print(f"Error creating database tables: {e}")

# Include the chat router
app.include_router(chat_router, prefix="/api/v1/conversations")

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to the AI-Powered Todo Chatbot API",
        "status": "running",
        "description": "This is a FastAPI-powered backend for managing tasks with AI assistance",
        "endpoints": {
            "health": "/health",
            "tasks": "/api/v1/users/{user_id}/tasks",
            "chat": "/api/v1/conversations/{user_id}"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# For Vercel deployment
app_var = app