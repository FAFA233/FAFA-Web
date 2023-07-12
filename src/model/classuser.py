from flask import Flask, request, jsonify
from sql import UserDB
class user():
    def __init__(self) :
        self.user=UserDB()
        user_name=request.form.get('username')
        password=request.form.get('password')
        new_password=request.form.get('new_password')
        is_login=request.form.get('is_login')
    def login( user_name ,password):
        try :
            self.user.find(user_name , password)
        except:
            print:("ERROR")
    
    def register( user_name,password ):
        try:
            self.user.add(user_name,password)
        except:
            print("ERROR")

    def change(user_name,new):
        try:
            self.user.change(user_name, new_password) 
        except:
            print("ERROR")       

    def delete(user_name, password):
        try:
            self.user.delete(user_name, new_password)
        except:
            print("ERROR")

    def login_stastus(user_name,is_login):
        try:
            self.user.change_login_status(user_name,is_login)
        except:
            print('ERROR')