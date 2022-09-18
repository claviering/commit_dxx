import requests


def get_version(openid, cookie):
    version_url = f'http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=getNewestVersionInfo&openid={openid}'
    headers = {
        "Host": "qndxx.youth54.cn",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3234 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.15.2020(0x28000F30) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://qndxx.youth54.cn",
        "Referer": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=pageSdtwdt",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }
    version_response = requests.post(url=version_url, headers=headers)
    version_response.encoding = version_response.apparent_encoding
    content = version_response.json()
    print(content)
    if content['errcode'] == '0':
        beforeversion = content['beforeversion']
        versionname = content['versionname']
        version = content['version']
        data = {
            'beforeversion': beforeversion,
            'versionname': versionname,
            'version': version,
            'status': 200
        }
    else:
        data = {
            'beforeversion': '',
            'versionname': '',
            'version': '',
            'status': 404
        }
    # print(data)
    return data


def commit_dxx(openid, cookie, version):
    commit_url = 'http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=studyLatest'
    headers = {
        "Host": "qndxx.youth54.cn",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3234 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/6170 MicroMessenger/8.0.15.2020(0x28000F30) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://qndxx.youth54.cn",
        "Referer": "http://qndxx.youth54.cn/SmartLA/dxx.w?method=pageSdtwdt",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }
    data = {
        'openid': openid,
        'version': version

    }
    response = requests.post(url=commit_url, headers=headers, params=data)
    response.encoding = response.apparent_encoding
    content = response.json()
    print(content)
    return content['errcode']


if __name__ == '__main__':

    # 以下两个需要自行抓包
    openid = ''
    cookie = ''
    
    content = get_version(openid, cookie)
    if content['status'] == 200:
        version = content['version']
        status = commit_dxx(openid, cookie, version)
        if status == '0':
            print(f"{content['versionname']}-提交成功！")
        else:
            print(f"{content['versionname']}-提交失败！")
    else:
        print('大学习提交失败！')
