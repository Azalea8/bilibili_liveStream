# bilibili_liveStream
B站直播间说书人脚本，脚本挂载后可实现开播，脚本自动执行并发送邮件通知，下播后自动终止发送邮件通知

房间号在 mine/request_mine.py 设置，可以为短号也可以为长号

敏感信息通过 txt 文件夹读取，book.txt 是想要说的书，cookie.txt 是 B站用户信息，password.txt 是邮箱 smtp服务的密码。

send 函数里的 data字典，需要在直播间手动发送一条弹幕，F12检查

<img alt="img.png" height="300" src="img/img.png" />

cookie是在Headers里最长的那个，注意：cookie保存了个人信息，不要随便泄露

<img alt="img_1.png" height="200" src="img/img_1.png" />