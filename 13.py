import json
import re
import requests
session=requests.Session()

headers = { 'cookie': 'sessionid=ivanb48sx4so2sb5k6xtbr3ywuge4dto'}

response=session.get('https://match.yuanrenxue.cn/match/13',headers=headers)
print(response.text)
data=re.findall("'(.*?)'",response.text)
ck=''
for i in data:
    ck+=i
print(ck)

session.cookies.set(ck.split('=')[0],ck.split('=')[1])
global num
num=0
for i in range(1,6):
    url = f"https://match.yuanrenxue.cn/api/match/13?page={i}"

    response = session.get(url)
    print(session.cookies)
    print(response.text)
    data=json.loads(response.text)
    for i in data['data']:
        num+=i['value']
print(num)