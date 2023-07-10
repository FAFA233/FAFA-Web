from sqlalchemy import create_engine

class sql():
    def __init__(self):
        database_ur1 = "sqlite:///database.db"#SQLite数据库app = Flask(__name__)的URL
        engine = create_engine(database_ur1)#创建SQLite数据库引擎并链接到数据库

    def add(self,user):#添加用户
        with self.engine.connect() as connection:
            connection.execute(f"INSERT INTO users (name, password) VALUES ('{user['name']}', {user['password']})")
            #这条插入语句的目的是将用户的名称(name)和密码(password)插入到 users 表的相应列中，以创建一个新的用户记录
        return "添加成功"

    def find(self,name):#查找用户
        with self.engine.connect() as connection:#执行查询
            result=connection.execute(f"SELECT * FROM users WHERE names='{name}'")
            #connection.execute() 方法用于执行 SQL 查询语句,WHERE names='{name}'：这是查询条件的语法，指定筛选条件
            return result.fetchall()#查询结果中获取所有行的数据
        
    def change(self,name,password):
        with self.engine.connect() as connection:
            connection.execute(f"UPDATE users SETS password='{password}'WHERE name='{name}'")
            #将密码更新
        return "修改成功"
