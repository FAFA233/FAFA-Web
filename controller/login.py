from flask import Flask, request, jsonify
from model import user
app = Flask(__name__)

@app.route('/login', methods=['POST'])#'/login'为url
def login():
    # 从前端表单中获取账号密码
    username = request.form.get('username')
    password = request.form.get('password')
    

    return "Login successful"  # 返回登录成功的提示信息

if __name__ == '__main__':
    app.run()