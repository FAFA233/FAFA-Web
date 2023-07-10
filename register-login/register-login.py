import sqlite3

class user():
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def register(self,username,password):#用户注册
        self.username = username
        self.password = password

    
       


@app.route('/login',methods=['post'])
def login():#用户登录
    data = request.get_json()
    name = data['name']
    password = data['password']
    """从request对象中获取请求的JSON数据,
    并将其存储在data变量中"""

    user_info = UserInformation(name = user_info.name,password = user_info.password)

    with Session(engine) as session:#创建一个会话对象session.会话对象负责管理数据库连接和事务处理
        user = session.exec(User).where(User.name == user_info.name).first()
        """筛选条件，用于指定查询的用户名必须与输入的 name 变量匹配。.first()
          表示只返回查询结果的第一个对象。"""
        if user and user.password == user_info.password:
            return jsonify({'message':'登录成功'})
    return jsonify({'message':'登录失败'})
    """如果用户的名字和密码匹配，返回登录成功。否则返回登录失败"""


def forget():#用户忘记密码
    data = request.get_json()
    name = data['name']
    new_password = data['new_password']#用户输入的新密码
    user_info = UserInformation(name = user_info.name,password = '')#重置用户的密码为空

    with Session(engine) as session:
        user =  session.exec(User).where(User.name == user_info.name).first()#找到数据库中用户名字
        if user:
            user.password = new_password
            session.commit()
            return jsonify({'message':'密码重置成功'})
        #如果用户设置了新密码，则把之前密码替换为新密码，并把数据提交到数据库中，返回“密码重置成功”

if __name__=='__main__':
    app.run()
    mport sqlite3

class User:
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