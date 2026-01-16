# from fastapi import FastAPI, Depends
# from .api.chat import router as chat_router
# from .database import create_db_and_tables
# from .auth import get_current_user
# from .models.user import User


# app = FastAPI(title="AI-Powered Todo Chatbot API")


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


# # Include the chat router
# app.include_router(chat_router)


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the AI-Powered Todo Chatbot API"}


# @app.get("/health")
# def health_check():
#     return {"status": "healthy"}


# # Example of a protected endpoint
# @app.get("/users/me")
# def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user


# main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .api.chat import router as chat_router
from .database import create_db_and_tables
from .auth import get_current_user
from .models.user import User


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
        "http://127.0.0.1:3002"
    ],  # Common development origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Include the chat router
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