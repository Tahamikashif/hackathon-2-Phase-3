import sqlite3
conn = sqlite3.connect('todo_chatbot.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print('Tables in database:')
for table in tables:
    print(f'  {table[0]}')
    
    # Get row count for each table
    cursor.execute(f'SELECT COUNT(*) FROM `{table[0]}`')
    count = cursor.fetchone()[0]
    print(f'    Row count: {count}')

conn.close()