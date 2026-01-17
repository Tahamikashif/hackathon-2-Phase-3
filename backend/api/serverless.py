# api/serverless.py - Serverless function for Vercel
import os
import sys
from pathlib import Path
import json
from urllib.parse import parse_qs

# Add the parent directory to the path so we can import from src
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from mangum import Mangum
from src.main import app  # Import the main FastAPI app

# Create the mangum handler for Vercel
handler = Mangum(app)

def main(event, context):
    return handler(event, context)

# Export the handler for Vercel
lambda_handler = handler