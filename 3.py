import requests
from collections import Counter

url='https://match.yuanrenxue.cn/jssm'
headers = {
    'Host': 'match.yuanrenxue.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://match.yuanrenxue.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie':'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1704179119; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1704179129; tk=8486590297633298700; sessionid=mco3ovp188vvsbxky9k5r6kl0fxncsen; qpfccr=true; no-alert3=true; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1704181627; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1704181634'

}
a_List=[]
session=requests.session()
session.headers=headers
for i in range(1,6):
    session.post(url)
    response=session.get(f'https://match.yuanrenxue.cn/api/match/3?page={i}')
    print(response.json())
    data=response.json()['data']
    for da in data:
        a_List.append(da['value'])
count = dict(Counter(a_List))
print(count)
max_value = sorted(count.items(), key=lambda a: a[-1])[-1][0]
print(max_value)