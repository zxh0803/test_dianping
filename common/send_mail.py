# coding:utf-8
import os
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
'''发送邮件'''
cf_path = os.path.join("D:\\PycharmProjects\\autotest\\config","mail.ini")
cf = configparser.ConfigParser()
cf.read(cf_path)        #此处打开读取配置文件，并且进行解析
f_user = str(cf["sendmail"]["f_user"])
t_user = str(cf["sendmail"]["t_user"])
pwd = str(cf["sendmail"]["pwd"])
port = int(cf["sendmail"]["port"])
smtpserver = str(cf["sendmail"]["smtpserver"])

result_path = os.path.join(r"D:\PycharmProjects\autotest\report",r"result.html")

def sendmail():

    with open(result_path,'rb') as f:result_data = f.read()
    msg = MIMEMultipart()
    body = result_data
    att = MIMEText(body,'html','utf-8')
    msg.attach(att)
    msg['from'] = f_user
    msg['to'] = t_user
    msg['subject'] = '自动化测试报告'

    att2 = MIMEText(result_data,'base64','utf-8')
    att2["Content-Type"] = "application/octet-stream"
    att2["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(att2)

    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(f_user,pwd)
    smtp.sendmail(f_user,t_user,msg.as_string())
    smtp.quit()
if __name__ == '__main__':
    sendmail()