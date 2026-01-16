import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OPENAI_API_KEY if not already set
if not os.getenv('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = 'test_key'

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")