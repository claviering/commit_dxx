import requests

get_token_headers = {
    "Host": "qzymb.gzyouth.cn",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "auth": "true",
    "content-type": "application/json",
    "Accept": "*/*",
    "Origin": "http://qzymb.gzyouth.cn",
    "X-Requested-With": "com.tencent.mm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
# 以下参数需要自行抓取，抓包时此链接请求部分就是：http://qzymb.gzyouth.cn/youth/api/learnerController/register
params = {
    "openId": "",
    "nickname": "",
    "photo": "",
    "universityId": "",
    "universityCode": "",
    "collegeId": "",
    "collegeCode": "",
    "deptStr": "",
    "name": "",
    "areaIndex": "",
    "type": "",
    "editType": ""
}
get_token_url = "http://qzymb.gzyouth.cn/youth/api/learnerController/register"
response = requests.post(url=get_token_url, headers=get_token_headers, json=params)
response.encoding = response.apparent_encoding
token = response.json()['data']['token']
print("Token为：%s" % token)
commit_headers = {
    "Host": "qzymb.gzyouth.cn",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "Authorization": token,
    "content-type": "application/json",
    "Accept": "*/*",
    "Origin": "http://qzymb.gzyouth.cn",
    "X-Requested-With": "com.tencent.mm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
commit_url = "http://qzymb.gzyouth.cn/youth/api/term/getReadedTermIds"
response = requests.post(url=commit_url, headers=commit_headers)
response.encoding = response.apparent_encoding
if response.json()['code'] == 10001:
    print("提交成功！")
else:
    print("提交失败！")
