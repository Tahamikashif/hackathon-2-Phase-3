import sqlite3
import os

db_path = 'C:/Users/CSC/Desktop/Hackathon-5-phases/Hackathon-2/phase-3/backend/todo_chatbot_local.db'
print(f'Database path: {db_path}')
print(f'Database exists: {os.path.exists(db_path)}')

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f'Tables: {tables}')
    
    # Check each table
    for table_name in tables:
        table = table_name[0]
        try:
            cursor.execute(f'SELECT COUNT(*) FROM {table};')
            count = cursor.fetchone()[0]
            print(f'{table}: {count} records')
            
            # If it's message or conversation table and has records, show some
            if (table in ['message', 'conversation', 'user'] and count > 0):
                cursor.execute(f'SELECT * FROM {table} LIMIT 3;')
                rows = cursor.fetchall()
                print(f'  Sample {table} data: {rows}')
                
        except sqlite3.OperationalError as e:
            print(f'Error accessing {table}: {e}')
    
    conn.close()
else:
    print('Database file does not exist')