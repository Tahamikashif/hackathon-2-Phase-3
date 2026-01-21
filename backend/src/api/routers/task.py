from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from ...database import get_session
from ...models.task import Task, TaskRead, TaskUpdate, TaskBase
from ...models.user import User
from ...tools.task_operations import (
    add_task, list_tasks, complete_task, delete_task, update_task
)

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskRead)
async def create_task(task_base: TaskBase, session: Session = Depends(get_session)):
    """Create a new task for a user"""
    result = await add_task(task_base.user_id, task_base.title, task_base.description)
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    # Fetch the created task from the database to return full details
    task = session.get(Task, result["task_id"])
    if not task:
        raise HTTPException(status_code=404, detail="Task not found after creation")
    return task

@router.get("/", response_model=List[TaskRead])
async def get_tasks(user_id: str, status: str = "all", session: Session = Depends(get_session)):
    """Get all tasks for a user with optional status filter"""
    tasks_data = await list_tasks(user_id, status)
    
    if tasks_data and "error" in tasks_data[0]:
        raise HTTPException(status_code=404, detail=tasks_data[0]["error"])
    
    # Convert the task data to TaskRead objects
    task_ids = [task["task_id"] for task in tasks_data if "task_id" in task]
    tasks = []
    
    for task_id in task_ids:
        task = session.get(Task, task_id)
        if task:
            tasks.append(task)
    
    return tasks

@router.put("/{task_id}", response_model=TaskRead)
async def update_task_endpoint(
    user_id: str, 
    task_id: int, 
    task_update: TaskUpdate, 
    session: Session = Depends(get_session)
):
    """Update a specific task for a user"""
    result = await update_task(
        user_id, 
        task_id, 
        title=task_update.title, 
        description=task_update.description
    )
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    # Fetch the updated task from the database to return full details
    task = session.get(Task, result["task_id"])
    if not task:
        raise HTTPException(status_code=404, detail="Task not found after update")
    return task

@router.patch("/{task_id}/complete", response_model=TaskRead)
async def complete_task_endpoint(user_id: str, task_id: int, session: Session = Depends(get_session)):
    """Mark a task as completed"""
    result = await complete_task(user_id, task_id)
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    # Fetch the updated task from the database to return full details
    task = session.get(Task, result["task_id"])
    if not task:
        raise HTTPException(status_code=404, detail="Task not found after completion")
    return task

@router.delete("/{task_id}")
async def delete_task_endpoint(user_id: str, task_id: int, session: Session = Depends(get_session)):
    """Delete a specific task for a user"""
    result = await delete_task(user_id, task_id)
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    return {"message": "Task deleted successfully"}