from flask import Flask, request, jsonify
import sys
sys.path.append('E:/workspace/FAFA-Web/')
from src.model.user import user
import logging
# 配置日志记录
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建日志记录器
logger = logging.getLogger(__name__)
user=user()

def login():
    user_id = request.form.get('user_id')
    user_name = request.form.get('username')
    password = request.form.get('password')
    is_login = request.form.get('is_login')
    try:
        user.login(user_id,user_name,is_login, password)
        login_status()
        logger.info('用户成功登录：{}'.format(user_name))
        return jsonify({'message': '登录成功'}) 
    except Exception as e:
        logger.error('登录失败：{}'.format(e))
        return jsonify({'message': '登录失败'}) 

def register():
    user_name = request.form.get('username')
    password = request.form.get('password')
    try:
        user.register(user_name,password)
        logger.info('用户成功注册：{}'.format(user_name))
        return jsonify({'message': '注册成功'}) 
    except Exception as e:
        logger.error('注册：{}'.format(e))
        return jsonify({'message': '注册失败'}) 
    
def change_password():
    user_name = request.form.get('username')
    new_password = request.form.get('new_password')
    try:
        user.change(user_name, new_password)
        logger.info('修改成功：{}'.format(user_name))
        return jsonify({'message': '修改成功'}) 
    except Exception as e:
        logger.error('修改失败：{}'.format(e))
        return jsonify({'message': '修改失败'}) 
    
def delete():
    user_id = request.form.get('user_id')
    user_name = request.form.get('username')
    password = request.form.get('password')
    try:
        user.delete(user_id,user_name, password)
        logger.info('删除成功：{}'.format(user_name))
        return jsonify({'message': '删除成功'}) 
    except Exception as e:
        logger.error('删除失败：{}'.format(e))
        return jsonify({'message': '删除失败'}) 
    
def login_status():
    user_name = request.form.get('username')
    is_login = request.form.get('is_login')
    try:
        user.login_stastus(user_name, is_login)
        logger.info('登录状态修改成功：{}'.format(user_name))
    except Exception as e:
        logger.error('登录状态修改失败：{}'.format(e))



