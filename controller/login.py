from flask import Flask, request, jsonify
from model.user import user
app = Flask(__name__)

@app.route('/login', methods=['POST'])#'/login'为url
class user_information:
    username = request.form.get('username')
    password = request.form.get('password')#从前端获取账号密码

def login():

    if(user.login(user_information.username,user_information.password)==True):
        return "Login successful"  # 返回登录成功的提示信息
    else:
        return "Login failed"
    
if __name__ == '__main__':
    app.run()
