import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
sendMenu=2
sendAgain=1

def gmail():
    from_addr = input('请输入登录邮箱：')
    password = input('请输入邮箱登录密码：')

    # 收信方邮箱
    to_addrs = []
    while True:
        a = input('请输入收件人邮箱：')
        to_addrs.append(a)
        b = input('是否继续输入，n退出，任意键继续：')
        if b == 'n':
            break

    # 发信服务器
    smtp_server = 'smtp.gmail.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    text = input('请输入发送内容：')
    msg = MIMEText(text,'plain','utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr) # 这些内容可以修改
    msg['To'] = Header(",".join(to_addrs)) # 这些内容可以修改
    msg['Subject'] = Header(input('请输入发送主题：')) # 这些内容可以修改
    msg['Bcc'] = Header(",". join(to_addrs)) #如果需要发送大量的邮件

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addrs, msg.as_string())
    # 关闭服务器
    server.quit()

def qq():
    from_addr = input('请输入登录邮箱：')
    password = input('请输入邮箱登录密码：')

    # 收信方邮箱
    to_addrs = []
    while True:
        a = input('请输入收件人邮箱：')
        to_addrs.append(a)
        b = input('是否继续输入，n退出，任意键继续：')
        if b == 'n':
            break

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    text = input('请输入发送内容：')
    msg = MIMEText(text,'plain','utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr) # 这些内容可以修改
    msg['To'] = Header(",".join(to_addrs)) # 这些内容可以修改
    msg['Subject'] = Header(input('请输入发送主题：')) # 这些内容可以修改
    msg['Bcc'] = Header(",". join(to_addrs)) #如果需要发送大量的邮件

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addrs, msg.as_string())
    # 关闭服务器
    server.quit()

def displayMenu():
   while sendMenu == 2:
        print('''
                 -.                 `|.     
                 |:\-,              .| \.
                 |: `.------------------------------------.
                 / /   o o o o o o o o o o o o o.-.o o   (_`. 
                /_ \_              .     .=     |'|         `)  
                     ``"""""""""""//    /  """"" `"""------"'   
                                <//   /_(+   
                                //  /      
                               // /      
    +--------------------------------------------+
    |Welcome to Python sendmail program          |
    |Press 1 for Gmail                           |
    |Press 2 for QQ                              |
    |Press 3 to exit                             |      
    +--------------------------------------------+
    ''')
        print('Choose a services provider:')
        sendMail = input()
        sendMail = int(sendMail)
        time.sleep (2)
        if sendMail == 1:
            print('Your program is loading...')
            time.sleep(2)
            gmail()
        if sendMail == 2:
            print('Your program is loading...')
            time.sleep(2)
            qq()
        if sendMail == 3:
            exit
            break
        while sendMail != 1 and sendMail != 2 and playAgain !=5:
            print('I don\'t understand what you are typing, please type again')
            print('Type 1 for Gmail, Type 2 for QQ, Type 3 to exit')
            sendAgain = input()
            sendAgain = int(sendAgain)
            break
            break
displayMenu ()