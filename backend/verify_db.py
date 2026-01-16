import sqlite3
conn = sqlite3.connect('todo_chatbot_local.db')
cursor = conn.cursor()

# Check conversations table
cursor.execute('SELECT COUNT(*) FROM conversation;')
conv_count = cursor.fetchone()[0]
print('Number of conversations:', conv_count)

# Check messages table
cursor.execute('SELECT COUNT(*) FROM message;')
msg_count = cursor.fetchone()[0]
print('Number of messages:', msg_count)

# Show some sample conversations
if conv_count > 0:
    cursor.execute('SELECT * FROM conversation LIMIT 5;')
    conversations = cursor.fetchall()
    print('Sample conversations:', conversations)

# Show some sample messages
if msg_count > 0:
    cursor.execute('SELECT * FROM message LIMIT 5;')
    messages = cursor.fetchall()
    print('Sample messages:', messages)

conn.close()