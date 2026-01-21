import asyncio
import asyncpg
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_chatbot_local.db")

async def test_connection():
    if DATABASE_URL.startswith("postgresql"):
        try:
            # Extract connection parameters from the URL
            # Format: postgresql://user:password@host:port/database
            import re
            pattern = r"postgresql://([^:]+):([^@]+)@([^:]+):?(\d+)?/(.+)(?:\?(.+))?"
            
            # For Neon URL format: postgresql://user:pass@ep-xxx.region.aws.neon.tech/dbname?sslmode=require
            import urllib.parse
            parsed = urllib.parse.urlparse(DATABASE_URL)
            
            conn = await asyncpg.connect(
                host=parsed.hostname,
                port=parsed.port or 5432,
                user=parsed.username,
                password=parsed.password,
                database=parsed.path[1:],  # Remove leading slash
                ssl='require'
            )
            
            # Test the connection
            result = await conn.fetchval('SELECT version();')
            print(f"Successfully connected to Neon database!")
            print(f"PostgreSQL version: {result}")
            
            # Close the connection
            await conn.close()
            print("Connection closed.")
            
        except Exception as e:
            print(f"Error connecting to Neon database: {e}")
    else:
        print("Using SQLite database - skipping Neon connection test")

if __name__ == "__main__":
    asyncio.run(test_connection())