import sqlite3
conn = sqlite3.connect('todo_chatbot.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print('Tables in database:')
for table in tables:
    table_name = table[0]
    print(f'  {table_name}')
    
    # Get row count for each table
    cursor.execute(f'SELECT COUNT(*) FROM `{table_name}`')
    count = cursor.fetchone()[0]
    print(f'    Row count: {count}')
    
    # Get first few rows if table has data
    if count > 0:
        cursor.execute(f'SELECT * FROM `{table_name}` LIMIT 3')
        rows = cursor.fetchall()
        for row in rows:
            print(f'      {row}')

conn.close()