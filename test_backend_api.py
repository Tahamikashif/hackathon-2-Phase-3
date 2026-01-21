import requests
import json

# Test the backend API directly
def test_backend_api():
    url = "http://localhost:8000/api/v1/conversations/test-user"
    
    # Test general question
    payload = {
        "message": "Hello, how are you?"
    }
    
    print("Testing general question...")
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    # Test task-related message
    payload = {
        "message": "Add a task to buy groceries"
    }
    
    print("\nTesting task-related message...")
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    test_backend_api()