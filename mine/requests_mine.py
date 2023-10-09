import requests
import json

from mine.email_mine import email

with open('txt/cookie.txt', 'r', encoding='utf-8') as file:
    tmp = file.read()

def isStart():
    flag = 0
    url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/w_live_users?size=10'
    headers = {
        'cookie': tmp,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
    }
    response = requests.get(url=url, headers=headers)
    ans = json.loads(response.text)
    try:
        list = ans['data']['items']
        for b in list:
            if b['uid'] == 299013902:
                flag = 1
    except:
        flag = 0
    return flag

def send(msg):
    global response
    url = 'https://api.live.bilibili.com/msg/send'

    data = {
        "bubble": '0',
        'msg': '',
        'color': '16777215',
        'mode': '1',
        'room_type': '0',
        'jumpfrom': '86002',
        'reply_mid': '0',
        'fontsize': '25',
        'rnd': '1696580396',
        'roomid': '14709735',
        'csrf': '2fa14b2152cc47312d90966f7c90b34f',
        'csrf_token': '2fa14b2152cc47312d90966f7c90b34f',
    }

    headers = {
        'cookie': tmp,
        'origin': 'https://live.bilibili.com',
        'referer': 'https://live.bilibili.com/84074?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.to_liveroom.0.click&live_from=86002',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
    }

    data['msg'] = msg

    try:
        response = requests.post(url=url, data=data, headers=headers)
    except:
        email(text='说书人脚本异常 || 状态码：' + str(response.status_code), subject='说书人脚本')

