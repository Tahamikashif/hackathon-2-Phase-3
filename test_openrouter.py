import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Test the OpenRouter API directly
async def test_openrouter_api():
    openrouter_api = os.getenv("OPENROUTER_API_KEY")
    if not openrouter_api:
        print("OPENROUTER_API_KEY not found in environment variables")
        return
    
    client = AsyncOpenAI(api_key=openrouter_api, base_url="https://openrouter.ai/api/v1")
    
    try:
        print("Testing OpenRouter API with a simple request...")
        response = await client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # Using a more reliable model
            messages=[{"role": "user", "content": "Hello, how are you?"}],
            max_tokens=100
        )
        
        print(f"Response received: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage}")
        
    except Exception as e:
        print(f"Error calling OpenRouter API: {e}")

# Run the test
import asyncio
asyncio.run(test_openrouter_api())