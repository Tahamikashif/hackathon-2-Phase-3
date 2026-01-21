"""
Test script to verify OpenRouter API integration with the enhanced Agent SDK
"""
import asyncio
import os
from dotenv import load_dotenv
from src.Agent_sdk.main import OpenAIAgentSDK, is_general_question

# Load environment variables
load_dotenv()

async def test_openrouter_integration():
    """Test the OpenRouter API integration"""
    print("Testing OpenRouter API integration...")
    
    try:
        # Initialize the agent SDK
        agent_sdk = OpenAIAgentSDK()
        print("[OK] Agent SDK initialized successfully")
        
        # Test general question
        test_messages = [
            {"role": "user", "content": "Hello, how are you today?"}
        ]
        
        print("\nTesting general question response...")
        result = await agent_sdk.process_general_question_with_history(test_messages, "test_user_123")
        
        print(f"Response: {result['content']}")
        print(f"Tool calls: {result['tool_calls']}")
        print(f"Usage: {result['usage']}")
        
        # Test if message classification works
        general_msg = "What's the weather like today?"
        task_msg = "Add a new task to buy groceries"
        
        print(f"\nMessage '{general_msg}' classified as general: {is_general_question(general_msg)}")
        print(f"Message '{task_msg}' classified as general: {is_general_question(task_msg)}")
        
        # Test with a more complex conversation
        complex_messages = [
            {"role": "user", "content": "I need to remember to buy groceries later"},
            {"role": "assistant", "content": "Sure, I can help you with that. Would you like me to add this as a task?"},
            {"role": "user", "content": "Yes, please add it as a task"},
        ]
        
        print("\nTesting complex conversation...")
        result = await agent_sdk.process_general_question_with_history(complex_messages, "test_user_123")
        
        print(f"Response: {result['content']}")
        print(f"Tool calls: {result['tool_calls']}")
        
        print("\n[SUCCESS] OpenRouter API integration test completed successfully!")
        
    except ValueError as e:
        print(f"[ERROR] Configuration error: {e}")
        print("Make sure you have set the OPENROUTER_API_KEY in your environment variables.")
    except Exception as e:
        print(f"[ERROR] Error during testing: {e}")

if __name__ == "__main__":
    asyncio.run(test_openrouter_integration())