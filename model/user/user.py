from sqlmodel import Field, Session,SQLModel,create_engine
from sql import sql

class User(SQLModel,table = True):
    def __init__(self):
        self.id: int = Field(default = None,primary_key = True)
        self.username: str = Field(default = None)
        self.password: str = Field(default = None)
        self.__db: sql = sql("user.db")


    def register():
       
        

    def login():
     