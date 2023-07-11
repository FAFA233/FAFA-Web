from flask import Flask, request, jsonify
from model.user import User
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')#获取用户名和密码
    password = request.form.get('password')
    
    if User.login(username, password):
        return jsonify({'message': 'Login successful'})#返回json登陆成功
    else:
        return jsonify({'message': 'Login failed'})

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if User.register(username, password):
        return jsonify({'message': 'Register successful'})
    else:
        return jsonify({'message': 'Register failed'})

@app.route('/forgotton_password', methods=['POST'])
def forgotton_password():
    username =request.form.get('username')
    new_password = request.form.get('new_password')

    if User.forgotton_password(username,new_password):
        return jsonify ({'message': 'Changing successful'})
    else:
        return jsonify({'message': 'changing successful'})
    
if __name__ == '__main__':#run！
    app.run()
