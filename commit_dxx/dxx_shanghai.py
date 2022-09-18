import requests
# 以下数据需要自行抓取
accessToken = ""
nid = ""
name = ""
cookie = ""

headers = {
    "Host": "qcsh.h5yunban.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/json;charset=UTF-8",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://qcsh.h5yunban.com/youth-learning/signUp.php?rv=2020",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": cookie
}
url = f"https://qcsh.h5yunban.com/youth-learning/cgi-bin/common-api/course/current?accessToken={accessToken}"
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
course = response.json()['result']['id']
print(course)
commit_url = f"https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/course/join?accessToken={accessToken}"
params = {
    "course": course,
    "nid": nid,
    "cardNo": name
}
response = requests.post(url=commit_url, headers=headers, json=params)
response.encoding = response.apparent_encoding
print(response.json())
