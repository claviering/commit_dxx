import requests
import time
# 以下数据需要自行抓取
openid = ""

new_headers = {
    "Host": "stu.redrock.team",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.20.2100(0x28001438) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "X-Requested-With": "com.tencent.mm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
new_url = f"http://stu.redrock.team/new_course.json?time={int(time.time())}"
new_response = requests.get(url=new_url, headers=new_headers)
new_response.encoding = new_response.apparent_encoding
print(new_response.json())
course_id = new_response.json()['data'][0]['id']
commit_url = f"http://stu.redrock.team/api/course/studyCourse?openid={openid}&id={course_id}"
response = requests.get(url=commit_url, headers=new_headers)
response.encoding = response.apparent_encoding
print(response.json())
if response.json()['status'] == 200:
    print("提交成功！")
elif response.json()['status'] == 201:
    print("重复提交")
else:
    print("提交失败")
