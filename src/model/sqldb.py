import sqlite3

conn = sqlite3.connect(database='user.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sql (
        user_id TEXT,
        user_name TEXT,
        password TEXT
    )
''')

cursor.execute('''
    INSERT INTO sql (user_id, user_name, password)
    VALUES ('1', 'John Doe', 'password123'),
           ('2', 'Jane Smith', 'password456'),
           ('3', 'Alice Johnson', 'password789')
''')


conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()