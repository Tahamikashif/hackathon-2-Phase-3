import os
os.environ['OPENAI_API_KEY'] = 'test_key'

# Test database connection
from backend.src.database import engine
from backend.src.models.task import Task
from sqlmodel import select

try:
    # Try to query the database
    from sqlmodel import Session
    with Session(engine) as session:
        # Count tasks for our test user
        statement = select(Task).where(Task.user_id == "demo-user-123")
        tasks = session.exec(statement).all()
        print(f"Found {len(tasks)} tasks for demo-user-123")
        
        # Try to add a task directly
        from backend.src.models.task import Task
        new_task = Task(
            title="Test task from direct DB access",
            description="This is a test task added directly to the database",
            user_id="demo-user-123",
            completed=False
        )
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        print(f"Successfully added task with ID: {new_task.id}")
        
except Exception as e:
    print(f"Database error: {e}")
    import traceback
    traceback.print_exc()