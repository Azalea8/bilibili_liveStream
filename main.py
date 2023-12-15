import time

from mine.email_mine import email
from mine.requests_mine import send, isStart, qqbot_send

with open('txt/book.txt', 'r', encoding='utf-8') as file:
    content = file.read()
file.close()

content = content.replace('\t', '')  # 去除制表符
content = content.replace('\n', '')
content = content.replace(' ', '')

chunks = [content[i:i + 20] for i in range(0, len(content), 20)]

while 1:
    while 1:
        flag = isStart()
        if flag == 1:
            email(text='检测到炫神开播，说书人脚本启动', subject='说书人脚本')
            qqbot_send('检测到炫神开播，说书人脚本启动')
            break
        else:
            print('炫神未开播')
            time.sleep(600)

    count = 0
    flag_api = 0
    for chunk in chunks:
        flag_api = send(chunk)
        # print(str(count) + '  ||  ' + chunk)
        count += 1
        if count % 100 == 0:
            flag = isStart()
            if flag == 0:
                email(text=f'检测到炫神下播，说书人脚本终止，共发送弹幕{count}条', subject='说书人脚本')
                qqbot_send(f'检测到炫神下播，说书人脚本终止，共发送弹幕{count}条')
                break
            else:
                print(f'{count}条弹幕在播检测通过，脚本继续')
        if flag_api == 0:
            email(text=f'说书人异常脚本终止，共发送弹幕{count}条', subject='说书人脚本')
            qqbot_send(f'说书人异常脚本终止，共发送弹幕{count}条')
            break
        time.sleep(5)

    if flag_api == 0:
        break

