from flask import Flask, request, jsonify
import sys
sys.path.append('D:/code/python/FAFA-Web/src/model')
from src.model.sql import UserDB
import logging
import os
# 配置日志记录
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建日志记录器
logger = logging.getLogger(__name__)

class User:
    userDB = UserDB()

    def __init__(self):
        pass

    def login(self, data):
        try:
            user_id = data['user_id']
            user_name = data['username']
            is_login = data['is_login']
            password = data['password']
            self.userDB.check(user_name, password)
            self.userDB.change_login_status(user_id, is_login)
            logger.info('用户登录成功：{}'.format(user_name))
        except Exception as e:
            pass

    def register(self, data):
        try:
            user_name = data['username']
            password = data['password']
            self.userDB.add(user_name, password)
            logger.info('用户注册成功：{}'.format(user_name))
        except Exception as e:
            pass

    def change(self, data):
        try:
            user_id = data['user_id']
            new_password = data['new_password']
            self.userDB.change(user_id, new_password)
            logger.info('用户密码修改成功：{}'.format(user_id))
        except Exception as e:
            pass

    def delete_user(self, data):
        try:
            user_id = data['user_id']
            user_name = data['username']
            new_password = data['new_password']
            self.userDB.delete(user_id, user_name, new_password)
            logger.info('用户删除成功：{}'.format(user_id))
        except Exception as e:
            pass

    def change_login_status(self, user_id, is_login):
        try:
            self.userDB.change_login_status(user_id, is_login)
            logger.info('用户登录状态更新成功：{}'.format(user_id))
        except Exception as e:
            pass

    def has_permission(self, permission):
        try:
            return permission in self.userDB.get_permissions()

        except Exception as e:
            pass
app = Flask(__name__)

class Administrator(User):
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
        
        
    

        
    



   
        

        

        
        
    
        
    









