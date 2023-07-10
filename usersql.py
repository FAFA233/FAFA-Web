from sqlmodel import Field, Session, SQLModel,  create_engine
from sqlalchemy import inspect


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(default=None)
    password: str = Field(default=None)

class sql_connection:

    def __init__(self, db_url: str):
        self.db_url = db_url

    def create_database(self):              #创建数据库和其中的表格
        engine = create_engine(self.db_url)#创建引擎
        SQLModel.metadata.create_all(engine)#创建表格

    def get_session(self):
        engine = create_engine(self.db_url)#创建一个数据库引擎
        return Session(engine)#返回Session创建的数据库会话对象
    
    def add_user(self, user: User):
        session = self.get_session()
        session.add(user)
        session.commit()
        session.close()

    def delete_user(self, user_id: int):
        session = self.get_session()
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def update_user(self, user: User):
        session = self.get_session()
        user_in_db = session.get(User, user.id)
        if user_in_db:
            inspect_user = inspect(user)
            for attr in inspect_user.dict:
                if attr != "id":
                    setattr(user_in_db, attr, getattr(user, attr))
            session.commit()
        session.close()

    def get_user(self, user_id: int):
        session = self.get_session()
        user = session.get(User, user_id)
        session.close()
        return user
