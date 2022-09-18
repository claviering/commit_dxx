import requests

# 以下信息需要自己手动抓取
cookie = ""

# 以下获取最新一期大学习id
get_new_study_headers = {
    "Host": "hnqndaxuexi.dahejs.cn",
    "Connection": "keep-alive",
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/json",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://hnqndaxuexi.dahejs.cn/study/studyList",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
get_new_study_url = "http://hnqndaxuexi.dahejs.cn/stw/news/list?&pageNumber=1&pageSize=10"
response = requests.get(url=get_new_study_url, headers=get_new_study_headers)
response.encoding = response.apparent_encoding
dxx_list = response.json()['obj']['news']['list'][0]
newsid = dxx_list['id']
print(newsid)
dxx_name = dxx_list['title']
# 以下链接获取用户详细信息
get_user_headers = {
    "Host": "hnqndaxuexi.dahejs.cn",
    "Connection": "keep-alive",
    "Content-Length": "2",
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/json",
    "Origin": "http://hnqndaxuexi.dahejs.cn",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://hnqndaxuexi.dahejs.cn/study/personalSet",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
params = {
}
get_user_info_url = "http://hnqndaxuexi.dahejs.cn/stw/front-user/info"
response = requests.post(url=get_user_info_url, headers=get_user_headers, json=params)
response.encoding = response.apparent_encoding
token = response.json()['obj']['openId']
# 以下获取最新一期大学习详细信息
news_info_headers = {
    "Host": "hnqndaxuexi.dahejs.cn",
    "Connection": "keep-alive",
    "Content-Length": "26",
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/json",
    "Origin": "http://hnqndaxuexi.dahejs.cn",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://hnqndaxuexi.dahejs.cn/study/gohome",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
params = {
    "newsld": newsid
}
news_info_url = "http://hnqndaxuexi.dahejs.cn/stw/news/info"  # 带参数newsid
response = requests.post(url=news_info_url, headers=news_info_headers, json=params)
response.encoding = response.apparent_encoding
print(response.text)
commit_url = f"http://hnqndaxuexi.dahejs.cn/stw/news/study/{newsid}"
commit_headers = {
    "Host": "hnqndaxuexi.dahejs.cn",
    "Connection": "keep-alive",
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "token": token,
    "Content-Type": "application/json",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://hnqndaxuexi.dahejs.cn/study/studyList",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
response = requests.post(url=commit_url, headers=commit_headers)
response.encoding = response.apparent_encoding
print(response.json())
