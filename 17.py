import httpx


headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://match.yuanrenxue.cn/match/17",
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
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1704179119,1704275647",
    "tk": "8486590297633298700",
    "sessionid": "ajocken27f8lqdex8gkj3s033kj8f1h2",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1704179129,1704275680",
    "qpfccr": "true",
    "no-alert3": "true",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1704275708",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1704275710"
}
url = "https://match.yuanrenxue.cn/api/match/17"
global sum
sum=0

client=httpx.Client(http2=True)
for i in range(1,6):
    params = {
        "page": f"{i}"
    }
    response = client.get(url, headers=headers, cookies=cookies, params=params)

    data=response.json()
    print(response)
    data=data['data']
    print(data)
    for i in data:
        sum+=i['value']
print(sum)