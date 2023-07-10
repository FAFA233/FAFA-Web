from sqlmodel import Field, Session,SQLModel,create_engine
from sql import sql

class User(SQLModel,table = True):
    def __init__(self):
        self.id: int = Field(default = None,primary_key = True)
        self.username: str = Field(default = None)
        self.password: str = Field(default = None)
        self.__db: sql = sql("user.db")

    def register(username,password):

       user = {
           "name":username,
           "password":password
       }
       db = sql("user.db")
       db.add(user)
       return "注册成功"
        
    def login(username,password):
              
        db = sql("user.db")
        result = db.find(username)

        if len(result) > 0:
            stored_password = result[0]['password']
            if password == stored_password:
                return True
            else:
                return False
        else:
            return "用户不存在"