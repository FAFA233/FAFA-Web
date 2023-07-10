from flask import Flask, request, jsonify
from model.user import User
app = Flask(__name__)

@app.route('/login', methods=['POST'])#'/login'为url
class user_info:
    username = request.form.get('username')
    password = request.form.get('password')#从前端获取账号密码

def login():

    if(User.login(user_info.username,user_info.password)==True):
        return "Login successful"  # 返回登录成功的提示信息
    else:
        return "Login failed"

def register():
    if(User.register(user_info.username , user_info.password)):
        return "registe successfully"
    
if __name__ == '__main__':
    app.run()
