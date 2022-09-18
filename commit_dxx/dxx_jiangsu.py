import requests
import re
# 以下参数需自行抓取
cookie=""

info_headers = {
    "Host": "service.jiangsugqt.org",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": '1',
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "X-Requested-With": "com.tencent.mm",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
infor_url = "https://service.jiangsugqt.org/youth/lesson/confirm"
response = requests.get(url=infor_url, headers=info_headers)
response.encoding = response.apparent_encoding
token = re.findall(r'var token = "(.*?)";', response.text)[0]
lesson_id = re.findall(r"'lesson_id':(.*)", response.text)[0]
commit_url = "https://service.jiangsugqt.org/youth/lesson/confirm"
params = {
    "_token": token,
    "lesson_id": lesson_id
}
response = requests.post(url=commit_url, headers=info_headers, json=params)
response.encoding = response.apparent_encoding
print(response.text)
