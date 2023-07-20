
import sqlite3

# 连接到数据库文件
conn = sqlite3.connect('articles.db')

# 创建一个游标对象，用于执行数据库操作
cursor = conn.cursor()

# 创建 articles 表格（如果表格不存在）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        article_name TEXT,
        author_name TEXT,
        create_time REAL,
        update_time REAL
    )
''')

# 添加测试数据
articles_data = [
    ('Article 1', 'Author 1', 1626748743.123, 1626748743.123),
    ('Article 2', 'Author 2', 1626748743.123, 1626748743.123),
    ('Article 3', 'Author 3', 1626748743.123, 1626748743.123),
    ('Article 4', 'Author 4', 1626748743.123, 1626748743.123),
]

# 执行插入数据的 SQL 语句
cursor.executemany('INSERT INTO articles (article_name, author_name, create_time, update_time) VALUES (?, ?, ?, ?)', articles_data)

# 提交更改
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()