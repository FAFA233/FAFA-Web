from flask import Flask, request, jsonify
from src.model import User


def login():
    if username := request.form.get('username') is None:
        username = ""
    #获取用户名和密码
    if password := request.form.get('password') is None:
        password = ""
    
    if User().login(username, password):
        return jsonify({'message': 'Login successful'})#返回json登陆成功
    else:
        return jsonify({'message': 'Login failed'})


def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if User.register(username, password):
        return jsonify({'message': 'Register successful'})
    else:
        return jsonify({'message': 'Register failed'})


def forgotton_password():
    username =request.form.get('username')
    new_password = request.form.get('new_password')

    if User.forgotton_password(username,new_password):
        return jsonify ({'message': 'Changing successful'})
    else:
        return jsonify({'message': 'changing successful'})
    

