from flask import Flask, request, jsonify
from .sql import UserDB

app = Flask(__name__)

class user():
    def __init__(self):
        with app.app_context():
            self.user=UserDB()
            self.user_id=request.form.get('user_id')
            self.user_name=request.form.get('username')
            self.password=request.form.get('password')
            self.new_password=request.form.get('new_password')
            self.is_login=request.form.get('is_login')
            self.permissions=['login','register','change','delete']#用户权限列表
        
    
    def login(self,user_id,user_name ,is_login,password):
        self.user.check(user_name,password)
        self.user.change_login_status(user_id, is_login)
            
    def register(self,user_name,password):
        self.user.add(user_name,password)
        
    def change(self,user_id,new_password):
        self.user.change(user_id,new_password) 

    def delete(self,user_id,user_name,new_password):
        self.user.delete(user_id,user_name,new_password)
       
    def login_stastus(self,user_id,is_login):
        self.user.change_login_status(user_id,is_login)
 
    def has_permission(self,permission):#判断用户是否有权限
        return permission in self.permissions

class Administrator(user):
    def __init__(self):#赋予管理员三个权限
        super().__init__()
        self.permissions=['reset_password','delete_user']
        self.admin=UserDB()


    def delete_user(self,user_id,user_name,password):#删除用户
        user_delete=self.admin.find(user_id)
        if user_delete is not None and user_delete != self and user_delete != self.user_id:
            #判断要删除的用户对象是否为空,是否与管理员对象不同，并且用户名也不同。
                self.admin.check(user_name,password)#检查用户名是否与密码匹配
                self.admin.delete(user_id,user_name,password)#删除
        else:       
             raise Exception("删除失败")


    def reset_password(self,user_id):
        user_reset=self.admin.find(user_id)
        if user_reset is not None and user_reset != self and user_reset != self.user_id:
            self.admin.change(user_id,"123456")
        else:
            raise Exception("重置失败")
        
    

        
    



   
        

        

        
        
    
        
    









