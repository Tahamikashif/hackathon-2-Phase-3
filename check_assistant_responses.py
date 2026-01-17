import sqlite3

db_path = 'C:/Users/CSC/Desktop/Hackathon-5-phases/Hackathon-2/phase-3/backend/todo_chatbot_local.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all messages with role 'assistant' (these are the AI responses)
cursor.execute("SELECT id, conversation_id, role, content FROM message WHERE role='assistant' ORDER BY id DESC LIMIT 10;")
assistant_messages = cursor.fetchall()

print('Latest assistant responses in the database:')
for msg in assistant_messages:
    print(f'ID: {msg[0]}, Conv: {msg[1]}, Content: {repr(msg[3])}')

conn.close()