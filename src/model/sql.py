from sqlmodel import create_engine,SQLModel

import uuid

class SModel(SQLModel):
    user_id: str
    user_name: str
    password:str

class DB(object):
    def __init__(self,path):

        self.engine = create_engine("sqlite:///{path}")
        SQLModel.metadata.create_all(self.engine)
        self.connection = self.engine.connect()


    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass

    def check(self):
        pass

class UserDB(DB):
    def __init__(self):#UserDB类构造函数,调用DB类,将user.db作为参数传递给它
        super(UserDB, self).__init__("sqlite:///user.db")

    def add(self,name, password):#向users表中添加新用户,将信息插入到数据库中
        self.user_id=str(uuid.uuid4())
        self.connection.execute(f"INSERT INTO users (user_id, username, password) VALUES ('{self.user_id}', '{name}', '{password}')")
        
     
    def delete(self, user_id, username, password):#在user表中删除用户信息
        self.connection.execute(f"DELETE FROM users WHERE user_id='{user_id}' AND name='{username}' AND password='{password}'")
    
    def change(self, user_id, password):#更改指定用户ID的密码
        self.connection.execute(f"UPDATE users SET password='{password}' WHERE user_id='{user_id}'")
        #更新条件的语法，指定要更新的记录的筛选条件。根据具体的表结构定义列名，用 user_id 列来匹配特定用户ID。
        

    def find(self, user_id) -> str:#查找指定用户,返回列表中用户信息
        result = self.connection.execute(f"SELECT * FROM users WHERE user_id='{user_id}'")
        # 查询条件,指定筛选条件。根据您具体的表结构定义的列名
        user = result.fetchone()
        return user
    
    def change_login_status(self, user_id, is_login):#根据用户ID和登录状态更新is_login的值
        self.connection.execute(f"UPDATE users SET is_login={int(is_login)} WHERE user_id='{user_id}'")
            
 
    def check(self,username, password):#检查用户名与密码是否匹配
        mate="SELECT username FROM users WHERE user_id=? AND username=? AND password=?"
        result=self.connection.execute(mate, (username, password)).fetchone()
        if result is None:
            raise Exception("用户名与密码未匹配")

  
        
    

