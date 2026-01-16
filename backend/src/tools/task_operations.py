from sqlmodel import Session, select
from typing import Dict, Any, List, Optional
from ..database import get_session
from ..models.task import Task, TaskRead
from ..models.user import User


# Mock classes for MCP tools since the actual package isn't available
class Tool:
    def __init__(self, name, description, parameters, handler):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.handler = handler

    def model_dump(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters
            }
        }


class ToolResult:
    def __init__(self, content: str):
        self.content = content


# Tool: add_task
async def add_task(user_id: str, title: str, description: Optional[str] = None) -> Dict[str, Any]:
    """
    Create a new task
    
    Args:
        user_id: Identifier for the user creating the task
        title: Title of the task
        description: Detailed description of the task (optional)
    
    Returns:
        Dictionary with task_id, status, and title
    """
    with next(get_session()) as session:
        # Verify user exists
        user = session.exec(select(User).where(User.id == user_id)).first()
        if not user:
            return {
                "error": f"User with id {user_id} does not exist",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Create new task
        task = Task(
            user_id=user_id,
            title=title,
            description=description,
            completed=False
        )
        session.add(task)
        session.commit()
        session.refresh(task)
        
        return {
            "task_id": task.id,
            "status": "pending",
            "title": task.title
        }


# Tool: list_tasks
async def list_tasks(user_id: str, status: Optional[str] = "all") -> List[Dict[str, Any]]:
    """
    Retrieve tasks for a user
    
    Args:
        user_id: Identifier for the user whose tasks to retrieve
        status: Filter tasks by status ("all", "pending", "completed") - defaults to "all"
    
    Returns:
        List of task objects with properties
    """
    with next(get_session()) as session:
        # Verify user exists
        user = session.exec(select(User).where(User.id == user_id)).first()
        if not user:
            return [{"error": f"User with id {user_id} does not exist"}]
        
        # Build query based on status filter
        query = select(Task).where(Task.user_id == user_id)
        
        if status == "pending":
            query = query.where(Task.completed == False)
        elif status == "completed":
            query = query.where(Task.completed == True)
        # For "all", no additional filter is needed
        
        tasks = session.exec(query).all()
        
        result = []
        for task in tasks:
            result.append({
                "task_id": task.id,
                "status": "completed" if task.completed else "pending",
                "title": task.title,
                "description": task.description
            })
        
        return result


# Tool: complete_task
async def complete_task(user_id: str, task_id: int) -> Dict[str, Any]:
    """
    Mark a task as completed
    
    Args:
        user_id: Identifier for the user who owns the task
        task_id: Unique identifier for the task to complete
    
    Returns:
        Dictionary with task_id, status, and title
    """
    with next(get_session()) as session:
        # Verify user exists
        user = session.exec(select(User).where(User.id == user_id)).first()
        if not user:
            return {
                "error": f"User with id {user_id} does not exist",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Get the task
        task = session.get(Task, task_id)
        if not task:
            return {
                "error": f"Task with id {task_id} does not exist",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Verify task belongs to user
        if task.user_id != user_id:
            return {
                "error": f"Task with id {task_id} does not belong to user {user_id}",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Update task completion status
        task.completed = True
        session.add(task)
        session.commit()
        session.refresh(task)
        
        return {
            "task_id": task.id,
            "status": "completed",
            "title": task.title
        }


# Tool: delete_task
async def delete_task(user_id: str, task_id: int) -> Dict[str, Any]:
    """
    Delete a task
    
    Args:
        user_id: Identifier for the user who owns the task
        task_id: Unique identifier for the task to delete
    
    Returns:
        Dictionary with task_id, status, and title
    """
    with next(get_session()) as session:
        # Verify user exists
        user = session.exec(select(User).where(User.id == user_id)).first()
        if not user:
            return {
                "error": f"User with id {user_id} does not exist",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Get the task
        task = session.get(Task, task_id)
        if not task:
            return {
                "error": f"Task with id {task_id} does not exist",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Verify task belongs to user
        if task.user_id != user_id:
            return {
                "error": f"Task with id {task_id} does not belong to user {user_id}",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Delete the task
        session.delete(task)
        session.commit()
        
        return {
            "task_id": task.id,
            "status": "pending" if not task.completed else "completed",
            "title": task.title
        }


# Tool: update_task
async def update_task(
    user_id: str, 
    task_id: int, 
    title: Optional[str] = None, 
    description: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update task title or description
    
    Args:
        user_id: Identifier for the user who owns the task
        task_id: Unique identifier for the task to update
        title: New title for the task (optional)
        description: New description for the task (optional)
    
    Returns:
        Dictionary with task_id, status, and title
    """
    with next(get_session()) as session:
        # Verify user exists
        user = session.exec(select(User).where(User.id == user_id)).first()
        if not user:
            return {
                "error": f"User with id {user_id} does not exist",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Get the task
        task = session.get(Task, task_id)
        if not task:
            return {
                "error": f"Task with id {task_id} does not exist",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Verify task belongs to user
        if task.user_id != user_id:
            return {
                "error": f"Task with id {task_id} does not belong to user {user_id}",
                "task_id": None,
                "status": None,
                "title": None
            }
        
        # Update task fields if provided
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        
        session.add(task)
        session.commit()
        session.refresh(task)
        
        return {
            "task_id": task.id,
            "status": "completed" if task.completed else "pending",
            "title": task.title
        }


# Register tools with the MCP framework
add_task_tool = Tool(
    name="add_task",
    description="Create a new task",
    parameters={
        "type": "object",
        "properties": {
            "user_id": {"type": "string", "description": "Identifier for the user creating the task"},
            "title": {"type": "string", "description": "Title of the task"},
            "description": {"type": "string", "description": "Detailed description of the task (optional)"}
        },
        "required": ["user_id", "title"]
    },
    handler=add_task
)

list_tasks_tool = Tool(
    name="list_tasks",
    description="Retrieve tasks for a user",
    parameters={
        "type": "object",
        "properties": {
            "user_id": {"type": "string", "description": "Identifier for the user whose tasks to retrieve"},
            "status": {"type": "string", "enum": ["all", "pending", "completed"], "description": "Filter tasks by status (defaults to 'all')"}
        },
        "required": ["user_id"]
    },
    handler=list_tasks
)

complete_task_tool = Tool(
    name="complete_task",
    description="Mark a task as completed",
    parameters={
        "type": "object",
        "properties": {
            "user_id": {"type": "string", "description": "Identifier for the user who owns the task"},
            "task_id": {"type": "integer", "description": "Unique identifier for the task to complete"}
        },
        "required": ["user_id", "task_id"]
    },
    handler=complete_task
)

delete_task_tool = Tool(
    name="delete_task",
    description="Delete a task",
    parameters={
        "type": "object",
        "properties": {
            "user_id": {"type": "string", "description": "Identifier for the user who owns the task"},
            "task_id": {"type": "integer", "description": "Unique identifier for the task to delete"}
        },
        "required": ["user_id", "task_id"]
    },
    handler=delete_task
)

update_task_tool = Tool(
    name="update_task",
    description="Update task title or description",
    parameters={
        "type": "object",
        "properties": {
            "user_id": {"type": "string", "description": "Identifier for the user who owns the task"},
            "task_id": {"type": "integer", "description": "Unique identifier for the task to update"},
            "title": {"type": "string", "description": "New title for the task (optional)"},
            "description": {"type": "string", "description": "New description for the task (optional)"}
        },
        "required": ["user_id", "task_id"]
    },
    handler=update_task
)