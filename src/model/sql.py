from sqlmodel import create_engine

class DB(object):
    def __init__(self, path):
        self.database_url = f"sqlite://{path}"
        self.connection = create_engine(self.database_url).connect()

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass

class UserDB(DB):
    def __init__(self):#UserDB类构造函数,调用DB类,将user.db作为参数传递给它
        super(UserDB, self).__init__("user.db")

    def add(self,name,password):#向users表中添加新用户,将信息插入到数据库中
        self.connection.execute(f"INSERT INTO users (name, password) VALUES ('{name}', '{password}')")
        
     
    def delete(self,name,password):#在user表中删除用户信息
        self.connection.execute(f"DELETE FROM users WHERE name='{name}' AND password='{password}'")
        #删除
    
    def change(self,name,password):#更改指定用户名称的密码
        self.connection.execute(f"UPDATE users SET password='{password}' WHERE name='{name}'")
        #更新条件的语法，指定要更新的记录的筛选条件。根据具体的表结构定义列名，用 name 列来匹配特定名称。
        

    def find(self,name) -> str:#查找指定用户,返回列表中用户信息
        result = self.connection.execute(f"SELECT * FROM users WHERE name='{name}'")
        # 查询条件,指定筛选条件.根据您具体的表结构定义的列名
        user = result.fechone()
        return user
    
    def change_login_status(self,name, is_login):#根据用户名字和登录状态更新is_login的值
            self.connection.execute(f"UPDATE users SET is_login={int(is_login)} WHERE name='{name}'")
            



