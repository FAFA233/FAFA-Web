import sqlite3
import json
from flask import Flask
app=Flask(__name__)
@app.route('/get_article_titles_from_database', methods=['POST'])
def get_article_titles_from_database(database_path):
    # 连接到数据库)
    conn = sqlite3.connect(database_path)
    
    # 创建游标对象
    cursor = conn.cursor()

    # 执行查询语句，提取所有文章标题
    cursor.execute("SELECT article_name FROM articles")
    
    # 获取所有查询结果
    results = cursor.fetchall()
    
    # 关闭数据库连接
    conn.close()
    
    # 从结果中提取文章标题
    article_titles = [result[0] for result in results]
    
    # 转换为JSON格式
    json_data = json.dumps(article_titles)
    return json_data

if __name__ == '__main__':
    get_article_titles_from_database('E:/workspace/FAFA-Web/articles.db')
    app.run() 
    