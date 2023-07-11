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
    url = 'https://v1.hitokoto.cn'
    js= requests.get(url)
    l_str=json.loads(js.text)
    return l_str['hitokoto']
    

if __name__ == '__main__':
    app.run()
