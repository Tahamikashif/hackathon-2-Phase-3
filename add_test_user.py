import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('backend/todo_chatbot.db')
cursor = conn.cursor()

# Insert a test user
user_id = "demo-user-123"
email = "demo@example.com"
name = "Demo User"
created_at = datetime.utcnow().isoformat()
updated_at = datetime.utcnow().isoformat()

try:
    cursor.execute("""
        INSERT INTO user (id, email, name, created_at, updated_at) 
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, email, name, created_at, updated_at))
    
    conn.commit()
    print(f"User {user_id} created successfully!")
except sqlite3.IntegrityError:
    print(f"User {user_id} already exists.")
    # Update the existing user instead
    cursor.execute("""
        UPDATE user 
        SET email=?, name=?, updated_at=?
        WHERE id=?
    """, (email, name, updated_at, user_id))
    conn.commit()

conn.close()
print("Test user setup complete.")