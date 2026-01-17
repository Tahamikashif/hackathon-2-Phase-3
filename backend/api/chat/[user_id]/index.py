# api/chat/[user_id]/index.py - Vercel API route for chat endpoint
import os
import sys
from pathlib import Path
import json
from urllib.parse import parse_qs

# Add the parent directory to the path so we can import from src
parent_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(parent_dir))

from src.agents.todo_agent import TodoAgent
from src.database import get_session
from src.models.user import User
from sqlmodel import select

def handler(event, context):
    # Extract the user_id from the path
    path_parts = event['path'].split('/')
    user_id = path_parts[-2] if len(path_parts) >= 4 else None
    
    if not user_id:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': 'Missing user_id'})
        }
    
    # Handle preflight requests
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': '{}'
        }
    
    if event['httpMethod'] == 'POST':
        # Parse the request body
        body = json.loads(event['body']) if event['body'] else {}
        message = body.get('message', '')
        model_provider = body.get('model_provider', 'openai')
        
        # Create user if they don't exist
        session_gen = get_session()
        session = next(session_gen)
        
        user = session.exec(select(User).where(User.id == user_id)).first()
        if not user:
            from src.models.user import User as UserModel
            from datetime import datetime
            user = UserModel(
                id=user_id,
                email=f"{user_id}@example.com",
                name=user_id
            )
            session.add(user)
            session.commit()
            session.refresh(user)
        
        # Create a conversation-like structure for the agent
        messages = [
            {"role": "user", "content": message, "user_id": user_id}
        ]
        
        # Use the TodoAgent to generate a response
        agent = TodoAgent(model_provider=model_provider)
        response = agent.run_with_tool_execution(messages, [], user_id)
        
        # Return the response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'conversation_id': 1,  # Simple ID for this example
                'response': response.content,
                'tool_calls': []
            })
        }
    
    return {
        'statusCode': 405,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'error': 'Method not allowed'})
    }