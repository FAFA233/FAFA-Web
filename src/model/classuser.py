from flask import Flask, request, jsonify
from sql import UserDB
class user():
    def __init__(self) :
        self.user=UserDB()
        self.user_name=request.form.get('username')
        self.password=request.form.get('password')
        self.new_password=request.form.get('new_password')
        self.is_login=request.form.get('is_login')

    def login(self,user_name ,password):
        self.user.find(user_name )
            
    def register(self, user_name,password ):
        self.user.register(user_name,password)
        
    def change(self,user_name,new_password):
        self.user.change(user_name, new_password) 

    def delete(self,user_name, new_password):
        self.user.delete(user_name, new_password)
       
    def login_stastus(self,user_name,is_login):
        self.user.change_login_status(user_name,is_login)

class Administrators(user):
    def __init__(self):
        super().__init__()
    #用了父类 user 的 __init__ 方法,以便进行必要的初始化
    
    def promote_user(self,user_name):
        self.user.change(user_name,'admin')
    #将用户的权限提升至管理员

    def demote_user(self,user_name):
        self.user.change(user_name,'user')
    #把管理员权限降至普通用户

    def delete_user(self,user_name):
        self.user.delete(user_name,'')
    #删除指定用户

    def find_user(self,user_name):
        user_info = self.user.find(user_name)
        return user_info
    #查找用户信息,返回用户信息

