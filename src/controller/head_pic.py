from flask import request,jsonify,Flask
import os

app=Flask(__name__)

# 设置文件上传目录,名为avatars
app.config['UPLOAD_FOLDER'] = 'avatars/'

@app.route('/upload_file', methods=['POST'])

def upload_file():
    # 获取用户传递的文件
    avatar = request.files.get('avatar')
    user_id = request.form.get('user_id')

    if avatar and user_id:
        #是一个用于拼接路径的函数调用,生成唯一的路径
        user_folder=os.path.join(app.config['UPLOAD_FOLDER'], user_id)
        os.makedirs(user_folder) # 创建一个文件夹
        avatar.save(os.path.join(user_folder,user_id))
        avatar_url = f"/avatars/{user_id}/" 
        return jsonify({'avatar_url': avatar_url})
    else:
        return jsonify({'message': '头像上传失败'})
    
if __name__ == '__main__':
    app.run() 
    