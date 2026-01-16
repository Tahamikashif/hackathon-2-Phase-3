import os
import sys
import asyncio
sys.path.insert(0, './backend')

# Set the API key
os.environ['OPENAI_API_KEY'] = 'test_key'

# Import and test the agent directly
from backend.src.agents.todo_agent import TodoAgent

def test_agent():
    print("Testing the TodoAgent directly...")
    
    # Sample messages
    messages = [
        {"role": "user", "content": "Add a task to buy groceries"},
    ]
    
    # Sample tools
    from backend.src.tools.task_operations import (
        add_task_tool, list_tasks_tool, complete_task_tool,
        delete_task_tool, update_task_tool
    )
    
    tools = [
        add_task_tool.model_dump(),
        list_tasks_tool.model_dump(),
        complete_task_tool.model_dump(),
        delete_task_tool.model_dump(),
        update_task_tool.model_dump()
    ]
    
    # Create and run the agent
    agent = TodoAgent()
    
    try:
        result = agent.run_with_tool_execution(messages, tools, "demo-user-123")
        print("Agent response content:", result.content)
        print("Agent response tool_calls:", result.tool_calls)
        print("Success: Agent ran without errors")
    except Exception as e:
        print(f"Error running agent: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_agent()