import requests
import json

def test_model_providers():
    """
    Test different model providers to ensure they work correctly
    """
    print("Testing different model providers...")
    
    api_url = "http://localhost:8000/api/v1/conversations/"
    user_id = "test-user-providers"
    
    # Test 1: OpenAI provider (should use LLM for general questions)
    print("\n1. Testing OpenAI provider for general question:")
    payload = {
        "message": "What is the meaning of life?",
        "model_provider": "openai"
    }
    
    response = requests.post(f"{api_url}{user_id}", json=payload)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Response: {data['response'][:100]}...")  # First 100 chars
        print(f"   Tool Calls: {data['tool_calls']}")
        print("   [OK] OpenAI provider working for general questions")
    else:
        print(f"   [ERROR] Failed: {response.text}")
    
    # Test 2: OpenAI provider for task operation
    print("\n2. Testing OpenAI provider for task operation:")
    payload = {
        "message": "Add a task to buy groceries",
        "model_provider": "openai"
    }
    
    response = requests.post(f"{api_url}{user_id}", json=payload)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Response: {data['response'][:100]}...")  # First 100 chars
        print(f"   Tool Calls: {data['tool_calls']}")
        print("   [OK] OpenAI provider working for task operations")
    else:
        print(f"   [ERROR] Failed: {response.text}")
    
    # Test 3: Other provider (should use task operations)
    print("\n3. Testing other provider (e.g., gemini) for task operation:")
    payload = {
        "message": "Add another task to call mom",
        "model_provider": "gemini"  # This should trigger the fallback to task operations
    }
    
    response = requests.post(f"{api_url}{user_id}", json=payload)
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Response: {data['response'][:100]}...")  # First 100 chars
        print(f"   Tool Calls: {data['tool_calls']}")
        print("   [OK] Other provider working for task operations")
    else:
        print(f"   [ERROR] Failed: {response.text}")

if __name__ == "__main__":
    test_model_providers()