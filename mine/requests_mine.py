import requests
import json
import time

from mine.email_mine import email

with open('txt/cookie.txt', 'r', encoding='utf-8') as file:
    cookie = file.read()

with open('txt/csrf.txt', 'r', encoding='utf-8') as file:
    csrf = file.read()

# 直播间房间号，可以用短号，如该直播间短号为 84074
room_id = 14709735


def isStart():
    url = f'https://api.live.bilibili.com/room/v1/Room/get_info?room_id={room_id}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
    }
    response = requests.get(url=url, headers=headers)
    ans = json.loads(response.text)
    # print(ans)
    flag = ans['data']['live_status']
    return flag


def qqbot_send(msg):
    params = {
        'user_id': 2574292235,
        'message': msg,
    }
    requests.get(url='http://127.0.0.1:5700/send_private_msg', params=params)


def send(msg):
    url = 'https://api.live.bilibili.com/msg/send'

    data = {
        "bubble": '0',
        'msg': '',
        'color': '16777215',
        'mode': '1',
        'room_type': '0',
        'jumpfrom': '84002',
        'reply_mid': '0',
        'fontsize': '25',
        'rnd': '1700921525',
        'roomid': '14709735',
        'csrf': csrf,
        'csrf_token': csrf,
    }

    headers = {
        'cookie': cookie,
        # 'origin': 'https://live.bilibili.com',
        # 'referer': 'https://live.bilibili.com/84074?live_from=84002&spm_id_from=333.337.0.0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
    }

    data['msg'] = msg

    temp = 0
    tmp = None

    try:
        response = requests.post(url=url, data=data, headers=headers)
        tmp = response.text
        print(tmp)
        message = json.loads(tmp)
    except:
        temp = 1
        email(text=f'说书人脚本出现一次异常: \n{tmp}', subject='说书人脚本')
        # qqbot_send(msg=f"说书人脚本异常:\n{tmp}")

    if temp == 0:
        if message['code'] < 0:
            email(text='说书人脚本异常终止: \n' + str(message['message']), subject='说书人脚本')
            # qqbot_send(msg='说书人脚本异常终止: \n' + str(message['message']))
            return 0
        elif message['message'] == '你被禁言啦':
            email(text=f"说书人脚本异常: {message['message']}" + ',脚本暂停一天', subject='说书人脚本')
            # qqbot_send(msg=f"说书人脚本异常: {message['message']}" + ',脚本暂停一天')
            return 2
        elif message['message'] == '系统升级中':
            email(text=f"说书人脚本异常: {message['message']}", subject='说书人脚本')
            # qqbot_send(msg=f"说书人脚本异常: {message['message']}")
            return 3
        else:
            return 1
    else:
        return 1

