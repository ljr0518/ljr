from http.client import responses
from idlelib.rpc import response_queue
from pydoc import resolve
import json
import requests
import random
from fake_useragent import UserAgent
from urllib.parse import quote,unquote
import gzip
# #找到目标url
# url='https://baidu.com'
# #构建请求头:
# headers={
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
# }
# #带上user-argent发送请求
# #headers接收字典形式的请求头，请求头字段名为key，值为value
# result=requests.get(url,headers=headers)
# #打印响应
# print(result.content.decode())
#
#
#确定目标url
# url='https://ts1.cn.mm.bing.net/th/id/R-C.987f582c510be58755c4933cda68d525?rik=C0D21hJDYvXosw&riu=http%3a%2f%2fimg.pconline.com.cn%2fimages%2fupload%2fupc%2ftx%2fwallpaper%2f1305%2f16%2fc4%2f20990657_1368686545122.jpg&ehk=netN2qzcCVS4ALUQfDOwxAwFcy41oxC%2b0xTFvOYy5ds%3d&risl=&pid=ImgRaw&r=0'
# #发送请求获取响应
# res=requests.get(url)
# print(res.content)
# #保存响应
# with open('1.jpg','wb') as f:
#     f.write(res.content)


#
# UAlist=[
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
#     'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',
#     'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0'
# ]
# print(random.choice(UAlist))
# print(UserAgent().random)
# print(unquote('%E5%8F%82%E6%95%B0'))

# 随机生成User-Agent并爬取图片
# import random
# UAlist=[
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
#     'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',
#     'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0'
# ]
# url='https://p1.music.126.net/pjYYS77ujdAfyYJ_-lQEUg==/109951170139599702.jpg?imageView&quality=89'
# rando=random.choice(UAlist)
# headers={
#     'User-Agent':rando
# }
# page=requests.get(url,headers=headers)
# with open('1.jpg','wb') as f:
#     f.write(page.content)




# 获取网易云单首歌的资源
# url='https://m10.music.126.net/20241111162426/7a25ceff249802df5ee31c7bf7be30d6/yyaac/obj/wonDkMOGw6XDiTHCmMOi/14050790823/7cbc/c66b/8e32/82f5bdc750f1a611bde1f19f25eb415d.m4a'
# res=requests.get(url)
# print(res.content)
# with open('wyy.mp3','wb') as f:
#     f.write(res.content)

# 获取网易云单个mv
# url='https://vodkgeyttp8.vod.126.net/cloudmusic/MTI5MDc0OTc=/ab5352f3c383ddaf8cdeea09a07a359c/4e132af660ad3df55ce361e7b3d8bac1.mp4?wsSecret=59c54fad23750abb22396b184bfbfbe6&wsTime=1731312961'
# res=requests.get(url)
# with open('wyy.mp4','wb') as f:
#     f.write(res.content)


#百度贴吧单页获取案例
# url='https://tieba.baidu.com/f?ie=utf-8&kw=%E6%A3%AE%E6%9E%97&fr=search'
# headers={
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
# }
# res=requests.get(url,headers=headers)
# with open('baidutb.html','wb') as f:
#     f.write(res.content)


#百度贴吧翻页获取案例
# https://tieba.baidu.com/f?kw=%E6%A3%AE%E6%9E%97&ie=utf-8&pn=0
# https://tieba.baidu.com/f?kw=%E6%A3%AE%E6%9E%97&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=%E6%A3%AE%E6%9E%97&ie=utf-8&pn=100
# headers={
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
# }
# word=input("请输入贴吧名:")
# page=int(input("请输入要保存的页数:"))
# for i in range(page):
#     params={
#         'kw':word,
#         'pn':i*50
#     }
#     url='https://tieba.baidu.com/f?'
#     response=requests.get(url,headers=headers,params=params)
#     with open(f'{word}_{i+1}.html','wb') as f:
#         f.write(response.content)



#面向对象改写翻页
# 重新学习



# post请求
# post请求(更安全):登录注册,传输大文本内容
# requests.post(url,data)
# data参数接收一个字典

# get跟post区别
# get请求直接向服务器发送请求,获取响应内容
# post请求是先给服务器一些数据,然后在获取一些响应

# get请求携带参数   --parmas
# post请求携带参数  --data


# cookie   模拟登陆
# 找到登录后的url
# url='https://www.bilibili.com/'
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
#     'Cookie':'buvid3=D19184B4-488A-9961-1D09-04D6DA12CB1C68953infoc; b_nut=1711887468; i-wanna-go-back=-1; b_ut=7; _uuid=892EF141-DDC3-10DFA-E2FD-103BE5EBDF8C269832infoc; buvid4=8F5D153F-670F-62E9-9D23-7F8E4484F1F471211-024033112-%2BeJjaSI%2B6RQW19SA%2BBQULMOMuJM0xU21A0IW47RT%2Fc7ph95EoBcJnbUEI5101sKH; enable_web_push=DISABLE; rpdid=0zbfAGGO9x|FVdBrLS|3337|3w1RQUde; header_theme_version=CLOSE; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; CURRENT_BLACKGAP=0; is-2022-channel=1; CURRENT_FNVAL=4048; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3117268386453663; hit-dyn-v2=1; fingerprint=d32047c03fd63cd111c857ff8674aba5; buvid_fp=d32047c03fd63cd111c857ff8674aba5; CURRENT_QUALITY=0; PVID=1; bp_t_offset_3546787300248371=998086932858667008; SESSDATA=2f02d301%2C1746777353%2Cd70f3%2Ab2CjCCQpQzuRweCql8N5PADk-WNcDz9sI5HGhEpMV6_DG44OohzHGdr1YFIjj3nyebvPwSVlpLSU1BbnN6OFRDeW9weFpyUVBWN081MDBMUmF4QnZiNDF3ZmxKTzg2TXFxN3VlNGIzSEFFUTZyTHJFZFNMS1c5YnNoMXpEMVZSUDJiUVkzUE9rSVVBIIEC; bili_jct=6b4019537bf654ec925801e8499def0c; DedeUserID=3494364439382756; DedeUserID__ckMd5=a2a165dbc8c3014c; b_lsid=C106111EE_1931B423548; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzE1ODgzNDQsImlhdCI6MTczMTMyOTA4NCwicGx0IjotMX0.5ffvhPKOfYO7-QPx-4Bby3flPv91NiXvhdFTP_OMPu0; bili_ticket_expires=1731588284; bp_t_offset_3494364439382756=998540245181923328; sid=8sbamgg9; home_feed_column=4; browser_resolution=1090-1452'
#
# }
# requests.get(url,headers=headers)




# post请求举例--金山翻译
# url='https://ifanyi.iciba.com/index.php?c=trans'
#
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
# }
# # 构建data参数字典
# word=input("请输入你要翻译的内容：")
# post_data={
#     'from':'zh',
#     'to':'en',
#     'q':word
# }
# res=requests.post(url,headers=headers,data=post_data)
# print(res.text)
# # 将json数据转换为Python字典
# dic=json.loads(res.text)
# print(dic["out"])




# session---自动处理cookie
# requests模块中的Session类能够自动处理发送请求获取响应过程中产生的cookie，进而达到状态保持的目的
# 自动处理cookie，即下一次请求会带上前一次的cookie
# requests.session()  实例化session对象
# 1.对访问登录后才能访问的页面进行抓包
# 2.确定登录请求的url地址，请求方法和所需的参数
# 3.确定登录后才访问的页面url和请求方法
# 4.利用requests.session完成代码

# cookie池的介绍
# user-agent池：短时间内多次发送请求，尽量每一次的请求都用不同的用户代理
# cookie池：每一个cookie就代表一个账号
# cookie有有效期，session不用担心有效期问题

# cookie与session区别：
# 1.cookie数据放在客户的浏览器上。session数据放置在服务器上
# 2.cookie不是很安全，别人可以分析放在本地的cookie并进行cookie欺骗，考虑安全问题应当使用session
# 3.session会在一定时间内保存在服务器上，考虑到减轻服务器性能方面，应当使用cookie
# 4.考虑将登录信息等重要信息存放在session，其他信息如果需要保留，可以放在cookie中


# 1.代理
# 代理ip是一个ip，指向的是一个代理服务器
# 代理服务器能够帮我们向目标服务器转发请求
#
# ip地址：精确的定位
#
# 2.正向代理和反向代理
# 正向代理：给客户做代理，让服务器不知道客户端的真实身份
# 保护自己的ip地址不会被封，要封也是代理ip
# 反向代理：给服务器做代理，让浏览器不知道服务器的真实地址
# 正向代理保护客户端，反向代理保护服务器
# 实际上理论来说分为三类：
# 1.透明代理：服务器知道我们使用了代理ip，也知道真实ip
# 2.匿名代理：服务器能够检测到使用了代理ip，但不知道真实ip
# 3.高匿代理：服务器既不能检测到使用代理ip，也不知道真实ip


# 代理ip的使用
#
# proxies的形式：字典
# proxies = {
#     # 以键值对的形式，固定的语法，IP地址：端口号
#     "http":"http://12.34.56.78:1234",
#     "http":"http://12.34.56.78:1234"
# }
# responses=requests.get(url,proxies=proxies)


# 举例
# url="https://www.baidu.com"
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
# }
# # 构建代理字典
# proxies={
# #     第一种写法
#       'http':'12.34.56.78:1234',
# #     第二种写法
#       'http':'http://12.34.56.78:1234'
# }
#
# requests.get(url,headers=headers,proxies=proxies)
#
# # 代理ip无效时，会自动使用本机的真实ip，所以会访问成功
