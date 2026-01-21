from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from src.api.routers.chat import router as chat_router
from src.database import create_db_and_tables

# Load environment variables
load_dotenv()

# Create the FastAPI app
app = FastAPI(title="AI-Powered Todo Chatbot API")

# Add CORS middleware - include common frontend origins
cors_origins = [
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
    # Add Vercel deployment URLs
    "https://your-frontend-deployment.vercel.app",  # Replace with your actual frontend URL
    "https://*.vercel.app",  # Allow any Vercel deployment
    "http://localhost:3004",  # Additional port that Next.js might use
    "http://localhost:3005",
    "http://localhost:3006",
    "http://localhost:3007",
    "http://localhost:3008",
    "http://localhost:3009",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    """Create database tables on startup"""
    create_db_and_tables()

# Include the chat router - the route will be /api/v1/conversations/{user_id}
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

# For Vercel deployment, make sure the app instance is named 'app'
# This is what Vercel will look for
app_var = app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), log_level="info")