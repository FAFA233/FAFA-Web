import sqlite3

class UserInformation():

    def __init__(self, db_name):
        self.db_name = db_name

    def register(self, username, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # 检查用户名是否已存在
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            conn.close()
            return "用户名已存在"
        
        # 注册新用户
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return "注册成功"

    def login(self, username, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # 验证用户名和密码
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if cursor.fetchone():
            conn.close()
            return "登录成功"

        conn.close()
        return "用户名或密码错误"

class s