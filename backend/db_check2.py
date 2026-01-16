import sqlite3
conn = sqlite3.connect('todo_chatbot.db')
cursor = conn.cursor()

# Get column info
cursor.execute('PRAGMA table_info(user)')
columns = cursor.fetchall()
print('User table structure:')
for col in columns:
    print(f'  {col}')

# Get all users with column names
cursor.execute('SELECT * FROM user')
users = cursor.fetchall()
print('\nAll users in the database:')
for user in users:
    print(f'  {user}')

conn.close()