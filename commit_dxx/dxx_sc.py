import requests

headers = {
    "Referer": 'http://scyol.com/v_prod6.02/',
    "Host": "dxx.scyol.com",
    "Connection": "keep-alive",
    "Content_Length": '9',
    "Content_Type": "application/json",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3224 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.15.2020(0x28000F30) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Origin": "http://scyol.com",
    "X-Requested-With": "com.tencent.mm",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "token": '',  # 此处的token需自己手动抓取
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}
commit_url = 'https://dxx.scyol.com/api/student/commit'
# 以下数据需自己抓包获取：此链接https://dxx.scyol.com/api/stages/currentInfo会返回相应数据
data_json = {
    "name": "",  # 此处填姓名
    "tel": "",  # 此处填手机号
    "org": "",  # #学校所属上级pid#学校pid#学院pid#班级（团支部）pid#
    "lastOrg": "",
    "orgName": "",  # 班级名称
    "allOrgName": ""  # #学校所属上级名称#学校名称#学院名称+团委#班级（团支部）名称#
}
response = requests.post(commit_url, headers=headers, json=data_json)
response.encoding = response.apparent_encoding
print(response.json())
