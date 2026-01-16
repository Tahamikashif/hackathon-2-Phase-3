import os
os.environ['OPENAI_API_KEY'] = 'dummy_key'

try:
    from src.main import app
    print("App imported successfully")
    
    # Test importing the agent
    from src.agents.todo_agent import TodoAgent
    print("TodoAgent imported successfully")
    
    # Test importing the tools
    from src.tools.task_operations import add_task
    print("Task operations imported successfully")
    
    # Test importing the database
    from src.database import get_session
    print("Database connection imported successfully")
    
    print("All imports successful - no obvious errors")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()