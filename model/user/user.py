from sqlmodel import Field, Session,SQLModel,create_engine
from sql import Sql

class User(SQLModel,table = True):
    def __init__(self):
        self.id: int = Field(default = None,primary_key = True)
        self.username: str = Field(default = None)
        self.password: str = Field(default = None)
        self.__db: Sql = Sql("user.db")

    def register(self,username : str, password : str):
        """实现注册

        Args:
            username (str): 用户名
            password (str): 密码
        """
        user = {
           "name":username,
           "password":password
        }
        #创建了一个名为 db 的变量，并实例化了一个名为 sql 的类，并传递了 "user.db" 作为参数。
        self.__db.add(user) #对象的数据插入到数据库适当位置，以创建一个新的用户记录
        return True
        
    def login(self,username : str, password : str):
        """实现登录

        Args:
            username (str): 用户名
            password (str): 密码
        """
        
        result = self.__db.find(username)#函数调用 “db” 的数据库对象，“username” 作为搜索条件查找并返回所有与给定用户名匹配的记录
        if len(result) > 0:#判断列表长度是否大于0
            stored_password = result[0]['password']
            #result[0]表示获取结果列表result中的第一个元素（记录）,然后通过['password']来获取该记录中名为"password"的字段的值。
            if password == stored_password:
                return True#密码正确返回true
            else:
                return False#否则返回false
        else:
            return False#如果找不到用户名，返回false
    
    def forgotton_password(self,username : str,new_password : str):
        """实现修改密码

        Args:
            username (str): 用户名
            new_password (str): 新密码
        """
        result = self.__db.find(username)
        if result:
            self.__db.change(username,new_password)#如果找到用户,则修改他的密码
            return True#修改成功返回True
        else:
            return False#否则返回False
            
        
