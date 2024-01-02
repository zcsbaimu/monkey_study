import json

import requests
import base64

headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://match.yuanrenxue.cn/match/12",
    "sec-ch-ua": "^\\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1704179119,1704275647,1704351344",
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "8486590297633298700",
    "sessionid": "ivanb48sx4so2sb5k6xtbr3ywuge4dto",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1704179129,1704275680,1704351377",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1704351377",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1704351389"
}
url = "https://match.yuanrenxue.cn/api/match/12"
global sume
sume=0
for i in range(1,6):
    data=f'yuanrenxue{i}'
    data_bytes=data.encode()
    base_data=base64.b64encode(data_bytes)
    print(base_data)
    params = {
        "page": f"{i}",
        "m": base_data
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.text)
    data = response.json()
    print(response)
    data = data['data']
    print(data)
    for i in data:
        sume += i['value']
print(sume)