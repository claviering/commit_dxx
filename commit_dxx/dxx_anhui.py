import requests
# 以下信息需要自行抓取
token=""
username=""
gender= ""
mobile= ""
level1= ""
level2= ""
level3= ""
level4= ""
level5= ""

headers = {
    "Host": "dxx.ahyouth.org.cn",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3234 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.15.2020(0x28000F30) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "http://dxx.ahyouth.org.cn/",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    'Content-Type': 'application/x-www-form-urlencoded',
    "X-Requested-With": 'com.tencent.mm',
    "Origin": 'http://dxx.ahyouth.org.cn',
    "token": token
}
data = {
    'username':username,
    'gender': gender,
    'mobile': mobile,
    'level1': level1,
    'level2': level2,
    'level3': level3,
    'level4': level4,
    'level5': level5
}
url = 'http://dxx.ahyouth.org.cn/api/saveUserInfo'  # 获取个人信息
commit_url='http://dxx.ahyouth.org.cn/api/newLearn' #post请求
response = requests.post(url=commit_url, headers=headers, params=data)
response.encoding = response.apparent_encoding
print(response.json())
