import smtplib
from email.mime.text import MIMEText

with open('txt/password.txt', 'r', encoding='utf-8') as file:
    password = file.read()


def email(text, subject, receivers=None, ):
    if receivers is None:
        receivers = ['liangwhm@s.upc.edu.cn']

    mail_host = 'smtp.qq.com'
    mail_user = '2574292235'
    mail_pass = password
    sender = '2574292235@qq.com'

    message = MIMEText(text, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = subject
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    try:
        # 部署到阿里云服务器上时发现程序发送smtp邮件必须通过SSL协议端口发送
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # 连接到服务器
        smtpObj.connect(mail_host, 465)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print(text + '  ||  邮件通知发送成功')
    except smtplib.SMTPException as e:
        print('error', e)


if __name__ == '__main__':
    email(text='说书人脚本被禁言: ' + '脚本暂停一天', subject='说书人脚本')
