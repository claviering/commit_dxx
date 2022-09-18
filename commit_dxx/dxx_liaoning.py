import json
import requests
import gzip

# 以下数据需要自行抓取
cookie = ""

get_user_info_url = "http://api.lngqt.shechem.cn/user/user/find"
get_user_info_headers = {
    "Host": "api.lngqt.shechem.cn",
    "Connection": "keep-alive",
    "Content-Length": "6",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://websecond.lngqt.shechem.cn",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://websecond.lngqt.shechem.cn/my",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
params = {
    "token": ""
}
response = requests.post(url=get_user_info_url, headers=get_user_info_headers, json=params)
response = gzip.decompress(response.content).decode("utf-8")
print(response)
token = json.loads(response)['data']['openid']
get_new_study_url = "http://api.lngqt.shechem.cn/webapi/learn/getnowlearn"
get_new_study_headers = {
    "Host": "api.lngqt.shechem.cn",
    "Connection": "keep-alive",
    "Content-Length": "6",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://websecond.lngqt.shechem.cn",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://websecond.lngqt.shechem.cn/study",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
params = {
    "token": token
}
response = requests.post(url=get_new_study_url, headers=get_new_study_headers, json=params)
response = gzip.decompress(response.content).decode("utf-8")
print(response)
lid = json.loads(response)['data']['id']
commit_url = "http://api.lngqt.shechem.cn/webapi/learn/addlearnlog"
params = {
    "lid": lid,
    "token": token
}
response = requests.post(url=commit_url, headers=get_new_study_headers, json=params)
response = gzip.decompress(response.content).decode("utf-8")
print(json.loads(response))
