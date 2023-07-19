import requests
import json
from flask import Flask, jsonify

app=Flask(__name__)
@app.route('/display_json')#url

def print_json():
    """
        从一言获取json
    Returns:
        json里的名言部分
    """
    url = 'https://v1.hitokoto.cn/?c=a&c&i&d&k=c'#限定获取句子的种类
    js= requests.get(url)
    l_str=json.loads(js.text)
    return l_str['hitokoto']
    

if __name__ == '__main__':
    app.run()
'''
果当前模块是作为主程序运行(即__name__ 的值为__main__)
则执行特定的操作。如果模块是被导入的，则不执行这些操作。
'''