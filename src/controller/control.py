from flask import Flask, request, jsonify
from src.model.classuser import user

app=Flask(__name__)
user=user()


def login():
    user_name = request.form.get('username')
    password = request.form.get('password')
    try:
        user.login(user_name, password)
    except:
        pass
        

def register():
    user_name = request.form.get('username')
    password = request.form.get('password')
    try:
        user.register(user_name, password)
    except:
        pass

def change_password():
    user_name = request.form.get('username')
    new_password = request.form.get('new_password')
    try:
        user.change(user_name, new_password)
    except:
        pass

def delete():
    user_name = request.form.get('username')
    password = request.form.get('password')
    try:
        user.delete(user_name, password)
    except:
        pass

def login_status():
    user_name = request.form.get('username')
    is_login = request.form.get('is_login')
    try:
        user.login_stastus(user_name, is_login)
    except:
        pass

if __name__ == '__main__':
    app.run()


