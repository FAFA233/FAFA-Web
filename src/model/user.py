from flask import Flask, request, jsonify
from sql import UserDB
class user():
    def __init__(self):
        self.user=UserDB()
        self.user_name=request.form.get('username')
        self.password=request.form.get('password')
        self.new_password=request.form.get('new_password')
        self.is_login=request.form.get('is_login')
        self.permissions=['login','register','change','delete']#用户权限列表

    def login(self,user_name ,is_login,password):
        self.user.check(user_name,password)
        self.user.change_login_status(user_name, is_login)
            
    def register(self,user_name,password):
        self.user.add(user_name,password)
        
    def change(self,user_name,new_password):
        self.user.change(user_name,new_password) 

    def delete(self,user_name,new_password):
        self.user.delete(user_name,new_password)
       
    def login_stastus(self,user_name,is_login):
        self.user.change_login_status(user_name,is_login)
 
    def has_permission(self,permission):#判断用户是否有权限
        return permission in self.permissions

class Administrator(user):
    def __init__(self):#赋予管理员三个权限
        super().__init__()
        self.permissions=['reset_password','delete_user','promote_admin']
        self.admin=UserDB()

    def delete_user(self,user_name,password):#删除用户
        user_delete=self.admin.find(user_name)
        if user_delete is not None and user_delete != self and user_delete != self.user_name:
            #判断要删除的用户对象是否为空,是否与管理员对象不同，并且用户名也不同。
            try:
                self.admin.check(user_name,password)#检查用户名是否与密码匹配
                self.admin.delete(user_name,password)#删除
            except:
                raise Exception("删除失败")
        else:
            raise Exception("用户未找到")
        
    def reset_password(self,user_name):
        user_reset=self.admin.find(user_name)
        if user_reset is not None and user_reset != self and user_reset != self.user_name:
            self.admin.change(user_name,"123456")
        else:
            raise Exception("重置失败")
        
    

        
    



   
        

        

        
        
    
        
    









