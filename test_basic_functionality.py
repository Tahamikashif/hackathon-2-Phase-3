"""
Simple test to verify the basic functionality of the AI Todo Chatbot
"""
import asyncio
from backend.src.tools.task_operations import add_task, list_tasks, complete_task, delete_task, update_task
from backend.src.database import create_db_and_tables
from backend.src.models.user import User
from sqlmodel import Session, select
from backend.src.database import engine


async def test_basic_functionality():
    print("Setting up database...")
    create_db_and_tables()

    # Create a test user first
    user_id = "test_user_123"
    user_email = "test@example.com"

    with Session(engine) as session:
        # Check if user already exists
        existing_user = session.exec(select(User).where(User.id == user_id)).first()
        if not existing_user:
            # Create a new user
            user = User(id=user_id, email=user_email)
            session.add(user)
            session.commit()
            print(f"Created test user: {user_id}")
        else:
            print(f"Using existing test user: {user_id}")

    print("\n1. Testing add_task...")
    result = await add_task(user_id, "Buy groceries", "Milk, eggs, bread")
    print(f"Add task result: {result}")
    task_id = result.get("task_id")

    if task_id:
        print(f"\n2. Testing list_tasks...")
        tasks = await list_tasks(user_id)
        print(f"Tasks for user: {tasks}")

        print(f"\n3. Testing update_task...")
        update_result = await update_task(user_id, task_id, title="Buy groceries and fruits")
        print(f"Update task result: {update_result}")

        print(f"\n4. Testing complete_task...")
        complete_result = await complete_task(user_id, task_id)
        print(f"Complete task result: {complete_result}")

        print(f"\n5. Testing list_tasks again (should show completed task)...")
        tasks_after_complete = await list_tasks(user_id)
        print(f"Tasks after completion: {tasks_after_complete}")

        print(f"\n6. Testing delete_task...")
        delete_result = await delete_task(user_id, task_id)
        print(f"Delete task result: {delete_result}")

        print(f"\n7. Testing list_tasks after deletion (should be empty)...")
        tasks_after_delete = await list_tasks(user_id)
        print(f"Tasks after deletion: {tasks_after_delete}")

    print("\nBasic functionality test completed!")


if __name__ == "__main__":
    asyncio.run(test_basic_functionality())