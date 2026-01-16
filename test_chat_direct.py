import asyncio
import json
from backend.src.api.chat import chat, ChatRequest
from backend.src.database import get_session
from sqlmodel import Session

async def test_chat_endpoint():
    # Create a proper request object
    request = ChatRequest(message="Add a task to buy Groceries")

    # Get a session
    session_gen = get_session()
    session = next(session_gen)

    try:
        # Call the chat endpoint directly
        result = await chat(
            user_id="demo-user-123",
            request=request,
            session=session
        )
        print("Chat endpoint result:", result)
    except Exception as e:
        print(f"Error calling chat endpoint: {e}")
        import traceback
        traceback.print_exc()
    finally:
        session.close()

# Run the test
asyncio.run(test_chat_endpoint())