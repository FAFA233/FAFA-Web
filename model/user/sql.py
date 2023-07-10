from sqlalchemy import create_engine

class Sql():
    def __init__(self, path : str):
        database_url = f"sqlite:///{path}"  # SQLite数据库URL
        self.engine = create_engine(database_url)  # 创建SQLite数据库引擎并链接到数据库

    def add(self, user):#执行添加用户

        with self.engine.connect() as connection:
            connection.execute(f"INSERT INTO users (name, password) VALUES ('{user['name']}', '{user['password']}')")
            #将用户的名称(name)和密码(password)插入到 users 表的相应列中，以创建一个新的用户记录
        return "添加成功"
    
    def delete(self, name, password):
        with self.engine.connect() as connection:
            connection.execute(f"DELETE FROM users WHERE name='{name}' AND password='{password}'")
            #将用户的名称(name)和密码(password)删除
        return "删除成功"

    def find(self, name):#执行查找用户
        with self.engine.connect() as connection:
            result = connection.execute(f"SELECT * FROM users WHERE name='{name}'")
            # 查询条件,指定筛选条件.根据您具体的表结构定义的列名
        return result.fetchall()
        #是用于从查询结果中获取所有行的数据，返回一个包含所有匹配记录的列表

    def change(self, name, password):#执行用户数据更新
        with self.engine.connect() as connection:
            connection.execute(f"UPDATE users SET password='{password}' WHERE name='{name}'")
            #更新条件的语法，指定要更新的记录的筛选条件。根据具体的表结构定义列名，用 name 列来匹配特定名称。
        return "修改成功"