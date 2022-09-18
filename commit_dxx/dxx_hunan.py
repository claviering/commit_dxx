import requests
import time

# 以下数据需要自行抓取
cookie = ""

dxx_url = f"http://dxx.hngqt.org.cn/project/list?time={int(time.time())}"
dxx_headers = {
    "Host": "dxx.hngqt.org.cn",
    "Connection": "keep-alive",
    "Content-Length": "13",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://dxx.hngqt.org.cn",
    "Referer": "http://dxx.hngqt.org.cn/project/index",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
params = {
    "page": "1",
    "pageSize": "10"
}
response = requests.post(url=dxx_url, headers=dxx_headers, timeout=20, json=params)
response.encoding = response.apparent_encoding
project_id = response.json()['data']['list'][5]['project_id']
print(project_id)
dxx_name = response.json()['data']['list'][5]['name']
print(dxx_name)
time.sleep(5)
commit_url = f"http://dxx.hngqt.org.cn/study/studyAdd?time={int(time.time())}"
# 历史提交
# commit_url = f"http://dxx.hngqt.org.cn/historystudy/studyHistoryAdd?time={int(time.time())}"
params = {
    "projectid": project_id
}
# 历史提交
# params = {
#     "projectId": project_id
# }
response = requests.post(url=commit_url, headers=dxx_headers, timeout=20, json=params)
response.encoding = response.apparent_encoding
print(response.json())
if response.json()['success']:
    print(f"{dxx_name}提交成功！")
else:
    print(f"{dxx_name}提交失败！")
