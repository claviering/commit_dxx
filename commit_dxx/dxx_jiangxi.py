import requests
import json
import secrets
from anti_useragent import UserAgent
# 以下数据需要自行抓取
openid = ''
nid = ''
name = ''
suborg = ''
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'close',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'JSESSIONID=' + secrets.token_urlsafe(40),
    'Host': 'www.jxqingtuan.cn',
    'Origin': 'http://www.jxqingtuan.cn',
    'Referer': 'http://www.jxqingtuan.cn/html/h5_index.html?&accessToken=' + openid,
    'User-Agent': UserAgent(platform="iphone",max_version=5,min_version=1).wechat,
    'X-Requested-With': 'XMLHttpRequest'
}
url = "http://www.jxqingtuan.cn/pub/vol/volClass/current"
course = requests.get(url=url, headers=headers, timeout=30)
course.encoding = course.apparent_encoding
if json.loads(course.text).get('status') == 200:
    title = json.loads(course.text).get('result').get('title')
    coursejson = json.loads(course.text).get("result").get('id')
    resp_url = 'http://www.jxqingtuan.cn/pub/vol/volClass/join?accessToken='
    data = {"course": coursejson, "nid": nid, "cardNo": name, "subOrg": suborg}
    res = requests.post(url=resp_url, headers=headers, data=json.dumps(data), timeout=30)
    res.encoding = res.apparent_encoding
    resp = json.loads(res.text)
    if resp.get("status") == 200:
        print(f'青年大学习{title}-提交成功！')
    else:
        print(f'青年大学习{title}-提交失败！')
