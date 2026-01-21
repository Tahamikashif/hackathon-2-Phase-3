from fastapi import APIRouter
from .routers import task, chat

api_router = APIRouter()
api_router.include_router(task.router, prefix="/users/{user_id}", tags=["tasks"])
api_router.include_router(chat.router, prefix="/conversations", tags=["chat"])