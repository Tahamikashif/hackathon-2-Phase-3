import requests
import json

def test_frontend_backend_interaction():
    """
    This script simulates how the frontend sends requests to the backend
    and receives LLM responses
    """
    print("Testing frontend-backend interaction for LLM responses...")
    
    # Backend API endpoint
    api_url = "http://localhost:8000/api/v1/conversations/"
    
    # Test user ID
    user_id = "test-user-frontend"
    
    # Test 1: General question
    print("\n1. Testing general question to LLM:")
    general_payload = {
        "message": "Hello, how are you today?"
    }
    
    response = requests.post(f"{api_url}{user_id}", json=general_payload)
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"   Conversation ID: {data['conversation_id']}")
        print(f"   LLM Response: {data['response']}")
        print(f"   Tool Calls: {data['tool_calls']}")
        print("   [OK] General question processed successfully")
    else:
        print(f"   [ERROR] Failed to get response: {response.text}")
    
    # Test 2: Task operation
    print("\n2. Testing task operation:")
    task_payload = {
        "message": "Add a new task to buy groceries"
    }
    
    response = requests.post(f"{api_url}{user_id}", json=task_payload)
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"   Conversation ID: {data['conversation_id']}")
        print(f"   LLM Response: {data['response']}")
        print(f"   Tool Calls: {data['tool_calls']}")
        print("   [OK] Task operation processed successfully")
    else:
        print(f"   [ERROR] Failed to get response: {response.text}")
    
    # Test 3: List tasks
    print("\n3. Testing list tasks:")
    list_payload = {
        "message": "What tasks do I have?"
    }
    
    response = requests.post(f"{api_url}{user_id}", json=list_payload)
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"   Conversation ID: {data['conversation_id']}")
        print(f"   LLM Response: {data['response']}")
        print(f"   Tool Calls: {data['tool_calls']}")
        print("   [OK] List tasks processed successfully")
    else:
        print(f"   [ERROR] Failed to get response: {response.text}")

if __name__ == "__main__":
    test_frontend_backend_interaction()