import requests
import random
import json
UAlist=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0'
]
headers = {
    'User-Agent': random.choice(UAlist),
    'Referer': 'https://pintia.cn/problem-sets/1852233710680576000/exam/rankings?page=0',
    'Accept': 'application/json',
    'cookie':'_bl_uid=k4mnb034uqgdaaa4soqUktkvRvth; _ga=GA1.1.143543713.1730527944; PTASession=fdb05ca4-ac24-4fe9-95f9-86b6095b03c5; _ga_ZHCNP8KECW=GS1.1.1731587451.3.1.1731589094.60.0.0; JSESSIONID=51E157FD42B40E22497976DE0B6DDD5C'
}
params = {
    'page': '0',
    'limit': '4111',
}
response = requests.get(
    'https://pintia.cn/api/problem-sets/1852233710680576000/rankings',
    headers=headers,
    params=params
)
print(response.headers['Content-Type'])
data = response.json()
print(data)
with open('第n页.json','w', encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False)