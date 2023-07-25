from flask import Flask, request, jsonify
import uuid
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

    """用户初始化所用的方法，其将为系统创建一个新的未登录的用户对象"""
    def __init__(self, username : str, password : str):
        self.username = username
        self.password = password
        self.is_login = False

    """用户在创建之后可调用的其中一种方法，即为通俗的登录过程，在此方法中，用户将获得True的登录状态"""
    def login(self, user_id):
        try:
            self.user_id = user_id
            self.userDB.check(self.username, self.password)
            self.userDB.change_login_status(self.user_id, True)
            logger.info('用户登录成功：{}'.format(self.username))
            self.is_login = True
        except Exception as e:
            logger.error("出现错误，用户登录失败：" + e.__str__())

    """用户可选择的途径，注册将为用户创建新的身份，并提供True的登录状态"""
    def register(self):
        self.user_id = str(uuid.uuid4())
        try:
            self.userDB.add(self.user_id, self.username, self.password)
            self.userDB.change_login_status(self.user_id, True)
            logger.info('用户注册成功：{}'.format(self.username))
            self.is_login = True
        except Exception as e:
            logger.error("出现错误，用户注册失败：" + e.__str__())

    """用户可对自身的密码进行修改"""
    def change(self, user_id, user_name, new_password):
        try:
            self.userDB.change(self.user_id, new_password)
            logger.info('用户密码修改成功：{}'.format(self.user_id))
        except Exception as e:
            logger.error("出现错误，密码修改失败：" + e.__str__())

    def delete_user(self, data):
        # TODO: ?
        try:
            user_id = data['user_id']
            user_name = data['username']
            new_password = data['new_password']
            self.userDB.delete(user_id, user_name, new_password)
            logger.info('用户删除成功：{}'.format(user_id))
        except Exception as e:
            logger.error("出现错误，用户删除失败：" + e.__str__())

    def has_permission(self, permission):
        # TODO: ?
        try:
            return permission in self.userDB # TODO:

        except Exception as e:
            pass

class Administrator(User):
    def __init__(self):#赋予管理员三个权限
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
        
        
    

        
    



   
        

        

        
        
    
        
    









