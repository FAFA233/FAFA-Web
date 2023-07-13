from flask import Flask, request, jsonify
from sql import UserDB
class user():
    def __init__(self):
        self.user=UserDB()
        self.user_name=request.form.get('username')
        self.password=request.form.get('password')
        self.new_password=request.form.get('new_password')
        self.is_login=request.form.get('is_login')
        self.permissions=[]#用户权限列表

    def login(self,user_name ,password):
        self.user.find(user_name,password)
            
    def register(self, user_name,password):
        self.user.add(user_name,password)
        
    def change(self,user_name,new_password):
        self.user.change(user_name, new_password) 

    def delete(self,user_name, new_password):
        self.user.delete(user_name, new_password)
       
    def login_stastus(self,user_name,is_login):
        self.user.change_login_status(user_name,is_login)

    def has_permission(self,permission):#判断用户是否有权限
        return permission in self.permissions

class Administrator(user):
    def __init__(self):#赋予管理员三个权限
        super().__init__()
        self.permissions=['reset_password','creat_user','delete_user']

    def delete_user(self,user_name):#删除用户
        self.user.delete(user_name)

    def creat_user(self,user_name,password):#创建用户
        self.user.add(user_name,password)

    def reset_password(self,user_name,password):#重置用户密码
        self.user.change(user_name,password)


