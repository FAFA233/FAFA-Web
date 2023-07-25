from flask import Flask, request, jsonify
import sys
print(sys.path)
sys.path.append('E:/workspace/FAFA-Web/')
from src.model.user import User
import logging
# 配置日志记录
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建日志记录器
logger = logging.getLogger(__name__)
app=Flask(__name__)

"""用户登录入口，接收必要数据，并修改用户的登录状态

Returns:
    Response: 向用户发回json消息，并返回一个Response类型的结果报告
"""
@app.route('/login', methods=['POST'])
def login():
    try:
        user_id = request.form.get('user_id')
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        is_login = request.form.get('is_login')
        user = User(username, password) # 创建出的新用户对象 
        user.login(user_id)
        login_status()
        logger.info('用户成功登录：{}'.format(username))
        return jsonify({'message': '登录成功'}) 
    except Exception as e:
        logger.error('登录失败：{}'.format(e))
        return jsonify({'message': '登录失败'}) 

"""用户注册入口，将接收必要数据，创建用户对象并完成注册

Returns:
    Response: 向用户发回json消息，并返回一个Response类型的结果报告
"""
@app.route('/register', methods=['POST'])
def register():
    try:
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))

        user = User(username, password) # 创建出的新用户对象 
        user.register()
        logger.info('用户成功注册：{}'.format(username))
        return jsonify({'message': '注册成功'}) 
    except Exception as e:
        logger.error('注册：{}'.format(e))
        return jsonify({'message': '注册失败'}) 

"""此入口用于修改密码

Returns:
    _type_: _description_
"""
@app.route('/change_password', methods=['POST'])    
def change_password():
    # TODO: ?
    user_id = request.form.get('user_id')
    user_name = request.form.get('username')
    new_password = request.form.get('new_password')
    try:
        # User.change(user_id, user_name, new_password) # ?
        logger.info('修改成功：{}'.format(user_name))
        return jsonify({'message': '修改成功'}) 
    except Exception as e:
        logger.error('修改失败：{}'.format(e))
        return jsonify({'message': '修改失败'}) 
    
# @app.route('/delete', methods=['POST'])   
# def delete():
#     user_id = request.form.get('user_id')
#     user_name = request.form.get('username')
#     password = request.form.get('password')
#     try:
#         user.delete(user_id,user_name, password)
#         logger.info('删除成功：{}'.format(user_name))
#         return jsonify({'message': '删除成功'}) 
#     except Exception as e:
#         logger.error('删除失败：{}'.format(e))
#         return jsonify({'message': '删除失败'}) 
        
# def login_status():
#     user_name = request.form.get('username')
#     is_login = request.form.get('is_login')
#     try:
#         user.login_stastus(user_name, is_login)
#         logger.info('登录状态修改成功：{}'.format(user_name))
#     except Exception as e:
#         logger.error('登录状态修改失败：{}'.format(e))

