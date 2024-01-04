# -*- coding: utf-8 -*-
import time
import math
import random
import pywasm
import requests


def js_wasm():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
    cookie={
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1704179119,1704275647,1704351344",
    "qpfccr": "true",
    "sessionid": "ivanb48sx4so2sb5k6xtbr3ywuge4dto",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1704179129,1704275680,1704351377",
    "no-alert3": "true",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1704361137",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1704364652"
}

    sum_num = 0
    for i in range(1, 6):
        t = int(time.time())
        t1 = int(t / 2)
        t2 = int(t / 2 - math.floor(random.random() * 50 + 1))
        runtime = pywasm.load("./main.wasm")
        r = runtime.exec("encode", [t1, t2])
        m = f"{r}|{t1}|{t2}"
        params = {
            "m": m,
            "page": i,
        }
        response = requests.get(url="http://match.yuanrenxue.com/api/match/15", params=params, headers=headers,cookies=cookie)
        print(response.text)
        response=response.json()
        print(response)
        for num in response["data"]:
            sum_num += num["value"]
    print(sum_num)


if __name__ == "__main__":
    js_wasm()
