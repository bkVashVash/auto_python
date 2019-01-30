# todo 如果后台接收失败，重新发送 json数据

import json
import os
import datetime
import requests

""" 重新发送当天采集数据 """
file_names = os.path.abspath('../') + '\\jsons\\bz2{}.json'.format(datetime.datetime.now().strftime('%Y-%m-%d'))
with open(file_names, 'rb') as file:
    str = file.read()
data = json.loads(str)

result = dict()
result['itemInfo'] = data[0]
# item中存在同名keywords
result['articleList'] = data[1:]

payload = json.dumps(result)
print(payload)

# #
headers = {'Content-Type': 'application/json'}

def cc():
    r = requests.post(url='https:XXXX.php',headers=headers,data=payload)
    print(json.loads(r.text))

# todo 这个并没有生效
try:
    cc()
except requests.exceptions.SSLError:
    cc()