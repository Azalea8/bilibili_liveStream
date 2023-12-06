import requests
import json

from mine.email_mine import email

with open('txt/cookie.txt', 'r', encoding='utf-8') as file:
    tmp = file.read()

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
    global response
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
        'csrf': '44fa6c87946e48d376c290656c92d788',
        'csrf_token': '44fa6c87946e48d376c290656c92d788',
    }

    headers = {
        'cookie': tmp,
        # 'origin': 'https://live.bilibili.com',
        # 'referer': 'https://live.bilibili.com/84074?live_from=84002&spm_id_from=333.337.0.0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
    }

    data['msg'] = msg

    response = requests.post(url=url, data=data, headers=headers)
    message = json.loads(response.text)
    print(message)
    print('\n')
    if message['code'] < 0:
        email(text='说书人脚本异常终止: \n' + str(message), subject='说书人脚本')
        qqbot_send(msg='说书人脚本异常终止: \n' + str(message))
        return 0
    else:
        return 1

