from sqlmodel import Field, Session,SQLModel,create_engine
from sql import sql

class User(SQLModel,table = True):
    def __init__(self):
        self.id: int = Field(default = None,primary_key = True)
        self.username: str = Field(default = None)
        self.password: str = Field(default = None)
        self.__db: sql = sql("user.db")

    def register(username, password):
        """实现注册

        Args:
            username (str): 用户名
            password (str): 密码
        """
        user = {
           "name":username,
           "password":password
       }
        db = sql("user.db")
        db.add(user)
        return True
        
    def login(username : str, password : str):
        """实现登录

        Args:
            username (str): 用户名
            password (str): 密码
        """
        db = sql("user.db")
        result = db.find(username)#函数调用 “db” 的数据库对象，“username” 作为搜索条件查找并返回所有与给定用户名匹配的记录
        if len(result) > 0:#判断列表长度是否大于0
            stored_password = result[0]['password']#
            if password == stored_password:
                return True
            else:
                return False
        else:
            return "用户不存在"