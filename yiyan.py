import requests
import json
url = 'https://v1.hitokoto.cn'
js= requests.get(url)
l_str=json.loads(js.text)
print(l_str['hitokoto'])