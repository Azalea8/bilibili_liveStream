import time

from mine.email_mine import email
from mine.requests_mine import send, isStart

with open('txt/book.txt', 'r', encoding='utf-8') as file:
    content = file.read()
file.close()

content = content.replace('\t', '')  # 去除制表符
content = content.replace('\n', '')
content = content.replace(' ', '')

chunks = [content[i:i + 20] for i in range(0, len(content), 20)]

flag = -1
count = 0
flag_api = 0

for chunk in chunks:
    if flag == -1:
        while 1:
            flag = isStart()
            if flag == 1:
                email(text='检测到炫神开播，说书人脚本启动', subject='说书人脚本')
                # qqbot_send('检测到炫神开播，说书人脚本启动')
                break
            else:
                print('炫神未开播')
                time.sleep(600)

    flag_api = send(chunk)

    if flag_api == 0:
        flag = -1
        break
    elif flag_api == 2:
        # 暂停一天
        flag = -1
        time.sleep(3600 * 24)

    count += 1
    if count % 100 == 0:
        flag = isStart()
        if flag == 0:
            email(text=f'检测到炫神下播，说书人脚本终止，共发送弹幕{count}条', subject='说书人脚本')
            # qqbot_send(f'检测到炫神下播，说书人脚本终止，共发送弹幕{count}条')
            count = 0
            flag = -1
        else:
            print(f'{count}条弹幕在播检测通过，脚本继续')

    time.sleep(5)

email(text=f'说书人脚本真正结束', subject='说书人脚本')
# qqbot_send(f'说书人脚本真正结束')

