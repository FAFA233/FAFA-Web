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
        }#user里面有name，password
        db = sql("user.db")#创建了一个名为 db 的变量，并实例化了一个名为 sql 的类，并传递了 "user.db" 作为参数。
        db.add(user) #对象的数据插入到数据库的适当位置，以创建一个新的用户记录
        print("注册成功")
        
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
                print("登录成功")
            else:
                print("密码错误")
        else:
            print("用户不存在")