import requests
import json
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Referer': 'https://pintia.cn/problem-sets/1852233710680576000/exam/rankings?page=0',
    'Accept': 'application/json',
    'cookie':'_bl_uid=k4mnb034uqgdaaa4soqUktkvRvth; _ga=GA1.1.143543713.1730527944; PTASession=fdb05ca4-ac24-4fe9-95f9-86b6095b03c5; _ga_ZHCNP8KECW=GS1.1.1731587451.3.1.1731589094.60.0.0; JSESSIONID=51E157FD42B40E22497976DE0B6DDD5C'
}
all_data = []
next_data = []
total_pages = 1
for nowpage in range(total_pages):
    params = {
        'page': nowpage,
        'limit': '50',
    }
    response = requests.get(
        'https://pintia.cn/api/problem-sets/1852233710680576000/rankings',
        headers=headers,
        params=params
    )
    data = response.json()
    next_data= data['commonRankings']['commonRankings']
    all_data.extend(next_data)
    time.sleep(0.1)
print(response.headers['Content-Type'])
with open('第一页.json','w', encoding='utf-8') as f:
    json.dump(all_data,f,ensure_ascii=False)