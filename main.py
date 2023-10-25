import time

from mine.email_mine import email
from mine.requests_mine import send, isStart

while 1:
    flag = isStart()
    if flag == 1:
        email(text='检测到炫神开播了，说书人脚本启动', subject='说书人脚本')
        break
    else:
        print('炫神未开播')
        time.sleep(600)

with open('txt/book.txt', 'r', encoding='utf-8') as file:
    content = file.read()

content = content.replace('\t', '')  # 去除制表符
content = content.replace('\n', '')
content = content.replace(' ', '')

chunks = [content[i:i + 20] for i in range(0, len(content), 20)]

count = 1
for chunk in chunks:
    send(chunk)
    # print(str(count) + '  ||  ' + chunk)
    count += 1
    if count % 100 == 0:
        flag = isStart()
        if flag == 0:
            email(text='检测到炫神下播，说书人脚本终止', subject='说书人脚本')
            break
        else:
            print('100条弹幕在播检测通过，脚本继续')
    time.sleep(5)
