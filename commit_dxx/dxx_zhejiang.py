import json
import time
import requests
# 以下数据需要自己抓取
openid = ''
nid = ''
name = ''
time_stamp = str(int(time.time()))
headers = {
    "Host": "qczj.h5yunban.com",
    "Connection": "keep-alive",
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; PACM00 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3164 MMWEBSDK/20211001 Mobile Safari/537.36 MMWEBID/556 MicroMessenger/8.0.16.2040(0x28001056) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}
access_token_url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/login/we-chat/callback?callback=https%3A%2F%2Fqczj.h5yunban.com%2Fqczj-youth-learning%2Findex.php&scope=snsapi_userinfo&appid=wx56b888a1409a2920&openid=" + openid + "&nickname=ZhangSan&headimg=&time=" + time_stamp + "&source=common&sign=&t=" + time_stamp
access_token_rsp = requests.get(url=access_token_url, headers=headers, timeout=30)
access_token_rsp.encoding = access_token_rsp.apparent_encoding
access_token = access_token_rsp.text[45:81]
course_url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/common-api/course/current?accessToken=" + access_token
course_rsp = requests.get(url=course_url, headers=headers, timeout=30)
course_rsp.encoding = course_rsp.apparent_encoding
res_json = json.loads(course_rsp.text)
title = res_json['result']['title']
course_id = res_json['result']['id']
data = {
    "course": course_id,
    "subOrg": None,
    "nid": nid,
    "cardNo": name
}
sent_url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/user-api/course/join?accessToken=" + access_token
sent_rsp = requests.post(url=sent_url, headers=headers, data=json.dumps(data), timeout=30)
sent_rsp.encoding = sent_rsp.apparent_encoding
resp = json.loads(sent_rsp.text)
if resp.get("status") == 200:
    print(f'青年大学习{title}-提交成功！')
else:
    print(f'青年大学习{title}-提交失败！')
